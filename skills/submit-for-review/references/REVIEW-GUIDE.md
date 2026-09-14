# Write the PR for its human reviewer

Derive the PR body from the delivered candidate. Scale the explanation to the change and its risk. A small change should have a small review guide.

## Start with the concrete problem

State what was wrong before the change and its consequence. Then explain the delivered behavior and why it addresses that cause. Introduce codebase-specific terms only when the reviewer needs them.

Use a before-and-after flow when it clarifies a meaningful behavior change. Include the boundaries and invariants that control whether the result is correct. Do not import planned behavior or speculative risks from a parent spec.

## Give the reviewer a route through the change

Organize review points around important behavior or risk, not a list of every changed file. For each main point:

- Link the code that enforces the behavior, using precise diff or source locations when possible.
- State the contract or decision the reviewer should inspect.
- Link the test or check that provides evidence and explain what it proves.
- Disclose a material evidence gap when no suitable proof exists.

Include commit review order when it helps the reader understand how the solution comes together. Give each listed commit its purpose. Omit the section when the history is already obvious.

## Match the format to the change

Use concise prose and short lists by default. Add diagrams, detailed flows, responsibility maps, or longer background only when they reduce the work needed to understand a complex or risky change. Keep detailed preparation history outside the main body unless it affects the candidate's provenance or review safety.

Do not overstate evidence. A focused test proves only the behavior it exercises. Name the candidate revision and environment for reported checks, and state any limit that changes confidence in the result.

## Check the finished body

Verify the title, claims, links, and test results against the final candidate. A reviewer should be able to identify the prior problem, the delivered result, the important code, and the available evidence without reconstructing the change from scratch.
