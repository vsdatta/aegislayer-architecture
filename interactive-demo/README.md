# Interactive Demo

This directory contains a static, client-side demonstration for AegisLayer reference architecture concepts.

## Scope

- No backend required
- No external API dependency
- No secrets
- Deterministic simulation data only
- No analytics or tracking

## Included Demonstrations

1. Governed request simulator
2. Identity and authority validation flow
3. Policy decision and approval path
4. Capability scope and revocation behavior
5. Connector readiness outcomes
6. Runtime state transition view
7. Evidence-chain walkthrough
8. Continuous verification and revocation
9. Threat-to-control explorer
10. Incident containment walkthrough
11. Architecture diagram explorer

## Run Locally

Open `interactive-demo/index.html` in a browser, or host the directory with any static file server.

## GitHub Pages Strategy

Publish under `/demo/` so it does not overwrite the MkDocs root site.

Example destination:

- `https://vsdatta.github.io/aegislayer-architecture/demo/`

## Hugging Face Static Space

Use the export package under `huggingface/hf_space/` or copy this directory contents into an HF Static Space repository.

## Disclaimer

This demo is conceptual and educational. It does not represent proprietary runtime internals and does not claim guaranteed prevention of unauthorized activity.
