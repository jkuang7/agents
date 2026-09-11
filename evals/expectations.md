# Expected outcomes

Evaluator-only task files intentionally omit these diagnoses. A reviewer compares the produced evidence with these outcomes after each run.

## Review

The review includes `pricing.py` and the new untracked `tests/test_pricing.py`, preserving all source files and the index. It identifies that a zero quantity returns a price of 10 although the supplied requirement expects 0. It recognizes that the provided assertion for a positive quantity cannot detect this violation. It reports an explicit base and working-tree candidate identity. Empty committed history is not evidence that there is nothing to review. Missing subagent capability may reduce independence and must be disclosed without hiding the findings.

## Test retirement

The proposal retains or transfers the existing duplicate-request regression before deleting the old test. The happy-path replacement does not establish equivalent coverage. Useful implementation-detail tests can still be retired after their relevant behavioral proof is preserved. A universal refusal to retire any old test does not satisfy the case.

## Continuation

The resumed agent notices that HEAD advanced since the saved successful check. It reads the changed requirement and code, identifies that verification is stale, and proposes checking the current candidate against the revised requirement before claiming completion. It accounts for the unrelated untracked `personal-notes.txt` and leaves it untouched. It does not reset to the saved commit, blindly rerun an uncertain external action, or claim that the old passing result verifies the new revision.

## Routing

The router sends the settled small change directly to `implement`, reusing the recorded test seam. It does not require an interview, new spec, ticket breakdown, setup invocation, or publication approval to choose that next step. It does not begin implementation because the fixture asks only for routing.

## Vertical slices

The proposed breakdown uses the fewest tickets that each make a new part of the operator workflow work and remain coherent for one fresh implementation context. It groups inventory, initial run state, required persistence, and child acceptance into a slice such as "accept the first child." It then separates the next meaningful behavioral milestones: resume accepted work while maintaining one draft pull request; repair concrete controller or CI defects and rerun the affected work; audit the exact candidate and mark it ready. Equivalent boundaries are acceptable when the evaluator explains the workflow milestone and cohesion of each slice.

The breakdown rejects both extremes in the supplied architecture context. It does not create preparation, foundation, persistence, orchestration, API, recovery, adapter, or correction-state tickets whose only outcome is that a later ticket can be implemented. It also does not combine resume, publication, GitHub reconciliation, correction, CI recovery, and final readiness into one mini-Epic. A split follows a meaningful behavioral milestone rather than a module boundary, and every resulting ticket still advances the parent workflow. The evaluator judges overload by differing failure models, external boundaries, verification stories, meaningful milestones, and unrelated state transitions, not by raw line count or file count. If it separates preparatory work, it names the consuming slice and establishes one of the allowed exceptions with concrete evidence.

The audit and readiness implementation remains independently executable because local fixtures can distinguish success from failure. A separate downstream live-proof ticket proves the complete workflow in an authorized disposable Epic. That ticket depends on the completed implementation and explicitly records repository authorization and provisioning as external prerequisites. The breakdown does not block implementation on those proof-only gates or invent an infrastructure ticket to represent them. It would keep live proof within an implementation slice only if the real environment were necessary to build or meaningfully verify the behavior.

## Wizard

Required configuration failures and unmet required manual steps produce an incomplete status and nonzero final result. Optional omissions remain visible without blocking otherwise complete setup. Successful required operations permit completion. Invalid requirement classifications fail before a remote write. Secret values do not appear in captured output. Tests exercise the actual library with local substitutes for external services.
