#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import zipfile

import typer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from musescore_schema.musescore_3_6_2 import (
    Accidental2,
    Channel1,
    Chord1,
    Clef2,
    CurrentLayer,
    Division1,
    Duration,
    DurationType1,
    EnableVerticalSpread,
    Extension,
    Height,
    Harmony1,
    Instrument1,
    InstrumentId,
    KeySig1,
    LayerTag,
    LongName,
    MaxPitchA,
    MaxPitchP,
    Measure1,
    MetaTag,
    MinPitchA,
    MinPitchP,
    MuseScore,
    Name,
    Part1,
    Pitch,
    Program2,
    ProgramRevision,
    ProgramVersion,
    Rest1,
    Root,
    Score1,
    ShowFrames,
    ShowInvisible,
    ShowMargins,
    ShowUnprintable,
    ShortName2,
    SigD,
    SigN1,
    Spatium1,
    Staff1,
    StaffType2,
    Style1,
    Style2,
    Synti,
    Text1,
    Text2,
    TimeSig1,
    TrackName2,
    Tpc,
    UseStandardNoteNames,
    Vbox,
    Voice,
    Lyrics,
    Note1,
)


app = typer.Typer(add_completion=False)


def content_text(value: str) -> list[object]:
    return [value]


def note(pitch: int, tpc: int) -> Note1:
    return Note1(content=[Pitch(content=content_text(str(pitch))), Tpc(content=content_text(str(tpc)))])


def lyric(text: str) -> Lyrics:
    return Lyrics(content=[Text2(content=content_text(text))])


def chord(duration: str, pitch: int, tpc: int, lyric_text: str | None = None) -> Chord1:
    content: list[object] = [DurationType1(content=content_text(duration))]
    if lyric_text:
        content.append(lyric(lyric_text))
    content.append(note(pitch, tpc))
    return Chord1(content=content)


def harmony(root_tpc: int, extension_value: str = "1") -> Harmony1:
    return Harmony1(
        content=[Root(content=content_text(str(root_tpc))), Extension(content=content_text(extension_value))]
    )


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
) -> MuseScore:
    if measures < 1:
        raise typer.BadParameter("Measures must be >= 1")

    sig_n, sig_d = parse_time_sig(time_sig)

    style = Style1(
        content=[
            EnableVerticalSpread(content=content_text("1")),
            UseStandardNoteNames(content=content_text("0")),
            Spatium1(content=content_text("1.75")),
        ]
    )

    part_staff = Staff1(
        id="1",
        content=[
            StaffType2(
                group="pitched",
                content=[Name(content=content_text("stdNormal"))],
            )
        ],
    )

    instrument = Instrument1(
        id="piano",
        content=[
            LongName(content=content_text("Piano")),
            ShortName2(content=content_text("Pno.")),
            TrackName2(content=content_text("Piano")),
            MinPitchP(content=content_text("21")),
            MaxPitchP(content=content_text("108")),
            MinPitchA(content=content_text("21")),
            MaxPitchA(content=content_text("108")),
            InstrumentId(content=content_text("keyboard.piano")),
            Clef2(staff="2", content=content_text("F")),
            Channel1(
                content=[
                    Program2(value="0"),
                    Synti(content=content_text("Fluid")),
                ]
            ),
        ],
    )

    part = Part1(
        content=[
            part_staff,
            TrackName2(content=content_text("Piano")),
            instrument,
        ]
    )

    vbox = Vbox(
        content=[
            Height(content=content_text("10")),
            Text1(
                content=[
                    Style2(content=content_text("Title")),
                    Text2(content=content_text(title)),
                ]
            ),
            Text1(
                content=[
                    Style2(content=content_text("Composer")),
                    Text2(content=content_text(composer)),
                ]
            ),
        ]
    )

    staff_measures: list[Measure1] = []
    for index in range(measures):
        voice_content: list[object] = []
        if index == 0:
            voice_content.append(
                TimeSig1(
                    content=[
                        SigN1(content=content_text(str(sig_n))),
                        SigD(content=content_text(str(sig_d))),
                    ]
                )
            )
            voice_content.append(KeySig1(content=[Accidental2(content=content_text(str(key_sig)))]))
        voice_content.append(
            Rest1(
                content=[
                    DurationType1(content=content_text("measure")),
                    Duration(content=content_text(f"{sig_n}/{sig_d}")),
                ]
            )
        )

        staff_measures.append(Measure1(content=[Voice(content=voice_content)]))

    score_staff = Staff1(
        id="1",
        content=[vbox, *staff_measures],
    )

    score = Score1(
        content=[
            LayerTag(id="0", tag="default"),
            CurrentLayer(content=content_text("0")),
            Division1(content=content_text(str(division))),
            style,
            ShowInvisible(content=content_text("1")),
            ShowUnprintable(content=content_text("1")),
            ShowFrames(content=content_text("1")),
            ShowMargins(content=content_text("0")),
            MetaTag(name="workTitle", content=content_text(title)),
            MetaTag(name="composer", content=content_text(composer)),
            part,
            score_staff,
        ]
    )

    root = MuseScore(
        version="3.02",
        content=[
            ProgramVersion(content=content_text(program_version)),
            ProgramRevision(content=content_text(program_revision)),
            score,
        ],
    )

    return root


def build_amazing_grace(
    title: str,
    composer: str,
    program_version: str,
    program_revision: str,
) -> MuseScore:
    division = 480
    sig_n, sig_d = 3, 4

    style = Style1(
        content=[
            EnableVerticalSpread(content=content_text("1")),
            UseStandardNoteNames(content=content_text("0")),
            Spatium1(content=content_text("1.75")),
        ]
    )

    part_staff = Staff1(
        id="1",
        content=[
            StaffType2(
                group="pitched",
                content=[Name(content=content_text("stdNormal"))],
            )
        ],
    )

    instrument = Instrument1(
        id="voice",
        content=[
            LongName(content=content_text("Voice")),
            ShortName2(content=content_text("Vo.")),
            TrackName2(content=content_text("Voice")),
            MinPitchP(content=content_text("36")),
            MaxPitchP(content=content_text("94")),
            MinPitchA(content=content_text("40")),
            MaxPitchA(content=content_text("79")),
            InstrumentId(content=content_text("voice.vocals")),
            Channel1(content=[Program2(value="52")]),
        ],
    )

    part = Part1(
        content=[
            part_staff,
            TrackName2(content=content_text("Voice")),
            instrument,
        ]
    )

    vbox = Vbox(
        content=[
            Height(content=content_text("10")),
            Text1(
                content=[
                    Style2(content=content_text("Title")),
                    Text2(content=content_text(title)),
                ]
            ),
            Text1(
                content=[
                    Style2(content=content_text("Composer")),
                    Text2(content=content_text(composer)),
                ]
            ),
        ]
    )

    tpc_map = {
        "C": 14,
        "D": 16,
        "E": 18,
        "F": 13,
        "G": 15,
        "A": 17,
        "B": 19,
    }

    melody = [
        ("C4", "A-"),
        ("E4", "maz-"),
        ("G4", "ing"),
        ("C5", "grace"),
        ("B4", "how"),
        ("A4", "sweet"),
        ("G4", "the"),
        ("E4", "sound"),
        ("C4", "that"),
        ("E4", "saved"),
        ("G4", "a"),
        ("A4", "wretch"),
        ("G4", "like"),
        ("E4", "me"),
        ("C4", ""),
        ("D4", ""),
        ("E4", ""),
        ("F4", ""),
        ("E4", ""),
        ("D4", ""),
        ("C4", ""),
        ("C4", ""),
        ("C4", ""),
        ("C4", ""),
    ]

    pitch_map = {
        "C4": 60,
        "D4": 62,
        "E4": 64,
        "F4": 65,
        "G4": 67,
        "A4": 69,
        "B4": 71,
        "C5": 72,
    }

    tpc_for = {
        "C4": tpc_map["C"],
        "D4": tpc_map["D"],
        "E4": tpc_map["E"],
        "F4": tpc_map["F"],
        "G4": tpc_map["G"],
        "A4": tpc_map["A"],
        "B4": tpc_map["B"],
        "C5": tpc_map["C"],
    }

    harmony_roots = [
        tpc_map["C"],
        tpc_map["C"],
        tpc_map["F"],
        tpc_map["C"],
        tpc_map["C"],
        tpc_map["G"],
        tpc_map["C"],
        tpc_map["C"],
    ]

    measures: list[Measure1] = []
    melody_index = 0
    for measure_index in range(8):
        voice_content: list[object] = []
        if measure_index == 0:
            voice_content.append(
                TimeSig1(
                    content=[
                        SigN1(content=content_text(str(sig_n))),
                        SigD(content=content_text(str(sig_d))),
                    ]
                )
            )
            voice_content.append(KeySig1(content=[Accidental2(content=content_text("0"))]))

        voice_content.append(harmony(harmony_roots[measure_index]))

        for _ in range(3):
            pitch_key, syllable = melody[melody_index]
            melody_index += 1
            voice_content.append(
                chord(
                    "quarter",
                    pitch_map[pitch_key],
                    tpc_for[pitch_key],
                    syllable if syllable else None,
                )
            )

        measures.append(Measure1(content=[Voice(content=voice_content)]))

    score_staff = Staff1(
        id="1",
        content=[vbox, *measures],
    )

    score = Score1(
        content=[
            LayerTag(id="0", tag="default"),
            CurrentLayer(content=content_text("0")),
            Division1(content=content_text(str(division))),
            style,
            ShowInvisible(content=content_text("1")),
            ShowUnprintable(content=content_text("1")),
            ShowFrames(content=content_text("1")),
            ShowMargins(content=content_text("0")),
            MetaTag(name="workTitle", content=content_text(title)),
            MetaTag(name="composer", content=content_text(composer)),
            part,
            score_staff,
        ]
    )

    root = MuseScore(
        version="3.02",
        content=[
            ProgramVersion(content=content_text(program_version)),
            ProgramRevision(content=content_text(program_revision)),
            score,
        ],
    )

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

    config = SerializerConfig(pretty_print=True, xml_declaration=True, encoding="UTF-8")
    serializer = XmlSerializer(config=config)
    xml = serializer.render(root)

    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix == ".mscz":
        score_name = f"{output.stem}.mscx"
        container_xml = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            "<container>\n"
            "  <rootfiles>\n"
            f'    <rootfile full-path="{score_name}">\n'
            "      </rootfile>\n"
            "    </rootfiles>\n"
            "  </container>\n"
        )
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("META-INF/container.xml", container_xml)
            archive.writestr(score_name, xml)
    else:
        output.write_text(xml, encoding="utf-8")
    typer.echo(str(output))


@app.command()
def amazing_grace(
    output: Path = typer.Argument(..., help="Output .mscx or .mscz file path"),
    title: str = typer.Option("Amazing Grace", help="Score title"),
    composer: str = typer.Option("Traditional", help="Composer name"),
    program_version: str = typer.Option("3.6.2", help="MuseScore program version"),
    program_revision: str = typer.Option("3224f34", help="MuseScore program revision"),
) -> None:
    root = build_amazing_grace(
        title=title,
        composer=composer,
        program_version=program_version,
        program_revision=program_revision,
    )

    config = SerializerConfig(pretty_print=True, xml_declaration=True, encoding="UTF-8")
    serializer = XmlSerializer(config=config)
    xml = serializer.render(root)

    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix == ".mscz":
        score_name = f"{output.stem}.mscx"
        container_xml = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            "<container>\n"
            "  <rootfiles>\n"
            f'    <rootfile full-path="{score_name}">\n'
            "      </rootfile>\n"
            "    </rootfiles>\n"
            "  </container>\n"
        )
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("META-INF/container.xml", container_xml)
            archive.writestr(score_name, xml)
    else:
        output.write_text(xml, encoding="utf-8")
    typer.echo(str(output))


if __name__ == "__main__":
    app()
