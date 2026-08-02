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

Related: ADR-0001, ADR-0002, ADR-0003, ADR-0004.

## Pattern 2: High-Impact Action
- Classify impact.
- Require accountable human approval.
- Bind approval to scope and validity.
- Monitor execution.
- Preserve evidence.

Related: ADR-0007.

## Pattern 3: Connector Invocation
- Discover capability.
- Verify compatibility and health.
- Authorize the specific capability.
- Validate parameters.
- Execute with least privilege.
- Validate outputs.

Related: ADR-0005.

## Pattern 4: Continuous Trust
- Observe identity, approvals, connectors, runtime, and evidence.
- Detect material context changes.
- Re-evaluate trust.
- Revoke or constrain execution when required.

Related: ADR-0006.

## Pattern 5: Incident Response
- Detect anomaly.
- Preserve evidence.
- Contain execution.
- Escalate to authorized reviewers.
- Record outcome and lessons learned.

Related: ADR-0003, ADR-0004, ADR-0006.

## Pattern Usage

These patterns are conceptual building blocks intended to promote consistent documentation, diagrams, and governance decisions across the repository. They are not implementation specifications and intentionally omit production-sensitive details.
