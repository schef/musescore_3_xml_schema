#!/usr/bin/env python3
import argparse
import glob
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


CALL_RE = re.compile(
    r"\bxml\.(?:tag|tagE|stag|ntag|netag)\s*\(([^;]*?)\);",
    re.DOTALL,
)
STRING_RE = re.compile(r'"([^"\\]*(?:\\.[^"\\]*)*)"')

READ_TAG_RES = [
    re.compile(r'\btag\s*==\s*"([^"]+)"'),
    re.compile(r'\btag\s*==\s*QString\("([^"]+)"\)'),
    re.compile(r'\be\.name\(\)\s*==\s*"([^"]+)"'),
    re.compile(r'\bname\(\)\s*==\s*"([^"]+)"'),
]

XML_TAG_RE = re.compile(r"<([A-Za-z_][\w.-]*)")


def _is_valid_name(name: str) -> bool:
    return re.match(r"^[A-Za-z_][\w.-]*$", name) is not None


def _extract_from_write_calls(text: str) -> set:
    names = set()
    for call in CALL_RE.findall(text):
        strings = STRING_RE.findall(call)
        if not strings:
            continue
        first = strings[0].encode("utf-8").decode("unicode_escape")
        token = first.strip().split()[0] if first.strip() else ""
        if not token or token.startswith("%"):
            continue
        if _is_valid_name(token):
            names.add(token)
    return names


def _extract_from_read_conditions(text: str) -> set:
    names = set()
    for rx in READ_TAG_RES:
        for name in rx.findall(text):
            if _is_valid_name(name):
                names.add(name)
    return names


def _extract_from_mscx(text: str) -> set:
    return {name for name in XML_TAG_RE.findall(text) if _is_valid_name(name)}


def collect_element_names(mscore_root: Path) -> set:
    names = set()
    for path in mscore_root.rglob("*.cpp"):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        names.update(_extract_from_write_calls(content))
        names.update(_extract_from_read_conditions(content))

    for path in mscore_root.rglob("*.h"):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        names.update(_extract_from_write_calls(content))
        names.update(_extract_from_read_conditions(content))

    for path in mscore_root.rglob("*.mscx"):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        names.update(_extract_from_mscx(content))

    return names


def collect_example_structure(example_paths: list[Path]) -> dict:
    structure = {}

    def ensure(tag: str) -> dict:
        if tag not in structure:
            structure[tag] = {"children": set(), "attrs": set(), "text": False}
        return structure[tag]

    def walk(elem: ET.Element) -> None:
        info = ensure(elem.tag)
        if elem.text and elem.text.strip():
            info["text"] = True
        if elem.attrib:
            info["attrs"].update(elem.attrib.keys())
        for child in list(elem):
            info["children"].add(child.tag)
            walk(child)

    paths: list[Path] = []
    for path in example_paths:
        if path.is_dir():
            paths.extend(path.rglob("*.mscx"))
        elif path.is_file() and path.suffix == ".mscx":
            paths.append(path)

    paths = sorted(set(paths))
    if not paths:
        raise SystemExit("No .mscx files found in examples")

    for path in paths:
        try:
            tree = ET.parse(path)
        except ET.ParseError as exc:
            print(f"Skipping invalid XML: {path} ({exc})", file=sys.stderr)
            continue
        root = tree.getroot()
        walk(root)

    return structure


def write_schema(output_path: Path, element_names: list, structure: dict) -> None:
    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append('<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">')
    lines.append("  <xs:annotation>")
    lines.append("    <xs:documentation>")
    lines.append("      MuseScore 3.6.2 MSCX schema (permissive).")
    lines.append("      Generated from MuseScore source tags and templates.")
    lines.append("    </xs:documentation>")
    lines.append("  </xs:annotation>")

    for name in element_names:
        lines.append(f'  <xs:element name="{name}" type="{name}Type"/>')

    for name in element_names:
        info = structure.get(name, {"children": set(), "attrs": set(), "text": False})
        children = sorted(info["children"])
        attrs = sorted(info["attrs"])
        mixed = "true"

        lines.append(f'  <xs:complexType name="{name}Type" mixed="{mixed}">')
        if children:
            lines.append("    <xs:sequence>")
            lines.append('      <xs:choice minOccurs="0" maxOccurs="unbounded">')
            for child in children:
                lines.append(f'        <xs:element ref="{child}"/>')
            lines.append("      </xs:choice>")
            lines.append("    </xs:sequence>")
        for attr in attrs:
            lines.append(f'    <xs:attribute name="{attr}" type="xs:string"/>')
        lines.append("  </xs:complexType>")

    lines.append("</xs:schema>")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a strict MSCX XSD from MuseScore source",
    )
    parser.add_argument(
        "--mscore-root",
        required=True,
        help="Path to MuseScore 3.6.2 source root",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output XSD path",
    )
    parser.add_argument(
        "--examples",
        required=True,
        action="append",
        help="Path or glob to MSCX examples (repeatable)",
    )
    args = parser.parse_args()

    mscore_root = Path(args.mscore_root).resolve()
    output_path = Path(args.output).resolve()

    if not mscore_root.exists():
        raise SystemExit(f"MuseScore root not found: {mscore_root}")

    example_paths: list[Path] = []
    for value in args.examples:
        matches = glob.glob(value, recursive=True)
        if not matches:
            example_paths.append(Path(value))
        else:
            example_paths.extend(Path(match) for match in matches)

    missing = [p for p in example_paths if not p.exists()]
    if missing:
        missing_list = ", ".join(str(p) for p in missing)
        raise SystemExit(f"Examples path(s) not found: {missing_list}")

    structure = collect_example_structure(example_paths)

    names = collect_element_names(mscore_root)
    if not names:
        raise SystemExit("No element names found; check input path")

    structure_names = set(structure.keys())
    for info in structure.values():
        structure_names.update(info["children"])

    element_names = sorted(names | structure_names)
    write_schema(output_path, element_names, structure)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
