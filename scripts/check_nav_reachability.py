#!/usr/bin/env python3
"""Check that markdown docs are reachable from mkdocs nav entries."""

from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]
MKDOCS = REPO / "mkdocs.yml"
DOCS = REPO / "docs"


def main() -> int:
    nav_text = MKDOCS.read_text(encoding="utf-8")
    referenced = set(re.findall(r"([A-Za-z0-9_./-]+\.md)", nav_text))

    docs_files = {
        str(path.relative_to(DOCS))
        for path in DOCS.rglob("*.md")
        if "lifecycle" not in path.parts
    }

    missing = sorted(p for p in docs_files if p not in referenced)
    if missing:
        print("Docs not reachable from mkdocs nav:")
        for file in missing:
            print(f"- docs/{file}")
        return 1

    print("Nav reachability audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
