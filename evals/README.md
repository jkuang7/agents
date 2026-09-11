# Behavioral regression cases

This directory keeps compact cases for observed, consequential skill failures:

- `spec-scope/` checks that `to-spec` selects the smallest complete outcome
  without weakening correctness or inventing recovery machinery.
- `vertical-slices/` checks that `to-tickets` produces coherent workflow slices
  and keeps proof-only external gates out of implementation tickets.
- `make_fixture.py` generates four disposable repository cases for working-tree
  review, regression-test retirement, stale continuation evidence, and routing.
  Their expected behavior is in `generated-expected.md`.

To inspect a case, give an evaluator its `task.md`, the files named by that task,
and the referenced skill. Keep the case's expected-behavior notes from the
evaluator, then compare its answer with them. These cases are manual prompts,
not a scoring platform.

Generate the repository-backed cases with one of:

```sh
python3 evals/make_fixture.py review
python3 evals/make_fixture.py retirement
python3 evals/make_fixture.py continuation
python3 evals/make_fixture.py routing
```

`test_wizard.py` is a normal unit test for executable shell behavior. Run it
with:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest evals/test_wizard.py
```

Add a behavioral case only after an observed failure could cause meaningful
harm and could realistically recur. Keep the input and expected behavior small.
Delete the case when the behavior disappears or a deterministic test replaces
it. Do not retain run reports, digests, control registries, or generated copies.
