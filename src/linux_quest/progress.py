import json
import os
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path


class SaveError(Exception):
    pass


def default_path() -> Path:
    base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local/share"))
    return base / "linux-quest/progress.json"


class Progress:
    """The save lives on the host, never inside a learner-writable mount."""
    def __init__(self, path: Path | None = None):
        self.path = path or default_path()
        self.session = uuid.uuid4().hex
        self.data = {"version": 1, "difficulty": "beginner", "current": None,
                     "missions": {}, "questions": {}, "exams": [], "xp": 0,
                     "clues": [], "cursor": None}
        if self.path.exists():
            try:
                saved = json.loads(self.path.read_text(encoding="utf-8"))
                if (saved.get("version") != 1 or not isinstance(saved.get("missions"), dict)
                        or not isinstance(saved.get("questions"), dict)
                        or not isinstance(saved.get("xp"), int)):
                    raise ValueError("지원하지 않는 저장 형식")
                if (saved.get("difficulty") not in ("beginner", "intermediate", "advanced")
                        or not isinstance(saved.get("exams"), list)
                        or not isinstance(saved.get("clues"), list)
                        or saved["xp"] < 0):
                    raise ValueError("잘못된 진도 데이터")
                for record in saved["missions"].values():
                    if (not isinstance(record, dict)
                            or not isinstance(record.get("completed"), bool)
                            or not isinstance(record.get("solutions"), list)
                            or not all(isinstance(record.get(k), int) and record[k] >= 0
                                       for k in ("attempts", "max_hint", "skips"))
                            or not isinstance(record.get("review_passed"), bool)):
                        raise ValueError("잘못된 미션 기록")
                current = saved.get("current")
                if current is not None and (not isinstance(current, dict)
                        or not isinstance(current.get("id"), str)
                        or current.get("difficulty") not in ("beginner", "intermediate", "advanced")
                        or current.get("variant") not in ("a", "b", "c")
                        or not isinstance(current.get("hint"), int) or not 0 <= current["hint"] <= 3):
                    raise ValueError("잘못된 이어하기 기록")
                self.data.update(saved)
            except (ValueError, OSError, TypeError) as exc:
                raise SaveError(f"저장 파일을 읽을 수 없습니다. 원본은 보존했습니다: {self.path}\n{exc}") from exc

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        name = None
        try:
            with tempfile.NamedTemporaryFile("w", dir=self.path.parent, encoding="utf-8",
                                             prefix=".progress-", delete=False) as stream:
                name = stream.name
                json.dump(self.data, stream, ensure_ascii=False, indent=2)
                stream.flush()
                os.fsync(stream.fileno())
            os.chmod(name, 0o600)
            os.replace(name, self.path)
        except OSError as exc:
            raise SaveError(f"진도를 저장하지 못했습니다: {exc}") from exc
        finally:
            if name and os.path.exists(name):
                os.unlink(name)

    def record(self, mid):
        return self.data["missions"].setdefault(mid, {"completed": False, "attempts": 0,
            "max_hint": 0, "skips": 0, "solutions": [], "review_passed": False})

    def begin(self, mid, difficulty, variant, review=False):
        record = self.record(mid)
        record["attempts"] += 1
        self.data["difficulty"] = difficulty
        self.data["current"] = {"id": mid, "difficulty": difficulty,
            "variant": variant, "hint": 0, "review": review}
        self.data["cursor"] = mid
        self.save()

    def hint(self):
        current = self.data["current"]
        current["hint"] = min(3, current["hint"] + 1)
        record = self.record(current["id"])
        record["max_hint"] = max(record["max_hint"], current["hint"])
        self.save()
        return current["hint"]

    def complete(self, mission, next_mission=None):
        current = self.data["current"]
        record = self.record(mission.id)
        first = not record["completed"]
        record["completed"] = True
        if first:
            self.data["xp"] += 100 if mission.boss else 30
        independent = current["hint"] == 0 and current["difficulty"] != "beginner"
        previous = record["solutions"]
        if independent:
            if current["review"] and any(s["session"] != self.session and
                    s["variant"] != current["variant"] for s in previous):
                record["review_passed"] = True
            if not any(s["session"] == self.session and s["variant"] == current["variant"] for s in previous):
                previous.append({"variant": current["variant"], "session": self.session})
        if mission.clue and mission.id not in self.data["clues"]:
            self.data["clues"].append(mission.id)
        self.data["current"] = None
        self.data["cursor"] = next_mission
        self.save()
        return first

    def skip(self):
        if self.data["current"]:
            self.record(self.data["current"]["id"])["skips"] += 1
            self.data["current"] = None
            self.save()

    def answer(self, question, correct):
        record = self.data["questions"].setdefault(question.id, {"wrong": 0, "correct": 0,
                                                                  "last_correct": False})
        record["correct" if correct else "wrong"] += 1
        record["last_correct"] = correct
        self.save()

    def add_exam(self, result):
        self.data["exams"].append({**result, "at": datetime.now(timezone.utc).isoformat()})
        self.save()

    def rank(self):
        count = sum(r["completed"] for r in self.data["missions"].values())
        return next(title for threshold, title in [(32, "운영 책임자"), (22, "선임 관리자"),
            (12, "서버 관리자"), (4, "주니어 관리자"), (0, "신입 관리자")] if count >= threshold)
