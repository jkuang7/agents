---
name: submit-for-review
description: Prepare and publish current work as a reviewable PR or MR, with coherent commits, verified integration, and a review guide. Use when asked to submit work for review; excludes merging and releasing.
---

# Submit for review

Publish one review request whose commits tell a coherent story and preserve the delivered behavior while integrating the selected base.

The PR or MR should reduce the human's work of understanding. Write connected, easy-to-understand prose that lets a reader unfamiliar with the codebase follow the reasoning to why the change matters. Explain the concrete problem, what causes it, how the change addresses that cause, and what consequence follows. Introduce the context and terms needed for each step before relying on them. Assume the reader has never worked in this codebase. Introduce what the relevant part of the application does, who uses it, and one concrete action. Explain the current flow and the responsibilities that matter, then compare the same action after the change. State what changes, what stays the same, and how that affects the user or maintainer. Define codebase-specific terms when they first appear.

Make the explanation understandable without opening the spec, diff, or linked sources. Use links to support claims and help the reader inspect evidence. Use diagrams to clarify relationships, with prose that explains the causal connections. State assumptions, tradeoffs, and unresolved gaps where they affect the conclusion so the reader can assess the reasoning independently.

Use plain prose and short lists in proposals, review bodies, and handoffs. Preserve technical meaning, evidence links, uncertainty, and authorization boundaries. Use a diagram only when it makes a relationship easier to understand. Do not use tables.

## 1. Ground the submission

For a Sandcastle controller-assigned submission worker, read [SANDCASTLE.md](references/SANDCASTLE.md) first and act as the persistent history-shaper directly. Otherwise, use one persistent history-shaper subagent for investigation, history preparation, verification, and publication. Give it the repository, this skill's path, scope, history policy, user reasoning, and existing authorization. Keep detailed notes with that agent; the parent presents the proposal and final handoff. If delegation is unavailable, report the missing capability.

Resolve the repository that owns the changes and read its instructions. Before reading or publishing issues, follow the [issue tracker contract](../../references/issue-tracker.md). Use named issues as scope, otherwise derive scope from branch evidence and relevant conversation. Live code determines what was delivered; paraphrase intent without publishing private transcripts.

Record the starting branch, HEAD and tree, staged and unstaged changes, source commits, remotes, and existing review. Select the existing review's base, otherwise the user-named base or remote default. Fetch and record exact base and remote head SHAs, the original merge base, and whether human review has started. Inspect both the complete feature diff and upstream changes. Stop if there is nothing to submit.

For a Sandcastle cumulative handoff, read [SANDCASTLE.md](references/SANDCASTLE.md) before planning; its history and issue rules override the ordinary flow. For Local Markdown trackers, read [LOCAL-CLEANUP.md](references/LOCAL-CLEANUP.md) before proposing cleanup.

Grounding is complete when the recorded revisions and checkout state identify the source changes, selected base, existing review, and applicable history and cleanup rules.

## 2. Propose the commit story

Group ordinary submissions by intent and dependency, retaining good grouping. Fold fixes and tests into the change they prove; separate preparatory work when it helps a reviewer understand later behavior. Account for the complete diff, including excluded unrelated changes and orchestration artifacts. Record an old-to-new map for splits, folds, and exclusions.

Present a concise proposal: prior behavior and delivered result, acceptance criteria and constraints, proposed commit order, inclusion/exclusion decisions, fetched base, integration risks, planned history changes, and exact cleanup paths. Keep detailed mappings in a linked preparation note. The proposal is ready when the user can assess scope and consequential actions without reconstructing the diff.

Use existing authorization for cleanup and publication. Ask only for consequential actions it does not cover; identify the proposed action and why approval is needed. Rewriting a published branch after human review has started requires explicit authorization covering that circumstance.

## 3. Prepare and verify

Keep submission work off the default/base branch and other contributors' branches. If starting on the base branch, prepare a distinct `codex/<review-slug>` branch at the source HEAD.

Preserve unrelated uncommitted work and the user's index; never stash implicitly. When unrelated work is present, prepare a separate branch in an isolated worktree and transfer only in-scope changes. If mixed changes cannot be separated reliably, resolve ownership before transferring them. Report which branch and worktree hold the submission; do not reset the original checkout to the result.

Before rewriting or pruning history, create a local unpushed backup at the original HEAD and preserve any in-scope uncommitted content in the preparation worktree. Record the scoped source tree and diff before integration. Rebuild ordinary submissions onto the exact fetched base when integration or regrouping requires it; keep already-good history when neither is needed.

Use `resolving-merge-conflicts` for conflicts and record resolutions by intended behavior. Compare ranges with `git range-diff` and inspect the final diff. Account for every difference from the scoped source. With an unchanged base, require the final tree to equal the scoped source tree; with an advanced base, explain differences caused by integration.

Run required checks on the final candidate. Reuse results only when valid for that tree and environment; rerun affected checks after integration. Verify intermediate commits where practical. Proceed when the preparation worktree is clean, differences are accounted for, and required checks pass.

## 4. Publish

Refresh the base and remote head before pushing. Compare the remote head with the SHA inspected during preparation. If it changed, inspect and reconcile the new work before proceeding; never adopt a newly fetched SHA as a lease merely to permit overwriting it. Reverify any changed candidate. If the base advanced, integrate and recheck once; if it advances again, report the moving base and retain the prepared work.

Push new or fast-forward branches normally. For an authorized rewrite, use `--force-with-lease=<ref>:<inspected-sha>` with the reconciled remote head. On lease failure, reassess remote changes rather than refreshing and retrying blindly. Verify that the remote head matches the verified candidate.

Before drafting or revising the PR or MR body, read [REVIEW-GUIDE.md](references/REVIEW-GUIDE.md) for its structure, implementation links, commit review order, and evidence requirements. The body is ready when it states the prior problem and delivered change, and every main review risk has an implementation link and test evidence or an explicit evidence gap.

Link delivered issues, using confirmed close-on-merge references for ordinary submissions; leave remote parent specs open. Apply the Sandcastle issue rules when applicable. Update the existing open PR or MR, or create one if absent. Read back the published body and verify its links and candidate revision. Publication is complete when the forge returns a canonical URL and the published body matches the checked draft. Do not merge, release, deploy, or message others without separate authorization.

## 5. Hand off

Perform applicable local cleanup after confirmed publication. Return the canonical URL, a short behavior summary and review order, check results, and material caveats. Report rewrites, backup/preparation locations, and cleanup outcomes. Keep detailed evidence in the preparation note and review guide rather than repeating them in chat.

Complete when the verified candidate matches the remote, has one open review request, and applicable authorized cleanup is finished. On partial failure, distinguish what succeeded from what remains, preserve recovery artifacts, and report the next step without claiming full completion.
