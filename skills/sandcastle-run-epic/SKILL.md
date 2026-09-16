---
name: sandcastle-run-epic
description: Start or resume an existing Sandcastle Epic through its trusted controller. Use for run, resume, or continue requests, including AFK execution and one-child limits. Requirement changes use the separate change-request workflow.
---

# Sandcastle run Epic

Hand an existing Epic to its trusted controller. Determine start or resume from durable state, confirm that Sandcastle acquired ownership, then return control to the user.

## 1. Select execution mode

Use `one-child` only for an explicit request for one child/subissue/slice/iteration, one issue at a time, or stopping after the next accepted child. Limit acceptance to at most one child.

Otherwise use `afk`: normal controller execution without a run limit.

## 2. Resolve the Epic and trusted runtime

Resolve one repository, follow workspace/repository instructions and the issue-tracker convention before tracker reads, and confirm the Epic exists and is open. Ask only if ownership remains ambiguous.

Establish the trusted operator revision, routing, delivery/worktree identity, durable accepted state, starting accepted HEAD, and controller ownership using [runtime.md](references/runtime.md). Unresolved identity, state, or ownership stops execution.

If the selected delivery already has a live controller, do not launch another. Confirm and report its ownership as the successful handoff unless the user explicitly asks to change or stop it through a supported controller interface.

Resolve and reuse the runtime-established cumulative PR, leaving creation to normal publication when accepted progress becomes publishable.

## 3. Invoke the existing controller once

For a new delivery, use the normal trusted Epic entry point. For an existing delivery, resume through current durable accepted state; already accepted children are not replayed.

Plain `resume` does not authorize retrying a durable block. Report it unless retry is explicitly authorized; use only supported retry, stop, and recovery interfaces in [runtime.md](references/runtime.md).

Invoke the current documented command once with limit `1` for `one-child`, or no limit for `afk`. Use the trusted operator even when the Epic changes Sandcastle itself. Candidate runtime code cannot activate itself.

Confirm through the runtime's supported evidence that the controller passed startup and acquired ownership of the selected Epic delivery. A process spawn, PID, lock file, or historical log alone is insufficient. If launch fails, the controller exits during startup, or ownership cannot be corroborated, preserve durable state and report a failed handoff.

After ownership is confirmed, return control to the user. Sandcastle owns implementation, review, verification, acceptance, publication, readiness, retries, recovery, and terminal stopping. The `one-child` limit configures the controller; it does not require this agent to wait for a child acceptance. Do not add an outer polling or relaunch loop, manual integration path, or duplicate controller logic.

## 4. Report the handoff

Report the Epic/repository, execution mode, trusted operator revision, starting accepted HEAD, and the supported evidence that the controller owns the selected delivery. If handoff failed, report the startup or ownership evidence that prevented it without claiming execution started.

Observation is a separate, explicit user-requested path. When asked to wait, watch, or attach, use only the current runtime's read-only Epic `--attach` or `--attach-worker` interface described in [runtime.md](references/runtime.md). Stopping an observer must not stop the controller or transfer execution ownership back to this agent.

## Scope boundary

Requirement changes belong to `sandcastle-change-request`. This skill must not create/edit implementation children, change Epic requirements, merge the PR, advance `main`, close the parent Epic, create another delivery branch or PR, or bypass durable blocks. Normal controller-owned progress notes, publication, and child closure remain part of execution.
