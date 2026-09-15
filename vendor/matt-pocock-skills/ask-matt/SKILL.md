---
name: ask-matt
description: Ask which skill or flow fits your situation. A router over the skills in this repo.
disable-model-invocation: true
---

# Ask Matt

Route from the user's outcome and current evidence. Reuse sufficient existing decisions and artifacts; the owning skill supplies its workflow. Skip stages with no remaining purpose. Routing grants no new authorization.

## Uncertainty

- Clear small work or an accepted spec: `implement`.
- Consequential competing strategies: `review-approach`.
- Requested stress test or unresolved design interview: `grilling`; `grill-me` is its stateless shortcut, and `grill-with-docs` adds domain recording. A repository alone does not require an interview.
- Factual gap: `research`; handle cheap lookups directly.
- Runnable evidence for a design question: `prototype`.
- Large effort whose decisions cannot yet be specified: `wayfinder`.

## Delivery

Use `to-spec` when settled intent needs a durable contract, then `to-tickets` when independent delivery slices are needed. `implement` produces a verified candidate; `tdd` owns its test-first method. `code-review` independently assesses the candidate and returns findings to the implementation owner. Use `submit-for-review` for requested publication and `accept-pr` for explicitly requested acceptance or merge. Prepared tickets need no automatic retriage.

## Other entry points

- Incoming issues or external PRs: `triage`.
- Broken behavior or performance regression: `diagnosing-bugs`.
- Architectural investigation: `improve-codebase-architecture`.
- In-progress merge or rebase conflict: `resolving-merge-conflicts`.
- Questions for someone else's knowledge: `to-questionnaire`.
- Steps only a human can perform: `wizard`.
- Unclear explanation: `wait-what`.
- Learning across sessions: `teach`.

`domain-modeling` owns repository vocabulary and qualifying ADRs; `codebase-design` owns module design vocabulary; `writing-for-agents` owns agent-document authoring and maintenance.

Read [PHASE-BOUNDARIES.md](PHASE-BOUNDARIES.md) when choosing whether to continue, compact, clear, delegate, or hand off. Use `handoff` for a discoverable continuation record when work transfers. Follow target repository instructions; use `setup-matt-pocock-skills` only for missing initial configuration or explicit setup requests.
