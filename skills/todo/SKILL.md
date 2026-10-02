---
name: todo
description: Collect a brain dump of tasks over several messages, then add them as Task rows in the Notion Objective database and plan each with the user so todo-run can run them AFK. Use when the user types /todo, says add these tasks, or pastes a list of things to do. Running them is todo-run.
---

# Todo

You do the reasoning while the user is here, so `todo-run` can run AFK without asking.

## Listen

Until the user says go (or done, ship it, your turn), reply only "Got it." Don't read code, run tools or write to Notion. Answer only questions asked directly, in one line. Go counts only as a standalone message or a message's closing words, never inside task text such as "go to the bank"; a message that closes with go is acted on at once.

## Write

On go, take every user message since /todo (or since the first message, if the skill triggered without it) and after the last write, word for word and in order; later messages override earlier ones, including removing or changing a task. Write them to the Notion data source `collection://1b37b752-4055-8097-8011-000b41a46d67` ("Objective", under Journal) with the Notion MCP. It also holds Docs and Active rows: read and change only rows with Type = Task and Archive = No, and never create a database. Don't run tasks; that is `todo-run`.

No Notion MCP: stop and tell the user: in Codex, `codex mcp add notion --url https://mcp.notion.com/mcp` then `codex mcp login notion`; in Claude Code, connect the Notion connector.

1. Split the dump into one task each: a short imperative Name keeping every detail the user gave (links, names, constraints). Merge repeats.
2. Query the open Task rows (Status Backlog or In progress), plus Done or Blocked Task rows created today. Skip a task that means the same as one of them, even if worded differently.
3. Create each remaining row with Type = Task, Archive = No, Status = Backlog, Due Date = today (local date). Route stays blank unless the user named a worker or tool for the task (Muse, Codex, the advisor); then copy their words. Leave Result blank.

## Plan

Plan each new row, plus any open Task row without a complete `Plan` (a planning session that ended early); keep answers already recorded. For each, decide its goal, route (`todo-run`'s Routing section), needs, blockers and prerequisites. Recommend the simplest approach that meets the goal, on the cheapest route that does the job (the priorities in `/Volumes/T9/Dev/AGENTS.md`). Judgment-heavy planning (architecture, design, tradeoffs) follows the model-routing rule there and may go to the `advisor`. Look up what you can; ask the user only what the plan can't settle, and ask a question shared by several rows once. The user's replies here are answers, not a new dump.

1. **Ask** in one numbered round, grouped by task and ordered so a question other answers depend on, or that unblocks the most work, comes first. Each question has a recommended simplest answer and a one-line reason, so the user may answer "defaults" or by number. No questions: skip to Record. Include what applies:
   - for each task whose intent or done-criterion is genuinely unclear, every question needed to choose its approach
   - logins, 2FA or credentials the user must supply or confirm
   - pre-approval for each action that spends money or messages a person as the user
   - multi-PR work: `todo-run` starts `specs`, or the user takes it to a `/babysit` thread
   - screen tasks (Muse, ChatGPT, computer use) share one screen: may they run while the user is away from the Mac
   - a user-written Route that conflicts with the task
2. **Follow up** only on answers that change what else must be asked, in as few rounds as possible, never repeating a question. Re-plan any row an answer changes.
3. **Record** on each row, in its page body, a `Plan` section with these lines; a row is ready when all five are filled:

   ```
   Goal: <one line>
   Done when: <checkable criterion>
   Route: <worker> — <one-line reason>
   After: <names of rows that must finish first, or none>
   Decisions: <each answer, including approvals and screen permission, or none>
   ```

## Report

Reply in one or two lines: the count and titles added and planned, any skipped as duplicates, and any still unplanned with why. Then leave this mode; a later go handles only tasks given since this write, plus unplanned rows.
