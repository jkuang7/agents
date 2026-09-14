---
name: implement
description: Implement one assigned task as a verified candidate, without expanding its scope from parent work.
---

# Implement

Implement one assigned piece of work and return a verified candidate.

## Scope

The assigned ticket or task defines implementation scope. Read its parent spec or Epic for context, invariants, and constraints. Parent requirements constrain the current slice; they do not add work to it.

Build behavior from the parent only when a parent invariant requires that behavior for the current slice to be correct. Add the minimum needed now.

Before handoff, ask:

> Did I add behavior mainly because the parent will need it later?

If yes, remove or defer it unless the current task would otherwise be incorrect.

## Implementation

Use red → green → refactor, one small behavioral capability at a time.

Prefer the simplest correct design that fits the existing architecture. Keep cognitive load, coupling, implementation risk, and the cost of testing and review low.

Reuse existing seams and abstractions when they help. Introduce an abstraction only when it reduces total complexity for the current task by hiding a real boundary, removing meaningful duplication, reducing coupling, or improving testability.

When the internal design is uncertain, use the smallest useful tracer bullet to obtain evidence before choosing a broader structure. Implement directly when the design is clear and low-risk.

## Boundary check

Check the important boundaries and guarantees of the current slice before handoff. When correctness depends on a meaningful state boundary, ask:

> What event makes the new state true, and can downstream mutation happen before it?

Also ask:

> Could this implementation satisfy the visible tests or state while violating the underlying guarantee?

Address boundary problems supported by the current task and evidence. Do not expand the work around hypothetical failures.

## Commits

Use one or more commits. Group them by logical purpose. Keep commits small when that makes the change easier to review.

Before handoff, ask:

> Can a reviewer understand how the solution comes together by reading the commits in order?

Reorganize or squash only when it improves that review story.

## Finish

Run the repository's required checks on the final candidate. Report the delivered behavior, candidate revision or working-tree state, verification results, and any evidence gap.

Stop with the verified candidate. Publish, merge, close issues, or start another ticket only when the user requests it. Independent review remains a separate phase.
