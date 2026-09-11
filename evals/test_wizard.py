"""Exercise the shared wizard library without browsers, credentials, or remote calls."""

from pathlib import Path
import subprocess
import tempfile
import unittest


TEMPLATE = Path(__file__).resolve().parents[1] / "vendor/matt-pocock-skills/wizard/template.sh"


class WizardCompletionTests(unittest.TestCase):
    def run_wizard(self, body, gh_result=0):
        library = TEMPLATE.read_text().split("# STAGES: author this section.", 1)[0]
        # A shell function shadows any installed gh. Secret input is consumed locally.
        fake_gh = f"""
gh() {{
  if [[ "$1" == auth ]]; then return 0; fi
  if [[ "$1" == secret ]]; then cat >/dev/null; fi
  return {gh_result}
}}
"""
        with tempfile.TemporaryDirectory(prefix="wizard-eval-") as directory:
            return subprocess.run(
                ["bash"], input=library + fake_gh + body, cwd=directory,
                text=True, capture_output=True, timeout=10,
            )

    def test_required_secret_failure_is_incomplete(self):
        result = self.run_wizard('set_secret CI_TOKEN fake-private-value\nfinish\n', 1)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("Setup incomplete", result.stdout)
        self.assertIn("CI_TOKEN", result.stdout)
        self.assertNotIn("Setup complete", result.stdout)
        self.assertNotIn("fake-private-value", result.stdout + result.stderr)

    def test_required_variable_failure_is_incomplete(self):
        result = self.run_wizard('set_var SERVICE_REGION local-test\nfinish\n', 1)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("SERVICE_REGION", result.stdout)

    def test_optional_failure_does_not_block_required_success(self):
        result = self.run_wizard('set_var ANALYTICS_REGION local-test optional\nfinish\n', 1)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Setup complete", result.stdout)
        self.assertIn("Optional steps skipped", result.stdout)
        self.assertIn("ANALYTICS_REGION", result.stdout)

    def test_successful_writes_complete_without_exposing_secret(self):
        result = self.run_wizard(
            'set_secret CI_TOKEN fake-private-value\nset_var SERVICE_REGION local-test\nfinish\n'
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Setup complete", result.stdout)
        self.assertNotIn("fake-private-value", result.stdout + result.stderr)

    def test_manual_required_step_blocks_completion(self):
        result = self.run_wizard('record_skip "Confirm migration outcome"\nfinish\n')
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("Confirm migration outcome", result.stdout)

    def test_optional_skip_cannot_hide_required_skip(self):
        result = self.run_wizard(
            'record_skip "Required service"\nrecord_skip "Optional dashboard" optional\nfinish\n'
        )
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("Required service", result.stdout)
        self.assertIn("Optional dashboard", result.stdout)

    def test_unknown_requirement_is_rejected_before_remote_write(self):
        result = self.run_wizard(
            'gh() { printf "unexpected remote call"; return 0; }\n'
            'set_secret CI_TOKEN fake-private-value optinoal\nfinish\n'
        )
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertNotIn("unexpected remote call", result.stdout)

    def test_unauthenticated_required_step_is_incomplete(self):
        result = self.run_wizard('gh() { return 1; }\nset_var REGION local-test\nfinish\n')
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("Setup incomplete", result.stdout)


if __name__ == "__main__":
    unittest.main()
