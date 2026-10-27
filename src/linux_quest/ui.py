import os
import re
import select
import shutil
import sys
import termios
import time
import tty
import unicodedata
from contextlib import contextmanager


BANNER = r""" _     ___ _   _ _   ___  __
| |   |_ _| \ | | | | \ \/ /
| |    | ||  \| | | | |\  /
| |___ | || |\  | |_| |/  \
|_____|___|_| \_|\___//_/\_\
          Q U E S T"""

ANSI = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
PALETTE = {"accent": "1;36", "command": "1;33", "hint": "1;35", "success": "1;32",
           "warning": "1;33", "muted": "2", "strong": "1", "selected": "1;36"}


def cell_width(text):
    """Terminal columns, including Hangul; ANSI styling occupies no columns."""
    return sum(0 if unicodedata.combining(char) or unicodedata.category(char) in ("Cc", "Cf")
               else 2 if unicodedata.east_asian_width(char) in ("W", "F") else 1
               for char in ANSI.sub("", text))


def wrap_cells(text, width):
    """Wrap at word boundaries where possible, splitting long paths only if necessary."""
    width = max(1, width)
    result = []
    for paragraph in text.expandtabs(4).split("\n"):
        if not paragraph:
            result.append("")
            continue
        line = ""
        for word in re.findall(r"\S+|\s+", paragraph):
            if word.isspace():
                if line and not line.endswith(" "):
                    line += " "
                continue
            if line and cell_width(line + word) > width:
                result.append(line.rstrip())
                line = ""
            for char in word:
                if line and cell_width(line + char) > width:
                    result.append(line.rstrip())
                    line = ""
                line += char
        result.append(line.rstrip())
    return result


@contextmanager
def raw_input():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd, when=termios.TCSANOW)
        yield
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


class UI:
    def __init__(self, color="always"):
        self.interactive = sys.stdin.isatty() and sys.stdout.isatty() and os.environ.get("TERM") != "dumb"
        self.color = color == "always" or (color == "auto" and self.interactive and "NO_COLOR" not in os.environ)

    def print(self, text=""):
        print(text, flush=True)

    @property
    def width(self):
        # Leave room for the terminal's last column, which can trigger an unwanted wrap.
        return max(8, min(80, shutil.get_terminal_size((80, 24)).columns - 2))

    def paint(self, text, tone="accent"):
        return f"\033[{PALETTE[tone]}m{text}\033[0m" if self.color else text

    def clear(self):
        if self.interactive:
            print("\033[2J\033[H", end="", flush=True)

    def page(self, title, meta=""):
        self.clear()
        if not self.interactive:
            self.print("\n" + "─" * self.width)
        if meta:
            self.text(meta, "muted")
        self.text(title, "strong")
        self.print(self.paint("─" * self.width, "accent"))

    def text(self, text, tone=None, indent=0):
        indent = min(indent, max(0, self.width - 4))
        for line in wrap_cells(text, self.width - indent):
            self.print(" " * indent + (self.paint(line, tone) if tone else line))

    def section(self, title, tone="accent"):
        self.print()
        self.text(title, tone)

    def panel(self, title, body, tone="accent", code=False):
        self.print()
        width = self.width
        if width < 24:
            self.text(title, tone)
            for line in body.split("\n"):
                self.text(line, "command" if code else None, indent=2)
            return
        caption = " " + title + " "
        if cell_width(caption) > width - 4:
            caption = wrap_cells(caption, width - 4)[0].rstrip() + " "
        self.print(self.paint("╭─" + caption + "─" * max(0, width - 3 - cell_width(caption)) + "╮", tone))
        inner = width - 4
        for raw in body.split("\n"):
            prefix = "" if not code or not raw else ("  " if raw.lstrip().startswith("#") else "$ ")
            lines = wrap_cells(raw, inner - len(prefix))
            for i, line in enumerate(lines):
                content = (prefix if i == 0 else " " * len(prefix)) + line
                padding = " " * max(0, inner - cell_width(content))
                styled = self.paint(content, "muted" if code and raw.lstrip().startswith("#") else "command") if code else content
                self.print(self.paint("│", tone) + " " + styled + padding + " " + self.paint("│", tone))
        self.print(self.paint("╰" + "─" * (width - 2) + "╯", tone))

    def commands(self, tutorial):
        self.section("배우기")
        for line in tutorial.split("\n"):
            parts = re.split(r" {2,}", line.strip(), maxsplit=1)
            if len(parts) == 2 and cell_width(parts[0]) <= min(28, self.width // 2):
                command, description = parts
                column = min(30, max(8, cell_width(command) + 2))
                available = self.width - column - 2
                if available >= 8:
                    for i, fragment in enumerate(wrap_cells(description, available)):
                        label = self.paint(command, "command") if i == 0 else ""
                        self.print("  " + label + " " * (column - (cell_width(command) if i == 0 else 0)) + fragment)
                    continue
            self.text(line, indent=2)

    def choices(self, choices):
        self.print()
        for i, label in enumerate(choices, 1):
            prefix = f"  {i}. "
            for j, line in enumerate(wrap_cells(label, self.width - len(prefix))):
                self.print((self.paint(prefix, "accent") if j == 0 else " " * len(prefix)) + line)

    def lab_help(self):
        self.print()
        self.text("힌트 quest hint · 목표 quest mission · 채점 quest check", indent=2)
        self.text("초기화 quest reset · 나가기 quest exit · 메뉴 Ctrl+]", "muted", indent=2)

    def title(self):
        self.clear()
        width, height = shutil.get_terminal_size((80, 24))
        self.print(self.paint(BANNER if width >= 42 and height >= 20 else "[ LINUX QUEST ]", "accent"))
        self.text("리눅스마스터 2급 · 2026 · Rocky Linux 8", "muted")
        self.print()

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
                    self.clear()
                self.text(title, "strong")
                self.print(self.paint("─" * self.width, "accent"))
                self.print()
                for i, (key, label) in enumerate(entries):
                    marker = ">" if i == selected else " "
                    suffix = " (기록 없음)" if key in disabled else ""
                    line = f"  {marker} {i+1}. {label}{suffix}"
                    self.text(line, "selected" if i == selected else "muted" if key in disabled else None)
                    if len(entries) <= 6:
                        self.print()
                self.text("↑↓ 선택 · Enter 확인 · 숫자+Enter" + (f"  [{digits}]" if digits else ""), "muted")
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
            if self.color:
                self.print("\033[0m")

    def ask(self, prompt, deadline=None):
        prompt = self.paint(prompt, "accent")
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
