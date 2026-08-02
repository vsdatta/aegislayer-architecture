# ADR-0003: Evidence by Design

- **Status:** Accepted
- **Date:** 2026-08-01

## Context

Consequential AI actions must be reviewable after the fact. Logging added only after execution may be incomplete, inconsistent, mutable, or disconnected from the decision that authorized the action.

## Decision

Evidence generation is a first-class architectural requirement across the full request lifecycle.

The architecture must capture, where applicable:

1. Request identity, origin, and provenance.
2. Structured intent, target, and scope.
3. Policy inputs, risk context, and decision.
4. Approval identity, conditions, and validity.
5. Capability issuance and limits.
6. Connector selection and readiness results.
7. Execution events, outputs, errors, retries, and containment actions.
8. Correlation, causation, timestamp, sequence, and integrity metadata.
9. Final outcome and record-closure status.

Finalized evidence should be protected against unauthorized alteration and retained according to applicable requirements.

## Rationale

This approach supports:

- Accountability and non-repudiation.
- Incident reconstruction.
- Policy and approval verification.
- Security investigations.
- Continuous improvement.
- Independent review and audit.

## Consequences

### Benefits

- Stronger traceability.
- Better incident response.
- Consistent governance records.
- Greater confidence in post-execution review.

### Trade-offs

- Increased storage and processing requirements.
- More complex data-retention and access controls.
- Evidence systems become security-critical components.

### Residual Risks

- Evidence may be incomplete if upstream components fail before capture.
- Incorrect timestamps, identities, or correlations may reduce reliability.
- Authorized administrators may still misuse evidence systems without adequate separation of duties.

## Acceptance Criteria

- Evidence capture begins at request intake.
- Policy, approval, capability, and execution records are correlated.
- Finalized records include integrity metadata.
- Evidence access is restricted and reviewable.
- Missing mandatory evidence causes denial, escalation, or explicit incomplete status rather than silent success.

## Public Release Review

This ADR excludes confidential schemas, retention schedules, deployment details, credentials, and proprietary implementation information.
