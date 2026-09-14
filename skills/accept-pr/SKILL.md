---
name: accept-pr
description: Accept and merge a PR, resolve integration conflicts from project context, and remove obsolete worktrees and branches tied to the accepted change.
---

# Accept a PR

Finish with the accepted PR merged, the primary checkout clean on the current
remote integration branch, and obsolete worktrees and branches for that change
removed. An explicit acceptance or merge request authorizes this workflow,
including cleanup of worktrees and branches proven to belong to the accepted
change. A cleanup-only request starts from an already merged PR. Reviewing or
preparing a PR alone does not authorize merging it.

## Establish scope

Resolve the repository, PR, remote, and base branch from the conversation and
repository metadata. Follow applicable repository and issue-tracker instructions
before reading linked issues. Use explicit repository arguments for tracker
operations. Use the actual integration branch if the repository uses a name
other than `main`; a PR targeting a release branch does not authorize promoting
it to `main`.

Fetch current remote refs. Inspect the PR state, head SHA, checks, reviews, and
linked specification. Read `git worktree list --porcelain`, branch tracking, and
each relevant worktree's tracked and untracked changes. Tell the user the
absolute paths of the primary and PR worktrees.

Map cleanup candidates to the accepted change using PR heads, commit ancestry,
branch tracking, and repository metadata. A matching name is a clue, not proof
that a branch or worktree can be deleted. Check whether another open PR or active
process still uses each candidate. Completion means every candidate has a
recorded path, branch, tip, and reason it belongs to this change.

## Integrate and verify

If the PR is already merged, fetch the merge result and proceed to synchronization
and cleanup. Otherwise, honor the repository's merge strategy and required
checks. Use a merge commit when no policy or user preference chooses another
strategy. Bind the merge to the inspected PR head, and recheck if that head
changes. Never bypass branch protection.

Preserve existing work. Include local changes when the session authorizes
committing them; otherwise leave unrelated changes in their checkout and
integrate in an isolated worktree. Avoid destructive resets, broad staging of
unrelated files, and force pushes as shortcuts to a clean checkout.

For conflicts, apply
[resolving-merge-conflicts](../resolving-merge-conflicts/SKILL.md). Read both
sides' commits, the accepted spec and discussion, and relevant architecture or
domain docs. Preserve both intents where compatible. Resolve routine
implementation choices from that context; ask only when incompatible product
behavior remains undecidable. Stage the resolved files explicitly, finish the
merge or rebase, and verify the combined result.

Run the repository's required checks and tests appropriate to the integrated
changes. Reuse successful verification for the same integrated revision when no
relevant inputs have changed. If verification is blocked, report the concrete
failure and resolve it before claiming completion. Inspect the staged diff for
generated artifacts; keep reusable configuration tracked and local worktrees,
logs, build outputs, and scratch drafts ignored. Ignore rules do not untrack
existing files: remove obsolete tracked artifacts from the index explicitly,
preserving local copies when useful. Verify the committed ignore rules work
without relying on machine-local exclusions.

Publish the authorized integration through the repository's supported merge
path. Confirm that the host reports the PR as merged. A queued merge is still
pending; a local merge or successful push alone does not prove that the host has
recorded acceptance.

## Synchronize and clean up

Operate from the primary checkout or another directory outside all removal
candidates. Fetch the merge result, switch the primary checkout to the
integration branch, and fast-forward to its remote tracking branch. If local
commits diverge, account for and integrate authorized work rather than resetting
it away. Preserve unrelated dirty work and explain any remaining obstacle to a
clean primary checkout.

Before removing each candidate, verify:

- The PR is merged and the candidate's work is included in the integration
  branch. Prefer `git merge-base --is-ancestor <tip> <remote-base>`. For squash
  or rebase merges, inspect patch equivalence and the recorded merged PR head; a
  branch name or merged PR alone cannot establish that later commits are
  disposable.
- Tracked and untracked files contain no unique work. Inspect ignored files too;
  worktree removal may delete ignored files. Generated caches may go with the
  obsolete worktree, while unique artifacts and credentials must be preserved
  outside it.
- No active process or other open PR still needs it. Stop a process only after
  confirming that it belongs to the accepted change and must stop for cleanup,
  then recheck status and tips.

Remove verified candidates with `git worktree remove <exact-path>`, then delete
their local branches with `git branch -d <exact-name>`. If a squash merge
requires `-D`, first establish and report equivalence and the absence of unique
commits. Never use forced worktree removal to discard unknown files. Delete
obsolete branches from the repository's remote only after verifying that their
current tips are the inspected tips, using an exact ref and an expected-tip
lease. Leave fork or unrelated remote branches alone unless explicitly included.

Prune stale remote refs and worktree registrations after removal. Preserve any
unique logs or recovery records before removing their worktree. Do not
recursively delete a broad parent directory.

## Completion

Verify all of the following from fresh Git and host state:

- The PR is merged, with its merge SHA recorded.
- The primary checkout is on the integration branch, its HEAD equals the current
  remote tip, and `git status --porcelain` is empty.
- Each obsolete worktree and local or remote branch selected for cleanup is
  gone. Any retained candidate has a concrete preservation reason.

Report the PR, final SHA, checks, and removed worktree paths and branches. State
unresolved blockers directly; do not claim a clean or synchronized checkout
when preserved work prevents it.
