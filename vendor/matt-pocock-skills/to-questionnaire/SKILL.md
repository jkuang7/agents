---
name: to-questionnaire
description: Turn a decision you can't fully answer into a questionnaire for someone else to fill in.
disable-model-invocation: true
---

# To questionnaire

Create a Markdown discovery questionnaire for one person whose knowledge can resolve the user's gap, asynchronously or in a meeting.

Grill the send, not the subject. Establish the recipient's role, expertise, relationship, and the decisions or facts the user needs back. Reuse known context; ask only missing framing questions rather than asking the user to supply knowledge the recipient holds.

## Write

Order questions most important first and group by theme when helpful. Include:

- Purpose, sender, recipient, and how answers will be used.
- Enough context for someone outside the conversation.
- Known deadline and effort expectations, with partial answers and explicit uncertainty welcomed.
- One idea per question, an answer stub, and a short rationale only when it prevents misunderstanding or throwaway answers.
- A closing opportunity to supply missed information.

Write concrete questions aimed at the established gap. Keep context short and every question independently answerable. Save `to-questionnaire-<slug>.md` in the current directory and return its path. Complete when every requested decision or fact is covered. Creating the document does not authorize sending it.
