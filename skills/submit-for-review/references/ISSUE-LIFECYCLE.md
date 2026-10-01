# Issue and Epic lifecycle

Use this contract when preparing or accepting a PR unless the target repository
defines a stricter lifecycle.

## Delivery issues

A delivery issue is a child issue or other independently closable unit whose
complete scope is delivered by one PR.

Use a forge close-on-merge keyword for a delivery issue only when the PR delivers
all of that issue and closure is intended. Otherwise use a non-closing link. The
forge closes a correctly referenced delivery issue when the PR merges; submission
and acceptance do not close it manually unless a separately authorized workflow
explicitly owns that mutation.

## Parent Epics

Link a parent Epic without a close-on-merge keyword. Merging a PR does not by
itself authorize or establish closure of the Epic.

Close a parent Epic only when both conditions hold:

1. Separate lifecycle authorization exists: the user explicitly requested the
   closure, or an already-authorized governing workflow explicitly owns and
   requires it. Repository policy can constrain closure but does not itself grant
   mutation authority.
2. Fresh evidence establishes that the Epic is complete: every required child
   is closed by its merged PR or has equivalent recorded delivery evidence; no
   required scope remains open; and, for a Sandcastle Epic, the runner reported
   `complete` after the last child PR merged.

Branch names, issue proximity, a parent link alone, or the merge itself are not
delivery evidence. If authorization or completion evidence is missing or
ambiguous, leave the Epic open and report the missing condition.

## Precedence

Honor an explicit user instruction to keep an issue open. A stricter repository
policy may require more evidence or prohibit automatic closure. A looser policy
does not broaden the user's authorization to mutate issue state.
