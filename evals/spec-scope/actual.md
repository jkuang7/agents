# A. Export currently filtered orders to CSV

## Problem Statement

An operator needs to download the orders matching the current filters as CSV so they can try the export with their working data.

## Solution

Provide a direct CSV download from the filtered orders view. The operator can apply filters, export, and inspect the resulting file.

## Acceptance Requirements

- **A1:** Starting an export uses the filters active at that moment and exports all matching orders the operator is authorized to access, including results beyond the displayed page. Later filter changes do not change the in-flight request.
- **A2:** The download produces a valid CSV using the existing CSV escaping and export format conventions. An empty result produces a valid CSV with headers and no order rows.
- **A3:** The export preserves existing authorization and service rate limits. Denied and rate-limited requests retain the existing behavior.
- **A4:** The export uses existing streaming, cancellation, and error handling. Cancellation stops the export; failures follow the existing error behavior and are not presented as successful completed downloads.

## Implementation Decisions

Reuse the authorized filtered-query interface and existing CSV escaping and streaming export facilities. Connect the current filter state to the direct export request. Follow existing order-field and export-format conventions; do not introduce a separate query, permission, or rate-limit system.

## Testing Decisions

Verify through the existing orders/export public seam that combined filters, results spanning multiple pages, and authorization boundaries produce the expected rows. Inspect output for an empty result and fields containing commas, quotes, and line breaks. Exercise denied and rate-limited requests, cancellation, and stream failure through existing test facilities. Reuse existing helper coverage rather than duplicating CSV and streaming implementation tests. Manually apply a filter and download a CSV to confirm the operator can try the complete flow.

## Out of Scope

Background exports, emailed download links, scheduled exports, and a new export infrastructure.

# B. Reassess invoice delivery retries

The timeout discovery invalidates the current spec's assumption that a failed response means delivery failed. A successful delivery and a failed delivery can look identical to us. With no provider idempotency or delivery lookup, retrying an ambiguous attempt can duplicate an invoice. Routing, a durable scheduler, and failover do not resolve that uncertainty; failover can deliver a second copy through another provider.

I would pause the retry and failover work affected by this assumption and revise the whole spec before adding capabilities. Preserve existing implementation work and issue history. Identify child tickets covering failure classification, retry execution, delivery state, and duplicate-prevention tests, then reconcile their acceptance requirements with the chosen revision before resuming them.

The smallest proposed revision keeps delivery to the current provider and preserves the no-duplicate requirement:

- Retry only outcomes that establish that delivery did not occur.
- Record an ambiguous timeout as an unknown outcome and prevent automatic retry or failover for that attempt. Check that the client or transport is not silently retrying it either.
- Make the unknown outcome visible for operator investigation. Without evidence of non-delivery, investigation must not automatically authorize resending.
- Verify the case where the provider delivers successfully but the response times out: no second delivery attempt occurs, including after worker restart or concurrent processing. Also verify retry of a definitively undelivered attempt through the existing delivery seam.

This revision gives up automatic recovery for ambiguous outcomes. If automatic recovery is essential, the replacement approach needs a delivery mechanism that supports deduplication or authoritative reconciliation. The present provider cannot guarantee both eventual redelivery after an ambiguous failure and no duplicates.

The unresolved choice blocks the affected retry implementation: should the revised spec retain this provider and stop on ambiguous outcomes, or require a provider capability change so automatic recovery can meet the no-duplicate guarantee?

# C. Prevent concurrent reservations from overselling

## Problem Statement

Two requests can both reserve the last available item. A successful reservation must claim stock exactly once without allowing the available quantity to become negative.

## Solution

Make stock acquisition atomic using the existing database transaction and conditional-update facilities. When two requests compete for the last item, one succeeds and the other receives the existing insufficient-stock behavior.

## Acceptance Requirements

- **C1:** With one item available and two concurrent valid reservation requests for one item each, exactly one reservation succeeds, exactly one reservation is persisted, and the available quantity becomes zero.
- **C2:** A reservation acquires stock only when sufficient quantity is available at the atomic update. An unsuccessful stock acquisition creates no reservation and returns the existing insufficient-stock response.
- **C3:** Stock acquisition and reservation persistence commit together. A failure before commit leaves neither a stock decrement nor a partial reservation.
- **C4:** Existing authorization, request validation, error behavior, and successful reservation response remain unchanged. An unauthorized request does not change stock or create a reservation.

## Implementation Decisions

Within the existing transaction, conditionally decrement available stock only if it is sufficient for the requested quantity. Use the update result to determine whether stock was acquired; a prior read is not authority to reserve. Persist the reservation in the same transaction and roll back both changes on failure. Use existing response and error mapping conventions. No new lock service or reservation scheduler is required.

## Testing Decisions

Exercise the reservation service's existing public seam against the real database transaction behavior. Use two independent connections and a controlled interleaving to make valid requests compete for the last item. Assert both responses and committed stock/reservation state. Also verify sufficient stock for both requests, already exhausted stock, unauthorized requests, and a forced reservation-write failure after stock acquisition to demonstrate rollback. Reuse existing validation and error-contract coverage to check preservation.

## Out of Scope

Reservation expiry, waiting lists, distributed locks, stock-system redesign, and changes to authorization or public error contracts.
