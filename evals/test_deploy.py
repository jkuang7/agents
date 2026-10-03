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
        local_specs = self.add_skill("skills", "specs")
        vendor_wizard = self.add_skill("vendor/matt-pocock-skills", "wizard")

        result = self.run_deploy()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for runtime in self.runtime_roots:
            self.assertEqual(self.deployed_source(runtime, "accept-pr"), local_accept)
            self.assertEqual(self.deployed_source(runtime, "implement"), local_implement)
            self.assertEqual(self.deployed_source(runtime, "tdd"), local_tdd)
            self.assertEqual(self.deployed_source(runtime, "review-approach"), local_review)
            self.assertEqual(self.deployed_source(runtime, "submit-for-review"), local_submit)
            self.assertEqual(self.deployed_source(runtime, "specs"), local_specs)
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

    def test_claude_agents_deploy_and_prune(self):
        agents = self.repository / "claude-agents"
        agents.mkdir()
        reviewer = agents / "reviewer.md"
        reviewer.write_text("---\nname: reviewer\n---\n")
        retired = agents / "retired.md"
        retired.write_text("---\nname: retired\n---\n")
        claude_agents = self.runtime_roots["CLAUDE_HOME"] / "agents"

        self.assertEqual(self.run_deploy().returncode, 0)
        self.assertEqual((claude_agents / "reviewer.md").readlink(), reviewer)

        retired.unlink()
        result = self.run_deploy()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse((claude_agents / "retired.md").is_symlink())
        self.assertFalse((self.runtime_roots["CODEX_HOME"] / "agents").exists())
        self.assertEqual(self.run_deploy("--check").returncode, 0)


    def test_codex_agents_file_carries_workspace_rules_and_route(self):
        (self.root / "AGENTS.md").write_text("# Workspace rules\n")
        route = self.repository / "skills/route"
        route.mkdir(parents=True)
        (route / "SKILL.md").write_text(
            "---\nname: route\ndescription: Test.\n---\n\n# Route body\n"
        )
        codex_agents = self.runtime_roots["CODEX_HOME"] / "AGENTS.md"
        codex_agents.parent.mkdir(parents=True)
        codex_agents.symlink_to(self.root / "AGENTS.md")

        self.assertEqual(self.run_deploy("--check").returncode, 1)
        result = self.run_deploy()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        text = codex_agents.read_text()
        self.assertFalse(codex_agents.is_symlink())
        self.assertIn("# Workspace rules", text)
        self.assertIn("# Route body", text)
        self.assertNotIn("description: Test.", text)
        self.assertEqual(self.run_deploy("--check").returncode, 0)

        (route / "SKILL.md").write_text("---\nname: route\n---\n# Changed\n")
        self.assertEqual(self.run_deploy("--check").returncode, 1)

        codex_agents.write_text("hand written\n")
        self.assertEqual(self.run_deploy().returncode, 1)
        self.assertEqual(codex_agents.read_text(), "hand written\n")


if __name__ == "__main__":
    unittest.main()
