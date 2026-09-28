---
name: to-spec
description: "Understand the problem, find the simplest change that fixes its root cause, and publish it as a draft spec PR or Epic issues."
disable-model-invocation: true
---

# To spec

Write the smallest spec that solves the real problem. Every requirement costs effort to build, review, and maintain, so try the simplest fix before anything bigger.

## 1. Understand the problem

- **Goal:** State what the human is trying to achieve, including tradeoffs such as cost against quality. If they asked for a specific solution or measurement, find the problem behind it. A suggested mechanism is a hypothesis, not a requirement, unless they confirm it.
- **Root cause:** Before designing anything, work out the bottleneck, the constraints, and what makes this hard. Base it on evidence: logs, data, prior runs, code, and tracker history, read from the original source rather than a wrapper. Theory without evidence is not understanding. For new features with no observed problem, understand the goal, constraints, and existing capabilities to build on.
- **Investigate now:** If existing evidence can answer a question, analyze it yourself now, or ask to. Never spec an analysis tool, report, or telemetry to find a cause. Propose new recording only when existing evidence cannot reveal the problem, and keep it minimal. Say what you could not establish instead of adding speculative requirements.
- **Simplest fix:** Prefer an existing capability, an established practice, or a small direct change. Build more only when the problem needs it, not for hypothetical futures. Name the evidence that will show whether the fix worked.

## 2. Choose the route

- **Single PR:** one focused change that can be reviewed as a whole.
- **Existing Epic:** fits that Epic's goal without making its final PR much harder to review; otherwise use a separate Epic.
- **New Epic:** several child issues that add up to one reviewable final PR.
- **Multiple Epics:** only when no single reviewable PR can deliver the goal. Each Epic must be safe to merge alone, even if no later one happens. Do not nest Epics.

Every final PR must be safe to merge: existing behavior preserved, touched behavior complete, no half-finished user flow. Epic children must be reviewable and provable on their own and combine safely, but they do not need to ship alone, so skip feature flags or compatibility layers added just for a child.

Show the goal, your understanding of the problem, the proposed fix, and the route. Wait for the human to confirm before drafting.

## 3. Write the spec

Add a requirement only if the fix fails without it. Describe observable outcomes, not implementation, unless the mechanism is the fix. Never trade correctness for brevity.

- **Acceptance criteria:** Prove behavior with fast, deterministic tests. If the outcome truly needs a slow or external check, keep it and keep it narrow.
- **Failures:** Cover a failure only if it can actually happen and would block progress, corrupt data, report a false or wrong result, break existing behavior, or make a merge unsafe. For unattended work, say when it continues, when it stops for a human, that failed work cannot advance, and where it restarts. Do not design retry or recovery machinery the goal does not need.
- **Questions:** Ask only when an implementer would otherwise have to invent product behavior, and give a recommended answer.
- **Blockers:** If the confirmed goal cannot be met as stated, stop and bring the human a smaller or alternative proposal. Do not add infrastructure or drop a confirmed guarantee yourself.
- **Someone else's draft:** List what you removed and why, so the human can restore anything they need.
- **Epics:** Draft the parent and every child before review. Children proposed by `to-tickets` go through review too.
- **Size:** Aim for under about 4,000 characters and five acceptance criteria per spec. Explain if you go over. If staying under would change the confirmed route or child split, ask the human first. State each requirement once.

## 4. Review

Start a fresh reviewer in a new context. Give it the goal, the guarantees the human confirmed, the agreed understanding and route, and the full spec. Mechanisms the human only suggested are not binding. The reviewer may check stated facts against their sources.

Its first question: **is there a much simpler change that fixes the same root cause?** Then it checks scope, route, and child split; that every requirement is needed; that acceptance criteria are clear and sufficient; and that every final PR is safe to merge.

The reviewer returns at most one important finding. Prefer fixing it by removing or narrowing a requirement. If the fix would change the agreed understanding, fix, or route, or drop a confirmed guarantee, ask the human instead. Otherwise revise and start a new reviewer on the full spec. Stop after a clean pass. After three passes with findings, show the human the spec, your revisions, and the open finding, and ask how to proceed. Resumed review restarts the count and still needs a clean pass.

## 5. Publish

Follow the repository's instructions and tracker policy.

- **Single PR:** Do not wait for approval. Create a `spec/<short-name>` branch from the latest `main` with one empty commit, open a **draft** PR with the spec as its body, and end with the link. The human reviews and edits the spec there. Opening the PR does not start Sandcastle.
- **Epics:** Show the final specs and wait for approval. Then create or update the child issue in an existing Epic, or create the approved Epics and child issues. Each child issue is the binding spec; the parent is context.

Do not modify Sandcastle under this skill.
