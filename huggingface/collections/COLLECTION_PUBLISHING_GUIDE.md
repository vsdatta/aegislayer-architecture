# Collection Publishing Guide

## Purpose

This package prepares the copy and ordering required to create or update Hugging Face Collections for AegisLayer.

## What Can Be Automated

- generation of collection descriptions and ordered item manifests in this repository
- release packaging in `dist/huggingface/collections/`
- validation that collection items point to canonical public artifacts
- creation or update of the AegisLayer Core collection through `huggingface_hub`
- insertion of the expected Space and dataset items with stable ordering

## What Still Requires Owner Action

- pinning or reordering Collections in the Hugging Face UI if you want a different visual presentation
- deciding whether to create additional thematic Collections beyond AegisLayer Core

## Current Live Collection

- AegisLayer Core: <https://huggingface.co/collections/AEGISLAYER/aegislayer-core-6a6f5eafc1742c4f90327c9a>

## Publishing Steps

1. Run `Launch Hugging Face Promotion` to create or reconcile the collection automatically.
2. Review the collection URL recorded in `huggingface/PUBLICATION_STATUS.md`.
3. If desired, fine-tune pinning or visual order in the Hugging Face UI.
4. Record any owner-side adjustments back into the release notes or launch posts.
