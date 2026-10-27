"""Bounded, read-only workspace snapshots using the learner's own permissions.

Compatible with Rocky 8 / Python 3.6. Never follows symlinks or opens special files.
"""
import grp
import codecs
import json
import os
import pwd
import stat

ROOTS = ("/home/learner", "/srv/archive", "/srv/backup")
IGNORE = {".bash_history", ".viminfo", ".lesshst", ".cache", "__pycache__"}
MAX_ENTRIES, MAX_BYTES = 160, 8192
entries, errors = {}, []
limited = False


def collect(path):
    global limited
    if len(entries) >= MAX_ENTRIES:
        limited = True
        return
    try:
        info = os.lstat(path)
        entry = {"mode": format(stat.S_IMODE(info.st_mode), "04o"),
                 "uid": info.st_uid, "gid": info.st_gid}
        try:
            entry["owner"] = pwd.getpwuid(info.st_uid).pw_name
        except KeyError:
            entry["owner"] = str(info.st_uid)
        try:
            entry["group"] = grp.getgrgid(info.st_gid).gr_name
        except KeyError:
            entry["group"] = str(info.st_gid)
        if stat.S_ISLNK(info.st_mode):
            entry.update(kind="symlink", target=os.readlink(path))
        elif stat.S_ISDIR(info.st_mode):
            entry["kind"] = "directory"
        elif stat.S_ISREG(info.st_mode):
            entry.update(kind="file", size=info.st_size)
            try:
                with open(path, "rb") as stream:
                    body = stream.read(MAX_BYTES+1)
                entry["truncated"] = len(body) > MAX_BYTES
                if entry["truncated"]:
                    entry["updated"] = info.st_mtime_ns
                try:
                    entry["text"] = codecs.getincrementaldecoder("utf-8")().decode(body[:MAX_BYTES], final=not entry["truncated"]) if b"\0" not in body else None
                except UnicodeDecodeError:
                    entry["text"] = None
                if entry["text"] is None:
                    entry["updated"] = info.st_mtime_ns
            except OSError:
                entry["read_error"] = True
        else:
            entry["kind"] = "special"
        entries[path] = entry
    except OSError:
        errors.append(path)


for root in ROOTS:
    if not os.path.lexists(root):
        continue
    collect(root)
    if entries.get(root, {}).get("kind") != "directory":
        continue
    for folder, dirs, files in os.walk(root, topdown=True, followlinks=False,
                                      onerror=lambda error: errors.append(error.filename or root)):
        dirs[:] = sorted(name for name in dirs if name not in IGNORE)
        for name in sorted(dirs + [name for name in files if name not in IGNORE]):
            collect(os.path.join(folder, name))
            if limited:
                break
        if limited:
            break
    if limited:
        break
print(json.dumps({"files": entries, "limited": limited, "errors": errors}, ensure_ascii=False))
