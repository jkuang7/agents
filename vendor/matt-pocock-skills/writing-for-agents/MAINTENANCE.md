# Evidence-based skill maintenance

Start from the failed outcome and its evidence. Put the correction at the
earliest owner that can prevent recurrence. Script failures belong in scripts;
judgment errors belong in the skill that makes the decision. Preserve the
user's intent and authorization boundaries.

Before adding a line, answer three questions:

1. Can code enforce it? Then put it in code, a script or a test instead.
2. Does a doc or another skill already own it? Then point to the owner.
3. What gets cut so the skill stays under the size limit?

Write the correction as a general rule, with its reason. Keep the incident
itself (issue and PR numbers, ADR numbers, commit SHAs, dates) in the commit
message or evaluation case, not in the skill. Those can be renumbered, deleted
or go stale, and the skill must still read correctly without them. Name a
repository's documents by role ("the README", "the runtime's result contract")
rather than by number. In this repository, `evals/test_skills.py` enforces
this, the size limit, one owner per passage, resolvable links and skill names,
and matching invocation settings across runtimes.

For a consequential failure that could recur, add one small behavioral case to
the collection's evaluation directory. In this repository, follow
`evals/README.md` at the repository root. Give an evaluator a realistic
request and only the artifacts needed to perform it. Keep the expected behavior
separate. Use a deterministic unit test when executable code can prove the
contract.

Record the failure and expected correction in the case itself. A result note is
useful only when it contains evidence needed to understand an unresolved limit.
Remove the case when the behavior no longer exists or a deterministic test
replaces it.

Complete the correction when the relevant case or test passes on the changed
artifact. State any remaining limit. Metadata validation alone does not prove a
behavioral change.
