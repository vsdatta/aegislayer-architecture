# Architecture Decision Records

This directory contains the public Architecture Decision Records (ADRs) for the AegisLayer reference architecture.

ADRs explain why important architectural choices were made, which alternatives were considered, what consequences follow, and how future maintainers should determine whether a decision remains valid.

## ADR Status Values

- **Proposed** — Under review and not yet authoritative.
- **Accepted** — Approved and currently authoritative.
- **Superseded** — Replaced by a later ADR.
- **Deprecated** — Retained for history but no longer recommended.
- **Rejected** — Considered but not adopted.

## Current ADR Catalog

| ADR | Title | Status |
|---|---|---|
| [ADR-0000](0000-template.md) | ADR Template | Template |
| [ADR-0001](0001-separate-ai-reasoning-from-execution-authority.md) | Separate AI Reasoning from Execution Authority | Accepted |
| [ADR-0002](0002-identity-first-authorization.md) | Identity-First Authorization | Accepted |
| [ADR-0003](0003-evidence-by-design.md) | Evidence by Design | Accepted |
| [ADR-0004](0004-fail-closed-execution.md) | Fail-Closed Execution | Accepted |
| [ADR-0005](0005-capability-scoped-connectors.md) | Capability-Scoped Connectors | Accepted |
| [ADR-0006](0006-continuous-verification-and-monitoring.md) | Continuous Verification and Monitoring | Accepted |
| [ADR-0007](0007-human-approval-for-high-impact-actions.md) | Human Approval for High-Impact Actions | Accepted |

## Foundational Decision Set

The initial ADR set establishes the following architecture:

1. AI reasoning is separated from execution authority.
2. Identity and authority are validated before authorization.
3. Evidence is generated across the full request lifecycle.
4. Missing mandatory trust conditions fail closed.
5. Connector access is capability-scoped and least-privilege.
6. Trust conditions are monitored and re-evaluated continuously.
7. High-impact actions require accountable human approval.

These decisions are designed to reinforce one another. They should be interpreted as a connected governance model rather than isolated recommendations.

## Relationship to Public Documentation

The ADRs complement the following public documents:

- [`../VISION.md`](../VISION.md)
- [`../ARCHITECTURE.md`](../ARCHITECTURE.md)
- [`../THREAT_MODEL.md`](../THREAT_MODEL.md)
- [`../GOVERNANCE.md`](../GOVERNANCE.md)
- [`../DIAGRAMS.md`](../DIAGRAMS.md)
- [`../GLOSSARY.md`](../GLOSSARY.md)

## Decision Lifecycle

### 1. Proposal

Create a new ADR from `0000-template.md` using the next available number.

A proposal should define:

- The problem or decision context.
- Decision drivers and constraints.
- Alternatives considered.
- Security and governance implications.
- Consequences and residual risks.
- Validation and acceptance criteria.

### 2. Review

Review should consider:

- Alignment with existing accepted ADRs.
- Threat-model impact.
- Least-privilege and fail-closed behavior.
- Evidence and audit requirements.
- Human accountability.
- Compatibility with public architecture and diagrams.
- Public-release and intellectual-property suitability.

### 3. Acceptance

An ADR becomes authoritative when its status is changed to **Accepted** by the designated decision owner or maintainer.

### 4. Implementation and Documentation Alignment

Accepted decisions should be reflected, where applicable, in:

- Architecture documentation.
- Governance documentation.
- Threat models.
- Mermaid diagrams.
- Reference examples.
- Tests or demonstrations.
- Changelog entries.

### 5. Supersession or Deprecation

An accepted ADR should not be rewritten to hide historical decisions.

When a material decision changes:

1. Create a new ADR.
2. Mark the old ADR as **Superseded** or **Deprecated**.
3. Link both records.
4. Explain the reason for the change.
5. Update affected documentation and diagrams.

## Numbering Rules

- Use four-digit sequential numbering.
- Do not reuse ADR numbers.
- Keep file names concise and descriptive.
- Preserve historical ADRs in the repository.

## Public-Release Boundaries

ADRs in this repository must not intentionally disclose:

- Credentials or secrets.
- Customer or personal data.
- Confidential infrastructure.
- Security-sensitive deployment configurations.
- Proprietary production controls.
- Unapproved patent-sensitive implementation details.

## Change Control

Material changes to the ADR catalog should update this index and, where appropriate, `../../CHANGELOG.md`.

Copyright © VND TECH LLC.
