---
name: route
description: Who does a piece of work, which model, agent, reviewer or tool, and how to change that. Use for /route to view or update routing, and before starting a subagent, escalating a decision, running a code review or audit, routing a /todo or /todo-run task, or doing browser or screen work.
---

# Route

The only place routing is written; Claude Code always loads it (`~/.claude/rules/route.md`). Elsewhere, point here instead of restating it.

**Updating:** `/route <change>` edits this file (`/Volumes/T9/Dev/agents/skills/route/SKILL.md`), moves any routing found restated elsewhere into it, and finishes through a PR. `/route` alone summarizes the current routes.

## Models and agents

- Claude sessions run on Sonnet and do the work themselves. Subagents: `worker` for decided work, `Explore` to search, `worker-high` to retry after a review rejection. Name the type; never `general-purpose`.
- Judgment goes to the `advisor` (Opus, medium): choosing between materially different designs, a tradeoff the user must live with, changing an interface, ADR or spec intent, or a failure with no clear next step. Brief it with the question, options and evidence paths; it starts without this conversation. From Codex: `claude -p --agent advisor --model opus --permission-mode bypassPermissions "<brief>"` from the working directory, waiting in the foreground.
- An Opus context (`advisor`, or a skill pinned to `model: opus`) decides these itself and hands decided work to `worker`.
- Runner workers (such as Sandcastle's) follow the runner's prompt instead: no agents, reviews or merges.

## Review

- Code review and audit: Sol at high effort, prompt on stdin starting with the `reviewer` agent's rubric: `codex exec -m gpt-6.1-sol -s read-only --skip-git-repo-check -C <dir> -c model_reasoning_effort=high -o <file> -`. It found twice as many known bugs as Sol medium or Sonnet, with no invalid findings (`/Volumes/T9/Dev/.scratch/review-eval/results.md`).
- The Sonnet `reviewer` agent: frontend or visual review, spec and ticket review, and when `codex exec` fails or is rate-limited.
- Opus skills judge themselves; their review loops follow this section.

## Task kinds

| Work | Route |
|---|---|
| Web research, shopping comparisons, email or Gmail | Muse (free app); current sources, cited |
| Reddit or community opinion | ChatGPT web |
| Signed-in screen inspection, computer use, any browser step | Codex computer use (below) |
| Code changes and engineering investigations | Codex, following the target repository's AGENTS.md and the sections above |
| Creating, editing, updating or deleting a skill | Sonnet 5.5 (`claude-sonnet-5-5`), following `/Volumes/T9/Dev/docs/agents/skills.md`; from Codex: `claude -p --model sonnet --permission-mode bypassPermissions "<brief>"` |
| Architecture, design tradeoffs, unclear technical direction | `advisor`, then route the decided work |
| A Sandcastle Epic or issue to run or resume | `/babysit` |
| Claude as the worker | only when the user explicitly asks, through the approved route and its required tap |

A task about a product (such as a Claude artifact) doesn't make its maker the worker. If a required route is unavailable, block that task with the reason.

## Browser and screen

- Browser work uses Codex computer use (`cua_repl`) in the user's local Zen browser on GPT-6.1-Sol at high effort, starting from Zen's open tabs and session. Never Playwright, Chrome DevTools or an in-app browser, even when available. Shell, API and connector work isn't browser work.
- If the session can't provide this or you can't tell, pause browser work, say accurately what is running or unavailable, and ask the user to choose a session. Never claim the runtime changed, invent a setting, or switch browsers.
- Muse, ChatGPT and computer use share one screen: one screen task at a time, and while the user is away only when the task's recorded decisions allow it.
