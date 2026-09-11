"""Create disposable repositories for four observed workflow regressions."""

import argparse
from pathlib import Path
import subprocess
import tempfile


SKILLS = Path(__file__).resolve().parents[1] / "vendor" / "matt-pocock-skills"


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
    write(repo, "SPEC.md", "total(0) returns 0; total(n) returns 10*n for positive integers.\n")
    write(repo, "pricing.py", "def total(quantity):\n    return quantity * 10\n")
    base = commit(repo, "Initial pricing")
    write(repo, "pricing.py", "def total(quantity):\n    return max(1, quantity) * 10\n")
    write(repo, "tests/test_pricing.py", "import unittest\nfrom pricing import total\n\nclass PricingTests(unittest.TestCase):\n    def test_order(self):\n        self.assertEqual(total(2), 20)\n")
    return (
        f"Use {SKILLS / 'code-review' / 'SKILL.md'} to review the working tree in {repo}. "
        f"The base is {base}; SPEC.md is authoritative. Include pricing.py and tests/. "
        "Do not edit or stage files. Return the findings and candidate identity."
    )


def retirement(repo):
    write(repo, "legacy.py", "def charge(seen, request_id):\n    if request_id in seen:\n        return 0\n    seen.add(request_id)\n    return 10\n")
    write(repo, "billing.py", "class Checkout:\n    def __init__(self):\n        self._seen = set()\n\n    def pay(self, request_id):\n        if request_id in self._seen:\n            return 0\n        self._seen.add(request_id)\n        return 10\n")
    write(repo, "tests/test_legacy.py", "import unittest\nfrom legacy import charge\n\nclass ChargeTests(unittest.TestCase):\n    def test_duplicate(self):\n        seen = set()\n        self.assertEqual(charge(seen, 'r1'), 10)\n        self.assertEqual(charge(seen, 'r1'), 0)\n")
    write(repo, "tests/test_billing.py", "import unittest\nfrom billing import Checkout\n\nclass CheckoutTests(unittest.TestCase):\n    def test_payment(self):\n        self.assertEqual(Checkout().pay('r1'), 10)\n")
    commit(repo, "Candidate billing refactor")
    return (
        f"Use {SKILLS / 'codebase-design' / 'SKILL.md'} and its deepening reference "
        f"to assess deleting tests/test_legacy.py in {repo}. Checkout replaces legacy.charge "
        "and behavior must remain unchanged. Give a concrete recommendation without editing."
    )


def continuation(repo):
    write(repo, "SPEC.md", "normalize lowercases names.\n")
    write(repo, "names.py", "def normalize(value):\n    return value.lower()\n")
    write(repo, "tests/test_names.py", "import unittest\nfrom names import normalize\n\nclass NameTests(unittest.TestCase):\n    def test_name(self):\n        self.assertEqual(normalize('Alice'), 'alice')\n")
    old = commit(repo, "Lowercase names")
    write(repo, "SPEC.md", "normalize trims and lowercases names; blank names raise ValueError.\n")
    write(repo, "names.py", "def normalize(value):\n    return value.strip().lower()\n")
    commit(repo, "Update name handling")
    write(repo, "personal-notes.txt", "Unrelated user notes. Preserve this file.\n")
    write(repo, ".scratch/names/continuation.md", (
        f"# Continuation\n\nRecorded HEAD: {old}\nRequirements: SPEC.md\n"
        "Scope: names.py and tests/test_names.py\nVerification at recorded HEAD: unit tests passed.\n"
        "Preserve personal-notes.txt. Reconcile current state before resuming.\n"
    ))
    return (
        f"Use {SKILLS / 'handoff' / 'CONTINUATION.md'} to assess resuming from "
        f"{repo}/.scratch/names/continuation.md. Report the next safe action and which "
        "evidence still applies. Do not edit files."
    )


def routing(repo):
    write(repo, "SPEC.md", "Accepted change: normalize trims surrounding whitespace. The function is the agreed test seam.\n")
    write(repo, "names.py", "def normalize(value):\n    return value.lower()\n")
    commit(repo, "Existing utility")
    return (
        f"Use {SKILLS / 'ask-matt' / 'SKILL.md'} to recommend the next skill for {repo}. "
        "SPEC.md and its test seam are approved. Recommend the next step only."
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=["review", "retirement", "continuation", "routing"])
    args = parser.parse_args()
    root = Path(tempfile.mkdtemp(prefix=f"skill-{args.case}-"))
    repo = root / "repo"
    repo.mkdir()
    git(repo, "init", "-q")
    write(root, "task.md", globals()[args.case](repo) + "\n")
    print(root / "task.md")


if __name__ == "__main__":
    main()
