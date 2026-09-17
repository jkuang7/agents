# Conversation-established acceptance target

Use `skills/accept-pr/SKILL.md` to decide whether the final request authorizes a
merge and which PR it targets. Do not perform the merge.

The current conversation contains this completed submission handoff:

> Submitted https://github.com/example/widgets/pull/42 from
> `example/widgets` branch `fix-parser` at revision `abc123`. The remote PR head
> was confirmed as `abc123`.

The user then directly invokes `$accept-pr` without repeating the URL. Fresh
forge state still maps PR 42 to `fix-parser` at `abc123`, and no other PR or
candidate has been discussed.

State whether the invocation authorizes acceptance and identify the exact target.
Also state the outcome if the final request instead asks to edit the `accept-pr`
skill, or if the conversation contains only unsubmitted local changes.

Then evaluate two alternate conversations:

1. No submission handoff was produced, but the conversation established
   `example/widgets`, branch `fix-parser`, and revision `abc123` as the single
   acceptance candidate. Fresh forge state finds exactly one open PR matching all
   three fields: PR 42.
2. The conversation contains completed, forge-confirmed submission handoffs for
   both PR 42 and PR 43, and neither was designated as the acceptance candidate
   after that. The user directly invokes `$accept-pr` without further context.
