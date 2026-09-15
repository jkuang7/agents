# Deepening

How to deepen a cluster of shallow modules safely, given its dependencies. Assumes the vocabulary in [SKILL.md](SKILL.md): **module**, **interface**, **seam**, **adapter**.

## Dependency categories

When assessing a candidate for deepening, classify its dependencies. The category determines how the deepened module is tested across its seam.

### 1. In-process

Pure computation, in-memory state, no I/O. Always deepenable: merge the modules and test through the new interface directly. No adapter needed.

### 2. Local-substitutable

Dependencies that have local test stand-ins (PGLite for Postgres, in-memory filesystem). Deepenable if the stand-in exists. The deepened module is tested with the stand-in running in the test suite. The seam is internal; no port at the module's external interface.

### 3. Remote but owned (Ports & Adapters)

Your own services across a network boundary (microservices, internal APIs). Define a **port** (interface) at the seam. The deep module owns the logic; the transport is injected as an **adapter**. Tests use an in-memory adapter. Production uses an HTTP/gRPC/queue adapter.

### 4. True external (Mock)

Third-party services (Stripe, Twilio, etc.) you don't control. The deepened module takes the external dependency as an injected port; tests provide a mock adapter.

Apply seam discipline from [SKILL.md](SKILL.md), including justified variation and private internal seams.

## Testing strategy

- Retire old tests after the replacement tests demonstrate equivalent relevant behavioral and regression coverage, or the old behavior is intentionally removed. Map known failure, concurrency, and preservation cases before deleting their proof. Keep focused tests when the broader interface cannot discriminate those cases. The existence of a new test suite alone does not justify deletion.
- Test observable outcomes at the deepened module's interface so coverage survives internal refactors.

A stand-in or mock proves the behavior it models. When correctness depends on real adapter atomicity, authorization, transport, or compatibility, include focused contract or real-adapter evidence for that claim. Keep the logic tests fast without presenting them as proof of an untested external guarantee.
