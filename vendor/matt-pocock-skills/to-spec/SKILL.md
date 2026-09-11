---
name: to-spec
description: "Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed."
---

Specify the smallest useful end-to-end outcome the user can verify and learn from. Require only what current evidence, the user-visible outcome, or clear correctness requirements justify. Synthesize the conversation and relevant codebase evidence. Reuse settled intent and authorization instead of running a general design interview.

Prefer mechanically defined requirements. Express a rule as a concrete observable state when that avoids semantic interpretation. For example, define a correction cycle by one observed failure, its verification condition, and a fixed attempt budget that ends on pass or exhaustion. Introduce identities such as a "same blocker," "equivalent failure," or "renamed finding" only when the product contract requires them.

For work under `/Volumes/T9/Dev/repos`, resolve the target repository and read [the shared issue-tracker convention](/Volumes/T9/Dev/docs/agents/issue-tracker.md) and [triage label mappings](/Volumes/T9/Dev/docs/agents/triage-labels.md) before tracker operations. Apply any target repository overrides from its `AGENTS.md` or `CLAUDE.md`. Elsewhere, use the project's configured tracker and labels; if missing, establish them before publishing.

## Process

1. Identify the concrete problem and the smallest complete end-to-end outcome that addresses it. State how the user will verify the outcome and what they will learn from it. Explore relevant code, domain vocabulary, and ADRs to confirm that boundary is feasible.

2. Include obvious correctness hazards in the initial spec when the outcome clearly requires them. These can include concurrent mutation of the same state, duplicate irreversible actions, accepting or publishing the wrong revision, loss or replay of accepted work, unsafe permissions, and claiming completion from incomplete evidence. A narrow scope must still preserve the security, data integrity, concurrency safety, and correctness guarantees required by the outcome.

   Keep recovery, retries, rate-limit handling, crash reconstruction, reconciliation, and similar machinery out of the contract until current evidence or an explicit requirement justifies it. When work can stop safely, a fail-closed result such as `BLOCKED` may be the complete requirement. Keep accepted decisions distinct from proposals and unresolved questions.

3. Include an architecture constraint only when it is important enough to be part of the outcome's contract. State the responsibility, ownership boundary, dependency direction, or high-level workflow that implementations must preserve. Leave exact files, modules, refactors, directory structures, and code organization to implementation.

4. Define acceptance evidence. Include at least one realistic end-to-end verification of the proposed outcome. Add focused tests only for correctness hazards, fail-closed behavior, and compatibility guarantees that are part of the contract. Prefer existing public seams and the highest seam that discriminates the required behavior.

5. When revising an existing spec, use concrete implementation or end-to-end evidence to determine whether the contract is missing a requirement. Add only the smallest requirement needed to address a demonstrated gap. Leave ordinary implementation details and hypothetical failures out of the spec.

6. Write only the detail needed to state and verify the contract, using the template below. Reuse previously agreed seams and authorization. Clarify only a consequential new choice that existing intent does not settle.

   Publish the bounded spec to the project issue tracker. Apply `ready-for-agent` when consequential requirements are settled; otherwise use the configured pending-information status and identify the blocked work. Publication and labels do not establish design approval or suitability for a particular executor. Return the publication link and unresolved decisions.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The smallest useful end-to-end outcome, from the user's perspective, and how the user can verify it.

## User Stories

Include distinct user stories only when they clarify behavior beyond the solution and acceptance requirements.

## Acceptance Requirements

Give observable requirements stable identifiers. State the obvious correctness properties and fail-closed outcomes required for this result. Include preservation and compatibility guarantees only when the outcome depends on them. Exclude speculative recovery behavior.

## Implementation Decisions

Include only implementation decisions necessary for correctness or architecture constraints important enough to be part of the contract. State binding responsibilities, boundaries, or mechanisms, with the evidence and rationale for consequential constraints. Leave exact files, modules, refactors, and code organization to implementation.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.

## Testing Decisions

Describe a realistic end-to-end verification of the proposed outcome as acceptance evidence. Add tests that discriminate obvious correctness hazards, required refusal or fail-closed behavior, and compatibility guarantees in the contract. Name existing test seams and relevant prior art. Do not specify tests for recovery behavior the contract does not promise.

## Unresolved Decisions

Omit when empty. Separate factual investigation from a consequential choice requiring human input. State the missing evidence or decision, its completion condition, and the requirements it blocks.

## Out of Scope

List adjacent capabilities outside this spec. When relevant, explicitly defer recovery, automation, scaling, retry, or resilience machinery.

## Further Notes

Omit unless needed to implement or verify this outcome.

</spec-template>
