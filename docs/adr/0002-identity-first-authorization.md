# ADR-0002: Identity-First Authorization

- **Status:** Accepted
- **Date:** 2026-08-01

## Summary

Every request must establish identity and delegated authority before policy evaluation, approval, capability issuance, or execution. Identity is treated as a prerequisite for authorization rather than an optional attribute.

## Decision

The architecture adopts an identity-first model where:

1. Identity is validated before authorization.
2. Authority is evaluated independently from AI-generated reasoning.
3. Authorization decisions are scoped to the specific request, target, and time window.
4. Least-privilege capabilities are issued only after successful validation.
5. Missing or unverifiable identity causes execution to fail closed or escalate.

## Rationale

This approach:

- Reduces unauthorized execution risk.
- Supports accountability and auditability.
- Simplifies policy evaluation.
- Enables consistent evidence generation.
- Aligns with the repository's governance and trust-boundary principles.

## Consequences

### Benefits

- Stronger attribution.
- Clear authorization boundaries.
- Better incident investigation.
- Reduced privilege escalation opportunities.

### Trade-offs

- Additional validation steps.
- Dependence on identity infrastructure.
- Increased architectural complexity.

## Acceptance Criteria

- Identity validation precedes authorization in architecture diagrams.
- Policy evaluation assumes validated identity.
- Capability issuance requires verified authority.
- Failure to establish identity results in denial or escalation.

## Public Release Review

This ADR intentionally excludes credentials, deployment details, confidential infrastructure, and proprietary implementation information.
