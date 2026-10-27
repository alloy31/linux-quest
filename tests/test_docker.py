import os
import unittest

from linux_quest.campaign import MISSIONS, MISSION_BY_ID
from linux_quest.runtime import DockerLab, EventDecoder, LabError, docker, ensure_image


@unittest.skipUnless(os.environ.get("RUN_DOCKER_TESTS") == "1", "RUN_DOCKER_TESTS=1로 실제 Docker 검증")
class DockerIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ensure_image()

    def execute_solution(self, lab, script):
        token = "integration-test"
        result = lab.run("export LQ_TOKEN=" + token + "\n" + script +
                         '\nquest _prompt "$PWD" "$?" "$(umask)"\n')
        events = EventDecoder(token).feed(result.stdout.encode())
        for kind, value in events:
            if kind == "event":
                lab.apply_event(value)

    def test_read_only_grep_and_real_file_changes(self):
        mission = MISSION_BY_ID["03-search"]
        with DockerLab() as lab:
            lab.setup(mission.setup.replace("{v}", "a"))
            self.assertFalse(lab.track_changes())
            output = lab.run("grep ERROR ~/logs_a/system.log").stdout
            self.assertIn("ERROR permission", output)
            self.assertFalse(lab.track_changes())
            lab.run("grep ERROR ~/logs_a/system.log > ~/logs_a/errors.txt")
            report = lab.track_changes()
            created = next(change for change in report.files if change.path.endswith("errors.txt"))
            self.assertEqual(created.status, "생성")
            self.assertIn("+ERROR disk", created.lines)
            lab.run("sed -i 's/ERROR disk/ERROR storage/' ~/logs_a/errors.txt")
            modified = lab.track_changes().files[0]
            self.assertIn("-ERROR disk", modified.lines)
            self.assertIn("+ERROR storage", modified.lines)
            lab.run("chmod 600 ~/logs_a/errors.txt")
            self.assertIn("권한: 0644 → 0600", lab.track_changes().files[0].details)
            lab.run("rm ~/logs_a/errors.txt")
            self.assertEqual(lab.track_changes().files[0].status, "삭제")

    def test_snapshot_does_not_follow_symlinks_or_open_fifos(self):
        with DockerLab() as lab:
            lab.setup("")
            lab.run("ln -s /etc/passwd ~/external; mkfifo ~/channel")
            snapshot = lab.snapshot()
            self.assertEqual(snapshot["files"]["/home/learner/external"]["kind"], "symlink")
            self.assertEqual(snapshot["files"]["/home/learner/external"]["target"], "/etc/passwd")
            self.assertNotIn("text", snapshot["files"]["/home/learner/external"])
            self.assertEqual(snapshot["files"]["/home/learner/channel"]["kind"], "special")
            self.assertNotIn("/etc/passwd", snapshot["files"])
            lab.run("python3 -c \"open('/home/learner/large', 'w').write('가'*4000)\"")
            large = lab.snapshot()["files"]["/home/learner/large"]
            self.assertTrue(large["truncated"])
            self.assertIsNotNone(large["text"])
            self.assertLessEqual(len(large["text"].encode()), 8192)

    def test_every_lab_difficulty_and_variant_is_solvable_and_not_precompleted(self):
        for mission in MISSIONS:
            if mission.kind == "scenario":
                continue
            for difficulty, variant in zip(("beginner", "intermediate", "advanced"), ("a", "b", "c")):
                with self.subTest(mission=mission.id, difficulty=difficulty, variant=variant):
                    with DockerLab(mission.network) as lab:
                        lab.setup(mission.setup.replace("{v}", variant))
                        goals = mission.conditions(difficulty, variant)
                        self.assertFalse(lab.check(goals).success, "미션이 처음부터 완료돼 있습니다")
                        script = mission.hints[2].replace("{v}", variant)
                        if mission.id == "07-edit":
                            script = (f"sed -i 's@/tmp/wrong@/srv/backup@' ~/backup_{variant}.conf\n"
                                      f"chmod 640 ~/backup_{variant}.conf\nexport BACKUP_TARGET=/srv/backup")
                        self.execute_solution(lab, script)
                        result = lab.check(goals)
                        self.assertTrue(result.success, result.unmet)

    def test_symbolic_permission_solution_and_partial_failure(self):
        mission = MISSION_BY_ID["04-mode"]
        with DockerLab() as lab:
            lab.setup(mission.setup.replace("{v}", "a"))
            lab.run("chmod u=rw,go= ~/secret_a.txt")
            self.assertTrue(lab.check(mission.conditions("beginner", "a")).success)
            self.assertFalse(lab.check(mission.conditions("advanced", "a")).success)

    def test_container_configuration_has_no_host_mounts_ports_or_shared_network(self):
        import json
        with DockerLab() as lab:
            info = json.loads(docker("inspect", lab.name).stdout)[0]
            self.assertEqual(info["Mounts"], [])
            self.assertFalse(info["HostConfig"]["Privileged"])
            self.assertEqual(info["HostConfig"]["NetworkMode"], "none")
            self.assertEqual(info["HostConfig"]["PortBindings"], {})
            self.assertEqual(info["HostConfig"]["PidsLimit"], 128)
            self.assertEqual(info["HostConfig"]["Memory"], 512 * 1024 * 1024)

    def test_stopped_container_is_reported_and_cleaned_up(self):
        with DockerLab() as lab:
            docker("stop", "-t", "1", lab.name)
            with self.assertRaises(LabError):
                lab.check(MISSION_BY_ID["01-arrival"].conditions("beginner"))
        self.assertNotEqual(docker("inspect", lab.name, check=False).returncode, 0)
