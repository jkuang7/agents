---
name: sandcastle-run-epic
description: Run or resume a Sandcastle issue (an Epic or an issue with no sub-issues) through its trusted controller, or act as its caller for a queue of issues. Use for run, resume, continue, AFK and queue requests. Requirement changes use the separate change-request workflow.
---

# Sandcastle run Epic

Sandcastle is the runner; this skill is its caller. One runner command runs one issue until it has something for the caller, then exits with one result record (ADR 0003). The caller acts on that record: it merges, reruns, closes or asks. The runner never merges, advances `main`, closes the Epic or runs a queue.

## 1. Select mode

- `handoff` (default): start or resume one issue, confirm the controller owns it, and return to the user.
- `queue`: the user asked this thread to continue, run AFK, or work through a queue. Act as the caller (step 4) after every run. Merging PRs and closing Epics need the user's explicit authorization for this queue; continue or AFK alone doesn't grant it.

If the user asks for only one child and the runtime supports a run limit, pass a limit of 1.

## 2. Resolve the issue and trusted runtime

Resolve one repository, follow workspace and repository instructions and the issue-tracker convention, and confirm the issue exists and is open. Ask only if ownership remains ambiguous.

Establish the trusted operator revision, routing, the issue's durable state and controller ownership using [runtime.md](references/runtime.md). If a controller already owns this issue, do not launch another. Report it as the handoff when its ownership is established; otherwise report the gap.

## 3. Invoke the controller once

Invoke the current documented command once for the issue, from the trusted operator checkout, in an execution surface that outlives this agent. Use the trusted operator even when the issue changes Sandcastle itself; candidate runtime code cannot activate itself. A plain resume or rerun never authorizes an explicit retry control such as `--retry-blocked`. Retry a decision block only after its inputs change or the user authorizes the retry.

Confirm through supported runtime evidence that the controller passed startup and acquired ownership. A process spawn, PID, lock file or historical log alone is insufficient. If launch fails or ownership cannot be corroborated, preserve durable state and report a failed handoff.

In `handoff` mode, report the issue, operator revision, ownership evidence, and a copyable command that changes to the operator checkout and runs the runtime's read-only `--attach` for this issue, then return. Sandcastle owns implementation, review, checks, publication, retries within its budgets, and stopping. Observation is a separate, explicit request; use only the runtime's read-only watchers, and stopping one never stops the controller.

## 4. Act as the caller (queue mode)

Detect each controller exit (a background wait on the process or its recorded result), then read its **result record** (the last stdout line and durable state; see [runtime.md](references/runtime.md)) and act on exactly what it says:

| Result | Caller action |
|---|---|
| `ready`, with a child PR | If merging is authorized for this queue: wait for CI to pass, then merge it with `accept-pr` (merge commit, matching the head commit). The merge closes the child through `Closes #<child>`. Sync local `main` (step 5) and rerun the same command. Otherwise report the PR and stop. |
| `ready`, with one combined Epic PR (older runtimes) | Merge it under the same rules, then treat the Epic as complete. |
| `complete` | The last child PR has merged (its review ran the Epic's real-world check). If closure is authorized and the checks in `accept-pr`'s issue lifecycle contract pass, close the Epic. Report it and start the next queued issue. |
| `blocked`, class `transient` | Rerun once. If the same signature blocks again, treat it as a decision. |
| `blocked`, class `decision`, cause `runtime` | A Sandcastle defect. Check whether an open issue already has the same `signature`. Otherwise diagnose it with `diagnosing-bugs` against the recorded state and logs, and file one issue with the reproduction and root cause. Fix it through a focused issue, or, when the user authorized hotfixes and the runner cannot fix itself, through a hand-made hotfix PR. Then rerun. |
| `blocked`, class `decision`, cause `environment` | Missing authentication, permission or target. Fix access directly when you can (for example `gh auth login`, or a missing remote or repository); otherwise ask the user to fix it. Then rerun: environment blocks are not replayed. |
| any other `decision` (spec, drift, no progress, regression, self-change, budget) | Stop the queue and ask the user the record's `question`, with the reason and evidence. Rerun only after they answer by changing the spec, children or budget. Any amendment to a started child's spec, including one the user authorized for clear spec gaps, follows `sandcastle-change-request`'s scope check. |
| no result record, or a record that doesn't fit this table | Investigate the logs. Treat anything unclear as a decision. |

Fix operational problems in the runner's environment directly, such as a stale lock whose writers are proven gone, or auth or disk issues. Report every block with its class and cause.

**Spec concerns:** on a `ready` or `blocked` result for a child, search that run's raw review logs (`review-<n>.log` in the run's log directory) for `Spec concern:`. The logs are Codex JSONL: take the `item.text` of the `agent_message` that contains the `<review>` verdict tag, split it into lines, and keep only lines that start with `Spec concern:`. Don't match the phrase anywhere in the log; the review prompt, spec, diff and command output also contain it. These are a reviewer's non-blocking notes that a spec rule gives a wrong answer for a realistic case; the progress log omits them. Pass each one to the user with the result, quoted and attributed to the review, and for a `ready` child also post them as one comment on its PR. They never block a merge or change the caller's action; the user decides whether to amend the spec or file a follow-up.

**Moved spec paths:** a `spec` block from Sandcastle's moved-path check lists `old → new` path pairs. It is a clarification, not a question for the user. Update those paths where the spec tells the implementer to read, change or test them; leave history and context text as written. Edit the issue body directly when its run hasn't started, or, for a started child, follow `sandcastle-change-request` (its scope check, amendment comment and third-amendment rule), whose invocation is the rerun. Then rerun without asking the user. Every other `spec` block goes to the user, as the table says. A missing path with no rename is not checked; the implementer's spec conflict covers it.

**Reading cost:** on a `complete` result, report two figures with it so the user can see when the code is getting harder for workers to navigate. Compute them from the Epic's stage logs (`implementation-*`, `review-*` and `final-review-*` in every run directory under `.sandcastle/logs/epic-<N>/`), skipping `worker-*` logs because they duplicate the stage logs:

- the share of `command_execution` commands that search or list (`rg`, `grep`, `find`, `ls`);
- the three repository files with the most command output, crediting each command's output to every file path it names.

The figures are approximate and for information only. File nothing and change nothing based on them; the user decides whether something needs a spec. If the logs can't be read, say so and continue the queue.

## 5. Queue order, parallel runs and `main`

- **Order:** follow the queue the user set. Children of one Epic always run in order, one PR at a time.
- **Parallel:** after each run, list queued issues whose prerequisites have merged. Two issues may run at the same time only when the files they will change do not overlap, shared tests included. Compare each running issue's open child PR or candidate diff with the files the other issue names or will clearly change. Otherwise run them one after another. Report what runs in parallel and why the others wait.
- **Keep `main` runnable:** when the runner runs from this repository's `main`, merge only while no controller runs. Merge only after CI passes and, from the PR head in a temporary worktree, `npm ci` and `--help` both succeed; chain the merge on their success with `&&`, never through a pipe or `||`. (Run logs live only in the operator checkout, so `--usage` from a fresh worktree always fails.) The first controller start after the merge is the real check: if the merge broke startup, revert its merge commit through a PR and file an issue.
- **Merging:** merge one PR at a time. Resolve a later PR's conflicts on its own branch and wait for CI to pass again before merging it.
- **Local `main`:** fast-forward the operator checkout, and reinstall dependencies when the lockfile changed, only while no controller that runs from it is live.

## Scope boundary

Requirement and spec changes belong to `sandcastle-change-request`, `to-spec` and `to-tickets`. This skill does not create or edit child issues or change specs, apart from the moved-path clarifications in step 4, and does not merge, close or advance anything outside step 4's table and the user's queue authorization.
