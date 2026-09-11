# Evidence for approach decisions

Research only questions that could change the candidates, ranking, confidence, or mitigation.

Prefer local source and reproducible behavior, then official documentation, source, release notes, and maintainer discussions. Use first-hand reports to understand outcomes under comparable conditions; use community summaries to find stronger evidence. A source's authority does not establish its relevance to this repository.

For each finding that materially affects the decision, retain the claim, source and date, affected version or environment, matching local condition, and implication. Distinguish documented behavior, reproduced defects, unverified reports, and your own inference. Link evidence to the candidate it affects; a formal grading system is unnecessary.

When evaluating a dependency or workaround:

- Verify that it covers this problem shape and the relevant versions and configuration.
- Check maintenance, compatibility, testing support, adoption cost, and operational burden. Investigate license or security constraints when relevant to adoption.
- Look for comparable successes and failures, including open and resolved issues, maintainer responses, and linked fixes.
- Distinguish current defects from historical issues fixed in another version. Confirm that the local usage triggers the reported problem.
- Deduplicate reports by root cause and assess whether workarounds move complexity to callers.

Apply the same evidence bar to native, library, and custom options. Popularity is a discovery signal; absence of reports is weak evidence of reliability. Keep ranking-changing contradictions visible until reconciled, and cite uncertainty when the evidence cannot settle them.
