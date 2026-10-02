---
name: to-tickets
description: "Break an accepted parent spec into small behavioral subissues, each delivered as its own mergeable PR toward the parent outcome; also re-split an existing Epic's unstarted children or add one child to it. Use when the user asks to write or split tickets or sub-issues, or names to-tickets."
model: opus
---

# To tickets

Turn an accepted parent spec into small behavioral slices that each prove useful progress. Each slice is one subissue delivered as its own PR, merged to `main` before the next slice starts. There is no separate final review: each slice's review runs its own real-world check, and the last slice's review also runs the parent's. The parent remains authoritative; decomposition does not redesign it.

## Choose slices

Read the parent and inspect code only enough to identify behavioral boundaries. Use no more slices than the Size rule and one-concern ownership need; every slice costs a run, a review and a merge. If splitting shows a parent requirement that neither its goal nor its real-world check needs, and it isn't a confirmed guarantee, choose one cut to the parent (as `specs`'s **Design smell** does) before decomposing it; otherwise decompose the parent as written. Each slice is a bounded piece of the parent: every parent behavior has exactly one owning slice. Other slices may depend on or exercise that behavior but must not duplicate its acceptance responsibility. Each slice owns one behavioral concern, includes the incidental implementation it needs, and can be implemented through red, green, and refactor, verified, and reviewed in one fresh session.

Prefer slices whose acceptance can be proven by fast deterministic tests at a stable boundary, such as fixtures rather than live services or paid runs. Short feedback loops keep each red-green-refactor cycle cheap. When the behavior inherently needs a slower or external check, keep it and confine that proof to the narrowest boundary, with the rest of the slice proven through a seam that is easy to test.

Every slice meets `specs`'s **Safe to merge** rule, even if no later slice happens. Order slices so each builds on the merged ones before it, and otherwise follow the parent's requirement order. Prefer a split that needs no feature flags or compatibility layers; if a slice can't be made safe alone, merge it with its neighbor.

**Size:** size each slice for one fresh session and one reviewable PR. Estimate changed lines as additions plus deletions, including tests, but excluding generated files, lockfiles, and snapshots. Aim for about 350; at about 500, look for a natural behavioral split. Line count is a signal, never the reason to split: keep a coherent slice whole when splitting it would only create scaffolding, and split a small slice when it spans several state machines or responsibilities. Coherent behavior, observable acceptance, and a stable verification boundary come before size. State each slice's estimate.

Keep slices vertical. Foundation, abstraction, infrastructure, or cleanup work earns a ticket only when it independently makes required behavior work. Combine concerns only when they cannot be implemented or proven independently.

Consider splitting at a distinct verification boundary, especially when one role changes a candidate and another verifies that exact result. Split when it produces useful behavior or materially reduces reasoning complexity; keep small extensions of the same proof path together.

When a shared schema or interface migration cannot pass in independent behavioral slices, read [WIDE-REFACTORS.md](references/WIDE-REFACTORS.md) for the compatibility sequence. A large file count alone does not trigger it.

Let implementation evidence shape architecture. Stop decomposition where downstream choices depend on facts earlier work has not yet established; state what must be learned before planning further.

## Write each ticket

Use concrete behavior and plain language at the parent contract's abstraction level. Include only established requirements and the parent context needed to choose or prove this slice. Assign duplicated concerns to one owner; other tickets carry only necessary context. Mention orchestration mechanics such as commits, checkpoints, branches, or PR reuse only when the parent requires them.

Use sections that earn their place:

- Parent link.
- Outcome and how it advances the parent.
- Current behavior and necessary context.
- Observable acceptance criteria at the highest appropriate stable system boundary, including relevant failure behavior.
- Real-world check (required): as `specs` defines it, for this slice's outcome. Its review runs it.
- Governing constraints.
- Genuine prerequisites.
- Design direction, when warranted.

Apply `specs`'s **Existing tests** rule to each ticket's acceptance. Carry into each ticket the parent's counterexamples and failure behavior for the rules and saved results that slice owns, and apply `specs`'s **Rules** and **Saved results** guidance to any the slice introduces.

Add design direction only when the existing code suggests one that would make the slice easier to test, maintain, or reason about: a seam to test through, a deep module that hides complexity behind a small interface, an adapter at a boundary the slice must fake in tests, or a pattern the codebase already uses. Include a structure only when it earns its place in this slice. Use `codebase-design` vocabulary. State it as a recommendation with its reason; the implementer may depart from it when implementation evidence supports a better approach. Acceptance stays behavioral: never make a recommended structure an acceptance criterion.

The sequence is ready when every slice has one required behavioral reason to exist, is safe to merge alone and within the size target or explained, is as small as useful independent proof permits, carries no requirement beyond what its behavior needs, and leaves implementers free to discover internal mechanics. A split that merely prepares machinery is insufficient.

## Publish

Before showing it, have a fresh reviewer (in Claude, the `reviewer` agent) in a new context check the sequence against the parent and every rule above. Give it the parent and the `specs` sections this skill points to. Run `specs`'s **Review loop** on the sequence, looking for a simpler split where it says to look for a simpler design.

Show the proposed sequence as a simple story of what becomes possible after each slice, with each slice's size estimate and any stop point, then publish it without waiting; sort any open choice, including the cut above, by `specs`'s **Decisions** and add the linear and shape ones to the parent's decisions comment, creating it if missing. Publish only those tickets as native subissues in agreed order (when re-splitting an existing Epic, change only unstarted children; remove each replaced child from the Epic before closing it with a link to its successors, since a closed but still-linked child can block the Epic), following the resolved tracker policy. After publishing, remove the parent's `not-ready` label if it has one. Sandcastle runs children in their sub-issue order and reads no labels or blocking links, so that order is the run order. When the repository runs Sandcastle, run its on-demand preflight, with the parent body, on each ticket that has no unmerged sibling before it, against current `main`, and fix every conflict it reports. Sandcastle preflights later tickets at their own base, after earlier ones merge. Publication does not start execution.
