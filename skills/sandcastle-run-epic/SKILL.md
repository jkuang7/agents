---
name: sandcastle-run-epic
description: Run or resume a Sandcastle issue (an Epic or an issue with no sub-issues) through its trusted controller, or act as its caller for a queue of issues. Use for run, resume, continue, AFK and queue requests. Requirement changes use the separate change-request workflow.
---

# Sandcastle run Epic

Sandcastle is the runner; this skill is its caller. One runner command runs one issue until it has something for the caller, then exits with one result record. The caller acts on that record: it merges, reruns, closes or asks. The runner never merges, advances `main`, closes the Epic or runs a queue.

## 1. Select mode

- `handoff` (default): start or resume one issue, confirm the controller owns it, and return to the user.
- `queue`: the user asked this thread to continue, run AFK, or work through a queue. Act as the caller (step 4) after every run. Merging PRs and closing Epics need the user's explicit authorization for this queue; continue or AFK alone doesn't grant it.

If the user asks for only one child and the runtime supports a run limit, pass a limit of 1.

## 2. Resolve the issue and trusted runtime

Resolve one repository, follow workspace and repository instructions and the issue-tracker convention, and confirm the issue exists and is open. Ask only if ownership remains ambiguous.

Establish the trusted operator revision, routing, the issue's durable state and controller ownership using [runtime.md](references/runtime.md). If a controller already owns this issue, do not launch another. Report it as the handoff when its ownership is established; otherwise report the gap.

## 3. Invoke the controller once

Invoke the current documented command once for the issue, from the trusted operator checkout, detached so it outlives this agent (see Commands below). Don't open a new terminal tab per run. Use the trusted operator even when the issue changes Sandcastle itself; candidate runtime code cannot activate itself. A plain resume or rerun never authorizes an explicit retry control such as `--retry-blocked`. Retry a decision block only after its inputs change or the user authorizes the retry.

Confirm through supported runtime evidence that the controller passed startup and acquired ownership. A process spawn, PID, lock file or historical log alone is insufficient. If launch fails or ownership cannot be corroborated, preserve durable state and report a failed handoff.

In `handoff` mode, report the issue, operator revision, ownership evidence, and a copyable command that changes to the operator checkout and runs the runtime's read-only `--attach` for this issue, then return. Sandcastle owns implementation, review, checks, publication, retries within its budgets, and stopping. Observation is a separate, explicit request; use only the runtime's read-only watchers, and stopping one never stops the controller.

## 4. Act as the caller (queue mode)

Detect each controller exit (a background wait on the process or its recorded result), then read its **result record** (the last stdout line and durable state; see [runtime.md](references/runtime.md)) and act on exactly what it says:

| Result | Caller action |
|---|---|
| `ready`, with a child PR | If merging is authorized for this queue: wait for CI to pass, then merge it through the merge gate (Commands), which is this repository's merge path for `accept-pr`; apply `accept-pr`'s confirmation and cleanup to the merged PR. The merge closes the child through `Closes #<child>`. Sync local `main` (step 5) and rerun the same command. Otherwise report the PR and stop. |
| `complete` | The last child PR has merged (its review ran the Epic's real-world check). If closure is authorized and the checks in `accept-pr`'s issue lifecycle contract pass, close the Epic. Report it and start the next queued issue. |
| `blocked`, class `transient` | Rerun once. If the same signature blocks again, treat it as a decision. |
| `blocked`, class `decision`, cause `runtime` | A Sandcastle defect. Check whether an open issue already has the same `signature`. Otherwise diagnose it with `diagnosing-bugs` against the recorded state and logs, and file one issue with the reproduction and root cause. Fix it through a focused issue, or, when the user authorized hotfixes and the runner cannot fix itself, through a hand-made hotfix PR. Then rerun. |
| `blocked`, class `decision`, cause `environment` | Missing authentication, permission or target. Fix access directly when you can (for example `gh auth login`, or a missing remote or repository); otherwise ask the user to fix it. Then rerun: environment blocks are not replayed. |
| any other `decision` (spec, drift, no progress, regression, self-change, budget) | Stop the queue and ask the user the record's `question`, with the reason and evidence. Rerun only after they answer by changing the spec, children or budget. Any amendment to a started child's spec, including one the user authorized for clear spec gaps, follows `sandcastle-change-request`'s scope check. After amending a spec for a `spec` block, run the on-demand preflight (Commands) on the amended body and rerun only when it reports no conflicts. Fixing only the reported conflict lets each rerun block on the next one. |
| no result record, or a record that doesn't fit this table | Investigate the logs. Treat anything unclear as a decision. |

Fix operational problems in the runner's environment directly, such as a stale lock whose writers are proven gone, or auth or disk issues. Report every block with its class and cause.

**Spec concerns:** on a `ready` or `blocked` result for a child, search that run's raw review logs (`review-<n>.log` in the run's log directory) for `Spec concern:`. The logs are Codex JSONL: take the `item.text` of the `agent_message` that contains the `<review>` verdict tag, split it into lines, and keep only lines that start with `Spec concern:`. Don't match the phrase anywhere in the log; the review prompt, spec, diff and command output also contain it. These are a reviewer's non-blocking notes that a spec rule gives a wrong answer for a realistic case; the progress log omits them. Pass each one to the user with the result, quoted and attributed to the review, and for a `ready` child also post them as one comment on its PR. They never block a merge or change the caller's action; the user decides whether to amend the spec or file a follow-up.

**Moved spec paths:** a `spec` block from Sandcastle's moved-path check lists `old → new` path pairs. It is a clarification, not a question for the user. Update those paths where the spec tells the implementer to read, change or test them; leave history and context text as written. Edit the issue body directly when its run hasn't started, or, for a started child, follow `sandcastle-change-request` (its scope check, amendment comment and third-amendment rule), whose invocation is the rerun. Then rerun without asking the user. Every other `spec` block goes to the user, as the table says. A missing path with no rename is not checked; the implementer's spec conflict covers it.

**Reading cost:** only when the user asks, report how hard the code is getting for workers to navigate, from the Epic's `implementation-*` and `review-*` stage logs (skip `worker-*`, which duplicate them): the share of `command_execution` commands that search or list (`rg`, `grep`, `find`, `ls`), and the three repository files with the most command output.

## 5. Queue order, parallel runs and `main`

- **Order:** follow the queue the user set. Children of one Epic always run in order, one PR at a time.
- **Parallel:** after each run, list queued issues whose prerequisites have merged. Two issues may run at the same time only when the files they will change do not overlap, shared tests included. Compare each running issue's open child PR or candidate diff with the files the other issue names or will clearly change. Otherwise run them one after another. Report what runs in parallel and why the others wait.
- **Keep `main` runnable:** when the runner runs from this repository's `main`, merge only while no controller runs. Merge only after CI passes and the merge gate (Commands) succeeds; chain the merge on its success with `&&`, never through a pipe or `||`. (Run logs live only in the operator checkout, so `--usage` from a fresh worktree always fails.) The first controller start after the merge is the real check: if the merge broke startup, revert its merge commit through a PR and file an issue.
- **Merging:** merge one PR at a time. Resolve a later PR's conflicts on its own branch and wait for CI to pass again before merging it.
- **Local `main`:** fast-forward the operator checkout, and reinstall dependencies when the lockfile changed, only while no controller that runs from it is live.

## 6. Commands

Run these from the operator checkout. Confirm each against the current README and `--help` first, and use the documented form when they differ. `<n>` is the issue, `<pr>` and `<sha>` the child PR and its head.

- **Start:** `(nohup npm start -- <n> >> .scratch/queue-orchestration/controller-<n>.out 2>&1 < /dev/null &)`. Wait about 20 seconds, then confirm ownership with `pgrep -fl "node.*loader.mjs src/cli/main.ts <n>$"` and a `started` line in that file.
- **Exit watcher:** one background command with the longest timeout, which fires only on exit. Don't poll or add milestone monitors:
  `while pgrep -f "node.*loader.mjs src/cli/main.ts <n>$" >/dev/null; do sleep 30; done; tail -1 .scratch/queue-orchestration/controller-<n>.out`
- **CI:** `gh pr checks <pr> --watch >/dev/null 2>&1; gh pr checks <pr>`, in the background.
- **Merge gate:** check that `gh pr view <pr> --json headRefOid -q .headRefOid` still equals `<sha>`, then:
  `git fetch -q origin pull/<pr>/head && git worktree add --detach .worktrees/merge-gate-<pr> <sha> && (cd .worktrees/merge-gate-<pr> && npm ci --silent && npx tsx src/cli/main.ts --help && gh pr merge <pr> --merge --match-head-commit <sha>)`
- **After the merge:** `git worktree remove --force .worktrees/merge-gate-<pr> && git pull --ff-only origin main`. Run `npm ci` only if `package-lock.json` changed. Then rerun the issue to get `complete`.
- **On-demand preflight:** `npm start -- preflight <issue-body.md> <base-commit> [parent-body.md]`.

## Queue defaults

Unless the user says otherwise, put robustness first, then speed, then leanness, and prefer less machinery. Keep the state that only this thread knows (queue order, authorization, current issue) in `.scratch/queue-orchestration/continuation.md`, so a handoff carries state and authorization, not procedure.

## Scope boundary

Requirement and spec changes belong to `sandcastle-change-request`, `to-spec` and `to-tickets`. This skill does not create or edit child issues or change specs, apart from the moved-path clarifications in step 4, and does not merge, close or advance anything outside step 4's table and the user's queue authorization.
