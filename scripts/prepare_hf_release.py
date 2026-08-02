#!/usr/bin/env python3
"""Prepare bundled Hugging Face release artifacts and publication summary."""

from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys

REPO = Path(__file__).resolve().parents[1]
DIST_ROOT = REPO / "dist" / "huggingface"
PACKAGE_ROOT = DIST_ROOT / "release-package"


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=REPO, check=True)


def copy_tree(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)


def main() -> int:
    run(["python", "scripts/build_hf_portfolio.py"])
    run(["python", "scripts/validate_hf_assets.py"])
    run(["python", "scripts/build_hf_datasets.py"])
    run(["python", "scripts/validate_hf_datasets.py"])

    PACKAGE_ROOT.mkdir(parents=True, exist_ok=True)
    for source, name in [
        (REPO / "huggingface", "huggingface"),
        (REPO / "promotion", "promotion"),
        (REPO / "assets" / "huggingface", "branding"),
        (REPO / "dist" / "huggingface" / "datasets", "datasets"),
    ]:
        copy_tree(source, PACKAGE_ROOT / name)

    manifest = json.loads((REPO / "huggingface" / "spaces" / "manifest.json").read_text(encoding="utf-8"))
    summary = {
        "source_commit": subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=REPO, check=True, text=True, capture_output=True
        ).stdout.strip(),
        "spaces": [space["slug"] for space in manifest["spaces"]],
        "datasets": [
            "aegislayer-governance-scenarios",
            "threat-control-map",
            "architecture-catalog",
        ],
        "collections_manifest": "huggingface/collections/collections.json",
        "promotion_assets": "promotion/",
    }
    (DIST_ROOT / "publication-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print("Prepared Hugging Face release artifacts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())