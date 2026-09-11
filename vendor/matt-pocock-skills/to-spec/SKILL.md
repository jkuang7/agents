---
name: to-spec
description: "Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed."
---

# To spec

Write the smallest useful outcome that satisfies the user's intent and can be
verified. Base the contract on the conversation, repository evidence, and clear
correctness requirements. Reuse settled decisions instead of starting a design
interview.

Before tracker operations, follow the [issue tracker contract](../../../references/issue-tracker.md).

## Define the contract

Inspect the relevant code, domain terms, and architecture decisions. State the
user-visible problem and one complete outcome that addresses it.

Require only behavior justified by current evidence or the promised outcome.
Protect clear hazards such as concurrent writes, duplicate irreversible
actions, unsafe permissions, accepting the wrong revision, or reporting success
without complete evidence.

Prefer mechanical rules and observable states. Use fail-closed behavior when
stopping is safe and automatic recovery is not required. Leave retries, crash
recovery, reconciliation, scaling, and similar machinery out until evidence or
an explicit requirement calls for them.

Include an architecture constraint only when responsibility, ownership, or
dependency direction is part of the contract. Leave file layout, module shape,
and refactoring choices to implementation.

When revising a spec, use implementation or acceptance evidence to identify the
missing contract. Add the smallest requirement that closes the demonstrated
gap. Return a material change in scope, guarantees, or design to the user when
existing intent does not settle it.

## Define acceptance evidence

Name a realistic verification seam that proves the complete outcome. Prefer an
existing public or end-to-end seam when it is practical. A lower seam is enough
when it exercises the whole contract and would fail for a broken implementation.
Add focused cases for the correctness hazards and compatibility guarantees in
scope. Do not require an artificial end-to-end exercise that adds no proof.

## Write and publish

Use only the sections that add information:

<spec-template>

## Problem statement

Describe the problem from the user's perspective.

## Solution

Describe the smallest complete outcome and how the user can verify it.

## Acceptance requirements

Give observable requirements stable identifiers. Include required safeguards,
preserved behavior, and fail-closed outcomes.

## Implementation decisions

Record only binding mechanisms or architecture constraints. Include a compact
prototype-derived state machine, schema, or type shape when it states an
accepted decision more precisely than prose.

## Testing decisions

Name the verification seam and the cases that prove the contract.

## Unresolved decisions

State each consequential choice, the missing evidence or decision, and the work
it blocks. Omit this section when empty.

## Out of scope

List adjacent capabilities that the spec does not promise.

</spec-template>

Publish the spec to the configured tracker. Mark it `ready-for-agent` when its
requirements are settled. Otherwise use the configured pending-information
status and name the blocked work. Return the link and any unresolved decisions.
