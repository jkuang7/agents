---
name: sandcastle-change-request
description: Record or update a focused requirement in an already-selected Sandcastle Epic child or standalone PR, then start or resume its trusted controller and confirm ownership.
---

# Sandcastle change request

Kickstart or resume one already-selected focused assignment through the existing trusted Sandcastle runtime. `to-spec` owns the delivery shape and contract. This skill validates and updates that exact authoritative target, then hands it to Sandcastle. After a successful handoff, the runtime owns implementation, review, verification, acceptance, publication, retries, recovery, and readiness; keep its procedures in [runtime.md](references/runtime.md).

Apply-and-resume requests authorize the tracker/PR updates and invocation below. Preparation-only requests stop before tracker, PR, controller, or delivery mutations.

## Require the selected assignment target

Resolve the target repository and follow its instructions and issue-tracker convention.

The request or approved context must identify exactly one authoritative assignment target:

- a specific selected Epic child assignment, whether newly published or existing; or
- a specific focused standalone PR.

Do not search for an Epic, select or create a child, choose standalone instead, or otherwise reinterpret the request into another delivery shape. If the target is missing or ambiguous, report that and stop.

Before changing the selected authority, use [runtime capability discovery](references/runtime.md#selected-target-capability-discovery) to verify that the current trusted operator supports that exact target and binding-source boundary. If support is absent or unproven, prepare only the smallest durable proposed update for the selected target, report the capability evidence, and stop. Do not mutate the authority, choose another shape, invent a controller loop, or add orchestration capability under this skill.

## Record and confirm the specification

Before editing an assignment owned by a live controller, use [controller stop and snapshot](references/runtime.md#controller-stop-and-snapshot) and wait for ownership release.

Apply the requested change to the selected authority only when needed. Record the complete scoped requirement, acceptance criteria, exclusions, and superseded requirements without rewriting an already-correct contract. Any parent constraint intended to bind an Epic child must be copied or restated in that child. Preserve other parent material separately as non-binding context; never enlarge the child's contract by inference.

- Epic mode: the selected unaccepted child issue is the complete binding contract. The parent supplies only non-binding context, rationale, and broader intent. Preserve accepted history and native child ordering.
- Standalone mode: the focused PR is the live specification authority. Runtime/bootstrap records may identify and observe it, but never copy or replace it as a second specification.

Read the authoritative specification back from the tracker or PR and confirm the selected child/PR and the runtime's actual canonical authority observation before invocation. Verify that the observation respects the selected binding-source boundary; do not prescribe an Epic projection the trusted runtime does not implement. A running worker is bound to the observed authority; later authoritative edits are handled by the runtime's fail-closed change detection.

If the runtime cannot consume the selected authoritative source, preserve the specification, report the unsupported handoff, and stop.

## Invoke the trusted flow

Invoke the trusted controller that matches the selected child or PR using [runtime.md](references/runtime.md). Do not switch modes when invocation fails. Confirm through the runtime's supported evidence that the controller accepted and acquired ownership of this delivery. Starting a process without establishing ownership is not a successful handoff.

After that confirmation, return control to the user. Do not supervise workers, reconstruct runtime state from the conversation, or wait for readiness. If the user explicitly asks to wait, watch, or attach, use [supported observation](references/runtime.md#controller-ownership-handoff-and-observation); observation does not transfer ownership back to this agent.

If launch fails or ownership cannot be established, preserve the authoritative assignment and report the failed handoff. If execution becomes unsupported after launch, use only the runtime's supported stop/recovery boundary. If an independently authorized runtime change must be activated first, use [operator activation and recovery](references/runtime.md#operator-activation-and-recovery); never activate an unverified candidate runtime.

Never merge the PR, advance `main`, close the Epic, or create another delivery path. Report the authoritative assignment, operator revision, and the evidence that ownership was accepted, or the evidence that prevented handoff.
