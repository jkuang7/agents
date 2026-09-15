---
name: code-review
description: Review a PR, branch, or working-tree candidate against a fixed base for repository standards and accepted requirements.
---

Two-axis review of an explicit candidate against a fixed base:

- **Standards**: does the code conform to this repo's documented coding standards?
- **Spec**: does the code faithfully implement the originating issue / spec?

Both axes run as **parallel sub-agents** so they don't pollute each other's context, then this skill aggregates their findings.

If delegation is unavailable, perform both passes directly and disclose the reduced independence. Preserve the same candidate and evidence requirements; do not claim a separate reviewer ran.

Resolve the target repository and its instructions. Before reading issues, follow the tracker policy identified by applicable repository or inherited workspace instructions.

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

Read [SMELL-BASELINE.md](SMELL-BASELINE.md) for the Standards pass and supply its path or contents to that worker.

### 4. Spawn both sub-agents in parallel

**Standards sub-agent prompt** should include:

- The review packet, exact base and candidate identity, comparison mode, and commit list where applicable.
- The list of standards-source files you found in step 3, the baseline reference path or contents, with instructions to read and apply it.
- The brief: "Report, per file/hunk where relevant, (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline smell you spot: name it and quote the hunk. Distinguish hard violations from judgement calls: documented-standard breaches can be hard, but baseline smells are always judgement calls, and a documented repo standard overrides the baseline. Skip anything tooling enforces. Under 400 words."

**Spec sub-agent prompt** should include:

- The same review packet and candidate identity, plus verification commands, outcomes, and any continuation record relevant to this handoff.
- The path or fetched contents of the spec.
- The brief: "Report requirements that are missing, partial, or incorrectly implemented; unrequested behavior; and unresolved assumptions that change correctness. Assess whether verification actually discriminates the required outcome and applies to this candidate, including preserved regression coverage. For a work transfer, check that evidence and the next action are usable. Cite the governing requirement and concrete code or evidence for each finding. Distinguish an observed defect from missing evidence. Under 400 words."

If the spec is missing, skip the Spec sub-agent and note this in the final report.

### 5. Aggregate

Present the two reports under `## Standards` and `## Spec` headings, verbatim or lightly cleaned. Do **not** merge or rerank findings, because the two axes are deliberately separate.

End with a one-line summary: total findings per axis, and the worst issue _within each axis_ (if any). Don't pick a single winner across axes: that's the reranking the separation exists to prevent.

Include the reviewed candidate identity and material evidence limits. Return actionable findings to the implementation owner. The owner applies corrections, reruns affected checks, and requests review of changes that invalidate prior conclusions. A completed review report is not a claim that its findings have been fixed or that the candidate is ready to ship.
