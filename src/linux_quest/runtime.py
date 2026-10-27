import base64
import fcntl
import hashlib
import json
import os
import pty
import secrets
import select
import shutil
import signal
import subprocess
import sys
import termios
import tty
from pathlib import Path

from .model import CheckResult

IMAGE = "linux-quest:2026.1"
ASSETS = Path(__file__).parent / "assets/docker"


class LabError(Exception):
    pass


def docker(*args, input=None, timeout=30, check=True):
    try:
        result = subprocess.run(["docker", *args], input=input, text=True,
                                capture_output=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise LabError(f"Docker에 연결할 수 없습니다: {exc}") from exc
    if check and result.returncode:
        raise LabError(result.stderr.strip() or result.stdout.strip() or "Docker 명령 실패")
    return result


def image_fingerprint(root=ASSETS):
    digest = hashlib.sha256()
    for path in sorted(root.iterdir()):
        if path.is_file() and not path.name.startswith("."):
            digest.update(path.name.encode())
            digest.update(b"\0")
            digest.update(path.read_bytes())
    return digest.hexdigest()


def ensure_image(announce=print):
    if not shutil.which("docker"):
        raise LabError("Docker를 찾을 수 없습니다. Docker Desktop을 설치·실행한 후 다시 시작하세요.")
    docker("info", "--format", "{{.ServerVersion}}", timeout=10)
    fingerprint = image_fingerprint()
    result = docker("image", "inspect", IMAGE, "--format", '{{json .Config.Labels}}', check=False)
    if result.returncode == 0:
        labels = json.loads(result.stdout) or {}
        if (labels.get("org.linux-quest.image-version") == "2026.1" and
                labels.get("org.linux-quest.source-hash") == fingerprint):
            return
    announce("실습 환경을 준비·갱신합니다. 첫 실행에는 이미지·패키지 다운로드가 필요합니다.")
    # Inherit output so a multi-minute first build has visible progress.
    result = subprocess.run(["docker", "build", "-t", IMAGE, "--label",
                             "org.linux-quest.source-hash=" + fingerprint, str(ASSETS)])
    if result.returncode:
        raise LabError("실습 이미지 준비에 실패했습니다. 네트워크와 Docker 상태를 확인해 주세요.")


class EventDecoder:
    """Streaming framing, including split UTF-8/output and split OSC events."""
    def __init__(self, token):
        self.prefix = b"\x1b]777;LQ;" + token.encode() + b";"
        self.buffer = b""

    def feed(self, chunk):
        self.buffer += chunk
        result = []
        while self.buffer:
            index = self.buffer.find(self.prefix)
            if index < 0:
                keep = 0
                for n in range(1, min(len(self.buffer), len(self.prefix)-1)+1):
                    if self.buffer.endswith(self.prefix[:n]):
                        keep = n
                output = self.buffer[:-keep] if keep else self.buffer
                if output:
                    result.append(("output", output))
                self.buffer = self.buffer[-keep:] if keep else b""
                break
            if index:
                result.append(("output", self.buffer[:index]))
                self.buffer = self.buffer[index:]
            end = self.buffer.find(b"\x07", len(self.prefix))
            if end < 0:
                if len(self.buffer) > 65536:
                    self.buffer = b""
                break
            raw = self.buffer[len(self.prefix):end]
            self.buffer = self.buffer[end+1:]
            try:
                event = json.loads(base64.b64decode(raw, validate=True))
                if isinstance(event, dict) and isinstance(event.get("command"), str):
                    result.append(("event", event))
            except (ValueError, TypeError):
                pass
        return result


class DockerLab:
    def __init__(self, network=False):
        self.name = "linux-quest-" + secrets.token_hex(6)
        self.network = network
        self.netname = self.name + "-net"
        self.sidecar = self.name + "-vault"
        self.token = secrets.token_hex(16)
        self.context = {"cwd": "/home/learner", "env": {}, "umask": "0022", "answer": ""}
        self.created = False
        self.process = None

    def __enter__(self):
        try:
            if self.network:
                docker("network", "create", "--internal", "--label", "org.linux-quest.managed=true", self.netname)
                docker("run", "-d", "--name", self.sidecar, "--label", "org.linux-quest.managed=true",
                    "--network", self.netname, "--network-alias", "quest-vault", "--memory", "128m",
                    "--cpus", "0.5", "--pids-limit", "64", "--cap-drop", "ALL",
                    "--security-opt", "no-new-privileges:true", "--workdir", "/opt/quest-network",
                    IMAGE, "python3", "-m", "http.server", "8080")
            docker("run", "-d", "--init", "--name", self.name, "--label", "org.linux-quest.managed=true",
                "--network", self.netname if self.network else "none", "--memory", "512m",
                "--cpus", "1", "--pids-limit", "128", "--hostname", "quest", IMAGE)
            self.created = True
            if self.network:
                readiness = """import socket, time
for attempt in range(40):
    try:
        connection = socket.create_connection(('quest-vault', 8080), timeout=0.5)
        connection.close()
        break
    except OSError:
        time.sleep(0.1)
else:
    raise RuntimeError('Internal lab service did not start')
"""
                docker("exec", self.name, "python3", "-c", readiness, timeout=25)
            return self
        except BaseException:
            self.close()
            raise

    def close(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()
        # Only exact random names owned by this object; never prune shared Docker resources.
        for name in (self.name, self.sidecar) if self.network else (self.name,):
            try:
                docker("rm", "-f", name, check=False, timeout=10)
            except LabError:
                pass
        if self.network:
            try:
                docker("network", "rm", self.netname, check=False, timeout=10)
            except LabError:
                pass

    def __exit__(self, *args):
        self.close()

    def setup(self, script):
        common = "mkdir -p /srv/archive/team /srv/archive/logs /srv/backup /run/quest\n"
        common += "chown -R learner:archive /srv/archive /srv/backup\n"
        docker("exec", "-i", "--user", "root", self.name, "bash", "-e", input=common + script)

    def run(self, script, user="learner", timeout=20):
        return docker("exec", "-i", "--user", user, self.name, "bash", "-e", input=script, timeout=timeout)

    def check(self, goals):
        try:
            result = docker("exec", "-i", "--user", "root", self.name,
                "python3", "/opt/quest/checks.py", input=json.dumps({"goals": goals, "context": self.context}))
            data = json.loads(result.stdout)
            return CheckResult(data["success"], data["unmet"])
        except (ValueError, KeyError) as exc:
            raise LabError("채점 결과를 읽지 못했습니다. 미션을 다시 시작해 주세요.") from exc

    def apply_event(self, event):
        if event["command"] == "_prompt":
            args = event.get("args", [])
            if len(args) >= 3:
                self.context.update(cwd=args[0], umask=args[2], env=event.get("env", {}))
        elif event["command"] == "answer":
            self.context["answer"] = " ".join(event.get("args", []))

    def interact(self, handler):
        """Full PTY relay: never interprets learner command strings on the host."""
        if not sys.stdin.isatty():
            raise LabError("실제 실습에는 대화형 터미널이 필요합니다. 일반 터미널에서 실행해 주세요.")
        master, slave = pty.openpty()
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        previous_winch = signal.getsignal(signal.SIGWINCH)
        decoder = EventDecoder(self.token)

        def resize(*_):
            try:
                size = fcntl.ioctl(fd, termios.TIOCGWINSZ, b"\0" * 8)
                fcntl.ioctl(master, termios.TIOCSWINSZ, size)
            except OSError:
                pass

        try:
            resize()
            signal.signal(signal.SIGWINCH, resize)
            args = ["docker", "exec", "-it", "--user", "learner", "-e", "LQ_TOKEN=" + self.token,
                    "-e", "TERM=" + os.environ.get("TERM", "xterm-256color")]
            if "NO_COLOR" in os.environ:
                args += ["-e", "NO_COLOR=1"]
            args += [self.name, "bash", "--noprofile", "--rcfile", "/opt/quest/bashrc", "-i"]
            self.process = subprocess.Popen(args, stdin=slave, stdout=slave, stderr=slave,
                                            start_new_session=True)
            os.close(slave)
            slave = -1
            tty.setraw(fd, when=termios.TCSANOW)
            while True:
                ready, _, _ = select.select([master, fd], [], [], 0.3)
                if master in ready:
                    try:
                        chunk = os.read(master, 32768)
                    except OSError:
                        chunk = b""
                    if not chunk:
                        return "disconnected"
                    for kind, value in decoder.feed(chunk):
                        if kind == "output":
                            os.write(sys.stdout.fileno(), value)
                            continue
                        self.apply_event(value)
                        termios.tcsetattr(fd, termios.TCSADRAIN, old)
                        try:
                            action = handler(value, self)
                        finally:
                            tty.setraw(fd, when=termios.TCSANOW)
                        if action:
                            return action
                if fd in ready:
                    key = os.read(fd, 4096)
                    if not key:
                        return "exit"
                    if b"\x1d" in key:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old)
                        try:
                            action = handler({"command": "pause"}, self)
                        finally:
                            tty.setraw(fd, when=termios.TCSANOW)
                        if action:
                            return action
                        os.write(master, b"\x0c")
                        continue
                    os.write(master, key)
                if self.process.poll() is not None and not ready:
                    return "disconnected"
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
            signal.signal(signal.SIGWINCH, previous_winch)
            os.close(master)
            if slave != -1:
                os.close(slave)
