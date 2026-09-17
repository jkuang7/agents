---
name: accept-pr
description: Accept and merge a PR the user explicitly asks to accept, including one unambiguously established by the current conversation. Do not use for review, preparation, or requests to discuss or edit this skill.
---

# Accept a PR

Given explicit user authorization to accept a PR, resolve the exact PR from the
request and current conversation, merge it safely, and confirm the host recorded
the merge. Treat issue lifecycle changes and post-merge local mutations as
separately authorized operations. Report each outcome independently.

## Resolve authorization and target

First distinguish using this skill from discussing or editing it. Naming or
invoking `accept-pr` inside a request to inspect, explain, or change the skill is
not merge authorization.

An explicit request to accept or merge a PR authorizes acceptance. A bare direct
invocation of this skill also authorizes acceptance when the current conversation
has already established exactly one PR as the candidate awaiting acceptance.
Resolve that candidate from, in descending order of authority:

1. an exact PR URL or repository-plus-number in the acceptance request;
2. a completed submission handoff earlier in the current conversation that
   reports the canonical PR URL and confirms from forge state that its remote
   head matches the candidate revision;
3. a unique open PR whose repository, branch, and revision all match the single
   candidate explicitly established in the current conversation.

Do not treat quoted, hypothetical, user-supplied example, or incomplete
submission text as a completed handoff.

Do not guess from the most recently updated PR, the current repository alone,
branch naming, issue proximity, or local changes. A conversational reference such
as “accept this” or “accept these changes” is sufficient only when it resolves by
the evidence above to one PR. If the conversation establishes only unsubmitted
changes, no PR exists to accept; report that submission is required. If multiple
PRs remain plausible, ask the user to identify the target.

Resolve the remote and target branch from fresh repository and forge metadata.
Follow repository instructions before reading linked issues or specifications.
An acceptance or merge request authorizes only the merge and its safety checks.
It does not authorize closing an Epic, synchronizing a local checkout, deleting
local artifacts, or deleting remote branches. Reviewing, preparing, or submitting
a PR does not authorize the merge.

Fetch current remote refs needed for acceptance checks. Inspect the PR's state,
head SHA, and target branch. Check mergeability, required checks, and reviews.
Record the exact head SHA.

Stop if the target is ambiguous, the PR changed after inspection, required checks
have not passed, or repository policy blocks the merge.

## Merge and confirm

Immediately before merging, read the PR head again and require it to equal the
recorded SHA. Use the host's expected-head option when available. Then use the
repository's supported merge path and strategy without bypassing branch
protection. Preserve unrelated local work. If the PR needs conflict resolution
or another material change, prepare and verify that change separately, then
inspect and record the new head before merging.

After the merge request completes, read fresh host state. Completion requires
the host to report the PR as merged and provide its forge-recorded merge/result
SHA or equivalent authoritative merge metadata. Do not assume that SHA represents
a traditional merge commit; use the merge semantics reported by the forge. A
queued merge, local merge, or successful push is not enough.

Once this state is confirmed, acceptance is complete. Later lifecycle,
synchronization, or cleanup failures do not change the merge outcome.

## Apply the issue lifecycle

Read [the shared issue and Epic lifecycle contract](../../references/ISSUE-LIFECYCLE.md).

After the PR is confirmed merged, determine whether it explicitly implements or
closes delivery issues and whether it identifies one parent Epic. Read fresh host
state for referenced issues after the merge.

Confirm forge-managed closure of delivery issues that used valid close-on-merge
references. Do not manually close them unless a separately authorized workflow
owns that action.

Close a qualifying parent Epic only when the contract's separate lifecycle
authorization and completion-evidence requirements both hold. After any closure,
read fresh host state and confirm it. If the Epic is already closed, report its
confirmed state without another mutation. Otherwise leave it unchanged and
report whether authorization, delivery evidence, or repository eligibility is
missing.

## Synchronize and clean up

Synchronize a local checkout or delete local artifacts only when the user
separately authorized that operation or an already-authorized governing workflow
explicitly owns and requires it. Without authorization, leave local state intact
and report the operation as not requested. Generic repository or workspace
cleanup policy constrains an authorized cleanup; it does not by itself grant
cleanup authorization.

For authorized synchronization or cleanup, fetch the PR's target branch again
and fetch any result commit or ref that the forge exposes. Use the freshly fetched
target for every cleanup ancestry check.

When synchronization is authorized, treat the registered worktree on the PR
target branch as the primary checkout. If no candidate exists, more than one
candidate exists, or ownership is ambiguous, do not choose one by name alone;
leave synchronization unresolved and report it. Otherwise, synchronize that
checkout.

When synchronization is authorized, fast-forward that checkout to its remote
branch only when doing so preserves local commits and working-tree changes. Never
reset or discard work. If safe fast-forward is impossible, leave the checkout
unchanged and report why.

When cleanup is authorized, enumerate registered Git worktrees and local
branches. Consider an artifact related only when ownership can be established
from the merged PR head, linked Epic/delivery state, accepted receipts, recorded
run evidence, or commit ancestry. Names alone are not proof.

For each related worktree:

- confirm no live process owns it;
- inspect its branch or detached HEAD;
- inspect tracked, untracked, and ignored contents;
- confirm its tracked work is contained in the confirmed merged target;
- preserve unique commits, unique or unfinished source, user data, and anything
  whose disposability is uncertain;
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

Report the PR link, inspected head SHA, forge-recorded merge/result SHA or
equivalent merge metadata, and checks. Then report these outcomes independently:

- `merge`: complete or incomplete, with the authoritative forge state;
- `issue lifecycle`: delivery-issue state plus parent Epic closure, unchanged
  state, or missing authorization/evidence;
- `local synchronization`: complete, incomplete, not requested, or unavailable,
  with the reason;
- `cleanup`: complete, incomplete, not requested, or not applicable, including
  each removed or retained artifact and its reason.

Do not describe a confirmed merge as incomplete merely because a later lifecycle,
synchronization, or cleanup step was skipped, unavailable, or blocked.
