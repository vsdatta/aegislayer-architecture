# Collection Publishing Guide

## Purpose

This package prepares the copy and ordering required to create or update Hugging Face Collections for AegisLayer.

## What Can Be Automated

- generation of collection descriptions and ordered item manifests in this repository
- release packaging in `dist/huggingface/collections/`
- validation that collection items point to canonical public artifacts

## What Still Requires Owner Action

- creating a Collection in the Hugging Face UI if it does not already exist
- selecting the final owner account or organization context
- pinning or reordering items in the UI if API support is unavailable

## Publishing Steps

1. Open the relevant collection card in this directory.
2. Copy the title, description, and purpose text into the Hugging Face Collection editor.
3. Add the listed items in the documented order.
4. Verify canonical links and descriptions against the repository state.
5. Record the live Collection URL back into release notes or launch posts.
