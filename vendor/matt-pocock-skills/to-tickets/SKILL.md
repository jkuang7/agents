---
name: to-tickets
description: "Break an accepted parent spec into small, independently provable behavioral subissues that accumulate toward the parent outcome."
disable-model-invocation: true
---
Turn an accepted parent spec into a sequence of **small behavioral slices that each prove useful progress toward the parent outcome**.

Each ticket should be simple enough for a fresh implementer to understand, implement with red → green → refactor, verify, and review independently.

Accepted slices accumulate into the same parent delivery candidate and final PR.

The parent spec remains the source of truth. Do not redesign or restate it.

## Process

1. Read the accepted parent spec.

   Inspect code only as needed to identify clean behavioral boundaries. Do not perform implementation-level discovery before proposing slices.
2. Choose the smallest useful behavioral slices.

   For each slice, ask:

   > What is the smallest meaningful behavior we can make true and prove here?
   >

   Prefer several simple, independently provable slices over one deeper, more complex ticket.
3. Keep slices vertical.

   Do not split by module, layer, abstraction, or implementation step.

   Fold incidental implementation work into the behavioral slice that needs it.

   Keep each slice focused on one behavioral concern. If two proposed tickets carry the same rule, assign it to the ticket that owns that behavior. Leave the other ticket with only the context needed to implement or prove its slice.

   A ticket may reference a parent invariant when that invariant determines the correct behavior or proof. Do not restate adjacent behavior owned by another slice. Combine concerns only when they cannot be implemented or proven independently.
4. Do not assume the final architecture.

   Let each slice and its evidence shape what comes next.

   If later slices depend on learning that does not yet exist, stop decomposition there rather than inventing downstream tickets.
5. Keep each ticket easy to understand.

   A technically capable human should be able to understand the ticket on first read.

   Use concrete behavior and plain language. Include enough parent context to explain the goal without forcing the reader to reconstruct the whole Epic.

   Include a parent rule in a child ticket only if the implementer needs it to choose the correct behavior or prove the slice.

   Use only behavior, constraints, dependencies, and context established by the parent spec or current evidence. Leave absent details absent.

   Keep ticket titles, outcomes, context, and acceptance criteria at the parent contract's level of abstraction. Describe what must survive, continue, or be delivered. Mention commits, checkpoints, branches, or reuse of an existing pull request only when the parent makes that detail part of the contract.

   Avoid orchestration jargon, compressed state-machine language, and speculative implementation detail.
6. Make each slice easy to prove.

   Acceptance criteria should describe observable behavior at the highest appropriate stable system boundary and be concrete enough to drive red → green → refactor.

   Prefer tests of observable contracts over tests coupled to internal representation.
7. Prefer low complexity per slice.

   Split a ticket when doing so makes implementation or proof materially simpler while still producing meaningful behavioral progress.

   Use one fresh implementation session as a practical size limit. A fresh implementer should be able to understand the behavior, drive it through red → green → refactor, verify it, and review the resulting diff without holding several independent proof boundaries in context.

   Treat each distinct verification boundary as a reason to consider a split, especially when one role changes a candidate and another role must verify that exact result. Split only when the smaller ticket still delivers useful behavior or materially reduces reasoning complexity. If the additional boundary is a small extension of the existing path, keep it in the same slice.

   Do not create foundation, abstraction, infrastructure, or cleanup tickets unless they independently make required behavior work.
8. Before publishing anything, show the proposed ticket sequence to the user as a simple story.

   Each item should say, in plain language, what the system will be able to do after that slice:

   1. **Ticket title** — a short explanation of the behavior this adds.
   2. **Ticket title** — what this adds on top of the previous slice.
   3. **Ticket title** — what becomes possible next.

   The sequence should make the parent workflow easy to understand from top to bottom.

   Include only slices justified by current evidence.

   If later slices depend on what earlier work teaches us, stop there and state:

   **Stop point:** what must be learned or proven before planning further work.
9. Wait for the user to approve the proposed sequence.
10. After approval, publish only the approved tickets as native subissues of the parent Epic, in the agreed order.

   Add blocking relationships only where one ticket genuinely cannot proceed before another.

   Apply the implementation-ready label where appropriate.

## Ticket

Use only sections that earn their place.

### Parent

Link the parent Epic.

### Outcome

Describe the single new behavior this slice makes possible and how it moves the parent forward.

### Context

Explain why this slice exists and what currently happens.

Give a fresh implementer only the parent context needed to understand the goal.

### Acceptance Criteria

Describe observable evidence that proves the slice works, including relevant failure behavior.

Criteria should be concrete enough to drive red → green → refactor without prescribing the internal implementation.

### Constraints

Include only parent constraints or existing behavior that materially constrain this slice.

### Blocked By

Include only genuine prerequisites, if any.

Before proposing or publishing a slice, ask:

> Is this the smallest useful behavior that can be implemented and proven independently?

If not, split or simplify it.

Then ask:

> Can one fresh implementer complete red → green → refactor, verification, and diff review without crossing several distinct verification boundaries?

If not, split at a meaningful proof boundary. Keep the behavior together when a split would only create preparatory machinery.

Then ask:

> Does each ticket have one clear behavioral reason to exist?

If a ticket contains concerns that can be proven separately, split it. If the same concern appears in multiple tickets, assign it to one and remove the duplication.

Then ask:

> Does this make real progress toward the parent contract, or is it merely preparing machinery?

Prefer real behavior.

Finally ask:

> Am I deciding something the implementer should be free to discover through red → green → refactor?

Remove it.
