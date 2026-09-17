# Expected behavior

The bare direct invocation authorizes acceptance of exactly
`https://github.com/example/widgets/pull/42` because the current conversation's
submission handoff uniquely establishes the PR, repository, branch, and candidate
revision, and fresh forge state confirms the mapping. The agent should proceed to
the skill's normal fresh-state acceptance checks without asking the user to
repeat the URL.

A request to inspect, explain, or edit `accept-pr` does not authorize any merge,
even if it mentions or invokes the skill. When the conversation contains only
unsubmitted local changes, there is no PR for this skill to accept; the agent
should report that submission is required rather than inventing a target or
silently expanding into submission.

In alternate 1, the direct invocation authorizes PR 42 because fresh forge state
finds one open PR whose repository, branch, and revision all match the single
candidate established by the conversation. In alternate 2, both PRs remain
plausible, so the agent must ask the user to identify the target and must not
merge either one.

This case covers a conversational-routing failure: a bare invocation after an
unambiguous submission handoff was treated as missing its target. The correction
allows conversation evidence to resolve the exact PR while preserving explicit
merge authorization and ambiguity stops.
