# Getting Started with the AegisLayer Architecture Repository

## Purpose

This repository is a public reference for conceptual AI governance and architecture. It is intended to explain architectural principles, not to provide production deployment instructions.

## Start Here

- Read the [Home page](index.md) for repository purpose and scope.
- Review the [Vision](VISION.md) to understand intent and boundaries.
- Continue into [Architecture](ARCHITECTURE.md), [Threat Model](THREAT_MODEL.md), and [Governance](GOVERNANCE.md).
- Use the [Reference Architecture Guide](REFERENCE_ARCHITECTURE_GUIDE.md) as your navigation hub.

## Suggested Reading Order

1. [README](https://github.com/vsdatta/aegislayer-architecture/blob/main/README.md)
2. [Vision](VISION.md)
3. [Architecture](ARCHITECTURE.md)
4. [Threat Model](THREAT_MODEL.md)
5. [Governance](GOVERNANCE.md)
6. [Security Design Principles](SECURITY_DESIGN_PRINCIPLES.md)
7. [Diagram Catalog](DIAGRAMS.md)
8. [Control Mapping](CONTROL_MAPPING.md)
9. [Pattern Library](PATTERN_LIBRARY.md)
10. [Reference Examples](REFERENCE_EXAMPLES.md)
11. [ADR Index](adr/README.md)
12. [RFC Index](rfc/README.md)

## Key Concepts

- Governance before execution
- Identity-first authorization
- Evidence by design
- Fail-closed behavior
- Capability-scoped connectors
- Continuous verification
- Human approval for high-impact actions

## Repository Structure

- `docs/` — public documentation set for MkDocs and GitHub Pages.
- `docs/adr/` — accepted and proposed architecture decisions.
- `docs/rfc/` — request-for-comments process and templates.
- `diagrams/` — Mermaid source files for conceptual architecture diagrams.
- `.github/` — documentation quality workflows and community templates.

## How to Contribute Safely

- Use [Contributing](https://github.com/vsdatta/aegislayer-architecture/blob/main/CONTRIBUTING.md) for contribution expectations.
- Use [Security Policy](https://github.com/vsdatta/aegislayer-architecture/blob/main/SECURITY.md) for private vulnerability reporting.
- Use [Architecture Review Checklist](ARCHITECTURE_REVIEW_CHECKLIST.md) before proposing major changes.
- Propose significant architectural changes through the [RFC process](rfc/README.md).

## What Good Changes Look Like

- Keep wording precise and avoid absolute security claims.
- Preserve the separation between AI capability and execution authority.
- Keep diagrams and narrative documentation aligned.
- Update [CHANGELOG](https://github.com/vsdatta/aegislayer-architecture/blob/main/CHANGELOG.md) and [ROADMAP](https://github.com/vsdatta/aegislayer-architecture/blob/main/ROADMAP.md) for material repository-level changes.

## Contributing

For significant architectural proposals, begin with an RFC. Accepted architectural changes should be reflected in ADRs, documentation, diagrams, and control mappings as appropriate.
