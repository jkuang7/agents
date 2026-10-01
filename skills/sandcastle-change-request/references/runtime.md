# Runtime discovery and handoff

Consult the current trusted operator source, README, command help, and repository instructions before acting. Discover paths, revisions, and supported interfaces each time. This reference locates the existing runtime; the controller owns its state machine.

## Selected target capability discovery

Validate only the assignment target already selected by the request or approved context. Do not use runtime capability to choose between Epic and standalone delivery.

For a selected Epic child, confirm from the trusted operator source, README, and command help:

- the concrete Epic entry point and target repository;
- the operator revision;
- that the selected child is the complete binding contract and parent Epic material is separate non-binding context unless copied or restated in the child;
- the runtime's actual canonical authority observation and fail-closed change check;
- that the observation respects the binding-source boundary without assuming a field layout or authority projection the trusted runtime does not implement; and
- the target, delivery, resume, retry, and observation prerequisites and any blocking reasons.

For a selected focused standalone PR, confirm:

- the concrete standalone entry point and bootstrap/input shape;
- the operator revision;
- that the selected PR is the live specification authority;
- the runtime's actual canonical authority observation and change check: for the current design, the PR identity plus one canonical content digest;
- any separate revision only when the source exposes an independent, stable, body-specific revision signal;
- that implementation, fresh review, exact correction verification, publication, and readiness use that authority;
- the target/base/branch prerequisites and any blocking reasons;
- the durable standalone state location and supported launch, resume, retry, and observation interfaces.

For standalone, use the runtime's capability command when available and record its actual result. Do not infer standalone support merely from source files or an Epic command.

If support is absent or cannot be established for the selected target, follow the skill's unsupported-execution preparation and stop. Do not switch modes, invent commands, create an artificial Epic, or substitute an ad hoc loop and call it Sandcastle. Adding runtime capability requires separate authorization.

## Existing standalone discovery and handoff

These are discovery hints; confirm them against the current operator:

- Confirm that the supported standalone bootstrap/input identifies the already-selected focused PR.
- Read the PR body as the live assignment authority; controller-owned status/evidence is not assignment scope.
- For standalone work, keep the PR human-reviewable: use a clear title and concise body that states the requested behavior, acceptance criteria, exclusions, and relevant constraints; controller-owned status/evidence must remain separate from the human specification.
- Inspect `.sandcastle/standalone/` only for durable execution/recovery state, not as a competing or copied specification source.
- Through the runtime's supported interface, confirm that its canonical observation still matches the live PR before resume. Discover the observation the runtime actually implements instead of requiring a cached field layout. For the current design, this is the PR identity and one content digest; do not persist or require a second representation of the PR specification.
- Confirm the saved branch/worktree, accepted candidate, publication state, operator revision, and bootstrap ownership through the runtime's supported interfaces.
- Resume through the documented standalone entry point; do not reconstruct the workflow manually.

## Existing Epic discovery and handoff

These are discovery hints; confirm them against the current operator:

- The README names where the issue's durable state and run logs live (operator `.sandcastle/logs/epic-<number>/current` points to the current run). Read them with the issue's native sub-issues and each child's PR to establish which children are accepted (in the per-child PR model, a child is accepted when its PR has merged), which child is next, and any recorded block or candidate.
- GitHub native sub-issues determine the required set and order, including closed children. A closed child that is still linked but was never accepted blocks the Epic. Read the order back after any assignment change.
- Discover the trusted runtime's actual canonical observation of the selected child. Verify that it treats the child's contract-bearing title and body as the complete binding contract, excludes comments and workflow metadata from binding authority, and keeps parent Epic material as separate non-binding context. Do not infer inherited constraints or prescribe an unimplemented authority projection.
- Determine whether the selected child is the next executable assignment when immediate execution matters. The controller rereads the child order at each child boundary. Preserve native ordering and report a later child as queued. Do not reorder, bypass or manually target it unless the trusted runtime documents that capability.
- CLI help lists the entry point, the read-only watchers (`--attach`, `--attach-worker`; stopping one leaves the controller running), and the current resume or retry controls.

Check the operator's selected repository, including `gh repo view` where used, against the durable target before launch. `origin` may point upstream while delivery targets a fork; `-R` on issue edits does not change controller routing. Resolve mismatches through authorized configuration or stop.

## Controller ownership handoff and observation

Discover the supported controller launch and ownership signals from the trusted operator's README, command help, source, and capability/state interface. Launch the documented controller command in an execution surface that can remain alive after this agent returns.

A handoff succeeds only after the controller passes preflight and the runtime's supported output or state confirms that it acquired and accepted ownership of the selected delivery. A spawned process, PID, or lock file alone is not enough. If the controller exits during launch, rejects the assignment, or ownership cannot be corroborated, preserve the authoritative assignment and report that handoff failed.

Once ownership is confirmed, return control to the user. Sandcastle remains responsible for its workers and lifecycle; do not poll it to readiness or reconstruct its state in the originating conversation.

If the user explicitly requests observation, use only the interface the current runtime documents. Epic attach commands are controller-independent watchers, and stopping a watcher must leave the controller running. The current standalone interface may expose state through capability discovery without providing an attach command; do not invent one. Use a documented snapshot or watcher only when it satisfies the request, and report when no supported observation mode exists.

## Controller stop and snapshot

Resolve the selected delivery's controller, operator revision, worktree/branch, and PR from durable evidence. Follow repository worktree placement rules and retain existing registered locations. For Epic work, pin the accepted children, required-child order, `main` HEAD, any open child PR or recorded candidate, and relevant working-tree status from durable state, logs, and PR metadata. For standalone work, inspect only state used by its supported mechanism. Dirty candidate work remains unfinished.

Only stop a controller that exists for the selected delivery. Verify its command, working directory, run identity, and liveness before signaling; the PID/start time in `.sandcastle/logs/checkout.lock` is insufficient alone. Prefer its owning terminal or documented graceful interrupt. Wait for workers and host commands to exit and ownership to release, then re-read state, because acceptance or publication may have completed during interruption.

Preserve durable state and unfinished work. Uncertain locks or workers that will not exit require investigation, not lock deletion or a competing controller. For proven stale ownership, use documented recovery only after confirming original writers exited; without that interface, leave the run stopped.

## Operator activation and recovery

Use the runtime's documented activation and recovery interfaces only for a separately authorized, approved runtime/policy change. Stop any live selected controller safely first. Activate only accepted, independently verified runtime revisions; never run an unverified candidate as the controller.

Preserve any local operator changes and verify the resulting runtime before activation. Keep operator-only changes separate from delivery work. Resume through the normal trusted entry point after safe activation.

Where `.sandcastle/review-policy.md` or `verify-policy.md` is supported, resolve worker policies from their trusted pinned sources. Candidate copies cannot authorize themselves or change the assignment's trust boundaries.

## Correction handoff

For an explicitly authorized review correction, record the assignment and proof in its durable source (a child issue, or a correction sub-issue) and let the runtime deliver it through its normal flow. Preserve accepted history. An audit recommendation alone does not authorize unrelated cleanup. Use only integration or recovery interfaces the runtime actually exposes, and only after fresh exact approval.

## Trusted flow controls

Use the current runtime's documented retry, blocking and publication controls. Do not hardcode limits or recreate controller logic here.

Preserve durable blocks. A plain resume or rerun never authorizes an explicit retry control such as `--retry-blocked`. Retry only where the runtime's documented behavior allows it, or with the user's explicit authorization. Do not automatically relaunch after exhaustion or no-progress stops.

For Epic work, use the normal publication path (a PR per child in the per-child PR model). For standalone work, use only the supported mechanism established above.
