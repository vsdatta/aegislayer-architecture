# Architectural Control Mapping

This document cross-references the core governance principles of the AegisLayer reference architecture with documentation, Architecture Decision Records (ADRs), diagrams, and the RFC process.

| Control Principle | ADRs | Diagrams | Core Documentation |
| --- | --- | --- | --- |
| Separation of AI reasoning and execution authority | [ADR-0001](adr/0001-separate-ai-reasoning-from-execution-authority.md) | Architecture Overview, Governance Approval Workflow, End-to-End AI Request Lifecycle | [ARCHITECTURE.md](ARCHITECTURE.md), [GOVERNANCE.md](GOVERNANCE.md) |
| Identity-first authorization | [ADR-0002](adr/0002-identity-first-authorization.md) | Trust Boundaries, Zero Trust Reference Architecture | [ARCHITECTURE.md](ARCHITECTURE.md), [THREAT_MODEL.md](THREAT_MODEL.md) |
| Evidence by design | [ADR-0003](adr/0003-evidence-by-design.md) | Evidence Lifecycle, End-to-End AI Request Lifecycle | [GOVERNANCE.md](GOVERNANCE.md), [DIAGRAMS.md](DIAGRAMS.md) |
| Fail-closed execution | [ADR-0004](adr/0004-fail-closed-execution.md) | Runtime Execution Sequence, Zero Trust Reference Architecture | [THREAT_MODEL.md](THREAT_MODEL.md), [GOVERNANCE.md](GOVERNANCE.md) |
| Capability-scoped connectors | [ADR-0005](adr/0005-capability-scoped-connectors.md) | Connector Trust Model, Threat-to-Control Mapping | [ARCHITECTURE.md](ARCHITECTURE.md), [PATTERN_LIBRARY.md](PATTERN_LIBRARY.md) |
| Continuous verification and monitoring | [ADR-0006](adr/0006-continuous-verification-and-monitoring.md) | Zero Trust Reference Architecture, Runtime Execution Sequence | [THREAT_MODEL.md](THREAT_MODEL.md), [REFERENCE_EXAMPLES.md](REFERENCE_EXAMPLES.md) |
| Human approval for high-impact actions | [ADR-0007](adr/0007-human-approval-for-high-impact-actions.md) | Governance Approval Workflow, End-to-End AI Request Lifecycle | [GOVERNANCE.md](GOVERNANCE.md), [REFERENCE_EXAMPLES.md](REFERENCE_EXAMPLES.md) |

## Diagram Sources

The conceptual diagram sources are stored in `diagrams/`:

- `../diagrams/architecture-overview.mmd`
- `../diagrams/trust-boundaries.mmd`
- `../diagrams/runtime-execution-sequence.mmd`
- `../diagrams/evidence-lifecycle.mmd`
- `../diagrams/governance-approval-workflow.mmd`
- `../diagrams/threat-to-control-mapping.mmd`
- `../diagrams/connector-trust-model.mmd`
- `../diagrams/zero-trust-reference-architecture.mmd`
- `../diagrams/end-to-end-ai-request-lifecycle.mmd`

## Usage

When proposing a material architectural change:

1. Review the affected control principles.
2. Determine whether an RFC is required by [rfc/README.md](rfc/README.md).
3. Update or create ADRs if an architectural decision changes.
4. Revise affected diagrams.
5. Update the related documentation.
6. Verify cross-references remain consistent.

The goal of this matrix is to help reviewers identify where a proposed change has downstream documentation and governance impacts.

## Related References

- [Reference Architecture Guide](REFERENCE_ARCHITECTURE_GUIDE.md)
- [Pattern Library](PATTERN_LIBRARY.md)
- [Reference Examples](REFERENCE_EXAMPLES.md)
- [Architecture Review Checklist](ARCHITECTURE_REVIEW_CHECKLIST.md)
