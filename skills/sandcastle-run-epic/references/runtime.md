# Runtime discovery and control

Use the selected trusted runtime's repository instructions, README, CLI/help, and source as the authority. Locate the relevant entry points there before acting. This reference identifies evidence to establish; it does not define runtime behavior or supply fallback controller logic.

## Trusted operator and routing

Inspect operator validation and CLI repository selection. Establish the accepted operator revision, its eligibility under repository policy, and the tracker repository actually selected by the controller. Confirm routing against the requested Epic and durable delivery state, including forks. Keep operator and candidate code separate under the runtime's trust model.

## Delivery identity and durable state

Locate the registered Epic worktree through Git's worktree inventory. Inspect current delivery validation and durable-state loading to establish its repository, branch, worktree identity, and accepted HEAD. Follow workspace placement and retention rules; preserve registered locations and unfinished work.

Account for all durable accepted advances, including corrections or reconciliations where supported. Branch names, issue closure, and the last child receipt alone do not establish current accepted HEAD. Record starting accepted state outside candidate control so fresh evidence can identify children accepted during this invocation. Inconsistent or missing state requires supported recovery or a reported stop.

## Controller ownership and safe stop

Inspect current locking, process handling, and observation interfaces. Correlate lock/process/log evidence with the selected delivery and active run. A PID, lock, or historical log alone does not establish live ownership. Retain ownership protection while writers or identity remain uncertain.

For an already-live controller, use supported current-run evidence to establish its configured run limit as well as ownership. Compare that evidence with the requested mode, preserving an explicit evidence gap when the active configuration cannot be established.

For a new launch, discover the supported startup and ownership signals from the trusted operator's README, CLI/help, source, capability/state interfaces, and durable state. Start the documented controller in an execution surface that remains alive after this agent returns. Handoff succeeds only after the controller passes preflight and current runtime evidence corroborates that it accepted ownership of the selected Epic delivery. If the controller exits during startup or ownership remains unproven, report a failed handoff.

After confirmed ownership, return without following the run to readiness. Use the documented `--attach` or `--attach-worker` watcher only for an explicit observation request; these are read-only interfaces, and stopping one leaves the controller running.

For an explicitly requested stop/change, use the supported controller interface. Wait for the controller and its writers to exit and ownership to release before a replacement launch. Re-read accepted HEAD after shutdown because acceptance may finish during interruption. Recover stale ownership only through the documented procedure after proving its writers have exited. Stopping a read-only observer does not stop the controller.

## Cumulative PR

Inspect current publication lookup and validation to resolve the cumulative PR for this delivery. Confirm its identity and target through runtime-established evidence. Reuse it or leave creation to normal publication. Ambiguous or conflicting PR evidence requires a stop rather than guessing or creating a replacement.

## Invocation and retry/recovery

Discover current command forms and run-limit semantics from CLI/help and the entry point. Use the existing controller and read-only observation interfaces.

For authorized retry or recovery, establish the supported control and its prerequisites from current runtime documentation and validation code. Durable blocks remain binding without explicit retry authorization. Provenance reconciliation alone does not establish approval. Unsupported controls require a reported stop; preserve state rather than substituting manual integration or an outer retry loop.

## Fresh state

Read durable accepted state, invocation receipts/logs, and cumulative PR metadata together when establishing starting state, ownership, or an explicitly requested observation result. Process exit, observer exit, or a ready flag alone does not prove ownership or completion.
