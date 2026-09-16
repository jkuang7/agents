# Skill mechanics

## Invocation

Preserve an existing invocation policy unless the user requests a change. For new skills, retain the target runtime's default discovery policy unless the user requests explicit-only invocation; sensitivity alone does not establish that intent. Invocation policy controls discovery, not authorization to perform the skill's actions.

For model invocation, keep a model-facing description naming distinct trigger branches for autonomous discovery or use by another workflow; direct user invocation remains available.

When the user requests explicit-only invocation, set `disable-model-invocation: true` where supported and use a short human-facing description. Keep invocation metadata consistent with that intent; verify field support and loading behavior in the target runtime.

## Splitting and routing

Split an independently discoverable skill only when it has a distinct trigger used in prompts or is needed by another workflow.

Use a plain referenced file when consumers need to read it without implicitly invoking a user-only skill.

Use a user-invoked router to reduce entry points. Name skills and the outcomes they own. Route using existing decisions and authorization; leave detailed execution and stopping rules in each owner. A router must not add behavior or imply an invocation capability the runtime does not support.
