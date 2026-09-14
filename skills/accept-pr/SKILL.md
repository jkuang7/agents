---
name: accept-pr
description: Accept and merge a specific PR when the user explicitly asks to accept or merge it. Do not use for review or preparation alone.
---

# Accept a PR

Given explicit user authorization to accept a PR, verify the exact PR, merge it
safely, confirm the host recorded the merge, synchronize the primary checkout,
and clean up only artifacts proven to belong to that accepted change.

## Verify the acceptance target

Resolve the repository, PR, remote, and target branch from the request and
repository metadata. Follow repository instructions before reading linked
issues or specifications. An acceptance or merge request authorizes this
workflow. Reviewing, preparing, or submitting a PR does not.

Fetch current remote refs. Inspect the PR's state, head SHA, target branch,
mergeability, required checks, and reviews. Record the exact head SHA. Stop if
the target is ambiguous, the PR changed after inspection, required checks have
not passed, or repository policy blocks the merge.

## Merge and confirm

Immediately before merging, read the PR head again and require it to equal the
recorded SHA. Use the host's expected-head option when available. Then use the
repository's supported merge path and strategy without bypassing branch
protection. Preserve unrelated local work. If the PR needs conflict resolution
or another material change, prepare and verify that change separately, then
inspect and record the new head before merging.

After the merge request completes, read fresh host state. Completion requires
the host to report the PR as merged and provide the recorded merge commit. A
queued merge, local merge, or successful push is not enough.

## Synchronize and clean up

Fetch the recorded merge and locate the primary checkout for the PR's target
branch. Fast-forward that checkout to its remote branch only when doing so
preserves local commits and working-tree changes. Never reset or discard work
to synchronize it. If local state prevents a safe fast-forward, preserve it and
report the checkout as unsynchronized.

Treat cleanup as optional unless ownership is proven. A matching name alone is
not proof. For each candidate worktree or local branch, verify its path, branch,
tip, relationship to the accepted PR head, and absence of unique tracked,
untracked, or ignored files. Remove only a clean worktree whose contents are
included in the accepted change. Delete its local branch with the non-forcing
form only. Retain anything uncertain or anything Git refuses to delete.

Leave remote branches and active processes alone. Their deletion or termination
requires a separate explicit request and fresh ownership checks.

## Report

Report the PR link, inspected head SHA, recorded merge commit, checks, primary
checkout synchronization, and each removed or retained artifact with its
reason. State any blocker without claiming the workflow completed.
