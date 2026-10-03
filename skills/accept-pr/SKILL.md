---
name: accept-pr
description: Merge a PR and clean up after it. Use when the user asks to accept or merge a PR, or when standing instructions authorize merging a task's own verified PR. Not for reviewing or preparing a PR.
---

# Accept a PR

## Target and authorization

Merge only a PR you can name exactly: a URL or number from the user, the PR this conversation submitted, or the single open PR whose repository, branch and head match the candidate this conversation established. If more than one is plausible, ask. If only unsubmitted changes exist, there is nothing to accept; submit first.

The merge is authorized by the user's request, or by workspace or repository instructions that authorize merging a task's own completed work. Reviewing or submitting a PR doesn't authorize merging it, and discussing or editing this skill isn't a request to use it.

## Merge

1. Read the PR's head SHA, target branch and checks. Wait for required checks: right after a push none are registered yet, so "no checks reported" means wait, not done. Use `gh pr checks <pr> --watch --required`, retrying until the branch protection's required checks (`gh api repos/<repo>/branches/<base>/protection/required_status_checks`) appear and pass. Stop if one fails, or if the PR needs conflict resolution or another change; prepare and verify that change separately, then start again.
   If the PR integrated a base branch and resolved a conflict by dropping one side's changes, its merge commit message and description must name each dropped change (commit or PR), say why dropping it is safe, and say whether its tests were kept, and its final review must have examined the dropped side. Stop if any is missing.
2. Merge with the repository's usual strategy and the host's head guard (`gh pr merge <pr> --match-head-commit <sha>`), so a head that moved after you checked it is refused. Never bypass branch protection.
3. Confirm that the host reports the PR merged. A queued or local merge isn't done.

## Issues

Follow [the issue lifecycle](../submit-for-review/references/ISSUE-LIFECYCLE.md). Closing keywords close delivery issues on merge; don't close them by hand.

## Clean up

Start only after step 3 confirms the merge, in separate commands from the merge, never chained with `;`: a refused or failed merge leaves the branch, worktrees and checkout exactly as they were. Unless the user asked to keep them:

- Delete the PR's remote head branch when it's in the PR's own repository and no other open PR targets it.
- If the primary checkout is on the head branch, switch it to the target branch first.
- Remove worktrees checked out on the head branch with `git worktree remove`, and delete the local branch with `git branch -d`. Both refuse when tracked or untracked work would be lost: leave it and report why instead of forcing. `git worktree remove` does delete ignored files silently, so first list them (`git -C <worktree> status --ignored --short`) and keep the worktree if any are user data rather than build output, dependencies or caches. After a squash or rebase merge `git branch -d` refuses even merged work; force-delete only when the branch tip equals the head SHA that was merged.
- Fast-forward the primary checkout of the target branch with `git pull --ff-only` when it has no local changes; otherwise leave it and report.

## Report

One line: the PR link, the merge result, and what was removed or kept and why. A failed cleanup doesn't undo a confirmed merge.
