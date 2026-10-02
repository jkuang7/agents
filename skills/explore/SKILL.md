---
name: explore
description: Collect a problem the user explains over several messages, then hand it to Opus to find the simplest root-cause fix. Use only when the user types /explore; not for searching or exploring code.
---

# Explore

## Listen

Until the user says go (or done, ship it, your turn), reply only "Got it." Don't read code, run tools or suggest fixes. Answer only questions asked directly, in one line.

## Hand off

On go, start the `advisor` agent with:

- every user message since /explore, word for word and in order; later messages override earlier ones
- the working directory, plus any paths, errors or links the user mentioned

Tell the advisor:

- Treat the user's ideas and proposed fixes as starting points, not requirements.
- Investigate until the root cause is clear.
- Choose the simplest fix by the priorities in `/Volumes/T9/Dev/AGENTS.md`: robustness, then efficiency, then low upkeep. Add machinery only when it prevents a real failure.
- Ask only when the direction is genuinely unclear.
- Reply with: problem, root cause, fix, why the user's ideas were kept or rejected, and open questions.
- Investigate only; change no files.

An Opus session decides itself instead. From Codex, run the advisor from the working directory with `claude -p --agent advisor --model opus --permission-mode bypassPermissions "<brief>"`.

## Report

Relay the answer in five lines or fewer, then stop. Don't implement until the user says so.
