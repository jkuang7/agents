---
name: setup-matt-pocock-skills
description: "Configure missing issue tracker, triage label vocabulary, and domain doc conventions for the engineering skills, reusing existing repository or inherited policy."
disable-model-invocation: true
---

# Setup Matt Pocock's skills

Configure missing tracker, triage vocabulary, and domain-document conventions. Reuse existing repository or inherited workspace policy rather than requiring duplicate setup.

## Discover and propose

Read applicable AGENTS.md/CLAUDE.md, existing agent docs, Git remotes, local ticket artifacts, and domain layout. Establish whether triage is installed and whether genuine multi-context structure exists.

Resolve known choices from existing policy. For unresolved choices, recommend:

- Tracker matching the remote host, or local Markdown when no supported host exists. For another tracker, capture the user's workflow. Use the relevant seed below.
- Canonical triage labels, preserving existing mappings when triage is installed. Omit label configuration when it is not.
- A single root CONTEXT.md and docs/adr/ by default. Offer a context map only when repository structure justifies multiple contexts.

Keep external PRs as a triage request surface disabled unless intentionally enabled. Domain files are created lazily when terms or decisions resolve, not during setup.

## Write configuration

Show a concrete draft for unresolved configuration before writing. Reuse authorization and accepted choices. Prefer editing existing CLAUDE.md, otherwise existing AGENTS.md; if neither exists, ask which to create. Preserve surrounding content and update an existing Agent skills section in place.

The Agent skills section needs only a summary and conditional pointer for each configured policy: tracker before issue/spec operations, label mapping before triage state changes, and domain conventions before relevant codebase exploration. Reuse inherited policy pointers where they already suffice.

Use these seeds only for policy that needs a local file:

- [issue-tracker-github.md](issue-tracker-github.md)
- [issue-tracker-gitlab.md](issue-tracker-gitlab.md)
- [issue-tracker-local.md](issue-tracker-local.md)
- [triage-labels.md](triage-labels.md), when triage is installed
- [domain.md](domain.md)

Place local policies in docs/agents/. For another tracker, write its policy from the accepted workflow. Complete when needed conventions are discoverable from applicable agent instructions and consistent with existing policy. Report changed files and explain that policies can be edited directly; setup need not be repeated per session.
