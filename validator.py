#!/usr/bin/env python3
import argparse
from pathlib import Path
from typing import Any


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate MSCX against an XSD schema",
    )
    parser.add_argument("--xsd", required=True, help="Path to XSD schema")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--xml", help="Path to MSCX XML file")
    group.add_argument("--dir", help="Directory of MSCX files")
    args = parser.parse_args()

    xsd_path = Path(args.xsd)
    if not xsd_path.exists():
        raise SystemExit(f"XSD not found: {xsd_path}")

    etree: Any = None
    try:
        from lxml import etree as _etree  # type: ignore[import-not-found]

        etree = _etree
    except ImportError as exc:
        raise SystemExit("Missing dependency: lxml. Install with: pip install lxml") from exc

    schema_doc = etree.parse(str(xsd_path))
    schema = etree.XMLSchema(schema_doc)

    if args.xml:
        xml_path = Path(args.xml)
        if not xml_path.exists():
            raise SystemExit(f"XML not found: {xml_path}")
        return validate_file(schema, etree, xml_path)

    xml_dir = Path(args.dir)
    if not xml_dir.exists():
        raise SystemExit(f"Directory not found: {xml_dir}")

    failures = 0
    for xml_path in sorted(xml_dir.glob("*.mscx")):
        failures += validate_file(schema, etree, xml_path)

    if failures:
        print(f"FAILED: {failures}")
        return 1
    print("OK")
    return 0


def validate_file(schema, etree, xml_path: Path) -> int:
    try:
        xml_doc = etree.parse(str(xml_path))
    except Exception as exc:
        print(f"FAILED: {xml_path} ({exc})")
        return 1

    if schema.validate(xml_doc):
        return 0

    error = schema.error_log.last_error
    if error is not None:
        print(f"FAILED: {xml_path} ({error.message} line {error.line})")
    else:
        print(f"FAILED: {xml_path} (Validation failed)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
