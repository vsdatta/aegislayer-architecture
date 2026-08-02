# Requests for Comments

This directory contains public Requests for Comments (RFCs) for proposed changes to the AegisLayer reference architecture, governance model, documentation system, diagram library, and repository processes.

RFCs are proposals under review. They are not authoritative architecture decisions until they are accepted and, where appropriate, converted into or linked from an Architecture Decision Record (ADR).

## RFC Status Values

- **Draft** — Initial proposal under development.
- **Review** — Open for structured technical and governance review.
- **Accepted** — Approved for implementation or documentation alignment.
- **Rejected** — Considered but not adopted.
- **Withdrawn** — Removed by the author before a final decision.
- **Superseded** — Replaced by a later RFC.
- **Implemented** — Accepted work has been completed and verified.

## Current RFC Catalog

| RFC | Title | Status |
|---|---|---|
| [RFC-0000](0000-template.md) | RFC Template | Template |

## Purpose

Use an RFC when a proposed change is significant enough to require review before it becomes part of the accepted architecture or governance model.

Examples include:

- New architecture layers or trust boundaries.
- Changes to identity, authority, policy, approval, or execution models.
- New connector, capability, evidence, monitoring, or incident-response patterns.
- Material revisions to accepted ADRs.
- New public control mappings or reference patterns.
- Major documentation, automation, or publication changes.
- Changes that may affect security, privacy, legal, operational, or intellectual-property risk.

Minor corrections, spelling fixes, link repairs, and non-material editorial changes generally do not require an RFC.

## RFC Lifecycle

### 1. Draft

Create a new RFC from `0000-template.md` using the next available four-digit number.

The draft should contain enough detail for reviewers to understand:

- The problem.
- The proposed change.
- Security and governance implications.
- Alternatives considered.
- Validation and acceptance criteria.
- Public-release boundaries.

### 2. Initial Screening

Before broad review, maintainers should confirm that the RFC:

- Is within repository scope.
- Does not disclose prohibited confidential material.
- Identifies affected ADRs, diagrams, and documents.
- Contains a meaningful threat and governance analysis.
- Is sufficiently complete for review.

### 3. Review

Reviewers should evaluate:

- Alignment with accepted ADRs.
- Identity and authority implications.
- Least-privilege and fail-closed behavior.
- Human approval requirements.
- Evidence and auditability.
- Monitoring, revocation, and incident response.
- Privacy and data handling.
- Compatibility and migration impact.
- Technical clarity and operational feasibility.
- Public-release and intellectual-property suitability.

### 4. Revision

The author updates the RFC in response to review comments.

Material revisions should be recorded in the change-history table. Open questions should be resolved or explicitly accepted as residual uncertainty.

### 5. Decision

The RFC receives one of the defined status outcomes.

An accepted RFC should include:

- Decision date.
- Decision summary.
- Required follow-up work.
- Related or resulting ADR.
- Documentation and diagram changes.
- Validation obligations.

### 6. Implementation and Verification

Accepted work should be reflected, where applicable, in:

- Architecture documentation.
- Governance documentation.
- Threat models.
- ADRs.
- Mermaid diagrams.
- Automation workflows.
- Reference examples.
- Changelog entries.

The RFC may be marked **Implemented** only when required work has been completed and verified.

### 7. Supersession

Do not delete or silently rewrite decided RFCs to hide history.

When a proposal is replaced:

1. Create a new RFC.
2. Mark the previous RFC as **Superseded**.
3. Link the two records.
4. Explain the reason for replacement.
5. Update affected ADRs and documentation.

## Numbering Rules

- Use four-digit sequential numbering.
- Do not reuse RFC numbers.
- Keep file names concise and descriptive.
- Preserve decided RFCs for historical review.

## RFC and ADR Relationship

The normal governance path is:

```text
RFC Draft → Review → Decision → Accepted RFC → ADR or ADR Update → Documentation and Diagram Alignment → Verification
```

Not every RFC requires a new ADR. A new or revised ADR is appropriate when the RFC establishes or materially changes an authoritative architectural decision.

## Public-Release Boundaries

RFCs must not intentionally disclose:

- Credentials or secrets.
- Customer, personal, or regulated data.
- Confidential infrastructure.
- Security-sensitive deployment configurations.
- Proprietary production controls.
- Unapproved patent-sensitive implementation details.

Security vulnerabilities must be reported privately under the repository security policy rather than proposed through a public RFC.

## Change Control

Material changes to the RFC catalog should update this index and, where appropriate, `../../CHANGELOG.md` and the MkDocs navigation.

Copyright © VND TECH LLC.
