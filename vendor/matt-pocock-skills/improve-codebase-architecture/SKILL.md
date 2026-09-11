---
name: improve-codebase-architecture
description: Delegate a codebase architecture scan and HTML report to a subagent, return the file, then grill through whichever opportunity you pick.
disable-model-invocation: true
---

# Improve Codebase Architecture

Keep the scan and report generation in a subagent context so the main task retains room for the user's decisions.

## 1. Delegate the review

Resolve the target repository and pass its absolute path, the user's requested scope or pain point, and any relevant constraints to one subagent. If the target is ambiguous, clarify it before dispatching.

Use a fresh context (`fork_turns="none"` when supported), with a concise brief rather than the conversation history. Give the subagent the absolute path to [REVIEW-WORKER.md](REVIEW-WORKER.md) and instruct it to read and execute that file. The worker owns history analysis, domain and ADR reading, code exploration, design vocabulary, and HTML generation. Load those materials only in the worker context during this phase.

Wait for the worker to finish. If it reports a recoverable failure, continue with the same worker. If subagents are unavailable, explain the limitation and ask whether the user wants an inline review; do not silently consume the main context with the scan.

## 2. Return the report

Use the worker's compact handoff to check that the report file exists and is nonempty, without reading the full HTML into the main context. Open it with the available file preview or OS opener (`open` on macOS, `xdg-open` on Linux, `start` on Windows).

Return a clickable Markdown link using the absolute file path and a one-sentence top recommendation. Ask: "Which of these would you like to explore?" If opening fails, still return the file link. If no report was produced, state the blocker instead.

## 3. Grilling loop

After the user picks, load only the chosen candidate's report section and the source/domain context needed for that discussion. Reuse the reviewer for a concise candidate-specific handoff if helpful.

Once the user picks a candidate, call the Skill tool with "grilling" to walk the decision tree with them: constraints, dependencies, the shape of the deepened module, what sits behind the seam, what tests survive.

Side effects happen inline as decisions crystallize; call the Skill tool with "domain-modeling" to keep the domain model current as you go:

- **Naming a deepened module after a concept not in `CONTEXT.md`?** Add the term to `CONTEXT.md`. Create the file lazily if it doesn't exist.
- **Sharpening a fuzzy term during the conversation?** Update `CONTEXT.md` right there.
- **User rejects the candidate with a load-bearing reason?** Offer an ADR, framed as: _"Want me to record this as an ADR so future architecture reviews don't re-suggest it?"_ Only offer when the reason would actually be needed by a future explorer to avoid re-suggesting the same thing; skip ephemeral reasons ("not worth it right now") and self-evident ones.
- **Want to explore alternative interfaces for the deepened module?** Call the Skill tool with "codebase-design" and use its design-it-twice parallel sub-agent pattern.
