#!/usr/bin/python3
"""Only emits framed control messages. Docker credentials are never in the lab."""
import base64
import json
import os
import sys

command = sys.argv[1] if len(sys.argv) > 1 else "help"
allowed = ("mission", "hint", "check", "reset", "skip", "exit", "answer", "lesson", "help", "_prompt")
if command not in allowed:
    print("quest mission | hint | check | reset | skip | exit | answer 답 | lesson")
    sys.exit(2)
body = {"command": command, "args": sys.argv[2:]}
if command == "_prompt":
    body["env"] = {key: os.environ.get(key, "") for key in ("ARCHIVE_ENV", "BACKUP_TARGET")}
payload = base64.b64encode(json.dumps(body).encode()).decode()
sys.stdout.write("\033]777;LQ;" + os.environ.get("LQ_TOKEN", "") + ";" + payload + "\007")
sys.stdout.flush()
