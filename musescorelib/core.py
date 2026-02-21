from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable

from musescore_schema.musescore_3_6_2 import (
    Accidental2,
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
    Note1,
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
    Channel1,
)


def _content_text(value: str) -> list[object]:
    return [value]


def _note(pitch: int, tpc: int) -> Note1:
    return Note1(content=[Pitch(content=_content_text(str(pitch))), Tpc(content=_content_text(str(tpc)))])


def _lyric(text: str) -> Lyrics:
    return Lyrics(content=[Text2(content=_content_text(text))])


def _chord(duration: str, pitch: int, tpc: int, lyric_text: str | None = None) -> Chord1:
    content: list[object] = [DurationType1(content=_content_text(duration))]
    if lyric_text:
        content.append(_lyric(lyric_text))
    content.append(_note(pitch, tpc))
    return Chord1(content=content)


def _harmony(root_tpc: int, extension_value: str = "1") -> Harmony1:
    content = [
        Root(content=_content_text(str(root_tpc))),
        Extension(content=_content_text(extension_value)),
    ]
    return Harmony1(content=content)


def _find_score(muse_score: MuseScore) -> Score1:
    for item in muse_score.content:
        if isinstance(item, Score1):
            return item
    raise ValueError("MuseScore document has no Score element")


def _find_staff(score: Score1, staff_id: str = "1") -> Staff1:
    for item in score.content:
        if isinstance(item, Staff1) and item.id == staff_id:
            return item
    raise ValueError(f"Score has no Staff with id {staff_id}")


def _find_part(score: Score1) -> Part1:
    for item in score.content:
        if isinstance(item, Part1):
            return item
    raise ValueError("Score has no Part element")


def _ensure_meta(score: Score1, name: str, value: str) -> None:
    for item in score.content:
        if isinstance(item, MetaTag) and item.name == name:
            item.content = _content_text(value)
            return
    score.content.append(MetaTag(name=name, content=_content_text(value)))


_PITCH_RE = re.compile(r"^([A-Ga-g])([#b]?)(-?\d+)$")
_TPC_MAP = {
    "C": 14,
    "C#": 21,
    "Db": 8,
    "D": 16,
    "D#": 23,
    "Eb": 10,
    "E": 18,
    "F": 13,
    "F#": 20,
    "Gb": 7,
    "G": 15,
    "G#": 22,
    "Ab": 9,
    "A": 17,
    "A#": 24,
    "Bb": 11,
    "B": 19,
}
_SEMITONE_MAP = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


def _parse_pitch(value: str) -> tuple[int, int]:
    match = _PITCH_RE.match(value.strip())
    if not match:
        raise ValueError(f"Invalid pitch format: {value}")
    note, accidental, octave_text = match.groups()
    note = note.upper()
    octave = int(octave_text)
    key = f"{note}{accidental}"
    tpc = _TPC_MAP.get(key)
    if tpc is None:
        raise ValueError(f"Unsupported pitch: {value}")
    semitone = _SEMITONE_MAP[note] + (1 if accidental == "#" else -1 if accidental == "b" else 0)
    midi = (octave + 1) * 12 + semitone
    return midi, tpc


def _parse_chord_root(value: str) -> tuple[int, str]:
    match = re.match(r"^([A-Ga-g])([#b]?)(.*)$", value.strip())
    if not match:
        raise ValueError(f"Invalid chord name: {value}")
    note, accidental, _rest = match.groups()
    key = f"{note.upper()}{accidental}"
    tpc = _TPC_MAP.get(key)
    if tpc is None:
        raise ValueError(f"Unsupported chord root: {value}")
    return tpc, value.strip()


def _new_measure() -> Measure1:
    return Measure1(content=[Voice(content=[])])


@dataclass
class HarmonyEvent:
    staff_id: str
    measure_index: int
    beat: float
    root_tpc: int | None
    text: str | None


def _text_from_content(content: list[object] | None) -> str | None:
    if not content:
        return None
    for value in content:
        if isinstance(value, str):
            return value
    return None


def _extract_duration_beats(item: object, time_sig: tuple[int, int]) -> float:
    duration_type = None
    duration_value = None
    content = getattr(item, "content", None)
    if isinstance(content, list):
        for child in content:
            if isinstance(child, DurationType1):
                duration_type = _text_from_content(child.content)
            if isinstance(child, Duration):
                duration_value = _text_from_content(child.content)

    if duration_value:
        parts = duration_value.split("/")
        if len(parts) == 2:
            try:
                n = float(parts[0])
                d = float(parts[1])
                return (n / d) * 4.0
            except ValueError:
                pass

    if duration_type == "measure":
        return time_sig[0] * (4.0 / time_sig[1])

    mapping = {
        "whole": 4.0,
        "half": 2.0,
        "quarter": 1.0,
        "eighth": 0.5,
        "16th": 0.25,
        "32nd": 0.125,
        "64th": 0.0625,
    }
    return mapping.get(duration_type or "", 0.0)


def _extract_harmony_data(harmony: Harmony1) -> tuple[int | None, str | None]:
    root_value: int | None = None
    text_value: str | None = None
    for item in harmony.content:
        if isinstance(item, Root):
            text = _text_from_content(item.content)
            if text is not None:
                try:
                    root_value = int(text)
                except ValueError:
                    root_value = None
        if isinstance(item, Text2):
            text_value = _text_from_content(item.content)
    return root_value, text_value


@dataclass
class MuseScoreDocument:
    muse_score: MuseScore

    @property
    def score_node(self) -> Score1:
        return _find_score(self.muse_score)

    @property
    def score(self) -> "ScoreAccessor":
        return ScoreAccessor(self)

    def set_title(self, title: str) -> None:
        _ensure_meta(self.score_node, "workTitle", title)
        self._ensure_vbox_text("Title", title)

    def set_composer(self, composer: str) -> None:
        _ensure_meta(self.score_node, "composer", composer)
        self._ensure_vbox_text("Composer", composer)

    def add_measure(
        self,
        notes: Iterable[tuple[int, int, str, str | None]] | None = None,
        add_harmony_root: int | None = None,
        staff_id: str = "1",
    ) -> None:
        staff = _find_staff(self.score_node, staff_id)
        voice_content: list[object] = []
        if add_harmony_root is not None:
            voice_content.append(_harmony(add_harmony_root))

        if notes:
            for pitch, tpc, duration, lyric in notes:
                voice_content.append(_chord(duration, pitch, tpc, lyric))
        else:
            voice_content.append(Rest1(content=[DurationType1(content=_content_text("measure"))]))

        staff.content.append(Measure1(content=[Voice(content=voice_content)]))

    def count_measures(self, staff_id: str = "1") -> int:
        staff = _find_staff(self.score_node, staff_id)
        return sum(1 for item in staff.content if isinstance(item, Measure1))

    def count_lyrics(self, staff_id: str = "1") -> int:
        staff = _find_staff(self.score_node, staff_id)
        count = 0
        for measure in (item for item in staff.content if isinstance(item, Measure1)):
            for voice in (item for item in measure.content if isinstance(item, Voice)):
                for chord in (item for item in voice.content if isinstance(item, Chord1)):
                    count += sum(1 for item in chord.content if isinstance(item, Lyrics))
        return count

    def list_harmony_roots(self, staff_id: str = "1") -> list[int]:
        staff = _find_staff(self.score_node, staff_id)
        roots: list[int] = []
        for measure in (item for item in staff.content if isinstance(item, Measure1)):
            for voice in (item for item in measure.content if isinstance(item, Voice)):
                for harmony in (item for item in voice.content if isinstance(item, Harmony1)):
                    for root in (item for item in harmony.content if isinstance(item, Root)):
                        for value in root.content:
                            if isinstance(value, str):
                                try:
                                    roots.append(int(value))
                                except ValueError:
                                    continue
        return roots

    def harmony_events(self, staff_id: str = "1", voice_index: int = 1) -> list["HarmonyEvent"]:
        staff = _find_staff(self.score_node, staff_id)
        return StaffAccessor(self, staff).harmony_events(voice_index=voice_index)

    def _ensure_vbox_text(self, style_name: str, text_value: str) -> None:
        staff = _find_staff(self.score_node, "1")
        vbox = None
        for item in staff.content:
            if isinstance(item, Vbox):
                vbox = item
                break
        if vbox is None:
            vbox = Vbox(content=[Height(content=_content_text("10"))])
            staff.content.insert(0, vbox)

        for item in vbox.content:
            if isinstance(item, Text1):
                style = next((c for c in item.content if isinstance(c, Style2)), None)
                if style is not None and style.content and style.content[0] == style_name:
                    text_node = next((c for c in item.content if isinstance(c, Text2)), None)
                    if text_node is None:
                        item.content.append(Text2(content=_content_text(text_value)))
                    else:
                        text_node.content = _content_text(text_value)
                    return

        vbox.content.append(
            Text1(
                content=[
                    Style2(content=_content_text(style_name)),
                    Text2(content=_content_text(text_value)),
                ]
            )
        )


class ScoreAccessor:
    def __init__(self, doc: MuseScoreDocument) -> None:
        self._doc = doc

    @property
    def node(self) -> Score1:
        return self._doc.score_node

    def part(self, index: int = 1) -> "PartAccessor":
        parts = [item for item in self.node.content if isinstance(item, Part1)]
        if index < 1 or index > len(parts):
            raise ValueError(f"Part index out of range: {index}")
        return PartAccessor(self._doc, parts[index - 1])

    def staff(self, index: int = 1) -> "StaffAccessor":
        staffs = [item for item in self.node.content if isinstance(item, Staff1)]
        if index < 1 or index > len(staffs):
            raise ValueError(f"Staff index out of range: {index}")
        return StaffAccessor(self._doc, staffs[index - 1])


class PartAccessor:
    def __init__(self, doc: MuseScoreDocument, part: Part1) -> None:
        self._doc = doc
        self._part = part

    @property
    def node(self) -> Part1:
        return self._part

    def staff(self, index: int = 1) -> "StaffAccessor":
        return self._doc.score.staff(index)


class StaffAccessor:
    def __init__(self, doc: MuseScoreDocument, staff: Staff1) -> None:
        self._doc = doc
        self._staff = staff

    @property
    def node(self) -> Staff1:
        return self._staff

    def measure(self, index: int) -> "MeasureAccessor":
        if index < 1:
            raise ValueError("Measure index must be >= 1")
        measures = [item for item in self._staff.content if isinstance(item, Measure1)]
        while len(measures) < index:
            new_measure = _new_measure()
            self._staff.content.append(new_measure)
            measures.append(new_measure)
        return MeasureAccessor(self._doc, measures[index - 1])

    def add_measure(self) -> "MeasureAccessor":
        new_measure = _new_measure()
        self._staff.content.append(new_measure)
        return MeasureAccessor(self._doc, new_measure)

    def harmony_events(self, voice_index: int = 1) -> list["HarmonyEvent"]:
        events: list["HarmonyEvent"] = []
        measures = [item for item in self._staff.content if isinstance(item, Measure1)]
        current_time_sig = (4, 4)

        for measure_index, measure in enumerate(measures, start=1):
            voices = [item for item in measure.content if isinstance(item, Voice)]
            if voice_index < 1 or voice_index > len(voices):
                continue
            voice = voices[voice_index - 1]
            beat = 1.0
            for item in voice.content:
                if isinstance(item, TimeSig1):
                    nom = den = None
                    for child in item.content:
                        if isinstance(child, SigN1):
                            nom = _text_from_content(child.content)
                        if isinstance(child, SigD):
                            den = _text_from_content(child.content)
                    if nom and den:
                        try:
                            current_time_sig = (int(nom), int(den))
                        except ValueError:
                            pass
                if isinstance(item, Harmony1):
                    root_value, text_value = _extract_harmony_data(item)
                    events.append(
                        HarmonyEvent(
                            staff_id=self._staff.id or "1",
                            measure_index=measure_index,
                            beat=beat,
                            root_tpc=root_value,
                            text=text_value,
                        )
                    )
                if isinstance(item, (Chord1, Rest1)):
                    beat += _extract_duration_beats(item, current_time_sig)

        return events


class MeasureAccessor:
    def __init__(self, doc: MuseScoreDocument, measure: Measure1) -> None:
        self._doc = doc
        self._measure = measure

    @property
    def node(self) -> Measure1:
        return self._measure

    def voice(self, index: int = 1) -> "VoiceAccessor":
        if index < 1:
            raise ValueError("Voice index must be >= 1")
        voices = [item for item in self._measure.content if isinstance(item, Voice)]
        while len(voices) < index:
            new_voice = Voice(content=[])
            self._measure.content.append(new_voice)
            voices.append(new_voice)
        return VoiceAccessor(self._doc, voices[index - 1])


class VoiceAccessor:
    def __init__(self, doc: MuseScoreDocument, voice: Voice) -> None:
        self._doc = doc
        self._voice = voice

    @property
    def node(self) -> Voice:
        return self._voice

    def add_note(self, pitch: str, duration: str, lyric: str | None = None) -> None:
        midi, tpc = _parse_pitch(pitch)
        self._voice.content.append(_chord(duration, midi, tpc, lyric))

    def add_rest(self, duration: str) -> None:
        self._voice.content.append(Rest1(content=[DurationType1(content=_content_text(duration))]))

    def add_harmony(self, chord_name: str, extension_value: str = "1") -> None:
        root_tpc, text = _parse_chord_root(chord_name)
        harmony = Harmony1(
            content=[
                Root(content=_content_text(str(root_tpc))),
                Extension(content=_content_text(extension_value)),
                Text2(content=_content_text(text)),
            ]
        )
        self._voice.content.append(harmony)

    def add_time_sig(self, nom: int, den: int) -> None:
        self._voice.content.append(
            TimeSig1(
                content=[
                    SigN1(content=_content_text(str(nom))),
                    SigD(content=_content_text(str(den))),
                ]
            )
        )

    def add_key_sig(self, accidental: int) -> None:
        self._voice.content.append(KeySig1(content=[Accidental2(content=_content_text(str(accidental)))]))


def new_document(
    title: str = "Title",
    composer: str = "Composer",
    measures: int = 4,
    time_sig: str = "4/4",
    key_sig: int = 0,
    program_version: str = "3.6.2",
    program_revision: str = "3224f34",
    instrument_id: str = "keyboard.piano",
    track_name: str = "Piano",
    long_name: str = "Piano",
    short_name: str = "Pno.",
    min_pitch: int = 21,
    max_pitch: int = 108,
) -> MuseScoreDocument:
    parts = time_sig.split("/")
    if len(parts) != 2:
        raise ValueError("time_sig must be N/D")
    sig_n, sig_d = int(parts[0]), int(parts[1])

    style = Style1(
        content=[
            EnableVerticalSpread(content=_content_text("1")),
            UseStandardNoteNames(content=_content_text("0")),
            Spatium1(content=_content_text("1.75")),
        ]
    )

    part_staff = Staff1(
        id="1",
        content=[
            StaffType2(
                group="pitched",
                content=[Name(content=_content_text("stdNormal"))],
            )
        ],
    )

    instrument = Instrument1(
        id=instrument_id.split(".")[-1],
        content=[
            LongName(content=_content_text(long_name)),
            ShortName2(content=_content_text(short_name)),
            TrackName2(content=_content_text(track_name)),
            MinPitchP(content=_content_text(str(min_pitch))),
            MaxPitchP(content=_content_text(str(max_pitch))),
            MinPitchA(content=_content_text(str(min_pitch))),
            MaxPitchA(content=_content_text(str(max_pitch))),
            InstrumentId(content=_content_text(instrument_id)),
            Clef2(staff="2", content=_content_text("F")),
            Channel1(
                content=[
                    Program2(value="0"),
                    Synti(content=_content_text("Fluid")),
                ]
            ),
        ],
    )

    part = Part1(
        content=[
            part_staff,
            TrackName2(content=_content_text(track_name)),
            instrument,
        ]
    )

    vbox = Vbox(
        content=[
            Height(content=_content_text("10")),
            Text1(
                content=[
                    Style2(content=_content_text("Title")),
                    Text2(content=_content_text(title)),
                ]
            ),
            Text1(
                content=[
                    Style2(content=_content_text("Composer")),
                    Text2(content=_content_text(composer)),
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
                        SigN1(content=_content_text(str(sig_n))),
                        SigD(content=_content_text(str(sig_d))),
                    ]
                )
            )
            voice_content.append(KeySig1(content=[Accidental2(content=_content_text(str(key_sig)))]))

        voice_content.append(
            Rest1(
                content=[
                    DurationType1(content=_content_text("measure")),
                    Duration(content=_content_text(f"{sig_n}/{sig_d}")),
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
            CurrentLayer(content=_content_text("0")),
            Division1(content=_content_text("480")),
            style,
            ShowInvisible(content=_content_text("1")),
            ShowUnprintable(content=_content_text("1")),
            ShowFrames(content=_content_text("1")),
            ShowMargins(content=_content_text("0")),
            MetaTag(name="workTitle", content=_content_text(title)),
            MetaTag(name="composer", content=_content_text(composer)),
            part,
            score_staff,
        ]
    )

    root = MuseScore(
        version="3.02",
        content=[
            ProgramVersion(content=_content_text(program_version)),
            ProgramRevision(content=_content_text(program_revision)),
            score,
        ],
    )

    doc = MuseScoreDocument(muse_score=root)
    return doc
