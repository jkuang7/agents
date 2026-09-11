---
name: to-tickets
description: Break a plan, spec, or the current conversation into tracer-bullet tickets, published to the configured tracker with blocking dependencies and native sub-issue links to an existing parent spec.
---

# To tickets

Break a plan, spec, or conversation into a set of **tickets**: tracer-bullet vertical slices, each declaring the tickets that **block** it.

For work under `/Volumes/T9/Dev/repos`, resolve the target repository and read [the shared issue-tracker convention](/Volumes/T9/Dev/docs/agents/issue-tracker.md) and [triage label mappings](/Volumes/T9/Dev/docs/agents/triage-labels.md) before tracker operations. Apply any target repository overrides from its `AGENTS.md` or `CLAUDE.md`. Elsewhere, use the project's configured tracker and labels; if missing, establish them before publishing.

Before drafting or revising the breakdown or ticket bodies, read [unslop](/Users/jian/.codex/skills/unslop/SKILL.md) and apply its editing process. Use plain prose and short lists. Do not use tables.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a reference (a spec path, an issue number or URL) as an argument, fetch it and read its full body and comments.

For an existing parent spec, refresh its body and all comments even when the reference came from conversation. Compare the current spec with subsequent human decisions. The spec remains authoritative. Classify contradictions and unresolved decisions in step 3, and reconcile accepted corrections into the spec before publishing affected tickets. Use existing authorization for parent edits; if it does not cover the correction, present the exact edit for approval. Preserve unrelated requirements and human discussion. A `ready-for-agent` label is not human design approval.

### 2. Verify the relevant codebase facts

Inspect the relevant code and contracts unless current evidence already establishes them. Resolve factual uncertainties through investigation before asking the user to make a decision. Ticket titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching.

Identify preparatory changes only when a specific slice needs them. Explain the dependency and preserve existing behavior; keep small preparation within the slice when separating it adds no review or verification value.

Read [bounded implementation handoff](/Volumes/T9/Dev/docs/agents/bounded-handoff.md) when preparing bounded-executor or Sandcastle work. Gather the navigation and proof evidence required by that reference.

### 3. Resolve gaps that change what counts as correct

Compare the spec, later human decisions, and current code evidence. Classify each unresolved concern by its effect on the affected slice:

- A decision needs a human answer when it changes an observable contract, accepted constraint, scope, or consequential tradeoff that existing requirements and authorization do not settle. Multiple internal approaches that satisfy the same contract are implementation discretion. Examples include ownership guarantees, unsafe retry behavior, consistency expectations, and consequential security or operational tradeoffs. Identify the requirement or acceptance test that cannot be settled.
- An implementation detail can remain open when outcomes and constraints already define correctness. Module shape, helper boundaries, and internal mechanisms may emerge through TDD. Record the guarantees to preserve and the observable behavior to test, with room to refactor as evidence develops.
- A factual uncertainty needs investigation. Read the code or service contract, or define a bounded investigation with a concrete question and completion criterion. Use its result to determine whether a human decision is still needed.
- An authorized internal decision can still require frontier reasoning. Resolve consequential architecture or coordination during planning when evidence permits. If the contract is settled but realization remains difficult, classify the slice for a frontier executor. Do not treat implementation discretion as evidence that the normal bounded executor is suitable.

Use a short, focused clarification round only for the first category. Follow the question process here directly; the broader `grilling`, `grill-me`, and `grill-with-docs` workflows apply only when the user requests a broader design interview. Ask the smallest set of questions whose prerequisites are settled. For each, explain the current guarantee, missing decision, affected outcome, and recommended answer with its tradeoff. Resolve facts yourself and reuse prior human answers. Continue only with dependent questions exposed by those answers; stop when the affected work has a clear definition of correctness.

Record accepted decisions in the authoritative spec under the authorization rules in step 1. When no spec exists, update the source plan if authorized; otherwise record the decisions in the approved breakdown and relevant ticket bodies. Create a parent spec only when explicitly requested. Treat recommendations in issue discussion as proposals until accepted. A decision is settled for decomposition when the source requirements, recorded decisions, and ticket criteria agree on its observable consequences.

Defer only implementation tickets whose scope or correctness depends on an unresolved answer. Continue drafting and publishing approved, unaffected slices. If an investigation must happen first, propose it as a bounded ticket or next step rather than marking dependent implementation ready. TDD may discover how to meet the contract; it cannot supply a missing product or safety contract.

Gap review is complete when each concern is resolved, assigned to implementation discovery under stated guarantees, or tied to an explicit decision or investigation and the work it blocks.

### 4. Draft vertical slices

Break the work into **tracer bullet** tickets.

<vertical-slice-rules>

- A valid vertical slice advances the parent workflow and remains cognitively coherent enough for one fresh implementation context.
- Prefer the fewest tracer-bullet tickets that satisfy both tests below. Do not split work merely because persistence, orchestration, API access, recovery, or another internal responsibility can be tested independently.
- Test each proposed ticket for verticality: "After this ticket completes, what new part of the parent workflow actually works?" If the answer is only that an internal prerequisite exists, fold it into the earliest ticket that consumes it. Separate it only when it is independently useful to the user, multiple already-approved slices depend on it, or it cannot fit safely in the consuming slice.
- Test each proposed ticket for cohesion: "Is this one coherent behavioral step, or does it bundle several independently meaningful behaviors merely because they occur next to each other in the workflow?"
- Split a proposed ticket when it contains multiple substantial responsibilities with different failure models or external boundaries, independent verification stories, or separate meaningful workflow milestones. Also split when execution would require reasoning about several unrelated state transitions at once.
- Each slice completes a narrow behavior through the relevant layers and verifies its observable outcome. A backend-only change can be a complete slice; add schema or UI work only when the behavior requires it.
- A completed slice is demoable or verifiable on its own
- Set ticket boundaries at behavioral milestones in the parent workflow, not at individual acceptance requirements, modules, or technical subsystems.
- Do not split by module or subsystem merely to reduce size. Split at the next meaningful behavioral milestone, and require every resulting ticket to pass the verticality test.
- Prefer a sequence such as "accept the first child," then "resume accepted work and maintain one draft pull request," then "self-heal concrete controller or CI defects," then "audit and make the exact candidate ready." This is better than separate inventory, persistence, adapter, and correction-state tickets, and better than one ticket that combines resume, publication, reconciliation, correction, CI recovery, and final readiness.
- Do not create preparation, foundation, or infrastructure milestones merely to mirror internal architecture.
- Treat context-window size as a constraint after finding behavioral boundaries. Use cognitive coherence, not raw line count or file count, to decide whether a vertical slice is overloaded. Context-window size is not by itself a reason to horizontalize the design.
- For bounded-executor or Sandcastle work, each slice passes the separate cognitive-suitability assessment in the shared handoff reference and records `bounded`, `frontier`, or `blocked` with evidence. Small context size alone is insufficient.
- Keep preparation, foundations, and infrastructure in the first slice that uses them. Separate preparatory work only when folding it into that slice would make the slice unsuitable for execution under the criteria above. Name the consuming slice, explain the exception, and make the dependency explicit.

</vertical-slice-rules>

#### Separate implementation from externally gated proof

A ticket should not be blocked by an external authorization, credential, environment, or test target unless that external dependency is inherently required to implement the behavior itself.

Classify prerequisites during decomposition:

- Implementation prerequisites are code or behavior that must exist before the slice can be built.
- Verification prerequisites are external conditions needed only to prove completed behavior in a real environment.

If local tests, mocks, fixtures, or integration seams can implement and verify the behavior without the external dependency, keep the implementation ticket independently executable. Create a separate live-proof or operational-validation ticket when the real end-to-end check requires explicit authorization, credentials or infrastructure may be unavailable, the validation target is externally provisioned, or a validation failure should produce evidence about an otherwise completed implementation.

The live-proof ticket depends on the completed implementation slice and the exact external authorization or environment. Its outcome is concrete evidence about the implemented workflow in that target. Record the external gate as an external prerequisite rather than inventing an infrastructure ticket whose only purpose is to hold the dependency.

Prefer "implement audit and readiness," followed by "prove the complete workflow in an authorized disposable Epic," over one implementation ticket that remains blocked until someone authorizes a disposable repository. Keep live proof in the implementation ticket when the real environment is necessary to implement or meaningfully verify the behavior.

Give each ticket its **blocking edges**: the other tickets that must complete before it can start. Record external prerequisites separately from ticket edges. An approved implementation ticket with settled requirements and no implementation blockers can start immediately.

**Decomposition must preserve the parent contract, not enlarge it.**

- Carry every parent acceptance requirement, invariant, safeguard, accepted failure or recovery policy, and proof or verification obligation into the slices that implement or verify it. Keep ticket criteria self-contained because execution workers may receive parent and child bodies without comments.
- Draft acceptance criteria from the accepted contract. Do not invent failure handling, recovery behavior, retries, reconciliation rules, architecture constraints, or proof obligations to make a ticket look complete.
- When a required test or end-to-end check must exercise a specific branch, use an intentional, reproducible trigger where possible, such as a controlled fixture, known failing case, adapter behavior, or test Epic. If the trigger cannot be controlled, state that uncertainty and do not treat an accidental occurrence as acceptance evidence. Add no generalized testing or recovery infrastructure unless the existing contract requires it.
- If decomposition reveals a missing requirement that changes observable behavior, correctness, scope, or an important architectural constraint, revise the parent spec before publishing the affected implementation tickets.
- Leave implementation details, module boundaries, helper shapes, refactors, and mechanism choices to implementation discovery through TDD when the contract already defines correctness. Do not promote them into ticket acceptance criteria.
- Use a named cross-slice checkpoint only when the parent contract requires behavior that cannot be verified within one slice. Do not add checkpoints for completeness or project-management ceremony.

Use issue discussion to inform decomposition, and distinguish unaccepted suggestions from requirements. For details left to TDD, state the outcomes and constraints implementation must preserve while leaving discovery open. Reference the `tdd` skill when test-first implementation is intended.

For routed work, immediate execution also requires its selected capability tier to be available. Split known independent behavior; resolve missing design upstream; retain frontier implementation for irreducible difficulty. Keep the parent invariants and evidence intact when choosing slice boundaries.

For a shared schema or interface change whose callers cannot migrate in independently passing slices, read [WIDE-REFACTORS.md](references/WIDE-REFACTORS.md) before choosing the ticket sequence. It covers compatibility migrations and the integration-branch exception.

Write each ticket for someone who has not worked in the codebase. Introduce the relevant application context and one concrete action. Explain its current flow, the problem and cause, the intended flow, and why the difference matters. State what stays unchanged when it constrains the slice. Keep this explanation proportional to the change and understandable without opening comments or source links. Links support evidence and navigation.

### 5. Review the breakdown

Present the proposed breakdown as a numbered list. For each ticket, show:

- Give a short title.
- Identify prerequisite tickets, if any.
- Explain the current problem and the observable change the ticket delivers.
- Explain why the ticket is one coherent behavioral step. Identify any substantial adjacent behavior that belongs in a later milestone.
- Distinguish implementation prerequisites from external conditions needed only for live proof.
- For routed work, show the execution suitability and any unresolved prerequisite.

Present enough detail to assess slice size, dependencies, and any proposed merges or splits. Use existing approval when it covers this breakdown; otherwise ask for approval of the concrete proposal. Keep design questions in step 3 so granularity approval cannot silently settle behavior.

During review, reject or merge any proposed ticket whose only observable outcome is that later tickets can now be implemented. Also reject and split a ticket that advances the workflow but contains multiple independently substantial behavioral responsibilities. Apply both the verticality and cohesion tests from step 4 before asking for approval. When splitting an overloaded slice, verify that every resulting ticket still makes a new part of the parent workflow work.

For each externally blocked ticket, ask: "Is this ticket blocked because its behavior cannot yet be implemented, or only because its final live proof needs an external prerequisite?" If only the proof is externally gated, split the live proof into its own downstream ticket. Keep the implementation ticket ready when local, mocked, fixture, or integration seams can distinguish success from failure. The downstream ticket must name both the completed implementation slice and the external authorization or environment it requires.

A ticket is ready to publish for implementation when its required behavior is settled, accepted requirement corrections are recorded, and its acceptance criteria let an implementation worker distinguish success from failure. List deferred work separately with its unresolved prerequisite. Keep implementation discovery open where step 3 established sufficient guarantees.

### 6. Publish the tickets to the configured tracker

Before publication, verify that every ticket dependency points to a known ticket or approved slice and represents a real implementation prerequisite. Verify external prerequisites separately and attach them only to the tickets that need them. Check the proposed ticket graph together with relevant existing dependencies for cycles and self-dependencies. Resolve invalid edges before publishing affected tickets.

Publish the approved tickets to the tracker resolved above:

- For local files, write one file per ticket under `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01` in dependency order (blockers first). Each file's "Blocked by" section lists its prerequisite numbers and titles. Use the shared ticket format below, with one ticket per file.
- For an issue tracker such as GitHub or Linear, publish one issue per ticket in dependency order (blockers first) so each ticket's blocking edges can reference real identifiers. Use native blocking dependencies where supported, and retain the "Blocked by" references in each issue body. Apply `ready-for-agent` to settled implementation work; blocked work retains the appropriate pending status. Dispatch additionally requires verified support for its declared route and refusal of unavailable routes.

When the source is an existing parent spec issue, attach every published ticket using the tracker's native parent/sub-issue relationship. On GitHub, add the tickets as sub-issues of the spec so it serves as the epic. Keep the `## Parent` reference for readability and fallback consumers. Parentage means scope membership; blocking dependencies mean execution order and must be recorded separately. If the source is only a plan file or conversation, omit parentage unless the user supplies or requests a parent issue.

For Sandcastle publication or revision, follow the [Sandcastle handoff](/Volumes/T9/Dev/docs/agents/bounded-handoff.md#sandcastle-handoff) after child IDs exist. Complete its metadata and reconciliation checks before declaring publication complete.

Read back each published ticket body and its native blocking relationships, including all pages. Verify that the acceptance criteria and dependency direction match the approved breakdown, every target exists, and body references agree with native relationships. Recheck for cycles through relevant existing dependencies. When a parent exists, read its complete sub-issue list and verify every published ticket is attached. For local files, perform the equivalent body and dependency checks against the written files. When native dependencies are unavailable, verify body references and disclose that limitation.

On retries, reuse the issues already created and add only missing relationships; preserve any existing different parent and report the conflict. If creation, attachment, or dependency verification fails, report the created identifiers and exact missing or mismatched relationships so the operation can resume. Preserve unrelated relationships and resolve conflicting edits before changing them.

Use text-only parent references when the tracker lacks native hierarchy support, and disclose that limitation. Partial native attachment is incomplete. Sandcastle uses native children when any exist and only falls back to `## Parent` references when none exist.

Publication is complete when all approved tickets have verified bodies, required parent links, and a valid dependency graph matching the approved breakdown. Report canonical issue URLs or local paths, deferred work, and any incomplete verification. Identify the tickets whose blockers are all done as the next available work. Ticket publication does not start implementation.

Attaching the approved children is part of publishing. Preserve the parent issue's title and open/closed state. Limit parent body edits to authorized spec reconciliation and the required Sandcastle milestone declaration; preserve unrelated content and discussion.

## Ticket format

Use the shared body below for local files and tracker issues. For local files, prepend `# <NN>: <Ticket title>` and include `## Status` with the applicable status, normally `ready-for-agent` for published implementation work. Use local numbers and titles for dependencies. For tracker issues, put the title in the issue title field and use canonical issue references. Omit optional sections when they add nothing.

<ticket-template>

## Parent

Link the existing parent spec when present. Omit this section otherwise.

## Context and current behavior

Introduce the relevant part of the application and one concrete action. Explain what happens now, what is wrong or missing, and its cause. Define unfamiliar domain terms as needed.

## Intended change

Follow the same action after the change. Explain the new outcome, how the change addresses the cause, and why it matters. Include accepted constraints and preserved behavior needed to understand the scope.

## Acceptance criteria

- [ ] State an observable outcome that distinguishes success from failure.
- [ ] Include applicable failure behavior, risk safeguards, and evidence needed to verify the slice.

## Implementation discovery

Optional. Identify details implementation may discover through TDD, along with the settled behavior, constraints, and agreed test boundaries it must preserve. For an investigation ticket, state the question, evidence to gather, and completion criterion instead of inventing an implementation outcome.

## Implementation anchors

For routed work: owning responsibility, searchable interface, analogous implementation, and inspected revision. Mark prerequisite outputs as planned.

## Verification seams

For routed work: observable seam, requirement-backed proof cases, controls, focused commands, repository verification, and any cross-slice evidence owner.

## Execution suitability

For routed work: the assessed route, supporting evidence, permitted discovery, and escalation conditions. For Sandcastle, include the execution declaration from the shared reference.

## Blocked by

List the verified prerequisite tickets, or state that there are none. For a live-proof or operational-validation ticket, also name the required external authorization, credential, environment, or test target and distinguish it from ticket dependencies. Keep unresolved human decisions and investigations visible in the deferred-work report; do not label dependent implementation ready while its correctness is unsettled.

</ticket-template>

In either form, distinguish binding contracts from navigation hints and avoid edit scripts. Paths may support discovery at a recorded revision; they do not prescribe exact edits. If a prototype produced a snippet that encodes a decision more precisely than prose can, inline the decision-rich state machine, schema, or type shape and identify its origin. Sandcastle's execution declaration is contract metadata, not implementation code.
