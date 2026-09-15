---
name: domain-modeling
description: Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md, or recording or editing an ADR.
---

# Domain modeling

Actively sharpen the project's domain language and record resolved terms and qualifying decisions as they crystallize. Reading an existing glossary alone does not require this skill.

## Language

Read the relevant `CONTEXT.md`, following a root `CONTEXT-MAP.md` when present, and relevant ADRs. Challenge conflicts with established terms, propose precise names for vague or overloaded concepts, and stress-test relationships through concrete scenarios. Check claimed behavior against code; surface contradictions for resolution.

Update resolved terms immediately using [CONTEXT-FORMAT.md](CONTEXT-FORMAT.md). CONTEXT.md is a domain glossary, not a spec or implementation notebook. Create it lazily at the first resolved term; use a root glossary by default, or the context named by an existing map and repository policy.

## Decisions

Offer an ADR only when the decision is hard to reverse, surprising without context, and the result of a real tradeoff. Record qualifying decisions using [ADR-FORMAT.md](ADR-FORMAT.md). Create `docs/adr/` lazily, respecting repository or context-specific layout.
