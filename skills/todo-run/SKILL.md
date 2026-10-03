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

Keep root checkboxes in execution order. Re-evaluate the order when new tasks arrive, a blocker or prerequisite changes, or a task completes. Respect explicit user ordering and `After` dependencies first; then prioritize work that unblocks multiple tasks or the queue, batch compatible work sharing a repo/source/account/setup/screen route to reduce context switching, do foundations before dependent conclusions, and avoid rework. Use the existing order as a tiebreaker. Never group work across permission boundaries or run more than one screen-based task at once. Reorder whole checkbox/details blocks without changing their contents or statuses; keep unchecked work ahead of checked history, preserving completed items' relative order.

## Run the queue

1. Read all task blocks and their plan lines. For an unplanned task, fill only missing plan lines using workspace instructions and available evidence. If a user decision is needed, mark it blocked with `Status: blocked — needs you: <question>`. Order the unchecked queue using the rule above before selecting work.
2. Respect each `After` dependency. Run only after prerequisite checkboxes are complete. If a prerequisite is blocked, missing, or part of a cycle, mark this task blocked with the reason.
3. Before starting a task, re-read its block. If it remains unchecked and unblocked, set `Status: running` in that block and set the Todo container's database Status to In progress before doing work. If it is already checked or blocked, skip it.
4. Follow its plan and route, using the canonical routing file (see Routing). A user-specified route in the task's Decisions or Route line takes precedence where compatible with higher-level routing and authorization. Resolve the route before doing the work; the model running `/todo-run` is not automatically the right worker for every checkbox. Use the specified app or model (for example, Muse, Codex, or Claude) and its required authorization. Do not silently substitute the current session model when the selected route is available. If the required route is unavailable, block only this checkbox with the specific reason and continue the queue. If a task describes a product (for example, a Claude artifact), that alone does not select its maker as the worker.
5. On completion, check the box and add a one-line `Result YYYY-MM-DD: ...` inside its details only when Done when is met. Put longer findings in the linked source page or a relevant artifact and summarize/link it in Result. If completion is not met after one retry, leave unchecked and replace running with `Status: blocked — <reason>`.
6. A blocker pauses only that checkbox. Immediately re-scan for and start the next independent runnable checkbox; do not stop the run while runnable unchecked work remains. When a task is waiting on a long-running route or a subagent, use the available time to advance independent work, subject to the one-screen-task limit below. Re-fetch the page before each edit and update only the task block being changed, preserving concurrent edits and other task blocks. Re-scan after each completion or blocker so newly added or newly unblocked tasks are considered. Stop only when all checkboxes are complete or every unchecked checkbox is blocked or waiting on an incomplete prerequisite. Reconcile the container Status from the checkbox states before stopping: Done if all are checked; Blocked if every unchecked item is blocked; Backlog if unchecked work remains and none is running.

If an ambiguity has one clearly likeliest and reversible reading, proceed and record that reading in Result. Otherwise block with the specific question. Never leave work marked running when stopping. If an unplanned external side effect is needed, block the task and ask for the required decision instead of doing it. Spending money or messaging someone as the user requires explicit approval in Decisions. Do not treat read-only inspection, research, or drafting as approval to send or purchase.

## Routing

`/Volumes/T9/Dev/repos/agent-hub/router/preferences.md` is the canonical routing file: worker and model, browser, screen routes, and personal-source lookup. Read it when resolving a task's route or source, and record the resolved route and any source plan in the task's Route or Decisions. Workspace and repository `AGENTS.md` win where they conflict. Todo-run adds one limit: screen routes run only when the task's Decisions allow use while the user is away (otherwise block the task with that question), and one at a time.

For multi-issue coding work, follow the task's recorded decision: if the user approved starting `/specs`, complete it and report the Epic with “next: /babysit”; if the user chose `/babysit`, hand off there; if no path was approved, block and request planning rather than inventing a multi-issue workflow.

## Parallel work

Dispatch independent non-screen tasks to subagents when the environment supports it and running them at once saves time; do tiny tasks directly. A task is independent when its `After` prerequisites are complete and it writes no working files that running work writes; code tasks in the same repository may run together only in separate worktrees under that repository's `.worktrees/`. Give each subagent its task's Goal, Done when, Decisions, and source links; subagents never open a browser, and the parent runs browser steps. A task keeps its recorded Route: an app route such as Codex runs there, and screen routes, including Codex computer use, stay with the parent. Otherwise choose the agent type and model from the Route and the workspace `AGENTS.md` routing rules, such as `worker` for decided work, `Explore` for search, and `advisor` for judgment; never default every task to one model (such as Luna) or to the session's own model.

The parent alone claims tasks, edits the Todo page, and records results. Set `Status: running` before dispatch, and track each dispatched checkbox title with its agent until the result arrives; skip these tasks when re-scanning. Subagents return results and never edit the page. Check Done when against the returned result before checking the box. A subagent that needs a user decision, spending, or messaging as the user returns that need, and the parent blocks the task with that question under the approval rules above. While work runs, re-scan the queue and start other runnable tasks; when one task blocks or fails, mark only that task and keep the rest going. Do not stop or reconcile the container Status until every dispatched task has returned. Screen routes share one screen, so they run one at a time and never alongside another screen task.

## Report

End each run with a short report under three headings. Give each task one or two plain sentences, so length grows with the task count rather than a fixed line limit:

- **Completed:** each task finished this run, its concrete result, and what that means for the user. List tasks that were already complete before this run separately, so they are not mistaken for new work.
- **Blocked:** each unfinished task, what remains undone, the blocker, and the action that unblocks it. Group tasks that share a blocker under it, naming every affected task.
- **Next:** specific next steps in priority order, each with its purpose.

For any failed or blocked step, state what was attempted, the observed failure or error, the cause only as far as evidence shows it, and the recovery action. If the root cause is unknown, say so and label any guess as a hypothesis; a failed tool action alone does not establish a technical cause. Keep this to task-level context, not logs.

Keep detailed evidence in the linked Notion page or report; link it instead of repeating it. Use plain words, not internal jargon.

If the run's findings support concrete new follow-ups not already on Todo, list them under Next with a short title and outcome, kept separate from decisions that unblock existing tasks. Keep suggestions outside the Todo page until the user accepts them, and ask one short question: add all, selected, or none? When accepted, use `/todo` to capture and order them; adding them does not itself authorize another run. Without useful follow-ups, ask nothing and invent none.
