---
name: codebase-design
description: Design deep modules and their interfaces, seams, and testing strategy. Use for module design or shared design vocabulary.
---

# Codebase design

Design deep modules: substantial behavior behind a small interface, located at a clean seam and testable through that interface. Favor leverage for callers, locality for maintainers, and testability.

## Vocabulary

Use these terms consistently for the concepts below; preserve distinct repository domain concepts rather than treating their synonyms as architectural substitutes.

- **Module**: anything with an interface and implementation, from a function to a tier-spanning slice. Use module rather than unit, component, or service for this concept.
- **Interface**: everything callers must know, including signatures, invariants, ordering, errors, configuration, and performance. API signatures or public methods alone are too narrow.
- **Implementation**: code inside the module. Distinguish substance from an adapter's role.
- **Depth**: behavior callers or tests can exercise per unit of interface they must learn. Deep modules offer substantial behavior through small interfaces; shallow interfaces approach their implementation's complexity. Depth is not a ratio of code-line counts.
- **Seam**: a place where behavior can change without editing at that place. Its placement is distinct from the implementation behind it. Use seam for this concept; boundary can mean a DDD bounded context.
- **Adapter**: a concrete implementation satisfying an interface at a seam. The name describes its role, not its size.
- **Leverage**: capability gained by callers per unit of interface learned.
- **Locality**: relevant changes, bugs, knowledge, and verification concentrate in one place.

## Design principles

Reduce methods, simplify parameters, and hide complexity callers need not know. A deep module can contain small interchangeable parts and internal test seams; keep these private rather than exposing them through its external interface.

Apply the deletion test: if removing a module eliminates complexity, it was a pass-through; if complexity reappears across callers, the module earned its place.

Callers and tests cross the module's interface. Tests reaching past it suggest the module shape needs reconsideration. Introduce an interchangeable seam only when something actually varies: one adapter is hypothetical, while two justified adapters establish real variation.

For testable logic, accept dependencies rather than constructing them internally and prefer returned results over incidental mutation. Keep interfaces small so callers and tests need less setup.

Read [DEEPENING.md](DEEPENING.md) when deepening a cluster with dependencies and replacing tests. Read [DESIGN-IT-TWICE.md](DESIGN-IT-TWICE.md) when exploring materially different interfaces.
