---
name: wayfinder
description: Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear.
disable-model-invocation: true
---

# Wayfinder

Plan a multi-session effort as a shared map of decision tickets. Resolve the route to a named destination, rather than slicing or delivering the build. Execution belongs in the map only when its Notes explicitly includes it.

Resolve the target repository and its inherited tracker policy before operations. Use its wayfinding conventions; fall back to local Markdown only when no policy is supplied. Missing per-repo setup is not a reason to ignore inherited configuration.

## Map and frontier

The map is one issue labelled `wayfinder:map`, with child decision tickets. It is an index: resolutions live in tickets, while the map retains named links and one-line gists. Refer to maps and tickets by linked titles in human communication.

Use these map sections:

- Destination: the spec, decision, or authorized change that ends this effort.
- Notes: domain, standing preferences, required skills, and any execution override.
- Decisions so far: one named link and gist per resolved decision.
- Not yet specified: in-scope questions not yet precise enough to ticket.
- Out of scope: consciously excluded work and its reason.

Open tickets are queried as children, not duplicated in the map body. Each ticket states one precise question sized to one session, carries `wayfinder:<type>`, and links generated assets.

The frontier contains open, unblocked, unclaimed children in map order. Use native blocking relationships for visual discoverability, falling back to body conventions only where unsupported. A ticket is unblocked only when every blocker is closed. Claim it for the driving developer before work so concurrent sessions skip it. Reconcile shared tracker edits rather than overwriting other sessions.

## Ticket types

- Research, AFK: establish a fact through `research`.
- Prototype, HITL: use `prototype` to produce concrete evidence for the human to judge.
- Grilling, HITL: use `grilling` and `domain-modeling` to resolve decisions. This is the default.
- Task, HITL or AFK: perform a prerequisite needed to make a decision. It earns its place by unblocking that decision, not delivering the destination. Record completed actions and resulting facts; give a precise checklist when only the human can act.

HITL resolutions require the human's actual judgment. Never simulate their side. Handle small factual lookups directly; delegate substantial independent research through its owning skill. Keep shared unresolved decisions sequential.

## Chart the map

1. Use grilling and domain-modeling to settle the destination and scope.
2. Explore decisions breadth-first to establish the visible frontier and fog. If the route is already clear and fits one session, omit the map and return the next decision to the user.
3. Create the map and precise child questions, then wire dependencies after identifiers exist. Keep unformulated questions in Not yet specified.
4. Resolve independent unblocked research when useful, reconciling returned evidence and linking findings. Isolate concurrent writes as needed.
5. Stop after charting; other HITL tickets remain for later sessions.

## Work through the map

1. Read the map's low-resolution view. Take the named ticket or first frontier ticket, and claim it before work.
2. Resolve it with the Notes' skills and relevant related tickets loaded on demand. Use grilling and domain-modeling when uncertain.
3. Post the resolution, close the ticket, and append its named pointer to Decisions so far.
4. Turn newly precise fog into tickets and wire dependencies, clearing the duplicated fog entry. Update invalidated tickets as decisions change.

Resolve at most one non-research ticket per session. The map is complete when no decision remains before the destination can be pursued.

## Scope changes

A precise but unanswered question is a ticket; a question that cannot yet be formulated is fog. Neither includes settled or excluded work.

When a ticket proves out of scope, close it with its reason and link it under Out of scope, not Decisions so far. Excluded work returns only through a redrawn destination and a fresh effort, not ordinary fog graduation.
