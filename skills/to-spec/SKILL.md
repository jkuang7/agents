---
name: to-spec
description: "Turn the current conversation into a lean, workflow-first spec and publish it to the project issue tracker."
disable-model-invocation: true
---

# To spec

Turn accepted conversation, codebase context, or an existing issue into the smallest complete specification of what must become true. A technically capable human should understand and judge it on first read.

## Converge on the contract

1. Establish the governing outcome, current behavior, important invariants, and observable success. Inspect code only where existing context is insufficient. Let the outcome set emphasis: unattended work needs a complete path to success or a useful human handoff; operator-driven work may stop safely between steps.
2. Resolve only consequential ambiguity that would force an implementer to invent product behavior. Ask for the unclear behavior with a simple recommendation and short reason. Prefer an existing invariant or one workflow rule covering a class of cases.
3. Include failure behavior only when it could prevent required progress, corrupt accepted work, or falsely report success, and the contract does not already settle it. For unattended orchestration, define continuation, human stopping conditions, what failed work cannot advance, and the safe restart boundary before adding specific recovery cases.
4. Write once consequential decisions are resolved. Preserve opinionated requirements; leave implementation mechanisms open unless the mechanism itself is required. Specify testing decisions only when they add useful guidance, favoring observable behavior at stable system boundaries.

The contract is sufficient when a reasonable implementer can build the right behavior without inventing important requirements. Stop looking for gaps then, and remove detail that does not strengthen the required outcome.

## Write and publish

Use only sections that earn their place: problem, desired outcome, user stories, core invariants, testing decisions, additional review or verification boundaries, acceptance criteria, constraints, and out of scope. Each requirement has one home.

For an existing issue, show proposed changes first; edit, replace, or create issues only when explicitly requested. Show a new spec draft before publishing. Resolve repository instructions and tracker policy before tracker operations.
