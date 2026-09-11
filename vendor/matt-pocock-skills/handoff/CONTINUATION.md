# Continuation records

Use for sustained work, an interruption, a blocked exit, or transfer to another worker. The active workflow owns the record. Reuse its existing plan, task record, or execution state instead of creating another authority.

When no record exists, use the repository's local artifact convention, falling back to `.scratch/<task>/continuation.md`. Keep operational notes out of product commits. Without a repository, use `~/.agents/handoffs/<task>/continuation.md` unless the user named a location. Use a task-specific directory, return its absolute path, and put a pointer in the existing task or plan when that artifact is available and updating it is authorized. Preserve accepted decisions in their authoritative specification rather than only in this record.

Keep the record compact, with links to detailed evidence:

- Task and requirement references, scope, accepted decisions, and remaining assumptions.
- Repository, branch, current HEAD, review base, and any candidate snapshot identity.
- Owned unfinished changes and unrelated work to preserve, including relevant new files.
- Completed and pending outcomes, commands and results, the candidate they checked, and review findings still open.
- Blocker or uncertainty, attempted actions that should not be repeated unchanged, and one concrete next action.

Refresh it at meaningful phase boundaries and before yielding incomplete work. Preserve the last usable record when an update fails, and report that failure. Do not create checkpoints for every small edit or store secrets in evidence.

On resume, read the referenced requirements and compare the recorded branch, HEAD, dirty work, and verification inputs with live state. Reconcile differences before editing. Reuse checks only for unchanged relevant inputs. For an operation with an uncertain external outcome, inspect its actual state before retrying. A recorded intention or a completion checkbox is not proof that the operation succeeded.

Mark completed work as complete with its final evidence and remaining caveats. A clean checkout is not required for a safe handoff when owned and unrelated unfinished work is explicitly accounted for. Preserve that work rather than cleaning it away to satisfy a summary.
