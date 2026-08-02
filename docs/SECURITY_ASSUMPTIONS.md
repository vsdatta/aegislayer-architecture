# Security Assumptions and Non-Assumptions

This page records explicit architecture assumptions to reduce ambiguity.

## Security Assumptions

- Identity assertions can be validated through trusted identity infrastructure.
- Authority context can be represented as scoped, time-bound claims.
- Policy decisions are evaluated before external execution attempts.
- High-impact actions can be gated by accountable human approval.
- Runtime trust conditions can be monitored continuously.
- Evidence can be generated with correlation identifiers and UTC timestamps.

## Explicit Non-Assumptions

- The architecture does not assume perfect model behavior.
- The architecture does not assume connectors are always healthy.
- The architecture does not assume policy inputs are always complete.
- The architecture does not assume approvals are evergreen.
- The architecture does not assume logs alone guarantee integrity.
- The architecture does not assume every threat can be prevented.

## Security Language Boundary

This reference architecture is intended to reduce risk and improve governance visibility. It does not claim universal prevention of unauthorized activity.

Related:

- [Threat Model](THREAT_MODEL.md)
- [Security Design Principles](SECURITY_DESIGN_PRINCIPLES.md)
- [Governance](GOVERNANCE.md)
