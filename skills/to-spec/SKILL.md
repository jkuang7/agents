---
name: to-spec
description: "Understand the problem, find the simplest change that fixes its root cause, and publish it as a single-PR issue or an Epic parent issue."
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
- **Existing Epic:** fits that Epic's goal as one more child PR, which `to-tickets` writes from the confirmed need; otherwise use a separate Epic.
- **New Epic:** several child issues toward one goal. Sandcastle delivers each child as its own PR, merged to `main` before the next child starts; the last child's review also runs the Epic's real-world check. There is no separate final review.
- **Multiple Epics:** only when the goals are separate. Do not nest Epics.

Every PR must be safe to merge on its own: existing behavior preserved, touched behavior complete, no half-finished user flow. For an Epic this skill writes the parent only; `to-tickets` splits the approved parent into child PRs, each safe to merge alone.

Show the goal, your understanding of the problem, the proposed fix, and the route. Wait for the human to confirm before drafting.

## 3. Write the spec

Add a requirement only if the fix fails without it. Describe observable outcomes, not implementation, unless the mechanism is the fix. Leave modules, interfaces, and design direction to `to-tickets` and implementation. Never trade correctness for brevity. Use the repository's `CONTEXT.md` vocabulary and respect its ADRs.

A single-PR spec and an Epic parent use these sections in this order, so reviewers and `to-tickets` always find the same parts in the same place. Omit an optional section when it would be empty; do not add other sections.

1. `## Goal`: the outcome and its tradeoffs, and whether this delivery achieves it or only enables a later step. An Epic's goal also names a **real-world check**: one concrete command or observation on real data that shows the goal was met, such as "`--usage` on a real run log shows non-zero totals". Passing tests alone is not a real-world check. Name it so the last child's review can run it (or its stated scripted substitute).
2. `## Problem`: current behavior, the root cause, and the evidence with its source. Say what you could not establish.
3. `## Requirements`: numbered `R1`, `R2`, and so on. Each one is a single observable outcome, stated once. The numbers let `to-tickets` and reviewers refer to each requirement.
4. `## Acceptance`: numbered `A1`, `A2`, and so on. Each one names the requirements it proves, such as `(R1)`. Every requirement has at least one.
5. `## Constraints` (optional): existing behavior or invariants that must not change.
6. `## Failures` (optional): see Failures below.
7. `## Open questions` (optional): each with a recommended answer.
8. `## Out of scope`: what a reasonable implementer might otherwise do.
9. `## Evidence of effect` (optional, single-PR specs only; an Epic uses its Goal's real-world check): how the human will know the goal was met, when passing acceptance does not show it.

- **Readability:** Write for a human reviewer first: plain sentences, no jargon a newcomer wouldn't know, and no phrase repeated at the start of every item. Put a shared lead-in once above a list, and give each numbered item a short label.
- **Wording:** When the reason for a requirement isn't obvious, state it, so the implementer can handle cases the wording doesn't cover. Use absolute words (always, never, only) only when any exception would be a defect. If a spec's wording turns out wrong for the task, the implementer stops and reports it rather than overriding the spec, so the reasons must be in the spec.
- **Acceptance criteria:** Prove behavior with fast, deterministic tests. Choose each test's level by the regression it must catch, using the fastest level that catches it: a unit test for a rule, an integration test through the real entry point when the risk is in how parts work together, and end-to-end only when that risk spans the whole system. If the outcome truly needs a slow or external check, keep it and keep it narrow.
- **Existing tests:** for each acceptance criterion that changes behavior, search the existing tests for assertions of the behavior it replaces. Name every hit in the acceptance text ("Existing tests pass with assertions unchanged, except: …", with the test and the new expectation). An implementer told to keep tests unchanged stops when one contradicts the spec, and each such stop costs a full implementation.
- **Failures:** Cover a failure only if it can actually happen and would block progress, corrupt data, report a false or wrong result, break existing behavior, or make a merge unsafe. For unattended work, say when it continues, when it stops for a human, that failed work cannot advance, and where it restarts. Do not design retry or recovery machinery the goal does not need.
- **Rules:** For each rule that sorts cases into outcomes (retry or stop, transient or decision, accept or reject), give a realistic example of each outcome and at least one realistic case the rule must not cover, such as "Transient: a dropped connection. Not transient: expired auth, a missing permission, a 404." A rule without a counterexample is how a spec that looks right ships wrong behavior: the implementer builds it exactly and every reviewer checks against it.
- **Saved results:** For each new piece of saved state, cached result, or recorded decision, name every input that invalidates it, and say in `## Failures` what happens on a crash before and after it is written, on a rerun, and when its inputs change partway through a run. A cached result keyed on only some of its inputs goes stale silently.
- **Questions:** Ask only when an implementer would otherwise have to invent product behavior, and give a recommended answer.
- **Blockers:** If the confirmed goal cannot be met as stated, stop and bring the human a smaller or alternative proposal. Do not add infrastructure or drop a confirmed guarantee yourself.
- **Someone else's draft:** Tell the human what you removed and why, so they can restore anything they need. Put this in your reply or a PR comment, not in the spec, because workers read the spec as binding.
- **Size:** Aim for under about 4,000 characters and five acceptance criteria per spec. Explain if you go over. If staying under would change the confirmed route, ask the human first. State each requirement once.

## 4. Review

Start a fresh reviewer in a new context. Give it the goal, the guarantees the human confirmed, the agreed understanding and route, and the full spec. Mechanisms the human only suggested are not binding. The reviewer may check stated facts against their sources.

Its first question: **is there a much simpler change that fixes the same root cause?** Then it checks scope and route; that every requirement is needed; that an Epic's goal names a real-world check; that acceptance criteria are clear and sufficient and cover every requirement; that every existing test asserting replaced behavior is named as an exception; that single-PR specs and Epic parents follow the section format; and that the PR, or each Epic's goal, can be delivered by PRs that are each safe to merge.

It also looks for rules that are wrong, not only rules that conflict: for each rule, it tries to find a realistic case where the rule gives the wrong answer, and checks that the spec names counterexamples. For each saved result, it checks that the spec names every input that invalidates it and what happens on crash, rerun, and mid-run change.

The reviewer returns every important finding it can support, most important first, so one pass can settle several. Prefer fixing each by removing or narrowing a requirement. If a fix would change the agreed understanding, fix, or route, or drop a confirmed guarantee, ask the human instead. Otherwise revise for all findings. Watch what the fixes do to the spec. If a pass's fixes add requirements or machinery (saved state, new formats, extra rules) rather than remove or narrow them, the design is probably too complex. Before the next pass, look for a simpler design that drops the need, and if none exists, ask the human whether the goal is worth the machinery. A spec that grows on every pass is the same warning sign as a running child whose spec keeps gaining behavior. Start a new reviewer on the full spec only when the pass changed a requirement or the design; when its findings only tighten tests or wording, apply them and stop. Expect two passes: the first finds design problems, the second confirms the fixes. If a third pass still finds requirement- or design-level problems, show the human the spec, your revisions, and the open findings, and ask how to proceed, since the spec likely needs their judgment rather than another round. Resumed review restarts the count.

## 5. Publish

Follow the repository's instructions and tracker policy.

- **Single PR:** Do not wait for approval. Create one issue with the spec as its body and no sub-issues, and end with the link. The human reviews and edits the spec there. Sandcastle runs an issue with no sub-issues as itself, delivering one PR, once its README says it supports that; until then, run it as an Epic with one child. Publishing does not start Sandcastle.
- **Epics:** Show the final parent spec and wait for approval. Then create the Epic issue, or confirm the existing Epic, and ask the human to run `/to-tickets` on it to write and publish the child issues. Each child issue is the binding spec; the parent is context.

Do not modify Sandcastle under this skill.
