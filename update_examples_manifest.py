#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


def main() -> int:
    base = Path(__file__).resolve().parent
    examples_root = base / "examples_features"
    if not examples_root.exists():
        raise SystemExit(f"Missing examples_features: {examples_root}")

    lines: list[str] = []
    lines.append("# Feature-focused examples")
    lines.append("")
    lines.append("This directory contains a curated set of small, feature-focused MSCX files.")
    lines.append("Each subfolder targets a specific MuseScore feature so you can track schema")
    lines.append("coverage and test behavior independently.")
    lines.append("")
    lines.append("## Contents")
    lines.append("")

    for subdir in sorted(p for p in examples_root.iterdir() if p.is_dir()):
        files = sorted(p.name for p in subdir.glob("*.mscx"))
        if not files:
            continue
        lines.append(f"- {subdir.name}")
        for name in files:
            lines.append(f"  - `{name}`")

    readme = examples_root / "README.md"
    readme.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
