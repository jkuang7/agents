# Runtime discovery and control

The trusted runtime's README, CLI help, repository instructions and source are the authority. Discover the current command forms, result contract and state locations there before acting. This reference names the evidence to establish; it supplies no fallback controller logic.

## Trusted operator and routing

Establish the operator checkout's accepted revision, that it is clean and contained in `main`, and the tracker repository the controller will select. That includes forks: `-R` on an issue command does not change controller routing. Keep operator code and candidate code separate.

## Issue state

Locate the issue's durable state and logs from the README. They typically hold budgets, the current child, any recorded candidate or open child PR, the last result record, and the log directory with its `current` pointer. Read them fresh, together with the issue's native sub-issues and their PRs, to establish where the issue stands. Branch names, issue closure or a last log line alone do not establish state. Inconsistent or missing state calls for the documented recovery or a reported stop.

## Controller ownership

Correlate the checkout lock, the process and the current run log with the selected issue. A PID, lock or log alone does not prove live ownership. Start a new controller detached from this agent, as the skill's Commands section shows, not in a new terminal tab. The handoff succeeds only when current runtime evidence shows that the controller passed startup and owns the issue.

To stop a controller, use its documented interface or a graceful interrupt, wait for it and its workers to exit, then re-read state. A controller that has recorded its result and released its lock but has not exited may be interrupted. Recover a stale lock only after proving that its writers exited, using the runtime's procedure where one exists.

## Result record

Read the result contract from the README and ADR 0003: status, class, cause, signature, reason, question, and the child PR when there is one. It is the last line of stdout and is also saved in durable state. Treat anything ambiguous as a decision.

## Child PRs

Each child's PR is the runner's publication for that child. Confirm its number, base (`main`), head commit and CI status from the forge before merging. Ambiguous PR evidence stops the merge rather than creating or guessing a replacement.

## Resume and retry

Discover from CLI help how a rerun resumes and whether a block needs an explicit retry control. Durable decision blocks stay binding until their inputs change or the user authorizes a retry. Unsupported controls call for a reported stop, not manual integration or an outer retry loop.
