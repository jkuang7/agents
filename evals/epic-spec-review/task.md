Use the repository's `skills/specs/SKILL.md` section 4 as the reviewer of this Epic draft. This is an offline evaluation: return review findings only. Do not publish, access external services, or edit skills.

Draft Epic parent:

## Goal

Checks run by the runner clean up after themselves whatever the candidate's scripts do. Real-world check: run a check against a candidate whose test script hangs and confirm the runner returns.

## Requirements

R1. Every check stops all processes it started, whatever the candidate's scripts do.
R2. A check that exceeds its time limit is reported as failed.

## Acceptance

A1. A hanging test is killed and the check fails (R1, R2).
A2. Cancelling a check with a running grandchild process leaves no process behind (R1).

## Out of scope

Changing the time limit.

Codebase facts: checks run in their own process group; a candidate script can start a process in another group, clear its environment, or hold the output streams open. No sandbox exists.
