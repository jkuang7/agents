---
name: sandcastle-run-epic
description: Run or resume a Sandcastle issue (an Epic or an issue with no sub-issues) through its controller, or act as its caller for a queue of issues. Use for Sandcastle run, resume, AFK and queue requests. Requirement changes use sandcastle-change-request.
---

# Sandcastle run Epic

Sandcastle is the runner; this skill is its caller. One run delivers at most one child PR, then exits with one result record as the last line of its output. The caller acts on that record: it merges, reruns, closes or asks. The runner never merges, advances `main`, closes the Epic or runs a queue.

Sandcastle's README and `--help` own its commands, result contract, block causes, budgets and recovery. Read them once per session and again after `main` changes; where this skill and they disagree, they win. Sandcastle itself refuses a second controller on the same checkout, recovers stale locks, fails closed on spec edits and replays saved decisions, so the caller doesn't re-check those.

## Modes

- `handoff` (default): start or resume one issue, confirm it started, give the user the `--attach` command, and return.
- `queue`: the user asked this thread to run AFK or work through a queue. Act on every result as below. Merging PRs and closing Epics need the user's authorization for this queue; "continue" or "AFK" alone doesn't grant it.

Always launch from the operator checkout on clean `main`, even when the issue changes Sandcastle itself.

## Act on each result (queue mode)

| Result | Caller action |
|---|---|
| `ready`, with a child PR | When merging is authorized: wait for CI, merge through the merge gate, sync `main`, and rerun the same issue. Otherwise report the PR and stop. |
| `complete` | When closure is authorized, close the Epic. Report it and start the next queued issue. |
| `blocked`, class `transient`, or cause `environment` or `self-change` | Fix the stated condition (auth or access, a clean operator checkout), then rerun. If the same cause blocks twice in a row, treat it as a decision. |
| `blocked`, cause `runtime` | A Sandcastle defect. Look for an open issue with the same `signature`; otherwise diagnose it with `diagnosing-bugs` and file one issue with the reproduction and cause. Then rerun. |
| `blocked`, class `fixable` | Checks or review still failed after corrections. Rerun once; if it blocks the same way, treat it as a decision. |
| Any other decision | Stop the queue and ask the user the record's `question`, with its `reason`. Rerun after they change the spec, children or budget. |
| No result record, or one this table doesn't cover | Read the run's logs and treat it as a decision. |

**Spec blocks:** the record's `reason` lists every conflict, its `question` only the first. Resolve all of them in one amendment, through `sandcastle-change-request` for a started child, and run the on-demand preflight on the amended body before rerunning. A moved-path block (`old → new` pairs) is a clarification: update those paths and rerun without asking.

**Spec concerns:** for a `ready` or `blocked` child, read the reviewer's verdict message in the run's `review-*.log` (the `agent_message` containing `<review>`) and keep its lines starting `Spec concern:`. Matching the phrase anywhere else in the log gives false hits. Quote each to the user and, for a `ready` child, post them as one PR comment. They never block a merge.

## Queue rules

- Run one issue at a time: one operator checkout runs one controller. Children of an Epic run in their sub-issue order.
- Merge only while no controller runs, one PR at a time, and only after CI passes and the merge gate succeeds. If a merge breaks the next start, revert it through a PR and file an issue.
- Keep the queue order, authorization and current issue in `.scratch/queue-orchestration/continuation.md`, so a handoff carries state, not procedure.
- Unless the user says otherwise, put robustness first, then speed, then leanness.

## Commands

Run from the operator checkout. `<n>` is the issue; `<pr>` and `<sha>` are the child PR and its head. Each command is self-contained, because every shell starts fresh.

- **Already running?** If `kill -0 $(cat .scratch/queue-orchestration/controller-<n>.pid 2>/dev/null) 2>/dev/null` succeeds, don't launch: report it running and give the attach command.
- **Start:** `mkdir -p .scratch/queue-orchestration && (nohup npm --silent start -- <n> >> .scratch/queue-orchestration/controller-<n>.out 2>&1 < /dev/null & echo $! > .scratch/queue-orchestration/controller-<n>.pid)`. Don't open a terminal tab per run. After about 20 seconds, check the process is alive and the output shows the run started. A run with nothing new to do (a replayed decision, `ready` before its merge, `complete`) exits within seconds: then read its result instead of reporting a failed start.
- **Result record:** `grep '^{"status"' .scratch/queue-orchestration/controller-<n>.out | tail -1`.
- **Attach (for the user):** `cd <operator checkout> && npm start -- <n> --attach`.
- **Exit watcher:** one background command that fires only on exit; restart it if it times out while the process lives:
  `while kill -0 $(cat .scratch/queue-orchestration/controller-<n>.pid) 2>/dev/null; do sleep 30; done; grep '^{"status"' .scratch/queue-orchestration/controller-<n>.out | tail -1`
- **CI:** `gh pr checks <pr> --watch >/dev/null 2>&1; gh pr checks <pr>`, in the background. CI has passed only when the final `gh pr checks` exits 0; read its exit status, not a slice of its output. The repository has no branch protection, so this is the only CI gate.
- **Merge gate:** proves the PR head starts before it reaches `main`:
  `git fetch -q origin pull/<pr>/head && git worktree add --detach .worktrees/merge-gate-<pr> <sha> && (cd .worktrees/merge-gate-<pr> && npm ci --silent && npm start -- --help >/dev/null && gh pr merge <pr> --merge --match-head-commit <sha>)`
- **After the merge:** `git worktree remove --force .worktrees/merge-gate-<pr> && git pull --ff-only origin main`, and `npm ci` if `package-lock.json` changed.
- **On-demand preflight:** see the README's preflight section.

## Scope

Spec and child changes belong to `sandcastle-change-request`, `to-spec` and `to-tickets`. This skill edits a spec only for moved-path clarifications.
