---
name: specs
description: "Understand the problem, find the simplest change that fixes its root cause, and publish it as a single-PR issue or an Epic with child tickets, asking the human only when the direction is unclear. Use when the user asks for a spec or names specs or to-spec."
model: opus
effort: medium
---

# Specs

Write the smallest spec that solves the real problem; each requirement costs build, review and upkeep. Run end to end: understand, spec, review, publish, and for an Epic, `to-tickets`, then `/babysit`.

**Decisions:** A decision is any choice this skill or `to-tickets` would otherwise put to the human. Decide it yourself (escalating as the `route` skill says) and sort it:

- **linear:** one obvious answer. Apply it.
- **shape:** several workable answers. Take the one with the least machinery.
- **unclear:** the goal or product behavior is ambiguous, you aren't confident, or the answer would drop a confirmed guarantee, need auth or credentials, add a paid service, or be hard to reverse. Stop, send a push notification (PushNotification), and ask the human with AskUserQuestion, recommended option first.

What the human said is confirmed; a linear or shape decision counts as confirmed from then on. After publishing, post every linear and shape decision as one **decisions comment** on the parent issue, one line each with its reason.

## 1. Understand the problem

- **Goal:** State what the human is trying to achieve, including tradeoffs such as cost against quality. Behind a requested solution or measurement, find the problem; a suggested mechanism is a hypothesis.
- **Root cause:** Before designing anything, work out the bottleneck, the constraints, and what makes this hard, from evidence (logs, data, prior runs, code, tracker history) read at its original source. For a new feature, find the existing capabilities to build on.
- **Investigate now:** Analyze existing evidence now instead of speccing an analysis tool, report or telemetry to find a cause; propose minimal new recording only when existing evidence cannot reveal it. Say what you could not establish; add no speculative requirements.
- **Simplest fix:** Find the simplest fix to maintain: fewest moving parts, least new state; reuse or delete before building, preferring an existing capability, established practice or small direct change. It must still meet every confirmed goal and guarantee. The human's idea stays the default unless yours is clearly simpler for the same problem; then recommend yours and say what it gives up. Name the evidence that will show the fix worked.

## 2. Choose the route

- **Single PR:** one focused change no larger than one `to-tickets` slice (about 150 non-test changed lines, counted as `to-tickets` does).
- **Existing Epic:** fits that Epic's goal as one more child PR; otherwise use a separate Epic.
- **New Epic:** too large for one PR: several child issues toward one goal, each its own PR. This skill writes the parent; `to-tickets` writes the children.
- **Multiple Epics:** only when the goals are separate. Do not nest Epics.

**Work order:** Order several pieces of work (problems, Epics, or an Epic's requirements) for the most speed and reliability soonest:

1. **Robustness:** what makes the system (including Sandcastle) unreliable or agents fail or redo work.
2. **Low-hanging fruit:** quick to build and verify.
3. **Compounding gains:** changes that speed up or de-risk every later run, such as cleanup that lets agents read less.
4. **New features and high-risk work:** last, because they take longest to prove.

Within a tier, larger gain first; a prerequisite goes just before the work needing it. Number an Epic's requirements in this order and show each item's tier with the route.

**Safe to merge:** Every PR must be safe to merge alone, even if no later Epic issue happens: existing behavior preserved, touched behavior complete, no half-finished user flow. Keep a flow's incomplete part unreachable until the issue that completes it.

Show the goal, problem understanding, fix (beside the human's idea when it differs, with your recommendation) and route as one decision; draft unless unclear.

## 3. Write the spec

Add a requirement only if the fix fails without it. Describe observable outcomes unless the mechanism is the fix. Use `CONTEXT.md` vocabulary and ADRs.

A single-PR spec and an Epic parent use these sections in this order; children use the `to-tickets` format. Omit an empty optional section; add none.

1. `## Goal`: the outcome and its tradeoffs, and whether this delivery achieves it or only enables a later step. It also names a **real-world check**: one concrete command or observation on real data (or a stated scripted substitute) that shows the goal, or the enabled step's outcome, was met; passing tests alone are not one. The review of the issue, or of an Epic's last child, runs it. When the result depends on a model's judgment, state what counts as a pass.
2. `## Problem`: current behavior, the root cause, and the evidence with its source. Say what you could not establish.
3. `## Requirements`: numbered `R1`, `R2`, and so on, each one observable outcome, stated once.
4. `## Acceptance`: numbered `A1`, `A2`, and so on. Each one names the requirements it proves, such as `(R1)`. Every requirement has at least one.
5. `## Constraints` (optional): existing behavior or invariants that must not change.
6. `## Failures` (optional): see below.
7. `## Open questions` (optional): only where an implementer would otherwise invent product behavior, each with a recommended answer.
8. `## Out of scope`: what a reasonable implementer might otherwise do.

- **Readability:** Plain sentences, no jargon, a short label per numbered item.
- **Wording:** State a requirement's reason when it isn't obvious, so the implementer can handle uncovered cases.
- **Rules, not examples:** A goal or requirement saying "always", "every", "never", "whatever" or "any" must list the paths it covers as acceptance cases or state what is out of scope and why; otherwise narrow it. The review rejects one with neither. When acceptance comes from a known failure, state the rule it breaks, give the failure as one example, list the paths the rule covers, and require a test for each; listed cases are read as complete. For a rule that sorts cases into outcomes (retry or stop, accept or reject), give a realistic example of each outcome and one realistic counterexample it must not cover (transient: a dropped connection; not transient: a 404)
- **Acceptance criteria:** Prove behavior with fast, deterministic tests at the fastest level that catches the regression: unit for a rule, integration through the real entry point when the risk is in how parts fit, end-to-end only when it spans the whole system.
- **Existing tests:** for each acceptance criterion that changes behavior, search the existing tests for assertions of the behavior it replaces, and for tests whose setup relies on it, such as a removed flag or a skipped step. Name every hit in the acceptance text ("Existing tests pass with assertions unchanged, except: …", with the new expectation), and a family of variants (parametrized or cached cases) by file and pattern.
- **Failures:** Cover a failure only if it can happen and would block progress, corrupt data, give a wrong result, break existing behavior, or make a merge unsafe. For unattended work, say when it continues, when it stops for a human, that failed work cannot advance, and where it restarts. Handle each by the first option that works: make it impossible by design (one representation per fact), else stop with a clear error, else recover automatically, only when stopping has hurt or the goal requires it.
- **Consumers:** When a requirement changes a shared file, result shape or loop, list every consumer (or state you found none) and the change's behavior on each failure and retry path.
- **Variants:** When a requirement adds a second variant of something hard-coded at several call sites (a tool, host, format or service), name the one place that will own the variants' facts and the call sites that must stop knowing which variant they have. A data table or one function is enough. With one call site, say so and require nothing.
- **Saved results:** For each new piece of saved state, cached result, or recorded decision, name every input that invalidates it and every path that reuses it (fresh run, resume, replay), and say in `## Failures` what happens on a crash before and after it is written, on a rerun, and when inputs change mid-run.
- **Blockers:** If the confirmed goal cannot be met as stated, a smaller or alternative proposal is an unclear decision; never add infrastructure or drop a confirmed guarantee yourself.
- **Someone else's draft:** Say what you removed and why in the decisions comment, never in the spec, which workers read as binding.
- **Size:** Aim for under about 4,000 characters and five acceptance criteria, excluding what other rules here require.
- **Architecture (Epics):** End an Epic's `## Goal` with `Architecture: extend` or `Architecture: reshape` and the intent in words: which responsibilities need one home, and why. Reshape for a new app, or when the current layout would force copied helpers or misplaced code. Name no files; the reshape slice records homes in the `AGENTS.md` code map. A large reshape is an unclear decision.

## 4. Review

Start a fresh reviewer in a new context (in Claude, the `reviewer` agent) with the goal, the confirmed guarantees, the agreed understanding and route, and the full spec; suggested mechanisms are not binding.

Its first question: **is there a much simpler change that fixes the same root cause?** Then it checks the spec against every rule in sections 2 and 3, including a finding for each unbounded absolute claim. It checks that a spec adding a variant names that owner (or a single call site) and flags speculative layering.

**Review loop** (`to-tickets` uses it too): For each rule in the work under review, the reviewer tries to find a realistic case where the rule gives the wrong answer and returns every important finding it can support, most important first. Prefer removing or narrowing a requirement. A fix that changes the agreed understanding, fix, or route is a decision; dropping a confirmed guarantee is always unclear; otherwise revise for all findings. After a pass that changed a requirement or the design, start a new reviewer on the full work. Stop when a pass finds only wording or test tightening; apply it.

**Design smell:** Sort each finding. A **robustness** fix tightens existing behavior (a missing failure case, test or wording gap); apply it. A **decision** fix needs a new rule, mode, cap, or exception, a guard for another guard, or a choice by the human. If a pass has a decision fix, or most findings trace to one capability, stop and choose **one cut**: less power for that capability, or one approval point instead of a set of rules. Record what it gives up. Take it as a shape decision; rerun review; a cut dropping a confirmed guarantee is unclear. Review that stops converging (a fixed finding returns, or a pass finds at least as many requirement- or design-level problems as the last) is unclear: show the human the work and open findings.

## 5. Publish

Follow the repository's instructions and tracker policy. Publish several items in work order, each with its own decisions comment.

- **Single PR:** Create one issue with the spec as its body and no sub-issues, and end with the link. The human reviews it via the decisions comment; once queued, changes go through `sandcastle-change-request`.
- **New Epic:** Create the Epic issue with the parent spec as its body and the `not-ready` label (create it if missing) so a runner skips it until it has children; it is the spec's only copy. Then run `to-tickets` on it now, which removes the label, and end with all links. Each child issue is the binding spec; the parent is context.
- **Existing Epic:** Choosing the Epic is a decision; then use `to-tickets` to add the child issue from the confirmed need.

After publishing, invoke `/babysit` for the repository in this same thread so the published issues run without a separate handoff.
