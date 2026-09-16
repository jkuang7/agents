# Sandcastle controller handoff

Use `skills/sandcastle-run-epic/SKILL.md`, `skills/sandcastle-change-request/SKILL.md`, and their runtime references to respond to each independent scenario. This is an offline evaluation: state the action and completion boundary only. Do not launch a controller, access GitHub, or edit an authority. Treat the supplied runtime evidence as established.

A. The trusted Epic controller has passed preflight, its supported live state confirms ownership of Epic #42's registered delivery, and a worker has started. The user asked to run the Epic AFK. No readiness evidence exists yet.

B. Starting Epic #42 returned a PID and created a checkout lock, but the controller exited before supported state or current logs corroborated ownership.

C. Epic #42 already has a live owning controller. The user asks to watch its concise progress, then stops watching before the controller finishes. The runtime documents `--attach` as a read-only watcher.

D. The user explicitly asks for one child of Epic #42. The trusted CLI documents a positive run limit that caps accepted children. Ownership is confirmed immediately after launch, before any child is accepted.

E. An already-selected Epic child #45 was updated as the binding contract. Runtime state shows open unaccepted children in native order #44, #45. The trusted Epic controller supports only normal queue execution; it cannot directly target #45.

F. An already-selected focused PR is the standalone authority. The trusted runtime observes its GitHub identity plus one canonical content digest, its bootstrap identifies only that PR without copying the body/specification, it keeps mutable status outside the PR body, and it confirms controller ownership after launch.

G. Epic #42 has no live controller. Its durable state records one accepted child and the matching accepted delivery HEAD. The user asks to resume AFK, and current runtime validation finds the saved state consistent and executable.
