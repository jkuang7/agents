# Local tracker cleanup

Apply only when the resolved tracker is Local Markdown.

During preparation, identify the exact `.scratch/<feature>/` directories belonging to the delivered scope and include them in the proposal. Preserve ambiguous or unrelated content. Confirm that lasting behavior, decisions, and review context are retained in submitted code, tests, durable documentation, or the review-request body.

Delete only authorized, explicitly identified directories after the forge confirms publication and returns the canonical URL. Recheck their contents before deletion; retain new or unrelated work. Remove `.scratch/` itself only if empty.

If publication fails, retain all tracker artifacts. If cleanup fails, preserve the successful review request and report cleanup as incomplete. Report removed and retained paths in the final handoff.
