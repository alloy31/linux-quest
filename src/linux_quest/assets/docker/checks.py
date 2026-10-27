"""Read-only lab inspection. Compatible with Rocky 8's Python 3.6."""
import json
import os
import pwd
import grp
import stat
import subprocess
import sys
import tarfile

payload = json.load(sys.stdin)
context = payload.get("context", {})
unmet = []
for goal in payload["goals"]:
    kind, path = goal["kind"], goal.get("path", "")
    expected = goal.get("value")
    ok = False
    try:
        if kind == "cwd":
            ok = context.get("cwd") == path
        elif kind == "file":
            ok = os.path.isfile(path) and not os.path.islink(path)
        elif kind == "dir":
            ok = os.path.isdir(path)
        elif kind == "missing":
            ok = not os.path.lexists(path)
        elif kind == "content":
            with open(path, encoding="utf-8") as stream:
                ok = stream.read() == expected
        elif kind == "contains":
            with open(path, encoding="utf-8") as stream:
                ok = expected in stream.read()
        elif kind == "mode":
            ok = stat.S_IMODE(os.stat(path).st_mode) == int(expected, 8)
        elif kind == "owner":
            ok = pwd.getpwuid(os.stat(path).st_uid).pw_name == expected
        elif kind == "group":
            ok = grp.getgrgid(os.stat(path).st_gid).gr_name == expected
        elif kind == "user":
            ok = pwd.getpwnam(expected).pw_uid >= 1000
        elif kind == "member":
            ok = goal["user"] in grp.getgrnam(expected).gr_mem
        elif kind == "symlink":
            ok = os.path.islink(path) and os.path.realpath(path) == expected
        elif kind == "hardlink":
            ok = not os.path.islink(path) and os.path.samefile(path, expected)
        elif kind == "env":
            ok = context.get("env", {}).get(path) == expected
        elif kind == "umask":
            ok = int(context.get("umask", "-1"), 8) == int(expected, 8)
        elif kind == "answer":
            ok = context.get("answer", "").strip().casefold() == expected.casefold()
        elif kind in ("process_absent", "nice"):
            with open(path) as stream:
                pid = int(stream.read().strip())
            proc = "/proc/{}/stat".format(pid)
            alive = os.path.exists(proc)
            if kind == "process_absent":
                if alive:
                    with open(proc) as stream:
                        state = stream.read().rsplit(")", 1)[1].split()[0]
                    alive = state != "Z"
                ok = not alive
            else:
                ok = alive and os.getpriority(os.PRIO_PROCESS, pid) == int(expected)
        elif kind == "archive":
            with tarfile.open(path, "r:gz" if path.endswith(".gz") else "r") as archive:
                wanted = goal["members"]
                names = [name.lstrip("./") for name in archive.getnames()]
                ok = all(name in names for name in wanted)
                if ok and "file_content" in goal:
                    member = next(m for m in archive.getmembers() if m.name.lstrip("./") == wanted[0])
                    source = archive.extractfile(member)
                    ok = source is not None and source.read().decode() == goal["file_content"]
        elif kind == "package":
            ok = subprocess.call(["rpm", "-q", expected], stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL) == 0
    except (OSError, ValueError, KeyError, tarfile.TarError):
        ok = False
    if not ok:
        unmet.append(goal["label"])
print(json.dumps({"success": not unmet, "unmet": unmet}, ensure_ascii=False))
