# Evidence-based skill maintenance

Start with the failed outcome and its evidence. Distinguish a misunderstood requirement, missing information, bad decision, broken helper, missing runtime control, and a report that overstates the result. Put the correction at the earliest owner that can prevent recurrence. A script failure belongs in the script; an authorization boundary belongs in its executor; a judgment rule belongs in the relevant skill. Preserve existing user intent and keep the change within the authorized scope.

Use the collection's existing evaluation location. For the shared skills under `/Volumes/T9/Dev/agents`, use [evals](/Volumes/T9/Dev/agents/evals/README.md). Retain a compact case for a consequential or recurring failure, including a serious first occurrence. Prefer an existing case when the cause is the same.

Keep evaluator inputs separate from the expected outcome and diagnosis. Supply a realistic request, the skill, and minimum raw artifacts in an isolated workspace. Judge behavior and delivered evidence rather than wording, headings, or whether the agent repeats the new instruction. Use deterministic tests for executable helpers and an independent agent pass for consequential judgment changes when available. Record any limit on independence or permitted execution.

Record the owning skill or helper, observed failure and consequence, retained case, changed control, skill revision or content digest, evaluation result and evidence, and a concrete review or retirement condition. Compare the prior behavior when a safe reproduction exists. Also record unnecessary questions, repeated work, or other overhead when the change could introduce them.

Review the control when its dependency changes, stronger enforcement replaces it, or evaluation shows it costs more than it prevents. Remove or narrow superseded instructions while retaining useful behavioral regression cases. An unchanged period with no reported failure is not by itself proof that the control is unnecessary.

Complete the correction when relevant cases pass on the changed artifacts and remaining limits are stated. Passing metadata validation alone does not establish good decisions. A failed or unrun case remains visible; do not relabel it as a pass or widen the user's task to make the evaluation easier.
