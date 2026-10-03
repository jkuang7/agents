---
name: todo
description: Collect a task dump, plan the tasks with the user, and capture them as checkboxes on the Todo page in Objective’s Backlog. Use for /todo, “add these tasks,” or a pasted list. Running tasks is /todo-run.
---

# Todo

Turn the dump into a durable, ready-to-run checklist. Do the planning while the user is present; the tasks run only through `/todo-run` after the report.

## Listen

For each message, reply only “Got it.” and collect it. Read no code, run no tools, and write nothing to Notion while collecting. Answer direct questions in one line. The dump ends when the user says “go,” “done,” “ship it,” or “your turn” as a standalone message or closing words. Do not mistake those words inside task text (for example, “go to the bank”) as the signal. A message ending in “go” means act on the dump immediately.

## Write and plan

On the signal, use all messages since `/todo` (or since the first message if invoked without `/todo`), in order. Later messages correct earlier ones. Merge repeated tasks while retaining their useful details, links, names, and constraints. Replies to planning questions are decisions, not new tasks.

Scope the checklist to this dump. Do not sweep unrelated open Objective rows or pages into it. Add an older task only when the user explicitly names it for migration; include just that task and a source link, not the source page's full contents. Keep its original page and database row visible unless the user separately asks to archive them.

Keep one persistent Notion Task page named **Todo** in the **Objective** database under Journal. This is the single checklist container shown in the Backlog view; individual dump items are checkboxes inside its page body, not separate database rows. Find and fetch the existing non-archived Todo Task before creating anything. If none exists, create one in Objective with Type = Task, Archive = No, and Status = Backlog. If multiple non-archived Todo Tasks exist, stop and report the ambiguity instead of choosing or creating another. Never create a separate Journal page or duplicate Todo container. When adding open tasks to an existing Done or Blocked container, set its Status back to Backlog. Confirm the data source has the Type, Archive, and Status properties and the required status options; if not, stop before writing.

Each task is one root checkbox, with its plan in a collapsible details block:

```markdown
- [ ] Short imperative task name preserving the user's intent
	<details>
	<summary>Plan</summary>
		Added: YYYY-MM-DD
		Goal: One-line outcome
		Done when: Checkable completion condition
		Route: Worker/tool and why
		After: prerequisite task names, or none
		Decisions: User decisions and approved boundaries, or none
	</details>
```

Use the user's local date for Added. Preserve supplied source links in the task's details. Keep the exact requested work; do not execute it during `/todo`.

Check the existing Todo page before adding tasks. Skip duplicates among open checkboxes and tasks completed today. Merge useful new details into an existing matching open item without erasing prior decisions. Do not remove completed items. Keep the Todo container's Archive property set to No while it holds active checklist items.

Plan every new dump task and every older task the user explicitly selected for migration. Do not plan or modify unrelated open Objective rows. Decide the goal, checkable finish, route, prerequisites, and boundaries. Route each task and escalate judgment with the `route` skill. Research facts that can be settled cheaply; ask only about decisions the evidence cannot settle.

Ask in one numbered round, grouped by task and ordered so dependent answers come later. Include only questions that matter: unclear intent or finish criteria, credentials or login the user must provide, approval before spending or messaging as the user, whether screen tasks may run while the user is away, and any user-written route that conflicts with the task. For multi-issue coding work ask whether `/todo-run` should start `/specs` and finish with “next: /babysit”. State the recommended answer and why. Follow up only when an answer changes another necessary question.

Once planning is resolved, write all five plan lines in each task's details block:

- **Goal:** intended outcome.
- **Done when:** checkable completion.
- **Route:** worker/tool and reason, chosen with the `route` skill.
- **After:** prerequisite task names or `none`.
- **Decisions:** answers, approvals, and limits, or `none`.

Only update the affected task blocks. Preserve unrelated page content and concurrent edits. If the Notion connector is unavailable, do not silently use a different store; report that the checklist could not be written.

## Report

Reply in one or two lines with the count and titles added and planned, duplicates skipped, and any item still unplanned with its reason. Then invoke `/todo-run` in this same thread to run them; skip it when nothing is runnable.
