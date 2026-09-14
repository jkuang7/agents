---
name: review-approach
description: Decide among consequential, materially different approaches when implementation cannot cheaply settle the choice.
---

# Review approach

Decide between materially different approaches only when the choice is consequential and implementation cannot settle it cheaply.

Use this review when all of these conditions hold:

- The choice is costly or hard to reverse.
- Several credible strategies differ in ways that matter.
- A poor choice would create meaningful risk.
- A small experiment cannot resolve the uncertainty at low cost.

Otherwise, recommend direct implementation when one approach clearly fits. When evidence is missing, recommend the smallest tracer bullet that can provide it.

## Compare the approaches

1. State the desired outcome and fixed constraints.
2. Identify only credible approaches whose differences could change the decision.
3. Compare them on correctness, cognitive load, coupling, testability, reversibility, operational risk, and migration cost when it applies.
4. Prefer the simplest supported approach with the lowest total risk.
5. If a missing fact controls the decision, identify the cheapest experiment that would answer it.
6. Stop when more analysis is unlikely to change the choice.

Use repository behavior and direct evidence when available. Separate known facts from judgment and state any assumption that affects the recommendation.

Keep the result short and readable. Include the outcome, credible options, decisive tradeoffs, recommendation, and the next experiment only when one is needed. Add a formal brief, diagram, or durable decision record only when it helps the people who must act on the choice.

If the best answer is to prove one small behavior first, say that.
