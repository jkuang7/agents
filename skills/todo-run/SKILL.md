---
name: todo-run
description: Run planned checkbox tasks on the Todo page in Objective’s Backlog, tracking completion and blockers there. Use for /todo-run, “run my todos,” or “work the task list.” Capture and plan tasks with /todo.
---

# Todo run

Run planned tasks AFK until none remain. One **Todo** Task page in Objective is the checklist container; its root checkboxes are the individual work items. Do not create a database row for each checkbox or copy tasks to another tracker.

## Find the queue

Find and fetch the existing non-archived Task named **Todo** in the Objective database under Journal. If the container cannot be resolved uniquely, stop and report that /todo must repair it. Read its page content and process only root-level task checkboxes. Preserve all other content.

Run only one `/todo-run` session at a time. The running marker is not an atomic lock, so concurrent runs could duplicate work.

State is stored in each checkbox and its details block:

- `- [ ]` with no blocked status: ready or waiting on prerequisites.
- `Status: running`: claimed by a run that may have stopped; inspect its details and continue without repeating recorded side effects.
- `Status: blocked — reason`: unchecked and paused. Leave it blocked; continue with other runnable tasks. The user retries it by deleting that status line.
- `- [x]` plus `Result YYYY-MM-DD: ...`: complete. Keep it on the page.

Each task's collapsible details should contain Added, Goal, Done when, Route, After, and Decisions. The root checkbox title identifies the task. The Todo container remains Archive = No while it has active checklist items. Set its Status to In progress while work is running, Backlog when open tasks remain but none is running, Blocked when every unchecked item is blocked, and Done when every item is checked. If new tasks are added later, /todo resets Done or Blocked to Backlog. Confirm the Objective data source has Type, Archive, and Status and the required status options before changing properties; if not, stop and report the missing option. The container is an Objective Task page; do not create task rows for individual checkboxes.

## Run the queue

1. Read all task blocks and their plan lines. For an unplanned task, fill only missing plan lines using workspace instructions, the `route` skill and available evidence. If a user decision is needed, mark it blocked with `Status: blocked — needs you: <question>`.
2. Respect each `After` dependency. Run only after prerequisite checkboxes are complete. If a prerequisite is blocked, missing, or part of a cycle, mark this task blocked with the reason.
3. Before starting a task, re-read its block. If it remains unchecked and unblocked, set `Status: running` in that block and set the Todo container's database Status to In progress before doing work. If it is already checked or blocked, skip it.
4. Follow its plan and route. A user-specified route in the task's Decisions or Route line takes precedence where compatible with the `route` skill and authorization.
5. On completion, check the box and add a one-line `Result YYYY-MM-DD: ...` inside its details only when Done when is met. Put longer findings in the linked source page or a relevant artifact and summarize/link it in Result. If completion is not met after one retry, leave unchecked and replace running with `Status: blocked — <reason>`.
6. After a blocker, continue with independent runnable tasks. Re-fetch the page before each edit and update only the task block being changed, preserving concurrent edits and other task blocks. Re-scan the page after finishing a batch so newly added tasks are considered. Reconcile the container Status from the checkbox states before stopping: Done if all are checked; Blocked if every unchecked item is blocked; Backlog if unchecked work remains and none is running.

If an ambiguity has one clearly likeliest and reversible reading, proceed and record that reading in Result. Otherwise block with the specific question. Never leave work marked running when stopping. If an unplanned external side effect is needed, block the task and ask for the required decision instead of doing it. Spending money or messaging someone as the user requires explicit approval in Decisions. Do not treat read-only inspection, research, or drafting as approval to send or purchase.

## Routing

Route each task with the `route` skill. After a task blocks on an unavailable route, continue with the others. Independent non-screen tasks may run in parallel when the tools and environment support it.

For multi-issue coding work, follow the task's recorded decision: if the user approved starting `/specs`, complete it and report the Epic with “next: /babysit”; if the user chose `/babysit`, hand off there; if no path was approved, block and request planning rather than inventing a multi-issue workflow.

## Report

Report completed tasks first, then blocked tasks and what each needs. Include source or artifact links for longer results. If the queue has no runnable tasks, say so and stop.
