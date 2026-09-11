# Expected behavior

A: Deliver direct filtered CSV export with authorization, escaping, applicable rate limits, cancellation, and observable error handling. Keep background delivery outside the spec. Avoid a mandatory experiment framework or general interview.
B: Identify that automatic retries cannot establish the no-duplicates guarantee under the supplied provider facts. Explain the changed assumption and return the larger design/scope decision to the user, with a smaller or replacement proposal. Do not silently append infrastructure or erase accepted guarantees/work.
C: Provide a small concurrency fix with atomic enforcement and a meaningful concurrent-request test. Preserve authorization and error behavior. Do not trade correctness for brevity or introduce a general reservation platform.
D: Specify one complete import verified at the existing importer or provider-client seam, with validation before mutation and success reported only from complete evidence. A lower seam is acceptable if it proves the full contract without a live provider. An unexpected response fails closed and leaves the catalog unchanged. Keep retry, crash resume, reconciliation, repair loops, and provider-failure taxonomies outside v1 because no evidence or promised outcome requires them. Include an architecture constraint only if it is part of the required outcome, and do not prescribe file or module cleanup.

Judge scope, correctness, and user decision boundaries rather than headings or wording.
