# Threat-to-Control Traceability

This page extends traceability from threat scenarios to architecture controls.

## Traceability Matrix

| Threat Theme | Primary Control Family | Evidence Requirement | Primary References |
| --- | --- | --- | --- |
| Unauthorized action execution | Identity + authority + policy-before-execution | identity and policy decision records | ADR-0002, ADR-0004 |
| Connector abuse | capability-scoped connectors + readiness gates | connector readiness and invocation evidence | ADR-0005 |
| Approval bypass | risk-based approval gates | approval request/decision records | ADR-0007 |
| Long-running trust drift | continuous verification + revocation | revocation and containment events | ADR-0006 |
| Audit ambiguity | evidence-by-design | correlation and causation linkage | ADR-0003 |

Related:

- [Control Mapping](CONTROL_MAPPING.md)
- [Threat Model](THREAT_MODEL.md)
- `diagrams/threat-to-control-mapping.mmd`
