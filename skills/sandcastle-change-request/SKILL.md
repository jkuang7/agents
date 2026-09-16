---
name: sandcastle-change-request
description: Record a focused Sandcastle requirement in the correct Epic child or supported standalone PR, then start or resume the trusted flow; prepare only when execution support is unproven.
---

# Sandcastle change request

Kickstart or resume one focused assignment through the existing trusted Sandcastle runtime. After a successful handoff, the runtime owns implementation, review, verification, acceptance, publication, retries, recovery, and readiness; keep its procedures in [runtime.md](references/runtime.md).

Apply-and-resume requests authorize the tracker/PR updates and invocation below. Preparation-only requests stop before tracker, PR, controller, or delivery mutations.

## Select the assignment path

Resolve the target repository and follow its instructions and issue-tracker convention.

- Use a user-specified Epic. Otherwise prefer one clearly relevant active Epic; never create an Epic merely to access Sandcastle.
- For Epic work, select one matching unaccepted child or create one focused child for new work or a change to accepted behavior.
- Without a relevant Epic, use [standalone capability discovery](references/runtime.md#standalone-capability-discovery). Proceed only when the current trusted operator proves the supported entry point and revision.
- For supported standalone work, reuse or create one focused PR as the authoritative specification, then invoke the supported standalone runtime against that PR using the entry point from [runtime.md](references/runtime.md). Add an issue only when repository policy requires it.

If standalone execution is absent or unproven, prepare the smallest durable specification or draft change record supported by the repository, report the capability evidence, and stop. Do not invent a controller loop or add orchestration capability under this skill.

## Record and confirm the specification

Before editing an assignment owned by a live controller, use [controller stop and snapshot](references/runtime.md#controller-stop-and-snapshot) and wait for ownership release.

Record the complete scoped requirement, acceptance criteria, exclusions, and superseded requirements in the authoritative assignment source. Any parent constraint intended to bind an Epic child must be copied or restated in that child. Preserve other parent material separately as non-binding context; never enlarge the child's contract by inference.

- Epic mode: the selected unaccepted child issue is the complete binding contract. The parent supplies only non-binding context, rationale, and broader intent. Preserve accepted history and native child ordering.
- Standalone mode: the focused PR is the live specification authority. Runtime/bootstrap records may identify and observe it, but never copy or replace it as a second specification.

Read the authoritative specification back from the tracker or PR and confirm the selected child/PR, the runtime's current canonical authority observation, and execution support before invocation. A running worker is bound to that observation; later authoritative edits are handled by the runtime's fail-closed change detection.

If the runtime cannot consume the selected authoritative source, preserve the specification, report the unsupported handoff, and stop.

## Invoke the trusted flow

Invoke the existing Epic resume entry point or established standalone entry point from [runtime.md](references/runtime.md). Confirm through the runtime's supported evidence that the controller accepted and acquired ownership of this delivery. Starting a process without establishing ownership is not a successful handoff.

After that confirmation, return control to the user. Do not supervise workers, reconstruct runtime state from the conversation, or wait for readiness. If the user explicitly asks to wait, watch, or attach, use [supported observation](references/runtime.md#controller-ownership-handoff-and-observation); observation does not transfer ownership back to this agent.

If launch fails or ownership cannot be established, preserve the authoritative assignment and report the failed handoff. If execution becomes unsupported after launch, use only the runtime's supported stop/recovery boundary. If an independently authorized runtime change must be activated first, use [operator activation and recovery](references/runtime.md#operator-activation-and-recovery); never activate an unverified candidate runtime.

Never merge the PR, advance `main`, close the Epic, or create another delivery path. Report the authoritative assignment, operator revision, and the evidence that ownership was accepted, or the evidence that prevented handoff.
