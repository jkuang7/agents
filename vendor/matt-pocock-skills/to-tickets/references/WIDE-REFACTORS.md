# Sequence changes across shared callers

Use this reference when changing a shared schema or interface would break callers that cannot migrate in independently passing slices. Establish the affected callers and compatibility constraints before choosing the sequence. A large file count alone does not require this exception.

1. Add the new form alongside the old form so existing callers continue to work. Give this compatibility slice observable acceptance criteria.
2. Migrate callers in bounded batches based on affected behavior or ownership. Each batch depends on the compatibility slice and must pass its required checks while remaining callers use the old form.
3. Remove the old form only after all caller migrations complete. Make this removal depend on every migration batch and verify that no required caller or stored-data consumer still needs the old form.

Each slice is merged on its own, so every batch must pass all checks and be safe to merge. If batches cannot pass independently even with a compatibility step, combine them into one slice and state its size estimate in the breakdown review.

The sequence is ready when every caller is accounted for, each ticket has explicit prerequisites and verification, and the removal ticket establishes that no caller still needs the old form. Keep the dependency graph acyclic.
