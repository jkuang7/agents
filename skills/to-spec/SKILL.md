---
name: to-spec
description: "Understand the problem, find the simplest change that fixes its root cause, and publish it as a single-PR issue or an Epic issue with a linked review PR. Use when the user asks for a spec or names to-spec."
---

# To spec

Write the smallest spec that solves the real problem. Every requirement costs effort to build, review, and maintain.

## 1. Understand the problem

- **Goal:** State what the human is trying to achieve, including tradeoffs such as cost against quality. Behind a requested solution or measurement, find the problem; a suggested mechanism is a hypothesis until they confirm it.
- **Root cause:** Before designing anything, work out the bottleneck, the constraints, and what makes this hard, from evidence (logs, data, prior runs, code, tracker history) read at its original source. Theory without evidence is not understanding. For a new feature, understand the constraints and the existing capabilities to build on.
- **Investigate now:** If existing evidence can answer a question, analyze it now. Never spec an analysis tool, report, or telemetry to find a cause; propose minimal new recording only when existing evidence cannot reveal it. Say what you could not establish instead of adding speculative requirements.
- **Simplest fix:** Prefer an existing capability, an established practice, or a small direct change; build more only when the problem needs it. Name the evidence that will show whether the fix worked.

## 2. Choose the route

- **Single PR:** one focused change of about 350 changed lines or less, delivered by one PR.
- **Existing Epic:** fits that Epic's goal as one more child PR; otherwise use a separate Epic.
- **New Epic:** too large for one PR, delivered as several child issues toward one goal, each its own PR. This skill writes the parent; `to-tickets` writes the children.
- **Multiple Epics:** only when the goals are separate. Do not nest Epics.

**Work order:** Order several pieces of work (problems, Epics, or an Epic's requirements) to win the most speed and reliability soonest, including for agent runs:

1. **Robustness:** anything that makes the system (including Sandcastle) unreliable, or makes agents fail or redo work.
2. **Low-hanging fruit:** quick to build and verify.
3. **Compounding gains:** changes that make every later run faster or less error-prone, such as cleanup that lets agents read less.
4. **New features and high-risk work:** last, because they take longest to prove.

Within a tier, put the larger gain first. A prerequisite goes first. Number an Epic's requirements in this order, and show each item's tier with the route.

**Safe to merge:** Every PR must be safe to merge on its own, even if no later issue in its Epic happens: existing behavior preserved, touched behavior complete, no half-finished user flow. When a flow cannot be finished within one PR, keep its incomplete part unreachable until the issue that completes it.

Show the goal, your understanding of the problem, the proposed fix, and the route. Wait for the human to confirm before drafting.

## 3. Write the spec

Add a requirement only if the fix fails without it. Describe observable outcomes unless the mechanism is the fix. Leave modules, interfaces, and design direction to `to-tickets` and implementation. Never trade correctness for brevity. Use the repository's `CONTEXT.md` vocabulary and respect its ADRs.

A single-PR spec and an Epic parent use these sections in this order; children use the `to-tickets` format. Omit an empty optional section; add no others.

1. `## Goal`: the outcome and its tradeoffs, and whether this delivery achieves it or only enables a later step. It also names a **real-world check**: one concrete command or observation on real data (or a stated scripted substitute) that shows the goal, or the enabled step's outcome, was met, such as "`--usage` on a real run log shows non-zero totals". Passing tests alone are not one. The review of the issue, or of an Epic's last child, runs it. When the result depends on a model's judgment, state what counts as a pass.
2. `## Problem`: current behavior, the root cause, and the evidence with its source. Say what you could not establish.
3. `## Requirements`: numbered `R1`, `R2`, and so on, each one observable outcome, stated once.
4. `## Acceptance`: numbered `A1`, `A2`, and so on. Each one names the requirements it proves, such as `(R1)`. Every requirement has at least one.
5. `## Constraints` (optional): existing behavior or invariants that must not change.
6. `## Failures` (optional): see below.
7. `## Open questions` (optional): only where an implementer would otherwise invent product behavior, each with a recommended answer.
8. `## Out of scope`: what a reasonable implementer might otherwise do.

- **Readability:** Write for a human reviewer: plain sentences, no jargon, a shared lead-in once above a list.
- **Wording:** State a requirement's reason when it isn't obvious, so the implementer can handle uncovered cases; implementers stop on wrong wording rather than override it. Use always, never, or only only when any exception would be a defect.
- **Acceptance criteria:** Prove behavior with fast, deterministic tests at the fastest level that catches the regression: unit for a rule, integration through the real entry point when the risk is in how parts fit, end-to-end only when it spans the whole system. Keep a truly needed slow or external check narrow.
- **Existing tests:** for each acceptance criterion that changes behavior, search the existing tests for assertions of the behavior it replaces, and for tests whose setup relies on it, such as a removed flag or a skipped step. Name every hit in the acceptance text ("Existing tests pass with assertions unchanged, except: …", with the new expectation), and name a family of variants (parametrized or cached cases) by file and pattern. An implementer told to keep tests unchanged stops when one contradicts the spec, which costs a full implementation.
- **Failures:** Cover a failure only if it can happen and would block progress, corrupt data, report a wrong result, break existing behavior, or make a merge unsafe. For unattended work, say when it continues, when it stops for a human, that failed work cannot advance, and where it restarts. Do not design retry or recovery machinery the goal does not need.
- **Rules:** For each rule that sorts cases into outcomes (retry or stop, accept or reject), give a realistic example of each outcome and at least one realistic case the rule must not cover, such as "Transient: a dropped connection. Not transient: expired auth, a 404." Without a counterexample, a wrong rule is built exactly and passes every review.
- **Saved results:** For each new piece of saved state, cached result, or recorded decision, name every input that invalidates it and every path that reuses it (a fresh run, a resume, a replay), and say in `## Failures` what happens on a crash before and after it is written, on a rerun, and when its inputs change mid-run. A result keyed on only some of its inputs goes stale silently.
- **Blockers:** If the confirmed goal cannot be met as stated, stop and bring the human a smaller or alternative proposal. Do not add infrastructure or drop a confirmed guarantee yourself.
- **Someone else's draft:** Tell the human what you removed and why in your reply or a PR comment, never in the spec, which workers read as binding.
- **Size:** Aim for under about 4,000 characters and five acceptance criteria. Explain if you go over; if staying under would change the confirmed route, ask first.

## 4. Review

Start a fresh reviewer in a new context. Give it the goal, the confirmed guarantees, the agreed understanding and route, and the full spec; mechanisms the human only suggested are not binding. It may check stated facts against their sources.

Its first question: **is there a much simpler change that fixes the same root cause?** Then it checks the spec against every rule in sections 2 and 3. For each rule in the spec, it tries to find a realistic case where the rule gives the wrong answer.

**Review loop** (`to-tickets` uses it too): The reviewer returns every important finding it can support, most important first. Prefer fixing each by removing or narrowing a requirement. If a fix would change the agreed understanding, fix, or route, or drop a confirmed guarantee, ask the human instead; otherwise revise for all findings. If a pass's fixes add requirements or machinery (saved state, formats, rules), look for a simpler design that drops the need; if none exists, ask the human whether the goal is worth it. After each pass that changed a requirement or the design, start a new reviewer on the full spec. Stop when a pass finds only wording or test tightening; apply it. Stop for the human early only when a fix needs their decision or review stops converging (a fixed finding returns, or a pass finds at least as many requirement- or design-level problems as the last). Then show the spec, your revisions, and the open findings.

## 5. Publish

Follow the repository's instructions and tracker policy.

- **Single PR:** Do not wait for approval. Create one issue with the spec as its body and no sub-issues, and end with the link; the human reviews and edits it there. Publishing does not start Sandcastle.
- **New Epic:** Do not wait for another approval after review. Create the GitHub Epic issue with the parent spec as its body. Create a `spec/<short-name>` branch from the latest `main` with one empty commit and open a **draft Epic spec PR** with the same spec as its body; link it and the Epic issue. End with both links. The Epic issue is the parent for native subissues; the draft PR is only its review surface. Do not publish child issues or start Sandcastle until the human approves the PR's spec. Then apply any approved edits to the Epic issue, use `to-tickets` to write and publish the children, and close the spec PR unmerged with a link to the Epic and delete its branch. Each child issue is the binding spec; the parent is context.
- **Existing Epic:** Confirm the Epic, then use `to-tickets` to add the child issue from the confirmed need.

Do not modify Sandcastle under this skill.
