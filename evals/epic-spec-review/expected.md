# Expected behavior

- Create a GitHub Epic issue whose body is the reviewed parent spec, plus a linked draft Epic spec PR with the same spec in its body. Return both links without waiting for another approval. An empty commit on a `spec/` branch is enough for this review artifact.
- Treat the Epic issue as the native parent and the PR as its review surface, distinct from Sandcastle's later implementation PR.
- After human approval of the PR's spec, apply any approved edits to the Epic issue before handing it to `to-tickets` for a proposed child sequence and its publication approval. Native subissues attach to the Epic issue.
- Do not start Sandcastle or publish child issues at the spec PR stage.
