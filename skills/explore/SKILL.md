---
name: explore
description: Collect a problem the user explains over several messages, then have Opus recommend the most efficient way to solve it. Use only when the user types /explore; not for searching or exploring code.
---

# Explore

## Listen

Until the user says go (or done, ship it, your turn), reply only "Got it." Don't read code, run tools or suggest fixes. Answer only questions asked directly, in one line.

## Hand off

On go, start the `advisor` agent with:

- every user message since /explore, word for word and in order; later messages override earlier ones
- the working directory, plus any paths, errors or links the user mentioned

Tell the advisor:

- Recommend the most efficient way to solve the problem: the least effort to build and maintain that fixes the root cause without losing robustness. Weigh options by the priorities in `/Volumes/T9/Dev/AGENTS.md`, and add machinery only when it prevents a real failure.
- Treat the user's ideas and proposed fixes as starting points, not requirements.
- Investigate only as far as the recommendation needs; change no files.
- Ask only when the direction is genuinely unclear.
- Reply with: the recommendation, why it beats the alternatives, which of the user's ideas were kept or rejected and why, and open questions.

An Opus session decides itself instead. From Codex, run the advisor from the working directory with `claude -p --agent advisor --model opus --permission-mode bypassPermissions "<brief>"`.

## Report

Relay the recommendation in five lines or fewer, leading with what to do, then stop. Don't implement until the user says so.
