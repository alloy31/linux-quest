import argparse
import fcntl
import os
import random
import sys
import time
from pathlib import Path

from . import __version__
from .campaign import CHAPTERS, MISSIONS, MISSION_BY_ID
from .exam import score_exam, select_exam, shuffle_choices
from .lessons import BASELINE, OFFICIAL_COVERAGE, TOPICS
from .model import DIFFICULTIES
from .progress import Progress, SaveError, default_path
from .questions import QUESTIONS
from .runtime import DockerLab, LabError, docker, ensure_image
from .ui import UI
from .tutorials import MISSION_QUESTIONS, TUTORIALS


def content_errors():
    errors = []
    ids = [m.id for m in MISSIONS]
    qids = [q.id for q in QUESTIONS]
    if len(ids) != len(set(ids)) or len(qids) != len(set(qids)):
        errors.append("중복 ID")
    covered = {t for m in MISSIONS for t in m.topics}
    assessed = {q.topic for q in QUESTIONS}
    for row, topics in OFFICIAL_COVERAGE.items():
        for topic in topics:
            if topic not in TOPICS or topic not in covered or topic not in assessed:
                errors.append(f"학습·평가 누락: {row}/{topic}")
    for m in MISSIONS:
        if any(qid not in qids for qid in MISSION_QUESTIONS.get(m.id, ())):
            errors.append(f"확인 문항 연결 오류: {m.id}")
        if len(m.hints) != 3 or not m.topics or m.chapter not in CHAPTERS:
            errors.append(f"미션 메타데이터 오류: {m.id}")
        if any(p not in ids[:ids.index(m.id)] for p in m.prerequisites):
            errors.append(f"선수 개념 순서 오류: {m.id}")
        if m.kind != "scenario" and not m.goals:
            errors.append(f"완료 조건 없음: {m.id}")
    for q in QUESTIONS:
        if len(set(q.choices)) != 4 or q.topic not in TOPICS or q.answer not in range(4):
            errors.append(f"문항 오류: {q.id}")
    if len({q.stem for q in QUESTIONS}) != len(QUESTIONS):
        errors.append("중복 문항")
    for stage in (1, 2):
        try:
            select_exam(stage, random.Random(0))
        except ValueError as exc:
            errors.append(f"시험 문항 수 부족: {stage}/{exc}")
    return errors


class Game:
    def __init__(self, ui, progress):
        self.ui = ui
        self.progress = progress
        self.image_ready = False

    def difficulty(self):
        return self.ui.menu("난이도를 선택하세요", [(key, value + " — " + info) for key, value, info in (
            ("beginner", "초급", "개념·명령어와 함께"),
            ("intermediate", "중급", "목표부터, 필요하면 힌트"),
            ("advanced", "고급", "여러 조건을 조합하는 사건"))])

    def main(self):
        while True:
            resumable = self.progress.data["current"] or self.progress.data["cursor"]
            choice = self.ui.menu("기록 보관소에 오신 것을 환영합니다", [
                ("start", "시작하기"), ("resume", "이어하기"), ("learn", "학습 메뉴"),
                ("exit", "종료")], disabled=() if resumable else ("resume",), banner=True)
            if choice == "exit":
                self.ui.print("진도는 저장되어 있습니다. 다음 점검 때 만나요.")
                return
            if choice == "start":
                difficulty = self.difficulty()
                self.ui.print("\n[첫 출근]\n당신은 기록 보관소의 신입 서버 관리자입니다.\n"
                    "매일 02:00, 백업은 실패하고 인수인계 자료는 사라집니다.\n"
                    "선임의 마지막 메시지부터 찾아봅시다.\n")
                self.ui.ask("Enter: 시작 · s: 도입 건너뛰기 ")
                self.campaign(0, difficulty)
            elif choice == "resume":
                current = self.progress.data["current"]
                mid = current["id"] if current else self.progress.data["cursor"]
                if mid not in MISSION_BY_ID:
                    self.ui.print("이 버전에 없는 미션입니다. 챕터 선택에서 새로 시작하세요.")
                    self.ui.pause()
                else:
                    self.ui.print("미완료 미션은 초기 환경에서 재개합니다. 완료·힌트·오답 기록은 유지됩니다.")
                    self.campaign(next(i for i, m in enumerate(MISSIONS) if m.id == mid),
                                  current["difficulty"] if current else self.progress.data["difficulty"],
                                  resume=current)
            else:
                self.learn_menu()

    def learn_menu(self):
        while True:
            choice = self.ui.menu("학습 메뉴", [("chapter", "챕터 선택"), ("review", "복습"),
                ("exam", "모의시험"), ("status", "학습 현황"), ("journal", "사건 기록"), ("back", "돌아가기")])
            if choice == "back":
                return
            if choice == "chapter":
                chapter = self.ui.menu("챕터 선택 · 선수 개념은 권장 사항입니다", [
                    (number, f"{title} ({self.chapter_count(number)}/4)")
                    for number, (title, _, _) in CHAPTERS.items()] + [(0, "돌아가기")])
                if chapter:
                    self.campaign(next(i for i, m in enumerate(MISSIONS) if m.chapter == chapter), self.difficulty())
            elif choice == "review":
                self.review()
            elif choice == "exam":
                stage = self.ui.menu("모의시험 · 자체 제작 문제", [(1, "1차 · 50문항 · 60분"),
                    (2, "2차 · 80문항 · 100분"), (0, "돌아가기")])
                if stage:
                    self.exam(stage)
            elif choice == "status":
                self.status()
            elif choice == "journal":
                self.journal()

    def chapter_count(self, number):
        return sum(self.progress.data["missions"].get(m.id, {}).get("completed", False)
                   for m in MISSIONS if m.chapter == number)

    def show_lessons(self, mission):
        self.ui.print(f"\n[학습 브리핑 · {BASELINE}]")
        for topic in mission.topics:
            info = TOPICS[topic]
            self.ui.print(f"\n{info.title}\n{info.lesson}")

    def show_mission(self, mission, difficulty, variant):
        self.ui.print(f"\n{'=' * 48}\n챕터 {mission.chapter} · {DIFFICULTIES[difficulty]} · "
                      + ("종합 사건" if mission.boss else "미션"))
        self.ui.print(f"[{mission.title}]\n{mission.story}\n")
        self.ui.print("목표\n" + mission.objective.replace("{v}", variant))
        if mission.kind != "scenario":
            for condition in mission.conditions(difficulty, variant):
                self.ui.print("  [ ] " + condition["label"])
        if mission.prerequisites:
            self.ui.print("권장 선수: " + ", ".join(MISSION_BY_ID[p].title for p in mission.prerequisites))
        if mission.kind in ("simulation", "scenario"):
            self.ui.print("[모의 상황] 실제 설치·부팅·물리 장치·GUI 조작을 수행하지 않습니다.")
        self.ui.print("\n" + BASELINE)

    def choose_variant(self, mission):
        record = self.progress.data["missions"].get(mission.id, {})
        used = {s["variant"] for s in record.get("solutions", [])}
        candidates = [v for v in mission.variants if v not in used]
        # Three independent variants are enough to establish delayed recall; reuse thereafter.
        return random.choice(candidates or mission.variants)

    def campaign(self, start, difficulty, resume=None):
        for index in range(start, len(MISSIONS)):
            mission = MISSIONS[index]
            if index != start and mission.chapter != MISSIONS[index-1].chapter:
                choice = self.ui.menu(f"다음 챕터 · {CHAPTERS[mission.chapter][0]}",
                    [("same", "같은 난이도로 계속"), ("change", "난이도 변경"), ("exit", "메인 메뉴")])
                if choice == "exit":
                    return
                if choice == "change":
                    difficulty = self.difficulty()
            action = self.play(mission, difficulty, resume=resume if index == start else None)
            if action == "exit":
                return
            if index + 1 < len(MISSIONS):
                self.progress.data["cursor"] = MISSIONS[index+1].id
                self.progress.save()
        self.ui.print("\n[사건 해결] 다음 담당자를 위한 인계가 끝났습니다.\n"
                      "건너뛴 미션과 오답은 복습 메뉴에서 이어갈 수 있습니다.")
        self.ui.pause()

    def practice_question(self, question, allow_hint=False):
        question = shuffle_choices(question)
        hint_used = False
        self.ui.print(f"\n[확인 문제 · {TOPICS[question.topic].title}]\n{question.stem}")
        for i, label in enumerate(question.choices, 1):
            self.ui.print(f"  {i}. {label}")
        while True:
            answer = self.ui.ask("답 1~4" + (" · h 힌트" if allow_hint else "") + " · s 해설 보기: ")
            if allow_hint and answer == "h":
                hint_used = True
                level = self.progress.hint()
                self.ui.print(f"[힌트 {level}/3] " + (
                    f"{TOPICS[question.topic].title}에서 각 용어의 역할을 구별하세요." if level == 1 else
                    TOPICS[question.topic].lesson if level == 2 else
                    f"정답: {question.choices[question.answer]}\n{question.explanation}"))
                continue
            if answer in ("1", "2", "3", "4", "s"):
                break
        correct = answer != "s" and int(answer)-1 == question.answer
        self.progress.answer(question, correct)
        self.ui.print(("✓ 정답" if correct else "다시 확인할 개념") +
                      f" · 정답 {question.answer+1}. {question.choices[question.answer]}\n{question.explanation}")
        return correct, hint_used

    def scenario(self, mission, difficulty, variant):
        if difficulty == "beginner":
            self.show_lessons(mission)
        else:
            self.ui.print("답변 중 h로 브리핑을 확인할 수 있습니다.")
        per_topic = {"beginner": 1, "intermediate": 2, "advanced": 3}[difficulty]
        selected = []
        for topic in mission.topics:
            pool = [q for q in QUESTIONS if q.topic == topic]
            # Variant controls a disjoint rotation within each topic, not just cosmetic file names.
            rotation = mission.variants.index(variant)
            selected.extend([pool[(rotation + j) % len(pool)] for j in range(min(per_topic, len(pool)))])
        wrong = []
        for q in selected:
            correct, _ = self.practice_question(q, allow_hint=True)
            if not correct:
                wrong.append(q)
        if wrong:
            self.ui.print("\n틀린 개념을 다시 확인합니다. 이 시도는 안내를 받은 해결로 기록합니다.")
            self.progress.hint()
            for q in wrong:
                while not self.practice_question(q)[0]:
                    self.ui.print("브리핑과 해설을 보고 다시 선택하세요.")
        self.progress.complete(mission)
        return self.after_mission(mission)

    def after_mission(self, mission):
        index = MISSIONS.index(mission)
        self.progress.data["cursor"] = MISSIONS[index+1].id if index+1 < len(MISSIONS) else None
        self.progress.save()
        self.ui.print("\n✓ 미션 완료 · " + self.progress.rank())
        if mission.debrief:
            self.ui.print(mission.debrief)
        if mission.clue:
            self.ui.print("[사건 기록] " + mission.clue)
        if self.chapter_count(mission.chapter) == 4:
            self.ui.print("[구역 복구] " + CHAPTERS[mission.chapter][1])
        value = self.ui.ask("\nEnter를 누르면 다음 미션 · r 재도전 · m 메인 메뉴: ")
        return "exit" if value == "m" else ("again" if value == "r" else "next")

    def play(self, mission, difficulty, resume=None, review=False):
        variant = resume["variant"] if resume else self.choose_variant(mission)
        preserved_hint = resume.get("hint", 0) if resume else 0
        while True:
            self.progress.begin(mission.id, difficulty, variant, review or bool(resume and resume.get("review")))
            self.progress.data["current"]["hint"] = preserved_hint
            self.progress.save()
            self.show_mission(mission, difficulty, variant)
            if mission.kind == "scenario":
                action = self.scenario(mission, difficulty, variant)
            else:
                if difficulty == "beginner":
                    self.ui.print("\n배우기\n" + TUTORIALS.get(mission.id, "quest lesson으로 개념을 확인하세요."))
                    self.ui.print("\n명령 예시\n" + mission.example.replace("{v}", variant))
                self.ui.print("\nquest mission · hint · check · reset · skip · exit · lesson\n"
                    "게임 메뉴: Ctrl+] · 명령 실행은 실제 Linux 안에서 진행됩니다.\n")
                try:
                    if not self.image_ready:
                        ensure_image(self.ui.print)
                        self.image_ready = True
                    with DockerLab(mission.network) as lab:
                        lab.setup(mission.setup.replace("{v}", variant))
                        first_prompt = True
                        previous_unmet = None

                        def handle(event, active):
                            nonlocal first_prompt, previous_unmet
                            command = event["command"]
                            if command == "mission":
                                self.show_mission(mission, difficulty, variant)
                            elif command in ("lesson", "hint"):
                                if command == "lesson":
                                    self.progress.hint()
                                    self.show_lessons(mission)
                                else:
                                    level = self.progress.hint()
                                    self.ui.print(f"\n[힌트 {level}/3]\n" + mission.hints[level-1].replace("{v}", variant))
                            elif command == "reset":
                                if self.ui.ask("실습 파일을 초기화할까요? 완료 기록은 유지됩니다. [y/N] ").lower() == "y":
                                    return "reset"
                            elif command == "skip":
                                self.progress.skip()
                                self.ui.print("미완료로 남겼습니다. 챕터 선택에서 다시 도전할 수 있습니다.")
                                return "next"
                            elif command == "exit":
                                return "exit"
                            elif command == "pause":
                                selected = self.ui.menu("게임 메뉴 · 현재 실습", [("continue", "실습 계속"),
                                    ("reset", "실습 초기화"), ("skip", "건너뛰기"), ("exit", "메인 메뉴")])
                                if selected == "skip":
                                    self.progress.skip()
                                    return "next"
                                if selected != "continue":
                                    return selected
                            elif command == "help":
                                self.ui.print("quest mission | hint | check | reset | skip | exit | answer 답 | lesson")
                            if command not in ("_prompt", "check", "answer"):
                                return None
                            result = active.check(mission.conditions(difficulty, variant))
                            if result.success:
                                self.ui.print("\n✓ 모든 완료 조건을 충족했습니다.")
                                self.progress.complete(mission)
                                pool = [q for q in QUESTIONS if q.id in MISSION_QUESTIONS.get(mission.id, ())]
                                if not pool:
                                    pool = [q for q in QUESTIONS if q.topic in mission.topics]
                                for q in random.sample(pool, min(2 if mission.boss else 1, len(pool))):
                                    self.practice_question(q)
                                return self.after_mission(mission)
                            if command == "check" or (not first_prompt and previous_unmet != result.unmet):
                                self.ui.print("\n남은 조건")
                                for label in result.unmet:
                                    self.ui.print("  [ ] " + label)
                            first_prompt = False
                            previous_unmet = result.unmet
                            return None

                        action = lab.interact(handle)
                except LabError as exc:
                    self.image_ready = False
                    self.ui.print(f"\n실습 연결 문제: {exc}\n완료 기록은 유지됩니다.")
                    action = "disconnected"
                if action == "disconnected":
                    action = self.ui.menu("셸 또는 Docker 연결이 종료되었습니다", [("reset", "환경을 새로 만들어 재시도"),
                        ("skip", "미완료로 남기고 다음 미션"), ("exit", "메인 메뉴")])
                    if action == "skip":
                        self.progress.skip()
                        action = "next"
            if action not in ("reset", "again"):
                return action
            if action == "again":
                variant = self.choose_variant(mission)
                preserved_hint = 0
            else:
                preserved_hint = self.progress.data["current"]["hint"]
            resume = None

    def review(self):
        weak = [mid for mid, r in self.progress.data["missions"].items()
                if mid in MISSION_BY_ID and (r["max_hint"] or r["skips"] or r["completed"])
                and not r["review_passed"]]
        wrong = [q for q in QUESTIONS if q.id in self.progress.data["questions"]
                 and not self.progress.data["questions"][q.id]["last_correct"]]
        choice = self.ui.menu(f"복습 · 미션 {len(weak)}개 · 오답 {len(wrong)}개", [
            ("missions", "변형 미션 풀기"), ("questions", "오답 다시 풀기"), ("back", "돌아가기")])
        if choice == "missions":
            if not weak:
                self.ui.print("아직 복습할 미션이 없습니다.")
            else:
                mid = self.ui.menu("복습할 미션", [(mid, MISSION_BY_ID[mid].title) for mid in weak] + [(None, "돌아가기")])
                if mid:
                    self.play(MISSION_BY_ID[mid], self.difficulty(), review=True)
        elif choice == "questions":
            for q in wrong:
                self.practice_question(q)
            if not wrong:
                self.ui.print("현재 오답이 없습니다.")
        if choice != "back":
            self.ui.pause()

    def status(self):
        self.ui.print(f"\n{self.progress.rank()} · XP {self.progress.data['xp']}")
        for chapter, (title, area, _) in CHAPTERS.items():
            count = self.chapter_count(chapter)
            self.ui.print(f"  {chapter:2}. {title}: {count}/4 · " + (area + " 복구" if count == 4 else "점검 중"))
        for mission in MISSIONS:
            record = self.progress.data["missions"].get(mission.id, {})
            if record.get("completed"):
                state = "복습 통과" if record.get("review_passed") else (
                    "자력 해결" if record.get("solutions") else "기본 완료")
                self.ui.print(f"  ✓ {mission.title} · {state}")
        self.ui.print("\n자력 해결: 중·고급에서 안내 없이 해결 · 복습 통과: 다음 실행에서 다른 변형을 자력 해결")
        for result in self.progress.data["exams"][-5:]:
            self.ui.print(f"  모의시험 {result['stage']}차: {result['score']}점 · " +
                          ("합격 기준 충족" if result["passed"] else "복습 필요"))
        self.ui.print(f"저장 위치: {self.progress.path}")
        self.ui.pause()

    def journal(self):
        self.ui.print("\n[사건 기록]\n기록 보관소 · 매일 02:00의 백업 실패와 사라진 인계 자료")
        for mid in self.progress.data["clues"]:
            if mid in MISSION_BY_ID:
                self.ui.print("\n" + MISSION_BY_ID[mid].title + "\n" + MISSION_BY_ID[mid].clue)
        if not self.progress.data["clues"]:
            self.ui.print("아직 발견한 단서가 없습니다.")
        self.ui.pause()

    def exam(self, stage):
        questions = select_exam(stage)
        duration = (60 if stage == 1 else 100) * 60
        self.ui.print(f"\n{stage}차 모의시험 · {len(questions)}문항 · {duration//60}분 · 자체 제작\n"
            "답 1~4 · n 다음 · p 이전 · s 제출\n합격: 총점 60점 이상" +
            (" + 각 과목 40% 이상" if stage == 2 else ""))
        self.ui.pause("Enter를 누르면 타이머가 시작됩니다.")
        deadline = time.monotonic() + duration
        answers, index, status = {}, 0, "submitted"
        try:
            while True:
                q = questions[index]
                remaining = max(0, int(deadline - time.monotonic()))
                self.ui.print(f"\n[{index+1}/{len(questions)}] 남은 시간 {remaining//60}:{remaining%60:02} · "
                              f"답변 {len(answers)}개\n{q.stem}")
                for i, label in enumerate(q.choices, 1):
                    self.ui.print(f"  {i}. {label}")
                if index in answers:
                    self.ui.print(f"현재 답: {answers[index]+1}")
                answer = self.ui.ask("선택: ", deadline=deadline)
                if answer == "s":
                    break
                if answer == "p":
                    index = max(0, index-1)
                elif answer == "n":
                    index = (index+1) % len(questions)
                elif answer in ("1", "2", "3", "4"):
                    answers[index] = int(answer)-1
                    if len(answers) == len(questions):
                        break
                    index = (index+1) % len(questions)
        except TimeoutError:
            status = "timed_out"
        except (EOFError, KeyboardInterrupt):
            status = "interrupted"
        result = score_exam(stage, questions, answers)
        result["status"] = status
        self.progress.add_exam(result)
        for i, q in enumerate(questions):
            if i in answers:
                self.progress.answer(q, answers[i] == q.answer)
        self.ui.print(f"\n[모의시험 결과] {result['score']}점 · {result['correct']}/{result['total']}\n" +
                      ("합격 기준 충족" if result["passed"] else "합격 기준 미충족"))
        if status != "submitted":
            self.ui.print("시간 종료" if status == "timed_out" else "중단한 시험 · 미응답은 오답으로 채점")
        for section, value in result["sections"].items():
            self.ui.print(f"  {section}: {value['correct']}/{value['total']} ({value['percent']}%)" +
                (" · 과락" if section in result["failed_sections"] else ""))
        self.ui.print("\n[문항 해설]")
        for i, q in enumerate(questions):
            if answers.get(i) != q.answer:
                self.ui.print(f"{i+1}. {q.stem}\n  정답: {q.choices[q.answer]} · {q.explanation}")
        if status != "interrupted":
            self.ui.pause()


def main():
    parser = argparse.ArgumentParser(description="리눅스마스터 2급 CLI 학습 게임")
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("--data-dir", type=Path, help="진도 저장 디렉터리")
    parser.add_argument("--doctor", action="store_true", help="실행 환경 점검")
    parser.add_argument("--build-lab", action="store_true", help="실습 이미지 준비")
    parser.add_argument("--list", action="store_true", help="챕터·미션 목록")
    parser.add_argument("--check-content", action="store_true", help="출제 범위·콘텐츠 검사")
    parser.add_argument("--mission", choices=list(MISSION_BY_ID), help="지정 미션으로 바로 시작")
    parser.add_argument("--difficulty", choices=list(DIFFICULTIES), default="beginner")
    parser.add_argument("--exam", type=int, choices=(1, 2), help="모의시험 바로 시작")
    args = parser.parse_args()
    ui = UI()
    if args.check_content:
        errors = content_errors()
        ui.print(f"{len(CHAPTERS)}개 챕터 · {len(MISSIONS)}개 미션 · {len(TOPICS)}개 개념 · {len(QUESTIONS)}개 자체 제작 문항")
        ui.print("\n".join(errors) if errors else f"공식 출제기준 {len(OFFICIAL_COVERAGE)}개 항목: 학습·평가 연결 확인")
        raise SystemExit(bool(errors))
    if args.list:
        for number, (title, _, _) in CHAPTERS.items():
            ui.print(f"\n{number}. {title}")
            for m in MISSIONS:
                if m.chapter == number:
                    ui.print(f"  {m.id}: {m.title}" + (" [모의 상황]" if m.kind != "lab" else " [실습]"))
        return
    if args.doctor or args.build_lab:
        try:
            if args.build_lab:
                ensure_image(ui.print)
            else:
                ui.print(f"Python {sys.version.split()[0]} · POSIX 터미널")
                result = docker("info", "--format", "{{.ServerVersion}}", timeout=10)
                ui.print("Docker " + result.stdout.strip() + " 연결 정상")
                ui.print("실습 이미지: " + ("준비됨" if docker("image", "inspect", "linux-quest:2026.1", check=False).returncode == 0 else "첫 실습에서 준비"))
            return
        except LabError as exc:
            ui.print(str(exc))
            raise SystemExit(1)
    path = args.data_dir / "progress.json" if args.data_dir else default_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    # One writer per save directory; a second terminal must not silently lose progress.
    with (path.parent / ".progress.lock").open("a+") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            ui.print("같은 진도로 실행 중인 게임이 있습니다. 다른 창을 종료하거나 --data-dir로 구분하세요.")
            raise SystemExit(1)
        try:
            game = Game(ui, Progress(path))
            if args.mission:
                game.play(MISSION_BY_ID[args.mission], args.difficulty)
            elif args.exam:
                game.exam(args.exam)
            else:
                game.main()
        except (EOFError, KeyboardInterrupt):
            ui.print("\n종료합니다. 미완료 미션은 다음 실행에서 초기 상태로 재개됩니다.")
        except (SaveError, OSError) as exc:
            ui.print(f"\n진행을 중단했습니다: {exc}")
            raise SystemExit(1)


if __name__ == "__main__":
    main()
