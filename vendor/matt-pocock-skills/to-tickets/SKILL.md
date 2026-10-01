---
name: to-tickets
description: "Break an accepted parent spec into small behavioral subissues, each delivered as its own mergeable PR toward the parent outcome; also re-split an existing Epic's unstarted children or add one child to it. Use when the user asks to write or split tickets or sub-issues, or names to-tickets."
---

# To tickets

Turn an accepted parent spec into small behavioral slices that each prove useful progress. Each slice is one subissue delivered as its own PR, merged to `main` before the next slice starts. There is no separate final review: each slice's review runs its own real-world check, and the last slice's review also runs the parent's. The parent remains authoritative; decomposition does not redesign it.

## Choose slices

Read the parent and inspect code only enough to identify behavioral boundaries. Prefer several simple slices over one complex ticket. Each slice is a bounded piece of the parent: every parent behavior has exactly one owning slice. Other slices may depend on or exercise that behavior but must not duplicate its acceptance responsibility. Each slice owns one behavioral concern, includes the incidental implementation it needs, and can be implemented through red, green, and refactor, verified, and reviewed in one fresh session.

Prefer slices whose acceptance can be proven by fast deterministic tests at a stable boundary, such as fixtures rather than live services or paid runs. Short feedback loops keep each red-green-refactor cycle cheap. When the behavior inherently needs a slower or external check, keep it and confine that proof to the narrowest boundary, with the rest of the slice proven through a seam that is easy to test.

Every slice must be safe to merge on its own, even if no later slice happens: existing behavior preserved, touched behavior complete, no half-finished user flow. When a user flow cannot be finished within one slice, keep its incomplete part unreachable until the slice that completes it. Order slices so each builds on the merged ones before it, and otherwise follow the parent's requirement order. Prefer a split that needs no feature flags or compatibility layers; if a slice can't be made safe alone, merge it with its neighbor.

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
- Real-world check (required): one concrete command or observation showing this slice's outcome, which its review runs. Use real data where possible, or a stated scripted substitute; passing tests alone is not one. When the result depends on a model's judgment, state what counts as a pass.
- Governing constraints.
- Genuine prerequisites.
- Design direction, when warranted.

For each acceptance criterion that changes behavior, search the existing tests for assertions of the behavior it replaces, and for tests whose setup relies on it, such as a removed flag or a skipped step. Name every hit as an exception in the acceptance text ("Existing tests pass with assertions unchanged, except: …"); when several variants of a test share the assertion, name the whole family by file and pattern. An implementer told to keep tests unchanged stops when one contradicts the ticket.

Carry into each ticket the parent's counterexamples and failure behavior for the rules and saved results that slice owns. When a slice introduces its own rule or saved result, apply `to-spec`'s **Rules** and **Saved results** guidance to it: realistic examples of each outcome, at least one case the rule must not cover, every input that invalidates a saved result and every path that reuses it, and what happens on crash, rerun, and mid-run change.

Add design direction only when the existing code suggests one that would make the slice easier to test, maintain, or reason about: a seam to test through, a deep module that hides complexity behind a small interface, an adapter at a boundary the slice must fake in tests, or a pattern the codebase already uses. Include a structure only when it earns its place in this slice. Use `codebase-design` vocabulary. State it as a recommendation with its reason; the implementer may depart from it when implementation evidence supports a better approach. Acceptance stays behavioral: never make a recommended structure an acceptance criterion.

The sequence is ready when every slice has one required behavioral reason to exist, is safe to merge alone and within the size target or explained, is as small as useful independent proof permits, carries no requirement beyond what its behavior needs, and leaves implementers free to discover internal mechanics. A split that merely prepares machinery is insufficient.

## Publish

Before showing it, have a fresh reviewer in a new context check the sequence against the parent: each behavior has one owner, every slice is safe to merge alone, size estimates are plausible, acceptance proves each slice, each slice names a real-world check, every existing test that asserts or relies on replaced behavior is named as an exception, with variant families named by file and pattern, no slice's rule gives a wrong answer for a realistic case, and every saved result names what invalidates it and every path that reuses it. Follow `to-spec`'s review loop: every important finding per pass, revise for all of them, review again only when a pass changed a requirement or the design, look for a simpler split when fixes keep adding requirements or machinery, and ask the human if a third pass still finds requirement- or design-level problems.

Show the proposed sequence as a simple story of what becomes possible after each slice, with each slice's size estimate and any stop point. Wait for approval unless the sequence is already approved. Then publish only those tickets as native subissues in agreed order (when re-splitting an existing Epic, change only unstarted children; remove each replaced child from the Epic before closing it with a link to its successors, since a closed but still-linked child can block the Epic), following the resolved tracker policy. Sandcastle runs children in their sub-issue order and reads no labels or blocking links, so that order is the run order. Publication does not start execution.
