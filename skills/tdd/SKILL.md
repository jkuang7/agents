---
name: tdd
description: Develop behavior test-first in small red, green, and refactor cycles at stable seams.
---

# Test-driven development

Develop one small behavioral capability at a time with this loop:

**red → green → refactor**

A cycle should be small enough that a failure teaches something clear. Write one failing test for required behavior, make it pass with the simplest correct implementation, then refactor when doing so reduces duplication, coupling, cognitive load, or risk. Keep the green implementation when refactoring would add no value.

## Test boundary

Test required behavior at the highest appropriate stable seam. Prefer observable contracts over internal representation, and reuse an existing seam when it gives strong evidence.

Lower-level tests can add confidence without making private implementation part of the contract. Add a new seam for testing only when it reduces total complexity rather than moving complexity into test infrastructure.

Keep slices vertical. Each cycle should prove a usable part of the behavior through its implementation boundary.

## Under uncertainty

When the interface or design is uncertain, use the next test as a tracer bullet for one behavioral assumption. Let the result shape the next cycle. Avoid committing to a large imagined test suite before implementation provides evidence.

## Tests to avoid

- Prompt, prose, or snapshot tests that only lock wording.
- Tests of private methods or internal representation.
- Mocks of internal collaborators when a stable behavioral seam is available.
- Exhaustive edge cases without a governing requirement.
- Speculative test infrastructure.

If an agent policy cannot be tested through behavior without substantial new evaluation infrastructure, use source review. Add a focused evaluation after a real failure justifies it.
