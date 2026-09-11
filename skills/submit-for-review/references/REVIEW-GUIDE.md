# Write the PR for its human reviewer

The PR body answers what changed after implementation and gives a reader unfamiliar with the codebase a route into the diff. Derive it from the delivered candidate, not from the spec or an earlier illustrative design. Scale to the change: a small fix may need only a short problem/fix explanation, one review check, and verification.

## Order the explanation for the reviewer

Use the reading order illustrated by [StickyMD PR #8](https://github.com/jkuang7/StickyMD/pull/8). The example guides presentation; the reviewed candidate supplies the facts.

1. Summarize the concrete problem and delivered fix, with a before/after comparison when it helps.
2. State the affected actions and scope, with delivered issue links.
3. Explain selected behavior flows, including the failures or cancellations that change their outcomes.
4. Show responsibility changes and retained state owners when needed to understand the implementation.
5. Give the review guide's targeted code checks and supporting evidence, followed by commit review order.
6. Report verification and material limits. Keep detailed preparation history in the preparation note or a collapsed section.

Combine or omit sections that add no distinct information. Explain behavior once, then use review checks to direct attention to the code that enforces it. A small fix can use a few paragraphs and one review check.

## Problem before benefit

Begin with the concrete prior failure or inconsistency and enough context to understand its consequence. Then identify the fix. A benefit such as "consistent safeguards" does not tell the reviewer what previously went wrong.

For example, this opening establishes a problem:

> Required safety steps lived in individual button and menu handlers instead of inside the shared action. As a result, using the relink shortcut could rearrange windows without the confirmation or explicit save that the titlebar performed.

Follow with the delivered responsibility change. Name architectural concepts only when they help explain the observed cause; distinguish already-shared operations from duplicated or omitted preparation. State plausible risk at its actual strength: missing save ordering is not proof of lost data.

## Diagrams carry mechanics; prose adds meaning

Use descriptive subtitles to let a reader scan the behavior before reading details. For comparisons, keep the same action, terms, direction, and abstraction level on both sides.

### Before, safeguards depend on the caller

```text
Note button → confirm → save → rearrange
Menu                         → rearrange
```

### After, callers inherit the safeguards

```text
Note button ──┐
              ├──→ shared action: confirm → save → rearrange
Menu ─────────┘
```

Useful adjacent prose explains why this matters: "Future callers inherit the required preparation, and maintainers can change the rules in one place." It need not narrate the arrows again. The opening still establishes the problem; diagrams do not replace that orientation.

For waits or failures, put branches beside the step they interrupt. Split diagrams when they answer different questions. Use short paragraphs and subtitles instead of dense blocks of implementation choices. Use diagrams for relationships and short lists for independent facts. Add captions only when they explain something absent from the heading and diagram.

## Review guide

Keep the **Review guide** heading. Organize the main file checks by consequential behavior, rather than listing every changed file. Suitable concerns include concurrency, target identity across awaits, exception propagation, partial persistence, rollback, and production routing. Select only those supported by this change.

Each review point should contain:

- A descriptive subtitle naming the behavior and risk.
- The important files, linked to precise diff locations or source lines at the reviewed revision.
- A concrete invariant or decision to inspect in those files.
- The corresponding test links and what their assertions establish, or an explicit evidence gap.

For example, adapted from StickyMD PR #8:

### A failed save stops the action before mutation

Inspect `src/lib/userActionWorkflow.ts`, `src/lib/Editor.svelte`, and the editor-readiness guard in `src/routes/+page.svelte`.

Check that required preparation is awaited, cancellation precedes the relink save, and an unavailable editor cannot silently permit mutation.

Tests in `tests/user-action-workflow.test.ts` inject failed saves for close and relink and assert that later effects do not occur.

In a published guide, those file mentions and tests must be verified links to the relevant code. A list of filenames alone does not supply a review route; "check race conditions" does not identify a check. Phrase checks as inspectable contracts, not a speculative essay about where the author's code might be wrong.

Preserve the required commit review order. Give each commit's SHA and link, purpose, and approach. A long cumulative history can sit in a collapsible subsection below these checks. Presentation does not authorize rewriting commits.

## Delivered choices and evidence limits

When implementation resolves a spec question, describe the actual user-visible behavior under a short scenario subtitle and link the code or recorded decision. Identify remaining gaps and deviations explicitly. Avoid importing hypothetical choices from a design example into the delivered narrative.

State boundaries precisely. A per-surface busy flag does not establish application-wide exclusion; successful event delivery does not establish completed execution; error aggregation does not establish repaired state. These distinctions materially affect review and belong beside the relevant check or in concise limitations.

Report commands, outcomes, candidate revision, and environment. Explain what the tests prove, distinguishing production wiring tests from injected-dependency behavior tests and native/manual checks. Preserve provenance for retained submission results; an author or controller's reported run is not a fresh run or an attached CI result. Acknowledge missing evidence without inventing results or generic warnings.

Keep meaningful scope, preserved ownership, and integration consequences. Put detailed preparation history outside the main narrative. A completion claim must match the delivered scope rather than the epic's aspirations.

## Check the finished guide

Apply the shared unslop process required by `submit-for-review` before publication. Check the edited body against the candidate and retained evidence. Every main review risk must still point to its implementation and supporting evidence or an explicit evidence gap. Keep safety qualifications, unresolved gaps, and the provenance of verification results intact.

When a Markdown preview is available, inspect the rendered draft before publication. Check diagram alignment, branch attachment, horizontal scrolling, and repeated meaning across headings, captions, and prose. Split wide diagrams and attach failure outcomes to the steps that cause them. If preview is unavailable, inspect the Markdown and fenced diagrams directly and report that limit in the handoff.

Skim the headings, diagrams, and captions for the prior problem and delivered change. Then read the prose in order without following links. Check that each important conclusion follows from an explained cause or stated assumption, including why the fix addresses the cause and why its consequences matter. The reader must be able to describe the relevant application context, the flow before the change, the flow with this PR applied, and why the difference matters without prior codebase knowledge. Distinguish delivered behavior from any further planned work. Finally, follow each review check to its implementation and evidence. The guide is ready when the explanation stands on its own and the links let the reader verify it.
