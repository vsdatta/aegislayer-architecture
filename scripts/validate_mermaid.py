#!/usr/bin/env python3
"""Validate Mermaid source files for baseline structural integrity."""

from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]
MERMAID_PATTERN = re.compile(
    r"^(flowchart|graph|sequenceDiagram|stateDiagram|stateDiagram-v2|classDiagram|erDiagram|journey|gantt|pie|mindmap|timeline|quadrantChart|requirementDiagram|gitGraph|C4Context|C4Container|C4Component|C4Dynamic|C4Deployment)",
    re.MULTILINE,
)


def main() -> int:
    files = sorted((REPO / "diagrams").glob("*.mmd"))
    if not files:
        print("No Mermaid files found.")
        return 1

    failures: list[str] = []
    for file in files:
        text = file.read_text(encoding="utf-8").strip()
        if not text:
            failures.append(f"empty file: {file.relative_to(REPO)}")
            continue
        if not MERMAID_PATTERN.search(text):
            failures.append(f"missing declaration: {file.relative_to(REPO)}")

    if failures:
        print("Mermaid validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Mermaid validation passed for {len(files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
