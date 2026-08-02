#!/usr/bin/env python3
"""Build reproducible Hugging Face dataset packages into dist."""

from __future__ import annotations

from pathlib import Path
import shutil
import sys

from validate_hf_datasets import DATASET_SPECS, validate_datasets

REPO = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPO / "huggingface" / "datasets"
DIST_ROOT = REPO / "dist" / "huggingface" / "datasets"


def main() -> int:
    errors = validate_datasets()
    if errors:
        for error in errors:
            print(error)
        return 1

    if DIST_ROOT.exists():
        shutil.rmtree(DIST_ROOT)
    DIST_ROOT.mkdir(parents=True, exist_ok=True)

    shutil.copy2(SOURCE_ROOT / "README.md", DIST_ROOT / "README.md")
    for spec in DATASET_SPECS:
        shutil.copytree(SOURCE_ROOT / spec["slug"], DIST_ROOT / spec["slug"])

    print("Built Hugging Face datasets:")
    for spec in DATASET_SPECS:
        print(f"- {spec['slug']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())