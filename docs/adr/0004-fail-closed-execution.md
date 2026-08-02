# ADR-0004: Fail-Closed Execution

- **Status:** Accepted
- **Date:** 2026-08-01

## Context

Autonomous and agentic AI systems operate across uncertain environments. Identity data may be unavailable, policy services may fail, approvals may expire, connectors may become unhealthy, credentials may be revoked, and evidence systems may become unreachable.

When trust conditions cannot be established, allowing execution by default would create a path for unauthorized, unsafe, or unauditable actions.

## Decision

AegisLayer adopts fail-closed execution as a default architectural rule.

Execution must not proceed when any mandatory trust condition is missing, invalid, stale, inconsistent, or unverifiable.

Mandatory conditions may include:

1. Verified requester, service, workload, or agent identity.
2. Valid direct or delegated authority.
3. Successful policy and risk evaluation.
4. Required approval that is current, scoped, and unrevoked.
5. Connector compatibility, health, and readiness.
6. Valid capability and credential scope.
7. Runtime availability and safety controls.
8. Required evidence and telemetry paths.

When a mandatory condition fails, the permitted outcomes are:

- Deny the action.
- Stop or cancel execution.
- Revoke the capability.
- Isolate the affected component.
- Request additional evidence.
- Route for human or specialist review.
- Retry only when explicitly authorized and bounded.

Silent continuation, implicit fallback to broader authority, or execution without required evidence is prohibited.

## Rationale

Fail-closed behavior:

- Reduces the chance of unauthorized execution.
- Prevents control-plane outages from becoming permission grants.
- Supports least privilege.
- Improves incident containment.
- Produces clearer governance and audit outcomes.
- Limits the impact of stale approvals and compromised connectors.

## Considered Alternatives

### Fail Open

Continue execution when control services are unavailable.

**Rejected because:** availability would be prioritized over authority, policy, evidence, and safety.

### Best-Effort Governance

Apply available controls and proceed when some checks fail.

**Rejected because:** mandatory controls would become optional under pressure or partial failure.

### Risk-Tiered Fail-Closed Model

Permit explicitly pre-authorized low-risk operations while requiring strict fail-closed behavior for other actions.

**Accepted as a constrained refinement:** only where the authorization, limits, expiry, evidence requirements, and safe fallback were defined in advance. This is not equivalent to default fail-open behavior.

## Consequences

### Benefits

- Stronger prevention of unauthorized actions.
- Clear and deterministic failure behavior.
- Easier audit and incident reconstruction.
- Better containment of compromised dependencies.
- Reduced risk of privilege expansion during outages.

### Trade-offs

- Reduced availability when governance dependencies fail.
- More operational escalations and denied requests.
- Higher reliability requirements for identity, policy, evidence, and approval services.
- Additional complexity for bounded retries and safe recovery.

### Residual Risks

- Incorrectly configured mandatory checks may block legitimate actions.
- Operators may attempt unsafe manual workarounds during outages.
- A compromised control service may return a falsely valid result.
- Pre-authorized low-risk fallback paths may be overly broad if poorly designed.

## Acceptance Criteria

- Architecture diagrams show denial or escalation when trust conditions fail.
- Missing approval never defaults to approval.
- Connector unreadiness prevents invocation.
- Expired or revoked capabilities cannot be used.
- Missing required evidence cannot be reported as normal success.
- Retries are bounded, policy-controlled, and evidence-producing.
- No component silently broadens authority to preserve availability.

## Operational Guidance

Implementations should:

- Distinguish denial, dependency failure, incomplete evidence, and security incident states.
- Provide safe and attributable escalation paths.
- Preserve evidence for failed and denied requests.
- Prevent repeated automated retries from creating resource exhaustion.
- Test failure behavior through dependency-outage and policy-denial scenarios.

## Public Release Review

This ADR contains public architectural principles only. It excludes production thresholds, customer environments, internal deployment details, credentials, and proprietary control logic.
