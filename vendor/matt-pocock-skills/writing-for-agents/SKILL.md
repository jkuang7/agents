---
name: writing-for-agents
description: Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md.
---

# Writing for agents

Write agent-consumed skills, instructions, and referenced documents so process and boundaries remain predictable across runs.

For skill frontmatter, invocation, and routing, read [SKILL-MECHANICS.md](SKILL-MECHANICS.md). For demonstrated failures or consequential workflow changes, read [MAINTENANCE.md](MAINTENANCE.md) and verify the correction proportionately.

## Instruction ROI

Optimize total cost to a correct outcome, not minimum prompt length. Optimization does not imply deletion. Preserve a document unchanged when its instructions already earn their load. Expand or clarify it when added guidance materially improves the outcome, encodes an important preference, or reduces total work or error risk.

Prefer the smallest genuine improvement, including no change. For each instruction, ask whether keeping, changing, adding, or removing it materially improves total cost to a correct outcome. Leave it alone when none of those changes earns its cost.

Evaluate every instruction as:

- **Outcome**: the state the agent must reach.
- **Opinionated method**: a preference, philosophy, or tradeoff that materially shapes a valid solution.
- **Necessary control**: correctness, authorization, trust, mutation order, recovery, concurrency, interoperability, or stopping boundaries.
- **Incidental mechanics**: execution details a strong agent can safely determine through competence or cheap authoritative discovery.

Keep the first three. Keep mechanics only when they materially reduce work, search, tool calls, ambiguity, or failure probability. Ask whether removing a "how" could yield an apparently correct solution that violates the intended philosophy, tradeoff, or boundary. If so, preserve it.

When an instruction is a true no-op, delete it rather than polishing it. Preserve non-obvious constraints and demonstrated fixes. Remove generic advice, stale branches, speculative guidance, or ceremony when they do not earn their load. Do not redesign a skill just to shorten it or flatten distinctions between roles.

## Context pointers

A pointer names material and the condition for reading it. Skill descriptions and agent-instruction links are pointers. Sharpen weak trigger wording before inlining the target.

Front-load the leading concept, give one trigger per distinct branch, and omit identity already carried by the body. Always-loaded pointers spend context and attention every turn, so prune them harder than bodies.

Before delegating behavior to a pointer, verify that its target exists, is current, and owns that behavior. A moved paragraph or speculative reference establishes no authority; retain the minimum instruction inline when no valid owner exists.

## Information hierarchy

Keep primary actions visible and reference available where needed. Inline what every branch needs; disclose material only some branches reach. Keep each concept's definition, rules, and caveats together. A flat set of peer criteria is valid without manufactured steps.

Progressive disclosure protects execution from excessive reference. Split by a real branch or sequence only when the smaller path earns the extra indirection. Context load is the agent's always-loaded burden; cognitive load is the human's burden of knowing which documents to reach. Spend human load where judgment matters.

## Completion and sequencing

Use checkable, exhaustive completion criteria. "Every modified model accounted for" demands more reliable legwork than "produce a change list."

Sharpen fuzzy bounds before splitting a sequence to prevent premature completion. Hide later steps only when observed rushing persists across an irreducibly fuzzy bound. That requires a real context boundary such as a handoff or worker dispatch; an inline call does not remove later steps from context. Merging sequences can reintroduce that pull.

Use explicit phases when each establishes evidence, reduces uncertainty or recovery cost, or protects a trust or mutation boundary. Each ends in a state that constrains the next action. Omit phases that add only ceremony.

## Leading words

Use compact established concepts such as lesson, frontier, tracer bullet, red, or tight to replace repeated explanations. Define a new concept clearly; prefer an existing word that already carries useful meaning. Reuse the same token in prompts, pointers, and bodies so invocation and execution share vocabulary. Repeat the word, not its definition.

Prefer concrete positive instructions. Retain prohibitions for hard guardrails that cannot be expressed sufficiently through a positive target, and pair them with what the agent should do.

## Ownership and relevance

Each meaning has one source of truth. Runtime wrappers usually need mode and invocation choice, required inputs, boundaries the runtime does not own, and result interpretation: select mode, invoke runtime, inspect result. Retain internal mechanics only when the wrapper must reason about them before invocation. Leave runtime-owned retries, state transitions, lifecycle, recovery, and validation to the runtime.

Prefer source, configuration, CLI help, and repository instructions over prose caching cheap lookups. Document unwritten conventions, rationale, and gotchas the environment cannot reveal. Necessary discovery should be narrow, cheap, and aimed at the owner likely to settle the decision in one pass.

Check every line for relevance and instruction ROI. Delete stale sediment and meanings that no longer bear on the task. Resolve disagreements about model competence through proportionate behavioral evidence rather than adding instructions defensively.
