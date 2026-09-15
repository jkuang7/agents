# Skill mechanics

Apply [writing-for-agents](SKILL.md) to a skill's body and description. Decide invocation intent before adding catalog load.

## Invocation

Use model invocation when the agent must discover the skill autonomously or another workflow needs that reach. Keep a model-facing description naming distinct trigger branches; direct user invocation remains available.

Use user invocation when the human intentionally chooses the skill. Set `disable-model-invocation: true` where supported and make the description a short human-facing summary. Keep runtime-specific invocation metadata consistent with that intent. Discover actual field support and loading behavior from the target runtime rather than assuming every deployed runtime handles catalog visibility identically.

## Splitting and routing

Split an independently discoverable skill only when it has a distinct trigger used in prompts or is needed by another workflow. Its catalog pointer must earn its ongoing load.

Shared reference should have one authoritative home. Use a plain referenced file when consumers need to read it without implicitly invoking a user-only skill.

A user-invoked router reduces the number of entry points the human must remember. Name skills and the outcomes they own. Route using existing decisions and authorization; leave detailed execution and stopping rules in each owner. A router must not add behavior or imply an invocation capability the runtime does not support.
