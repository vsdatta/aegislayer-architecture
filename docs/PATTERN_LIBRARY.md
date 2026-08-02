# AegisLayer Governance Pattern Library

This document collects reusable conceptual patterns that appear throughout the AegisLayer public reference architecture.

## Pattern 1: Governed Request Flow

- Validate identity and authority.
- Evaluate policy and risk.
- Obtain required approvals.
- Issue scoped capability.
- Execute in a controlled runtime.
- Produce evidence and telemetry.
- Review outcomes.

Related: [ADR-0001](adr/0001-separate-ai-reasoning-from-execution-authority.md), [ADR-0002](adr/0002-identity-first-authorization.md), [ADR-0003](adr/0003-evidence-by-design.md), [ADR-0004](adr/0004-fail-closed-execution.md).

## Pattern 2: High-Impact Action

- Classify impact.
- Require accountable human approval.
- Bind approval to scope and validity.
- Monitor execution.
- Preserve evidence.

Related: [ADR-0007](adr/0007-human-approval-for-high-impact-actions.md).

## Pattern 3: Connector Invocation

- Discover capability.
- Verify compatibility and health.
- Authorize the specific capability.
- Validate parameters.
- Execute with least privilege.
- Validate outputs.

Related: [ADR-0005](adr/0005-capability-scoped-connectors.md).

## Pattern 4: Continuous Trust

- Observe identity, approvals, connectors, runtime, and evidence.
- Detect material context changes.
- Re-evaluate trust.
- Revoke or constrain execution when required.

Related: [ADR-0006](adr/0006-continuous-verification-and-monitoring.md).

## Pattern 5: Incident Response

- Detect anomaly.
- Preserve evidence.
- Contain execution.
- Escalate to authorized reviewers.
- Record outcome and lessons learned.

Related: [ADR-0003](adr/0003-evidence-by-design.md), [ADR-0004](adr/0004-fail-closed-execution.md), [ADR-0006](adr/0006-continuous-verification-and-monitoring.md).

## Pattern Selection Guide

| Scenario | Primary Pattern | Supporting Patterns |
| --- | --- | --- |
| Standard request execution | Governed Request Flow | Continuous Trust |
| Irreversible or high-risk action | High-Impact Action | Governed Request Flow, Incident Response |
| Third-party tool integration | Connector Invocation | Continuous Trust, Incident Response |
| Long-running workflow | Continuous Trust | Governed Request Flow, Incident Response |
| Security anomaly or violation | Incident Response | Continuous Trust |

## Pattern Usage

These patterns are conceptual building blocks intended to promote consistent documentation, diagrams, and governance decisions across the repository. They are not implementation specifications and intentionally omit production-sensitive details.

When updating a pattern, review and align:

- [Control Mapping](CONTROL_MAPPING.md)
- [Reference Examples](REFERENCE_EXAMPLES.md)
- [Diagram Catalog](DIAGRAMS.md)
- [ADR Index](adr/README.md)
