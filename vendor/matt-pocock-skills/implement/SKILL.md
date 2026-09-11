---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
---

Implement the work described by the user in the spec or tickets.

Before tracker operations, follow the [issue tracker contract](../../../references/issue-tracker.md).

When the source is an issue, read its full body and comments before implementation. Reuse settled requirements and test seams. Resolve factual gaps from the repository; identify only consequential choices that existing intent cannot settle.

## Establish the candidate

Record the starting branch, HEAD, and staged, unstaged, and untracked work. Establish which changes belong to this task and preserve unrelated work and the user's index. Record an explicit review base before editing. Use the supplied base for existing branch work; for a new local change, the starting HEAD is the base. Resolve ownership before including mixed changes that cannot be separated reliably.

For sustained work, a blocked exit, or a session transfer, use [continuation records](../handoff/CONTINUATION.md). Reuse an existing workflow record. On resume, reconcile it with live requirements and checkout state before editing.

## Implement and verify

Use /tdd where possible, at pre-agreed seams. Run focused tests and typechecking as changes develop. Run the repository's required checks and the full suite on the completed candidate. Record commands, outcomes, environment limits, and the candidate they verify. A baseline failure remains an evidence gap; it does not establish that the candidate passes.

## Review, correct, and finish

Use /code-review with the recorded base, authoritative requirements, in-scope changes, and verification evidence. Name the candidate mode explicitly: the current working tree, including relevant new files, or a particular committed revision. Pause edits while it is reviewed, or provide an isolated snapshot. A HEAD-only diff cannot review uncommitted implementation.

Resolve actionable findings. Rerun affected checks after corrections and obtain review of the changed areas when they could invalidate the earlier verdict. Account for unresolved findings explicitly; a correctness blocker means the work is incomplete. Evidence may be reused only while its candidate contents and relevant environment remain valid.

Commit only the verified in-scope work on the task branch, preserving unrelated changes. Inspect the committed diff and confirm it matches the reviewed candidate; any hook or other change to the contents requires affected verification and review again. Report the commit, delivered outcomes, check results, and remaining limitations. Update the continuation record if work remains. Complete when acceptance is supported by evidence for the delivered candidate and review findings are resolved or explicitly accounted for.
