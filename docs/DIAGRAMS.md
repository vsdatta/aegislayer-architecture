# Architecture Diagram Catalog

This catalog provides a guided index to the public AegisLayer Mermaid diagrams. Each diagram is conceptual and intentionally omits confidential controls, proprietary implementation details, customer environments, credentials, and unapproved patent-sensitive material.

## 1. Architecture Overview

**Source:** `../diagrams/architecture-overview.mmd`

Shows the primary control flow from users, systems, and AI agents through identity, policy, approval, controlled execution, evidence, monitoring, and external systems.

Use this diagram for:

- Executive and stakeholder orientation
- Architecture introductions
- High-level presentations
- Documentation landing pages

## 2. Trust Boundaries

**Source:** `../diagrams/trust-boundaries.mmd`

Separates the architecture into external, AI reasoning, governance, runtime, evidence, and protected-resource trust domains.

Use this diagram for:

- Security architecture review
- Threat-model workshops
- Data-flow analysis
- Boundary and interface discussions

## 3. Runtime Execution Sequence

**Source:** `../diagrams/runtime-execution-sequence.mmd`

Shows the sequence of identity validation, policy evaluation, approval, capability issuance, controlled execution, evidence generation, monitoring, and incident containment.

Use this diagram for:

- Runtime design reviews
- Request tracing
- Approval and denial scenarios
- Incident-response walkthroughs

## 4. Evidence Lifecycle

**Source:** `../diagrams/evidence-lifecycle.mmd`

Describes evidence capture from request origin through policy decisions, execution events, integrity linkage, protected storage, review, retention, and authorized disposal.

Use this diagram for:

- Audit design
- Evidence-chain planning
- Incident reconstruction
- Retention and integrity discussions

## 5. Governance Approval Workflow

**Source:** `../diagrams/governance-approval-workflow.mmd`

Illustrates authority validation, policy decisions, specialist review, approval binding, expiry, execution, and final governance-record closure.

Use this diagram for:

- Governance design
- Human-in-the-loop workflows
- Separation-of-duties review
- Exception and escalation planning

## 6. Threat-to-Control Mapping

**Source:** `../diagrams/threat-to-control-mapping.mmd`

Maps public threat categories to primary control families and intended security outcomes.

Use this diagram for:

- Threat-model review
- Control-gap analysis
- Security-program planning
- Educational presentations

## 7. Connector Trust Model

**Source:** `../diagrams/connector-trust-model.mmd`

Shows how connector registration, capability discovery, compatibility, health, routing, credentials, runtime validation, evidence, and revocation fit together.

Use this diagram for:

- Tool and API integration review
- Connector governance
- Credential-boundary analysis
- Third-party trust assessment

## 8. Zero Trust Reference Architecture

**Source:** `../diagrams/zero-trust-reference-architecture.mmd`

Applies continuous verification, least privilege, short-lived capabilities, assume-breach thinking, trust-boundary inspection, and re-evaluation to AI execution.

Use this diagram for:

- Zero Trust planning
- Security principles training
- Architecture comparisons
- Continuous authorization design

## 9. End-to-End AI Request Lifecycle

**Source:** `../diagrams/end-to-end-ai-request-lifecycle.mmd`

Provides the capstone lifecycle from request initiation through policy, approval, connector selection, runtime execution, evidence, incident handling, and continuous improvement.

Use this diagram for:

- Complete system walkthroughs
- Architecture reviews
- Public demonstrations
- Cross-functional planning

## Diagram Maintenance Rules

When adding or revising diagrams:

1. Keep conceptual architecture separate from implementation claims.
2. Preserve fail-closed, least-privilege, and evidence-by-design principles.
3. Avoid credentials, customer data, confidential infrastructure, and security-sensitive deployment details.
4. Validate Mermaid syntax before merging.
5. Update this catalog and `CHANGELOG.md` when the public diagram set changes materially.
6. Keep terminology aligned with `GLOSSARY.md`.

## Rendering

GitHub and the MkDocs site can render Mermaid diagrams when they are embedded in fenced `mermaid` blocks. The `.mmd` files remain the canonical editable sources for the diagram library.

Copyright © VND TECH LLC.
