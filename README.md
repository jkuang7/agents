# agents

Shared, agent-agnostic skills and deployment helpers for Codex, Claude Code,
and other compatible coding agents.

Locally authored skills live in `skills/`. Skills derived from
[`mattpocock/skills`](https://github.com/mattpocock/skills) live in
`vendor/matt-pocock-skills/`, including locally patched variants. Run
`bin/deploy` to symlink both collections into the supported runtime homes:

- `~/.codex/skills`
- `~/.claude/skills`
- `~/.agents/skills`

Verify the links without changing them:

```sh
bin/deploy --check
```

See the [vendor notes](vendor/matt-pocock-skills/README.md) before updating an
upstream-derived skill.
