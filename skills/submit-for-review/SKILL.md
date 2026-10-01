---
name: submit-for-review
description: Turn a verified candidate into a concise, reviewable PR or MR without merging or releasing it.
---

# Submit for review

Turn a verified candidate into a PR or MR that minimizes the human reviewer's cognitive load.

## Ground the submission

Read the repository instructions and identify:

- The candidate and its current branch or revision.
- The target base.
- The delivered scope and relevant issue or spec.
- Any existing review and the remote head inspected with the candidate.

Inspect the candidate's status, commits, and complete diff. Preserve unrelated work. Investigate more history only when these facts or a material risk remain unclear. Stop if there is nothing to submit.

## Shape the commit story

Preserve commit boundaries that already tell a coherent story. Each commit should represent one understandable part of the delivered change, grouped by purpose rather than file type.

When history obscures the change, a submission request implicitly authorizes
rewriting only unpublished local candidate commits that are proven to belong to
the current task. Treat commits as unpublished only when they are not reachable
from any remote ref, have never been pushed or shared for review, and are not
known to be based on another contributor's work. Preserve the candidate's content
and unrelated history. If any condition is uncertain, preserve the history.

Rewriting published history requires explicit authorization for the rewrite,
such as a request to rebase, squash, amend, or force-update that branch. A request
to submit, push, create a PR, or update an existing PR does not provide that
authorization. Do not rewrite good history for appearance.

## Verify the candidate

Run the repository's required checks on the final candidate, leaving any suite that CI or a controller runs on it to them. Re-run affected checks after any integration or history change that changes the tree. Record the exact candidate revision, results, and material evidence gaps.

## Write for the reviewer

Read [REVIEW-GUIDE.md](references/REVIEW-GUIDE.md) before drafting the review body.

## Publish and hand off

Immediately before publishing, fetch the remote branch and compare its head with the inspected SHA. If it changed, reconcile that work and reverify the changed candidate. For an authorized rewrite, use `--force-with-lease` against the exact remote SHA from the final inspection. If the lease fails, stop and reassess instead of refreshing it and retrying blindly.

Push the candidate and create or update its review request against the selected
base. Choose closing references by [the issue lifecycle](references/ISSUE-LIFECYCLE.md).

Confirm that the remote revision matches the verified candidate and read back the published title, body, and canonical review URL. Submission is complete only when the verified candidate commits are the head of that exact PR or MR; do not present a local-only commit or a branch link as submitted. Merging is separate: use `accept-pr` when the user or standing instructions authorize it.

If publication includes authorized cleanup for a local Markdown tracker, follow [LOCAL-CLEANUP.md](references/LOCAL-CLEANUP.md).

Lead the handoff with a clickable canonical PR or MR link whose remote head
equals the reported candidate revision. Then give the candidate revision,
concise commit order, verification results, and material caveats.
