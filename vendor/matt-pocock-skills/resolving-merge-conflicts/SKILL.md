---
name: resolving-merge-conflicts
description: "Use when you need to resolve an in-progress git merge/rebase conflict."
---

1. **See the current state** of the merge/rebase. Record HEAD, staged, unstaged, and untracked work, the conflicting files, and which changes belong to the operation. Preserve unrelated changes and the user's index.

2. **Find the primary sources** for each conflict. Understand deeply why each change was made, and what the original intent was. Read the commit messages, check the PRs, check original issues/tickets.

3. **Resolve each hunk.** Preserve both intents where possible. Resolve routine choices from the accepted requirements and merge goal, recording material tradeoffs. When incompatible observable behavior cannot be settled from existing intent, preserve the in-progress operation and identify the precise decision needed. Continue independent resolutions; do not invent behavior or abort the operation without authorization.

4. Discover the project's **automated checks** and run them, typically typecheck, then tests, then format. Fix anything the merge broke.

5. **Finish the merge/rebase.** Stage resolved in-scope files explicitly and inspect the staged diff before committing. Include pre-existing staged work only when its ownership and authorization belong to this operation. If mixed changes cannot be separated reliably, preserve them and resolve ownership first. Continue an authorized rebase through its remaining commits. Reverify the final combined candidate after any later resolution or hook changes its contents; report incomplete while a conflict or required check remains unresolved.
