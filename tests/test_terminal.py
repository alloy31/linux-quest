"""Real terminal tests: keyboard menus, Docker PTY relay, vi, and recovery."""
import fcntl
import json
import os
import pty
import re
import select
import signal
import struct
import subprocess
import sys
import tempfile
import termios
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Terminal:
    def __init__(self, data_dir, *args, width=90, height=32, color="never"):
        self.fd, slave = pty.openpty()
        fcntl.ioctl(self.fd, termios.TIOCSWINSZ, struct.pack("HHHH", height, width, 0, 0))
        self.proc = subprocess.Popen([sys.executable, str(ROOT / "linux-quest"),
            "--data-dir", str(data_dir), *(["--color", color] if color else []), *args], stdin=slave, stdout=slave, stderr=slave,
            cwd=ROOT, env={**os.environ, "TERM": "xterm-256color", "NO_COLOR": "1"},
            start_new_session=True)
        os.close(slave)
        self.pending = b""
        self.transcript = bytearray()

    def send(self, value):
        os.write(self.fd, value.encode() if isinstance(value, str) else value)

    def expect(self, text, timeout=20):
        target = text.encode()
        deadline = time.monotonic() + timeout
        while target not in self.pending:
            if time.monotonic() >= deadline:
                raise AssertionError(f"터미널 대기 실패: {text}\n" + self.pending[-6000:].decode(errors="replace"))
            if select.select([self.fd], [], [], min(0.2, max(0, deadline-time.monotonic())))[0]:
                try:
                    chunk = os.read(self.fd, 65536)
                except OSError:
                    chunk = b""
                if not chunk:
                    raise AssertionError(f"터미널이 먼저 종료됨: {text}\n" + self.pending.decode(errors="replace"))
                self.transcript.extend(chunk)
                self.pending += chunk
        index = self.pending.index(target) + len(target)
        output, self.pending = self.pending[:index], self.pending[index:]
        return output.decode(errors="replace")

    def close(self):
        if self.proc.poll() is None:
            self.send(b"\x03")
            try:
                self.wait(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(self.proc.pid, signal.SIGTERM)
                self.proc.wait(timeout=5)
        os.close(self.fd)

    def wait(self, timeout=10):
        # Keep draining the terminal: tcsetattr(TCSADRAIN) may wait for the PTY reader.
        deadline = time.monotonic() + timeout
        while self.proc.poll() is None:
            if time.monotonic() > deadline:
                raise subprocess.TimeoutExpired(self.proc.args, timeout)
            if select.select([self.fd], [], [], 0.1)[0]:
                try:
                    chunk = os.read(self.fd, 65536)
                except OSError:
                    chunk = b""
                self.pending += chunk
                self.transcript.extend(chunk)
        return self.proc.returncode


class MenuTerminalTests(unittest.TestCase):
    def test_startup_settings_save_and_apply_on_the_next_launch(self):
        with tempfile.TemporaryDirectory() as tmp:
            terminal = Terminal(tmp, color=None)
            try:
                terminal.expect("숫자+Enter")
                terminal.send("4\r")
                terminal.expect("설정 · 변경하면 바로 저장됩니다")
                terminal.expect("숫자+Enter")
                terminal.send("1\r")
                terminal.expect("컬러 표시")
                terminal.expect("숫자+Enter")
                terminal.send("2\r")
                terminal.expect("컬러 표시 · 컬러 끄기")
                terminal.expect("숫자+Enter")
                terminal.send("2\r")
                terminal.expect("기본 난이도")
                terminal.expect("숫자+Enter")
                terminal.send("3\r")
                terminal.expect("기본 난이도 · 고급")
                terminal.expect("숫자+Enter")
                terminal.send("7\r")
                terminal.expect("숫자+Enter")
                terminal.send("5\r")
                terminal.expect("다음 점검 때 만나요")
                self.assertEqual(terminal.wait(), 0)
            finally:
                terminal.close()
            settings = json.loads((Path(tmp) / "settings.json").read_text())
            self.assertEqual(settings["color"], "never")
            self.assertEqual(settings["difficulty"], "advanced")
            resumed = Terminal(tmp, color=None)
            try:
                screen = resumed.expect("숫자+Enter")
                self.assertNotRegex(screen, r"\x1b\[[0-9;]*m")
                resumed.send("\r")
                resumed.expect("> 3. 고급")
            finally:
                resumed.close()

    def test_cli_color_override_does_not_change_saved_preferences(self):
        with tempfile.TemporaryDirectory() as tmp:
            from linux_quest.settings import Settings
            path = Path(tmp) / "settings.json"
            Settings(path).set("color", "never")
            terminal = Terminal(tmp, "--color", "always", color=None)
            try:
                self.assertIn("\033[1;36m", terminal.expect("숫자+Enter"))
                terminal.send("5\r")
                terminal.expect("다음 점검 때 만나요")
                self.assertEqual(terminal.wait(), 0)
            finally:
                terminal.close()
            self.assertEqual(Settings(path).data["color"], "never")

    def test_question_pages_wait_for_explanation_acknowledgement_before_clearing(self):
        with tempfile.TemporaryDirectory() as tmp:
            terminal = Terminal(tmp, "--mission", "01-foundations", "--difficulty", "beginner")
            try:
                terminal.expect("Enter를 누르면 확인 문제를 시작합니다.")
                terminal.send("\r")
                first = terminal.expect("문제 1/4")
                self.assertIn("\033[2J\033[H", first)
                terminal.expect("s 해설 보기:")
                terminal.send("s\r")
                feedback = terminal.expect("Enter를 누르면 다음 문제로 이동합니다.")
                self.assertIn("다시 확인할 개념", feedback)
                self.assertNotIn("\033[2J\033[H", feedback)
                self.assertNotIn("문제 2/4", feedback)
                terminal.send("\r")
                second = terminal.expect("문제 2/4")
                self.assertIn("\033[2J\033[H", second)
                terminal.expect("s 해설 보기:")
            finally:
                terminal.close()

    def test_default_launch_is_colored_even_when_no_color_is_inherited(self):
        with tempfile.TemporaryDirectory() as tmp:
            terminal = Terminal(tmp, color=None)
            try:
                screen = terminal.expect("숫자+Enter")
                self.assertIn("\033[1;36m", screen)
                terminal.send("5\r")
                terminal.expect("다음 점검 때 만나요")
                self.assertEqual(terminal.wait(), 0)
            finally:
                terminal.close()

    def test_mock_exam_navigation_revision_and_early_submission(self):
        for stage, total in ((1, 50), (2, 80)):
            with self.subTest(stage=stage), tempfile.TemporaryDirectory() as tmp:
                terminal = Terminal(tmp, "--exam", str(stage))
                try:
                    terminal.expect("타이머가 시작됩니다.")
                    terminal.send("\r")
                    terminal.expect(f"[1/{total}]")
                    terminal.expect("선택:")
                    terminal.send("1\r")
                    next_page = terminal.expect(f"[2/{total}]")
                    self.assertIn("\033[2J\033[H", next_page)
                    terminal.expect("선택:")
                    terminal.send("p\r")
                    terminal.expect("현재 답: 1")
                    terminal.expect("선택:")
                    terminal.send("2\r")
                    terminal.expect(f"[2/{total}]")
                    terminal.expect("선택:")
                    terminal.send("s\r")
                    terminal.expect("[모의시험 결과]")
                    terminal.expect("Enter를 누르면 계속합니다.")
                    saved = json.loads((Path(tmp) / "progress.json").read_text())
                    result = saved["exams"][-1]
                    self.assertEqual(result["total"], total)
                    self.assertEqual(result["status"], "submitted")
                    self.assertFalse(result["passed"])
                    # Revision must be counted once, not as two separate question attempts.
                    self.assertEqual(sum(r["correct"] + r["wrong"] for r in saved["questions"].values()), 1)
                    terminal.send("\r")
                    self.assertEqual(terminal.wait(timeout=5), 0)
                finally:
                    terminal.close()

    def test_ascii_title_disabled_resume_arrow_keys_and_number_enter(self):
        with tempfile.TemporaryDirectory() as tmp:
            terminal = Terminal(tmp)
            try:
                transcript = terminal.expect("숫자+Enter")
                self.assertIn("Q U E S T", transcript)
                self.assertIn("이어하기 (기록 없음)", transcript)
                # A pasted arrow sequence plus Enter must not be discarded by raw-mode setup.
                terminal.send(b"\x1b[A\r")
                terminal.expect("다음 점검 때 만나요")
                self.assertEqual(terminal.wait(timeout=5), 0)
            finally:
                terminal.close()

    def test_small_terminal_uses_compact_title_and_number_exit(self):
        with tempfile.TemporaryDirectory() as tmp:
            terminal = Terminal(tmp, width=36, height=14)
            try:
                transcript = terminal.expect("숫자+Enter")
                self.assertIn("[ LINUX QUEST ]", transcript)
                self.assertNotIn("Q U E S T", transcript)
                terminal.send("5\r")
                terminal.expect("다음 점검 때 만나요")
                terminal.wait(timeout=5)
            finally:
                terminal.close()


@unittest.skipUnless(os.environ.get("RUN_DOCKER_TESTS") == "1", "실제 Docker/PTY 검증은 opt-in")
class GameTerminalTests(unittest.TestCase):
    def test_full_start_hint_reset_persistent_shell_auto_check_and_resume(self):
        with tempfile.TemporaryDirectory() as tmp:
            terminal = Terminal(tmp)
            try:
                terminal.expect("숫자+Enter")
                terminal.send("\r")
                terminal.expect("초급 — 개념")
                terminal.expect("숫자+Enter")
                terminal.send(b"\x1b[B\x1b[A\r")
                terminal.expect("도입 건너뛰기")
                terminal.send("s\r")
                terminal.expect("learner@quest:~$")
                terminal.send("export ARCHIVE_ENV=production\r")
                terminal.expect("learner@quest:~$")
                terminal.send("printf 'persist=%s\\n' \"$ARCHIVE_ENV\"\r")
                terminal.expect("persist=production")
                terminal.expect("learner@quest:~$")
                terminal.send("sleep 30\r")
                terminal.expect("sleep 30")
                terminal.send(b"\x03")
                terminal.expect("learner@quest:~$")
                terminal.send("quest hint\r")
                terminal.expect("[힌트 1/3]")
                terminal.expect("learner@quest:~$")
                terminal.send("quest reset\r")
                terminal.expect("[y/N]")
                terminal.send("y\r")
                terminal.expect("learner@quest:~$")
                saved = json.loads((Path(tmp) / "progress.json").read_text())
                self.assertEqual(saved["current"]["hint"], 1)
                terminal.send("cd /srv/archive/team\r")
                terminal.expect("✓ 모든 완료 조건")
                terminal.expect("s 해설 보기:")
                terminal.send("s\r")
                terminal.expect("m 메인 메뉴:")
                terminal.send("\r")
                next_mission = terminal.expect("닫힌 서랍의 목록")
                self.assertIn("\033[2J\033[H", next_mission)
                self.assertNotIn("첫 출근 — 인수인계 자료 찾기", next_mission)
                terminal.expect("learner@quest:~$")
                terminal.send("quest exit\r")
                terminal.expect("숫자+Enter")
                saved = json.loads((Path(tmp) / "progress.json").read_text())
                self.assertTrue(saved["missions"]["01-arrival"]["completed"])
                self.assertEqual(saved["xp"], 30)
                self.assertEqual(saved["cursor"], "01-observe")
                terminal.send("5\r")
                terminal.expect("다음 점검 때 만나요")
                terminal.wait(timeout=5)
            finally:
                terminal.close()
            resumed = Terminal(tmp)
            try:
                resumed.expect("숫자+Enter")
                resumed.send("2\r")
                resumed.expect("닫힌 서랍의 목록")
                resumed.expect("learner@quest:~$")
                # Ctrl+D exits the real shell, then the host offers recovery.
                resumed.send(b"\x04")
                resumed.expect("셸 또는 Docker 연결이 종료")
                resumed.expect("숫자+Enter")
                resumed.send("3\r")
                resumed.expect("숫자+Enter")
                resumed.send("5\r")
                resumed.expect("다음 점검 때 만나요")
                resumed.wait(timeout=5)
            finally:
                resumed.close()

    def test_vi_is_interactive_and_checks_only_after_returning_to_shell(self):
        with tempfile.TemporaryDirectory() as tmp:
            terminal = Terminal(tmp, "--mission", "07-edit", "--difficulty", "advanced")
            try:
                terminal.expect("learner@quest:~$")
                saved = json.loads((Path(tmp) / "progress.json").read_text())
                variant = saved["current"]["variant"]
                terminal.send(f"vi ~/backup_{variant}.conf\r")
                terminal.expect("destination=/tmp/wrong")
                terminal.send(b"gg0Cdestination=/srv/backup\x1b")
                self.assertEqual(json.loads((Path(tmp) / "progress.json").read_text())["xp"], 0)
                terminal.send(":wq\r")
                terminal.expect("learner@quest:~$")
                terminal.send(f"chmod 640 ~/backup_{variant}.conf; export BACKUP_TARGET=/srv/backup\r")
                terminal.expect("✓ 모든 완료 조건")
                terminal.expect("s 해설 보기:")
                terminal.send("s\r")
                terminal.expect("m 메인 메뉴:")
                terminal.send("m\r")
                self.assertEqual(terminal.wait(timeout=10), 0)
            finally:
                terminal.close()
