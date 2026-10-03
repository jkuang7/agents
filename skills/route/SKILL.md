---
name: route
description: Who does a piece of work, which model, agent, reviewer or tool, and how to change that. Use for /route to view or update routing, and before starting a subagent, escalating a decision, running a code review or audit, routing a /todo or /todo-run task, or doing browser or screen work.
---

# Route

The only place routing is written; Claude Code always loads it (`~/.claude/rules/route.md`), and Codex gets it in `~/.codex/AGENTS.md`, both set up by `bin/deploy`. Elsewhere, point here instead of restating it.

**Updating:** `/route <change>` edits this file (`/Volumes/T9/Dev/agents/skills/route/SKILL.md`), moves any routing found restated elsewhere into it, and finishes through a PR, then runs `bin/deploy` so Codex's copy matches. `/route` alone summarizes the current routes.

## Models and agents

- Claude sessions run on Sonnet and do the work themselves. Subagents: `worker` for decided work, `Explore` to search, `worker-high` to retry after a review rejection. Name the type; never `general-purpose`.
- Judgment goes to the `advisor` (Opus, medium): choosing between materially different designs, a tradeoff the user must live with, changing an interface, ADR or spec intent, or a failure with no clear next step. Brief it with the question, options and evidence paths; it starts without this conversation. From Codex: `claude -p --agent advisor --model opus --effort medium --permission-mode bypassPermissions "<brief>"` from the working directory, waiting in the foreground.
- An Opus context (`advisor`, or a skill pinned to `model: opus`) decides these itself and hands decided work to `worker`.
- Runner workers (such as Sandcastle's) follow the runner's prompt instead: no agents, reviews or merges.

## Dispatch

Route the work, not the parent session. When work requires a different model, effort or tool, the coordinating parent starts a worker with that setup rather than asking the user to change the parent session. Use the runtime's supported delegation and pass the goal, recorded decisions (including away use), authorized side effects, forbidden actions, source links and completion criteria in a focused brief. Workers act within that brief, return unmet requirements to the parent and seek the parent's decision before unapproved side effects; runner workers retain their no-delegation rule. Keep small work in the parent when it already meets the route.

In Codex, use `collaboration.spawn_agent` with explicit `model` and `reasoning_effort` when the required model is available there. With overrides, use `fork_turns: "none"` plus the brief, or a positive recent-turn count, never full history. For browser work, name the task `worker` (or a unique `worker_*` name), select `gpt-6.1-sol` and `reasoning_effort: "high"`, and require the Browser and screen rules below in the brief. Before mutation, the worker checks that `cua_repl` is available and performs a read-only inspection of the actual local Zen session; it reports access or the concrete failure to the parent. Report requested model/effort separately from observed tool/session access; never claim the parent changed.

Claude Code uses its native named subagents, which must run the required model and effort through the agent definition or launch overrides the runtime actually supports; if neither can provide them, return the unmet setup instead of reporting success on a default setup. From Codex, use the advisor command above or `claude -p --agent worker --model <required-model> --effort <required-effort>` for decided Claude work, with approved permissions. Preserve explicit-request and tap requirements for Claude as a worker. A Claude worker cannot replace the required Codex browser worker: a Claude parent needs an exposed Codex delegation tool that provides the required setup; without one, report the browser task blocked by that missing capability. Do not assume `codex exec` has local computer-use access or invent a launch path. Report requested setup accurately on either runtime.

The worker owns its assigned work; the parent tracks it, waits for its result and checks evidence against the brief's completion criteria. Start only one screen worker at a time; wait for it to return or stop it before dispatching the next screen task. The parent, other agents, Muse and ChatGPT do no screen work while that worker owns the screen. Delegation preserves authorization and does not change the parent model or effort. If the supported worker cannot meet the route or access the required tools/session, report that concrete failure and ask only for the missing setup.

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
- If the coordinating parent doesn't meet this setup, dispatch a browser worker as above; an assigned worker returns a setup failure instead of delegating again. Pause and ask for setup only if no supported worker can provide the required model, effort, computer use and local Zen access. Never claim the parent runtime changed, invent a setting, or switch browsers.
- Muse, ChatGPT and computer use share one screen: one screen task at a time, and while the user is away only when the task's recorded decisions allow it.
