---
name: todo
description: Collect a task dump, plan the tasks with the user, and capture them as checkboxes on the Todo page in Objective’s Backlog. Use for /todo, “add these tasks,” or a pasted list. Running tasks is /todo-run.
---

# Todo

Turn the dump into a durable, ready-to-run checklist. Do the planning while the user is present; do not start the tasks.

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

Plan every new dump task and every older task the user explicitly selected for migration. Do not plan or modify unrelated open Objective rows. Decide the goal, checkable finish, route, prerequisites, and boundaries. Use workspace model-routing preferences for judgment-heavy choices. Research facts that can be settled cheaply; ask only about decisions the evidence cannot settle.

## Order the checklist

Order the work for efficient execution, not just in the order it was mentioned. Respect explicit user ordering and `After` dependencies first. Then put work that unblocks several tasks or the whole queue first; group compatible tasks that share a repo, source, account, setup, or screen route to reduce context switching; do foundational work before tasks that rely on its result; and avoid doing work likely to be replaced by a later decision. Use the dump's original order as a tiebreaker. Never group tasks in a way that violates permissions or the one-screen-task-at-a-time rule. When adding or merging items into an existing Todo, reconsider the order of all unchecked tasks using the same rule. Plan for parallel runs too: `/todo-run` may dispatch tasks to subagents at once, so treat tasks with no `After` link, no shared working files, and non-screen routes as able to run in parallel; same-repository code tasks can run in separate worktrees. When two such tasks must not overlap (same non-code files, account, or a result one needs from the other), add an `After` link or a Decisions note; otherwise leave them free. Starting agents or work stays with `/todo-run`. Move whole checkbox/details blocks together, leave their content and status intact, and keep checked historical tasks after the open queue in their existing relative order.

Ask in one numbered round, grouped by task and ordered so dependent answers come later. Include only questions that matter: unclear intent or finish criteria, credentials or login the user must provide, approval before spending or messaging as the user, whether screen tasks may run while the user is away, and any user-written route that conflicts with the task. For multi-issue coding work ask whether `/todo-run` should start `/specs` and finish with “next: /babysit”. State the recommended answer and why. Follow up only when an answer changes another necessary question.

Once planning is resolved, write all five plan lines in each task's details block:

- **Goal:** intended outcome.
- **Done when:** checkable completion.
- **Route:** correct worker/tool and reason. Read `/Volumes/T9/Dev/repos/agent-hub/router/preferences.md`, the canonical routing file, when resolving a task's route or source; workspace and repository `AGENTS.md` win where they conflict. Record in Route or Decisions what it sets for the task: browser or other screen steps (signed-in Zen for browsing; a screen task) and, for personal saved sources, the source plan (which chats and surfaces to check). Do not search those sources during `/todo`. A Claude product/artifact is the subject, not a request to use Claude as worker.
- **After:** prerequisite task names or `none`.
- **Decisions:** answers, approvals, and limits, or `none`.

Only update the affected task blocks. Preserve unrelated page content and concurrent edits. If the Notion connector is unavailable, do not silently use a different store; report that the checklist could not be written.

## Report

End with a short report covering only this dump under three headings. Give each task one or two plain sentences, so length grows with the task count rather than a fixed line limit:

- **Added:** each task captured, what it will deliver, and anything that shapes its run, such as route, prerequisite, or approved limit. Say which were merged into existing items or skipped as duplicates.
- **Blocked:** each task left unplanned, what is missing, and the decision or input that would let it be planned. Group tasks that share an open question under it, naming every affected task.
- **Next:** `/todo-run` to execute the queue, preceded by any answers the user should give first, in priority order.

For any failed or blocked step, state what was attempted, the observed failure or error, the cause only as far as evidence shows it, and the recovery action. If the root cause is unknown, say so and label any guess as a hypothesis; a failed tool action alone does not establish a technical cause. Keep this to task-level context, not logs.

Use plain words, not internal jargon.

Report capture only; nothing has run yet, and older unrelated tasks stay out of the summary.
