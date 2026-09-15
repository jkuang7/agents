---
name: implement
description: Implement one assigned task as a verified candidate, without expanding its scope from parent work.
---

# Implement

Return a verified candidate for one assigned task.

## Scope

The assigned task defines scope. Read its parent spec or Epic for context, invariants, and constraints. Parent requirements constrain this slice; add parent behavior only when the slice would otherwise be incorrect. Before handoff, remove or defer behavior added mainly for later parent work.

## Method

Use `tdd` for red, green, and refactor cycles, one small behavioral capability at a time.

Prefer the simplest correct design that fits the architecture and reduces total cognitive load, coupling, implementation risk, and testing and review cost. Introduce abstractions only when they reduce that complexity for the current task.

When design is uncertain, use the smallest useful tracer bullet to obtain evidence before committing to broader structure. Implement directly when the design is clear and low risk.

## Boundary check

Verify the slice's important guarantees. For a meaningful state boundary, identify the event that makes the state true and ensure downstream mutation cannot precede it. Check whether visible tests or state could pass while the underlying guarantee fails. Address problems supported by requirements and evidence, without expanding scope around hypothetical failures.

## Finish

Group commits by logical purpose so a reviewer can understand how the solution comes together. Reorganize or squash only when it improves that story within existing authorization.

Run required repository checks on the final candidate. Report delivered behavior, candidate revision or working-tree state, verification, and evidence gaps.

Stop with the verified candidate. Independent review is a separate phase. Publish, merge, close issues, or start another ticket only when requested.
