#!/usr/bin/env python3
from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

import typer


app = typer.Typer(add_completion=False)


def indent(elem: ET.Element, level: int = 0) -> None:
    indent_str = "  "
    prefix = "\n" + indent_str * level
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = prefix + indent_str
        for child in elem:
            indent(child, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = prefix
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = prefix


def add_text(parent: ET.Element, tag: str, text: str) -> ET.Element:
    elem = ET.SubElement(parent, tag)
    elem.text = text
    return elem


def parse_time_sig(value: str) -> tuple[int, int]:
    parts = value.split("/")
    if len(parts) != 2:
        raise typer.BadParameter("Time signature must be N/D")
    try:
        n = int(parts[0])
        d = int(parts[1])
    except ValueError as exc:
        raise typer.BadParameter("Time signature must be integers") from exc
    if n <= 0 or d <= 0:
        raise typer.BadParameter("Time signature values must be positive")
    return n, d


def build_score(
    title: str,
    composer: str,
    measures: int,
    time_sig: str,
    key_sig: int,
    division: int,
    program_version: str,
    program_revision: str,
) -> ET.Element:
    if measures < 1:
        raise typer.BadParameter("Measures must be >= 1")

    sig_n, sig_d = parse_time_sig(time_sig)

    root = ET.Element("museScore", {"version": "3.02"})
    add_text(root, "programVersion", program_version)
    add_text(root, "programRevision", program_revision)

    score = ET.SubElement(root, "Score")
    ET.SubElement(score, "LayerTag", {"id": "0", "tag": "default"})
    add_text(score, "currentLayer", "0")
    add_text(score, "Division", str(division))

    style = ET.SubElement(score, "Style")
    add_text(style, "enableVerticalSpread", "1")
    add_text(style, "useStandardNoteNames", "0")
    add_text(style, "Spatium", "1.75")

    add_text(score, "showInvisible", "1")
    add_text(score, "showUnprintable", "1")
    add_text(score, "showFrames", "1")
    add_text(score, "showMargins", "0")

    meta_title = ET.SubElement(score, "metaTag", {"name": "workTitle"})
    meta_title.text = title
    meta_composer = ET.SubElement(score, "metaTag", {"name": "composer"})
    meta_composer.text = composer

    part = ET.SubElement(score, "Part")
    staff = ET.SubElement(part, "Staff", {"id": "1"})
    staff_type = ET.SubElement(staff, "StaffType", {"group": "pitched"})
    add_text(staff_type, "name", "stdNormal")

    add_text(part, "trackName", "Piano")
    instrument = ET.SubElement(part, "Instrument", {"id": "piano"})
    add_text(instrument, "longName", "Piano")
    add_text(instrument, "shortName", "Pno.")
    add_text(instrument, "trackName", "Piano")
    add_text(instrument, "minPitchP", "21")
    add_text(instrument, "maxPitchP", "108")
    add_text(instrument, "minPitchA", "21")
    add_text(instrument, "maxPitchA", "108")
    add_text(instrument, "instrumentId", "keyboard.piano")
    clef = ET.SubElement(instrument, "clef", {"staff": "2"})
    clef.text = "F"
    channel = ET.SubElement(instrument, "Channel")
    ET.SubElement(channel, "program", {"value": "0"})
    add_text(channel, "synti", "Fluid")

    staff_score = ET.SubElement(score, "Staff", {"id": "1"})
    vbox = ET.SubElement(staff_score, "VBox")
    add_text(vbox, "height", "10")
    text_title = ET.SubElement(vbox, "Text")
    add_text(text_title, "style", "Title")
    add_text(text_title, "text", title)
    text_composer = ET.SubElement(vbox, "Text")
    add_text(text_composer, "style", "Composer")
    add_text(text_composer, "text", composer)

    for index in range(measures):
        measure = ET.SubElement(staff_score, "Measure")
        voice = ET.SubElement(measure, "voice")
        if index == 0:
            time_sig_elem = ET.SubElement(voice, "TimeSig")
            add_text(time_sig_elem, "sigN", str(sig_n))
            add_text(time_sig_elem, "sigD", str(sig_d))

            key_sig_elem = ET.SubElement(voice, "KeySig")
            add_text(key_sig_elem, "accidental", str(key_sig))

        rest = ET.SubElement(voice, "Rest")
        add_text(rest, "durationType", "measure")
        add_text(rest, "duration", f"{sig_n}/{sig_d}")

    return root


@app.command()
def create(
    output: Path = typer.Argument(..., help="Output .mscx file path"),
    title: str = typer.Option("Title", help="Score title"),
    composer: str = typer.Option("Composer", help="Composer name"),
    measures: int = typer.Option(4, help="Number of measures"),
    time_sig: str = typer.Option("4/4", help="Time signature N/D"),
    key_sig: int = typer.Option(0, help="Key signature accidentals"),
    division: int = typer.Option(480, help="Division value"),
    program_version: str = typer.Option("3.6.2", help="MuseScore program version"),
    program_revision: str = typer.Option("3224f34", help="MuseScore program revision"),
) -> None:
    root = build_score(
        title=title,
        composer=composer,
        measures=measures,
        time_sig=time_sig,
        key_sig=key_sig,
        division=division,
        program_version=program_version,
        program_revision=program_revision,
    )

    indent(root)
    tree = ET.ElementTree(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    tree.write(output, encoding="UTF-8", xml_declaration=True)
    typer.echo(str(output))


if __name__ == "__main__":
    app()
