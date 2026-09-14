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
- Any existing review for the candidate.

Inspect the candidate's status, commits, and complete diff. Preserve unrelated work. Investigate more history only when these facts or a material risk remain unclear. Stop if there is nothing to submit.

## Shape the commit story

Preserve commit boundaries that already tell a coherent story. Each commit should represent one understandable part of the delivered change, grouped by purpose rather than file type.

When history obscures the change, reorganize it only if current authorization permits the rewrite and the result will reduce review work. Do not rewrite good history for appearance. Do not rewrite a published branch after human review has started without explicit authorization.

## Verify the candidate

Run the repository's required checks on the final candidate. Re-run affected checks after any integration or history change that changes the tree. Record the exact candidate revision, results, and material evidence gaps.

## Write for the reviewer

Read [REVIEW-GUIDE.md](references/REVIEW-GUIDE.md) before drafting the review body.

Scale the body to the change. Give a technically capable reviewer enough information to understand:

- The concrete problem before the change.
- The delivered behavior and why it solves that problem.
- Important boundaries or invariants.
- The most useful code and test locations to inspect.
- Verification results and material evidence gaps.
- Commit review order when it helps.

Use concise prose and short lists. Use a diagram only when it makes a relationship easier to understand. Keep preparation history out of the main review narrative unless it affects trust in the candidate.

## Publish and hand off

Push the candidate and create or update its review request against the selected base. Confirm that the remote revision matches the verified candidate and read back the published title and body. Do not merge or release without separate authorization.

If publication includes authorized cleanup for a local Markdown tracker, follow [LOCAL-CLEANUP.md](references/LOCAL-CLEANUP.md).

Return the canonical review link, candidate revision, concise commit order, verification results, and material caveats.
