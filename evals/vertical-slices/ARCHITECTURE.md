Likely responsibilities include inventory, run state, persistence, child
acceptance, restart recovery, pull request publication, hosting-service
reconciliation, correction state, CI recovery, and final audit. Each
responsibility can be tested independently.

One possible plan puts every responsibility in one implementation ticket because
they occur in one controller workflow. Another blocks audit and readiness work
until a real disposable Epic is authorized, even though local fixtures can
verify that behavior.
