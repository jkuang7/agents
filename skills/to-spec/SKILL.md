---
name: to-spec
description: "Find the cause behind accepted intent, choose the simplest change that addresses it, route it to a reviewable single PR or Epic plan, and publish the spec after approval."
disable-model-invocation: true
---

# To spec

Turn a goal into the smallest change that solves the real problem, written as a contract a Sandcastle worker can implement and a human can review in one pass. Every new requirement is work to build, review, and maintain, so the default is less: validate the simplest fix before graduating to anything larger.

## 1. Find the cause

State the human's goal in their terms, including its tradeoffs, such as cost against result quality. When the request names a solution or a measurement, identify the problem it serves; the requested solution is a hypothesis, not the goal. For new behavior with no observed problem, state the goal and the existing capabilities it builds on, then go to step 2.

When the request fixes or improves an observed problem, before designing anything look at what already exists: logs, stored data, prior runs, code, and tracker history. Find the concrete mechanism producing the problem and show it as a short causal chain with numbers, such as `bulk reads → context grows 19k→149k → every call resends it → 8.5M input per launch`. Read facts at their authoritative source, such as a raw event rather than a wrapper's normalization.

Choose the simplest change that acts on that mechanism, and name the existing evidence that will show whether it worked. Analyzing existing evidence is investigation you do now, or ask the human to let you run first, never a deliverable to spec: do not spec an analysis tool, report, or telemetry to find a cause. Propose new recording only when existing evidence cannot identify a cause, and then only the minimum that would identify it. Say what you could not establish instead of filling the gap with speculative requirements.

## 2. Choose the delivery shape

- **Single PR:** one focused change can be implemented, tested, and reviewed as a whole.
- **Existing Epic:** the work serves that Epic's goal and original intent without making its final PR materially harder to review. Otherwise recommend a separate related Epic.
- **New Epic:** several coherent child assignments help implementation, while their result is still one reviewable final PR.
- **Multiple related Epics:** no single reviewable PR can deliver the goal. Split only at boundaries where each Epic is safe to merge alone even if no later Epic happens, with migrations, schemas, and APIs kept compatible where required. Do not nest Epics.

Each final PR must be production-mergeable: existing behavior preserved, touched behavior complete, no half-finished user flow exposed. Epic children are reviewable, independently provable slices that compose safely into the cumulative candidate; they need not be independently shippable, so do not add feature flags or compatibility layers just for a child.

Show the goal, causal chain, recommended change, and route together. Wait for the human to confirm or change them before drafting.

## 3. Write the contract

Start from nothing and add a requirement only when the change fails without it. Specify observable outcomes; include a mechanism only when the mechanism is the fix. Keep correctness: a smaller contract that allows a wrong result is not simpler.

- Prefer acceptance criteria provable with fast, deterministic evidence at an observable boundary. Test behavior, not internal mechanisms. When the outcome inherently needs a slower or external check, keep it and name its narrowest evidence path.
- Include failure behavior only when it is reachable and would prevent required progress, corrupt accepted work or persisted state, report a false success or wrong result, break existing behavior, or make a delivery boundary unsafe. For unattended work, state when it continues, when it stops for a human, that failed work cannot advance, and where it safely restarts. Do not design retry, recovery, or persistence machinery the outcome does not demand.
- Ask the human only about ambiguity that would force an implementer to invent product behavior, with a recommended answer.
- If you discover that the accepted goal cannot be met as stated, stop and return the decision to the human with a smaller or replacement proposal. Do not add infrastructure or drop an accepted guarantee on your own.
- When finalizing someone else's draft, list the requirements you dropped and why, so the human can restore any they own.

For an Epic route, draft the parent and every child contract before review; children proposed by `to-tickets` return to review and approval before publication.

Budget: a single PR contract or Epic child fits in about 4,000 characters with at most five acceptance criteria. Exceeding that requires a stated reason; usually it means the change should be smaller or split. Each requirement appears once.

## 4. Review

Start an independent reviewer in a new context window. Give it only the goal, the confirmed causal chain and route, and the complete spec; it may read minimal authoritative sources to verify stated facts. Its first question is: **is there a materially simpler change that addresses the same cause?** Then it checks that scope matches the intent, the route and any child split are sound, every requirement is needed, acceptance criteria are observable and sufficient, children compose safely into the cumulative candidate, and each final PR is safe to merge.

The reviewer returns at most one material finding. Prefer resolving a finding by removing or narrowing a requirement over adding one. If resolving it would change the confirmed cause, change, or route, or drop an accepted guarantee, return it to the human instead of revising. Otherwise revise, then start a fresh reviewer on the complete revised spec. Stop when a pass finds nothing material. After three passes with findings, return to the human with the spec, the revisions made, and the open finding, and ask how to resolve it; resumed review starts a new count, and approval requires a clean pass.

Show the final spec and wait for human approval before changing GitHub.

## 5. Publish

Resolve repository instructions and tracker policy first, then publish only the approved contracts:

- **Single PR:** create the focused PR; its body is the complete binding contract for standalone Sandcastle execution.
- **Existing Epic:** create or update the appropriate child issue as the binding contract.
- **New or related Epics:** create the approved Epics and only their approved child issues. Each child is the binding contract; the parent carries non-binding context.

Do not modify Sandcastle or add an execution model under this skill.
