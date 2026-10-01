# Expected behavior

- Create a GitHub Epic issue whose body is the reviewed parent spec, plus a linked draft Epic spec PR whose body links the issue instead of copying the spec. Return both links without waiting for another approval. An empty commit on a `spec/` branch is enough for this review artifact.
- Treat the Epic issue as the only copy of the spec and the native parent; the PR is where the human approves it, distinct from Sandcastle's later implementation PR.
- After approval, hand the Epic issue to `to-tickets` for a proposed child sequence and its publication approval. Native subissues attach to the Epic issue, and the spec PR is closed unmerged after they are published.
- Do not start Sandcastle or publish child issues at the spec PR stage.
