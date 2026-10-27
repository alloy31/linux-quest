import base64
import json
import io
import os
import tempfile
import unittest
import time
from unittest.mock import patch
from pathlib import Path

from linux_quest.model import Mission
from linux_quest.progress import Progress, SaveError
from linux_quest.runtime import EventDecoder
from linux_quest.ui import UI


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "progress.json"
        self.progress = Progress(self.path)
        self.mission = Mission("test", 1, "test", "story", ("files",), "goal", boss=True)

    def finish(self, difficulty="intermediate", variant="a", review=False, hints=0):
        self.progress.begin("test", difficulty, variant, review)
        for _ in range(hints):
            self.progress.hint()
        return self.progress.complete(self.mission)

    def test_rewards_only_once_and_hints_do_not_establish_independence(self):
        self.assertTrue(self.finish(hints=1))
        self.assertFalse(self.finish(variant="b"))
        self.assertEqual(self.progress.data["xp"], 100)
        self.assertEqual(len(self.progress.record("test")["solutions"]), 1)

    def test_review_requires_another_session_and_another_variant(self):
        self.finish()
        self.finish(variant="b", review=True)
        self.assertFalse(self.progress.record("test")["review_passed"])
        self.progress = Progress(self.path)
        self.finish(variant="c", review=True)
        self.assertTrue(self.progress.record("test")["review_passed"])

    def test_beginner_guidance_does_not_count_as_independent(self):
        self.finish(difficulty="beginner")
        self.assertEqual(self.progress.record("test")["solutions"], [])

    def test_skip_and_restart_preserve_completed_records(self):
        self.finish()
        self.progress.begin("later", "advanced", "a")
        self.progress.skip()
        self.progress = Progress(self.path)
        self.assertTrue(self.progress.record("test")["completed"])
        self.assertFalse(self.progress.record("later")["completed"])
        self.assertEqual(self.progress.data["xp"], 100)

    def test_corrupt_save_is_preserved(self):
        self.path.write_text("broken", encoding="utf-8")
        with self.assertRaises(SaveError):
            Progress(self.path)
        self.assertEqual(self.path.read_text(), "broken")

    def test_parseable_but_invalid_save_is_not_overwritten(self):
        self.progress.save()
        value = json.loads(self.path.read_text())
        value["current"] = {"id": "test", "difficulty": "advanced", "variant": "a", "hint": -1}
        raw = json.dumps(value)
        self.path.write_text(raw)
        with self.assertRaises(SaveError):
            Progress(self.path)
        self.assertEqual(self.path.read_text(), raw)


class ProtocolTests(unittest.TestCase):
    def test_events_can_cross_every_byte_boundary_without_losing_output(self):
        token = "random-test-token"
        event = {"command": "_prompt", "args": ["/srv/archive/team", "0", "0022"]}
        data = b"\x1b]777;LQ;" + token.encode() + b";" + base64.b64encode(json.dumps(event).encode()) + b"\x07"
        stream = "한글\r\n".encode() + data + b"learner@quest$ "
        for split in range(len(stream)):
            decoder = EventDecoder(token)
            parsed = decoder.feed(stream[:split]) + decoder.feed(stream[split:])
            self.assertEqual(b"".join(value for kind, value in parsed if kind == "output"),
                             "한글\r\n".encode() + b"learner@quest$ ")
            self.assertEqual([value for kind, value in parsed if kind == "event"], [event])

    def test_other_tokens_are_ordinary_terminal_output(self):
        output = b"\x1b]777;LQ;another;payload\x07"
        self.assertEqual(EventDecoder("mine").feed(output), [("output", output)])


class DeadlineTests(unittest.TestCase):
    def test_no_input_does_not_suspend_exam_clock(self):
        reader, writer = os.pipe()
        try:
            with os.fdopen(reader) as stdin, patch("sys.stdin", stdin), patch("sys.stdout", io.StringIO()):
                ui = UI()
                start = time.monotonic()
                with self.assertRaises(TimeoutError):
                    ui.ask("answer", deadline=start + 0.03)
                self.assertLess(time.monotonic() - start, 1)
        finally:
            os.close(writer)


if __name__ == "__main__":
    unittest.main()
