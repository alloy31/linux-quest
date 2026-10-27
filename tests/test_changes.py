import unittest

from linux_quest.changes import compare_snapshots


def state(text="before\n", **kwargs):
    return {"kind": "file", "mode": "0644", "owner": "learner", "group": "archive",
            "text": text, "size": len(text.encode()), **kwargs}


class ChangePreviewTests(unittest.TestCase):
    def test_read_only_commands_do_not_invent_changes(self):
        snapshot = {"files": {"/srv/archive/log": state()}}
        self.assertFalse(compare_snapshots(snapshot, snapshot))

    def test_edit_has_removed_and_added_lines_with_context(self):
        before = {"files": {"/srv/archive/log": state("one\nbefore\nthree\n")}}
        after = {"files": {"/srv/archive/log": state("one\nafter\nthree\n")}}
        report = compare_snapshots(before, after)
        self.assertEqual(report.files[0].status, "수정")
        self.assertIn("-before", report.files[0].lines)
        self.assertIn("+after", report.files[0].lines)
        self.assertIn(" one", report.files[0].lines)

    def test_created_and_deleted_files_are_visible(self):
        created = compare_snapshots({"files": {}}, {"files": {"new": state("hello\n")}})
        self.assertEqual(created.files[0].status, "생성")
        self.assertIn("+hello", created.files[0].lines)
        deleted = compare_snapshots({"files": {"old": state("hello\n")}}, {"files": {}})
        self.assertEqual(deleted.files[0].status, "삭제")
        self.assertIn("-hello", deleted.files[0].lines)

    def test_permissions_are_reported_without_claiming_content_change(self):
        before = {"files": {"secret": state(mode="0666")}}
        after = {"files": {"secret": state(mode="0600")}}
        change = compare_snapshots(before, after).files[0]
        self.assertIn("권한: 0666 → 0600", change.details)
        self.assertEqual(change.lines, [])

    def test_line_ending_only_changes_are_explained(self):
        report = compare_snapshots({"files": {"file": state("hello\r\n")}},
                                   {"files": {"file": state("hello\n")}})
        self.assertIn("줄바꿈 형식이 변경되었습니다.", report.files[0].details)

    def test_truncated_collection_does_not_claim_missing_file_was_deleted(self):
        before = {"files": {"kept": state(), "missing": state()}}
        after = {"files": {"kept": state("after\n")}, "limited": True}
        report = compare_snapshots(before, after)
        self.assertEqual([change.path for change in report.files], ["kept"])
        self.assertTrue(report.notes)
        self.assertFalse(compare_snapshots(after, after))

    def test_terminal_control_sequences_in_file_content_are_not_executed(self):
        report = compare_snapshots({"files": {}}, {"files": {"path\x1b[2J": state("\x1b[2Jdanger\n")}})
        text = str(report.files)
        self.assertNotIn("\x1b", text)
        self.assertIn("\\x1b", report.files[0].path)

    def test_binary_files_are_not_decoded_as_text(self):
        before = {"files": {"blob": {"kind": "file", "size": 1, "text": None}}}
        after = {"files": {"blob": {"kind": "file", "size": 2, "text": None}}}
        change = compare_snapshots(before, after).files[0]
        self.assertFalse(change.lines)
        self.assertIn("바이너리", change.details[0])

    def test_environment_and_umask_are_reported(self):
        report = compare_snapshots({"files": {}}, {"files": {}},
            {"env": {}, "umask": "0022"}, {"env": {"ARCHIVE_ENV": "production"}, "umask": "0077"})
        self.assertEqual(len(report.environment), 2)
        self.assertIn("ARCHIVE_ENV", report.environment[0])

    def test_displayed_diff_is_bounded_and_declares_limits(self):
        report = compare_snapshots({"files": {}}, {"files": {
            f"file-{i:02}": state("\n".join(str(j) for j in range(200))) for i in range(20)}})
        self.assertEqual(len(report.files), 12)
        self.assertTrue(report.notes)
        self.assertLessEqual(len(report.files[0].lines), 48)
