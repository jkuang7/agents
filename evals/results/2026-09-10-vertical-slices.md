# Vertical-slice boundary correction

## Failure and control

A ticket breakdown can fail in two directions. It can mirror internal responsibilities such as inventory, persistence, orchestration, recovery, and pull request publication, leaving several tickets that make no part of the parent workflow work. It can also combine resume, publication, reconciliation, correction, CI recovery, and readiness into one mini-Epic that overloads a fresh implementation context.

`to-tickets` now applies two tests to every proposed ticket. Verticality asks what new part of the parent workflow works. Cohesion asks whether the ticket is one coherent behavioral step. It folds internal prerequisites into the first consuming slice and splits overloaded slices at the next meaningful behavioral milestone. Breakdown review rejects both prerequisite-only tickets and tickets with multiple independently substantial behaviors.

A separate failure can occur when live proof needs an external authorization or environment but implementation does not. `to-tickets` now distinguishes implementation prerequisites from verification prerequisites. It keeps locally verifiable implementation executable and puts externally gated proof in a downstream validation ticket that depends on both the completed implementation and the named external condition.

## Retained case

The `vertical_slices` fixture supplies a run workflow and an architecture document that presents each internal responsibility as independently testable while also suggesting one ticket for the entire controller workflow. It also proposes blocking audit and readiness implementation on authorization for a disposable Epic even though local fixtures can verify the behavior. The evaluator must reject the horizontal and overloaded extremes, use coherent workflow milestones, and separate executable implementation from externally gated live proof. The expected outcome is recorded separately in `evals/expectations.md`.

The fixture generator completed successfully and produced an isolated Git repository and task. This run did not use an independent evaluator because delegation was outside the authorized task, so this correction does not claim a behavioral pass or a comparison with prior model behavior.

## Validation

- `python3 evals/make_fixture.py vertical_slices` completed successfully.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s evals -p 'test_*.py'` passed all eight executable tests.
- The bundled `quick_validate.py` reported `Skill is valid!` when run through `uv` with PyYAML.
- `git diff --check` passed.
- Evaluated `to-tickets/SKILL.md` SHA-256: `b500360b65125c2d47a9081c3cf6c49eac1160e5580bfa5fc8bf7337afa206dc`.

## Review condition

Review these controls when ticket sizing, executor routing, dependency representation, or live-environment validation policy changes. Also review them when real breakdowns still produce prerequisite-only tickets, overloaded mini-Epics, or implementation tickets blocked by proof-only external gates. Retire their wording only when another enforced review applies the verticality and cohesion tests and separates implementation prerequisites from verification prerequisites. Run the retained judgment case with an independent evaluator before claiming behavioral effectiveness.
