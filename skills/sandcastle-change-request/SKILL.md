---
name: sandcastle-change-request
description: Amend the spec of an already-selected Sandcastle child issue, then rerun it. Use when a requirement changes or a run blocks on a spec problem.
---

# Sandcastle change request

Amend one already-selected assignment and hand it back to Sandcastle. Choosing the target or its delivery shape is not this skill's job: if the request doesn't identify exactly one child issue, say so and stop.

The child issue's title and body are its whole binding spec; comments and the parent Epic are context only. Copy any parent constraint the child must obey into the child body. Sandcastle's README describes how it reads and checks it.

## Scope check

A child has started once it has run history, a recorded candidate or a block. Before amending a started child, ask: would the implementer have to build something the original spec didn't ask for?

- **Clarification (no):** amend. Examples: naming an existing test as an exception, fixing wording, resolving a contradiction without changing what the child must do, updating moved paths.
- **New behavior (yes):** don't amend; add it as a follow-up child or issue through `to-tickets` or `specs`, so the started child finishes with its original scope. New behavior is a new requirement, a new acceptance criterion or a new case to handle. One follow-up can hold every gap a later review finds.
- **Third amendment of any kind** to the same started child: the spec likely wasn't ready; re-review the whole child before amending, and ask the user only if its direction is unclear.

Record each amendment to a started child as one comment on it, saying what changed and which kind it is. Those comments are the count.

## Amend and rerun

1. Make sure no controller is running this issue. Sandcastle fails the current attempt closed when the spec changes mid-run, so an edit during a run wastes it.
2. Edit the title or body with the complete change: requirement, acceptance, exclusions and anything it supersedes. Leave an already-correct contract alone.
3. For a spec-conflict block, resolve every conflict in the record's `reason`, not only the one in `question`, then run the README's on-demand preflight on the amended body and continue only when it reports none.
4. Rerun a child issue through `babysit`; in queue mode, keep acting on its results there.

Never merge, advance `main`, close the Epic or create another delivery path here.
