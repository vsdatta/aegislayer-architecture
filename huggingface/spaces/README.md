# Hugging Face Space Portfolio

This directory contains the canonical source package for the AegisLayer Hugging Face Static Space portfolio.

## Structure

- `manifest.json`: portfolio metadata, discoverability settings, and per-Space content configuration.
- `shared/data/site.json`: canonical organization copy, public links, architecture layers, and trust-boundary descriptors.
- `<space-slug>/`: generated source Space packages with `README.md`, `index.html`, `assets/css/styles.css`, and `assets/js/app.js`.

## Spaces Included

- `organization-home`
- `architecture-explorer`
- `policy-playground`
- `evidence-chain-explorer`
- `threat-control-explorer`
- `connector-trust-simulator`
- `runtime-state-visualizer`
- `governance-library`

## Build Commands

- `python scripts/build_hf_portfolio.py`
- `python scripts/build_hf_space.py`

The full portfolio is exported into `dist/huggingface/<space-slug>/`.

The current `AEGISLAYER/README` Space is preserved through the legacy export path `huggingface/hf_space/`, which now mirrors the generated `organization-home` Space.
