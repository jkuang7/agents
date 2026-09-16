---
name: sandcastle-run-epic
description: Start or resume an existing Sandcastle Epic through its trusted controller. Use for run, resume, or continue requests, including AFK execution and one-child limits. Requirement changes use the separate change-request workflow.
---

# Sandcastle run Epic

Execute an existing Epic through its trusted controller. Determine start or resume from durable state.

## 1. Select execution mode

Use `one-child` only for an explicit request for one child/subissue/slice/iteration, one issue at a time, or stopping after the next accepted child. Limit acceptance to at most one child.

Otherwise use `afk`: normal controller execution without a run limit, through its terminal condition.

## 2. Resolve the Epic and trusted runtime

Resolve one repository, follow workspace/repository instructions and the issue-tracker convention before tracker reads, and confirm the Epic exists and is open. Ask only if ownership remains ambiguous.

Establish the trusted operator revision, routing, delivery/worktree identity, durable accepted state, starting accepted HEAD, and controller ownership using [runtime.md](references/runtime.md). Unresolved identity, state, or ownership stops execution.

If the selected delivery already has a live controller, do not launch another. Report the active run and stop unless the user explicitly asks to change or stop it through a supported controller interface.

Resolve and reuse the runtime-established cumulative PR, leaving creation to normal publication when accepted progress becomes publishable.

## 3. Invoke the existing controller once

For a new delivery, use the normal trusted Epic entry point. For an existing delivery, resume through current durable accepted state; already accepted children are not replayed.

Plain `resume` does not authorize retrying a durable block. Report it unless retry is explicitly authorized; use only supported retry, stop, and recovery interfaces in [runtime.md](references/runtime.md).

Invoke the current documented command once with limit `1` for `one-child`, or no limit for `afk`. Use the trusted operator even when the Epic changes Sandcastle itself. Candidate runtime code cannot activate itself.

Observe through read-only interfaces until the terminal condition; stopping an observer does not stop the controller. Leave implementation, review, acceptance, publication, and readiness to Sandcastle. Honor terminal stops without manual integration, recreated controller logic, an outer loop, or automatic relaunch.

## 4. Report fresh results

At the terminal condition, read fresh evidence using [runtime.md](references/runtime.md) and report:

- Epic/repository and execution mode;
- starting and final accepted HEAD;
- children accepted during this invocation;
- stop/block reason;
- cumulative PR link and draft/ready state;
- trusted operator revision;
- whether work remains, including pending final approval.

State unavailable evidence explicitly; process exit alone proves no success. A block before acceptance is not a successful one-child run; report an intentional limit stop only when reached. For AFK, distinguish completed/ready, blocked, cancelled, retry/no-progress, and other fail-closed stops.

## Scope boundary

Requirement changes belong to `sandcastle-change-request`. This skill must not create/edit implementation children, change Epic requirements, merge the PR, advance `main`, close the parent Epic, create another delivery branch or PR, or bypass durable blocks. Normal controller-owned progress notes, publication, and child closure remain part of execution.
