# Architectural Control Mapping

This document cross-rereferences the core governance principles of the AegisLayer reference architecture with the documentation, Architecture Decision Records (ADRs), diagrams, and future RFC process.

| Control Principle | ADRs | Diagrams | Core Documentation |
|---|---|---|---|
| Separation of AI reasoning and execution authority | ADR-0001 | Architecture Overview, Governance Approval Workflow, End-to-End AI Request Lifecycle | ARCHITECTURE.md, GOVERNANCE.md |
| Identity-first authorization | ADR-0002 | Trust Boundaries, Zero Trust Reference Architecture | ARCHITECTURE.md, THREAT_MODEL.md |
| Evidence by design | ADR-0003 | Evidence Lifecycle, End-to-End AI Request Lifecycle | GOVERNANCE.md, DIAGRAMS.md |
| Fail-closed execution | ADR-0004 | Runtime Execution Sequence, Zero Trust Reference Architecture | THREAT_MODEL.md, GOVERNANCE.md |
| Capability-scoped connectors | ADR-0005 | Connector Trust Model, Threat-to-Control Mapping | ARCHITECTURE.md |
| Continuous verification and monitoring | ADR-0006 | Zero Trust Reference Architecture, Runtime Execution Sequence | THREAT_MODEL.md |
| Human approval for high-impact actions | ADR-0007 | Governance Approval Workflow, End-to-End AI Request Lifecycle | GOVERNANCE.md |

## Usage

When proposing a material architectural change:

1. Review the affected control principles.
2. Determine whether an RFC is required.
3. Update or create ADRs if an architectural decision changes.
4. Revise affected diagrams.
5. Update the related documentation.
6. Verify cross-references remain consistent.

The goal of this matrix is to help reviewers identify where a proposed change has downstream documentation and governance impacts.
