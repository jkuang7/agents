# Agent briefs

Record accepted issue work or remaining work on an existing PR. Reconcile the brief with accepted requirements and human decisions; identify contradictions rather than assigning against competing contracts.

## Requirement transfer

Before executor handoff, establish which artifacts it receives. If comments are omitted, transfer accepted requirements into the supplied body or versioned requirement record under existing authorization, preserving unrelated content and linking the brief. Read back the supplied requirements to confirm agreement. If transfer is unauthorized, retain the concrete correction and report the handoff incomplete. A readiness label is not evidence of a complete execution contract.

## Durable contract

Describe behavior, constraints, and observable acceptance criteria rather than prescribing edits. Searchable concepts, interfaces, types, and configuration shapes help navigation. Paths or lines may identify evidence at a recorded revision; treat them as hints, not lasting requirements. Preserve opinionated design constraints when they are part of accepted intent.

State scope boundaries that prevent adjacent work. Include current versus desired behavior and relevant failure outcomes. For a PR, current behavior describes the attached diff and desired behavior states what remains to finish or correct.

## Format

Use a brief with category, summary, current behavior, desired behavior, useful key interfaces, independently verifiable acceptance criteria, and exclusions. Each section should earn its place; do not manufacture edge cases or prescribe speculative architecture.

Example for an enhancement PR:

```markdown
## Agent brief

**Category:** enhancement
**Summary:** Finish the contributor's JSON output flag.

**Current behavior:** The attached diff serializes successful list output, but errors remain plain text and lack coverage.

**Desired behavior:** With the flag, success and errors are JSON on stdout. Exit codes and unflagged output remain unchanged.

**Key interface:** Reuse the existing serializer; the error contract is an object containing an error string.

**Acceptance criteria:**
- Success and failure output parse as JSON.
- Focused tests discriminate both outcomes and preserve exit codes.
- Unflagged output remains unchanged.

**Out of scope:** Other commands and changes to the successful JSON shape.
```
