#!/usr/bin/env python3
"""Validate synthetic Hugging Face dataset packages."""

from __future__ import annotations

import csv
import json
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / "huggingface" / "datasets"
DATASET_SPECS = [
    {
        "slug": "aegislayer-governance-scenarios",
        "csv": "data/governance_scenarios.csv",
        "jsonl": "data/governance_scenarios.jsonl",
    },
    {
        "slug": "threat-control-map",
        "csv": "data/threat_control_map.csv",
        "jsonl": "data/threat_control_map.jsonl",
    },
    {
        "slug": "architecture-catalog",
        "csv": "data/architecture_catalog.csv",
        "jsonl": "data/architecture_catalog.jsonl",
    },
]
PROHIBITED_PATTERNS = [r"@", r"AKIA[0-9A-Z]{16}", r"ghp_[A-Za-z0-9]{20,}"]


def load_schema_keys(dataset_dir: Path) -> list[str]:
    schema = json.loads((dataset_dir / "schema.json").read_text(encoding="utf-8"))
    return schema["required"]


def validate_dataset(spec: dict) -> list[str]:
    dataset_dir = ROOT / spec["slug"]
    errors: list[str] = []
    required_files = [
        dataset_dir / "README.md",
        dataset_dir / "schema.json",
        dataset_dir / "LIMITATIONS.md",
        dataset_dir / "LICENSE.md",
        dataset_dir / spec["csv"],
        dataset_dir / spec["jsonl"],
    ]
    for path in required_files:
        if not path.exists():
            errors.append(f"Missing dataset file: {path.relative_to(REPO)}")

    if errors:
        return errors

    keys = load_schema_keys(dataset_dir)
    csv_path = dataset_dir / spec["csv"]
    jsonl_path = dataset_dir / spec["jsonl"]
    with csv_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        csv_rows = list(reader)
        if reader.fieldnames != keys:
            errors.append(f"CSV headers do not match schema for {spec['slug']}")

    jsonl_rows = [json.loads(line) for line in jsonl_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(csv_rows) != len(jsonl_rows):
        errors.append(f"CSV and JSONL row count mismatch for {spec['slug']}")

    for index, row in enumerate(jsonl_rows):
        if list(row.keys()) != keys:
            errors.append(f"JSONL keys do not match schema order in {spec['slug']} row {index + 1}")
        if index < len(csv_rows):
            csv_row = csv_rows[index]
            if [csv_row[key] for key in keys] != [str(row[key]) for key in keys]:
                errors.append(f"CSV and JSONL value mismatch in {spec['slug']} row {index + 1}")

    first_key = keys[0]
    ids = [row[first_key] for row in jsonl_rows]
    if ids != sorted(ids):
        errors.append(f"Dataset IDs must remain sorted for deterministic content: {spec['slug']}")

    text_blob = "\n".join(
        [
            (dataset_dir / "README.md").read_text(encoding="utf-8"),
            csv_path.read_text(encoding="utf-8"),
            jsonl_path.read_text(encoding="utf-8"),
        ]
    )
    for pattern in PROHIBITED_PATTERNS:
        if re.search(pattern, text_blob, flags=re.IGNORECASE):
            errors.append(f"Prohibited pattern {pattern!r} found in {spec['slug']}")

    return errors


def validate_datasets() -> list[str]:
    errors: list[str] = []
    for spec in DATASET_SPECS:
        errors.extend(validate_dataset(spec))
    return errors


def main() -> int:
    errors = validate_datasets()
    if errors:
        print("Dataset validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Dataset validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())