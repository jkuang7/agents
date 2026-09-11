# Sequence changes across shared callers

Use this reference when changing a shared schema or interface would break callers that cannot migrate in independently passing slices. Establish the affected callers and compatibility constraints before choosing the sequence. A large file count alone does not require this exception.

1. Add the new form alongside the old form so existing callers continue to work. Give this compatibility slice observable acceptance criteria.
2. Migrate callers in bounded batches based on affected behavior or ownership. Each batch depends on the compatibility slice and must pass its required checks while remaining callers use the old form.
3. Remove the old form only after all caller migrations complete. Make this removal depend on every migration batch and verify that no required caller or stored-data consumer still needs the old form.

If batches cannot pass independently even with a compatibility step, explain why and propose a shared integration branch in the breakdown review. Declare which checks each batch can satisfy and which must wait for the combined candidate. Add a final integration-and-verification ticket blocked by every batch. Make clear that intermediate work is not independently releasable and preserve the project's integration policy.

The sequence is ready when every caller is accounted for, each ticket has explicit prerequisites and verification, and the final ticket establishes compatibility and removal safety. Keep the dependency graph acyclic.
