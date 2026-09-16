# Expected behavior

A: Report a successful handoff using the supported ownership evidence and return immediately. Do not wait for readiness, poll to a terminal state, or reproduce implementation, review, verification, publication, retry, or recovery logic.

B: Report a failed handoff and preserve durable state. A PID and lock alone do not prove ownership; do not claim execution started or automatically relaunch.

C: Use `--attach` only as the explicit read-only observation path. Stopping the watcher leaves the controller running and does not transfer execution ownership to the observer.

D: Launch once with the controller's run limit of one, confirm ownership, and return before acceptance. The limit belongs to the controller; it does not turn Codex into a one-child supervisor.

E: Keep #45 as the selected binding authority but preserve the controller's native order. Report that #44 is next and #45 is queued; hand off the Epic controller without reordering, bypassing, manually targeting #45, or promising its immediate execution. The change-request skill must not choose a different delivery shape.

F: Preserve the PR body as the live human-authored specification and the single identity-plus-content-digest observation. Bootstrap identifies the PR, controller status remains separate, and the skill returns after supported evidence confirms ownership. Do not copy the specification into bootstrap or create a second status or recovery loop.

G: Resume the documented controller exactly once from the durable accepted state, corroborate ownership, and return. Do not replay the accepted child, reset or reconstruct runtime state, or add an outer relaunch loop.

Judge ownership, completion boundary, authority, ordering, and observation behavior rather than exact wording.
