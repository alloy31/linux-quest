import os
import select
import shutil
import sys
import termios
import time
import tty
from contextlib import contextmanager


BANNER = r""" _     ___ _   _ _   ___  __
| |   |_ _| \ | | | | \ \/ /
| |    | ||  \| | | | |\  /
| |___ | || |\  | |_| |/  \
|_____|___|_| \_|\___//_/\_\
          Q U E S T"""


@contextmanager
def raw_input():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        yield
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


class UI:
    def __init__(self):
        self.interactive = sys.stdin.isatty() and sys.stdout.isatty() and os.environ.get("TERM") != "dumb"
        self.color = self.interactive and "NO_COLOR" not in os.environ

    def print(self, text=""):
        print(text, flush=True)

    def title(self):
        if self.interactive:
            self.print("\033[2J\033[H")
        width, height = shutil.get_terminal_size((80, 24))
        self.print(BANNER if width >= 42 and height >= 20 else "[ LINUX QUEST ]")
        self.print("\n리눅스마스터 2급 · 2026 · Rocky Linux 8\n")

    def menu(self, title, entries, disabled=(), banner=False):
        """Entries are (value, label). Numbers followed by Enter also work."""
        enabled = [i for i, (key, _) in enumerate(entries) if key not in disabled]
        if not enabled:
            raise ValueError("활성 메뉴 없음")
        selected, digits = enabled[0], ""
        if not self.interactive:
            if banner:
                self.title()
            self.print(title)
            for i, (key, label) in enumerate(entries, 1):
                self.print(f"  {i}. {label}" + (" (기록 없음)" if key in disabled else ""))
            while True:
                choice = self.ask("선택: ")
                if choice.isdigit() and int(choice) - 1 in enabled:
                    return entries[int(choice)-1][0]
                self.print("활성화된 메뉴 번호를 입력하세요.")
        try:
            while True:
                if banner:
                    self.title()
                else:
                    self.print("\033[2J\033[H")
                self.print(title + "\n")
                for i, (key, label) in enumerate(entries):
                    marker = ">" if i == selected else " "
                    suffix = " (기록 없음)" if key in disabled else ""
                    line = f"  {marker} {i+1}. {label}{suffix}"
                    if self.color and i == selected:
                        line = "\033[1;36m" + line + "\033[0m"
                    self.print(line)
                self.print("\n↑↓ 선택 · Enter 확인 · 숫자+Enter" + (f"  [{digits}]" if digits else ""))
                with raw_input():
                    key = os.read(sys.stdin.fileno(), 1)
                    if key == b"\x1b" and select.select([sys.stdin], [], [], 0.08)[0]:
                        key += os.read(sys.stdin.fileno(), 1)
                        if key == b"\x1b[" and select.select([sys.stdin], [], [], 0.08)[0]:
                            key += os.read(sys.stdin.fileno(), 1)
                if key in (b"\x03", b"\x04", b""):
                    raise EOFError
                if key in (b"\x1b[A", b"k"):
                    selected = enabled[(enabled.index(selected)-1) % len(enabled)]
                    digits = ""
                elif key in (b"\x1b[B", b"j"):
                    selected = enabled[(enabled.index(selected)+1) % len(enabled)]
                    digits = ""
                elif key.isdigit():
                    digits = (digits + key.decode())[-2:]
                elif key in (b"\x7f", b"\x08"):
                    digits = digits[:-1]
                elif key in (b"\r", b"\n"):
                    if digits:
                        index = int(digits) - 1
                        digits = ""
                        if index not in enabled:
                            continue
                        selected = index
                    return entries[selected][0]
        finally:
            self.print("\033[0m")

    def ask(self, prompt, deadline=None):
        if deadline is None:
            return input(prompt).strip()
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError
        print(prompt, end="", flush=True)
        if not select.select([sys.stdin], [], [], remaining)[0]:
            self.print("\n시험 시간이 끝났습니다.")
            raise TimeoutError
        value = sys.stdin.readline()
        if value == "":
            raise EOFError
        if time.monotonic() > deadline:
            raise TimeoutError
        return value.strip()

    def pause(self, message="Enter를 누르면 계속합니다."):
        self.ask(message)
