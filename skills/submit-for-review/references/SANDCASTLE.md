# Sandcastle cumulative submission

A Sandcastle handoff supplies a cumulative branch, verified head, accepted child commits, parent epic, and any controller pre-authorization.

Verify the source matches the supplied head and every accepted commit is ancestral. Preserve existing commit boundaries, cumulative merges, and accepted ancestry. Explain commits in recorded order; the source commit map is an identity map. If source contents conflict with submission scope, return the discrepancy to the controller instead of pruning accepted history.

Integrate the fetched base with a non-rewriting `--no-ff` merge when it is not already ancestral. Resolve conflicts by intent, verify the resulting tree, rerun affected checks, and reconfirm accepted ancestry. Push normally; stop if publication would require rewriting history.

The controller has already closed accepted children and their parent epic. Link them without closing keywords and leave their state unchanged.

For an automatic handoff, write the proposal to the durable submission transcript and continue under the controller's explicit pre-authorization. That authorization covers only its stated publication and cleanup scope, never a rewrite or force push.

## Sandcastle worker compatibility

A dedicated submission worker dispatched by the controller already provides the persistent history-shaper context; it executes this skill directly without spawning a nested subagent. Keep the proposal, evidence, and final handoff in the controller-supplied transcript. Read the skill and this reference from their mounted paths.

The controller runs a separate fresh Epic Audit before submission. Require its successful result for the supplied source tip. Work in the controller-supplied submission branch and worktree, preserving the Epic Branch, Epic Worktree, and runtime state. On retries inspect retained preparation and the existing PR before continuing; update the same open PR. Integrate additional accepted source history by merge, preserving ancestry. Stop on a closed or merged prior PR for that submission branch and report it to the controller.

Controller authorization covers normal pushes of the named submission branch and creating or updating its PR, including the review guide. It excludes force pushes, history rewriting, merging the PR, issue mutations, and cleanup of runtime or local-tracker artifacts unless separately named. Complete only after required full verification passes at the candidate tip and the forge confirms an open PR for that exact remote head. If the skill, credentials, audit evidence, or publication is unavailable, retain recovery artifacts and report incomplete.

In Docker, resolve repository files from the current sandbox checkout; host worktree and transcript paths are controller metadata and may not be mounted at those paths. The controller captures your response stream as the durable transcript. Configure Git authentication with `gh auth setup-git` using the injected token. For an SSH origin without SSH credentials, use a container-global HTTPS `url.<base>.insteadOf` rule for that host; preserve the repository remote URL and never print credentials.
