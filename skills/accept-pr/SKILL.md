---
name: accept-pr
description: Accept and merge a specific PR when the user explicitly asks to accept or merge it. Do not use for review or preparation alone.
---

# Accept a PR

Given explicit user authorization to accept a PR, verify the exact PR, merge it
safely, confirm the host recorded the merge, close its unambiguously linked parent
Epic when eligible, synchronize the primary checkout, and clean up only artifacts
proven to belong to that accepted change.

## Verify the acceptance target

Resolve the repository, PR, remote, and target branch from the request and
repository metadata. Follow repository instructions before reading linked
issues or specifications. An acceptance or merge request authorizes this
workflow. Reviewing, preparing, or submitting a PR does not.

Fetch current remote refs needed for acceptance checks. Inspect the PR's state,
head SHA, target branch, mergeability, required checks, and reviews. Record the exact head SHA. Stop if
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

## Close the linked Epic

After the PR is confirmed merged, determine whether it explicitly implements or
closes one parent Epic. Use repository metadata and the PR body to resolve the
Epic. Branch names or issue proximity alone are not proof.

Close that Epic only if it is open, the merged PR explicitly identifies it as the delivered parent, and repository policy and the user's instructions permit closure.

Do not close child issues here unless separately required; their lifecycle belongs
to the delivery workflow. After closing the Epic, read fresh host state and
confirm it is closed. If the Epic is already closed, report its confirmed state
without another mutation.

If the PR is not tied unambiguously to one Epic, leave the Epic unchanged and
report that manual follow-up is required. If another closure condition fails,
leave it unchanged and report the reason. Preserve any explicit user instruction
to keep the Epic open.

## Synchronize and clean up

After the merge is confirmed, fetch the recorded merge and the PR's target
branch again. Use that freshly fetched target for every cleanup ancestry check.

Treat the registered worktree on the PR target branch as the primary checkout.
If no candidate exists, more than one candidate exists, or ownership is ambiguous,
do not choose one by name alone; leave synchronization unresolved and report it.
Otherwise, synchronize that checkout.

Fast-forward that checkout to its remote branch only when doing so preserves
local commits and working-tree changes. Never reset or discard work. If safe
fast-forward is impossible, leave the checkout unchanged and report why.

Then clean up local artifacts belonging to the accepted PR/Epic.

Enumerate registered Git worktrees and local branches. Consider an artifact
related only when ownership can be established from the merged PR head, linked
Epic/delivery state, accepted receipts, recorded run evidence, or commit ancestry.
Names alone are not proof.

For each related worktree:

- confirm no live process owns it;
- inspect its branch or detached HEAD;
- confirm its tracked work is contained in the confirmed merged target;
- preserve unique commits or unfinished source;
- remove it with `git worktree remove`;
- use force only when remaining files are proven disposable and no retention
  requirement applies.

Process nested related worktrees before their parents.

For each related local branch:

- confirm no registered worktree uses it;
- confirm its tip is contained in the freshly fetched merged target;
- delete it normally when possible;
- use force deletion only after independently proving its tip is already contained
  in the merged target and Git is refusing solely because of stale HEAD/upstream
  bookkeeping.

Confirm removed worktree registrations, paths, and local branch refs are gone.

Do not delete remote branches or terminate processes unless separately authorized.
Leave anything uncertain in place and report it.

## Report

Report the PR link, inspected head SHA, recorded merge commit, checks, linked
Epic and its confirmed closure or reason for leaving it unchanged, primary
checkout synchronization, and each removed or retained artifact with its reason. State any blocker without claiming the workflow completed.
