---
name: sandcastle-change-request
description: Record a focused Sandcastle requirement in the correct Epic child or supported standalone PR, then start or resume the trusted flow; prepare only when execution support is unproven.
---

# Sandcastle change request

Kickstart or resume one focused assignment through the existing trusted Sandcastle runtime. The runtime owns implementation, review, verification, acceptance, retries, recovery, and readiness; keep their procedures in [runtime.md](references/runtime.md).

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

Record the complete scoped requirement, acceptance criteria, exclusions, and superseded requirements in the authoritative assignment source. Identify applicable parent constraints without duplicating them unless the child must explicitly specialize or supersede them.

- Epic mode: the selected unaccepted child issue. The parent supplies context and applicable constraints, not additional assignment scope. Preserve accepted history and native child ordering.
- Standalone mode: the focused PR specification. Runtime/bootstrap records may snapshot or reference it, but never replace it as authority.

Read the authoritative specification back from the tracker or PR and confirm the selected child/PR, current revision, and execution support before invocation. A running worker is bound to the observed authoritative revision; later edits are handled by the runtime's fail-closed revision-change behavior.

If the runtime cannot consume the selected authoritative source, preserve the specification, report the unsupported handoff, and stop.

## Invoke the trusted flow

Invoke the existing Epic resume entry point or established standalone entry point from [runtime.md](references/runtime.md). Do not reproduce controller, review, verification, retry, recovery, acceptance, or readiness procedures in this skill.

If execution becomes unsupported, stop the selected controller safely, preserve the assignment, and report the handoff. If an independently authorized runtime change must be activated first, use [operator activation and recovery](references/runtime.md#operator-activation-and-recovery); never activate an unverified candidate runtime.

Stop when the runtime reports readiness or a durable stop. Never merge the PR, advance `main`, close the Epic, or create another delivery path. Report the authoritative assignment, ownership rationale, operator revision, and resulting runtime state.
