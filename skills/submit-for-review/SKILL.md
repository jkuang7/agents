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

When history obscures the change, reorganize it only if current authorization permits the rewrite and the result will reduce review work. Do not rewrite good history for appearance. Do not rewrite a published branch after human review has started without explicit authorization.

## Verify the candidate

Run the repository's required checks on the final candidate. Re-run affected checks after any integration or history change that changes the tree. Record the exact candidate revision, results, and material evidence gaps.

## Write for the reviewer

Read [REVIEW-GUIDE.md](references/REVIEW-GUIDE.md) before drafting the review body.

## Publish and hand off

Immediately before publishing, fetch the remote branch and compare its head with the inspected SHA. If it changed, reconcile that work and reverify the changed candidate. For an authorized rewrite, use `--force-with-lease` against the exact remote SHA from the final inspection. If the lease fails, stop and reassess instead of refreshing it and retrying blindly.

Push the candidate and create or update its review request against the selected base. Use a close-on-merge reference only for an issue this candidate delivers and is intended to close. Link parent specs or Epics without closing them unless the requested submission includes closure. Submission otherwise leaves issue state unchanged.

Confirm that the remote revision matches the verified candidate and read back the published title and body. Do not merge or release without separate authorization.

If publication includes authorized cleanup for a local Markdown tracker, follow [LOCAL-CLEANUP.md](references/LOCAL-CLEANUP.md).

Return the canonical review link, candidate revision, concise commit order, verification results, and material caveats.
