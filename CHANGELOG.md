# Changelog

All notable changes to this repository are documented in this file.

## [1.1.0-rc.1] - 2026-08-02

### Added

- Governance lifecycle enhancements:
  - Release metadata: `release/VERSION.json`
  - Release checklist: `docs/RELEASE_CHECKLIST.md`
  - CODEOWNERS and expanded PR/issue governance templates
- Expanded architecture lifecycle documentation:
  - Identity, policy, approval, connector, capability, evidence, runtime, monitoring, and incident lifecycles
  - Security assumptions, trust boundary deep dive, deployment reference architectures
  - Threat-to-control traceability and conformance criteria
  - Public/proprietary scope boundary pages
- New Mermaid sources:
  - identity-authority, policy-evaluation, approval, connector, runtime-state, incident containment, GitHub-to-HF publication flow
- Public conceptual reference SDK under `reference-sdk/`
- Static interactive demo under `interactive-demo/`
- Structured research program under `research/`
- Hugging Face alignment package under `huggingface/`
- Website integration package under `website-integration/`
- Community readiness assets:
  - `.github/ISSUE_SEEDS/`
  - `.github/labels.yml`
  - `.github/milestones.md`
- CI expansion with quality gates workflow for docs, links, MkDocs strict, Mermaid, SDK, demo, secret scanning, and artifacts

### Changed

- Updated root README and MkDocs navigation to include all new architecture and platform artifacts
- Updated core docs (guide, getting started, governance, mapping, patterns, examples, glossary, maturity model)
- Updated roadmap and contribution governance for RFC/ADR and release controls

### Security and Publication Notes

- Preserved fail-closed publication behavior for external sync workflows
- No secrets or proprietary runtime internals added

## [1.0.0] - 2026-08-02

### Added

- Production-quality public v1.0 documentation baseline
- Architecture, governance, threat model, diagrams, ADR/RFC framework
- Documentation quality automation and GitHub Pages deployment workflow

Copyright © VND TECH LLC.
