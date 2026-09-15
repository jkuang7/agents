---
name: prototype
description: Build a throwaway prototype to explore a logic/state model or UI design question.
---

# Prototype

Build throwaway code to answer one design question.

## Select the branch

- Logic, state model, or data shape: read [LOGIC.md](LOGIC.md) for a shareable HTML demo with free play and guided scenarios.
- UI appearance: read [UI.md](UI.md) for structurally different variants in app context.

Resolve the question from the request and surrounding code. If genuinely ambiguous, ask when reachable; otherwise choose the better-supported branch and state the assumption in the prototype.

## Common constraints

Clearly mark the code as a prototype and place it near the module or page it explores, following repository routing conventions. Make it trivial to run. Keep relevant state visible after actions or variant changes.

Use in-memory state by default. When persistence itself is being explored, use an explicitly disposable scratch database or file. Keep the demonstration lean: no tests, speculative abstractions, or error handling beyond what makes it runnable.

## Capture

Record the verdict and question settled in the implementation issue or a commit. Preserve the prototype as a rerunnable primary source on a throwaway branch, with a pointer from the issue. Keep exploratory code out of main.

Fold validated decisions into real code within the authorized implementation scope, using normal testing and review. A successful demonstration settles its design question, not production correctness. Retain its conclusion and evidence limits during adoption.
