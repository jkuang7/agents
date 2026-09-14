"""Verify single-source skill deployment and managed-link cleanup."""

from pathlib import Path
import os
import shutil
import subprocess
import tempfile
import unittest


DEPLOY = Path(__file__).resolve().parents[1] / "bin/deploy"


class DeployTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory(prefix="deploy-eval-")
        self.root = Path(self.temporary_directory.name)
        self.repository = self.root / "repository"
        (self.repository / "bin").mkdir(parents=True)
        shutil.copy2(DEPLOY, self.repository / "bin/deploy")

        self.runtime_roots = {
            "CODEX_HOME": self.root / "codex",
            "CLAUDE_HOME": self.root / "claude",
            "AGENTS_HOME": self.root / "agents",
        }

    def tearDown(self):
        self.temporary_directory.cleanup()

    def add_skill(self, source, name):
        skill = self.repository / source / name
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Test fixture.\n---\n"
        )
        return skill

    def run_deploy(self, *arguments):
        environment = os.environ.copy()
        environment.update({name: str(path) for name, path in self.runtime_roots.items()})
        return subprocess.run(
            [self.repository / "bin/deploy", *arguments],
            text=True,
            capture_output=True,
            timeout=10,
            env=environment,
        )

    def deployed_source(self, runtime, name):
        return (self.runtime_roots[runtime] / "skills" / name).readlink()

    def test_local_and_vendor_skills_deploy_from_their_sources(self):
        local_accept = self.add_skill("skills", "accept-pr")
        local_implement = self.add_skill("skills", "implement")
        local_tdd = self.add_skill("skills", "tdd")
        local_review = self.add_skill("skills", "review-approach")
        local_submit = self.add_skill("skills", "submit-for-review")
        local_to_spec = self.add_skill("skills", "to-spec")
        vendor_wizard = self.add_skill("vendor/matt-pocock-skills", "wizard")

        result = self.run_deploy()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for runtime in self.runtime_roots:
            self.assertEqual(self.deployed_source(runtime, "accept-pr"), local_accept)
            self.assertEqual(self.deployed_source(runtime, "implement"), local_implement)
            self.assertEqual(self.deployed_source(runtime, "tdd"), local_tdd)
            self.assertEqual(self.deployed_source(runtime, "review-approach"), local_review)
            self.assertEqual(self.deployed_source(runtime, "submit-for-review"), local_submit)
            self.assertEqual(self.deployed_source(runtime, "to-spec"), local_to_spec)
            self.assertEqual(self.deployed_source(runtime, "wizard"), vendor_wizard)

        check = self.run_deploy("--check")
        self.assertEqual(check.returncode, 0, check.stdout + check.stderr)

    def test_duplicate_skill_names_are_rejected(self):
        self.add_skill("skills", "implement")
        self.add_skill("vendor/matt-pocock-skills", "implement")

        result = self.run_deploy()

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("DUPLICATE skill name 'implement'", result.stdout)

    def test_deploy_prunes_stale_managed_links(self):
        self.add_skill("vendor/matt-pocock-skills", "wizard")
        retired = self.add_skill("vendor/matt-pocock-skills", "retired")
        codex_skills = self.runtime_roots["CODEX_HOME"] / "skills"
        codex_skills.mkdir(parents=True)
        stale_link = codex_skills / "retired"
        stale_link.symlink_to(retired)
        shutil.rmtree(retired)

        result = self.run_deploy()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse(stale_link.is_symlink())


if __name__ == "__main__":
    unittest.main()
