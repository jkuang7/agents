---
name: to-spec
description: "Route accepted intent to a reviewable single PR or Epic plan, draft the smallest complete specification, and publish it after approval."
disable-model-invocation: true
---

# To spec

Turn accepted conversation, codebase context, or an existing issue into the smallest set of meaningful, production-safe delivery units. Each final delivery unit must be production-mergeable. Epic child contracts must be coherent, reviewable implementation slices that accumulate safely into that delivery. Optimize for coherent human review, not the fewest PRs, issues, or Epics.

## Choose the delivery shape

Before drafting the detailed specification, inspect only enough repository and tracker context to recommend one route:

- **Single PR:** one focused change can be implemented, tested, understood, and accepted as a coherent whole.
- **Existing Epic:** the work clearly serves its goal, preserves its original intent, and will not make its cumulative final PR materially harder to review. Otherwise recommend a separate related Epic.
- **New Epic:** multiple meaningful child assignments help implementation, while their accumulated result remains one coherent final PR.
- **Multiple related Epics:** no single reasonably reviewable PR can deliver the overall goal. Split only at semantic delivery boundaries; do not introduce nested Epic machinery without a genuinely separate planning hierarchy.

The final PR is the sizing boundary. A competent reviewer should be able to understand the intent, diff, tests, and correctness of each delivery unit in one reasonable review without reconstructing other unmerged work. File count and line count are evidence only when they affect that judgment. Keep tightly coupled behavior together when splitting would obscure correctness; separate independently reviewable concerns when combining them would overload the review.

Each related Epic must be safe and supportable if merged alone and no later Epic happens. It must preserve existing behavior, leave touched behavior complete, keep migrations, schemas, APIs, and integrations compatible where required, and avoid exposing half-finished user flows. Later Epics may add capability but must not repair an unsafe earlier merge. Add compatibility layers or feature flags only when a concrete boundary requires them.

Show the recommended route and a short reviewability and production-safety rationale. Wait for the human to confirm or change it before drafting detailed specs.

## Converge on the contract

1. Establish the governing outcome, current behavior, important invariants, exclusions, and observable success. Inspect code only where existing context is insufficient. Let the outcome set emphasis: unattended work needs a complete path to success or a useful human handoff; operator-driven work may stop safely between steps.
2. Resolve only consequential ambiguity that would force an implementer to invent product behavior. Ask for the unclear behavior with a simple recommendation and short reason. Prefer an existing invariant or one workflow rule covering a class of cases.
3. Include failure behavior only when it is reachable from the proposed design and could prevent required progress, corrupt accepted work or persisted state, falsely report success, break existing behavior, or make a delivery boundary unsafe. For unattended orchestration, define continuation, human stopping conditions, what failed work cannot advance, and the safe restart boundary before adding specific recovery cases.
4. Write once consequential decisions are resolved. Preserve opinionated requirements; leave implementation mechanisms open unless the mechanism itself is required. Specify testing decisions only when they add useful guidance, favoring observable behavior at stable system boundaries.

Use only sections that improve understanding: problem, desired outcome, user stories, core invariants, testing decisions, additional review or verification boundaries, acceptance criteria, constraints, and out of scope. Each requirement has one home. A competent engineer should understand and judge each concise contract in one pass. Do not add future work, speculative hardening, or generalized infrastructure.

Each contract is complete when a reasonable implementer can build the right behavior without inventing important requirements. For an Epic route, draft the parent context and every needed child contract before review; `to-tickets` may help decompose the confirmed parent shape, but its proposed children must return to this review and approval flow before publication. Child issues are meaningful implementation contracts, not arbitrary slices. For multiple Epics, make each production-safe boundary and any required compatibility behavior explicit.

## Converge through independent review

For every review pass, start an independent reviewer in a new context window. Do not continue or reuse a prior reviewer context. Give it only the original intent, confirmed route, and complete current spec or specs. The reviewer does not implement the task or redesign the product. It checks that:

- the route and contracts are correct, preserve the original intent, and do not expand scope;
- each delivery unit is as small as reasonably possible and practical for a human to review;
- independently reviewable concerns are not combined and tightly coupled behavior is not split artificially;
- each final delivery unit is robust and production-mergeable, and child contracts compose safely without regressions or an invalid intermediate accepted state;
- reachable consequential failures are covered without speculative recovery or machinery;
- acceptance criteria are observable, sufficient, and unambiguous.

When review finds a material problem, it returns one concrete finding. Revise only what resolves that finding, then start an independent reviewer in a new context window on the complete corrected spec. Continue until a full pass finds no material issue: the specs are correct, lean, robust, easy for a human to review, and each final delivery is production-mergeable when completed. Return to the human when convergence requires a new product or architecture decision; do not let the loop reopen unrelated questions or accumulate speculative detail.

After review succeeds, show the final proposed spec or specs and wait for final human approval before changing GitHub.

## Publish the approved shape

Resolve repository instructions and tracker policy before tracker operations. Publish only the approved contracts:

- **Single PR:** create the focused PR; its body is the complete binding contract for standalone Sandcastle execution.
- **Existing Epic:** create or update the appropriate child issue as the complete binding contract.
- **New Epic:** create the Epic and only the child issues required by the approved plan.
- **Multiple related Epics:** create the approved related Epics and their necessary children, preserving the independently safe delivery boundaries.

In Epic work, each approved child is the binding implementation contract; the parent supplies broader non-binding context. Do not add a Sandcastle execution model or modify Sandcastle under this skill.
