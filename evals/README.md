# Skill behavioral cases

Keep a small set of observed failures and representative tasks for the shared skills. Inputs are separated from expected outcomes so an evaluator can receive the task without the diagnosis. Cases verify behavior and evidence, not the wording of instructions.

Run executable helper checks without external services:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s evals -p 'test_*.py'
```

Create isolated cases with:

```sh
python3 evals/make_fixture.py review
python3 evals/make_fixture.py retirement
python3 evals/make_fixture.py continuation
python3 evals/make_fixture.py routing
python3 evals/make_fixture.py vertical_slices
```

Each command creates a new temporary workspace and prints its task path. Give an evaluator only that task and the relevant installed skill. It may read the fixture artifacts. Keep [expected outcomes](expectations.md), prior conclusions, and the proposed correction out of the evaluator prompt. Inspect the resulting artifacts and compare them afterward. Evaluation commands must not publish, call real external services, or modify source skills. A fixture may be deleted after useful evidence has been retained.

Record skill or helper content digests, evaluator conditions, verdict, evidence locations, and process overhead in a result note. The maintained [control record](controls.md) ties each correction to its owner and review condition. Add cases for consequential or recurring failures, reuse related cases, and avoid a new framework until actual evaluation needs one.

The `wizard` cases shadow `gh` with a local shell function and load only the library, so they never open a browser or access credentials. The judgment fixtures have no automatic model runner; executing their setup alone is not a behavioral pass. Use an independent agent when available and disclose prior exposure or unavailable delegation.
