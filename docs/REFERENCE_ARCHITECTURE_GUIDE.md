# AegisLayer Reference Architecture Guide

## Overview

This guide serves as the central navigation document for understanding the public AegisLayer reference architecture.

## Audience and Use

Use this page as the canonical path through architecture, governance, threat-model, diagrams, decisions, and review artifacts.

This guide is optimized for:

- Security architects and platform architects
- AI engineering and governance teams
- Risk, compliance, and audit reviewers
- External contributors evaluating design intent

## Core Principles

1. Governance before execution
2. Identity-first authorization
3. Evidence by design
4. Fail-closed execution
5. Capability-scoped connectors
6. Continuous verification
7. Human approval for high-impact actions

## Documentation Map

| Topic | Primary Reference |
| --- | --- |
| Getting Started | [GETTING_STARTED.md](GETTING_STARTED.md) |
| Vision | [VISION.md](VISION.md) |
| Architecture | [ARCHITECTURE.md](ARCHITECTURE.md) |
| Threat Model | [THREAT_MODEL.md](THREAT_MODEL.md) |
| Governance | [GOVERNANCE.md](GOVERNANCE.md) |
| Security Design Principles | [SECURITY_DESIGN_PRINCIPLES.md](SECURITY_DESIGN_PRINCIPLES.md) |
| Diagrams | [DIAGRAMS.md](DIAGRAMS.md) |
| Control Mapping | [CONTROL_MAPPING.md](CONTROL_MAPPING.md) |
| Patterns | [PATTERN_LIBRARY.md](PATTERN_LIBRARY.md) |
| Examples | [REFERENCE_EXAMPLES.md](REFERENCE_EXAMPLES.md) |
| ADR Library | [adr/README.md](adr/README.md) |
| RFC Library | [rfc/README.md](rfc/README.md) |
| Architecture Review Checklist | [ARCHITECTURE_REVIEW_CHECKLIST.md](ARCHITECTURE_REVIEW_CHECKLIST.md) |
| Repository Maturity | [REPOSITORY_MATURITY_MODEL.md](REPOSITORY_MATURITY_MODEL.md) |

## Recommended Learning Path

- Understand the vision.
- Review the architecture and governance model.
- Study the threat model.
- Explore the diagrams.
- Read the ADRs.
- Review the security design principles and control mapping matrix.
- Review the pattern library and examples.
- Use the control mapping to understand relationships.
- Follow the RFC process for future architectural evolution.

## ADR and RFC Integration

- ADRs are authoritative architecture decisions once accepted.
- RFCs are structured proposals that may create or update ADRs when approved.
- Significant architectural changes should trace through: RFC -> ADR -> documents -> diagrams -> changelog.

Use:

- [ADR Index](adr/README.md)
- [RFC Index](rfc/README.md)
- [Architecture Review Checklist](ARCHITECTURE_REVIEW_CHECKLIST.md)

## Intended Audience

- Security architects
- AI researchers
- Software architects
- Governance professionals
- Engineering leaders
- Students and reviewers

## Scope

This repository is intended as a conceptual public reference architecture. It deliberately omits production-specific implementation details, confidential operational procedures, credentials, customer information, and other sensitive material.

## Validation References

For publication quality checks, use:

- [Diagram Catalog](DIAGRAMS.md)
- [Control Mapping](CONTROL_MAPPING.md)
- [Pattern Library](PATTERN_LIBRARY.md)
- [Reference Examples](REFERENCE_EXAMPLES.md)
