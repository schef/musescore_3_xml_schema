from __future__ import annotations

from pathlib import Path
import zipfile

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from musescore_schema.musescore_3_6_2 import MuseScore
from musescorelib.core import MuseScoreDocument


def load_mscx(path: Path) -> MuseScoreDocument:
    xml = Path(path).read_text(encoding="utf-8")
    parser = XmlParser()
    muse_score = parser.from_string(xml, MuseScore)
    return MuseScoreDocument(muse_score=muse_score)


def load_mscz(path: Path) -> MuseScoreDocument:
    path = Path(path)
    with zipfile.ZipFile(path, "r") as archive:
        container = archive.read("META-INF/container.xml").decode("utf-8")
        score_path = _extract_rootfile_path(container)
        xml = archive.read(score_path).decode("utf-8")

    parser = XmlParser()
    muse_score = parser.from_string(xml, MuseScore)
    return MuseScoreDocument(muse_score=muse_score)


def save_mscx(document: MuseScoreDocument, path: Path) -> None:
    path = Path(path)
    serializer = XmlSerializer(config=_serializer_config())
    xml = serializer.render(document.muse_score)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(xml, encoding="utf-8")


def save_mscz(document: MuseScoreDocument, path: Path) -> None:
    path = Path(path)
    serializer = XmlSerializer(config=_serializer_config())
    xml = serializer.render(document.muse_score)
    score_name = f"{path.stem}.mscx"
    container_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<container>\n"
        "  <rootfiles>\n"
        f'    <rootfile full-path="{score_name}">\n'
        "      </rootfile>\n"
        "    </rootfiles>\n"
        "  </container>\n"
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("META-INF/container.xml", container_xml)
        archive.writestr(score_name, xml)


def _serializer_config() -> SerializerConfig:
    return SerializerConfig(pretty_print=True, xml_declaration=True, encoding="UTF-8")


def _extract_rootfile_path(container_xml: str) -> str:
    start = 'full-path="'
    idx = container_xml.find(start)
    if idx == -1:
        raise ValueError("Invalid container.xml: missing full-path")
    idx += len(start)
    end = container_xml.find('"', idx)
    if end == -1:
        raise ValueError("Invalid container.xml: unterminated full-path")
    return container_xml[idx:end]
