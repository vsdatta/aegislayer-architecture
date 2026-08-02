# Architectural Control Mapping

This matrix maps architecture controls to ADRs, lifecycle pages, and diagrams.

| Control Principle | ADRs | Lifecycle Docs | Diagrams | Core Documentation |
| --- | --- | --- | --- | --- |
| Separation of AI reasoning and execution authority | ADR-0001 | Runtime State Model | Architecture Overview, End-to-End Request Lifecycle | ARCHITECTURE.md, GOVERNANCE.md |
| Identity-first authorization | ADR-0002 | Identity and Authority Lifecycle | Trust Boundaries, Identity Authority Lifecycle | ARCHITECTURE.md, THREAT_MODEL.md |
| Evidence by design | ADR-0003 | Evidence Lifecycle Deep Dive | Evidence Lifecycle | GOVERNANCE.md, THREAT_CONTROL_TRACEABILITY.md |
| Fail-closed execution | ADR-0004 | Runtime State Model, Incident Containment | Runtime Execution Sequence, Runtime State Model | THREAT_MODEL.md, SECURITY_DESIGN_PRINCIPLES.md |
| Capability-scoped connectors | ADR-0005 | Connector Lifecycle, Capability Lifecycle | Connector Trust Model, Connector Lifecycle | PATTERN_LIBRARY.md, REFERENCE_EXAMPLES.md |
| Continuous verification and monitoring | ADR-0006 | Continuous Verification Lifecycle | Runtime State Model, Incident Containment | THREAT_MODEL.md, ARCHITECTURE_CONFORMANCE_CRITERIA.md |
| Human approval for high-impact actions | ADR-0007 | Approval Lifecycle | Governance Approval Workflow, Approval Lifecycle | GOVERNANCE.md, REFERENCE_EXAMPLES.md |

## Related References

- [Threat-to-Control Traceability](THREAT_CONTROL_TRACEABILITY.md)
- [Diagram Catalog](DIAGRAMS.md)
- [Pattern Library](PATTERN_LIBRARY.md)
- [Reference Examples](REFERENCE_EXAMPLES.md)
