# Issue and Epic lifecycle

Use this unless the repository defines a stricter one.

- **Delivery issue:** an issue one PR fully delivers. Reference it with a closing keyword (`Closes #<n>`) only when the PR delivers all of it; otherwise link it without one. The forge closes it on merge.
- **Parent Epic:** link it without a closing keyword. Close it only when the user asked or a workflow they authorized owns closure, and every required child is closed by a merged PR with no required scope left open. Otherwise leave it open and say what's missing.
- An explicit instruction to keep an issue open always wins.
