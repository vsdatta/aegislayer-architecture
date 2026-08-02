# Architecture Review Checklist

Use this checklist for material architecture, governance, publication, SDK, or demo changes.

## Governance

- [ ] RFC opened for material architecture changes
- [ ] ADR updates applied for accepted architecture changes
- [ ] ADR/RFC status updates synchronized
- [ ] Release governance impacts assessed

## Security and Trust

- [ ] Identity and authority implications reviewed
- [ ] Policy-before-execution implications reviewed
- [ ] Least-privilege and capability-scope principles preserved
- [ ] Fail-closed behavior preserved
- [ ] Continuous verification and revocation impact reviewed
- [ ] Incident containment implications reviewed

## Documentation Synchronization

- [ ] Diagrams updated where affected
- [ ] Threat model and control mapping aligned
- [ ] Pattern library and reference examples aligned
- [ ] Glossary updated for new terms
- [ ] MkDocs navigation updated for new pages

## Release and Publication

- [ ] Changelog/release notes updated where needed
- [ ] Public claims are bounded and accurate
- [ ] No sensitive or proprietary disclosures
- [ ] Hugging Face/GitHub Pages implications reviewed

## Validation

- [ ] Markdown lint
- [ ] Link checks
- [ ] MkDocs strict build
- [ ] Mermaid validation
- [ ] SDK lint/type/test (if impacted)
- [ ] Demo validation (if impacted)
- [ ] Secret-pattern scan
