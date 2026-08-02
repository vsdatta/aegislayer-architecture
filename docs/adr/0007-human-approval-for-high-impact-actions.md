# ADR-0007: Human Approval for High-Impact Actions

- **Status:** Accepted
- **Date:** 2026-08-01

## Context

Some AI-initiated actions can create significant financial, legal, operational, security, privacy, safety, or reputational consequences. Even when identity, policy, and technical authorization checks succeed, fully autonomous execution may not be appropriate for actions that are irreversible, unusually sensitive, exceptional, or difficult to remediate.

Human judgment remains necessary where context, accountability, exception handling, or competing obligations cannot be reduced safely to automated rules alone.

## Decision

AegisLayer requires explicit human approval for high-impact actions when defined risk, policy, sensitivity, or governance thresholds are met.

Approval must be obtained before capability issuance or execution and must be bound to the specific:

1. Request and requester.
2. Proposed action.
3. Target system or resource.
4. Scope and permitted parameters.
5. Data classification and sensitivity.
6. Expected impact and reversibility.
7. Validity period and expiration.
8. Conditions, constraints, and compensating controls.
9. Approval identity and authority.
10. Correlation and evidence records.

Approval is not a general permission. It must not be reused outside the request, target, scope, or time period for which it was granted.

## High-Impact Triggers

Human approval should be required when one or more of the following apply:

- The action is irreversible or difficult to reverse.
- The action may create material financial, contractual, legal, or regulatory impact.
- Sensitive, personal, regulated, or confidential data is involved.
- Administrative, destructive, or security-critical privileges are required.
- The request exceeds predefined operational or risk thresholds.
- A policy exception is requested.
- The action affects multiple systems, users, tenants, or business units.
- The action may cause external communication, publication, payment, commitment, or public representation.
- The system detects ambiguity, conflicting instructions, abnormal behavior, or insufficient evidence.
- A prior approval has expired, been revoked, or no longer matches the current context.

## Approval Models

Depending on risk, the architecture may require:

- Single qualified approver.
- Multi-party approval.
- Separation-of-duties approval.
- Specialist review by security, legal, privacy, finance, safety, or domain experts.
- Executive or owner approval.
- Sequential approvals where each reviewer evaluates a distinct responsibility.

Approvers must have authority appropriate to the action being reviewed.

## Rationale

Human approval for high-impact actions:

- Preserves accountable decision-making.
- Adds contextual judgment where automated policy is insufficient.
- Reduces the likelihood of irreversible autonomous mistakes.
- Supports separation of duties.
- Strengthens exception governance.
- Produces attributable evidence for consequential decisions.
- Provides an escalation path for uncertainty and conflict.

## Considered Alternatives

### Fully Autonomous High-Impact Execution

Allow the system to execute whenever automated policy permits.

**Rejected because:** policy correctness does not eliminate contextual, ethical, legal, or operational uncertainty.

### Human Notification After Execution

Notify a person after the action has completed.

**Rejected as insufficient because:** notification cannot prevent an unauthorized or irreversible action.

### Risk-Based Human Approval

Require pre-execution human approval only when defined impact or governance thresholds are met.

**Accepted because:** it preserves automation for low-risk actions while maintaining accountable control for consequential actions.

## Approval Requirements

A valid approval record should include:

- Request identifier.
- Approver identity and role.
- Approved action and target.
- Scope, conditions, and limits.
- Decision rationale.
- Time of decision.
- Expiration and revocation status.
- Required follow-up or review.
- Integrity and correlation metadata.

Approval must be re-evaluated when the request, target, scope, policy, risk, or operating context materially changes.

## Consequences

### Benefits

- Reduced risk of harmful autonomous execution.
- Stronger accountability and attribution.
- Better handling of ambiguity and exceptions.
- Improved legal, security, and governance review.
- More precise authorization for sensitive actions.

### Trade-offs

- Increased latency.
- Additional operational burden on approvers.
- Potential bottlenecks or approval fatigue.
- Need for availability, delegation, escalation, and expiry processes.
- Human reviewers may still make incorrect or inconsistent decisions.

### Residual Risks

- Approvers may misunderstand the request or evidence.
- Approval interfaces may omit important context.
- Collusion or compromised approver accounts may defeat separation of duties.
- Repeated routine approvals may become superficial.
- Emergency processes may be abused if not tightly controlled.

## Acceptance Criteria

- High-impact criteria are explicitly defined by policy.
- Required approvals occur before capability issuance and execution.
- Approval is bound to request, target, scope, and validity period.
- Expired, revoked, missing, or mismatched approvals fail closed.
- Material context changes trigger re-approval.
- Approval decisions and rationale are recorded as evidence.
- Separation of duties is applied where risk requires it.
- Emergency or exception approvals are limited, attributable, time-bound, and reviewable.

## Operational Guidance

Implementations should:

- Present approvers with clear intent, target, impact, evidence, and alternatives.
- Minimize approval fatigue through risk-based thresholds.
- Prevent self-approval where separation of duties is required.
- Support delegation without losing accountability.
- Record denials, expirations, revocations, and requests for more evidence.
- Test stale, mismatched, revoked, and replayed approval scenarios.
- Review approval quality and threshold effectiveness periodically.

## Public Release Review

This ADR contains public governance principles only. It excludes internal approval thresholds, customer-specific workflows, confidential operating procedures, credentials, and proprietary implementation details.
