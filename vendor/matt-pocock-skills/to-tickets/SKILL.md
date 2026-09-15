---
name: to-tickets
description: "Break an accepted parent spec into small, independently provable behavioral subissues that accumulate toward the parent outcome."
disable-model-invocation: true
---

# To tickets

Turn an accepted parent spec into small behavioral slices that each prove useful progress. Accepted slices accumulate into the same parent delivery candidate and final PR. The parent remains authoritative; decomposition does not redesign it.

## Choose slices

Read the parent and inspect code only enough to identify behavioral boundaries. Prefer several simple slices over one complex ticket. Each slice owns one behavioral concern, includes the incidental implementation it needs, and can be implemented through red, green, and refactor, verified, and reviewed in one fresh session.

Keep slices vertical. Foundation, abstraction, infrastructure, or cleanup work earns a ticket only when it independently makes required behavior work. Combine concerns only when they cannot be implemented or proven independently.

Consider splitting at a distinct verification boundary, especially when one role changes a candidate and another verifies that exact result. Split when it produces useful behavior or materially reduces reasoning complexity; keep small extensions of the same proof path together.

When a shared schema or interface migration cannot pass in independent behavioral slices, read [WIDE-REFACTORS.md](references/WIDE-REFACTORS.md) for the compatibility and integration exception. A large file count alone does not trigger it.

Let implementation evidence shape architecture. Stop decomposition where downstream choices depend on facts earlier work has not yet established; state what must be learned before planning further.

## Write each ticket

Use concrete behavior and plain language at the parent contract's abstraction level. Include only established requirements and the parent context needed to choose or prove this slice. Assign duplicated concerns to one owner; other tickets carry only necessary context. Mention orchestration mechanics such as commits, checkpoints, branches, or PR reuse only when the parent requires them.

Use sections that earn their place:

- Parent link.
- Outcome and how it advances the parent.
- Current behavior and necessary context.
- Observable acceptance criteria at the highest appropriate stable system boundary, including relevant failure behavior.
- Governing constraints.
- Genuine prerequisites.

The sequence is ready when every slice has one required behavioral reason to exist, is as small as useful independent proof permits, and leaves implementers free to discover internal mechanics. A split that merely prepares machinery is insufficient.

## Publish

Show the proposed sequence as a simple story of what becomes possible after each slice, with any stop point. Wait for approval unless the sequence is already approved. Then publish only those tickets as native subissues in agreed order, following the resolved tracker policy. Add blocking relationships only for genuine prerequisites and apply the implementation-ready label where appropriate. Publication does not start execution.
