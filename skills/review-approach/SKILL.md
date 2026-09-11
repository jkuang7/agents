---
name: review-approach
description: Compare high-level solution strategies and choose one before detailed design.
---

# Review approach

Choose a strategy before detailed design. Treat the user's proposed implementation as a candidate. This review ends with a recorded user choice or a concrete step to resolve a blocker; design, prototypes, specifications, and implementation are subsequent work.

## Decision rule

Prefer the simplest supported strategy that meets the outcome and named scale requirements with the lowest total risk. Minimize caller-visible concepts and irreversible commitments. Accept internal complexity for module depth and locality. Fewer changed lines do not outweigh overloaded responsibilities or unreliable verification.

## 1. Frame and dispatch

The parent separates outcome, fixed constraints, non-goals, and proposed implementation. Ask only for missing information that could change the credible options. The outcome must be judgeable independently of implementation.

Create an OS temporary directory for `approach-review.md` and notes. Dispatch one persistent reviewer with this skill's path, the decision context, relevant user reasoning, and repository path if available. Prefer file paths over copied content; inherit only necessary conversation.

The reviewer owns investigation, comparison, and the brief. The parent owns user deliberation and forwards replies to that reviewer. Keep raw evidence in notes and return concise findings or later deltas; inspect specific evidence when resolving a disputed claim. Replace a lost reviewer from the brief and notes.

## 2. Ground and explore

The reviewer inspects relevant behavior, callers, ownership, tests, versions, and deployment conditions. Establish the bug's reproduction and expected behavior, or the feature's missing capability. Without a repository, record known conditions and assumptions.

Read `codebase-design` to assess responsibility, depth, locality, and testability. Trace ownership far enough to compare strategies; leave interface shape and final seam placement to detailed design.

Form provisional candidates, then investigate uncertainties that could change the options, ranking, confidence, or mitigation. Read [EVIDENCE.md](references/EVIDENCE.md) for external research. Scale effort to consequence and uncertainty; local evidence may suffice.

Look for materially different alternatives: native behavior, dependencies, custom code, migration, or the status quo. Retain candidates with a plausible strongest case, without a quota. Expand the set before committing to a favorite.

The reviewer may delegate separable investigations with the outcome, local conditions, neutral question, and output-note path. Investigators return evidence and uncertainty; the lead reconciles findings and owns the recommendation.

Proceed when evidence supports comparison, or a specific missing fact prevents it.

## 3. Compare and recommend

Apply the same criteria to each candidate:

- Strongest case and outcome coverage under local conditions.
- Responsibility fit, hidden complexity, and concepts callers must learn.
- Migration, rollback, verification, and realistic failure modes.
- Maintenance, support, operational cost, and required scale.

Describe ownership consequences and distinguish evidence from judgment. Expose tradeoffs when no candidate dominates. Stop when further investigation is unlikely to change the decision.

Read [HANDOFF.md](references/HANDOFF.md) to write the brief. Return a compact comparison, recommendation, confidence, decisive evidence, why alternatives lose, reopening conditions, and brief path.

If ranking needs an experiment, architecture answer, or unavailable evidence, name the gap and smallest step to resolve it. Hand off that question and resume this review with the result.

## 4. Deliberate and record

The parent presents the comparison. Send objections and new facts to the same reviewer to update the brief and return changed reasoning.

After the user's explicit choice, record their words or close paraphrase and date, including disagreement with the recommendation. Provide the handoff for detailed design. Completion requires a recorded choice and handoff; a blocked review retains its concrete next step.
