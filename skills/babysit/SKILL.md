---
name: babysit
description: Babysit one project's Sandcastle work AFK until its queue is done, fixing what breaks and asking only when direction is unclear. Use for babysit, Sandcastle run, resume, AFK and queue requests. Requirement changes use sandcastle-change-request.
---

# Babysit

You are the AFK babysitter for one project. Sandcastle does the work: each run delivers at most one child PR of an issue, then exits with a result record. You keep the queue moving: start runs, merge green PRs, rerun, pick up new work, and fix what breaks. Ask the user only when direction is unclear.

Roles: Sandcastle implements and reviews; you run the loop; the `advisor` judges; `worker` and `reviewer` write and check code, each as the `route` skill assigns. Sandcastle's README and `--help` own its commands, results, budgets and recovery; read them once per session and after `main` changes; they win over this skill. Sandcastle refuses a second controller, recovers stale locks, fails closed on spec edits and replays decisions; don't re-check those.

## Start

`/babysit [repo]`: `repo` is `sandcastle`, a repository name under `/Volumes/T9/Dev/repos`, or a checkout path; without it, the current checkout's project. `<O>` is the Sandcastle operator checkout `/Volumes/T9/Dev/sandcastle`; `<P>` is the project's checkout. Always launch from `<O>` on clean `main`; when `<P>` isn't `<O>`, add `--target <P>` to every `npm start`. The project's state file is `<P>/.scratch/queue-orchestration/continuation.md`.

Invoking `/babysit` authorizes merging the project's green Sandcastle child PRs, closing its finished Epics, and amending a spec when its intent is clear. Record that under `## Authority` in the state file; act within it; anything outside it is `unclear`. A request to only start one issue is a handoff: start it, confirm, give the attach command, return.

Orient before acting:

1. Read the state file if it exists: `## Authority`, `## Queue`, `## Inbox`, `Last drain`, and recorded reruns.
2. Check live state: a running controller ("Already running?"), open child PRs, and whether `main` matches `origin/main` in `<P>` and `<O>`.
3. Reconcile `## Queue` with GitHub: drop closed issues; add open Epics and standalone specs not yet queued, skipping `not-ready`, not-planned and non-spec issues, placed by the ordering rule. Without a state file, create one with `## Authority`, `## Queue`, `## Inbox` and `Last drain` (now).

Then continue from there, not fresh.

## The loop

1. Start the next queued issue (an Epic runs by its own number, children in sub-issue order) and watch for its exit.
2. Act on its result record (table below). For every `ready` or `blocked` child, also read its spec concerns.
3. Between runs, take in new work (below).
4. Repeat from step 1. Once the queue is empty and no issues are open, run **Cleanup** (Commands), update the state file and stop with nothing running: report the queue done; `/babysit` resumes.

| Result | Action |
|---|---|
| `ready`, with a PR | Run `gh pr checks <pr> --watch` in `<P>` in the background, then merge (`merge-green` decides pass or fail), then rerun the same issue. If merge refuses because checks failed, rerun the failed CI jobs once and try again; a second failure is a problem, normally the child-CI fix path. |
| `complete` | Close the Epic, then start the next queued issue. |
| `blocked`, class `transient` or `fixable`, or cause `environment` or `self-change` | Clear only what is safe (install a missing tool inside the project, remove your own scratch files from the operator checkout), then rerun once. The same class and cause again is a problem. Auth, access, and other files in the operator checkout go to the user. |
| `blocked` on a spec conflict | See spec blocks below. |
| `blocked`, cause `runtime` | A Sandcastle defect: the `main`/Sandcastle fix path below. |
| Anything else: other `blocked` causes, any other merge refusal, no record | A problem: the advisor answers the record's `question` (below). Rerun once its fix has landed or the spec, children or budget changed; the same cause again is `unclear`. |

**Readiness check:** before merging a `ready` child's PR, read its diff for removed or loosened test assertions and ask the worker why for each; an unexplained one is a problem. If the PR integrated a base branch and dropped changes, it needs the disclosure `accept-pr` requires.

**Spec concerns:** in a `ready` or `blocked` child's `review-*.log`, read only the reviewer's verdict message (the `agent_message` containing `<review>`) and keep its lines starting `Spec concern:`; the phrase elsewhere in the log gives false hits. The advisor triages each: valid and in scope goes through `sandcastle-change-request`, valid but out of scope becomes a follow-up issue, invalid gets one line saying why. For a `ready` child, post them with their triage as one PR comment. They never block a merge.

**Spec blocks:** the advisor resolves them through `sandcastle-change-request`, which owns resolving every conflict and the preflight, then rerun. A moved-path block (`old → new` pairs) is a clarification: update the paths and rerun.

## When something breaks

Every judgment goes to the advisor: problems from the table, spec concerns and spec blocks. Handle the table's other rows yourself. A problem's brief holds the result record or merge refusal, the run's log directory, the state file, and the question. For a merge refusal, it reads the refusal text first; if the refusal came after the merge (`git pull` or `npm ci` failed), it checks the PR state before anyone reruns. It judges by the engineering priorities in `/Volumes/T9/Dev/AGENTS.md` (robustness, then efficiency including token cost, then low upkeep) and the precedents in the state file, and answers with one of:

- `linear`: one obvious fix. Do it without asking.
- `shape`: several workable designs. Take the one with the least machinery and record the choice in the state file. Never ask the user to choose lean vs full; add machinery only after a real failure shows the lean design is unreliable.
- `unclear`: spec intent or product behavior is ambiguous, or the advisor isn't confident. Also anything needing auth or credentials, exceeding the budget, irreversible on `main` (revert, force push), or outside the project's queue. Stop and ask the user with AskUserQuestion, recommended option first, and send a push notification.

Fix code only through these paths, one attempt per issue and cause; the same failure after a fix goes to the user:

- **A ready child's CI fails because of the child, after the one CI-job rerun:** a `worker` commits the smallest fix, from the CI log, on the child branch as a descendant of the reviewed head, a `reviewer` approves it, CI goes green, and merge with `--accept-head <sha>`.
- **`main` is red, or Sandcastle has a defect:** the advisor writes a focused issue (`specs`, checked by a fresh `reviewer`), it runs standalone through Sandcastle and merges through `merge-green`, then the queue resumes. If Sandcastle can't run it, a `worker` makes a hotfix PR in `.worktrees/`, a `reviewer` approves it, and it merges through `merge-green`.
- **A flaky test:** rerun once and record its signature in the state file; the same signature again is a `main` fix.

**Running from Codex:** Codex runs the loop's commands and sends every judgment to the advisor by the `route` skill's Codex route from `<O>`, asking the advisor to carry out a `linear` or `shape` fix itself (specs in its own session, code through `worker` and `reviewer`) and report what it did. The reply's first line must be `linear`, `shape` or `unclear`; anything else counts as `unclear`. Codex never writes specs or code or chooses options. A Claude session escalates as the `route` skill says.

## New work

The project's whole GitHub repository is this thread's work; others may add work at any time. Between runs, never mid-run:

- Take each open issue that isn't queued, labelled `not-ready`, recorded as closed or not planned, or a non-spec, whenever it was created: an Epic loses `not-ready` only once its children are published. Apart from the fix issues under **When something breaks**, this thread writes no specs: a separate `specs` thread publishes them, and an `## Inbox` line is answered by telling the user to run `specs` with it.
- Place it in `## Queue` with a one-line reason, by the ordering rule. Update `Last drain`.
- A new sub-issue of a queued Epic runs on that Epic's next run in GitHub's order. If it belongs earlier, move it among the unstarted children: `gh api -X PATCH repos/<owner>/<repo>/issues/<epic>/sub_issues/priority -F sub_issue_id=<id> -F before_id=<id>` (ids from `gh api repos/<owner>/<repo>/issues/<n> -q .id`). Never move a started child.

**Ordering rule:** fixes that unblock the queue, `main` or Sandcastle first; then work that touches the running Epic's files, after that Epic; then work other items depend on; then the order that avoids rework (land what others build on, not what rewrites fresh code); first in, first out only as a tiebreak.

## Reporting

Write each message as a status update of at most five plain lines, without internal terms (result classes, causes, record fields, log paths) unless asked. Start with what changed, then what's next, then a `Needs you:` line with the decision you need or `nothing`. Give the URL of every PR you mention.

## Guardrails

- Run one issue at a time; babysit threads for different projects take turns on the one operator checkout.
- Merge only Sandcastle's own child PRs, only when green, through `merge-green`, one at a time, while no controller runs.
- Never hand-edit a child branch. The one exception is the child-CI fix above: one worker commit, reviewer-approved, merged with `--accept-head`. Any other new head stops the next run with `drift`.
- Write no code yourself; code goes through the fix paths.
- Link every PR the queue produces (child, fix, hotfix) as soon as it exists: call `link_pull_request` with its URL when available.
- Record every rerun (issue, class, cause; a CI-job rerun counts), the current issue and the queue order in the state file.

## Commands

Run from `<O>`. `Q` stands for `<P>/.scratch/queue-orchestration`, written out in full; `<n>` is the issue, `<pr>` the child PR. Each shell starts fresh, so every command is self-contained.

- **Already running?** If `kill -0 $(cat Q/controller-<n>.pid 2>/dev/null) 2>/dev/null` succeeds, don't launch; report it and give the attach command.
- **Start:** `mkdir -p Q && (nohup npm --silent start -- <n> >> Q/controller-<n>.out 2>&1 < /dev/null & echo $! > Q/controller-<n>.pid)`. After about 20 seconds, check the process is alive and the run started. A run with nothing new to do (replayed decision, `ready` before its merge, `complete`) exits within seconds: read its result instead of reporting a failed start.
- **Result:** `grep '^{"status"' Q/controller-<n>.out | tail -1`.
- **Exit watcher** (background; restart it if it times out while the process lives): `while kill -0 $(cat Q/controller-<n>.pid) 2>/dev/null; do sleep 30; done; grep '^{"status"' Q/controller-<n>.out | tail -1`
- **Attach** (for the user): `cd <O> && npm start -- --attach`, plus `--target <P>`, follows every run and issue of the checkout in one terminal. For a single run: `cd <O> && npm start -- <n> --attach`.
- **Merge:** `node scripts/merge-green.mjs <pr> [--accept-head <sha>]` in `<O>`, plus `--target <P>` for another project (`<sha>`: full 40-character lowercase PR head): checks CI on the PR head, runs the merge gate (Sandcastle only), merges, syncs `<P>`'s `main`; refuses while a controller runs.
- **Preflight:** see the README's preflight section.
- **Cleanup** (no controller running): delete merged child branches: `git -C <P> fetch -q --prune origin; for b in $(git -C <P> branch -r --list 'origin/sandcastle/*' | sed 's|^ *origin/||'); do [ "$(gh pr list -R <owner>/<repo> --head $b --state merged --json number -q length)" = 1 ] && git -C <P> push -q origin --delete $b; done`. Remove leftover `.worktrees/preflight-*` (`git -C <P> worktree remove --force`) and finished issues' spec and scratch dirs in `<O>/.scratch/`; keep the state file and controller output.
