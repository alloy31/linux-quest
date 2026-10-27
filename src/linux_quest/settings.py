"""Local display/learning preferences, stored separately from learner progress."""
import json
import os
import tempfile
from pathlib import Path


DEFAULTS = {"version": 1, "color": "always", "difficulty": "beginner",
            "briefing": "concise", "width": "auto", "clear_pages": True}
OPTIONS = {
    "color": [("always", "컬러 켜기"), ("never", "컬러 끄기"), ("auto", "환경에 맞춰 자동")],
    "difficulty": [("beginner", "초급"), ("intermediate", "중급"), ("advanced", "고급")],
    "briefing": [("concise", "간단히 · 필요한 명령어 중심"), ("detailed", "자세히 · 개념 브리핑 함께")],
    "width": [("auto", "자동 · 최대 80칸"), ("60", "좁게 · 최대 60칸"), ("100", "넓게 · 최대 100칸")],
    "clear_pages": [(True, "새 화면에서 시작"), (False, "이전 내용을 남기고 구분선 표시")],
}
LABELS = {"color": "컬러 표시", "difficulty": "기본 난이도", "briefing": "초급 설명 분량",
          "width": "안내 화면 너비", "clear_pages": "문제 전환 화면"}


class SettingsError(Exception):
    pass


class Settings:
    def __init__(self, path: Path):
        self.path = path
        self.data = dict(DEFAULTS)
        if path.exists():
            try:
                saved = json.loads(path.read_text(encoding="utf-8"))
                if not isinstance(saved, dict) or saved.get("version") != 1:
                    raise ValueError("지원하지 않는 설정 형식")
                for key, options in OPTIONS.items():
                    if key in saved:
                        if (key == "clear_pages" and type(saved[key]) is not bool) or saved[key] not in dict(options):
                            raise ValueError(f"잘못된 설정: {key}")
                        self.data[key] = saved[key]
            except (ValueError, TypeError, OSError) as exc:
                raise SettingsError(f"설정 파일을 읽을 수 없습니다. 원본을 보존했습니다: {path}\n{exc}") from exc

    def save(self):
        name = None
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile("w", dir=self.path.parent, encoding="utf-8",
                                             prefix=".settings-", delete=False) as stream:
                name = stream.name
                json.dump(self.data, stream, ensure_ascii=False, indent=2)
                stream.flush()
                os.fsync(stream.fileno())
            os.chmod(name, 0o600)
            os.replace(name, self.path)
        except OSError as exc:
            raise SettingsError(f"설정을 저장하지 못했습니다: {exc}") from exc
        finally:
            if name and os.path.exists(name):
                os.unlink(name)

    def set(self, key, value):
        if key not in OPTIONS or (key == "clear_pages" and type(value) is not bool) or value not in dict(OPTIONS[key]):
            raise ValueError("지원하지 않는 설정값")
        previous = dict(self.data)
        self.data[key] = value
        try:
            self.save()
        except SettingsError:
            self.data = previous
            raise

    def reset(self):
        previous = self.data
        self.data = dict(DEFAULTS)
        try:
            self.save()
        except SettingsError:
            self.data = previous
            raise
