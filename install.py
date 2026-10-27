#!/usr/bin/env python3
"""Install only a launcher symlink, without modifying shell configuration."""
import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(description="linux-quest 실행 명령 설치")
parser.add_argument("--bin-dir", type=Path, default=Path.home() / ".local/bin")
args = parser.parse_args()
source = Path(__file__).resolve().parent / "linux-quest"
source.chmod(source.stat().st_mode | 0o111)
args.bin_dir.mkdir(parents=True, exist_ok=True)
link = args.bin_dir / "linux-quest"
if link.exists() or link.is_symlink():
    if not link.is_symlink() or link.resolve() != source:
        raise SystemExit(f"기존 파일을 보존했습니다. 다른 --bin-dir를 선택하세요: {link}")
else:
    link.symlink_to(source)
print(f"설치됨: {link}\n실행: linux-quest")
if str(args.bin_dir) not in os.environ.get("PATH", "").split(os.pathsep):
    print(f"현재 PATH에 설치 경로가 없습니다. 직접 실행: {link}")
