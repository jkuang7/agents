# Expected behavior

The review returns a finding that the goal and R1 make an absolute claim ("whatever the candidate's scripts do", "every check", "all processes") with neither a list of covered paths nor a stated out-of-scope bound. Under the codebase facts, processes that leave the process group or clear their environment cannot be found without a sandbox, so the claim is unachievable as written. It asks to narrow the claim or bound it, for example by stating which processes are covered and which are out of scope and why.

It also finds that A1 and A2 list two scenarios instead of the rule, and asks for the rule with the failure as one example, the paths it covers (exit paths such as timeout, cancellation, normal pass, failure; kinds of leftover state such as same-group child, detached child, held-open streams) and a test for each.

Not expected: approving the draft, or a finding limited to wording.
