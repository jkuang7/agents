---
name: to-tickets
description: Break a plan, spec, or the current conversation into tracer-bullet tickets, published to the configured tracker with blocking dependencies and native sub-issue links to an existing parent spec.
---

# To tickets

Turn an accepted contract into the fewest coherent tracer-bullet tickets. Each
ticket must make a new part of the parent workflow work and name what blocks it.

Before tracker operations, follow the [issue tracker contract](../../../references/issue-tracker.md).
Write ticket bodies in plain prose and short lists. Do not use tables.

## Gather the contract

Read the supplied spec, plan, or issue, including comments. For an existing
parent issue, refresh it before drafting children. Inspect the relevant code,
domain terms, architecture decisions, and tests unless current evidence already
establishes them.

Treat the accepted spec as authoritative. Reconcile later human decisions into
it when existing authorization permits. Ask only about a consequential choice
that changes observable behavior, scope, safety, or an accepted constraint.
Resolve factual questions from code or service contracts. Leave internal design
choices to implementation when the contract already defines correctness.

## Choose slices

For every proposed ticket, answer both questions:

- What new part of the parent workflow works after this ticket?
- Is this one coherent behavioral step for a fresh implementation context?

Fold an internal prerequisite into the first slice that uses it. Separate it
only when it is independently useful, several approved slices need it, or it
cannot fit safely in the consuming slice. Split a ticket when it combines
independent workflow milestones with different failure modes, external
boundaries, or verification stories.

Use behavioral milestones instead of modules or acceptance-criterion counts.
A backend-only slice is valid when it delivers observable behavior. Context size
matters after the behavioral boundary is clear; it does not justify horizontal
foundation tickets.

If a shared interface cannot migrate through independently passing slices, read
[wide refactors](references/WIDE-REFACTORS.md) before choosing the sequence.

## Keep implementation separate from gated proof

Distinguish code needed to build the behavior from external conditions needed
only to prove it in a live environment. If local tests or fixtures can verify
the implementation, keep that ticket executable. Put an authorized live trial
in a later validation ticket and name its required credential, environment, or
test target as an external prerequisite.

Keep live proof in the implementation ticket only when the real environment is
necessary to build or meaningfully verify the behavior.

## Preserve the parent contract

Carry every parent requirement, invariant, safeguard, and proof obligation into
the slice that implements or verifies it. Do not add retries, recovery,
reconciliation, architecture constraints, or project-management checkpoints
that the parent does not require.

Use intentional fixtures or known cases for required failure paths. State an
uncontrollable verification gap instead of treating an accidental occurrence as
proof.

For each ticket, record its blocking ticket edges. Keep external prerequisites
separate. Do not mark implementation ready while a human decision or factual
investigation still defines what correct behavior means.

## Review and publish

Before publication, account for every parent requirement and apply all slice,
proof-gating, and dependency rules above. Fix any mismatch in the proposed
graph.

Create children in dependency order and add native sub-issue links when the
tracker supports them. Use canonical issue references for dependencies. After
publication, read the parent and children back, verify links and labels, and fix
any mismatch. Return the parent link, child links in execution order, blocking
edges, external prerequisites, and deferred work.

Use this ticket shape, omitting sections that add nothing:

<ticket-template>

## Parent

Link the existing parent spec.

## Context and current behavior

Describe one concrete action, what happens now, and the relevant cause.

## Intended change

Describe what will work after this ticket and what behavior remains unchanged.

## Acceptance criteria

- [ ] State observable success and the evidence that distinguishes it from failure.
- [ ] Include applicable failure behavior and safeguards.

## Implementation discovery

Record open internal choices and the contract they must preserve. For an
investigation, state the question, evidence to gather, and completion condition.

## Blocked by

List prerequisite tickets or state that there are none. Name external
prerequisites separately.

</ticket-template>
