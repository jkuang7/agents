# Decision brief and handoff

Temporary storage is sufficient during a disposable comparison. Before transferring ongoing work or ending with unresolved work, use the [continuation record](../../../vendor/matt-pocock-skills/handoff/CONTINUATION.md) to retain the decision brief and evidence at a discoverable location. Reuse the existing plan or task record. Preserve an accepted choice in the authoritative plan or specification when that update is authorized, and link the supporting brief. Return its absolute path.

## Brief

Keep the brief useful to a replacement reviewer or fresh design session. Include:

- Outcome, fixed constraints, non-goals, and repository or environment.
- Credible candidates and the comparison, with sources for decisive claims.
- Recommendation, confidence, material risks, and ownership consequences.
- Assumptions, reopening conditions, and unresolved questions.
- User decision and date, once chosen.

Use `Open` while deliberating, `Blocked` when missing evidence prevents ranking, and `Chosen` only after the user's explicit choice. A blocked brief names the missing evidence or question, affected candidates, and next step needed to resume. A recommendation alone is not a decision.

## Handoff

After a choice, provide a populated prompt for detailed design containing the absolute brief and repository paths, chosen strategy, who chose it and when, assumptions to verify, and unresolved design questions. Use the available `grilling` skill for the interview and `codebase-design` for architecture. Focus on the questions the brief leaves open; avoid repeating the strategy review. Reopen the choice when new evidence undermines it, explaining the evidence to the user before changing direction.

For a blocked review, provide a focused handoff containing the brief path, question or experiment, local conditions, affected candidates, and the evidence needed to distinguish them. Request only enough investigation, design, or prototyping to answer that question. Return the findings to the open review before choosing a strategy.
