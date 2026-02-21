#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import xml.etree.ElementTree as ET


def collect_elements(path: Path) -> set[str]:
    elements: set[str] = set()
    try:
        tree = ET.parse(path)
    except ET.ParseError:
        return elements
    for elem in tree.iter():
        elements.add(elem.tag)
    return elements


def main() -> int:
    base = Path(__file__).resolve().parent
    root = base / "examples_features"
    if not root.exists():
        raise SystemExit(f"Missing examples_features: {root}")

    per_feature: dict[str, set[str]] = defaultdict(set)
    per_file: dict[str, set[str]] = {}

    for subdir in sorted(p for p in root.iterdir() if p.is_dir()):
        for file_path in sorted(subdir.glob("*.mscx")):
            elements = collect_elements(file_path)
            per_feature[subdir.name].update(elements)
            per_file[str(file_path.relative_to(root))] = elements

    lines: list[str] = []
    lines.append("# Feature coverage report")
    lines.append("")
    lines.append("Counts are distinct XML element names observed in each group.")
    lines.append("")
    lines.append("## Per feature")
    lines.append("")
    for feature in sorted(per_feature.keys()):
        elements = sorted(per_feature[feature])
        lines.append(f"- {feature}: {len(elements)}")
        lines.append("  elements:")
        for name in elements:
            lines.append(f"  - {name}")

    lines.append("")
    lines.append("## Per file")
    lines.append("")
    for rel_path in sorted(per_file.keys()):
        elements = sorted(per_file[rel_path])
        lines.append(f"- {rel_path}: {len(elements)}")
        lines.append("  elements:")
        for name in elements:
            lines.append(f"  - {name}")

    report_path = root / "COVERAGE.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
