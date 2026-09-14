---
name: to-spec
description: "Turn the current conversation into a lean, workflow-first spec and publish it to the project issue tracker."
disable-model-invocation: true
---
Turn the current conversation, codebase context, or existing issue into the **smallest complete specification of what must become true**.

The spec should be easy for a technically capable human to understand, review, and judge for correctness.

Do not turn implementation choices into product requirements.

Use judgment. Do not perform every check mechanically.

## Process

1. Identify the user's governing outcome, then understand the current behavior, important invariants, and how success will be verified.

   Inspect code only if the existing conversation or issue does not already establish the relevant behavior.

   Let the governing outcome set the contract's emphasis. For example, an unattended workflow needs a complete path to success or a useful human handoff, while an operator-driven workflow may stop safely between steps.
2. Converge on the smallest sufficient contract.

   Ask:

   > Could a reasonable implementer build the right thing without inventing important product behavior?
   >

   If yes, stop looking for gaps.

   If no, surface only the ambiguity that prevents convergence.

   Prefer one workflow-level rule that covers a class of cases over separate requirements for each possible event.
3. Consider only failure behavior that poses a high risk to the governing outcome.

   A failure concern earns a place when it could prevent required progress, corrupt accepted work, or report success without sufficient evidence, and the existing contract does not already determine the outcome.

   For unattended orchestration, first define when work continues, when it stops for a person, what failed work must not advance, and the safe restart boundary. Use those general rules to cover retry and recovery concerns. Add a specific failure case only when those rules do not settle it.

   Stay at the behavioral level. Specify retry systems, persistence schemes, recovery protocols, reconciliation logic, state machines, or other implementation machinery only when the mechanism itself is required.
4.  When a consequential decision is needed, ask it simply:

   **Question:** what behavior is unclear?
   **Recommendation:** the simplest behavior that preserves the goal.
   **Why:** one short sentence.

   When resolving a gap, describe the behavior that must be true, not the mechanism used to implement it.

   Prefer:

   > The runner must not declare the project complete if it cannot safely account for changes to the task set.
   >

   over:

   > Reload the child set before publication and compare it with persisted membership.
   >

   Only specify the mechanism when the mechanism itself is part of the requirement.

   Prefer an existing invariant or general workflow rule if it already determines the outcome. Add a new rule only if the contract would otherwise remain ambiguous.

   Do not manufacture additional questions once the contract is sufficient.
5. Write or revise the spec only after consequential decisions are resolved.

   Keep it lean, clear, and implementation-agnostic wherever possible.
6. Define testing decisions only if they add useful guidance.

   Prefer observable behavior at stable system boundaries over tests coupled to internal representation.
7. If reviewing an existing issue, show suggested changes first.

   Do not edit, replace, or create issues unless the user explicitly asks.
8. If creating a new spec, show the draft before publishing.

## Spec

Use only sections that earn their place.

### Problem

What happens today and why it is insufficient.

### Desired Outcome

What must become true.

### User Stories

Why important guarantees matter.

### Core Invariants

What must never be violated.

### Testing Decisions

How required behavior will be proven through observable behavior.

### Review / Verification

Any additional trust or whole-system verification boundary beyond normal testing.

### Acceptance Criteria

Observable evidence that proves completion.

### Constraints

Existing behavior or boundaries that must be preserved.

### Out of Scope

Plausible adjacent work that is not part of the change.

Do not repeat the same requirement across sections.

Before presenting the spec, ask:

> Is the contract sufficient to guide implementation correctly?

If yes, stop adding detail.

Then ask:

> What can be removed without weakening the required outcome?

Remove it.
