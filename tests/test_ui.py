import io
import os
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from linux_quest.ui import ANSI, UI, cell_width, wrap_cells


class ReadabilityTests(unittest.TestCase):
    def test_hangul_combining_marks_and_ansi_have_correct_display_width(self):
        self.assertEqual(cell_width("cd 자료"), 7)
        self.assertEqual(cell_width("\033[33mcd 자료\033[0m"), 7)
        self.assertEqual(cell_width("e\u0301"), 1)
        self.assertEqual(wrap_cells("가나다 라마바", 6), ["가나다", "라마바"])

    def test_panels_and_code_do_not_overflow_narrow_or_wide_terminals(self):
        for width in (24, 36, 80, 120):
            with self.subTest(width=width), patch("shutil.get_terminal_size", return_value=os.terminal_size((width, 32))):
                output = io.StringIO()
                with redirect_stdout(output):
                    ui = UI(color="never")
                    ui.panel("이번 목표", "긴 한글 안내도 화면 폭에 맞춰 읽을 수 있어야 합니다. " * 4)
                    ui.panel("명령 예시", "cd /srv/archive/" + "very-long-path/" * 7, "command", code=True)
                    ui.commands("pwd  현재 위치 확인\nls  파일과 디렉터리 목록\n\n긴 설명도 줄바꿈합니다.")
                    ui.choices(("긴 선택지 " * 8, "두 번째 선택지", "셋", "넷"))
                lines = output.getvalue().splitlines()
                self.assertTrue(all(cell_width(line) <= min(80, width-2) for line in lines), lines)
                self.assertNotIn("\033[", output.getvalue())

    def test_explicit_color_overrides_no_color_but_auto_honors_it(self):
        with patch.dict(os.environ, {"NO_COLOR": "1"}):
            ui = UI(color="auto")
            self.assertNotIn("\033[", ui.paint("목표"))
            ui = UI()
            styled = ui.paint("목표")
            self.assertIn("\033[", styled)
            self.assertEqual(ANSI.sub("", styled), "목표")

    def test_redirected_pages_have_readable_boundaries_without_cursor_controls(self):
        output = io.StringIO()
        with redirect_stdout(output):
            ui = UI(color="never")
            ui.page("첫 번째 문제", "문제 1/2")
            ui.page("두 번째 문제", "문제 2/2")
        transcript = output.getvalue()
        self.assertIn("문제 1/2", transcript)
        self.assertIn("문제 2/2", transcript)
        self.assertGreaterEqual(transcript.count("─" * ui.width), 4)
        self.assertNotIn("\033[", transcript)
