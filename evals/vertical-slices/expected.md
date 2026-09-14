# Expected behavior

The breakdown uses the fewest tickets that each deliver a coherent workflow
milestone. It folds inventory, initial state, required persistence, and child
acceptance into the first slice that accepts a child. It separates later
milestones when they have distinct failure modes and verification stories, such
as preserving accepted work across restart, processing the current required job
set, publishing one draft pull request, repairing concrete orchestration or CI
failures, and auditing the exact candidate for readiness.

It creates no preparation, persistence, API, recovery, or adapter ticket whose
only result is a prerequisite for later work. It also avoids one ticket that
combines every resume, publication, correction, CI, and readiness behavior.

Ticket wording stays at the parent contract's level of abstraction. Accepted
work survives restart and is not repeated; restart continues from the last
accepted point when state is safe to establish. Publication produces one draft
pull request. Recording child commits, resuming from a commit, or reusing a
previous pull request remain implementation choices unless the parent spec
makes them binding.

Each child includes a parent rule only when the implementer needs it to choose
the correct behavior or prove the slice. It omits details that neither the
parent spec nor current evidence establishes.

Each behavioral concern has one owning ticket. The restart slice owns durable
acceptance, the child-processing slice owns current membership and ordering,
the publication slice owns the draft pull request, and the final-verification
slice owns readiness. Other tickets carry only the context they need and do not
restate adjacent behavior.

It treats one fresh implementation session as a practical size limit. When a
slice crosses distinct verification boundaries, such as a reviewer changing a
candidate that another fresh context must verify, the breakdown considers a
split. It makes that split only when each resulting ticket still proves useful
behavior or the split materially reduces reasoning complexity. It does not
create a machinery-only ticket for every extra verification step.

Local fixtures keep audit and readiness implementation executable. A downstream
live-proof ticket depends on the implementation and explicitly names repository
authorization and provisioning as external prerequisites.
