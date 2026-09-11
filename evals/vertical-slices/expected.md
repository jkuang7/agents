# Expected behavior

The breakdown uses the fewest tickets that each deliver a coherent workflow
milestone. It folds inventory, initial state, required persistence, and child
acceptance into the first slice that accepts a child. It separates later
milestones when they have distinct failure modes and verification stories, such
as resuming accepted work with one draft pull request, repairing concrete
controller or CI failures, and auditing the exact candidate for readiness.

It creates no preparation, persistence, API, recovery, or adapter ticket whose
only result is a prerequisite for later work. It also avoids one ticket that
combines every resume, publication, correction, CI, and readiness behavior.

Local fixtures keep audit and readiness implementation executable. A downstream
live-proof ticket depends on the implementation and explicitly names repository
authorization and provisioning as external prerequisites.
