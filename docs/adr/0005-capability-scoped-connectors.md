# ADR-0005: Capability-Scoped Connectors

- **Status:** Accepted
- **Date:** 2026-08-01

## Context

Connectors, tools, APIs, browsers, terminals, databases, and cloud integrations expand the practical authority of an AI system. Treating a connector as a single unrestricted capability creates excessive privilege and increases the impact of prompt injection, credential compromise, routing errors, or agent misbehavior.

A connector may expose many distinct actions with different risk levels, data-access implications, reversibility, and approval requirements. Governance therefore requires controls at the capability level rather than only at the connector level.

## Decision

AegisLayer adopts a capability-scoped connector model.

A connector must not be exposed to an AI agent as an undifferentiated, unrestricted tool. Each connector interaction must be mediated through explicit capabilities that define, where applicable:

1. Allowed action or operation.
2. Target system, tenant, account, repository, resource, or data domain.
3. Parameter and schema constraints.
4. Read, write, modify, delete, execute, or administrative permission level.
5. Time-to-live and validity window.
6. Request, workflow, and approval binding.
7. Data-classification and privacy limits.
8. Rate, cost, concurrency, and resource limits.
9. Required evidence, telemetry, and output handling.
10. Revocation and cancellation conditions.

Capability issuance must occur only after identity, authority, policy, approval, compatibility, health, readiness, and routing checks have succeeded.

## Connector Control Requirements

The conceptual connector control plane should support:

- Connector registration and ownership metadata.
- Capability discovery and normalization.
- Compatibility and structural validation.
- Health and readiness evaluation.
- Deterministic routing and selection.
- Scoped credential brokerage.
- Input and parameter validation.
- Runtime isolation and resource constraints.
- Output validation, redaction, and classification.
- Evidence, audit, telemetry, and revocation.

## Rationale

Capability-level scoping:

- Enforces least privilege.
- Reduces blast radius.
- Makes approval decisions more precise.
- Supports safer connector reuse across workflows.
- Improves evidence and audit specificity.
- Enables rapid revocation without disabling unrelated functions.
- Reduces reliance on broad long-lived credentials.

## Considered Alternatives

### Unrestricted Connector Access

Grant access to the connector as a whole.

**Rejected because:** it conflates many operations and exposes excessive privilege.

### Role-Based Connector Access Only

Permit connector use based on a broad user or service role.

**Rejected as insufficient because:** roles alone may not constrain the target, action, parameters, validity period, workflow, or data scope.

### Capability-Scoped Access

Issue narrow, contextual, short-lived permissions for specific connector operations.

**Accepted because:** it offers the strongest alignment with least privilege, policy-before-execution, and fail-closed governance.

## Consequences

### Benefits

- Smaller authorization surface.
- More precise approvals.
- Reduced credential and connector abuse risk.
- Better revocation and containment.
- Clearer connector evidence and diagnostics.
- Improved support for multi-tenant and sensitive environments.

### Trade-offs

- Additional metadata, policy, and runtime complexity.
- Capability discovery and normalization must remain accurate.
- More authorization decisions and evidence records are generated.
- Legacy connectors may require adapters or reduced functionality.

### Residual Risks

- A capability definition may still be overly broad.
- Connector implementations may perform hidden or undocumented side effects.
- Third-party APIs may change behavior without notice.
- Scoped credentials may still be stolen or replayed before expiry.
- Incorrect routing may select a valid but unintended connector.

## Acceptance Criteria

- Connectors expose normalized capability descriptors.
- Authorization is evaluated for the specific capability and target.
- Credentials are scoped and short-lived where supported.
- Connector health and readiness are checked before use.
- Parameters are validated before invocation.
- Outputs are validated before being returned or propagated.
- Capability issuance and use are recorded with correlation metadata.
- Revocation can stop or prevent further execution.
- No fallback silently broadens connector authority.

## Operational Guidance

Implementations should:

- Maintain an approved connector registry.
- Reject unknown, incompatible, unhealthy, or unready connectors.
- Distinguish discovery, authorization, routing, credentialing, and execution.
- Bind capabilities to a request or workflow context.
- Test denial, revocation, expiry, and connector-failure scenarios.
- Treat third-party connector output as untrusted input.

## Public Release Review

This ADR describes public architectural principles only. It excludes connector credentials, internal routing rules, production integrations, customer systems, proprietary adapters, and security-sensitive deployment details.
