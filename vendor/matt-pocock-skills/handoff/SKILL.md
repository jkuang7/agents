---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

# Handoff

Save a synthesis that lets a fresh agent continue from the present objective, rather than replaying the conversation. Tailor it to any focus supplied by the user.

Preserve:

- Current objective, problem framing, scope, governing constraints, and meaningful user preferences.
- Settled decisions and rationale needed to prevent reconsideration; rejected directions only when their reasons prevent backtracking.
- Current artifacts, work state, and evidence.
- Genuine open questions, competing options, assumptions, and remaining work.
- The next action or decision, conditional when not yet committed.

Be decisive about settled choices and explicit about uncertainty. Reference authoritative specs, plans, issues, ADRs, commits, and diffs instead of copying them. Redact secrets and sensitive personal information.

For ongoing work, read [CONTINUATION.md](CONTINUATION.md) and reuse its workflow-owned record. For a disposable conversation transfer with no unfinished task, an OS temporary file suffices; disclose its temporary nature.

Supply relevant suggested skills and a continuation prompt pointing to the record and requiring reconciliation with live state. Return a resolving absolute path. Completion requires a usable objective, settled direction, open loops, present state, supporting evidence, next action, and work to preserve. Transfer does not establish completion of the underlying task.
