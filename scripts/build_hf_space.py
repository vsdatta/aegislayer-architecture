#!/usr/bin/env python3
"""Build and validate the legacy Hugging Face publication directory."""

from pathlib import Path
import sys

from build_hf_portfolio import DIST_ROOT, LEGACY_EXPORT, main as build_portfolio_main

REPO = Path(__file__).resolve().parents[1]
TARGET = LEGACY_EXPORT
REQUIRED = ["index.html", "assets/css/styles.css", "assets/js/app.js", "README.md"]


def main() -> int:
    saved_argv = sys.argv[:]
    try:
        sys.argv = [saved_argv[0], "--space", "organization-home"]
        build_result = build_portfolio_main()
    finally:
        sys.argv = saved_argv

    if build_result != 0:
        return build_result

    missing = [name for name in REQUIRED if not (TARGET / name).exists()]
    if missing:
        print("HF export missing required files:")
        for name in missing:
            print(f"- {name}")
        return 1

    dist_target = DIST_ROOT / "organization-home"
    if not dist_target.exists():
        print("organization-home dist export missing")
        return 1

    print("HF static package ready.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
