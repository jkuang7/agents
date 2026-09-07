# agents

Shared, agent-agnostic skills and deployment helpers for Codex, Claude Code,
and other compatible coding agents.

Canonical skill sources live in `skills/`. Run `bin/deploy` to symlink every
skill into the supported runtime homes:

- `~/.codex/skills`
- `~/.claude/skills`
- `~/.agents/skills`

Verify the links without changing them:

```sh
bin/deploy --check
```

The Matt Pocock skills in this repository originate from
[`mattpocock/skills`](https://github.com/mattpocock/skills).
