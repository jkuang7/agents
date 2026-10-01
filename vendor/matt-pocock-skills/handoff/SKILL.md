---
name: handoff
description: Compact the current conversation into a pasteable Markdown handoff so the user can clear context and resume in a fresh session. Use when the user asks for a handoff or to pass context to another thread.
argument-hint: "What will the next session be used for?"
---

# Handoff

The user will copy your handoff, clear the conversation, and paste it as the first message of a fresh session. That session sees only the pasted text plus what it can read from disk. Write a synthesis that lets it continue the present objective without replaying the conversation. Tailor it to any focus supplied by the user.

## Handoff content

Preserve:

- Current objective, problem framing, scope, governing constraints, and meaningful user preferences, including how the user wants to work.
- Settled decisions and rationale needed to prevent reconsideration; rejected directions only when their reasons prevent backtracking.
- Current artifacts, work state, and evidence: absolute working directory, repository, branch, HEAD, owned uncommitted changes, key files by absolute path, and commands with their results.
- Genuine open questions, competing options, assumptions, and remaining work.
- The next action or decision, conditional when not yet committed.

Be decisive about settled choices and explicit about uncertainty. Knowledge that exists only in this conversation (user preferences, conclusions, failed attempts, gotchas discovered) must be stated in the handoff. Reference authoritative specs, plans, issues, ADRs, commits, and diffs by path or URL instead of copying them. Redact secrets and sensitive personal information.

## Continuation record

For ongoing work, read [CONTINUATION.md](CONTINUATION.md) and refresh its workflow-owned record, then point to it from the handoff. The pasted handoff must still stand alone for orientation and the next action; the record holds detail too long to paste. When the two differ, the record and live state take precedence over the pasted text. For a disposable conversation transfer with no unfinished task, skip the record.

## Output

Return the handoff in your reply as one fenced block tagged `markdown`, with an outer fence longer than any fence inside it (usually four backticks), so nested code fences survive copying. Put nothing inside the block that is addressed to the current user. Begin the block with a line telling the new session that it is resuming prior work, then end it with:

- Suggested skills for the next steps, by name.
- A resume instruction: read the referenced record, when one exists, and requirements, then reconcile recorded branch, HEAD, dirty work, and evidence with live state before editing.

After the block, give the record's absolute path when one was written.

Completion requires a pasteable block containing a usable objective, settled direction, open loops, present state, supporting evidence, next action, and work to preserve. Transfer does not establish completion of the underlying task.
