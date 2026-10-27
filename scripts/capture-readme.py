#!/usr/bin/env python3
"""Render real PTY output for the README. Optional developer dependency: Pillow.

No hand-written UI content: both images launch the actual CLI using isolated saves.
Provide --mono-font and --cjk-font on systems without the default macOS fonts.
"""
import argparse
import re
import sys
import tempfile
import unicodedata
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))
from test_terminal import Terminal

COLORS = ["#171e2c", "#ee7a7a", "#8bdf9c", "#efc56d", "#81a7e8", "#ce9bea", "#67dce4", "#e7edf6",
          "#8792a3", "#ff9696", "#a2ecb0", "#ffe09c", "#a1c1ff", "#e2baff", "#9becf4", "#ffffff"]
DEFAULT = "#e7edf6"


def screen_from_ansi(raw, columns=80, rows=32):
    grid = [[None] * columns for _ in range(rows)]
    x = y = 0
    fg, bold, dim = DEFAULT, False, False
    text, index = raw.decode("utf-8", errors="replace"), 0
    while index < len(text):
        if text[index] == "\x1b":
            match = re.match(r"\x1b\[([0-9;?]*)([@-~])", text[index:])
            if match:
                args, command = match.groups()
                values = [int(v) if v.isdigit() else 0 for v in args.split(";")]
                if command == "m":
                    for value in values:
                        if value == 0:
                            fg, bold, dim = DEFAULT, False, False
                        elif value == 1:
                            bold = True
                        elif value == 2:
                            dim = True
                        elif value == 22:
                            bold = dim = False
                        elif value == 39:
                            fg = DEFAULT
                        elif 30 <= value <= 37:
                            fg = COLORS[value-30]
                        elif 90 <= value <= 97:
                            fg = COLORS[value-90+8]
                elif command in ("H", "f"):
                    y = max(0, (values[0] or 1)-1)
                    x = max(0, (values[1] if len(values) > 1 and values[1] else 1)-1)
                elif command == "J" and values[0] in (2, 3):
                    grid = [[None] * columns for _ in range(rows)]
                elif command == "K":
                    for col in range(x, columns):
                        grid[min(y, rows-1)][col] = None
                index += len(match.group(0))
                continue
            index += 1
            continue
        char = text[index]
        index += 1
        if char == "\r":
            x = 0
        elif char == "\n":
            y += 1
        elif char == "\b":
            x = max(0, x-1)
        elif char == "\t":
            x = (x//8+1)*8
        elif ord(char) >= 32 and not unicodedata.combining(char):
            width = 2 if unicodedata.east_asian_width(char) in ("W", "F") else 1
            if x + width > columns:
                x, y = 0, y+1
            while y >= rows:
                grid.pop(0)
                grid.append([None] * columns)
                y -= 1
            grid[y][x] = (char, fg, bold, dim)
            x += width
        while y >= rows:
            grid.pop(0)
            grid.append([None] * columns)
            y -= 1
    while grid and not any(grid[-1]):
        grid.pop()
    return grid


def font(path, size, index=0):
    try:
        return ImageFont.truetype(str(path), size=size, index=index)
    except OSError:
        return ImageFont.truetype(str(path), size=size)


def render(raw, destination, title, mono, cjk):
    grid = screen_from_ansi(raw)
    cell, line, pad, bar = 13, 29, 28, 48
    width, height = 80*cell + pad*2, len(grid)*line + pad*2 + bar
    image = Image.new("RGB", (width, height), "#080e19")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((1, 1, width-2, height-2), radius=16, fill="#0e1726", outline="#28364d", width=2)
    draw.line((1, bar, width-2, bar), fill="#28364d", width=1)
    for i, color in enumerate(("#f47779", "#edc468", "#80ca9b")):
        draw.ellipse((20+i*20, 18, 31+i*20, 29), fill=color)
    regular, heavy = font(mono, 21), font(mono, 21, 1)
    korean, korean_heavy = font(cjk, 22, 4), font(cjk, 22, 6)
    draw.text((width/2, 25), title, fill="#98a8bf", font=font(mono, 13), anchor="mm")
    baseline = max(regular.getmetrics()[0], korean.getmetrics()[0])
    for row, cells in enumerate(grid):
        for col, value in enumerate(cells):
            if not value:
                continue
            char, color, bold, dim = value
            if dim:
                color = "#99a6b8"
            if char in "─│╭╮╰╯":
                # Draw the actual terminal line glyphs without depending on font coverage.
                x, y = pad+col*cell, bar+pad+row*line
                cx, cy, radius = x+cell/2, y+line/2, cell/2
                if char == "─":
                    draw.line((x, cy, x+cell, cy), fill=color, width=2)
                elif char == "│":
                    draw.line((cx, y, cx, y+line), fill=color, width=2)
                elif char == "╭":
                    draw.arc((cx, cy, cx+2*radius, cy+2*radius), 180, 270, fill=color, width=2)
                    draw.line((cx, cy+radius, cx, y+line), fill=color, width=2)
                elif char == "╮":
                    draw.arc((x-radius, cy, x+radius, cy+2*radius), 270, 360, fill=color, width=2)
                    draw.line((cx, cy+radius, cx, y+line), fill=color, width=2)
                elif char == "╰":
                    draw.line((cx, y, cx, cy-radius), fill=color, width=2)
                    draw.arc((cx, cy-2*radius, cx+2*radius, cy), 90, 180, fill=color, width=2)
                else:
                    draw.line((cx, y, cx, cy-radius), fill=color, width=2)
                    draw.arc((x-radius, cy-2*radius, x+radius, cy), 0, 90, fill=color, width=2)
                continue
            is_cjk = unicodedata.east_asian_width(char) in ("W", "F")
            selected = (korean_heavy if bold else korean) if is_cjk else (heavy if bold else regular)
            draw.text((pad+col*cell, bar+pad+row*line+baseline), char,
                      font=selected, fill=color, anchor="ls")
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, optimize=True)
    print(f"{destination.relative_to(ROOT)} · {width}x{height}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mono-font", type=Path, default=Path("/System/Library/Fonts/Menlo.ttc"))
    parser.add_argument("--cjk-font", type=Path, default=Path("/System/Library/Fonts/AppleSDGothicNeo.ttc"))
    args = parser.parse_args()
    if not args.mono_font.exists() or not args.cjk_font.exists():
        parser.error("--mono-font와 --cjk-font에 사용 가능한 글꼴 경로를 지정하세요.")
    with tempfile.TemporaryDirectory(prefix="quest-readme-") as tmp:
        terminal = Terminal(tmp, width=80, height=32, color=None)
        try:
            terminal.expect("숫자+Enter")
            render(bytes(terminal.transcript), ROOT / "docs/assets/start-screen.png",
                   "linux-quest", args.mono_font, args.cjk_font)
            terminal.send("5\r")
            terminal.expect("다음 점검 때 만나요")
            terminal.wait()
        finally:
            terminal.close()
        terminal = Terminal(tmp, "--mission", "01-arrival", width=80, height=36, color=None)
        try:
            terminal.expect(":~$ ")
            render(bytes(terminal.transcript), ROOT / "docs/assets/first-mission.png",
                   "linux-quest / first mission", args.mono_font, args.cjk_font)
            terminal.send("quest exit\r")
            terminal.wait()
        finally:
            terminal.close()


if __name__ == "__main__":
    main()
