# Out-of-scope knowledge base

Store durable rejected enhancement decisions in `.out-of-scope/<concept>.md`, one file per concept, grouping all prior issues or PRs requesting it. This preserves rationale and prevents repeated reconsideration. Temporary lack of time is a deferral, not a durable rejection.

## Record

Use a recognizable kebab-case filename. Write a short readable design note containing the decision, substantive rationale, and named links to prior requests. Include code or examples only when needed to explain a non-obvious constraint.

```markdown
# User-facing theming

The project leaves theming to downstream consumers.

## Why this is out of scope

The single-palette rendering contract is deliberate. Runtime switching would change that contract and is outside this project's content-authoring purpose.

## Prior requests

- [Add dark mode](issue URL)
```

## Lifecycle

During triage, match records by domain concept rather than wording and surface prior rationale for the maintainer's judgment. Confirmation appends the request and closes it; reconsideration updates or removes the decision record; a distinct request continues normal triage.

Create or update a record only for a rejected enhancement, including enhancement PRs. Already-implemented work is not a rejection; point to its implementation instead. Rejected bugs need no entry here.

Link the record from the closing comment before closing with wontfix. If the maintainer reverses the decision, remove or revise the record; prior closed requests remain history unless reopening is requested.
