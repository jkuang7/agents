---
name: todo-run
description: Run the planned Task rows in the Notion Objective database AFK until none remain, never asking. Use for todo-run, run my todos, or work the task list. Capturing and planning tasks is todo.
---

# Todo run

You route and track; workers do the work. `todo` already planned the rows with the user; you run them AFK and never stop to ask. Notion is the only state: hold none, poll nothing, and loop only over what a query returns. Use the Notion MCP on data source `collection://1b37b752-4055-8097-8011-000b41a46d67` ("Objective"). It also holds Docs and Active rows: read and change only rows with Type = Task and Archive = No, and never create a database or rows.

## Checks

- **No Notion MCP:** stop. Tell the user: in Codex, `codex mcp add notion --url https://mcp.notion.com/mcp` then `codex mcp login notion`; in Claude Code, connect the Notion connector.
- **Status lacks Done or Blocked:** fetch the data source schema first. If either option is missing, stop before claiming anything and tell the user to add it by hand in Notion.
- Run one `todo-run` at a time. Any row already In progress at start was left by a dead run.

## Loop

1. **Query** open rows: Status Backlog or In progress. Ignore Maybe, Done and Blocked. None: report and stop. Read each page body's `Plan` section (Goal, Done when, Route, After, Decisions; `todo` records it).
2. **Unplanned row** (any of the five `Plan` lines missing or empty, such as a row added straight in Notion): fill only the missing lines yourself, applying the ambiguity rule below; never overwrite recorded lines. If it needs a user decision, Block it with `needs todo planning:` and the question.
3. **Order:** a row runs only after the rows in its `After` line are Done. If one ended Blocked, or can't be found, or the `After` lines form a cycle, Block this row with the reason.
4. **Claim:** right before starting a row, re-read it; skip it unless its Status is Backlog, or it was In progress at start. Set Status = In progress. For a reclaimed In progress row, read its page body and Result first and continue from there; never repeat a side effect it records.
5. **Run** it by its `Plan`. A non-empty Route property, written by the user, overrides the plan's route; the guard below still applies.
6. **Finish** every claimed row, never leaving it In progress:
   - Done, only when its `Done when` is met: Result of at most three lines; anything longer goes in the page body. Not met after the retry: Blocked with what is missing.
   - Blocked: Result is one line giving the reason. Prefix `needs you:` when the user must act.
7. **Re-query** for Status Backlog only (rows added mid-run). In progress rows now are this run's own. Repeat from step 2 until no row is runnable; a row still waiting on its `After` rows then is Blocked with the reason.

**Ambiguity:** if one reading is clearly likeliest and acting on it is reversible, act on it and name the reading in Result; otherwise Block. Anything unforeseen: Block the row with a one-line reason and carry on with the rest. A failed worker gets one retry; then Block with the error. Blocked rows stay Blocked; the user sets one back to Backlog to retry it.

Spending money or messaging a person as the user needs a pre-approval for that action in the row's `Decisions`; without one, Block with `needs you:`. <!-- drop this line to lift the money/message guard -->

**Report** in a few lines: each done row, then each blocked row with what it needs.

## Routing

Judgment calls (architecture, design choices, tradeoffs, interface changes) follow the model-routing rule in `/Volumes/T9/Dev/AGENTS.md`: the `advisor` agent (Opus) decides. From Codex: `claude -p --agent advisor --model opus --permission-mode bypassPermissions "<brief>"`.

Route everything else by `/Volumes/T9/Dev/repos/agent-hub/router/preferences.md`; where its table differs from this list, the table wins, but judgment calls still go to the advisor:

- **Web research, shopping or comparison, anything email or Gmail:** Muse. **Reddit or community opinion:** ChatGPT. Drive them as the agent hub does: a Codex computer-use session in the signed-in Zen browser following `/Volumes/T9/Dev/repos/agent-hub/workers/relay-prompt.md`, read and draft only. If you can't run that session, or it returns `BLOCKED`, Block with `needs you:`.
- **Computer use** (unsubscribing, filling forms): Codex computer use.
- **Code fixes and features:** a Codex subagent on gpt-6.1-sol at medium effort, briefed with the repo and the task; it follows that repo's AGENTS.md. **Multi-PR work:** if `Decisions` says start `specs`, run it and finish Done with Result naming the Epic and "next: /babysit"; if it says `/babysit`, or nothing, finish Blocked with `needs you: run specs, then /babysit`.
- **Quick lookups:** do them yourself.

Muse, ChatGPT and computer use share one screen: run them one at a time, and only if the row's `Decisions` allows it while the user is away; otherwise Block with `needs you: screen task`. Run up to about three other tasks in parallel, claiming each before it starts.
