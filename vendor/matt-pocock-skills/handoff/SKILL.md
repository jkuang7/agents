---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff document so a fresh agent can continue the work from the conversation's present state. Synthesize the result rather than narrating the conversation in order.

Build the handoff around these distinctions:

- **Core objective.** State what the user is trying to accomplish now, even when it differs from the opening request.
- **Problem framing.** Capture the established view of the problem, including important constraints and "should be" or "shouldn't be" principles.
- **Convergence.** Where the evidence favors a direction, state the current thesis, recommendation, architecture, or design shape. Keep alternatives live only when the conversation has not resolved them.
- **Decisions and commitments.** Treat settled choices as settled. Include rationale when it prevents needless reconsideration or later work depends on it.
- **Open loops.** Separate unresolved questions, competing options, missing information, and requested experiments from points that appeared earlier but are now settled.
- **Rejected or superseded directions.** Preserve a discarded direction and its reason only when that context prevents backtracking.
- **Current state.** Describe the artifact, plan, design, argument, or code as it exists now.
- **User intent and judgment.** Retain meaningful preferences, standards, tradeoffs, and objections that should guide later choices.
- **Next frontier.** Identify the next likely decision or action. Present it as conditional when the user has not committed to it.
- **Uncertainty.** Be decisive where the discussion has converged and explicit about remaining ambiguity.

For ongoing work, read [CONTINUATION.md](CONTINUATION.md), then update or reuse its durable record and return the absolute path. For a disposable conversation transfer with no unfinished task, an OS temporary file is sufficient; disclose that it is temporary.

Include a "suggested skills" section naming relevant skills and when they apply. Supply a continuation prompt that points to the record and tells the next agent to reconcile it with live state before proceeding.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.

Complete when the saved document lets a fresh agent recover the current objective, settled direction, genuine open loops, present work state, next action and its supporting evidence, and work to preserve. Confirm that the returned path resolves. A handoff transfers work; it does not establish completion of that work.
