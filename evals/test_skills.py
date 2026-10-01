"""Mechanical checks that keep skill text from drifting.

Each check guards a rule in
vendor/matt-pocock-skills/writing-for-agents/MAINTENANCE.md.
"""

from pathlib import Path
import difflib
import os
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCES = [ROOT / "skills", ROOT / "vendor/matt-pocock-skills"]
SIZE_LIMIT = 12 * 1024
DUPLICATE_WORDS = 12

SKILLS = {
    skill.parent.name: skill.parent
    for source in SOURCES
    for skill in source.glob("*/SKILL.md")
}

# Placeholder numbers that illustrate a format rather than cite a real item.
EXAMPLE_NUMBERS = {"#42", "#45", "#123", "ADR-0007"}

BRITTLE = [
    ("issue or PR number", re.compile(r"(?<![\w&/])#\d+\b")),
    ("issue or PR number", re.compile(r"\b(?:PR|issue|Issue|MR)\s+\d+\b")),
    ("ADR number", re.compile(r"\bADR[- ]?\d+\b|\badr/\d{3,}")),
    ("date", re.compile(r"\b20\d\d-[01]\d-[0-3]\d\b")),
    ("commit ID", re.compile(r"\b(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}\b")),
]

NAME = r"([a-z0-9]+(?:-[a-z0-9]+)*)"
SKILL_REFERENCE = re.compile(
    rf"\b(?:[Uu]se|[Rr]un|[Ii]nvoke|[Ll]oad|[Rr]oute to|[Hh]and off to|via)\s+`/?{NAME}`"
    rf"|`/?{NAME}`\s+skill"
    rf"|(?<![\w$])\${NAME}(?=[\s`'),:.]|$)",
    re.MULTILINE,
)
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^(```|~~~).*?^\1", re.MULTILINE | re.DOTALL)


def skill_files():
    for name, directory in sorted(SKILLS.items()):
        for path in sorted(directory.rglob("*")):
            if path.is_file() and path.suffix in {".md", ".yaml"}:
                yield name, path


def exists_exactly(directory, target):
    """Resolve a link with case-sensitive names, as Linux CI does."""
    current = directory
    for part in Path(target).parts:
        if part in {".", ".."}:
            current = current / part
        elif not current.is_dir() or part not in os.listdir(current):
            return False
        else:
            current = current / part
    return True


def without_fences(text):
    return FENCE.sub("", text)


def frontmatter(path):
    text = path.read_text()
    if not text.startswith("---\n"):
        return ""
    return text.split("\n---", 1)[0]


def passages(text):
    text = re.sub(r"`[^`]*`|\[([^\]]*)\]\([^)]*\)", r"\1", without_fences(text))
    words = re.findall(r"[a-z0-9']+", text.lower())
    for start in range(len(words) - DUPLICATE_WORDS + 1):
        yield " ".join(words[start : start + DUPLICATE_WORDS])


def relative(path):
    return path.relative_to(ROOT)


class SkillTextTests(unittest.TestCase):
    def test_no_brittle_references(self):
        problems = []
        for _, path in skill_files():
            for number, line in enumerate(path.read_text().splitlines(), 1):
                for label, pattern in BRITTLE:
                    for match in pattern.finditer(line):
                        if match.group(0) not in EXAMPLE_NUMBERS:
                            problems.append(f"{relative(path)}:{number}: {label} {match.group(0)!r}")
        self.assertEqual(problems, [], "Keep incidents in commits, not skills (MAINTENANCE.md)")

    def test_skill_size_limit(self):
        problems = [
            f"{relative(directory / 'SKILL.md')}: {size} bytes"
            for directory in SKILLS.values()
            if (size := (directory / "SKILL.md").stat().st_size) > SIZE_LIMIT
        ]
        self.assertEqual(problems, [], f"Cut each SKILL.md to {SIZE_LIMIT} bytes or less")

    def test_invocation_policy_matches_between_runtimes(self):
        problems = []
        for name, directory in SKILLS.items():
            manual = re.search(r"^disable-model-invocation:\s*true\s*$", frontmatter(directory / "SKILL.md"), re.MULTILINE)
            policy = directory / "agents/openai.yaml"
            text = policy.read_text() if policy.exists() else ""
            implicit_off = re.search(r"^\s*allow_implicit_invocation:\s*false\s*$", text, re.MULTILINE)
            if bool(manual) != bool(implicit_off):
                problems.append(
                    f"{name}: disable-model-invocation {'true' if manual else 'unset'} but "
                    f"allow_implicit_invocation {'false' if implicit_off else 'not false'}"
                )
        self.assertEqual(problems, [])

    def test_relative_links_resolve(self):
        problems = []
        for _, path in skill_files():
            for target in LINK.findall(without_fences(path.read_text())):
                if re.match(r"[a-z]+:|#", target):
                    continue
                if not exists_exactly(path.parent, target.split("#", 1)[0]):
                    problems.append(f"{relative(path)}: {target}")
        self.assertEqual(problems, [])

    def test_named_skills_exist(self):
        problems = []
        for _, path in skill_files():
            for match in SKILL_REFERENCE.finditer(without_fences(path.read_text())):
                name = next(group for group in match.groups() if group)
                if name in SKILLS:
                    continue
                # A one-word name may be a command such as `gh`; flag it only
                # when it looks like a misspelled or renamed skill.
                if "-" in name or difflib.get_close_matches(name, SKILLS, cutoff=0.75):
                    problems.append(f"{relative(path)}: {name}")
        self.assertEqual(problems, [])

    def test_no_passage_repeated_across_skills(self):
        owners = {}
        shared = {}
        for name, path in skill_files():
            if path.suffix != ".md":
                continue
            for passage in passages(path.read_text()):
                first = owners.setdefault(passage, (name, path))
                if first[0] != name:
                    shared.setdefault(f"{relative(first[1])} and {relative(path)}", passage)
        problems = [f"{files}: {passage!r}" for files, passage in shared.items()]
        self.assertEqual(problems, [], "Keep one owner per rule and point to it")


if __name__ == "__main__":
    unittest.main()
