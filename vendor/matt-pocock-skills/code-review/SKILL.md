---
name: code-review
description: "Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/spec asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to \"review since X\"."
---

Two-axis review of an explicit candidate against a fixed base:

- **Standards**: does the code conform to this repo's documented coding standards?
- **Spec**: does the code faithfully implement the originating issue / spec?

Both axes run as **parallel sub-agents** so they don't pollute each other's context, then this skill aggregates their findings.

If delegation is unavailable, perform both passes directly and disclose the reduced independence. Preserve the same candidate and evidence requirements; do not claim a separate reviewer ran.

Resolve the target repository and its instructions. Under `/Volumes/T9/Dev`, follow [the shared tracker convention](/Volumes/T9/Dev/docs/agents/issue-tracker.md) before reading issues. Elsewhere, use the project's tracker policy. Shared skill installation does not require per-repository setup.

## Process

### 1. Pin the base and candidate

Use the caller's base and candidate when supplied. Resolve refs to exact SHAs and record the comparison's merge base once. Otherwise infer the base from an existing PR, the task's recorded starting point, or established branch context. Ask only when the comparison remains ambiguous. Inspect staged, unstaged, and untracked status before choosing the candidate mode.

- For a committed candidate, use `git diff <merge-base-sha> <candidate-sha>` and the corresponding commit list. Disclose dirty work excluded from an explicitly committed review.
- For working-tree changes, use `git diff <merge-base-sha> -- <in-scope-paths>` for tracked final contents. Enumerate `git ls-files --others --exclude-standard -- <in-scope-paths>` and include the contents of relevant new files separately. Git diff alone omits untracked files. Account for pre-existing and excluded work from the task's starting state. Use the whole change only when it is all in scope.

Capture the selected patch, new-file contents, file identities, and verification references in a review packet outside the candidate. Record hashes for a working-tree snapshot and preserve its relevant code context. Give both reviewers the same packet. Pause writers during review or use an isolated snapshot; if the candidate changes, refresh affected evidence and review before issuing a verdict. Reviewers may inspect code and write reports, but may not edit, stage, or commit the candidate. Use runtime read-only permissions when available; instructions alone do not enforce them.

Proceed when the base resolves, the selected changes are accounted for, and the packet identifies exactly what will be reviewed. An empty tracked diff is not an empty candidate when relevant new files exist.

### 2. Identify the spec source

Look for the originating spec, in this order:

1. Requirements or a path supplied by the user or calling workflow, including accepted conversation requirements.
2. Issue references in the commit messages (`#123`, `Closes #45`, GitLab `!67`, etc.), fetched through the resolved tracker policy.
3. A spec file under `docs/`, `specs/`, or `.scratch/` matching the branch name or feature.
4. If nothing is found, ask the user where the spec is. If they say there isn't one, the **Spec** sub-agent will skip and report "no spec available".

### 3. Identify the standards sources

Anything in the repo that documents how code should be written, such as `CODING_STANDARDS.md` or `CONTRIBUTING.md`.

On top of whatever the repo documents, the Standards axis always carries the **smell baseline** below: a fixed set of Fowler code smells (_Refactoring_, ch.3) that applies even when a repo documents nothing. Two rules bind it:

- **The repo overrides.** A documented repo standard always wins; where it endorses something the baseline would flag, suppress the smell.
- **Always a judgement call.** Each smell is a labelled heuristic ("possible Feature Envy"), never a hard violation. Like any standard here, skip anything tooling already enforces.

Each smell reads *what it is* → *how to fix*; match it against the diff:

- **Mysterious Name**: a function, variable, or type whose name doesn't reveal what it does or holds. → rename it; if no honest name comes, the design's murky.
- **Duplicated Code**: the same logic shape appears in more than one hunk or file in the change. → extract the shared shape, call it from both.
- **Feature Envy**: a method that reaches into another object's data more than its own. → move the method onto the data it envies.
- **Data Clumps**: the same few fields or params keep travelling together (a type wanting to be born). → bundle them into one type, pass that.
- **Primitive Obsession**: a primitive or string standing in for a domain concept that deserves its own type. → give the concept its own small type.
- **Repeated Switches**: the same `switch`/`if`-cascade on the same type recurs across the change. → replace with polymorphism, or one map both sites share.
- **Shotgun Surgery**: one logical change forces scattered edits across many files in the diff. → gather what changes together into one module.
- **Divergent Change**: one file or module is edited for several unrelated reasons. → split so each module changes for one reason.
- **Speculative Generality**: abstraction, parameters, or hooks added for needs the spec doesn't have. → delete it; inline back until a real need shows.
- **Message Chains**: long `a.b().c().d()` navigation the caller shouldn't depend on. → hide the walk behind one method on the first object.
- **Middle Man**: a class or function that mostly just delegates onward. → cut it, call the real target direct.
- **Refused Bequest**: a subclass or implementer that ignores or overrides most of what it inherits. → drop the inheritance, use composition.

### 4. Spawn both sub-agents in parallel

**Standards sub-agent prompt** should include:

- The review packet, exact base and candidate identity, comparison mode, and commit list where applicable.
- The list of standards-source files you found in step 3, **plus the smell baseline from step 3** pasted in full (the sub-agent has no other access to it).
- The brief: "Report, per file/hunk where relevant, (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline smell you spot: name it and quote the hunk. Distinguish hard violations from judgement calls: documented-standard breaches can be hard, but baseline smells are always judgement calls, and a documented repo standard overrides the baseline. Skip anything tooling enforces. Under 400 words."

**Spec sub-agent prompt** should include:

- The same review packet and candidate identity, plus verification commands, outcomes, and any continuation record relevant to this handoff.
- The path or fetched contents of the spec.
- The brief: "Report requirements that are missing, partial, or incorrectly implemented; unrequested behavior; and unresolved assumptions that change correctness. Assess whether verification actually discriminates the required outcome and applies to this candidate, including preserved regression coverage. For a work transfer, check that evidence and the next action are usable. Cite the governing requirement and concrete code or evidence for each finding. Distinguish an observed defect from missing evidence. Under 400 words."

If the spec is missing, skip the Spec sub-agent and note this in the final report.

### 5. Aggregate

Present the two reports under `## Standards` and `## Spec` headings, verbatim or lightly cleaned. Do **not** merge or rerank findings, because the two axes are deliberately separate (see _Why two axes_).

End with a one-line summary: total findings per axis, and the worst issue _within each axis_ (if any). Don't pick a single winner across axes: that's the reranking the separation exists to prevent.

Include the reviewed candidate identity and material evidence limits. Return actionable findings to the implementation owner. The owner applies corrections, reruns affected checks, and requests review of changes that invalidate prior conclusions. A completed review report is not a claim that its findings have been fixed or that the candidate is ready to ship.

## Why two axes

A change can pass one axis and fail the other:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail.**
- Code that does exactly what the issue asked but breaks the project's conventions → **Spec pass, Standards fail.**

Reporting them separately stops one axis from masking the other.
