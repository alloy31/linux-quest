import difflib
import unicodedata
from dataclasses import dataclass, field


def display_text(value):
    """File content is data, not terminal control sequences."""
    return "".join(char if char == "\t" or unicodedata.category(char) not in ("Cc", "Cf")
                   else f"\\x{ord(char):02x}" for char in str(value))


@dataclass
class FileChange:
    path: str
    status: str
    details: list[str] = field(default_factory=list)
    lines: list[str] = field(default_factory=list)


@dataclass
class ChangeReport:
    files: list[FileChange] = field(default_factory=list)
    environment: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def __bool__(self):
        return bool(self.files or self.environment or self.notes)


def compare_snapshots(before, after, old_context=None, new_context=None):
    report = ChangeReport()
    old_files, new_files = before.get("files", {}), after.get("files", {})
    incomplete = before.get("limited") or after.get("limited") or before.get("errors") or after.get("errors")
    if incomplete:
        report.notes.append("일부 경로는 수집 범위·접근 권한 때문에 생략했습니다. 추가·삭제 판정은 생략합니다.")
    for path in sorted(set(old_files) | set(new_files)):
        old, new = old_files.get(path), new_files.get(path)
        if old == new or (incomplete and (old is None or new is None)):
            continue
        change = FileChange(display_text(path), "생성" if old is None else "삭제" if new is None else "수정")
        a, b = old or {}, new or {}
        for key, label in (("mode", "권한"), ("owner", "소유자"), ("group", "그룹"), ("target", "링크 대상")):
            if a.get(key) != b.get(key):
                change.details.append(f"{label}: {display_text(a.get(key, '없음'))} → {display_text(b.get(key, '없음'))}")
        old_text = "" if old is None else a.get("text")
        new_text = "" if new is None else b.get("text")
        if old_text is not None and new_text is not None and old_text != new_text:
            raw = list(difflib.unified_diff(old_text.splitlines(), new_text.splitlines(),
                                           fromfile="이전", tofile="이후", n=2, lineterm=""))
            change.lines = [display_text(line[:400]) + (" …" if len(line) > 400 else "") for line in raw[:48]]
            if not raw:
                change.details.append("줄바꿈 형식이 변경되었습니다.")
            if len(raw) > 48:
                change.details.append("긴 diff는 처음 48줄만 표시합니다.")
            if bool(old_text.endswith("\n")) != bool(new_text.endswith("\n")):
                change.details.append(f"줄 끝 개행: {'있음' if old_text.endswith(chr(10)) else '없음'} → {'있음' if new_text.endswith(chr(10)) else '없음'}")
        elif a.get("read_error") or b.get("read_error"):
            change.details.append("파일 내용을 읽을 권한이 없습니다.")
        elif a.get("kind") == "file" or b.get("kind") == "file":
            if old_text is None or new_text is None:
                change.details.append(f"바이너리 또는 텍스트로 표시할 수 없는 파일 · {a.get('size', 0)} → {b.get('size', 0)} bytes")
            elif a.get("size") != b.get("size"):
                change.details.append(f"크기: {a.get('size', 0)} → {b.get('size', 0)} bytes")
        if a.get("truncated") or b.get("truncated"):
            change.details.append("큰 파일은 처음 8 KiB만 미리 봅니다. 나머지 내용은 직접 확인하세요.")
        report.files.append(change)
    if len(report.files) > 12:
        report.notes.append(f"변경 경로 {len(report.files)}개 중 처음 12개를 표시합니다.")
        report.files = report.files[:12]
    if old_context is not None and new_context is not None:
        for name in ("ARCHIVE_ENV", "BACKUP_TARGET"):
            a = old_context.get("env", {}).get(name, "")
            b = new_context.get("env", {}).get(name, "")
            if a != b:
                report.environment.append(f"{name}: {display_text(a or '(없음)')} → {display_text(b or '(없음)')}")
        if old_context.get("umask") != new_context.get("umask"):
            report.environment.append(f"umask: {display_text(old_context.get('umask', ''))} → {display_text(new_context.get('umask', ''))}")
    if not report.files and not report.environment and before == after:
        return ChangeReport()
    return report
