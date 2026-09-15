---
name: diagnosing-bugs
description: Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.
---

# Diagnosing bugs

Diagnose hard bugs and performance regressions through a tight feedback loop. Skip phases only with an explicit justification. Read relevant domain vocabulary and ADRs before exploring.

Redact secrets in displayed commands, output, and captured artifacts. Keep credentials in environment variables and quote only diagnostic signal. If redaction removes necessary evidence, explain the gap and ask for a usable source.

## 1. Establish a tight red loop

Spend disproportionate effort on a discriminating reproduction before theorizing. Prefer an existing failing test, then a script, browser driver, captured-trace replay, isolated harness, property loop, bisection, or differential comparison. Choose the cheapest seam that reaches the actual bug.

A tight loop is fast, deterministic, specific to the user's symptom, and agent-runnable. For flaky bugs, raise and stabilize the reproduction rate enough to distinguish hypotheses. For a human-only trigger, use [hitl-loop.template.sh](scripts/hitl-loop.template.sh) to structure actions and capture observations.

Proceed only after running and showing one redacted invocation that reaches the real bug path and can distinguish the exact symptom from success. Optimize setup and signal so repeated checks take seconds rather than minutes. If a tight loop is infeasible, report attempts and the missing access, captured artifact, or authorized instrumentation; keep diagnosis incomplete instead of substituting an untested theory.

## 2. Reproduce and minimize

Confirm the user's exact failure over repeated runs or a sufficiently high reproduction rate. Capture its observable symptom for final verification.

Remove inputs, callers, configuration, and steps one at a time, rerunning after each reduction. Keep the smallest scenario that stays red; remaining elements must be necessary for reproduction. Reproduce and minimize before testing causes.

## 3. Rank hypotheses

Generate 3 to 5 ranked, falsifiable hypotheses before testing. Each predicts how a specific change would remove or worsen the failure. Show the ranking so the user can contribute domain evidence, then proceed without blocking on their response.

## 4. Probe predictions

Map each probe to one hypothesis and change one variable at a time. Prefer debugger or REPL inspection, then targeted boundary logs. Tag every temporary log with a unique prefix for complete cleanup.

For performance regressions, establish a baseline measurement and use profiling or bisection to discriminate causes. Measure before fixing.

## 5. Fix with regression evidence

Turn the minimized repro into a failing regression test before fixing, but only at a seam that exercises the real call-site pattern. A shallow test that misses necessary callers or transitions gives false confidence. If no correct seam exists, report the architectural testing limitation.

Observe the test fail, apply the fix, observe it pass, and rerun the original unminimized scenario. Keep prototype demonstrations lightweight; production adoption still requires appropriate verification.

## 6. Finish

Completion requires the original repro to pass, regression evidence or a documented seam gap, and removal of tagged instrumentation and disposable artifacts. State the confirmed cause in the commit or PR and report remaining limits.
