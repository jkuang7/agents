---
name: route
description: Who does a piece of work, which model, agent, reviewer or tool. Use before starting a subagent, escalating a decision, running a code review or audit, routing a /todo or /todo-run task, or doing browser or screen work.
---

# Route

This is the only place routing is written. AGENTS.md and skills point here instead of restating it; when a model, agent or tool changes, edit only this file.

## Claude sessions

- Sessions run on Sonnet and do the work themselves.
- Judgment goes to the `advisor` agent (Opus, `medium` effort): choosing between materially different designs, a tradeoff the user must live with, changing an interface, ADR or spec intent, or a failure with no clear next step. Brief it with the question, the options and the evidence paths; it starts without this conversation.
- An Opus context (`advisor`, or a skill pinned to `model: opus`) decides these itself and hands decided work to `worker`.
- Subagents run on Sonnet: `worker` for decided work, `Explore` to search. Name the type; never fall back to `general-purpose`. A retry after a review rejection goes to `worker-high` (the same agent at high effort).

## Codex sessions

- Judgment goes to the advisor through Claude, run from the working directory: `claude -p --agent advisor --model opus --permission-mode bypassPermissions "<brief>"`. Codex can't wake on background tasks, so wait in the foreground.
- Reviews use `gpt-6.1-sol` as below.

## Review

- Code review and audit run on Sol at `high` effort, prompt on stdin starting with the `reviewer` agent's rubric: `codex exec -m gpt-6.1-sol -s read-only --skip-git-repo-check -C <dir> -c model_reasoning_effort=high -o <file> -`. High found twice as many known bugs as Sol medium or Sonnet, with no invalid findings (`/Volumes/T9/Dev/.scratch/review-eval/results.md`).
- Use the Sonnet `reviewer` agent for frontend or visual review, spec and ticket review (not tested), and when `codex exec` fails or Codex is rate-limited.
- Opus skills judge themselves; their review loops follow this section.

## Runner workers

Workers started by a runner such as Sandcastle follow the runner's prompt instead of this file: they start no agents or reviews and don't merge.

## Task kinds

For work that isn't a code change in this session, such as a `/todo` task:

| Work | Route |
|---|---|
| Web research, shopping comparisons, email or Gmail | Muse (free app); use current sources and cite them |
| Reddit or community opinion | ChatGPT web |
| Signed-in screen inspection or computer use | Codex computer use (see Browser and screen) |
| Code changes and engineering investigations | Codex, following the target repository's AGENTS.md and the sections above |
| Architecture, design tradeoffs or unclear technical direction | the `advisor` for the decision, then route the decided work |
| A Sandcastle Epic or issue to run or resume | `/babysit` |
| Claude as the worker or model | only when the user explicitly asks, through the route they approved and its required tap |

A task about a product, such as a Claude artifact, doesn't select its maker as the worker; route by the work requested. If a required route is unavailable, block that task with the reason.

## Browser and screen

- Browser or website UI work uses Codex computer use (`cua_repl`) in the user's local Zen browser on GPT-6.1-Sol at high reasoning effort; this setup is required. Start from Zen's open tabs and session; never use Playwright, Chrome DevTools or an in-app browser, even when available. It doesn't cover shell coding or API and connector operations.
- If the current session differs, is unknown or can't provide this setup, pause browser work, report accurately what is running or unavailable and ask the user to choose an appropriate session. Never claim the runtime changed, never invent a setting, and never switch to another browser.
- Muse, ChatGPT and computer use share the user's one screen: run screen tasks one at a time, never alongside another, and run them while the user is away only when the task's recorded decisions allow it.
