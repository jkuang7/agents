"""Create local, disposable inputs for skill judgment evaluations."""

import argparse
from pathlib import Path
import subprocess
import tempfile


def write(root, name, content):
    target = root / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content)


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), "-c", "core.hooksPath=/dev/null",
         "-c", "commit.gpgsign=false", "-c", "user.name=Skill evaluation",
         "-c", "user.email=evaluation@example.invalid", *args],
        text=True, capture_output=True, check=True,
    ).stdout.strip()


def commit(repo, message):
    git(repo, "add", ".")
    git(repo, "commit", "-qm", message)
    return git(repo, "rev-parse", "HEAD")


def review(repo):
    write(repo, "SPEC.md", "Quantity pricing: total(0) must return 0; total(n) must return 10*n for positive integers.\n")
    write(repo, "pricing.py", "def total(quantity):\n    return quantity * 10\n")
    base = commit(repo, "Initial pricing")
    write(repo, "pricing.py", "def total(quantity):\n    return max(1, quantity) * 10\n")
    write(repo, "tests/test_pricing.py", "import unittest\nfrom pricing import total\n\nclass PricingTests(unittest.TestCase):\n    def test_order(self):\n        self.assertEqual(total(2), 20)\n")
    return (
        f"Use the installed code-review skill to review the current working-tree changes in {repo}. "
        f"The base is {base}; SPEC.md is the accepted requirement. "
        "The scope is pricing.py and tests/. Do not edit or stage source files. "
        "You may run local checks and save review evidence outside the repository. "
        "Return your review and identify its candidate. If subagents are unavailable, disclose that limit."
    )


def retirement(repo):
    write(repo, "legacy.py", "def charge(seen, request_id):\n    if request_id in seen:\n        return 0\n    seen.add(request_id)\n    return 10\n")
    write(repo, "billing.py", "class Checkout:\n    def __init__(self):\n        self._seen = set()\n\n    def pay(self, request_id):\n        if request_id in self._seen:\n            return 0\n        self._seen.add(request_id)\n        return 10\n")
    write(repo, "tests/test_legacy.py", "import unittest\nfrom legacy import charge\n\nclass ChargeTests(unittest.TestCase):\n    def test_request_is_charged_once(self):\n        seen = set()\n        self.assertEqual(charge(seen, 'request-1'), 10)\n        self.assertEqual(charge(seen, 'request-1'), 0)\n")
    write(repo, "tests/test_billing.py", "import unittest\nfrom billing import Checkout\n\nclass CheckoutTests(unittest.TestCase):\n    def test_payment(self):\n        self.assertEqual(Checkout().pay('request-1'), 10)\n")
    commit(repo, "Candidate billing refactor")
    return (
        f"Use codebase-design and its deepening reference to assess this test-retirement proposal in {repo}: "
        "Checkout is the new public interface replacing legacy.charge. We propose deleting tests/test_legacy.py "
        "because tests/test_billing.py now exists. The behavior must remain unchanged. "
        "Give a concrete recommendation based on the repository. Do not edit files."
    )


def continuation(repo):
    write(repo, "SPEC.md", "normalize lowercases names.\n")
    write(repo, "names.py", "def normalize(value):\n    return value.lower()\n")
    write(repo, "tests/test_names.py", "import unittest\nfrom names import normalize\n\nclass NameTests(unittest.TestCase):\n    def test_name(self):\n        self.assertEqual(normalize('Alice'), 'alice')\n")
    old = commit(repo, "Lowercase names")
    check = subprocess.run(
        ["python3", "-B", "-m", "unittest", "discover", "-s", "tests"],
        cwd=repo, text=True, capture_output=True, check=True,
    )
    branch = git(repo, "branch", "--show-current")
    write(repo, "SPEC.md", "normalize trims surrounding whitespace and lowercases names. It must reject blank names with ValueError.\n")
    write(repo, "names.py", "def normalize(value):\n    return value.strip().lower()\n")
    commit(repo, "Update name handling")
    write(repo, "personal-notes.txt", "Unrelated notes owned by the user. Preserve this file.\n")
    write(repo, ".scratch/names/continuation.md", (
        f"# Names continuation\n\nRepository: {repo}\nBranch: {branch}\nRecorded HEAD and review base: {old}\n"
        "Requirements: SPEC.md. Scope: names.py and tests/test_names.py.\n"
        "Completed: lowercasing. Verification: python3 -B -m unittest discover -s tests, exit 0.\n"
        f"Observed output:\n```\n{check.stderr.strip()}\n```\n"
        "Unrelated work: preserve personal-notes.txt if present.\n"
        "Next action: reconcile current requirements and checkout, then finish the names task.\n"
    ))
    return (
        f"Use the continuation guidance at /Users/jian/.codex/skills/handoff/CONTINUATION.md "
        f"to resume from {repo}/.scratch/names/continuation.md. "
        "Inspect the repository and report the next safe action and which existing evidence applies. "
        "This is a read-only resume assessment; do not change files or commit."
    )


def routing(repo):
    write(repo, "SPEC.md", "Accepted change: normalize trims leading and trailing whitespace. The normalize function is the agreed public test seam. No API expansion or publication is requested.\n")
    write(repo, "names.py", "def normalize(value):\n    return value.lower()\n")
    commit(repo, "Existing names utility")
    return (
        f"Use ask-matt to recommend the next skill for {repo}. "
        "I have approved SPEC.md and its test seam. This is a small change in the existing function. "
        "Recommend the next step only; do not implement it or publish anything."
    )


def vertical_slices(repo):
    write(repo, "SPEC.md", (
        "An operator starts a run from discovered work. The run accepts its first completed child, "
        "publishes accepted progress to one draft pull request, and resumes that accepted progress safely "
        "after a process restart. The controller then repairs concrete controller or CI defects and reruns "
        "the affected work. Finally, it audits the exact candidate and marks that candidate ready. The "
        "complete workflow must then be proven in a disposable Epic on a real hosting service. Creating "
        "that Epic requires explicit authorization, and no disposable repository has been provisioned.\n"
    ))
    write(repo, "ARCHITECTURE.md", (
        "Likely responsibilities: inventory, run state, persistence, child acceptance, restart recovery, "
        "pull request publication, GitHub reconciliation, correction state, CI recovery, and final audit. "
        "Each responsibility can be tested independently. One possible plan puts every responsibility in "
        "one implementation ticket because they occur in one controller workflow. Another possible plan "
        "blocks audit and readiness implementation until a real disposable Epic is authorized, even though "
        "local fixtures can verify the audit and readiness behavior.\n"
    ))
    commit(repo, "Describe run workflow")
    return (
        f"Use the installed to-tickets skill to propose a ticket breakdown for {repo}/SPEC.md. "
        f"Use {repo}/ARCHITECTURE.md as codebase context. Present the proposed breakdown only. "
        "Do not publish tickets or edit files. The breakdown should be small enough for fresh-context "
        "implementation workers while preserving useful end-to-end progress after every ticket."
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=["review", "retirement", "continuation", "routing", "vertical_slices"])
    args = parser.parse_args()
    root = Path(tempfile.mkdtemp(prefix=f"skill-{args.case}-"))
    repo = root / "repo"
    repo.mkdir()
    git(repo, "init", "-q")
    task = globals()[args.case](repo)
    write(root, "task.md", task + "\n")
    print(root / "task.md")


if __name__ == "__main__":
    main()
