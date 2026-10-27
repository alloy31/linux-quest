import json
import io
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from contextlib import redirect_stdout

from linux_quest.settings import DEFAULTS, OPTIONS, Settings, SettingsError
from linux_quest.ui import UI


class SettingsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "settings.json"

    def test_first_launch_defaults_to_color_without_creating_a_file(self):
        settings = Settings(self.path)
        self.assertEqual(settings.data, DEFAULTS)
        self.assertFalse(self.path.exists())
        self.assertTrue(UI(color=settings.data["color"]).color)

    def test_all_supported_preferences_survive_restart(self):
        settings = Settings(self.path)
        for key, options in OPTIONS.items():
            settings.set(key, options[-1][0])
        self.assertEqual(Settings(self.path).data, settings.data)
        self.assertEqual(self.path.stat().st_mode & 0o777, 0o600)

    def test_reset_only_changes_settings_not_progress(self):
        progress = self.path.with_name("progress.json")
        progress.write_text('{"completed":"keep"}')
        settings = Settings(self.path)
        settings.set("difficulty", "advanced")
        settings.reset()
        self.assertEqual(Settings(self.path).data, DEFAULTS)
        self.assertEqual(progress.read_text(), '{"completed":"keep"}')

    def test_invalid_file_is_not_silently_overwritten(self):
        for value in ("broken", json.dumps({"version": 1, "color": "unknown"}),
                      json.dumps({"version": 1, "clear_pages": "false"})):
            self.path.write_text(value)
            with self.assertRaises(SettingsError):
                Settings(self.path)
            self.assertEqual(self.path.read_text(), value)

    def test_width_is_limited_by_the_physical_terminal(self):
        with patch("shutil.get_terminal_size", return_value=os.terminal_size((120, 30))):
            self.assertEqual(UI(width="60").width, 60)
            self.assertEqual(UI(width="100").width, 100)
        with patch("shutil.get_terminal_size", return_value=os.terminal_size((36, 14))):
            self.assertEqual(UI(width="100").width, 34)

    def test_page_setting_can_preserve_history_with_visible_separators(self):
        ui = UI(color="never", clear_pages=False)
        ui.interactive = True
        output = io.StringIO()
        with redirect_stdout(output):
            ui.page("다음 문제", "문제 2/3")
        self.assertNotIn("\033[2J", output.getvalue())
        self.assertIn("다음 문제", output.getvalue())
        self.assertIn("─", output.getvalue())
