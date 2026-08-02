#!/usr/bin/env python3
"""Build and validate Hugging Face static publication directory."""

from pathlib import Path
import shutil
import sys

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "interactive-demo"
TARGET = REPO / "huggingface" / "hf_space"
REQUIRED = ["index.html", "assets/css/styles.css", "assets/js/app.js", "README.md"]


def main() -> int:
    if not SOURCE.exists():
        print("interactive-demo directory missing")
        return 1

    if TARGET.exists():
        shutil.rmtree(TARGET)
    shutil.copytree(SOURCE, TARGET)

    template = TARGET / "SPACE_README_TEMPLATE.md"
    if template.exists():
        template.unlink()

    readme = TARGET / "README.md"
    readme.write_text(
        """---
title: AegisLayer Interactive Demo
emoji: 🛡️
colorFrom: green
colorTo: yellow
sdk: static
pinned: false
license: apache-2.0
---

## AegisLayer Interactive Demo

Exported from canonical GitHub repository: [vsdatta/aegislayer-architecture](https://github.com/vsdatta/aegislayer-architecture)
""",
        encoding="utf-8",
    )

    missing = [name for name in REQUIRED if not (TARGET / name).exists()]
    if missing:
        print("HF export missing required files:")
        for name in missing:
            print(f"- {name}")
        return 1

    print("HF static package ready.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
