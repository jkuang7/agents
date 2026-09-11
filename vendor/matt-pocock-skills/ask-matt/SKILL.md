---
name: ask-matt
description: Ask which skill or flow fits your situation. A router over the skills in this repo.
disable-model-invocation: true
---

# Ask Matt

Choose the next skill from the user's outcome, existing decisions, and current work. Reuse a sufficient task frame rather than restarting discovery. This router explains ownership and handoffs; each skill supplies its own detailed workflow.

## Start where the uncertainty is

- An accepted spec or clear small change can go directly to `implement`.
- Competing high-level strategies go to `review-approach` before detailed design.
- An explicitly requested stress test or unresolved design interview goes to `grilling`. Use `grill-with-docs` when the interview should maintain repository domain terms and qualifying ADRs, or `grill-me` for a stateless interview. The presence of a repository alone does not require an interview.
- A factual gap goes to `research`. A small lookup can be handled directly; delegate substantial independent reading with a bounded question and saved evidence.
- A design question needing a runnable answer goes to `prototype`. Record its conclusion before returning to design or implementation. Production adoption uses normal verification.
- A large effort whose decisions cannot yet be specified goes to `wayfinder`. Its decision map feeds `to-spec` once the requirements are settled. Keep a well-scoped feature out of this larger workflow.

## From settled intent to delivery

1. Use `to-spec` when a durable specification is needed. It synthesizes existing decisions and evidence.
2. Use `to-tickets` when work needs independently verifiable slices and blocking dependencies. Reuse an existing sufficient spec. Publication does not start implementation.
3. Use `implement` for authorized work. It drives TDD where appropriate, verifies a concrete candidate, requests `code-review`, resolves findings, and rechecks changes before committing. Use `tdd` directly for a focused test-first task and `code-review` directly for a review-only request.
4. Use `submit-for-review` when publication is requested. It prepares coherent history, verifies integration, and publishes the review request.
5. Use `accept-pr` only when acceptance, merge, or post-merge cleanup is requested. Preparing or reviewing work does not authorize merging it.

Skip stages whose outputs already exist or whose purpose the task does not need. Use the user's existing authorization and each skill's scope; routing does not grant new external actions.

## Other entry points

- `triage` handles incoming issues and PRs, verifies claims, and prepares accepted work. Tickets already prepared by `to-tickets` need no automatic retriage.
- `diagnosing-bugs` builds a discriminating reproduction, tests hypotheses, fixes the cause, and retains regression evidence. Use `improve-codebase-architecture` when architectural investigation is requested or needed to resolve a demonstrated testing or ownership problem.
- `resolving-merge-conflicts` preserves both intents and unrelated work while resolving an in-progress merge or rebase. It leaves undecidable consequential behavior explicitly unresolved.
- `to-questionnaire` prepares questions for knowledge held by another person. It does not send the document.
- `wizard` creates a script for steps only a human can perform. Required incomplete steps remain incomplete.
- `wait-what` re-explains unclear communication. `teach` supports learning across sessions.

## Shared references

`domain-modeling` owns repository vocabulary and consequential ADRs. `codebase-design` supplies module, interface, seam, and adapter concepts. `writing-for-agents` guides skill and agent-document authoring, including evidence-based maintenance. These references should remain the authoritative homes for their concepts.

## Context and continuation

At a meaningful phase boundary, retain accepted decisions, unresolved work, and evidence before changing context. Use `handoff` for a new worker or session, or when unfinished work needs a discoverable continuation record. Existing task and workflow records remain authoritative. Short disposable work need not acquire a persistent journal.

Read [PHASE-BOUNDARIES.md](PHASE-BOUNDARIES.md) when choosing whether to continue, compact, clear, or delegate. Select based on the next task's information needs and independent work, not a fixed token threshold. A summary can point to primary evidence without keeping all of it in context.

## Workspace conventions

Read the target repository's instructions. Use `setup-matt-pocock-skills` only when the environment needs initial skill or tracker setup, or when the user requests it.
