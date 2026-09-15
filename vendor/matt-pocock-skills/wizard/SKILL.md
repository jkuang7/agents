---
name: wizard
description: Create an interactive wizard for setup, credentials, or transitions requiring human-only steps.
---

# Wizard

Generate an interactive bash script for steps only a human can perform. Use [template.sh](template.sh) as the authoritative helper library; copy it and author only the stages below its marker. Preserve its consistent interaction and completion reporting.

## Scope and author

Discover the requested setup or transition from repository configuration, documentation, and CI requirements. Show the ordered stages and captured values for the user's review, resolving only choices not already authorized.

Before authoring, account for every stage's source, destination, secret/public classification, required/optional status, and observable completion condition. For interrupted or irreversible operations, define how to inspect the actual outcome before retrying; saved inputs alone are not completion evidence.

Give each stage a precise, current journey a stranger can follow. Check authoritative UI or command documentation when uncertain. Keep one focused task per stage and dependency order explicit.

Use template helpers for URL opening, hidden secret entry, persistence, CI writes, and confirmation before irreversible actions. Persist each intended value to its specified destination; write only values CI actually needs. Set the stage count correctly. Discover helper signatures in the template instead of recreating its internals.

Open each stage's URL before asking for the value found there.

Classify helper writes as optional only when the requested result permits omission. Record other unmet actions with `record_skip`, skip dependent actions while prerequisites are unmet, and retain `finish` as the final command. Required omissions must yield an incomplete result; optional omissions remain visible.

## Verify and hand off

Check shell syntax and use shellcheck when available. Trace every captured value to its destination and compare CI names with actual configuration. Make the script executable and return its path and run instructions. Leave end-to-end execution to the human because it blocks on their input and browser actions.

Use a scratch or scripts path for one-run wizards and remove them when done. Commit and link a repeatable setup path only when the user wants one.
