from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class ArpeggioHiddenInStdIfTabType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ArpeggioHookLenType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ArpeggioLineWidthType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ArpeggioNoteDistanceType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AttributeType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AudioType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeamModeType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BravuraType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CellType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ClefChangesType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CtrlType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DfermataAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DivisionType1:
    class Meta:
        name = "DivisionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DlongfermataAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DmarcatoAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DottedNotesType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DownMordentAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DownbowAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DportatoAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DshortfermataAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DstaccatissimoAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DupletsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DverylongfermataAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ElementType1:
    class Meta:
        name = "ElementType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EspressivoAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ExcerptType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FboxType:
    class Meta:
        name = "FBoxType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FsymbolType:
    class Meta:
        name = "FSymbolType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FamilyType1:
    class Meta:
        name = "FamilyType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FixMeasureNumbersType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FixMeasureWidthType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GenreType1:
    class Meta:
        name = "GenreType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HookType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HumanPerformanceType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentGroupType1:
    class Meta:
        name = "InstrumentGroupType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class KeySymType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class KeyType1:
    class Meta:
        name = "KeyType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LayerTagType:
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tag: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LayerType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LelandType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricType1:
    class Meta:
        name = "LyricType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MmrestRangeType:
    class Meta:
        name = "MMRestRangeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MagIdxType1:
    class Meta:
        name = "MagIdxType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MagType1:
    class Meta:
        name = "MagType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureCount2XLessType:
    class Meta:
        name = "MeasureCount2xLessType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MenuBarType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MenuType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MessageType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetaType1:
    class Meta:
        name = "MetaType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MidiOptionsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MordentAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MuseSynthType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NodeType:
    action: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    pos: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NonupletsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoteOffType1:
    class Meta:
        name = "NoteOffType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoteOnType1:
    class Meta:
        name = "NoteOnType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OmrPageType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OmrType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OuvertAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PaletteBoxType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PaletteType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PathType1:
    class Meta:
        name = "PathType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PetalumaType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PluginType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlusstopAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PrallAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PrallMordentAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PrallPrallAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PreferenceType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PreferencesType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ProgramType1:
    class Meta:
        name = "ProgramType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class QuadrupletsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class QuantValueType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class QuintupletsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RecognizePickupBarType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RevisionType1:
    class Meta:
        name = "RevisionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Sc4Type:
    class Meta:
        name = "SC4Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Sctype:
    class Meta:
        name = "SCType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Smftype:
    class Meta:
        name = "SMFType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ScoreViewType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SeptupletsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SforzatoaccentAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortcutType1:
    class Meta:
        name = "ShortcutType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortcutsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowMoreType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowStaccatoType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SimplifyDurationsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SnappizzicatorAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SpatiumType1:
    class Meta:
        name = "SpatiumType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SplitStaffType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaccatoAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffListType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffStateType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StateType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemDirectionType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemSlashType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SwingType1:
    class Meta:
        name = "SwingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SymbolListType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SymbolsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemDividerType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemType1:
    class Meta:
        name = "SystemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TempoTextType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TenutoAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ThumbAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ToolBarType1:
    class Meta:
        name = "ToolBarType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ToolbarType2:
    class Meta:
        name = "ToolbarType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TourType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TrackNameType1:
    class Meta:
        name = "TrackNameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TrackType1:
    class Meta:
        name = "TrackType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TracklistType:
    dst_track: None | str = field(
        default=None,
        metadata={
            "name": "dstTrack",
            "type": "Attribute",
        },
    )
    s_track: None | str = field(
        default=None,
        metadata={
            "name": "sTrack",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TrillAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TripletsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TurnAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UfermataAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UlongfermataAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UmarcatoAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UpMordentAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UpPrallAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UpbowAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UportatoAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UshortfermataAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UstaccatissimoAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UverylongfermataAnchorType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoiceCountType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WidgetType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WorkspaceType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ZerberusType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class APitchRangeType:
    class Meta:
        name = "aPitchRangeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AcciaccaturaType:
    class Meta:
        name = "acciaccaturaType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AccidentalDistanceType:
    class Meta:
        name = "accidentalDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AccidentalNoteDistanceType:
    class Meta:
        name = "accidentalNoteDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AccidentalType2:
    class Meta:
        name = "accidentalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ActionType:
    class Meta:
        name = "actionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ActualNotesType1:
    class Meta:
        name = "actual-notesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ActualNotesType2:
    class Meta:
        name = "actualNotesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AeolusType:
    class Meta:
        name = "aeolusType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AkkoladeDistanceType:
    class Meta:
        name = "akkoladeDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AlignType:
    class Meta:
        name = "alignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AllCapsNoteNamesType:
    class Meta:
        name = "allCapsNoteNamesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AlterType:
    class Meta:
        name = "alterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AlwaysShowBracketsWhenEmptyStavesAreHiddenType:
    class Meta:
        name = "alwaysShowBracketsWhenEmptyStavesAreHiddenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AnchorType:
    class Meta:
        name = "anchorType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AngledType:
    class Meta:
        name = "angledType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AppearanceType:
    class Meta:
        name = "appearanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AppoggiaturaType:
    class Meta:
        name = "appoggiaturaType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ArpeggiateType:
    class Meta:
        name = "arpeggiateType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ArrangerType:
    class Meta:
        name = "arrangerType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ArticulationChangeType:
    class Meta:
        name = "articulationChangeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ArticulationType2:
    class Meta:
        name = "articulationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ArticulationsType:
    class Meta:
        name = "articulationsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AttributesType:
    class Meta:
        name = "attributesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AutoAdjustType:
    class Meta:
        name = "autoAdjustType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AutoScaleType:
    class Meta:
        name = "autoScaleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AutomaticCapitalizationType:
    class Meta:
        name = "automaticCapitalizationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AutoplaceType:
    class Meta:
        name = "autoplaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BackType:
    class Meta:
        name = "backType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BackgroundColorType:
    class Meta:
        name = "backgroundColorType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BackslashType:
    class Meta:
        name = "backslashType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BackupType:
    class Meta:
        name = "backupType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarStyleType:
    class Meta:
        name = "bar-styleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarAccidentalDistanceType:
    class Meta:
        name = "barAccidentalDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarCountType:
    class Meta:
        name = "barCountType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarGraceDistanceType:
    class Meta:
        name = "barGraceDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarLineSpanFromType:
    class Meta:
        name = "barLineSpanFromType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarLineSpanToType:
    class Meta:
        name = "barLineSpanToType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarLineSpanType1:
    class Meta:
        name = "barLineSpanType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarNoteDistanceType:
    class Meta:
        name = "barNoteDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarWidthType:
    class Meta:
        name = "barWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarlineSpanType2:
    class Meta:
        name = "barlineSpanType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarlineType2:
    class Meta:
        name = "barlineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarlinesType:
    class Meta:
        name = "barlinesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BarreType:
    class Meta:
        name = "barreType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BaseCaseType:
    class Meta:
        name = "baseCaseType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BaseDotsType:
    class Meta:
        name = "baseDotsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BaseLenType:
    class Meta:
        name = "baseLenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BaseNoteType:
    class Meta:
        name = "baseNoteType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BaseType:
    class Meta:
        name = "baseType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BasicType:
    class Meta:
        name = "basicType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BassAlterType:
    class Meta:
        name = "bass-alterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BassStepType:
    class Meta:
        name = "bass-stepType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BassType:
    class Meta:
        name = "bassType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeamDistanceType:
    class Meta:
        name = "beamDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeamFlatteningType:
    class Meta:
        name = "beamFlatteningType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeamMaxSlopeType:
    class Meta:
        name = "beamMaxSlopeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeamMinLenType:
    class Meta:
        name = "beamMinLenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeamMinSlopeType:
    class Meta:
        name = "beamMinSlopeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeamType2:
    class Meta:
        name = "beamType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeamWidthType:
    class Meta:
        name = "beamWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeatTypeType:
    class Meta:
        name = "beat-typeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeatUnitDotType:
    class Meta:
        name = "beat-unit-dotType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeatUnitType:
    class Meta:
        name = "beat-unitType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeatsType:
    class Meta:
        name = "beatsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeginFontFaceType:
    class Meta:
        name = "beginFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeginFontSizeType:
    class Meta:
        name = "beginFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeginFontStyleType:
    class Meta:
        name = "beginFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeginHookHeightType:
    class Meta:
        name = "beginHookHeightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeginHookTypeType:
    class Meta:
        name = "beginHookTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeginHookType1:
    class Meta:
        name = "beginHookType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeginRepeatLeftMarginType:
    class Meta:
        name = "beginRepeatLeftMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeginSymbolOffsetType:
    class Meta:
        name = "beginSymbolOffsetType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeginSymbolType:
    class Meta:
        name = "beginSymbolType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeginTextAlignType:
    class Meta:
        name = "beginTextAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BeginTextPlaceType:
    class Meta:
        name = "beginTextPlaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BendAlignType:
    class Meta:
        name = "bendAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BendFontFaceType:
    class Meta:
        name = "bendFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BendFontSizeType:
    class Meta:
        name = "bendFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BendFramePaddingType:
    class Meta:
        name = "bendFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BendFrameWidthType:
    class Meta:
        name = "bendFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BoldType:
    class Meta:
        name = "boldType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BookType:
    class Meta:
        name = "bookType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BottomMarginType1:
    class Meta:
        name = "bottom-marginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BottomGapType:
    class Meta:
        name = "bottomGapType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BottomMarginType2:
    class Meta:
        name = "bottomMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BottomPitchType:
    class Meta:
        name = "bottomPitchType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BottomTpcType:
    class Meta:
        name = "bottomTpcType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BoxAutoSizeType:
    class Meta:
        name = "boxAutoSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BrType:
    class Meta:
        name = "brType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BracketDistanceType:
    class Meta:
        name = "bracketDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BracketSpanType:
    class Meta:
        name = "bracketSpanType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BracketTypeType:
    class Meta:
        name = "bracketTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BracketType1:
    class Meta:
        name = "bracketType"

    col: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    span: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BracketWidthType:
    class Meta:
        name = "bracketWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BracketsType:
    class Meta:
        name = "bracketsType"

    b0: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    b1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    b2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    b3: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    b4: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BreakMultiMeasureRestType:
    class Meta:
        name = "breakMultiMeasureRestType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BreathMarkType:
    class Meta:
        name = "breath-markType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class BreveType:
    class Meta:
        name = "breveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CaesuraType:
    class Meta:
        name = "caesuraType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CancelType:
    class Meta:
        name = "cancelType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CapoType:
    class Meta:
        name = "capoType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChannelSwitchType:
    class Meta:
        name = "channelSwitchType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    voice: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChannelType2:
    class Meta:
        name = "channelType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordLineType2:
    class Meta:
        name = "chord-lineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordDescriptionFileType:
    class Meta:
        name = "chordDescriptionFileType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordExtensionAdjustType:
    class Meta:
        name = "chordExtensionAdjustType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordExtensionMagType:
    class Meta:
        name = "chordExtensionMagType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordModifierAdjustType:
    class Meta:
        name = "chordModifierAdjustType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordModifierMagType:
    class Meta:
        name = "chordModifierMagType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordNamesUseJazzFontType:
    class Meta:
        name = "chordNamesUseJazzFontType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordStyleType:
    class Meta:
        name = "chordStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordSymbolAalignType:
    class Meta:
        name = "chordSymbolAAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordSymbolAfontFaceType:
    class Meta:
        name = "chordSymbolAFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordSymbolAfontSizeType:
    class Meta:
        name = "chordSymbolAFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordSymbolAfontStyleType:
    class Meta:
        name = "chordSymbolAFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordSymbolAframePaddingType:
    class Meta:
        name = "chordSymbolAFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordSymbolAframeWidthType:
    class Meta:
        name = "chordSymbolAFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordSymbolBalignType:
    class Meta:
        name = "chordSymbolBAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordSymbolBfontFaceType:
    class Meta:
        name = "chordSymbolBFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordSymbolBfontSizeType:
    class Meta:
        name = "chordSymbolBFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordSymbolBposAboveType:
    class Meta:
        name = "chordSymbolBPosAboveType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordSymbolPosAboveType:
    class Meta:
        name = "chordSymbolPosAboveType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChordsXmlFileType:
    class Meta:
        name = "chordsXmlFileType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChorusType:
    class Meta:
        name = "chorusType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ChromaticType:
    class Meta:
        name = "chromaticType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CircleXType:
    class Meta:
        name = "circle-xType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CircleType:
    class Meta:
        name = "circleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CleanType:
    class Meta:
        name = "cleanType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ClefOctaveChangeType:
    class Meta:
        name = "clef-octave-changeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ClefBarlineDistanceType:
    class Meta:
        name = "clefBarlineDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ClefKeyRightMarginType:
    class Meta:
        name = "clefKeyRightMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ClefLeftMarginType:
    class Meta:
        name = "clefLeftMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ClefSignType:
    class Meta:
        name = "clefSignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ClefType2:
    class Meta:
        name = "clefType"

    idx: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    staff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tick: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CodaType:
    class Meta:
        name = "codaType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CodeType:
    class Meta:
        name = "codeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ColorType:
    class Meta:
        name = "colorType"

    a: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    b: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    g: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    r: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ComposerFontFaceType:
    class Meta:
        name = "composerFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ComposerFontSizeType:
    class Meta:
        name = "composerFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ComposerFontSpatiumDependentType:
    class Meta:
        name = "composerFontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ComposerFontStyleType:
    class Meta:
        name = "composerFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ComposerFramePaddingType:
    class Meta:
        name = "composerFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ComposerFrameRoundType:
    class Meta:
        name = "composerFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ComposerFrameWidthType:
    class Meta:
        name = "composerFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ComposerType:
    class Meta:
        name = "composerType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ConcertClefTypeType:
    class Meta:
        name = "concertClefTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ConcertClefType1:
    class Meta:
        name = "concertClefType"

    staff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ConcertPitchType:
    class Meta:
        name = "concertPitchType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ContainerType:
    class Meta:
        name = "containerType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ContentType:
    class Meta:
        name = "contentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ContinuationLineType:
    class Meta:
        name = "continuationLineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ContinueAtType:
    class Meta:
        name = "continueAtType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ContinueSymbolOffsetType:
    class Meta:
        name = "continueSymbolOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ContinueSymbolType:
    class Meta:
        name = "continueSymbolType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ContinueTextPlaceType:
    class Meta:
        name = "continueTextPlaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ControllerType:
    class Meta:
        name = "controllerType"

    channel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ctrl: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tick: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CreateMultiMeasureRestsType:
    class Meta:
        name = "createMultiMeasureRestsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CreatedType:
    class Meta:
        name = "createdType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CreationDateType:
    class Meta:
        name = "creationDateType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CreatorType:
    class Meta:
        name = "creatorType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CreditTypeType:
    class Meta:
        name = "credit-typeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CreditWordsType:
    class Meta:
        name = "credit-wordsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CreditType1:
    class Meta:
        name = "creditType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CropBtype:
    class Meta:
        name = "cropBType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CropLtype:
    class Meta:
        name = "cropLType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CropRtype:
    class Meta:
        name = "cropRType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CropTtype:
    class Meta:
        name = "cropTType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CrossMeasureValuesType:
    class Meta:
        name = "crossMeasureValuesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CrossType:
    class Meta:
        name = "crossType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CueType:
    class Meta:
        name = "cueType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CurrentLayerType:
    class Meta:
        name = "currentLayerType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CursorTrackType:
    class Meta:
        name = "cursorTrackType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CustomSubtypeType:
    class Meta:
        name = "customSubtypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CustomType:
    class Meta:
        name = "customType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CutawayType:
    class Meta:
        name = "cutawayType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DashGapLengthType:
    class Meta:
        name = "dashGapLengthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DashLineLengthType:
    class Meta:
        name = "dashLineLengthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DashesType:
    class Meta:
        name = "dashesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DateType:
    class Meta:
        name = "dateType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultAlignType:
    class Meta:
        name = "defaultAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultClefType:
    class Meta:
        name = "defaultClefType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultConcertClefType:
    class Meta:
        name = "defaultConcertClefType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultFontFaceType:
    class Meta:
        name = "defaultFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultFontSpatiumDependentType:
    class Meta:
        name = "defaultFontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultFramePaddingType:
    class Meta:
        name = "defaultFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultFrameRoundType:
    class Meta:
        name = "defaultFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultFrameWidthType:
    class Meta:
        name = "defaultFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultLineHeightType:
    class Meta:
        name = "defaultLineHeightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultOffsetType:
    class Meta:
        name = "defaultOffsetType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultPitchType:
    class Meta:
        name = "defaultPitchType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultTransposingClefType:
    class Meta:
        name = "defaultTransposingClefType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultYoffsetType:
    class Meta:
        name = "defaultYOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultsType:
    class Meta:
        name = "defaultsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DefaultsVersionType:
    class Meta:
        name = "defaultsVersionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DegreeAlterType:
    class Meta:
        name = "degree-alterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DegreeTypeType:
    class Meta:
        name = "degree-typeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DegreeValueType:
    class Meta:
        name = "degree-valueType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DegreeType1:
    class Meta:
        name = "degreeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DelayedTurnType:
    class Meta:
        name = "delayed-turnType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DenType:
    class Meta:
        name = "denType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Denom2Type:
    class Meta:
        name = "denom2Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DenomType:
    class Meta:
        name = "denomType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DescrType:
    class Meta:
        name = "descrType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DescriptionType:
    class Meta:
        name = "descriptionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DiagonalType:
    class Meta:
        name = "diagonalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DiamondType:
    class Meta:
        name = "diamondType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DiatonicType:
    class Meta:
        name = "diatonicType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DiffType:
    class Meta:
        name = "diffType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DigitType:
    class Meta:
        name = "digitType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DirectionTypeType:
    class Meta:
        name = "direction-typeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DirectionType1:
    class Meta:
        name = "directionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DirtyType:
    class Meta:
        name = "dirtyType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DisplayOctaveType:
    class Meta:
        name = "display-octaveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DisplayStepType:
    class Meta:
        name = "display-stepType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DisplayInConcertPitchType:
    class Meta:
        name = "displayInConcertPitchType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DisplayNameType:
    class Meta:
        name = "displayNameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DisplayType:
    class Meta:
        name = "displayType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DistOffsetType:
    class Meta:
        name = "distOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DistancesType:
    class Meta:
        name = "distancesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DistributeType:
    class Meta:
        name = "distributeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DividerLeftType:
    class Meta:
        name = "dividerLeftType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DivisionType2:
    class Meta:
        name = "divisionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DivisionsType:
    class Meta:
        name = "divisionsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DoType:
    class Meta:
        name = "doType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DoitType:
    class Meta:
        name = "doitType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DontHidStavesInFirstSystmType:
    class Meta:
        name = "dontHidStavesInFirstSystmType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DotDotDistanceType:
    class Meta:
        name = "dotDotDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DotNoteDistanceType:
    class Meta:
        name = "dotNoteDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DotPositionType:
    class Meta:
        name = "dotPositionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DotType:
    class Meta:
        name = "dotType"

    fret: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DotsType:
    class Meta:
        name = "dotsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DoubleAngledType:
    class Meta:
        name = "double-angledType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DoubleDotType:
    class Meta:
        name = "double-dotType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DoubleSquareType:
    class Meta:
        name = "double-squareType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DoubleBarDistanceType:
    class Meta:
        name = "doubleBarDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DoubleBarWidthType:
    class Meta:
        name = "doubleBarWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DoubleflatType:
    class Meta:
        name = "doubleflatType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DoublesharpType:
    class Meta:
        name = "doublesharpType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DownloadUrlType:
    class Meta:
        name = "downloadUrlType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DpmmType:
    class Meta:
        name = "dpmmType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DragOffsetType:
    class Meta:
        name = "dragOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DrawObjType:
    class Meta:
        name = "drawObjType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DrawObjectsType:
    class Meta:
        name = "drawObjectsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DrumPaletteType:
    class Meta:
        name = "drumPaletteType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DrumsetType:
    class Meta:
        name = "drumsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DurationFontNameType:
    class Meta:
        name = "durationFontNameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DurationFontSizeType:
    class Meta:
        name = "durationFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DurationFontType:
    class Meta:
        name = "durationFontType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DurationFontYtype:
    class Meta:
        name = "durationFontYType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DurationTypeType:
    class Meta:
        name = "durationTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DurationType1:
    class Meta:
        name = "durationType"

    n: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    z: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DurationsType:
    class Meta:
        name = "durationsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DynTypeType:
    class Meta:
        name = "dynTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DynamicsFontFaceType:
    class Meta:
        name = "dynamicsFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DynamicsFontItalicType:
    class Meta:
        name = "dynamicsFontItalicType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DynamicsFontSizeType:
    class Meta:
        name = "dynamicsFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DynamicsFontStyleType:
    class Meta:
        name = "dynamicsFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DynamicsFramePaddingType:
    class Meta:
        name = "dynamicsFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DynamicsFrameWidthType:
    class Meta:
        name = "dynamicsFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DynamicsPosAboveType:
    class Meta:
        name = "dynamicsPosAboveType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DynamicsPosBelowType:
    class Meta:
        name = "dynamicsPosBelowType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DynamicsType:
    class Meta:
        name = "dynamicsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EaseInSpinType:
    class Meta:
        name = "easeInSpinType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EaseOutSpinType:
    class Meta:
        name = "easeOutSpinType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EditableType:
    class Meta:
        name = "editableType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ElementType2:
    class Meta:
        name = "elementType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ElementsType:
    class Meta:
        name = "elementsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ElisionType:
    class Meta:
        name = "elisionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EllipseType:
    class Meta:
        name = "ellipseType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EnableIndentationOnFirstSystemType:
    class Meta:
        name = "enableIndentationOnFirstSystemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EnableVerticalSpreadType:
    class Meta:
        name = "enableVerticalSpreadType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EncodingDateType:
    class Meta:
        name = "encoding-dateType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EncodingType:
    class Meta:
        name = "encodingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndBarDistanceType:
    class Meta:
        name = "endBarDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndBarWidthType:
    class Meta:
        name = "endBarWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndHookHeightType:
    class Meta:
        name = "endHookHeightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndHookTypeType:
    class Meta:
        name = "endHookTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndHookType1:
    class Meta:
        name = "endHookType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndRepeatType:
    class Meta:
        name = "endRepeatType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndSpannerType:
    class Meta:
        name = "endSpannerType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndSymbolOffsetType:
    class Meta:
        name = "endSymbolOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndSymbolType:
    class Meta:
        name = "endSymbolType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndTextAlignType:
    class Meta:
        name = "endTextAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndTextPlaceType:
    class Meta:
        name = "endTextPlaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndTextType:
    class Meta:
        name = "endTextType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndTickType:
    class Meta:
        name = "endTickType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndTrackType:
    class Meta:
        name = "endTrackType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndTupletType:
    class Meta:
        name = "endTupletType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndingType:
    class Meta:
        name = "endingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EndingsType:
    class Meta:
        name = "endingsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EnsembleType:
    class Meta:
        name = "ensembleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EvenFooterCtype:
    class Meta:
        name = "evenFooterCType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EvenFooterLtype:
    class Meta:
        name = "evenFooterLType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EvenFooterRtype:
    class Meta:
        name = "evenFooterRType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EvenFooterType:
    class Meta:
        name = "evenFooterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EvenHeaderCtype:
    class Meta:
        name = "evenHeaderCType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EvenHeaderLtype:
    class Meta:
        name = "evenHeaderLType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EvenHeaderRtype:
    class Meta:
        name = "evenHeaderRType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EvenHeaderType:
    class Meta:
        name = "evenHeaderType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EventType2:
    class Meta:
        name = "eventType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class EventsType2:
    class Meta:
        name = "eventsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ExpandedType:
    class Meta:
        name = "expandedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ExpressionFontFaceType:
    class Meta:
        name = "expressionFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ExpressionFontSizeType:
    class Meta:
        name = "expressionFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ExpressionFramePaddingType:
    class Meta:
        name = "expressionFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ExpressionFrameWidthType:
    class Meta:
        name = "expressionFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ExtendType:
    class Meta:
        name = "extendType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ExtendedType:
    class Meta:
        name = "extendedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ExtensionType:
    class Meta:
        name = "extensionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ExtraDistanceType:
    class Meta:
        name = "extraDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FType:
    class Meta:
        name = "fType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FaType:
    class Meta:
        name = "faType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FalloffType:
    class Meta:
        name = "falloffType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FamilyType2:
    class Meta:
        name = "familyType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FermataPosAboveType:
    class Meta:
        name = "fermataPosAboveType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FermataPosBelowType:
    class Meta:
        name = "fermataPosBelowType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FermataType2:
    class Meta:
        name = "fermataType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FifthsType:
    class Meta:
        name = "fifthsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FigureNumberType:
    class Meta:
        name = "figure-numberType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FigureType:
    class Meta:
        name = "figureType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FiguredBassType2:
    class Meta:
        name = "figured-bassType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FiguredBassFontFaceType:
    class Meta:
        name = "figuredBassFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FileType:
    class Meta:
        name = "fileType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FingeringFontFaceType:
    class Meta:
        name = "fingeringFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FingeringFontSizeType:
    class Meta:
        name = "fingeringFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FingeringFramePaddingType:
    class Meta:
        name = "fingeringFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FingeringFrameRoundType:
    class Meta:
        name = "fingeringFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FingeringFrameWidthType:
    class Meta:
        name = "fingeringFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FingeringType2:
    class Meta:
        name = "fingeringType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FirstSystemIdentationType:
    class Meta:
        name = "firstSystemIdentationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FixedLineType:
    class Meta:
        name = "fixedLineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FixedType:
    class Meta:
        name = "fixedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FlatType:
    class Meta:
        name = "flatType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FollowTextType:
    class Meta:
        name = "followTextType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FontsizeType:
    class Meta:
        name = "fontsizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FooterAlignType:
    class Meta:
        name = "footerAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FooterFontFaceType:
    class Meta:
        name = "footerFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FooterFontSizeType:
    class Meta:
        name = "footerFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FooterFramePaddingType:
    class Meta:
        name = "footerFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FooterFrameWidthType:
    class Meta:
        name = "footerFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FooterOddEvenType:
    class Meta:
        name = "footerOddEvenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ForInstrumentChangeType:
    class Meta:
        name = "forInstrumentChangeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ForegroundColorType:
    class Meta:
        name = "foregroundColorType"

    b: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    g: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    r: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FormatType:
    class Meta:
        name = "formatType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ForwardType:
    class Meta:
        name = "forwardType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FractionsType:
    class Meta:
        name = "fractionsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameFretsType:
    class Meta:
        name = "frame-fretsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameNoteType:
    class Meta:
        name = "frame-noteType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameStringsType:
    class Meta:
        name = "frame-stringsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameAlignType:
    class Meta:
        name = "frameAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameColorType:
    class Meta:
        name = "frameColorType"

    a: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    b: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    g: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    r: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameFontFaceType:
    class Meta:
        name = "frameFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameFontSizeType:
    class Meta:
        name = "frameFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameFontSpatiumDependentType:
    class Meta:
        name = "frameFontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameFramePaddingType:
    class Meta:
        name = "frameFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameFrameWidthType:
    class Meta:
        name = "frameFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FramePaddingType:
    class Meta:
        name = "framePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameRoundType:
    class Meta:
        name = "frameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameSystemDistanceType:
    class Meta:
        name = "frameSystemDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameTypeType:
    class Meta:
        name = "frameTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameType1:
    class Meta:
        name = "frameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameWidthStype:
    class Meta:
        name = "frameWidthSType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FrameWidthType:
    class Meta:
        name = "frameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FreeGlyphsType:
    class Meta:
        name = "free-glyphsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FretFontNameType:
    class Meta:
        name = "fretFontNameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FretFontSizeType:
    class Meta:
        name = "fretFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FretFontType:
    class Meta:
        name = "fretFontType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FretFontYtype:
    class Meta:
        name = "fretFontYType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FretOffsetType:
    class Meta:
        name = "fretOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FretType:
    class Meta:
        name = "fretType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FretsType:
    class Meta:
        name = "fretsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FunctionType:
    class Meta:
        name = "functionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GalleryType:
    class Meta:
        name = "galleryType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GateTimeType:
    class Meta:
        name = "gateTimeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GenClefType:
    class Meta:
        name = "genClefType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GenCourtesyClefType:
    class Meta:
        name = "genCourtesyClefType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GenCourtesyKeysigType:
    class Meta:
        name = "genCourtesyKeysigType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GenCourtesyTimesigType:
    class Meta:
        name = "genCourtesyTimesigType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GenKeysigType:
    class Meta:
        name = "genKeysigType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GenTimesigType:
    class Meta:
        name = "genTimesigType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GenreType2:
    class Meta:
        name = "genreType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GhostType:
    class Meta:
        name = "ghostType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GlissandoAlignType:
    class Meta:
        name = "glissandoAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GlissandoFontFaceType:
    class Meta:
        name = "glissandoFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GlissandoFontSizeType:
    class Meta:
        name = "glissandoFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GlissandoFramePaddingType:
    class Meta:
        name = "glissandoFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GlissandoFrameWidthType:
    class Meta:
        name = "glissandoFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GlissandoStyleType:
    class Meta:
        name = "glissandoStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GlissandoType2:
    class Meta:
        name = "glissandoType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GlyphIndexType:
    class Meta:
        name = "glyph-indexType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GlyphType:
    class Meta:
        name = "glyphType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Grace16Type:
    class Meta:
        name = "grace16Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Grace16AfterType:
    class Meta:
        name = "grace16afterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Grace32Type:
    class Meta:
        name = "grace32Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Grace32AfterType:
    class Meta:
        name = "grace32afterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Grace4Type:
    class Meta:
        name = "grace4Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Grace8AfterType:
    class Meta:
        name = "grace8afterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GraceNoteMagType:
    class Meta:
        name = "graceNoteMagType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GraceType:
    class Meta:
        name = "graceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GridHeightType:
    class Meta:
        name = "gridHeightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GridType:
    class Meta:
        name = "gridType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GridWidthType:
    class Meta:
        name = "gridWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GroupAbbreviationType:
    class Meta:
        name = "group-abbreviationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GroupBarlineType:
    class Meta:
        name = "group-barlineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GroupNameType:
    class Meta:
        name = "group-nameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GroupSymbolType:
    class Meta:
        name = "group-symbolType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GroupType:
    class Meta:
        name = "groupType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GrowLeftType:
    class Meta:
        name = "growLeftType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GrowRightType:
    class Meta:
        name = "growRightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class GuitarType:
    class Meta:
        name = "guitarType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HairpinCircledTipType:
    class Meta:
        name = "hairpinCircledTipType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HairpinContHeightType:
    class Meta:
        name = "hairpinContHeightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HairpinFontFaceType:
    class Meta:
        name = "hairpinFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HairpinFontSizeType:
    class Meta:
        name = "hairpinFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HairpinFramePaddingType:
    class Meta:
        name = "hairpinFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HairpinFrameWidthType:
    class Meta:
        name = "hairpinFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HairpinHeightType:
    class Meta:
        name = "hairpinHeightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HairpinWidthType:
    class Meta:
        name = "hairpinWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HalfCurveType:
    class Meta:
        name = "half-curveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HalfType:
    class Meta:
        name = "halfType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HalignType:
    class Meta:
        name = "halignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HarmonicType:
    class Meta:
        name = "harmonicType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HarmonyDurationType:
    class Meta:
        name = "harmonyDurationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HarmonyFretDistType:
    class Meta:
        name = "harmonyFretDistType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HarmonyPlayType:
    class Meta:
        name = "harmonyPlayType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HarmonyTypeType:
    class Meta:
        name = "harmonyTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HarmonyType2:
    class Meta:
        name = "harmonyType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HarmonyVoiceLiteralType:
    class Meta:
        name = "harmonyVoiceLiteralType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HarmonyVoicingType:
    class Meta:
        name = "harmonyVoicingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HarmonyYtype:
    class Meta:
        name = "harmonyYType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HasLineType:
    class Meta:
        name = "hasLineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HasNumberType:
    class Meta:
        name = "hasNumberType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeadSchemeType:
    class Meta:
        name = "headSchemeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeadTypeType:
    class Meta:
        name = "headTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeaderAlignType:
    class Meta:
        name = "headerAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeaderFirstPageType:
    class Meta:
        name = "headerFirstPageType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeaderFontBoldType:
    class Meta:
        name = "headerFontBoldType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeaderFontFaceType:
    class Meta:
        name = "headerFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeaderFontSizeType:
    class Meta:
        name = "headerFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeaderFontStyleType:
    class Meta:
        name = "headerFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeaderFramePaddingType:
    class Meta:
        name = "headerFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeaderFrameWidthType:
    class Meta:
        name = "headerFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeaderType:
    class Meta:
        name = "headerType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeadsType:
    class Meta:
        name = "headsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HeightType:
    class Meta:
        name = "heightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HideEmptyStavesType:
    class Meta:
        name = "hideEmptyStavesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HideInstrumentNameIfOneInstrumentType:
    class Meta:
        name = "hideInstrumentNameIfOneInstrumentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HideSystemBarLineType:
    class Meta:
        name = "hideSystemBarLineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HideWhenEmptyType:
    class Meta:
        name = "hideWhenEmptyType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HookHeightType:
    class Meta:
        name = "hookHeightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HookUpType:
    class Meta:
        name = "hookUpType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class IdType:
    class Meta:
        name = "idType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class IdentificationType:
    class Meta:
        name = "identificationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class IdxType:
    class Meta:
        name = "idxType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class IndexDiffType:
    class Meta:
        name = "indexDiffType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InfoType:
    class Meta:
        name = "infoType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InfoUrlType:
    class Meta:
        name = "infoUrlType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InitType:
    class Meta:
        name = "initType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentGroupType2:
    class Meta:
        name = "instrument-groupType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentNameType:
    class Meta:
        name = "instrument-nameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentSoundType:
    class Meta:
        name = "instrument-soundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentChangeAlignType:
    class Meta:
        name = "instrumentChangeAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentChangeFontFaceType:
    class Meta:
        name = "instrumentChangeFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentChangeFontSizeType:
    class Meta:
        name = "instrumentChangeFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentChangeFramePaddingType:
    class Meta:
        name = "instrumentChangeFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentChangeFrameWidthType:
    class Meta:
        name = "instrumentChangeFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentIdType:
    class Meta:
        name = "instrumentIdType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentNamesType:
    class Meta:
        name = "instrumentNamesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstrumentsType:
    class Meta:
        name = "instrumentsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class IntersType:
    class Meta:
        name = "intersType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InversionType:
    class Meta:
        name = "inversionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InvertedMordentType:
    class Meta:
        name = "inverted-mordentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InvertedTurnType:
    class Meta:
        name = "inverted-turnType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InvertedType:
    class Meta:
        name = "invertedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InvisibleType:
    class Meta:
        name = "invisibleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class IrregularType:
    class Meta:
        name = "irregularType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ItalicType:
    class Meta:
        name = "italicType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class JumpToType:
    class Meta:
        name = "jumpToType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class KeyAccidentalType:
    class Meta:
        name = "key-accidentalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class KeyAlterType:
    class Meta:
        name = "key-alterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class KeyStepType:
    class Meta:
        name = "key-stepType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class KeySigNaturalsType:
    class Meta:
        name = "keySigNaturalsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class KeySignType:
    class Meta:
        name = "keySignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class KeyType2:
    class Meta:
        name = "keyType"

    idx: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tick: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class KeysigLeftMarginType:
    class Meta:
        name = "keysigLeftMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class KeysigType2:
    class Meta:
        name = "keysigType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class KindType:
    class Meta:
        name = "kindType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class L1Type:
    class Meta:
        name = "l1Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class L2Type:
    class Meta:
        name = "l2Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LaType:
    class Meta:
        name = "laType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LabelType:
    class Meta:
        name = "labelType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LandscapeType:
    class Meta:
        name = "landscapeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LastSystemFillLimitType:
    class Meta:
        name = "lastSystemFillLimitType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LayoutModeType:
    class Meta:
        name = "layoutModeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LayoutOffsetType:
    class Meta:
        name = "layoutOffsetType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LayoutType:
    class Meta:
        name = "layoutType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LeadingSpaceType:
    class Meta:
        name = "leadingSpaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LedgerLineLengthType:
    class Meta:
        name = "ledgerLineLengthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LedgerLineWidthType:
    class Meta:
        name = "ledgerLineWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LedgerlinesType:
    class Meta:
        name = "ledgerlinesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LeftMarginType1:
    class Meta:
        name = "left-marginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LeftMarginType2:
    class Meta:
        name = "leftMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LeftParenType:
    class Meta:
        name = "leftParenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LenType:
    class Meta:
        name = "lenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LengthType:
    class Meta:
        name = "lengthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LengthXtype:
    class Meta:
        name = "lengthXType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LengthYtype:
    class Meta:
        name = "lengthYType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LetRingFontFaceType:
    class Meta:
        name = "letRingFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LevelType:
    class Meta:
        name = "levelType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LhGuitarFingeringFontFaceType:
    class Meta:
        name = "lhGuitarFingeringFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LhGuitarFingeringFontSizeType:
    class Meta:
        name = "lhGuitarFingeringFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LhGuitarFingeringFramePaddingType:
    class Meta:
        name = "lhGuitarFingeringFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LhGuitarFingeringFrameRoundType:
    class Meta:
        name = "lhGuitarFingeringFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LhGuitarFingeringFrameWidthType:
    class Meta:
        name = "lhGuitarFingeringFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LidType:
    class Meta:
        name = "lidType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LineColorType:
    class Meta:
        name = "lineColorType"

    b: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    g: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    r: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LineDistanceType:
    class Meta:
        name = "lineDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LineLenType:
    class Meta:
        name = "lineLenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LineStyleType:
    class Meta:
        name = "lineStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LineTypeType:
    class Meta:
        name = "lineTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LineType1:
    class Meta:
        name = "lineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LineVisibleType:
    class Meta:
        name = "lineVisibleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LineWidthType:
    class Meta:
        name = "lineWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LinesThroughType:
    class Meta:
        name = "linesThroughType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LinesType:
    class Meta:
        name = "linesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LinkPathType:
    class Meta:
        name = "linkPathType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LinkedMainType:
    class Meta:
        name = "linkedMainType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LinkedToType:
    class Meta:
        name = "linkedToType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LoadType:
    class Meta:
        name = "loadType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LockAspectRatioType:
    class Meta:
        name = "lockAspectRatioType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LongInstrumentAlignType:
    class Meta:
        name = "longInstrumentAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LongInstrumentFontFaceType:
    class Meta:
        name = "longInstrumentFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LongInstrumentFontSizeType:
    class Meta:
        name = "longInstrumentFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LongInstrumentFramePaddingType:
    class Meta:
        name = "longInstrumentFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LongInstrumentFrameWidthType:
    class Meta:
        name = "longInstrumentFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LowerCaseBassNotesType:
    class Meta:
        name = "lowerCaseBassNotesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LowerCaseMinorChordsType:
    class Meta:
        name = "lowerCaseMinorChordsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricFontType:
    class Meta:
        name = "lyric-fontType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricLanguageType:
    class Meta:
        name = "lyric-languageType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricType2:
    class Meta:
        name = "lyricType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricistFontFaceType:
    class Meta:
        name = "lyricistFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricistFontSizeType:
    class Meta:
        name = "lyricistFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricistFramePaddingType:
    class Meta:
        name = "lyricistFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricistFrameRoundType:
    class Meta:
        name = "lyricistFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricistFrameWidthType:
    class Meta:
        name = "lyricistFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricistType:
    class Meta:
        name = "lyricistType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsDashForceType:
    class Meta:
        name = "lyricsDashForceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsDashMaxLegthType:
    class Meta:
        name = "lyricsDashMaxLegthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsDashYposRatioType:
    class Meta:
        name = "lyricsDashYposRatioType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsDistanceType:
    class Meta:
        name = "lyricsDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsEvenFontFaceType:
    class Meta:
        name = "lyricsEvenFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsEvenFontSizeType:
    class Meta:
        name = "lyricsEvenFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsEvenFramePaddingType:
    class Meta:
        name = "lyricsEvenFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsEvenFrameWidthType:
    class Meta:
        name = "lyricsEvenFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsEvenOffsetType:
    class Meta:
        name = "lyricsEvenOffsetType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsLineThicknessType:
    class Meta:
        name = "lyricsLineThicknessType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsMinBottomDistanceType:
    class Meta:
        name = "lyricsMinBottomDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsMinDistanceType:
    class Meta:
        name = "lyricsMinDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsOddFontFaceType:
    class Meta:
        name = "lyricsOddFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsOddFontSizeType:
    class Meta:
        name = "lyricsOddFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsOddFramePaddingType:
    class Meta:
        name = "lyricsOddFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsOddFrameWidthType:
    class Meta:
        name = "lyricsOddFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsOddOffsetType:
    class Meta:
        name = "lyricsOddOffsetType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsPosBelowType:
    class Meta:
        name = "lyricsPosBelowType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LyricsSettingsType:
    class Meta:
        name = "lyricsSettingsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MagIdxType2:
    class Meta:
        name = "magIdxType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MagType2:
    class Meta:
        name = "magType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MarkIrregularMeasuresType:
    class Meta:
        name = "markIrregularMeasuresType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MarkType:
    class Meta:
        name = "markType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MarkerType2:
    class Meta:
        name = "markerType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MaxChordShiftAboveType:
    class Meta:
        name = "maxChordShiftAboveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MaxChordShiftBelowType:
    class Meta:
        name = "maxChordShiftBelowType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MaxFretShiftAboveType:
    class Meta:
        name = "maxFretShiftAboveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MaxFretShiftBelowType:
    class Meta:
        name = "maxFretShiftBelowType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MaxHarmonyBarDistanceType:
    class Meta:
        name = "maxHarmonyBarDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MaxPageFillSpreadType:
    class Meta:
        name = "maxPageFillSpreadType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MaxPitchAtype:
    class Meta:
        name = "maxPitchAType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MaxPitchPtype:
    class Meta:
        name = "maxPitchPType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MaxPitchType:
    class Meta:
        name = "maxPitchType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MaxSystemDistanceType:
    class Meta:
        name = "maxSystemDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureStyleType:
    class Meta:
        name = "measure-styleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberAlignType:
    class Meta:
        name = "measureNumberAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberAllStaffsType:
    class Meta:
        name = "measureNumberAllStaffsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberFontFaceType:
    class Meta:
        name = "measureNumberFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberFontSizeType:
    class Meta:
        name = "measureNumberFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberFontSpatiumDependentType:
    class Meta:
        name = "measureNumberFontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberFontStyleType:
    class Meta:
        name = "measureNumberFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberFramePaddingType:
    class Meta:
        name = "measureNumberFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberFrameWidthType:
    class Meta:
        name = "measureNumberFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberHplacementType:
    class Meta:
        name = "measureNumberHPlacementType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberIntervalType:
    class Meta:
        name = "measureNumberIntervalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberModeType:
    class Meta:
        name = "measureNumberModeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberOffsetType:
    class Meta:
        name = "measureNumberOffsetType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberPosAboveType:
    class Meta:
        name = "measureNumberPosAboveType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberPosBelowType:
    class Meta:
        name = "measureNumberPosBelowType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberSystemType:
    class Meta:
        name = "measureNumberSystemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureNumberVplacementType:
    class Meta:
        name = "measureNumberVPlacementType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureSpacingType:
    class Meta:
        name = "measureSpacingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasureType2:
    class Meta:
        name = "measureType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MeasuresType:
    class Meta:
        name = "measuresType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MergeMatchingRestsType:
    class Meta:
        name = "mergeMatchingRestsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetaTagType:
    class Meta:
        name = "metaTagType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetaType2:
    class Meta:
        name = "metaType"

    content_attribute: None | str = field(
        default=None,
        metadata={
            "name": "content",
            "type": "Attribute",
        },
    )
    http_equiv: None | str = field(
        default=None,
        metadata={
            "name": "http-equiv",
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetafileType:
    class Meta:
        name = "metafileType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetronomeNoteType:
    class Meta:
        name = "metronome-noteType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetronomeRelationType:
    class Meta:
        name = "metronome-relationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetronomeFontFaceType:
    class Meta:
        name = "metronomeFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetronomeFontSizeType:
    class Meta:
        name = "metronomeFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetronomeFontStyleType:
    class Meta:
        name = "metronomeFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetronomeFramePaddingType:
    class Meta:
        name = "metronomeFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetronomeFrameWidthType:
    class Meta:
        name = "metronomeFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MetronomeType:
    class Meta:
        name = "metronomeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MiType:
    class Meta:
        name = "miType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MidiBankType:
    class Meta:
        name = "midi-bankType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MidiChannelType1:
    class Meta:
        name = "midi-channelType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MidiDeviceType:
    class Meta:
        name = "midi-deviceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MidiInstrumentType:
    class Meta:
        name = "midi-instrumentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MidiProgramType1:
    class Meta:
        name = "midi-programType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MidiUnpitchedType:
    class Meta:
        name = "midi-unpitchedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MidiChannelType2:
    class Meta:
        name = "midiChannelType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MidiPortType:
    class Meta:
        name = "midiPortType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MidiProgramType2:
    class Meta:
        name = "midiProgramType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MillimetersType:
    class Meta:
        name = "millimetersType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MinDistanceType:
    class Meta:
        name = "minDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MinEmptyMeasuresType:
    class Meta:
        name = "minEmptyMeasuresType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MinHarmonyDistanceType:
    class Meta:
        name = "minHarmonyDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MinMmrestWidthType:
    class Meta:
        name = "minMMRestWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MinMeasureWidthType:
    class Meta:
        name = "minMeasureWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MinNoteDistanceType:
    class Meta:
        name = "minNoteDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MinPitchAtype:
    class Meta:
        name = "minPitchAType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MinPitchPtype:
    class Meta:
        name = "minPitchPType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MinPitchType:
    class Meta:
        name = "minPitchType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MinSystemDistanceType:
    class Meta:
        name = "minSystemDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MinimStyleType:
    class Meta:
        name = "minimStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MirrorType:
    class Meta:
        name = "mirrorType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MiscellaneousType:
    class Meta:
        name = "miscellaneousType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MmRestNumberPosType:
    class Meta:
        name = "mmRestNumberPosType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MmRestRangeBracketTypeType:
    class Meta:
        name = "mmRestRangeBracketTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MmRestRangeFontSizeType:
    class Meta:
        name = "mmRestRangeFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MmRestRangeVplacementType:
    class Meta:
        name = "mmRestRangeVPlacementType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MmRestShowMeasureNumberRangeType:
    class Meta:
        name = "mmRestShowMeasureNumberRangeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ModeType:
    class Meta:
        name = "modeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MordentType:
    class Meta:
        name = "mordentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MoreElementsType:
    class Meta:
        name = "moreElementsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MoveType:
    class Meta:
        name = "moveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MovementNumberType1:
    class Meta:
        name = "movement-numberType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MovementTitleType1:
    class Meta:
        name = "movement-titleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MovementNumberType2:
    class Meta:
        name = "movementNumberType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MovementTitleType2:
    class Meta:
        name = "movementTitleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MultiMeasureRestType:
    class Meta:
        name = "multiMeasureRestType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MultipleRestType:
    class Meta:
        name = "multiple-restType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MusicFontType:
    class Meta:
        name = "music-fontType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MusicXmlidType:
    class Meta:
        name = "musicXMLidType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MusicalSymbolFontType:
    class Meta:
        name = "musicalSymbolFontType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MusicalTextFontType:
    class Meta:
        name = "musicalTextFontType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MuteType:
    class Meta:
        name = "muteType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NashvilleNumberFontFaceType:
    class Meta:
        name = "nashvilleNumberFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NashvilleNumberFontSizeType:
    class Meta:
        name = "nashvilleNumberFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NaturalType:
    class Meta:
        name = "naturalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NeverHideType:
    class Meta:
        name = "neverHideType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoOffsetType:
    class Meta:
        name = "noOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoStemType:
    class Meta:
        name = "noStemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoType:
    class Meta:
        name = "noType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Nom1Type:
    class Meta:
        name = "nom1Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Nom2Type:
    class Meta:
        name = "nom2Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Nom3Type:
    class Meta:
        name = "nom3Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Nom4Type:
    class Meta:
        name = "nom4Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NomType:
    class Meta:
        name = "nomType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NonArpeggiateType:
    class Meta:
        name = "non-arpeggiateType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NormalDotType:
    class Meta:
        name = "normal-dotType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NormalNotesType1:
    class Meta:
        name = "normal-notesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NormalTypeType:
    class Meta:
        name = "normal-typeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NormalNotesType2:
    class Meta:
        name = "normalNotesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NormalType1:
    class Meta:
        name = "normalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NotationType:
    class Meta:
        name = "notationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NotationsType:
    class Meta:
        name = "notationsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoteOffType2:
    class Meta:
        name = "note-offType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoteOnType2:
    class Meta:
        name = "note-onType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoteBarDistanceType:
    class Meta:
        name = "noteBarDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoteObjectsType:
    class Meta:
        name = "noteObjectsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoteType2:
    class Meta:
        name = "noteType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoteheadSchemeType:
    class Meta:
        name = "noteheadSchemeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoteheadType:
    class Meta:
        name = "noteheadType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NotelinesType:
    class Meta:
        name = "notelinesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NotesType:
    class Meta:
        name = "notesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NumberTypeType:
    class Meta:
        name = "numberTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NumbersOnlyType:
    class Meta:
        name = "numbersOnlyType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class O1Type:
    class Meta:
        name = "o1Type"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class O2Type:
    class Meta:
        name = "o2Type"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class O3Type:
    class Meta:
        name = "o3Type"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class O4Type:
    class Meta:
        name = "o4Type"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OctaveChangeType:
    class Meta:
        name = "octave-changeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OctaveShiftType:
    class Meta:
        name = "octave-shiftType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OctaveType:
    class Meta:
        name = "octaveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OddFooterCtype:
    class Meta:
        name = "oddFooterCType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OddFooterLtype:
    class Meta:
        name = "oddFooterLType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OddFooterRtype:
    class Meta:
        name = "oddFooterRType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OddFooterType:
    class Meta:
        name = "oddFooterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OddHeaderCtype:
    class Meta:
        name = "oddHeaderCType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OddHeaderLtype:
    class Meta:
        name = "oddHeaderLType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OddHeaderRtype:
    class Meta:
        name = "oddHeaderRType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OddHeaderType:
    class Meta:
        name = "oddHeaderType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Off1Type:
    class Meta:
        name = "off1Type"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Off2Type:
    class Meta:
        name = "off2Type"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OffTimeOffsetType:
    class Meta:
        name = "offTimeOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OffTimeTypeType:
    class Meta:
        name = "offTimeTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OffsetTypeType:
    class Meta:
        name = "offsetTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OffsetType1:
    class Meta:
        name = "offsetType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OnLinesType:
    class Meta:
        name = "onLinesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OnNoteType:
    class Meta:
        name = "onNoteType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OnTimeOffsetType:
    class Meta:
        name = "onTimeOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OnTimeTypeType:
    class Meta:
        name = "onTimeTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OntimeType1:
    class Meta:
        name = "ontimeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OpenStringType:
    class Meta:
        name = "open-stringType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OrientationType:
    class Meta:
        name = "orientationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OrnamentStyleType:
    class Meta:
        name = "ornamentStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OrnamentsType:
    class Meta:
        name = "ornamentsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OtherDynamicsType:
    class Meta:
        name = "other-dynamicsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OttavaFontFaceType:
    class Meta:
        name = "ottavaFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OttavaFontItalicType:
    class Meta:
        name = "ottavaFontItalicType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OttavaFontSizeType:
    class Meta:
        name = "ottavaFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OttavaFontStyleType:
    class Meta:
        name = "ottavaFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OttavaFramePaddingType:
    class Meta:
        name = "ottavaFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OttavaFrameWidthType:
    class Meta:
        name = "ottavaFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OttavaHookAboveType:
    class Meta:
        name = "ottavaHookAboveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OttavaHookBelowType:
    class Meta:
        name = "ottavaHookBelowType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OttavaHookType:
    class Meta:
        name = "ottavaHookType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OttavaLineWidthType:
    class Meta:
        name = "ottavaLineWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class P1Type:
    class Meta:
        name = "p1Type"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class P2Type:
    class Meta:
        name = "p2Type"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PPitchRangeType:
    class Meta:
        name = "pPitchRangeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PaddingWidthStype:
    class Meta:
        name = "paddingWidthSType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PaddingWidthType:
    class Meta:
        name = "paddingWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageHeightType1:
    class Meta:
        name = "page-heightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageOffsetType:
    class Meta:
        name = "page-offsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageWidthType1:
    class Meta:
        name = "page-widthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageEvenBottomMarginType:
    class Meta:
        name = "pageEvenBottomMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageEvenLeftMarginType:
    class Meta:
        name = "pageEvenLeftMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageEvenTopMarginType:
    class Meta:
        name = "pageEvenTopMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageFillLimitType:
    class Meta:
        name = "pageFillLimitType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageFormatType:
    class Meta:
        name = "pageFormatType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageHeightType2:
    class Meta:
        name = "pageHeightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageNumberOddEvenType:
    class Meta:
        name = "pageNumberOddEvenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageObjectsType:
    class Meta:
        name = "pageObjectsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageOddBottomMarginType:
    class Meta:
        name = "pageOddBottomMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageOddLeftMarginType:
    class Meta:
        name = "pageOddLeftMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageOddTopMarginType:
    class Meta:
        name = "pageOddTopMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PagePrintableWidthType:
    class Meta:
        name = "pagePrintableWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageTwosidedType:
    class Meta:
        name = "pageTwosidedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageType2:
    class Meta:
        name = "pageType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PageWidthType2:
    class Meta:
        name = "pageWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PagesType:
    class Meta:
        name = "pagesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PalmMuteFontFaceType:
    class Meta:
        name = "palmMuteFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PanType:
    class Meta:
        name = "panType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ParenthesisRoundClosedType:
    class Meta:
        name = "parenthesisRoundClosedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ParenthesisRoundOpenType:
    class Meta:
        name = "parenthesisRoundOpenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ParenthesisSquareClosedType:
    class Meta:
        name = "parenthesisSquareClosedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ParenthesisSquareOpenType:
    class Meta:
        name = "parenthesisSquareOpenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartAbbreviationDisplayType:
    class Meta:
        name = "part-abbreviation-displayType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartAbbreviationType:
    class Meta:
        name = "part-abbreviationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartGroupType:
    class Meta:
        name = "part-groupType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartListType:
    class Meta:
        name = "part-listType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartNameDisplayType:
    class Meta:
        name = "part-name-displayType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartNameType:
    class Meta:
        name = "part-nameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartInstrumentFontFaceType:
    class Meta:
        name = "partInstrumentFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartInstrumentFontSizeType:
    class Meta:
        name = "partInstrumentFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartInstrumentFramePaddingType:
    class Meta:
        name = "partInstrumentFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartInstrumentFrameRoundType:
    class Meta:
        name = "partInstrumentFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartInstrumentFrameWidthType:
    class Meta:
        name = "partInstrumentFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartType2:
    class Meta:
        name = "partType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PathType2:
    class Meta:
        name = "pathType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PauseType:
    class Meta:
        name = "pauseType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PedalFontFaceType:
    class Meta:
        name = "pedalFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PedalFramePaddingType:
    class Meta:
        name = "pedalFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PedalFrameWidthType:
    class Meta:
        name = "pedalFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PedalLineWidthType:
    class Meta:
        name = "pedalLineWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PedalPosBelowType:
    class Meta:
        name = "pedalPosBelowType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PedalType2:
    class Meta:
        name = "pedalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PedalYtype:
    class Meta:
        name = "pedalYType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PerMinuteType:
    class Meta:
        name = "per-minuteType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PitchType:
    class Meta:
        name = "pitchType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlacementType:
    class Meta:
        name = "placementType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlatformType:
    class Meta:
        name = "platformType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlayModeType:
    class Meta:
        name = "playModeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlayRepeatsType:
    class Meta:
        name = "playRepeatsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlayType:
    class Meta:
        name = "playType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlayUntilType:
    class Meta:
        name = "playUntilType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlaybackVoice1Type:
    class Meta:
        name = "playbackVoice1Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlaybackVoice2Type:
    class Meta:
        name = "playbackVoice2Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlaybackVoice3Type:
    class Meta:
        name = "playbackVoice3Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlaybackVoice4Type:
    class Meta:
        name = "playbackVoice4Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PlopType:
    class Meta:
        name = "plopType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PluckType:
    class Meta:
        name = "pluckType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PoetType:
    class Meta:
        name = "poetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PointType:
    class Meta:
        name = "pointType"

    pitch: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    time: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vibrato: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PolygonType:
    class Meta:
        name = "polygonType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PosType:
    class Meta:
        name = "posType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PreferSharpFlatType:
    class Meta:
        name = "preferSharpFlatType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PrefixType:
    class Meta:
        name = "prefixType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PrintType:
    class Meta:
        name = "printType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ProgramRevisionType:
    class Meta:
        name = "programRevisionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ProgramType2:
    class Meta:
        name = "programType"

    channel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tick: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ProgramVersionType:
    class Meta:
        name = "programVersionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PropertyDistanceHeadType:
    class Meta:
        name = "propertyDistanceHeadType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PropertyDistanceStemType:
    class Meta:
        name = "propertyDistanceStemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PropertyDistanceType:
    class Meta:
        name = "propertyDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class QuarterType:
    class Meta:
        name = "quarterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ReType:
    class Meta:
        name = "reType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RectangleType:
    class Meta:
        name = "rectangleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RefType:
    class Meta:
        name = "refType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RehearsalMarkAlignType:
    class Meta:
        name = "rehearsalMarkAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RehearsalMarkFontBoldType:
    class Meta:
        name = "rehearsalMarkFontBoldType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RehearsalMarkFontFaceType:
    class Meta:
        name = "rehearsalMarkFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RehearsalMarkFontSizeType:
    class Meta:
        name = "rehearsalMarkFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RehearsalMarkFramePaddingType:
    class Meta:
        name = "rehearsalMarkFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RehearsalMarkFrameRoundType:
    class Meta:
        name = "rehearsalMarkFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RehearsalMarkFrameWidthType:
    class Meta:
        name = "rehearsalMarkFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RehearsalType:
    class Meta:
        name = "rehearsalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RelTempoType:
    class Meta:
        name = "relTempoType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RenderBaseType:
    class Meta:
        name = "renderBaseType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RenderFunctionType:
    class Meta:
        name = "renderFunctionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RenderRootType:
    class Meta:
        name = "renderRootType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RenderType:
    class Meta:
        name = "renderType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatBarTipsType:
    class Meta:
        name = "repeatBarTipsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatBarlineDotSeparationType:
    class Meta:
        name = "repeatBarlineDotSeparationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatLeftAlignType:
    class Meta:
        name = "repeatLeftAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatLeftFontFaceType:
    class Meta:
        name = "repeatLeftFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatLeftFontSizeType:
    class Meta:
        name = "repeatLeftFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatLeftFramePaddingType:
    class Meta:
        name = "repeatLeftFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatLeftFrameRoundType:
    class Meta:
        name = "repeatLeftFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatLeftFrameWidthType:
    class Meta:
        name = "repeatLeftFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatRightAlignType:
    class Meta:
        name = "repeatRightAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatRightFontFaceType:
    class Meta:
        name = "repeatRightFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatRightFontSizeType:
    class Meta:
        name = "repeatRightFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatRightFramePaddingType:
    class Meta:
        name = "repeatRightFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatRightFrameRoundType:
    class Meta:
        name = "repeatRightFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatRightFrameWidthType:
    class Meta:
        name = "repeatRightFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RepeatType:
    class Meta:
        name = "repeatType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RestType2:
    class Meta:
        name = "restType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ReverbType:
    class Meta:
        name = "reverbType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RevisionType2:
    class Meta:
        name = "revisionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RhGuitarFingeringFontFaceType:
    class Meta:
        name = "rhGuitarFingeringFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RhGuitarFingeringFontSizeType:
    class Meta:
        name = "rhGuitarFingeringFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RhGuitarFingeringFontStyleType:
    class Meta:
        name = "rhGuitarFingeringFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RhGuitarFingeringFramePaddingType:
    class Meta:
        name = "rhGuitarFingeringFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RhGuitarFingeringFrameRoundType:
    class Meta:
        name = "rhGuitarFingeringFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RhGuitarFingeringFrameWidthType:
    class Meta:
        name = "rhGuitarFingeringFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RichTextType:
    class Meta:
        name = "richTextType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RightMarginType1:
    class Meta:
        name = "right-marginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RightMarginType2:
    class Meta:
        name = "rightMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RightParenType:
    class Meta:
        name = "rightParenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RightsType:
    class Meta:
        name = "rightsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RoleType:
    class Meta:
        name = "roleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RootAlterType:
    class Meta:
        name = "root-alterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RootStepType:
    class Meta:
        name = "root-stepType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RootCaseType:
    class Meta:
        name = "rootCaseType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RootType:
    class Meta:
        name = "rootType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RootfileType:
    class Meta:
        name = "rootfileType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RootfilesType:
    class Meta:
        name = "rootfilesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RunTableType:
    class Meta:
        name = "run-tableType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RunsType:
    class Meta:
        name = "runsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RxoffsetType:
    class Meta:
        name = "rxoffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RyoffsetType:
    class Meta:
        name = "ryoffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SType:
    class Meta:
        name = "sType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ScalingType:
    class Meta:
        name = "scalingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ScoopType:
    class Meta:
        name = "scoopType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ScoreInstrumentType:
    class Meta:
        name = "score-instrumentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ScorePartType:
    class Meta:
        name = "score-partType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ScorePartwiseType:
    class Meta:
        name = "score-partwiseType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ScoreType2:
    class Meta:
        name = "scoreType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SectionPauseType:
    class Meta:
        name = "sectionPauseType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SegDeltaType:
    class Meta:
        name = "segDeltaType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SegnoType:
    class Meta:
        name = "segnoType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SelectedType:
    class Meta:
        name = "selectedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SeqType:
    class Meta:
        name = "seqType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SharpType:
    class Meta:
        name = "sharpType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SheetType:
    class Meta:
        name = "sheetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortNameType1:
    class Meta:
        name = "short-nameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortInstrumentFontFaceType:
    class Meta:
        name = "shortInstrumentFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortInstrumentFontSizeType:
    class Meta:
        name = "shortInstrumentFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortInstrumentFramePaddingType:
    class Meta:
        name = "shortInstrumentFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortInstrumentFrameWidthType:
    class Meta:
        name = "shortInstrumentFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortStemProgressionType:
    class Meta:
        name = "shortStemProgressionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortcutType2:
    class Meta:
        name = "shortcutType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortenStemType:
    class Meta:
        name = "shortenStemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortestStemType:
    class Meta:
        name = "shortestStemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowBackTiedType:
    class Meta:
        name = "showBackTiedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowCourtesyClefType:
    class Meta:
        name = "showCourtesyClefType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowCourtesySigType:
    class Meta:
        name = "showCourtesySigType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowCourtesyType:
    class Meta:
        name = "showCourtesyType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowFooterType:
    class Meta:
        name = "showFooterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowFramesType:
    class Meta:
        name = "showFramesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowHeaderType:
    class Meta:
        name = "showHeaderType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowIfSystemEmptyType:
    class Meta:
        name = "showIfSystemEmptyType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowInvisibleType:
    class Meta:
        name = "showInvisibleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowMarginsType:
    class Meta:
        name = "showMarginsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowMeasureNumberOneType:
    class Meta:
        name = "showMeasureNumberOneType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowMeasureNumberType:
    class Meta:
        name = "showMeasureNumberType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowNaturalsType:
    class Meta:
        name = "showNaturalsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowNutType:
    class Meta:
        name = "showNutType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowOmrType:
    class Meta:
        name = "showOmrType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowPageNumberOneType:
    class Meta:
        name = "showPageNumberOneType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowPageNumberType:
    class Meta:
        name = "showPageNumberType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowRestsType:
    class Meta:
        name = "showRestsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowTabFingeringType:
    class Meta:
        name = "showTabFingeringType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowType:
    class Meta:
        name = "showType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShowUnprintableType:
    class Meta:
        name = "showUnprintableType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SigDtype:
    class Meta:
        name = "sigDType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SigNtype1:
    class Meta:
        name = "sigNType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SignType2:
    class Meta:
        name = "signType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SingleNoteDynamicsType:
    class Meta:
        name = "singleNoteDynamicsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SizeIsSpatiumDependentType:
    class Meta:
        name = "sizeIsSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SizeIsSpatiumType:
    class Meta:
        name = "sizeIsSpatiumType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SizeType:
    class Meta:
        name = "sizeType"

    h: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    w: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SlashStyleType:
    class Meta:
        name = "slashStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SlashType:
    class Meta:
        name = "slashType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SlashedType:
    class Meta:
        name = "slashedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SlideType:
    class Meta:
        name = "slideType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SlurEndWidthType:
    class Meta:
        name = "slurEndWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SlurGateTimeType:
    class Meta:
        name = "slurGateTimeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SlurMidWidthType:
    class Meta:
        name = "slurMidWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SlurType2:
    class Meta:
        name = "slurType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SmallClefMagType:
    class Meta:
        name = "smallClefMagType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SmallNoteMagType:
    class Meta:
        name = "smallNoteMagType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SmallStaffMagType:
    class Meta:
        name = "smallStaffMagType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SmallStaffType:
    class Meta:
        name = "smallStaffType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SmallType:
    class Meta:
        name = "smallType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SoType:
    class Meta:
        name = "soType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SoftwareType:
    class Meta:
        name = "softwareType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SoloType:
    class Meta:
        name = "soloType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SoloistType:
    class Meta:
        name = "soloistType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SoloistsType:
    class Meta:
        name = "soloistsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SoundType:
    class Meta:
        name = "soundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SourceType:
    class Meta:
        name = "sourceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SpaceType:
    class Meta:
        name = "spaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SpacingType:
    class Meta:
        name = "spacingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SpanFromOffsetType:
    class Meta:
        name = "spanFromOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SpanToOffsetType:
    class Meta:
        name = "spanToOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SpanType:
    class Meta:
        name = "spanType"

    from_value: None | str = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    to: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SpatiumSizeDependentType:
    class Meta:
        name = "spatiumSizeDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SpatiumType2:
    class Meta:
        name = "spatiumType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SquareType:
    class Meta:
        name = "squareType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaccatoGateTimeType:
    class Meta:
        name = "staccatoGateTimeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StackType:
    class Meta:
        name = "stackType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffDetailsType:
    class Meta:
        name = "staff-detailsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffDistanceType1:
    class Meta:
        name = "staff-distanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffLayoutType1:
    class Meta:
        name = "staff-layoutType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffLinesType1:
    class Meta:
        name = "staff-linesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffTuningType:
    class Meta:
        name = "staff-tuningType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffAlignType:
    class Meta:
        name = "staffAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffDistanceType2:
    class Meta:
        name = "staffDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffFontFaceType:
    class Meta:
        name = "staffFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffFontItalicType:
    class Meta:
        name = "staffFontItalicType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffFontSizeType:
    class Meta:
        name = "staffFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffFramePaddingType:
    class Meta:
        name = "staffFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffFrameRoundType:
    class Meta:
        name = "staffFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffFrameWidthType:
    class Meta:
        name = "staffFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffLayoutType2:
    class Meta:
        name = "staffLayoutType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffLineWidthType:
    class Meta:
        name = "staffLineWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffLinesType2:
    class Meta:
        name = "staffLinesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffLowerBorderType:
    class Meta:
        name = "staffLowerBorderType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffMoveType:
    class Meta:
        name = "staffMoveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffOffsetType:
    class Meta:
        name = "staffOffsetType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffPlacementType:
    class Meta:
        name = "staffPlacementType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffPosAboveType:
    class Meta:
        name = "staffPosAboveType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffPosBelowType:
    class Meta:
        name = "staffPosBelowType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffTextMinDistanceType:
    class Meta:
        name = "staffTextMinDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffTextPosAboveType:
    class Meta:
        name = "staffTextPosAboveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffType3:
    class Meta:
        name = "staffType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StaffUpperBorderType:
    class Meta:
        name = "staffUpperBorderType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StafflinesType3:
    class Meta:
        name = "stafflinesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StafftypeType2:
    class Meta:
        name = "stafftypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StartBarlineMultipleType:
    class Meta:
        name = "startBarlineMultipleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StartBarlineSingleType:
    class Meta:
        name = "startBarlineSingleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StartRepeatType:
    class Meta:
        name = "startRepeatType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StartTrackType:
    class Meta:
        name = "startTrackType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StartWithLongNamesType:
    class Meta:
        name = "startWithLongNamesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StartWithMeasureOneType:
    class Meta:
        name = "startWithMeasureOneType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StavesType:
    class Meta:
        name = "stavesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StdType:
    class Meta:
        name = "stdType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemDir1Type:
    class Meta:
        name = "stemDir1Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemDir2Type:
    class Meta:
        name = "stemDir2Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemDir3Type:
    class Meta:
        name = "stemDir3Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemDir4Type:
    class Meta:
        name = "stemDir4Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemDirType:
    class Meta:
        name = "stemDirType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemHeightType:
    class Meta:
        name = "stemHeightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemType2:
    class Meta:
        name = "stemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemWidthType:
    class Meta:
        name = "stemWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemlessType:
    class Meta:
        name = "stemlessType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemsDownType:
    class Meta:
        name = "stemsDownType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StemsThroughType:
    class Meta:
        name = "stemsThroughType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StepOffsetType:
    class Meta:
        name = "stepOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StepType:
    class Meta:
        name = "stepType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StickingFontFaceType:
    class Meta:
        name = "stickingFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StraightType:
    class Meta:
        name = "straightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StretchDtype:
    class Meta:
        name = "stretchDType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StretchNtype:
    class Meta:
        name = "stretchNType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StretchType:
    class Meta:
        name = "stretchType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StringNumberFontFaceType:
    class Meta:
        name = "stringNumberFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StringNumberFontSizeType:
    class Meta:
        name = "stringNumberFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StringNumberOffsetType:
    class Meta:
        name = "stringNumberOffsetType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StringsType:
    class Meta:
        name = "stringsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StrokeStyleType:
    class Meta:
        name = "strokeStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StrongAccentType:
    class Meta:
        name = "strong-accentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StyleType2:
    class Meta:
        name = "styleType"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SubTitleFontFaceType:
    class Meta:
        name = "subTitleFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SubTitleFontSizeType:
    class Meta:
        name = "subTitleFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SubTitleFontSpatiumDependentType:
    class Meta:
        name = "subTitleFontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SubTitleFramePaddingType:
    class Meta:
        name = "subTitleFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SubTitleFrameRoundType:
    class Meta:
        name = "subTitleFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SubTitleFrameWidthType:
    class Meta:
        name = "subTitleFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SubtypeType:
    class Meta:
        name = "subtypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SuffixType:
    class Meta:
        name = "suffixType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SupType:
    class Meta:
        name = "supType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SupportsType:
    class Meta:
        name = "supportsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SwingRatioType:
    class Meta:
        name = "swingRatioType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SwingType2:
    class Meta:
        name = "swingType"

    ratio: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    unit: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SwingUnitType:
    class Meta:
        name = "swingUnitType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SyllabicType:
    class Meta:
        name = "syllabicType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SymType:
    class Meta:
        name = "symType"

    code: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SymbolRepeatType:
    class Meta:
        name = "symbolRepeatType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SymbolType2:
    class Meta:
        name = "symbolType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SyntiType:
    class Meta:
        name = "syntiType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SysInitBarLineTypeType:
    class Meta:
        name = "sysInitBarLineTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SysexType:
    class Meta:
        name = "sysexType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemDistanceType1:
    class Meta:
        name = "system-distanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemDividersType:
    class Meta:
        name = "system-dividersType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemLayoutType:
    class Meta:
        name = "system-layoutType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemMarginsType:
    class Meta:
        name = "system-marginsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemAlignType:
    class Meta:
        name = "systemAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemDistanceType2:
    class Meta:
        name = "systemDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemFlagType:
    class Meta:
        name = "systemFlagType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemFontFaceType:
    class Meta:
        name = "systemFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemFontSizeType:
    class Meta:
        name = "systemFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemFrameDistanceType:
    class Meta:
        name = "systemFrameDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemFramePaddingType:
    class Meta:
        name = "systemFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemFrameRoundType:
    class Meta:
        name = "systemFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemFrameWidthType:
    class Meta:
        name = "systemFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemOffsetType:
    class Meta:
        name = "systemOffsetType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemType2:
    class Meta:
        name = "systemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SystemsType:
    class Meta:
        name = "systemsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TabType:
    class Meta:
        name = "tabType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TagType:
    class Meta:
        name = "tagType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TechnicalType:
    class Meta:
        name = "technicalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TempoFontBoldType:
    class Meta:
        name = "tempoFontBoldType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TempoFontFaceType:
    class Meta:
        name = "tempoFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TempoFontSizeType:
    class Meta:
        name = "tempoFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TempoFontStyleType:
    class Meta:
        name = "tempoFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TempoFramePaddingType:
    class Meta:
        name = "tempoFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TempoFrameRoundType:
    class Meta:
        name = "tempoFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TempoFrameWidthType:
    class Meta:
        name = "tempoFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TempoOffsetType:
    class Meta:
        name = "tempoOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TempoPosAboveType:
    class Meta:
        name = "tempoPosAboveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TempoType2:
    class Meta:
        name = "tempoType"

    tick: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TenthsType:
    class Meta:
        name = "tenthsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TextDtype:
    class Meta:
        name = "textDType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TextLineFontFaceType:
    class Meta:
        name = "textLineFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TextLineFontSizeType:
    class Meta:
        name = "textLineFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TextLineFramePaddingType:
    class Meta:
        name = "textLineFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TextLineFrameWidthType:
    class Meta:
        name = "textLineFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TextLineTextAlignType:
    class Meta:
        name = "textLineTextAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TextNtype:
    class Meta:
        name = "textNType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TiType:
    class Meta:
        name = "tiType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Tick2Type:
    class Meta:
        name = "tick2Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TickOffsetType:
    class Meta:
        name = "tickOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TickType:
    class Meta:
        name = "tickType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TicklenType:
    class Meta:
        name = "ticklenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TicksType:
    class Meta:
        name = "ticksType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TicksFType:
    class Meta:
        name = "ticks_fType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TieType2:
    class Meta:
        name = "tieType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TiedType:
    class Meta:
        name = "tiedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TimeModificationType:
    class Meta:
        name = "time-modificationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TimeSignType:
    class Meta:
        name = "timeSignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TimeStretchType:
    class Meta:
        name = "timeStretchType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TimeType:
    class Meta:
        name = "timeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TimesigLeftMarginType:
    class Meta:
        name = "timesigLeftMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TimesigType2:
    class Meta:
        name = "timesigType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TitleFontFaceType:
    class Meta:
        name = "titleFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TitleFontSizeType:
    class Meta:
        name = "titleFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TitleFontSpatiumDependentType:
    class Meta:
        name = "titleFontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TitleFontStyleType:
    class Meta:
        name = "titleFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TitleFramePaddingType:
    class Meta:
        name = "titleFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TitleFrameRoundType:
    class Meta:
        name = "titleFrameRoundType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TitleFrameWidthType:
    class Meta:
        name = "titleFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TitleType:
    class Meta:
        name = "titleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TokenType:
    class Meta:
        name = "tokenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TopMarginType1:
    class Meta:
        name = "top-marginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TopSystemDistanceType:
    class Meta:
        name = "top-system-distanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TopAccidentalType:
    class Meta:
        name = "topAccidentalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TopGapType:
    class Meta:
        name = "topGapType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TopMarginType2:
    class Meta:
        name = "topMarginType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TopPitchType:
    class Meta:
        name = "topPitchType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TopTpcType:
    class Meta:
        name = "topTpcType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Tpc2Type:
    class Meta:
        name = "tpc2Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TpcType:
    class Meta:
        name = "tpcType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Track2Type:
    class Meta:
        name = "track2Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TrackNameType2:
    class Meta:
        name = "trackNameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TrackOffsetType:
    class Meta:
        name = "trackOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TrackType2:
    class Meta:
        name = "trackType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TrailingSpaceType:
    class Meta:
        name = "trailingSpaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TranslatorAlignType:
    class Meta:
        name = "translatorAlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TranslatorFontFaceType:
    class Meta:
        name = "translatorFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TranslatorFontSizeType:
    class Meta:
        name = "translatorFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TranslatorFramePaddingType:
    class Meta:
        name = "translatorFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TranslatorFrameWidthType:
    class Meta:
        name = "translatorFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TranslatorType:
    class Meta:
        name = "translatorType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TransposableType:
    class Meta:
        name = "transposableType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TransposeChromaticType:
    class Meta:
        name = "transposeChromaticType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TransposeDiatonicType:
    class Meta:
        name = "transposeDiatonicType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TransposeType:
    class Meta:
        name = "transposeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TransposingClefTypeType:
    class Meta:
        name = "transposingClefTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TransposingClefType1:
    class Meta:
        name = "transposingClefType"

    staff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TranspositionType:
    class Meta:
        name = "transpositionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TremoloType2:
    class Meta:
        name = "tremoloType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TriangleType:
    class Meta:
        name = "triangleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TrillMarkType:
    class Meta:
        name = "trill-markType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TrillPosAboveType:
    class Meta:
        name = "trillPosAboveType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TrillType2:
    class Meta:
        name = "trillType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TuningAlterType:
    class Meta:
        name = "tuning-alterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TuningOctaveType:
    class Meta:
        name = "tuning-octaveType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TuningStepType:
    class Meta:
        name = "tuning-stepType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TuningType:
    class Meta:
        name = "tuningType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletActualType:
    class Meta:
        name = "tuplet-actualType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletDotType:
    class Meta:
        name = "tuplet-dotType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletNormalType:
    class Meta:
        name = "tuplet-normalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletNumberType:
    class Meta:
        name = "tuplet-numberType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletTypeType:
    class Meta:
        name = "tuplet-typeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletBracketHookHeightType:
    class Meta:
        name = "tupletBracketHookHeightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletBracketWidthType:
    class Meta:
        name = "tupletBracketWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletFontFaceType:
    class Meta:
        name = "tupletFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletFontSizeType:
    class Meta:
        name = "tupletFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletFontStyleType:
    class Meta:
        name = "tupletFontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletFramePaddingType:
    class Meta:
        name = "tupletFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletFrameWidthType:
    class Meta:
        name = "tupletFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletNoteLeftDistanceType:
    class Meta:
        name = "tupletNoteLeftDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletOufOfStaffType:
    class Meta:
        name = "tupletOufOfStaffType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletStemLeftDistanceType:
    class Meta:
        name = "tupletStemLeftDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletType2:
    class Meta:
        name = "tupletType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletVheadDistanceType:
    class Meta:
        name = "tupletVHeadDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TupletVstemDistanceType:
    class Meta:
        name = "tupletVStemDistanceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TurnType:
    class Meta:
        name = "turnType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TypeType:
    class Meta:
        name = "typeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UnderlineType:
    class Meta:
        name = "underlineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UnpitchedType:
    class Meta:
        name = "unpitchedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UnsortedType:
    class Meta:
        name = "unsortedType"

    group: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UpType:
    class Meta:
        name = "upType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UpsideDownType:
    class Meta:
        name = "upsideDownType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UseDrumsetType:
    class Meta:
        name = "useDrumsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UseFrenchNoteNamesType:
    class Meta:
        name = "useFrenchNoteNamesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UseFullGermanNoteNamesType:
    class Meta:
        name = "useFullGermanNoteNamesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UseGermanNoteNamesType:
    class Meta:
        name = "useGermanNoteNamesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UseNumbersType:
    class Meta:
        name = "useNumbersType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UsePre36DefaultsType:
    class Meta:
        name = "usePre_3_6_defaultsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UseSolfeggioNoteNamesType:
    class Meta:
        name = "useSolfeggioNoteNamesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UseStandardNoteNamesType:
    class Meta:
        name = "useStandardNoteNamesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UseTablatureType:
    class Meta:
        name = "useTablatureType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UseTextLineType:
    class Meta:
        name = "useTextLineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User10FontFaceType:
    class Meta:
        name = "user10FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User11FontFaceType:
    class Meta:
        name = "user11FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User12FontFaceType:
    class Meta:
        name = "user12FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User1AlignType:
    class Meta:
        name = "user1AlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User1FontBoldType:
    class Meta:
        name = "user1FontBoldType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User1FontFaceType:
    class Meta:
        name = "user1FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User1FontSizeType:
    class Meta:
        name = "user1FontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User1FontSpatiumDependentType:
    class Meta:
        name = "user1FontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User1FramePaddingType:
    class Meta:
        name = "user1FramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User1FrameWidthType:
    class Meta:
        name = "user1FrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User1NameType:
    class Meta:
        name = "user1NameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User2AlignType:
    class Meta:
        name = "user2AlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User2FontFaceType:
    class Meta:
        name = "user2FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User2FontSizeType:
    class Meta:
        name = "user2FontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User2FontSpatiumDependentType:
    class Meta:
        name = "user2FontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User2FontStyleType:
    class Meta:
        name = "user2FontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User2FramePaddingType:
    class Meta:
        name = "user2FramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User2FrameWidthType:
    class Meta:
        name = "user2FrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User2NameType:
    class Meta:
        name = "user2NameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User3AlignType:
    class Meta:
        name = "user3AlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User3FontFaceType:
    class Meta:
        name = "user3FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User3FontSizeType:
    class Meta:
        name = "user3FontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User3FontSpatiumDependentType:
    class Meta:
        name = "user3FontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User3FramePaddingType:
    class Meta:
        name = "user3FramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User3FrameWidthType:
    class Meta:
        name = "user3FrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User3NameType:
    class Meta:
        name = "user3NameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User4AlignType:
    class Meta:
        name = "user4AlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User4FontFaceType:
    class Meta:
        name = "user4FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User4FontSizeType:
    class Meta:
        name = "user4FontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User4FontSpatiumDependentType:
    class Meta:
        name = "user4FontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User4FramePaddingType:
    class Meta:
        name = "user4FramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User4FrameWidthType:
    class Meta:
        name = "user4FrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User4NameType:
    class Meta:
        name = "user4NameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User5AlignType:
    class Meta:
        name = "user5AlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User5FontFaceType:
    class Meta:
        name = "user5FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User5FontSizeType:
    class Meta:
        name = "user5FontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User5FontSpatiumDependentType:
    class Meta:
        name = "user5FontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User5FramePaddingType:
    class Meta:
        name = "user5FramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User5FrameWidthType:
    class Meta:
        name = "user5FrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User5NameType:
    class Meta:
        name = "user5NameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User6AlignType:
    class Meta:
        name = "user6AlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User6FontFaceType:
    class Meta:
        name = "user6FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User6FontSizeType:
    class Meta:
        name = "user6FontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User6FontSpatiumDependentType:
    class Meta:
        name = "user6FontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User6FontStyleType:
    class Meta:
        name = "user6FontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User6FramePaddingType:
    class Meta:
        name = "user6FramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User6FrameWidthType:
    class Meta:
        name = "user6FrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User6NameType:
    class Meta:
        name = "user6NameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User7AlignType:
    class Meta:
        name = "user7AlignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User7FontFaceType:
    class Meta:
        name = "user7FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User7FontSizeType:
    class Meta:
        name = "user7FontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User7FontSpatiumDependentType:
    class Meta:
        name = "user7FontSpatiumDependentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User7FontStyleType:
    class Meta:
        name = "user7FontStyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User7FramePaddingType:
    class Meta:
        name = "user7FramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User7FrameWidthType:
    class Meta:
        name = "user7FrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User7NameType:
    class Meta:
        name = "user7NameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User8FontFaceType:
    class Meta:
        name = "user8FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class User9FontFaceType:
    class Meta:
        name = "user9FontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UserAccidentalType:
    class Meta:
        name = "userAccidentalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UserLen1Type:
    class Meta:
        name = "userLen1Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UserLen2Type:
    class Meta:
        name = "userLen2Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UserLenType:
    class Meta:
        name = "userLenType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ValType:
    class Meta:
        name = "valType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ValignType:
    class Meta:
        name = "valignType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VariantType:
    class Meta:
        name = "variantType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VariantsType:
    class Meta:
        name = "variantsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VeloChangeMethodType:
    class Meta:
        name = "veloChangeMethodType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VeloChangeSpeedType:
    class Meta:
        name = "veloChangeSpeedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VeloChangeType:
    class Meta:
        name = "veloChangeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VeloTypeType:
    class Meta:
        name = "veloTypeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VelocityType:
    class Meta:
        name = "velocityType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VerseType:
    class Meta:
        name = "verseType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VersionType:
    class Meta:
        name = "versionType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VerticalPosType:
    class Meta:
        name = "verticalPosType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VerticalType:
    class Meta:
        name = "verticalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VirtualInstrumentType:
    class Meta:
        name = "virtual-instrumentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VirtualLibraryType:
    class Meta:
        name = "virtual-libraryType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VirtualNameType:
    class Meta:
        name = "virtual-nameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VisibleType:
    class Meta:
        name = "visibleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoiceOffsetType:
    class Meta:
        name = "voiceOffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoicesType:
    class Meta:
        name = "voicesType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoicingType:
    class Meta:
        name = "voicingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoltaFontBoldType:
    class Meta:
        name = "voltaFontBoldType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoltaFontFaceType:
    class Meta:
        name = "voltaFontFaceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoltaFontSizeType:
    class Meta:
        name = "voltaFontSizeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoltaFramePaddingType:
    class Meta:
        name = "voltaFramePaddingType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoltaFrameWidthType:
    class Meta:
        name = "voltaFrameWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoltaLineWidthType:
    class Meta:
        name = "voltaLineWidthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoltaPosAboveType:
    class Meta:
        name = "voltaPosAboveType"

    x: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoltaType2:
    class Meta:
        name = "voltaType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VoltaYtype:
    class Meta:
        name = "voltaYType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VolumeType:
    class Meta:
        name = "volumeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VspacerDownType:
    class Meta:
        name = "vspacerDownType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VspacerFixedType:
    class Meta:
        name = "vspacerFixedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VspacerType:
    class Meta:
        name = "vspacerType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class VspacerUpType:
    class Meta:
        name = "vspacerUpType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WavyLineType1:
    class Meta:
        name = "wavy-lineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WavyLineType2:
    class Meta:
        name = "wavyLineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WedgeType:
    class Meta:
        name = "wedgeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WholeType:
    class Meta:
        name = "wholeType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WidthType:
    class Meta:
        name = "widthType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WordFontType:
    class Meta:
        name = "word-fontType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WordsType:
    class Meta:
        name = "wordsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WorkNumberType1:
    class Meta:
        name = "work-numberType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WorkTitleType1:
    class Meta:
        name = "work-titleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WorkNumberType2:
    class Meta:
        name = "workNumberType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WorkTitleType2:
    class Meta:
        name = "workTitleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WorkType:
    class Meta:
        name = "workType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class XType:
    class Meta:
        name = "xType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class XmlType:
    class Meta:
        name = "xmlType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class XoffType:
    class Meta:
        name = "xoffType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class XoffsetType:
    class Meta:
        name = "xoffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Y1Type:
    class Meta:
        name = "y1Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Y2Type:
    class Meta:
        name = "y2Type"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class YType:
    class Meta:
        name = "yType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class YoffType:
    class Meta:
        name = "yoffType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class YoffsetType:
    class Meta:
        name = "yoffsetType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ZType:
    class Meta:
        name = "zType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ZeroBeamValueType:
    class Meta:
        name = "zeroBeamValueType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ArpeggioHiddenInStdIfTab(ArpeggioHiddenInStdIfTabType):
    pass


@dataclass(kw_only=True)
class ArpeggioHookLen(ArpeggioHookLenType):
    pass


@dataclass(kw_only=True)
class ArpeggioLineWidth(ArpeggioLineWidthType):
    pass


@dataclass(kw_only=True)
class ArpeggioNoteDistance(ArpeggioNoteDistanceType):
    pass


@dataclass(kw_only=True)
class Attribute(AttributeType):
    pass


@dataclass(kw_only=True)
class Audio(AudioType):
    pass


@dataclass(kw_only=True)
class BeamMode(BeamModeType):
    pass


@dataclass(kw_only=True)
class Bravura(BravuraType):
    pass


@dataclass(kw_only=True)
class Cell(CellType):
    pass


@dataclass(kw_only=True)
class ClefChanges(ClefChangesType):
    pass


@dataclass(kw_only=True)
class Ctrl(CtrlType):
    pass


@dataclass(kw_only=True)
class DfermataAnchor(DfermataAnchorType):
    pass


@dataclass(kw_only=True)
class Division1(DivisionType1):
    class Meta:
        name = "Division"


@dataclass(kw_only=True)
class DlongfermataAnchor(DlongfermataAnchorType):
    pass


@dataclass(kw_only=True)
class DmarcatoAnchor(DmarcatoAnchorType):
    pass


@dataclass(kw_only=True)
class DottedNotes(DottedNotesType):
    pass


@dataclass(kw_only=True)
class DownMordentAnchor(DownMordentAnchorType):
    pass


@dataclass(kw_only=True)
class DownbowAnchor(DownbowAnchorType):
    pass


@dataclass(kw_only=True)
class DportatoAnchor(DportatoAnchorType):
    pass


@dataclass(kw_only=True)
class DshortfermataAnchor(DshortfermataAnchorType):
    pass


@dataclass(kw_only=True)
class DstaccatissimoAnchor(DstaccatissimoAnchorType):
    pass


@dataclass(kw_only=True)
class Duplets(DupletsType):
    pass


@dataclass(kw_only=True)
class DverylongfermataAnchor(DverylongfermataAnchorType):
    pass


@dataclass(kw_only=True)
class Element1(ElementType1):
    class Meta:
        name = "Element"


@dataclass(kw_only=True)
class EspressivoAnchor(EspressivoAnchorType):
    pass


@dataclass(kw_only=True)
class Excerpt(ExcerptType):
    pass


@dataclass(kw_only=True)
class Fbox(FboxType):
    class Meta:
        name = "FBox"


@dataclass(kw_only=True)
class Fsymbol(FsymbolType):
    class Meta:
        name = "FSymbol"


@dataclass(kw_only=True)
class Family1(FamilyType1):
    class Meta:
        name = "Family"


@dataclass(kw_only=True)
class FixMeasureNumbers(FixMeasureNumbersType):
    pass


@dataclass(kw_only=True)
class FixMeasureWidth(FixMeasureWidthType):
    pass


@dataclass(kw_only=True)
class Genre1(GenreType1):
    class Meta:
        name = "Genre"


@dataclass(kw_only=True)
class Hook(HookType):
    pass


@dataclass(kw_only=True)
class HumanPerformance(HumanPerformanceType):
    pass


@dataclass(kw_only=True)
class InstrumentGroup1(InstrumentGroupType1):
    class Meta:
        name = "InstrumentGroup"


@dataclass(kw_only=True)
class KeySym(KeySymType):
    pass


@dataclass(kw_only=True)
class Key1(KeyType1):
    class Meta:
        name = "Key"


@dataclass(kw_only=True)
class Layer(LayerType):
    pass


@dataclass(kw_only=True)
class LayerTag(LayerTagType):
    pass


@dataclass(kw_only=True)
class Leland(LelandType):
    pass


@dataclass(kw_only=True)
class Lyric1(LyricType1):
    class Meta:
        name = "Lyric"


@dataclass(kw_only=True)
class MmrestRange(MmrestRangeType):
    class Meta:
        name = "MMRestRange"


@dataclass(kw_only=True)
class MagIdx1(MagIdxType1):
    class Meta:
        name = "MagIdx"


@dataclass(kw_only=True)
class Mag1(MagType1):
    class Meta:
        name = "Mag"


@dataclass(kw_only=True)
class MeasureCount2XLess(MeasureCount2XLessType):
    class Meta:
        name = "MeasureCount2xLess"


@dataclass(kw_only=True)
class Menu(MenuType):
    pass


@dataclass(kw_only=True)
class MenuBar(MenuBarType):
    pass


@dataclass(kw_only=True)
class Message(MessageType):
    pass


@dataclass(kw_only=True)
class Meta1(MetaType1):
    class Meta:
        name = "Meta"


@dataclass(kw_only=True)
class MidiOptions(MidiOptionsType):
    pass


@dataclass(kw_only=True)
class MordentAnchor(MordentAnchorType):
    pass


@dataclass(kw_only=True)
class MuseSynth(MuseSynthType):
    pass


@dataclass(kw_only=True)
class Node(NodeType):
    pass


@dataclass(kw_only=True)
class Nonuplets(NonupletsType):
    pass


@dataclass(kw_only=True)
class NoteOff1(NoteOffType1):
    class Meta:
        name = "NoteOff"


@dataclass(kw_only=True)
class NoteOn1(NoteOnType1):
    class Meta:
        name = "NoteOn"


@dataclass(kw_only=True)
class Omr(OmrType):
    pass


@dataclass(kw_only=True)
class OmrPage(OmrPageType):
    pass


@dataclass(kw_only=True)
class OuvertAnchor(OuvertAnchorType):
    pass


@dataclass(kw_only=True)
class Palette(PaletteType):
    pass


@dataclass(kw_only=True)
class PaletteBox(PaletteBoxType):
    pass


@dataclass(kw_only=True)
class Path1(PathType1):
    class Meta:
        name = "Path"


@dataclass(kw_only=True)
class Petaluma(PetalumaType):
    pass


@dataclass(kw_only=True)
class Plugin(PluginType):
    pass


@dataclass(kw_only=True)
class PlusstopAnchor(PlusstopAnchorType):
    pass


@dataclass(kw_only=True)
class PrallAnchor(PrallAnchorType):
    pass


@dataclass(kw_only=True)
class PrallMordentAnchor(PrallMordentAnchorType):
    pass


@dataclass(kw_only=True)
class PrallPrallAnchor(PrallPrallAnchorType):
    pass


@dataclass(kw_only=True)
class Preference(PreferenceType):
    pass


@dataclass(kw_only=True)
class Preferences(PreferencesType):
    pass


@dataclass(kw_only=True)
class Program1(ProgramType1):
    class Meta:
        name = "Program"


@dataclass(kw_only=True)
class Quadruplets(QuadrupletsType):
    pass


@dataclass(kw_only=True)
class QuantValue(QuantValueType):
    pass


@dataclass(kw_only=True)
class Quintuplets(QuintupletsType):
    pass


@dataclass(kw_only=True)
class RecognizePickupBar(RecognizePickupBarType):
    pass


@dataclass(kw_only=True)
class Revision1(RevisionType1):
    class Meta:
        name = "Revision"


@dataclass(kw_only=True)
class Sc(Sctype):
    class Meta:
        name = "SC"


@dataclass(kw_only=True)
class Sc4(Sc4Type):
    class Meta:
        name = "SC4"


@dataclass(kw_only=True)
class Smf(Smftype):
    class Meta:
        name = "SMF"


@dataclass(kw_only=True)
class ScoreView(ScoreViewType):
    pass


@dataclass(kw_only=True)
class Septuplets(SeptupletsType):
    pass


@dataclass(kw_only=True)
class SforzatoaccentAnchor(SforzatoaccentAnchorType):
    pass


@dataclass(kw_only=True)
class Shortcut1(ShortcutType1):
    class Meta:
        name = "Shortcut"


@dataclass(kw_only=True)
class Shortcuts(ShortcutsType):
    pass


@dataclass(kw_only=True)
class ShowMore(ShowMoreType):
    pass


@dataclass(kw_only=True)
class ShowStaccato(ShowStaccatoType):
    pass


@dataclass(kw_only=True)
class SimplifyDurations(SimplifyDurationsType):
    pass


@dataclass(kw_only=True)
class SnappizzicatorAnchor(SnappizzicatorAnchorType):
    pass


@dataclass(kw_only=True)
class Spatium1(SpatiumType1):
    class Meta:
        name = "Spatium"


@dataclass(kw_only=True)
class SplitStaff(SplitStaffType):
    pass


@dataclass(kw_only=True)
class StaccatoAnchor(StaccatoAnchorType):
    pass


@dataclass(kw_only=True)
class StaffList(StaffListType):
    pass


@dataclass(kw_only=True)
class StaffState(StaffStateType):
    pass


@dataclass(kw_only=True)
class State(StateType):
    pass


@dataclass(kw_only=True)
class StemDirection(StemDirectionType):
    pass


@dataclass(kw_only=True)
class StemSlash(StemSlashType):
    pass


@dataclass(kw_only=True)
class Swing1(SwingType1):
    class Meta:
        name = "Swing"


@dataclass(kw_only=True)
class SymbolList(SymbolListType):
    pass


@dataclass(kw_only=True)
class Symbols(SymbolsType):
    pass


@dataclass(kw_only=True)
class SystemDivider(SystemDividerType):
    pass


@dataclass(kw_only=True)
class System1(SystemType1):
    class Meta:
        name = "System"


@dataclass(kw_only=True)
class TempoText(TempoTextType):
    pass


@dataclass(kw_only=True)
class TenutoAnchor(TenutoAnchorType):
    pass


@dataclass(kw_only=True)
class ThumbAnchor(ThumbAnchorType):
    pass


@dataclass(kw_only=True)
class ToolBar1(ToolBarType1):
    class Meta:
        name = "ToolBar"


@dataclass(kw_only=True)
class Toolbar2(ToolbarType2):
    class Meta:
        name = "Toolbar"


@dataclass(kw_only=True)
class Tour(TourType):
    pass


@dataclass(kw_only=True)
class TrackName1(TrackNameType1):
    class Meta:
        name = "TrackName"


@dataclass(kw_only=True)
class Track1(TrackType1):
    class Meta:
        name = "Track"


@dataclass(kw_only=True)
class Tracklist(TracklistType):
    pass


@dataclass(kw_only=True)
class TrillAnchor(TrillAnchorType):
    pass


@dataclass(kw_only=True)
class Triplets(TripletsType):
    pass


@dataclass(kw_only=True)
class TurnAnchor(TurnAnchorType):
    pass


@dataclass(kw_only=True)
class UfermataAnchor(UfermataAnchorType):
    pass


@dataclass(kw_only=True)
class UlongfermataAnchor(UlongfermataAnchorType):
    pass


@dataclass(kw_only=True)
class UmarcatoAnchor(UmarcatoAnchorType):
    pass


@dataclass(kw_only=True)
class UpMordentAnchor(UpMordentAnchorType):
    pass


@dataclass(kw_only=True)
class UpPrallAnchor(UpPrallAnchorType):
    pass


@dataclass(kw_only=True)
class UpbowAnchor(UpbowAnchorType):
    pass


@dataclass(kw_only=True)
class UportatoAnchor(UportatoAnchorType):
    pass


@dataclass(kw_only=True)
class UshortfermataAnchor(UshortfermataAnchorType):
    pass


@dataclass(kw_only=True)
class UstaccatissimoAnchor(UstaccatissimoAnchorType):
    pass


@dataclass(kw_only=True)
class UverylongfermataAnchor(UverylongfermataAnchorType):
    pass


@dataclass(kw_only=True)
class VoiceCount(VoiceCountType):
    pass


@dataclass(kw_only=True)
class Widget(WidgetType):
    pass


@dataclass(kw_only=True)
class Workspace(WorkspaceType):
    pass


@dataclass(kw_only=True)
class Zerberus(ZerberusType):
    pass


@dataclass(kw_only=True)
class APitchRange(APitchRangeType):
    class Meta:
        name = "aPitchRange"


@dataclass(kw_only=True)
class Acciaccatura(AcciaccaturaType):
    class Meta:
        name = "acciaccatura"


@dataclass(kw_only=True)
class AccidentalDistance(AccidentalDistanceType):
    class Meta:
        name = "accidentalDistance"


@dataclass(kw_only=True)
class AccidentalNoteDistance(AccidentalNoteDistanceType):
    class Meta:
        name = "accidentalNoteDistance"


@dataclass(kw_only=True)
class Accidental2(AccidentalType2):
    class Meta:
        name = "accidental"


@dataclass(kw_only=True)
class Action(ActionType):
    class Meta:
        name = "action"


@dataclass(kw_only=True)
class ActualNotes1(ActualNotesType1):
    class Meta:
        name = "actual-notes"


@dataclass(kw_only=True)
class ActualNotes2(ActualNotesType2):
    class Meta:
        name = "actualNotes"


@dataclass(kw_only=True)
class Aeolus(AeolusType):
    class Meta:
        name = "aeolus"


@dataclass(kw_only=True)
class AkkoladeDistance(AkkoladeDistanceType):
    class Meta:
        name = "akkoladeDistance"


@dataclass(kw_only=True)
class Align(AlignType):
    class Meta:
        name = "align"


@dataclass(kw_only=True)
class AllCapsNoteNames(AllCapsNoteNamesType):
    class Meta:
        name = "allCapsNoteNames"


@dataclass(kw_only=True)
class Alter(AlterType):
    class Meta:
        name = "alter"


@dataclass(kw_only=True)
class AlwaysShowBracketsWhenEmptyStavesAreHidden(
    AlwaysShowBracketsWhenEmptyStavesAreHiddenType
):
    class Meta:
        name = "alwaysShowBracketsWhenEmptyStavesAreHidden"


@dataclass(kw_only=True)
class Anchor(AnchorType):
    class Meta:
        name = "anchor"


@dataclass(kw_only=True)
class Angled(AngledType):
    class Meta:
        name = "angled"


@dataclass(kw_only=True)
class Appearance(AppearanceType):
    class Meta:
        name = "appearance"


@dataclass(kw_only=True)
class Appoggiatura(AppoggiaturaType):
    class Meta:
        name = "appoggiatura"


@dataclass(kw_only=True)
class Arpeggiate(ArpeggiateType):
    class Meta:
        name = "arpeggiate"


@dataclass(kw_only=True)
class Arranger(ArrangerType):
    class Meta:
        name = "arranger"


@dataclass(kw_only=True)
class ArticulationChange(ArticulationChangeType):
    class Meta:
        name = "articulationChange"


@dataclass(kw_only=True)
class Articulation2(ArticulationType2):
    class Meta:
        name = "articulation"


@dataclass(kw_only=True)
class Articulations(ArticulationsType):
    class Meta:
        name = "articulations"


@dataclass(kw_only=True)
class Attributes(AttributesType):
    class Meta:
        name = "attributes"


@dataclass(kw_only=True)
class AutoAdjust(AutoAdjustType):
    class Meta:
        name = "autoAdjust"


@dataclass(kw_only=True)
class AutoScale(AutoScaleType):
    class Meta:
        name = "autoScale"


@dataclass(kw_only=True)
class AutomaticCapitalization(AutomaticCapitalizationType):
    class Meta:
        name = "automaticCapitalization"


@dataclass(kw_only=True)
class Autoplace(AutoplaceType):
    class Meta:
        name = "autoplace"


@dataclass(kw_only=True)
class Back(BackType):
    class Meta:
        name = "back"


@dataclass(kw_only=True)
class BackgroundColor(BackgroundColorType):
    class Meta:
        name = "backgroundColor"


@dataclass(kw_only=True)
class Backslash(BackslashType):
    class Meta:
        name = "backslash"


@dataclass(kw_only=True)
class Backup(BackupType):
    class Meta:
        name = "backup"


@dataclass(kw_only=True)
class BarStyle(BarStyleType):
    class Meta:
        name = "bar-style"


@dataclass(kw_only=True)
class BarAccidentalDistance(BarAccidentalDistanceType):
    class Meta:
        name = "barAccidentalDistance"


@dataclass(kw_only=True)
class BarCount(BarCountType):
    class Meta:
        name = "barCount"


@dataclass(kw_only=True)
class BarGraceDistance(BarGraceDistanceType):
    class Meta:
        name = "barGraceDistance"


@dataclass(kw_only=True)
class BarLineSpanFrom(BarLineSpanFromType):
    class Meta:
        name = "barLineSpanFrom"


@dataclass(kw_only=True)
class BarLineSpanTo(BarLineSpanToType):
    class Meta:
        name = "barLineSpanTo"


@dataclass(kw_only=True)
class BarLineSpan1(BarLineSpanType1):
    class Meta:
        name = "barLineSpan"


@dataclass(kw_only=True)
class BarNoteDistance(BarNoteDistanceType):
    class Meta:
        name = "barNoteDistance"


@dataclass(kw_only=True)
class BarWidth(BarWidthType):
    class Meta:
        name = "barWidth"


@dataclass(kw_only=True)
class BarlineSpan2(BarlineSpanType2):
    class Meta:
        name = "barlineSpan"


@dataclass(kw_only=True)
class Barline2(BarlineType2):
    class Meta:
        name = "barline"


@dataclass(kw_only=True)
class Barlines(BarlinesType):
    class Meta:
        name = "barlines"


@dataclass(kw_only=True)
class Barre(BarreType):
    class Meta:
        name = "barre"


@dataclass(kw_only=True)
class Base(BaseType):
    class Meta:
        name = "base"


@dataclass(kw_only=True)
class BaseCase(BaseCaseType):
    class Meta:
        name = "baseCase"


@dataclass(kw_only=True)
class BaseDots(BaseDotsType):
    class Meta:
        name = "baseDots"


@dataclass(kw_only=True)
class BaseLen(BaseLenType):
    class Meta:
        name = "baseLen"


@dataclass(kw_only=True)
class BaseNote(BaseNoteType):
    class Meta:
        name = "baseNote"


@dataclass(kw_only=True)
class Basic(BasicType):
    class Meta:
        name = "basic"


@dataclass(kw_only=True)
class Bass(BassType):
    class Meta:
        name = "bass"


@dataclass(kw_only=True)
class BassAlter(BassAlterType):
    class Meta:
        name = "bass-alter"


@dataclass(kw_only=True)
class BassStep(BassStepType):
    class Meta:
        name = "bass-step"


@dataclass(kw_only=True)
class BeamDistance(BeamDistanceType):
    class Meta:
        name = "beamDistance"


@dataclass(kw_only=True)
class BeamFlattening(BeamFlatteningType):
    class Meta:
        name = "beamFlattening"


@dataclass(kw_only=True)
class BeamMaxSlope(BeamMaxSlopeType):
    class Meta:
        name = "beamMaxSlope"


@dataclass(kw_only=True)
class BeamMinLen(BeamMinLenType):
    class Meta:
        name = "beamMinLen"


@dataclass(kw_only=True)
class BeamMinSlope(BeamMinSlopeType):
    class Meta:
        name = "beamMinSlope"


@dataclass(kw_only=True)
class BeamWidth(BeamWidthType):
    class Meta:
        name = "beamWidth"


@dataclass(kw_only=True)
class Beam2(BeamType2):
    class Meta:
        name = "beam"


@dataclass(kw_only=True)
class BeatType(BeatTypeType):
    class Meta:
        name = "beat-type"


@dataclass(kw_only=True)
class BeatUnit(BeatUnitType):
    class Meta:
        name = "beat-unit"


@dataclass(kw_only=True)
class BeatUnitDot(BeatUnitDotType):
    class Meta:
        name = "beat-unit-dot"


@dataclass(kw_only=True)
class Beats(BeatsType):
    class Meta:
        name = "beats"


@dataclass(kw_only=True)
class BeginFontFace(BeginFontFaceType):
    class Meta:
        name = "beginFontFace"


@dataclass(kw_only=True)
class BeginFontSize(BeginFontSizeType):
    class Meta:
        name = "beginFontSize"


@dataclass(kw_only=True)
class BeginFontStyle(BeginFontStyleType):
    class Meta:
        name = "beginFontStyle"


@dataclass(kw_only=True)
class BeginHook(BeginHookType1):
    class Meta:
        name = "beginHook"


@dataclass(kw_only=True)
class BeginHookHeight(BeginHookHeightType):
    class Meta:
        name = "beginHookHeight"


@dataclass(kw_only=True)
class BeginHookType(BeginHookTypeType):
    class Meta:
        name = "beginHookType"


@dataclass(kw_only=True)
class BeginRepeatLeftMargin(BeginRepeatLeftMarginType):
    class Meta:
        name = "beginRepeatLeftMargin"


@dataclass(kw_only=True)
class BeginSymbol(BeginSymbolType):
    class Meta:
        name = "beginSymbol"


@dataclass(kw_only=True)
class BeginSymbolOffset(BeginSymbolOffsetType):
    class Meta:
        name = "beginSymbolOffset"


@dataclass(kw_only=True)
class BeginTextAlign(BeginTextAlignType):
    class Meta:
        name = "beginTextAlign"


@dataclass(kw_only=True)
class BeginTextPlace(BeginTextPlaceType):
    class Meta:
        name = "beginTextPlace"


@dataclass(kw_only=True)
class BendAlign(BendAlignType):
    class Meta:
        name = "bendAlign"


@dataclass(kw_only=True)
class BendFontFace(BendFontFaceType):
    class Meta:
        name = "bendFontFace"


@dataclass(kw_only=True)
class BendFontSize(BendFontSizeType):
    class Meta:
        name = "bendFontSize"


@dataclass(kw_only=True)
class BendFramePadding(BendFramePaddingType):
    class Meta:
        name = "bendFramePadding"


@dataclass(kw_only=True)
class BendFrameWidth(BendFrameWidthType):
    class Meta:
        name = "bendFrameWidth"


@dataclass(kw_only=True)
class Bold(BoldType):
    class Meta:
        name = "bold"


@dataclass(kw_only=True)
class Book(BookType):
    class Meta:
        name = "book"


@dataclass(kw_only=True)
class BottomMargin1(BottomMarginType1):
    class Meta:
        name = "bottom-margin"


@dataclass(kw_only=True)
class BottomGap(BottomGapType):
    class Meta:
        name = "bottomGap"


@dataclass(kw_only=True)
class BottomMargin2(BottomMarginType2):
    class Meta:
        name = "bottomMargin"


@dataclass(kw_only=True)
class BottomPitch(BottomPitchType):
    class Meta:
        name = "bottomPitch"


@dataclass(kw_only=True)
class BottomTpc(BottomTpcType):
    class Meta:
        name = "bottomTpc"


@dataclass(kw_only=True)
class BoxAutoSize(BoxAutoSizeType):
    class Meta:
        name = "boxAutoSize"


@dataclass(kw_only=True)
class Br(BrType):
    class Meta:
        name = "br"


@dataclass(kw_only=True)
class Bracket(BracketType1):
    class Meta:
        name = "bracket"


@dataclass(kw_only=True)
class BracketDistance(BracketDistanceType):
    class Meta:
        name = "bracketDistance"


@dataclass(kw_only=True)
class BracketSpan(BracketSpanType):
    class Meta:
        name = "bracketSpan"


@dataclass(kw_only=True)
class BracketType(BracketTypeType):
    class Meta:
        name = "bracketType"


@dataclass(kw_only=True)
class BracketWidth(BracketWidthType):
    class Meta:
        name = "bracketWidth"


@dataclass(kw_only=True)
class Brackets(BracketsType):
    class Meta:
        name = "brackets"


@dataclass(kw_only=True)
class BreakMultiMeasureRest(BreakMultiMeasureRestType):
    class Meta:
        name = "breakMultiMeasureRest"


@dataclass(kw_only=True)
class BreathMark(BreathMarkType):
    class Meta:
        name = "breath-mark"


@dataclass(kw_only=True)
class Breve(BreveType):
    class Meta:
        name = "breve"


@dataclass(kw_only=True)
class Caesura(CaesuraType):
    class Meta:
        name = "caesura"


@dataclass(kw_only=True)
class Cancel(CancelType):
    class Meta:
        name = "cancel"


@dataclass(kw_only=True)
class Capo(CapoType):
    class Meta:
        name = "capo"


@dataclass(kw_only=True)
class ChannelSwitch(ChannelSwitchType):
    class Meta:
        name = "channelSwitch"


@dataclass(kw_only=True)
class Channel2(ChannelType2):
    class Meta:
        name = "channel"


@dataclass(kw_only=True)
class ChordLine2(ChordLineType2):
    class Meta:
        name = "chord-line"


@dataclass(kw_only=True)
class ChordDescriptionFile(ChordDescriptionFileType):
    class Meta:
        name = "chordDescriptionFile"


@dataclass(kw_only=True)
class ChordExtensionAdjust(ChordExtensionAdjustType):
    class Meta:
        name = "chordExtensionAdjust"


@dataclass(kw_only=True)
class ChordExtensionMag(ChordExtensionMagType):
    class Meta:
        name = "chordExtensionMag"


@dataclass(kw_only=True)
class ChordModifierAdjust(ChordModifierAdjustType):
    class Meta:
        name = "chordModifierAdjust"


@dataclass(kw_only=True)
class ChordModifierMag(ChordModifierMagType):
    class Meta:
        name = "chordModifierMag"


@dataclass(kw_only=True)
class ChordNamesUseJazzFont(ChordNamesUseJazzFontType):
    class Meta:
        name = "chordNamesUseJazzFont"


@dataclass(kw_only=True)
class ChordStyle(ChordStyleType):
    class Meta:
        name = "chordStyle"


@dataclass(kw_only=True)
class ChordSymbolAalign(ChordSymbolAalignType):
    class Meta:
        name = "chordSymbolAAlign"


@dataclass(kw_only=True)
class ChordSymbolAfontFace(ChordSymbolAfontFaceType):
    class Meta:
        name = "chordSymbolAFontFace"


@dataclass(kw_only=True)
class ChordSymbolAfontSize(ChordSymbolAfontSizeType):
    class Meta:
        name = "chordSymbolAFontSize"


@dataclass(kw_only=True)
class ChordSymbolAfontStyle(ChordSymbolAfontStyleType):
    class Meta:
        name = "chordSymbolAFontStyle"


@dataclass(kw_only=True)
class ChordSymbolAframePadding(ChordSymbolAframePaddingType):
    class Meta:
        name = "chordSymbolAFramePadding"


@dataclass(kw_only=True)
class ChordSymbolAframeWidth(ChordSymbolAframeWidthType):
    class Meta:
        name = "chordSymbolAFrameWidth"


@dataclass(kw_only=True)
class ChordSymbolBalign(ChordSymbolBalignType):
    class Meta:
        name = "chordSymbolBAlign"


@dataclass(kw_only=True)
class ChordSymbolBfontFace(ChordSymbolBfontFaceType):
    class Meta:
        name = "chordSymbolBFontFace"


@dataclass(kw_only=True)
class ChordSymbolBfontSize(ChordSymbolBfontSizeType):
    class Meta:
        name = "chordSymbolBFontSize"


@dataclass(kw_only=True)
class ChordSymbolBposAbove(ChordSymbolBposAboveType):
    class Meta:
        name = "chordSymbolBPosAbove"


@dataclass(kw_only=True)
class ChordSymbolPosAbove(ChordSymbolPosAboveType):
    class Meta:
        name = "chordSymbolPosAbove"


@dataclass(kw_only=True)
class ChordsXmlFile(ChordsXmlFileType):
    class Meta:
        name = "chordsXmlFile"


@dataclass(kw_only=True)
class Chorus(ChorusType):
    class Meta:
        name = "chorus"


@dataclass(kw_only=True)
class Chromatic(ChromaticType):
    class Meta:
        name = "chromatic"


@dataclass(kw_only=True)
class Circle(CircleType):
    class Meta:
        name = "circle"


@dataclass(kw_only=True)
class CircleX(CircleXType):
    class Meta:
        name = "circle-x"


@dataclass(kw_only=True)
class Clean(CleanType):
    class Meta:
        name = "clean"


@dataclass(kw_only=True)
class ClefOctaveChange(ClefOctaveChangeType):
    class Meta:
        name = "clef-octave-change"


@dataclass(kw_only=True)
class ClefBarlineDistance(ClefBarlineDistanceType):
    class Meta:
        name = "clefBarlineDistance"


@dataclass(kw_only=True)
class ClefKeyRightMargin(ClefKeyRightMarginType):
    class Meta:
        name = "clefKeyRightMargin"


@dataclass(kw_only=True)
class ClefLeftMargin(ClefLeftMarginType):
    class Meta:
        name = "clefLeftMargin"


@dataclass(kw_only=True)
class ClefSign(ClefSignType):
    class Meta:
        name = "clefSign"


@dataclass(kw_only=True)
class Clef2(ClefType2):
    class Meta:
        name = "clef"


@dataclass(kw_only=True)
class Coda(CodaType):
    class Meta:
        name = "coda"


@dataclass(kw_only=True)
class Code(CodeType):
    class Meta:
        name = "code"


@dataclass(kw_only=True)
class Color(ColorType):
    class Meta:
        name = "color"


@dataclass(kw_only=True)
class Composer(ComposerType):
    class Meta:
        name = "composer"


@dataclass(kw_only=True)
class ComposerFontFace(ComposerFontFaceType):
    class Meta:
        name = "composerFontFace"


@dataclass(kw_only=True)
class ComposerFontSize(ComposerFontSizeType):
    class Meta:
        name = "composerFontSize"


@dataclass(kw_only=True)
class ComposerFontSpatiumDependent(ComposerFontSpatiumDependentType):
    class Meta:
        name = "composerFontSpatiumDependent"


@dataclass(kw_only=True)
class ComposerFontStyle(ComposerFontStyleType):
    class Meta:
        name = "composerFontStyle"


@dataclass(kw_only=True)
class ComposerFramePadding(ComposerFramePaddingType):
    class Meta:
        name = "composerFramePadding"


@dataclass(kw_only=True)
class ComposerFrameRound(ComposerFrameRoundType):
    class Meta:
        name = "composerFrameRound"


@dataclass(kw_only=True)
class ComposerFrameWidth(ComposerFrameWidthType):
    class Meta:
        name = "composerFrameWidth"


@dataclass(kw_only=True)
class ConcertClef(ConcertClefType1):
    class Meta:
        name = "concertClef"


@dataclass(kw_only=True)
class ConcertClefType(ConcertClefTypeType):
    class Meta:
        name = "concertClefType"


@dataclass(kw_only=True)
class ConcertPitch(ConcertPitchType):
    class Meta:
        name = "concertPitch"


@dataclass(kw_only=True)
class Container(ContainerType):
    class Meta:
        name = "container"


@dataclass(kw_only=True)
class Content(ContentType):
    class Meta:
        name = "content"


@dataclass(kw_only=True)
class ContinuationLine(ContinuationLineType):
    class Meta:
        name = "continuationLine"


@dataclass(kw_only=True)
class ContinueAt(ContinueAtType):
    class Meta:
        name = "continueAt"


@dataclass(kw_only=True)
class ContinueSymbol(ContinueSymbolType):
    class Meta:
        name = "continueSymbol"


@dataclass(kw_only=True)
class ContinueSymbolOffset(ContinueSymbolOffsetType):
    class Meta:
        name = "continueSymbolOffset"


@dataclass(kw_only=True)
class ContinueTextPlace(ContinueTextPlaceType):
    class Meta:
        name = "continueTextPlace"


@dataclass(kw_only=True)
class Controller(ControllerType):
    class Meta:
        name = "controller"


@dataclass(kw_only=True)
class CreateMultiMeasureRests(CreateMultiMeasureRestsType):
    class Meta:
        name = "createMultiMeasureRests"


@dataclass(kw_only=True)
class Created(CreatedType):
    class Meta:
        name = "created"


@dataclass(kw_only=True)
class CreationDate(CreationDateType):
    class Meta:
        name = "creationDate"


@dataclass(kw_only=True)
class Creator(CreatorType):
    class Meta:
        name = "creator"


@dataclass(kw_only=True)
class Credit(CreditType1):
    class Meta:
        name = "credit"


@dataclass(kw_only=True)
class CreditType(CreditTypeType):
    class Meta:
        name = "credit-type"


@dataclass(kw_only=True)
class CreditWords(CreditWordsType):
    class Meta:
        name = "credit-words"


@dataclass(kw_only=True)
class CropB(CropBtype):
    class Meta:
        name = "cropB"


@dataclass(kw_only=True)
class CropL(CropLtype):
    class Meta:
        name = "cropL"


@dataclass(kw_only=True)
class CropR(CropRtype):
    class Meta:
        name = "cropR"


@dataclass(kw_only=True)
class CropT(CropTtype):
    class Meta:
        name = "cropT"


@dataclass(kw_only=True)
class Cross(CrossType):
    class Meta:
        name = "cross"


@dataclass(kw_only=True)
class CrossMeasureValues(CrossMeasureValuesType):
    class Meta:
        name = "crossMeasureValues"


@dataclass(kw_only=True)
class Cue(CueType):
    class Meta:
        name = "cue"


@dataclass(kw_only=True)
class CurrentLayer(CurrentLayerType):
    class Meta:
        name = "currentLayer"


@dataclass(kw_only=True)
class CursorTrack(CursorTrackType):
    class Meta:
        name = "cursorTrack"


@dataclass(kw_only=True)
class Custom(CustomType):
    class Meta:
        name = "custom"


@dataclass(kw_only=True)
class CustomSubtype(CustomSubtypeType):
    class Meta:
        name = "customSubtype"


@dataclass(kw_only=True)
class Cutaway(CutawayType):
    class Meta:
        name = "cutaway"


@dataclass(kw_only=True)
class DashGapLength(DashGapLengthType):
    class Meta:
        name = "dashGapLength"


@dataclass(kw_only=True)
class DashLineLength(DashLineLengthType):
    class Meta:
        name = "dashLineLength"


@dataclass(kw_only=True)
class Dashes(DashesType):
    class Meta:
        name = "dashes"


@dataclass(kw_only=True)
class Date(DateType):
    class Meta:
        name = "date"


@dataclass(kw_only=True)
class DefaultAlign(DefaultAlignType):
    class Meta:
        name = "defaultAlign"


@dataclass(kw_only=True)
class DefaultClef(DefaultClefType):
    class Meta:
        name = "defaultClef"


@dataclass(kw_only=True)
class DefaultConcertClef(DefaultConcertClefType):
    class Meta:
        name = "defaultConcertClef"


@dataclass(kw_only=True)
class DefaultFontFace(DefaultFontFaceType):
    class Meta:
        name = "defaultFontFace"


@dataclass(kw_only=True)
class DefaultFontSpatiumDependent(DefaultFontSpatiumDependentType):
    class Meta:
        name = "defaultFontSpatiumDependent"


@dataclass(kw_only=True)
class DefaultFramePadding(DefaultFramePaddingType):
    class Meta:
        name = "defaultFramePadding"


@dataclass(kw_only=True)
class DefaultFrameRound(DefaultFrameRoundType):
    class Meta:
        name = "defaultFrameRound"


@dataclass(kw_only=True)
class DefaultFrameWidth(DefaultFrameWidthType):
    class Meta:
        name = "defaultFrameWidth"


@dataclass(kw_only=True)
class DefaultLineHeight(DefaultLineHeightType):
    class Meta:
        name = "defaultLineHeight"


@dataclass(kw_only=True)
class DefaultOffset(DefaultOffsetType):
    class Meta:
        name = "defaultOffset"


@dataclass(kw_only=True)
class DefaultPitch(DefaultPitchType):
    class Meta:
        name = "defaultPitch"


@dataclass(kw_only=True)
class DefaultTransposingClef(DefaultTransposingClefType):
    class Meta:
        name = "defaultTransposingClef"


@dataclass(kw_only=True)
class DefaultYoffset(DefaultYoffsetType):
    class Meta:
        name = "defaultYOffset"


@dataclass(kw_only=True)
class Defaults(DefaultsType):
    class Meta:
        name = "defaults"


@dataclass(kw_only=True)
class DefaultsVersion(DefaultsVersionType):
    class Meta:
        name = "defaultsVersion"


@dataclass(kw_only=True)
class Degree(DegreeType1):
    class Meta:
        name = "degree"


@dataclass(kw_only=True)
class DegreeAlter(DegreeAlterType):
    class Meta:
        name = "degree-alter"


@dataclass(kw_only=True)
class DegreeType(DegreeTypeType):
    class Meta:
        name = "degree-type"


@dataclass(kw_only=True)
class DegreeValue(DegreeValueType):
    class Meta:
        name = "degree-value"


@dataclass(kw_only=True)
class DelayedTurn(DelayedTurnType):
    class Meta:
        name = "delayed-turn"


@dataclass(kw_only=True)
class Den(DenType):
    class Meta:
        name = "den"


@dataclass(kw_only=True)
class Denom(DenomType):
    class Meta:
        name = "denom"


@dataclass(kw_only=True)
class Denom2(Denom2Type):
    class Meta:
        name = "denom2"


@dataclass(kw_only=True)
class Descr(DescrType):
    class Meta:
        name = "descr"


@dataclass(kw_only=True)
class Description(DescriptionType):
    class Meta:
        name = "description"


@dataclass(kw_only=True)
class Diagonal(DiagonalType):
    class Meta:
        name = "diagonal"


@dataclass(kw_only=True)
class Diamond(DiamondType):
    class Meta:
        name = "diamond"


@dataclass(kw_only=True)
class Diatonic(DiatonicType):
    class Meta:
        name = "diatonic"


@dataclass(kw_only=True)
class Diff(DiffType):
    class Meta:
        name = "diff"


@dataclass(kw_only=True)
class Digit(DigitType):
    class Meta:
        name = "digit"


@dataclass(kw_only=True)
class Direction(DirectionType1):
    class Meta:
        name = "direction"


@dataclass(kw_only=True)
class DirectionType(DirectionTypeType):
    class Meta:
        name = "direction-type"


@dataclass(kw_only=True)
class Dirty(DirtyType):
    class Meta:
        name = "dirty"


@dataclass(kw_only=True)
class Display(DisplayType):
    class Meta:
        name = "display"


@dataclass(kw_only=True)
class DisplayOctave(DisplayOctaveType):
    class Meta:
        name = "display-octave"


@dataclass(kw_only=True)
class DisplayStep(DisplayStepType):
    class Meta:
        name = "display-step"


@dataclass(kw_only=True)
class DisplayInConcertPitch(DisplayInConcertPitchType):
    class Meta:
        name = "displayInConcertPitch"


@dataclass(kw_only=True)
class DisplayName(DisplayNameType):
    class Meta:
        name = "displayName"


@dataclass(kw_only=True)
class DistOffset(DistOffsetType):
    class Meta:
        name = "distOffset"


@dataclass(kw_only=True)
class Distances(DistancesType):
    class Meta:
        name = "distances"


@dataclass(kw_only=True)
class Distribute(DistributeType):
    class Meta:
        name = "distribute"


@dataclass(kw_only=True)
class DividerLeft(DividerLeftType):
    class Meta:
        name = "dividerLeft"


@dataclass(kw_only=True)
class Division2(DivisionType2):
    class Meta:
        name = "division"


@dataclass(kw_only=True)
class Divisions(DivisionsType):
    class Meta:
        name = "divisions"


@dataclass(kw_only=True)
class Do(DoType):
    class Meta:
        name = "do"


@dataclass(kw_only=True)
class Doit(DoitType):
    class Meta:
        name = "doit"


@dataclass(kw_only=True)
class DontHidStavesInFirstSystm(DontHidStavesInFirstSystmType):
    class Meta:
        name = "dontHidStavesInFirstSystm"


@dataclass(kw_only=True)
class Dot(DotType):
    class Meta:
        name = "dot"


@dataclass(kw_only=True)
class DotDotDistance(DotDotDistanceType):
    class Meta:
        name = "dotDotDistance"


@dataclass(kw_only=True)
class DotNoteDistance(DotNoteDistanceType):
    class Meta:
        name = "dotNoteDistance"


@dataclass(kw_only=True)
class DotPosition(DotPositionType):
    class Meta:
        name = "dotPosition"


@dataclass(kw_only=True)
class Dots(DotsType):
    class Meta:
        name = "dots"


@dataclass(kw_only=True)
class DoubleAngled(DoubleAngledType):
    class Meta:
        name = "double-angled"


@dataclass(kw_only=True)
class DoubleDot(DoubleDotType):
    class Meta:
        name = "double-dot"


@dataclass(kw_only=True)
class DoubleSquare(DoubleSquareType):
    class Meta:
        name = "double-square"


@dataclass(kw_only=True)
class DoubleBarDistance(DoubleBarDistanceType):
    class Meta:
        name = "doubleBarDistance"


@dataclass(kw_only=True)
class DoubleBarWidth(DoubleBarWidthType):
    class Meta:
        name = "doubleBarWidth"


@dataclass(kw_only=True)
class Doubleflat(DoubleflatType):
    class Meta:
        name = "doubleflat"


@dataclass(kw_only=True)
class Doublesharp(DoublesharpType):
    class Meta:
        name = "doublesharp"


@dataclass(kw_only=True)
class DownloadUrl(DownloadUrlType):
    class Meta:
        name = "downloadUrl"


@dataclass(kw_only=True)
class Dpmm(DpmmType):
    class Meta:
        name = "dpmm"


@dataclass(kw_only=True)
class DragOffset(DragOffsetType):
    class Meta:
        name = "dragOffset"


@dataclass(kw_only=True)
class DrawObj(DrawObjType):
    class Meta:
        name = "drawObj"


@dataclass(kw_only=True)
class DrawObjects(DrawObjectsType):
    class Meta:
        name = "drawObjects"


@dataclass(kw_only=True)
class DrumPalette(DrumPaletteType):
    class Meta:
        name = "drumPalette"


@dataclass(kw_only=True)
class Drumset(DrumsetType):
    class Meta:
        name = "drumset"


@dataclass(kw_only=True)
class Duration(DurationType1):
    class Meta:
        name = "duration"


@dataclass(kw_only=True)
class DurationFont(DurationFontType):
    class Meta:
        name = "durationFont"


@dataclass(kw_only=True)
class DurationFontName(DurationFontNameType):
    class Meta:
        name = "durationFontName"


@dataclass(kw_only=True)
class DurationFontSize(DurationFontSizeType):
    class Meta:
        name = "durationFontSize"


@dataclass(kw_only=True)
class DurationFontY(DurationFontYtype):
    class Meta:
        name = "durationFontY"


@dataclass(kw_only=True)
class DurationType(DurationTypeType):
    class Meta:
        name = "durationType"


@dataclass(kw_only=True)
class Durations(DurationsType):
    class Meta:
        name = "durations"


@dataclass(kw_only=True)
class DynType(DynTypeType):
    class Meta:
        name = "dynType"


@dataclass(kw_only=True)
class Dynamics(DynamicsType):
    class Meta:
        name = "dynamics"


@dataclass(kw_only=True)
class DynamicsFontFace(DynamicsFontFaceType):
    class Meta:
        name = "dynamicsFontFace"


@dataclass(kw_only=True)
class DynamicsFontItalic(DynamicsFontItalicType):
    class Meta:
        name = "dynamicsFontItalic"


@dataclass(kw_only=True)
class DynamicsFontSize(DynamicsFontSizeType):
    class Meta:
        name = "dynamicsFontSize"


@dataclass(kw_only=True)
class DynamicsFontStyle(DynamicsFontStyleType):
    class Meta:
        name = "dynamicsFontStyle"


@dataclass(kw_only=True)
class DynamicsFramePadding(DynamicsFramePaddingType):
    class Meta:
        name = "dynamicsFramePadding"


@dataclass(kw_only=True)
class DynamicsFrameWidth(DynamicsFrameWidthType):
    class Meta:
        name = "dynamicsFrameWidth"


@dataclass(kw_only=True)
class DynamicsPosAbove(DynamicsPosAboveType):
    class Meta:
        name = "dynamicsPosAbove"


@dataclass(kw_only=True)
class DynamicsPosBelow(DynamicsPosBelowType):
    class Meta:
        name = "dynamicsPosBelow"


@dataclass(kw_only=True)
class EaseInSpin(EaseInSpinType):
    class Meta:
        name = "easeInSpin"


@dataclass(kw_only=True)
class EaseOutSpin(EaseOutSpinType):
    class Meta:
        name = "easeOutSpin"


@dataclass(kw_only=True)
class Editable(EditableType):
    class Meta:
        name = "editable"


@dataclass(kw_only=True)
class Element2(ElementType2):
    class Meta:
        name = "element"


@dataclass(kw_only=True)
class Elements(ElementsType):
    class Meta:
        name = "elements"


@dataclass(kw_only=True)
class Elision(ElisionType):
    class Meta:
        name = "elision"


@dataclass(kw_only=True)
class Ellipse(EllipseType):
    class Meta:
        name = "ellipse"


@dataclass(kw_only=True)
class EnableIndentationOnFirstSystem(EnableIndentationOnFirstSystemType):
    class Meta:
        name = "enableIndentationOnFirstSystem"


@dataclass(kw_only=True)
class EnableVerticalSpread(EnableVerticalSpreadType):
    class Meta:
        name = "enableVerticalSpread"


@dataclass(kw_only=True)
class Encoding(EncodingType):
    class Meta:
        name = "encoding"


@dataclass(kw_only=True)
class EncodingDate(EncodingDateType):
    class Meta:
        name = "encoding-date"


@dataclass(kw_only=True)
class EndBarDistance(EndBarDistanceType):
    class Meta:
        name = "endBarDistance"


@dataclass(kw_only=True)
class EndBarWidth(EndBarWidthType):
    class Meta:
        name = "endBarWidth"


@dataclass(kw_only=True)
class EndHook(EndHookType1):
    class Meta:
        name = "endHook"


@dataclass(kw_only=True)
class EndHookHeight(EndHookHeightType):
    class Meta:
        name = "endHookHeight"


@dataclass(kw_only=True)
class EndHookType(EndHookTypeType):
    class Meta:
        name = "endHookType"


@dataclass(kw_only=True)
class EndRepeat(EndRepeatType):
    class Meta:
        name = "endRepeat"


@dataclass(kw_only=True)
class EndSpanner(EndSpannerType):
    class Meta:
        name = "endSpanner"


@dataclass(kw_only=True)
class EndSymbol(EndSymbolType):
    class Meta:
        name = "endSymbol"


@dataclass(kw_only=True)
class EndSymbolOffset(EndSymbolOffsetType):
    class Meta:
        name = "endSymbolOffset"


@dataclass(kw_only=True)
class EndText(EndTextType):
    class Meta:
        name = "endText"


@dataclass(kw_only=True)
class EndTextAlign(EndTextAlignType):
    class Meta:
        name = "endTextAlign"


@dataclass(kw_only=True)
class EndTextPlace(EndTextPlaceType):
    class Meta:
        name = "endTextPlace"


@dataclass(kw_only=True)
class EndTick(EndTickType):
    class Meta:
        name = "endTick"


@dataclass(kw_only=True)
class EndTrack(EndTrackType):
    class Meta:
        name = "endTrack"


@dataclass(kw_only=True)
class EndTuplet(EndTupletType):
    class Meta:
        name = "endTuplet"


@dataclass(kw_only=True)
class Ending(EndingType):
    class Meta:
        name = "ending"


@dataclass(kw_only=True)
class Endings(EndingsType):
    class Meta:
        name = "endings"


@dataclass(kw_only=True)
class Ensemble(EnsembleType):
    class Meta:
        name = "ensemble"


@dataclass(kw_only=True)
class EvenFooter(EvenFooterType):
    class Meta:
        name = "evenFooter"


@dataclass(kw_only=True)
class EvenFooterC(EvenFooterCtype):
    class Meta:
        name = "evenFooterC"


@dataclass(kw_only=True)
class EvenFooterL(EvenFooterLtype):
    class Meta:
        name = "evenFooterL"


@dataclass(kw_only=True)
class EvenFooterR(EvenFooterRtype):
    class Meta:
        name = "evenFooterR"


@dataclass(kw_only=True)
class EvenHeader(EvenHeaderType):
    class Meta:
        name = "evenHeader"


@dataclass(kw_only=True)
class EvenHeaderC(EvenHeaderCtype):
    class Meta:
        name = "evenHeaderC"


@dataclass(kw_only=True)
class EvenHeaderL(EvenHeaderLtype):
    class Meta:
        name = "evenHeaderL"


@dataclass(kw_only=True)
class EvenHeaderR(EvenHeaderRtype):
    class Meta:
        name = "evenHeaderR"


@dataclass(kw_only=True)
class Event2(EventType2):
    class Meta:
        name = "event"


@dataclass(kw_only=True)
class Events2(EventsType2):
    class Meta:
        name = "events"


@dataclass(kw_only=True)
class Expanded(ExpandedType):
    class Meta:
        name = "expanded"


@dataclass(kw_only=True)
class ExpressionFontFace(ExpressionFontFaceType):
    class Meta:
        name = "expressionFontFace"


@dataclass(kw_only=True)
class ExpressionFontSize(ExpressionFontSizeType):
    class Meta:
        name = "expressionFontSize"


@dataclass(kw_only=True)
class ExpressionFramePadding(ExpressionFramePaddingType):
    class Meta:
        name = "expressionFramePadding"


@dataclass(kw_only=True)
class ExpressionFrameWidth(ExpressionFrameWidthType):
    class Meta:
        name = "expressionFrameWidth"


@dataclass(kw_only=True)
class Extend(ExtendType):
    class Meta:
        name = "extend"


@dataclass(kw_only=True)
class Extended(ExtendedType):
    class Meta:
        name = "extended"


@dataclass(kw_only=True)
class Extension(ExtensionType):
    class Meta:
        name = "extension"


@dataclass(kw_only=True)
class ExtraDistance(ExtraDistanceType):
    class Meta:
        name = "extraDistance"


@dataclass(kw_only=True)
class F(FType):
    class Meta:
        name = "f"


@dataclass(kw_only=True)
class Fa(FaType):
    class Meta:
        name = "fa"


@dataclass(kw_only=True)
class Falloff(FalloffType):
    class Meta:
        name = "falloff"


@dataclass(kw_only=True)
class Family2(FamilyType2):
    class Meta:
        name = "family"


@dataclass(kw_only=True)
class FermataPosAbove(FermataPosAboveType):
    class Meta:
        name = "fermataPosAbove"


@dataclass(kw_only=True)
class FermataPosBelow(FermataPosBelowType):
    class Meta:
        name = "fermataPosBelow"


@dataclass(kw_only=True)
class Fermata2(FermataType2):
    class Meta:
        name = "fermata"


@dataclass(kw_only=True)
class Fifths(FifthsType):
    class Meta:
        name = "fifths"


@dataclass(kw_only=True)
class Figure(FigureType):
    class Meta:
        name = "figure"


@dataclass(kw_only=True)
class FigureNumber(FigureNumberType):
    class Meta:
        name = "figure-number"


@dataclass(kw_only=True)
class FiguredBass2(FiguredBassType2):
    class Meta:
        name = "figured-bass"


@dataclass(kw_only=True)
class FiguredBassFontFace(FiguredBassFontFaceType):
    class Meta:
        name = "figuredBassFontFace"


@dataclass(kw_only=True)
class File(FileType):
    class Meta:
        name = "file"


@dataclass(kw_only=True)
class FingeringFontFace(FingeringFontFaceType):
    class Meta:
        name = "fingeringFontFace"


@dataclass(kw_only=True)
class FingeringFontSize(FingeringFontSizeType):
    class Meta:
        name = "fingeringFontSize"


@dataclass(kw_only=True)
class FingeringFramePadding(FingeringFramePaddingType):
    class Meta:
        name = "fingeringFramePadding"


@dataclass(kw_only=True)
class FingeringFrameRound(FingeringFrameRoundType):
    class Meta:
        name = "fingeringFrameRound"


@dataclass(kw_only=True)
class FingeringFrameWidth(FingeringFrameWidthType):
    class Meta:
        name = "fingeringFrameWidth"


@dataclass(kw_only=True)
class Fingering2(FingeringType2):
    class Meta:
        name = "fingering"


@dataclass(kw_only=True)
class FirstSystemIdentation(FirstSystemIdentationType):
    class Meta:
        name = "firstSystemIdentation"


@dataclass(kw_only=True)
class Fixed(FixedType):
    class Meta:
        name = "fixed"


@dataclass(kw_only=True)
class FixedLine(FixedLineType):
    class Meta:
        name = "fixedLine"


@dataclass(kw_only=True)
class Flat(FlatType):
    class Meta:
        name = "flat"


@dataclass(kw_only=True)
class FollowText(FollowTextType):
    class Meta:
        name = "followText"


@dataclass(kw_only=True)
class Fontsize(FontsizeType):
    class Meta:
        name = "fontsize"


@dataclass(kw_only=True)
class FooterAlign(FooterAlignType):
    class Meta:
        name = "footerAlign"


@dataclass(kw_only=True)
class FooterFontFace(FooterFontFaceType):
    class Meta:
        name = "footerFontFace"


@dataclass(kw_only=True)
class FooterFontSize(FooterFontSizeType):
    class Meta:
        name = "footerFontSize"


@dataclass(kw_only=True)
class FooterFramePadding(FooterFramePaddingType):
    class Meta:
        name = "footerFramePadding"


@dataclass(kw_only=True)
class FooterFrameWidth(FooterFrameWidthType):
    class Meta:
        name = "footerFrameWidth"


@dataclass(kw_only=True)
class FooterOddEven(FooterOddEvenType):
    class Meta:
        name = "footerOddEven"


@dataclass(kw_only=True)
class ForInstrumentChange(ForInstrumentChangeType):
    class Meta:
        name = "forInstrumentChange"


@dataclass(kw_only=True)
class ForegroundColor(ForegroundColorType):
    class Meta:
        name = "foregroundColor"


@dataclass(kw_only=True)
class Format(FormatType):
    class Meta:
        name = "format"


@dataclass(kw_only=True)
class Forward(ForwardType):
    class Meta:
        name = "forward"


@dataclass(kw_only=True)
class Fractions(FractionsType):
    class Meta:
        name = "fractions"


@dataclass(kw_only=True)
class Frame(FrameType1):
    class Meta:
        name = "frame"


@dataclass(kw_only=True)
class FrameFrets(FrameFretsType):
    class Meta:
        name = "frame-frets"


@dataclass(kw_only=True)
class FrameNote(FrameNoteType):
    class Meta:
        name = "frame-note"


@dataclass(kw_only=True)
class FrameStrings(FrameStringsType):
    class Meta:
        name = "frame-strings"


@dataclass(kw_only=True)
class FrameAlign(FrameAlignType):
    class Meta:
        name = "frameAlign"


@dataclass(kw_only=True)
class FrameColor(FrameColorType):
    class Meta:
        name = "frameColor"


@dataclass(kw_only=True)
class FrameFontFace(FrameFontFaceType):
    class Meta:
        name = "frameFontFace"


@dataclass(kw_only=True)
class FrameFontSize(FrameFontSizeType):
    class Meta:
        name = "frameFontSize"


@dataclass(kw_only=True)
class FrameFontSpatiumDependent(FrameFontSpatiumDependentType):
    class Meta:
        name = "frameFontSpatiumDependent"


@dataclass(kw_only=True)
class FrameFramePadding(FrameFramePaddingType):
    class Meta:
        name = "frameFramePadding"


@dataclass(kw_only=True)
class FrameFrameWidth(FrameFrameWidthType):
    class Meta:
        name = "frameFrameWidth"


@dataclass(kw_only=True)
class FramePadding(FramePaddingType):
    class Meta:
        name = "framePadding"


@dataclass(kw_only=True)
class FrameRound(FrameRoundType):
    class Meta:
        name = "frameRound"


@dataclass(kw_only=True)
class FrameSystemDistance(FrameSystemDistanceType):
    class Meta:
        name = "frameSystemDistance"


@dataclass(kw_only=True)
class FrameType(FrameTypeType):
    class Meta:
        name = "frameType"


@dataclass(kw_only=True)
class FrameWidth(FrameWidthType):
    class Meta:
        name = "frameWidth"


@dataclass(kw_only=True)
class FrameWidthS(FrameWidthStype):
    class Meta:
        name = "frameWidthS"


@dataclass(kw_only=True)
class FreeGlyphs(FreeGlyphsType):
    class Meta:
        name = "free-glyphs"


@dataclass(kw_only=True)
class Fret(FretType):
    class Meta:
        name = "fret"


@dataclass(kw_only=True)
class FretFont(FretFontType):
    class Meta:
        name = "fretFont"


@dataclass(kw_only=True)
class FretFontName(FretFontNameType):
    class Meta:
        name = "fretFontName"


@dataclass(kw_only=True)
class FretFontSize(FretFontSizeType):
    class Meta:
        name = "fretFontSize"


@dataclass(kw_only=True)
class FretFontY(FretFontYtype):
    class Meta:
        name = "fretFontY"


@dataclass(kw_only=True)
class FretOffset(FretOffsetType):
    class Meta:
        name = "fretOffset"


@dataclass(kw_only=True)
class Frets(FretsType):
    class Meta:
        name = "frets"


@dataclass(kw_only=True)
class Function(FunctionType):
    class Meta:
        name = "function"


@dataclass(kw_only=True)
class Gallery(GalleryType):
    class Meta:
        name = "gallery"


@dataclass(kw_only=True)
class GateTime(GateTimeType):
    class Meta:
        name = "gateTime"


@dataclass(kw_only=True)
class GenClef(GenClefType):
    class Meta:
        name = "genClef"


@dataclass(kw_only=True)
class GenCourtesyClef(GenCourtesyClefType):
    class Meta:
        name = "genCourtesyClef"


@dataclass(kw_only=True)
class GenCourtesyKeysig(GenCourtesyKeysigType):
    class Meta:
        name = "genCourtesyKeysig"


@dataclass(kw_only=True)
class GenCourtesyTimesig(GenCourtesyTimesigType):
    class Meta:
        name = "genCourtesyTimesig"


@dataclass(kw_only=True)
class GenKeysig(GenKeysigType):
    class Meta:
        name = "genKeysig"


@dataclass(kw_only=True)
class GenTimesig(GenTimesigType):
    class Meta:
        name = "genTimesig"


@dataclass(kw_only=True)
class Genre2(GenreType2):
    class Meta:
        name = "genre"


@dataclass(kw_only=True)
class Ghost(GhostType):
    class Meta:
        name = "ghost"


@dataclass(kw_only=True)
class GlissandoAlign(GlissandoAlignType):
    class Meta:
        name = "glissandoAlign"


@dataclass(kw_only=True)
class GlissandoFontFace(GlissandoFontFaceType):
    class Meta:
        name = "glissandoFontFace"


@dataclass(kw_only=True)
class GlissandoFontSize(GlissandoFontSizeType):
    class Meta:
        name = "glissandoFontSize"


@dataclass(kw_only=True)
class GlissandoFramePadding(GlissandoFramePaddingType):
    class Meta:
        name = "glissandoFramePadding"


@dataclass(kw_only=True)
class GlissandoFrameWidth(GlissandoFrameWidthType):
    class Meta:
        name = "glissandoFrameWidth"


@dataclass(kw_only=True)
class GlissandoStyle(GlissandoStyleType):
    class Meta:
        name = "glissandoStyle"


@dataclass(kw_only=True)
class Glissando2(GlissandoType2):
    class Meta:
        name = "glissando"


@dataclass(kw_only=True)
class Glyph(GlyphType):
    class Meta:
        name = "glyph"


@dataclass(kw_only=True)
class GlyphIndex(GlyphIndexType):
    class Meta:
        name = "glyph-index"


@dataclass(kw_only=True)
class Grace(GraceType):
    class Meta:
        name = "grace"


@dataclass(kw_only=True)
class Grace16(Grace16Type):
    class Meta:
        name = "grace16"


@dataclass(kw_only=True)
class Grace16After(Grace16AfterType):
    class Meta:
        name = "grace16after"


@dataclass(kw_only=True)
class Grace32(Grace32Type):
    class Meta:
        name = "grace32"


@dataclass(kw_only=True)
class Grace32After(Grace32AfterType):
    class Meta:
        name = "grace32after"


@dataclass(kw_only=True)
class Grace4(Grace4Type):
    class Meta:
        name = "grace4"


@dataclass(kw_only=True)
class Grace8After(Grace8AfterType):
    class Meta:
        name = "grace8after"


@dataclass(kw_only=True)
class GraceNoteMag(GraceNoteMagType):
    class Meta:
        name = "graceNoteMag"


@dataclass(kw_only=True)
class Grid(GridType):
    class Meta:
        name = "grid"


@dataclass(kw_only=True)
class GridHeight(GridHeightType):
    class Meta:
        name = "gridHeight"


@dataclass(kw_only=True)
class GridWidth(GridWidthType):
    class Meta:
        name = "gridWidth"


@dataclass(kw_only=True)
class Group(GroupType):
    class Meta:
        name = "group"


@dataclass(kw_only=True)
class GroupAbbreviation(GroupAbbreviationType):
    class Meta:
        name = "group-abbreviation"


@dataclass(kw_only=True)
class GroupBarline(GroupBarlineType):
    class Meta:
        name = "group-barline"


@dataclass(kw_only=True)
class GroupName(GroupNameType):
    class Meta:
        name = "group-name"


@dataclass(kw_only=True)
class GroupSymbol(GroupSymbolType):
    class Meta:
        name = "group-symbol"


@dataclass(kw_only=True)
class GrowLeft(GrowLeftType):
    class Meta:
        name = "growLeft"


@dataclass(kw_only=True)
class GrowRight(GrowRightType):
    class Meta:
        name = "growRight"


@dataclass(kw_only=True)
class Guitar(GuitarType):
    class Meta:
        name = "guitar"


@dataclass(kw_only=True)
class HairpinCircledTip(HairpinCircledTipType):
    class Meta:
        name = "hairpinCircledTip"


@dataclass(kw_only=True)
class HairpinContHeight(HairpinContHeightType):
    class Meta:
        name = "hairpinContHeight"


@dataclass(kw_only=True)
class HairpinFontFace(HairpinFontFaceType):
    class Meta:
        name = "hairpinFontFace"


@dataclass(kw_only=True)
class HairpinFontSize(HairpinFontSizeType):
    class Meta:
        name = "hairpinFontSize"


@dataclass(kw_only=True)
class HairpinFramePadding(HairpinFramePaddingType):
    class Meta:
        name = "hairpinFramePadding"


@dataclass(kw_only=True)
class HairpinFrameWidth(HairpinFrameWidthType):
    class Meta:
        name = "hairpinFrameWidth"


@dataclass(kw_only=True)
class HairpinHeight(HairpinHeightType):
    class Meta:
        name = "hairpinHeight"


@dataclass(kw_only=True)
class HairpinWidth(HairpinWidthType):
    class Meta:
        name = "hairpinWidth"


@dataclass(kw_only=True)
class Half(HalfType):
    class Meta:
        name = "half"


@dataclass(kw_only=True)
class HalfCurve(HalfCurveType):
    class Meta:
        name = "half-curve"


@dataclass(kw_only=True)
class Halign(HalignType):
    class Meta:
        name = "halign"


@dataclass(kw_only=True)
class Harmonic(HarmonicType):
    class Meta:
        name = "harmonic"


@dataclass(kw_only=True)
class HarmonyDuration(HarmonyDurationType):
    class Meta:
        name = "harmonyDuration"


@dataclass(kw_only=True)
class HarmonyFretDist(HarmonyFretDistType):
    class Meta:
        name = "harmonyFretDist"


@dataclass(kw_only=True)
class HarmonyPlay(HarmonyPlayType):
    class Meta:
        name = "harmonyPlay"


@dataclass(kw_only=True)
class HarmonyType(HarmonyTypeType):
    class Meta:
        name = "harmonyType"


@dataclass(kw_only=True)
class HarmonyVoiceLiteral(HarmonyVoiceLiteralType):
    class Meta:
        name = "harmonyVoiceLiteral"


@dataclass(kw_only=True)
class HarmonyVoicing(HarmonyVoicingType):
    class Meta:
        name = "harmonyVoicing"


@dataclass(kw_only=True)
class HarmonyY(HarmonyYtype):
    class Meta:
        name = "harmonyY"


@dataclass(kw_only=True)
class Harmony2(HarmonyType2):
    class Meta:
        name = "harmony"


@dataclass(kw_only=True)
class HasLine(HasLineType):
    class Meta:
        name = "hasLine"


@dataclass(kw_only=True)
class HasNumber(HasNumberType):
    class Meta:
        name = "hasNumber"


@dataclass(kw_only=True)
class HeadScheme(HeadSchemeType):
    class Meta:
        name = "headScheme"


@dataclass(kw_only=True)
class HeadType(HeadTypeType):
    class Meta:
        name = "headType"


@dataclass(kw_only=True)
class Header(HeaderType):
    class Meta:
        name = "header"


@dataclass(kw_only=True)
class HeaderAlign(HeaderAlignType):
    class Meta:
        name = "headerAlign"


@dataclass(kw_only=True)
class HeaderFirstPage(HeaderFirstPageType):
    class Meta:
        name = "headerFirstPage"


@dataclass(kw_only=True)
class HeaderFontBold(HeaderFontBoldType):
    class Meta:
        name = "headerFontBold"


@dataclass(kw_only=True)
class HeaderFontFace(HeaderFontFaceType):
    class Meta:
        name = "headerFontFace"


@dataclass(kw_only=True)
class HeaderFontSize(HeaderFontSizeType):
    class Meta:
        name = "headerFontSize"


@dataclass(kw_only=True)
class HeaderFontStyle(HeaderFontStyleType):
    class Meta:
        name = "headerFontStyle"


@dataclass(kw_only=True)
class HeaderFramePadding(HeaderFramePaddingType):
    class Meta:
        name = "headerFramePadding"


@dataclass(kw_only=True)
class HeaderFrameWidth(HeaderFrameWidthType):
    class Meta:
        name = "headerFrameWidth"


@dataclass(kw_only=True)
class Heads(HeadsType):
    class Meta:
        name = "heads"


@dataclass(kw_only=True)
class Height(HeightType):
    class Meta:
        name = "height"


@dataclass(kw_only=True)
class HideEmptyStaves(HideEmptyStavesType):
    class Meta:
        name = "hideEmptyStaves"


@dataclass(kw_only=True)
class HideInstrumentNameIfOneInstrument(HideInstrumentNameIfOneInstrumentType):
    class Meta:
        name = "hideInstrumentNameIfOneInstrument"


@dataclass(kw_only=True)
class HideSystemBarLine(HideSystemBarLineType):
    class Meta:
        name = "hideSystemBarLine"


@dataclass(kw_only=True)
class HideWhenEmpty(HideWhenEmptyType):
    class Meta:
        name = "hideWhenEmpty"


@dataclass(kw_only=True)
class HookHeight(HookHeightType):
    class Meta:
        name = "hookHeight"


@dataclass(kw_only=True)
class HookUp(HookUpType):
    class Meta:
        name = "hookUp"


@dataclass(kw_only=True)
class Id(IdType):
    class Meta:
        name = "id"


@dataclass(kw_only=True)
class Identification(IdentificationType):
    class Meta:
        name = "identification"


@dataclass(kw_only=True)
class Idx(IdxType):
    class Meta:
        name = "idx"


@dataclass(kw_only=True)
class IndexDiff(IndexDiffType):
    class Meta:
        name = "indexDiff"


@dataclass(kw_only=True)
class Info(InfoType):
    class Meta:
        name = "info"


@dataclass(kw_only=True)
class InfoUrl(InfoUrlType):
    class Meta:
        name = "infoUrl"


@dataclass(kw_only=True)
class Init(InitType):
    class Meta:
        name = "init"


@dataclass(kw_only=True)
class InstrumentGroup2(InstrumentGroupType2):
    class Meta:
        name = "instrument-group"


@dataclass(kw_only=True)
class InstrumentName(InstrumentNameType):
    class Meta:
        name = "instrument-name"


@dataclass(kw_only=True)
class InstrumentSound(InstrumentSoundType):
    class Meta:
        name = "instrument-sound"


@dataclass(kw_only=True)
class InstrumentChangeAlign(InstrumentChangeAlignType):
    class Meta:
        name = "instrumentChangeAlign"


@dataclass(kw_only=True)
class InstrumentChangeFontFace(InstrumentChangeFontFaceType):
    class Meta:
        name = "instrumentChangeFontFace"


@dataclass(kw_only=True)
class InstrumentChangeFontSize(InstrumentChangeFontSizeType):
    class Meta:
        name = "instrumentChangeFontSize"


@dataclass(kw_only=True)
class InstrumentChangeFramePadding(InstrumentChangeFramePaddingType):
    class Meta:
        name = "instrumentChangeFramePadding"


@dataclass(kw_only=True)
class InstrumentChangeFrameWidth(InstrumentChangeFrameWidthType):
    class Meta:
        name = "instrumentChangeFrameWidth"


@dataclass(kw_only=True)
class InstrumentId(InstrumentIdType):
    class Meta:
        name = "instrumentId"


@dataclass(kw_only=True)
class InstrumentNames(InstrumentNamesType):
    class Meta:
        name = "instrumentNames"


@dataclass(kw_only=True)
class Instruments(InstrumentsType):
    class Meta:
        name = "instruments"


@dataclass(kw_only=True)
class Inters(IntersType):
    class Meta:
        name = "inters"


@dataclass(kw_only=True)
class Inversion(InversionType):
    class Meta:
        name = "inversion"


@dataclass(kw_only=True)
class Inverted(InvertedType):
    class Meta:
        name = "inverted"


@dataclass(kw_only=True)
class InvertedMordent(InvertedMordentType):
    class Meta:
        name = "inverted-mordent"


@dataclass(kw_only=True)
class InvertedTurn(InvertedTurnType):
    class Meta:
        name = "inverted-turn"


@dataclass(kw_only=True)
class Invisible(InvisibleType):
    class Meta:
        name = "invisible"


@dataclass(kw_only=True)
class Irregular(IrregularType):
    class Meta:
        name = "irregular"


@dataclass(kw_only=True)
class Italic(ItalicType):
    class Meta:
        name = "italic"


@dataclass(kw_only=True)
class JumpTo(JumpToType):
    class Meta:
        name = "jumpTo"


@dataclass(kw_only=True)
class KeyAccidental(KeyAccidentalType):
    class Meta:
        name = "key-accidental"


@dataclass(kw_only=True)
class KeyAlter(KeyAlterType):
    class Meta:
        name = "key-alter"


@dataclass(kw_only=True)
class KeyStep(KeyStepType):
    class Meta:
        name = "key-step"


@dataclass(kw_only=True)
class KeySigNaturals(KeySigNaturalsType):
    class Meta:
        name = "keySigNaturals"


@dataclass(kw_only=True)
class KeySign(KeySignType):
    class Meta:
        name = "keySign"


@dataclass(kw_only=True)
class Key2(KeyType2):
    class Meta:
        name = "key"


@dataclass(kw_only=True)
class KeysigLeftMargin(KeysigLeftMarginType):
    class Meta:
        name = "keysigLeftMargin"


@dataclass(kw_only=True)
class Keysig2(KeysigType2):
    class Meta:
        name = "keysig"


@dataclass(kw_only=True)
class Kind(KindType):
    class Meta:
        name = "kind"


@dataclass(kw_only=True)
class L1(L1Type):
    class Meta:
        name = "l1"


@dataclass(kw_only=True)
class L2(L2Type):
    class Meta:
        name = "l2"


@dataclass(kw_only=True)
class La(LaType):
    class Meta:
        name = "la"


@dataclass(kw_only=True)
class Label(LabelType):
    class Meta:
        name = "label"


@dataclass(kw_only=True)
class Landscape(LandscapeType):
    class Meta:
        name = "landscape"


@dataclass(kw_only=True)
class LastSystemFillLimit(LastSystemFillLimitType):
    class Meta:
        name = "lastSystemFillLimit"


@dataclass(kw_only=True)
class Layout(LayoutType):
    class Meta:
        name = "layout"


@dataclass(kw_only=True)
class LayoutMode(LayoutModeType):
    class Meta:
        name = "layoutMode"


@dataclass(kw_only=True)
class LayoutOffset(LayoutOffsetType):
    class Meta:
        name = "layoutOffset"


@dataclass(kw_only=True)
class LeadingSpace(LeadingSpaceType):
    class Meta:
        name = "leadingSpace"


@dataclass(kw_only=True)
class LedgerLineLength(LedgerLineLengthType):
    class Meta:
        name = "ledgerLineLength"


@dataclass(kw_only=True)
class LedgerLineWidth(LedgerLineWidthType):
    class Meta:
        name = "ledgerLineWidth"


@dataclass(kw_only=True)
class Ledgerlines(LedgerlinesType):
    class Meta:
        name = "ledgerlines"


@dataclass(kw_only=True)
class LeftMargin1(LeftMarginType1):
    class Meta:
        name = "left-margin"


@dataclass(kw_only=True)
class LeftMargin2(LeftMarginType2):
    class Meta:
        name = "leftMargin"


@dataclass(kw_only=True)
class LeftParen(LeftParenType):
    class Meta:
        name = "leftParen"


@dataclass(kw_only=True)
class Len(LenType):
    class Meta:
        name = "len"


@dataclass(kw_only=True)
class Length(LengthType):
    class Meta:
        name = "length"


@dataclass(kw_only=True)
class LengthX(LengthXtype):
    class Meta:
        name = "lengthX"


@dataclass(kw_only=True)
class LengthY(LengthYtype):
    class Meta:
        name = "lengthY"


@dataclass(kw_only=True)
class LetRingFontFace(LetRingFontFaceType):
    class Meta:
        name = "letRingFontFace"


@dataclass(kw_only=True)
class Level(LevelType):
    class Meta:
        name = "level"


@dataclass(kw_only=True)
class LhGuitarFingeringFontFace(LhGuitarFingeringFontFaceType):
    class Meta:
        name = "lhGuitarFingeringFontFace"


@dataclass(kw_only=True)
class LhGuitarFingeringFontSize(LhGuitarFingeringFontSizeType):
    class Meta:
        name = "lhGuitarFingeringFontSize"


@dataclass(kw_only=True)
class LhGuitarFingeringFramePadding(LhGuitarFingeringFramePaddingType):
    class Meta:
        name = "lhGuitarFingeringFramePadding"


@dataclass(kw_only=True)
class LhGuitarFingeringFrameRound(LhGuitarFingeringFrameRoundType):
    class Meta:
        name = "lhGuitarFingeringFrameRound"


@dataclass(kw_only=True)
class LhGuitarFingeringFrameWidth(LhGuitarFingeringFrameWidthType):
    class Meta:
        name = "lhGuitarFingeringFrameWidth"


@dataclass(kw_only=True)
class Lid(LidType):
    class Meta:
        name = "lid"


@dataclass(kw_only=True)
class Line(LineType1):
    class Meta:
        name = "line"


@dataclass(kw_only=True)
class LineColor(LineColorType):
    class Meta:
        name = "lineColor"


@dataclass(kw_only=True)
class LineDistance(LineDistanceType):
    class Meta:
        name = "lineDistance"


@dataclass(kw_only=True)
class LineLen(LineLenType):
    class Meta:
        name = "lineLen"


@dataclass(kw_only=True)
class LineStyle(LineStyleType):
    class Meta:
        name = "lineStyle"


@dataclass(kw_only=True)
class LineType(LineTypeType):
    class Meta:
        name = "lineType"


@dataclass(kw_only=True)
class LineVisible(LineVisibleType):
    class Meta:
        name = "lineVisible"


@dataclass(kw_only=True)
class LineWidth(LineWidthType):
    class Meta:
        name = "lineWidth"


@dataclass(kw_only=True)
class Lines(LinesType):
    class Meta:
        name = "lines"


@dataclass(kw_only=True)
class LinesThrough(LinesThroughType):
    class Meta:
        name = "linesThrough"


@dataclass(kw_only=True)
class LinkPath(LinkPathType):
    class Meta:
        name = "linkPath"


@dataclass(kw_only=True)
class LinkedMain(LinkedMainType):
    class Meta:
        name = "linkedMain"


@dataclass(kw_only=True)
class LinkedTo(LinkedToType):
    class Meta:
        name = "linkedTo"


@dataclass(kw_only=True)
class Load(LoadType):
    class Meta:
        name = "load"


@dataclass(kw_only=True)
class LockAspectRatio(LockAspectRatioType):
    class Meta:
        name = "lockAspectRatio"


@dataclass(kw_only=True)
class LongInstrumentAlign(LongInstrumentAlignType):
    class Meta:
        name = "longInstrumentAlign"


@dataclass(kw_only=True)
class LongInstrumentFontFace(LongInstrumentFontFaceType):
    class Meta:
        name = "longInstrumentFontFace"


@dataclass(kw_only=True)
class LongInstrumentFontSize(LongInstrumentFontSizeType):
    class Meta:
        name = "longInstrumentFontSize"


@dataclass(kw_only=True)
class LongInstrumentFramePadding(LongInstrumentFramePaddingType):
    class Meta:
        name = "longInstrumentFramePadding"


@dataclass(kw_only=True)
class LongInstrumentFrameWidth(LongInstrumentFrameWidthType):
    class Meta:
        name = "longInstrumentFrameWidth"


@dataclass(kw_only=True)
class LowerCaseBassNotes(LowerCaseBassNotesType):
    class Meta:
        name = "lowerCaseBassNotes"


@dataclass(kw_only=True)
class LowerCaseMinorChords(LowerCaseMinorChordsType):
    class Meta:
        name = "lowerCaseMinorChords"


@dataclass(kw_only=True)
class LyricFont(LyricFontType):
    class Meta:
        name = "lyric-font"


@dataclass(kw_only=True)
class LyricLanguage(LyricLanguageType):
    class Meta:
        name = "lyric-language"


@dataclass(kw_only=True)
class Lyric2(LyricType2):
    class Meta:
        name = "lyric"


@dataclass(kw_only=True)
class Lyricist(LyricistType):
    class Meta:
        name = "lyricist"


@dataclass(kw_only=True)
class LyricistFontFace(LyricistFontFaceType):
    class Meta:
        name = "lyricistFontFace"


@dataclass(kw_only=True)
class LyricistFontSize(LyricistFontSizeType):
    class Meta:
        name = "lyricistFontSize"


@dataclass(kw_only=True)
class LyricistFramePadding(LyricistFramePaddingType):
    class Meta:
        name = "lyricistFramePadding"


@dataclass(kw_only=True)
class LyricistFrameRound(LyricistFrameRoundType):
    class Meta:
        name = "lyricistFrameRound"


@dataclass(kw_only=True)
class LyricistFrameWidth(LyricistFrameWidthType):
    class Meta:
        name = "lyricistFrameWidth"


@dataclass(kw_only=True)
class LyricsDashForce(LyricsDashForceType):
    class Meta:
        name = "lyricsDashForce"


@dataclass(kw_only=True)
class LyricsDashMaxLegth(LyricsDashMaxLegthType):
    class Meta:
        name = "lyricsDashMaxLegth"


@dataclass(kw_only=True)
class LyricsDashYposRatio(LyricsDashYposRatioType):
    class Meta:
        name = "lyricsDashYposRatio"


@dataclass(kw_only=True)
class LyricsDistance(LyricsDistanceType):
    class Meta:
        name = "lyricsDistance"


@dataclass(kw_only=True)
class LyricsEvenFontFace(LyricsEvenFontFaceType):
    class Meta:
        name = "lyricsEvenFontFace"


@dataclass(kw_only=True)
class LyricsEvenFontSize(LyricsEvenFontSizeType):
    class Meta:
        name = "lyricsEvenFontSize"


@dataclass(kw_only=True)
class LyricsEvenFramePadding(LyricsEvenFramePaddingType):
    class Meta:
        name = "lyricsEvenFramePadding"


@dataclass(kw_only=True)
class LyricsEvenFrameWidth(LyricsEvenFrameWidthType):
    class Meta:
        name = "lyricsEvenFrameWidth"


@dataclass(kw_only=True)
class LyricsEvenOffset(LyricsEvenOffsetType):
    class Meta:
        name = "lyricsEvenOffset"


@dataclass(kw_only=True)
class LyricsLineThickness(LyricsLineThicknessType):
    class Meta:
        name = "lyricsLineThickness"


@dataclass(kw_only=True)
class LyricsMinBottomDistance(LyricsMinBottomDistanceType):
    class Meta:
        name = "lyricsMinBottomDistance"


@dataclass(kw_only=True)
class LyricsMinDistance(LyricsMinDistanceType):
    class Meta:
        name = "lyricsMinDistance"


@dataclass(kw_only=True)
class LyricsOddFontFace(LyricsOddFontFaceType):
    class Meta:
        name = "lyricsOddFontFace"


@dataclass(kw_only=True)
class LyricsOddFontSize(LyricsOddFontSizeType):
    class Meta:
        name = "lyricsOddFontSize"


@dataclass(kw_only=True)
class LyricsOddFramePadding(LyricsOddFramePaddingType):
    class Meta:
        name = "lyricsOddFramePadding"


@dataclass(kw_only=True)
class LyricsOddFrameWidth(LyricsOddFrameWidthType):
    class Meta:
        name = "lyricsOddFrameWidth"


@dataclass(kw_only=True)
class LyricsOddOffset(LyricsOddOffsetType):
    class Meta:
        name = "lyricsOddOffset"


@dataclass(kw_only=True)
class LyricsPosBelow(LyricsPosBelowType):
    class Meta:
        name = "lyricsPosBelow"


@dataclass(kw_only=True)
class LyricsSettings(LyricsSettingsType):
    class Meta:
        name = "lyricsSettings"


@dataclass(kw_only=True)
class MagIdx2(MagIdxType2):
    class Meta:
        name = "magIdx"


@dataclass(kw_only=True)
class Mag2(MagType2):
    class Meta:
        name = "mag"


@dataclass(kw_only=True)
class Mark(MarkType):
    class Meta:
        name = "mark"


@dataclass(kw_only=True)
class MarkIrregularMeasures(MarkIrregularMeasuresType):
    class Meta:
        name = "markIrregularMeasures"


@dataclass(kw_only=True)
class Marker2(MarkerType2):
    class Meta:
        name = "marker"


@dataclass(kw_only=True)
class MaxChordShiftAbove(MaxChordShiftAboveType):
    class Meta:
        name = "maxChordShiftAbove"


@dataclass(kw_only=True)
class MaxChordShiftBelow(MaxChordShiftBelowType):
    class Meta:
        name = "maxChordShiftBelow"


@dataclass(kw_only=True)
class MaxFretShiftAbove(MaxFretShiftAboveType):
    class Meta:
        name = "maxFretShiftAbove"


@dataclass(kw_only=True)
class MaxFretShiftBelow(MaxFretShiftBelowType):
    class Meta:
        name = "maxFretShiftBelow"


@dataclass(kw_only=True)
class MaxHarmonyBarDistance(MaxHarmonyBarDistanceType):
    class Meta:
        name = "maxHarmonyBarDistance"


@dataclass(kw_only=True)
class MaxPageFillSpread(MaxPageFillSpreadType):
    class Meta:
        name = "maxPageFillSpread"


@dataclass(kw_only=True)
class MaxPitch(MaxPitchType):
    class Meta:
        name = "maxPitch"


@dataclass(kw_only=True)
class MaxPitchA(MaxPitchAtype):
    class Meta:
        name = "maxPitchA"


@dataclass(kw_only=True)
class MaxPitchP(MaxPitchPtype):
    class Meta:
        name = "maxPitchP"


@dataclass(kw_only=True)
class MaxSystemDistance(MaxSystemDistanceType):
    class Meta:
        name = "maxSystemDistance"


@dataclass(kw_only=True)
class MeasureStyle(MeasureStyleType):
    class Meta:
        name = "measure-style"


@dataclass(kw_only=True)
class MeasureNumberAlign(MeasureNumberAlignType):
    class Meta:
        name = "measureNumberAlign"


@dataclass(kw_only=True)
class MeasureNumberAllStaffs(MeasureNumberAllStaffsType):
    class Meta:
        name = "measureNumberAllStaffs"


@dataclass(kw_only=True)
class MeasureNumberFontFace(MeasureNumberFontFaceType):
    class Meta:
        name = "measureNumberFontFace"


@dataclass(kw_only=True)
class MeasureNumberFontSize(MeasureNumberFontSizeType):
    class Meta:
        name = "measureNumberFontSize"


@dataclass(kw_only=True)
class MeasureNumberFontSpatiumDependent(MeasureNumberFontSpatiumDependentType):
    class Meta:
        name = "measureNumberFontSpatiumDependent"


@dataclass(kw_only=True)
class MeasureNumberFontStyle(MeasureNumberFontStyleType):
    class Meta:
        name = "measureNumberFontStyle"


@dataclass(kw_only=True)
class MeasureNumberFramePadding(MeasureNumberFramePaddingType):
    class Meta:
        name = "measureNumberFramePadding"


@dataclass(kw_only=True)
class MeasureNumberFrameWidth(MeasureNumberFrameWidthType):
    class Meta:
        name = "measureNumberFrameWidth"


@dataclass(kw_only=True)
class MeasureNumberHplacement(MeasureNumberHplacementType):
    class Meta:
        name = "measureNumberHPlacement"


@dataclass(kw_only=True)
class MeasureNumberInterval(MeasureNumberIntervalType):
    class Meta:
        name = "measureNumberInterval"


@dataclass(kw_only=True)
class MeasureNumberMode(MeasureNumberModeType):
    class Meta:
        name = "measureNumberMode"


@dataclass(kw_only=True)
class MeasureNumberOffset(MeasureNumberOffsetType):
    class Meta:
        name = "measureNumberOffset"


@dataclass(kw_only=True)
class MeasureNumberPosAbove(MeasureNumberPosAboveType):
    class Meta:
        name = "measureNumberPosAbove"


@dataclass(kw_only=True)
class MeasureNumberPosBelow(MeasureNumberPosBelowType):
    class Meta:
        name = "measureNumberPosBelow"


@dataclass(kw_only=True)
class MeasureNumberSystem(MeasureNumberSystemType):
    class Meta:
        name = "measureNumberSystem"


@dataclass(kw_only=True)
class MeasureNumberVplacement(MeasureNumberVplacementType):
    class Meta:
        name = "measureNumberVPlacement"


@dataclass(kw_only=True)
class MeasureSpacing(MeasureSpacingType):
    class Meta:
        name = "measureSpacing"


@dataclass(kw_only=True)
class Measure2(MeasureType2):
    class Meta:
        name = "measure"


@dataclass(kw_only=True)
class Measures(MeasuresType):
    class Meta:
        name = "measures"


@dataclass(kw_only=True)
class MergeMatchingRests(MergeMatchingRestsType):
    class Meta:
        name = "mergeMatchingRests"


@dataclass(kw_only=True)
class MetaTag(MetaTagType):
    class Meta:
        name = "metaTag"


@dataclass(kw_only=True)
class Meta2(MetaType2):
    class Meta:
        name = "meta"


@dataclass(kw_only=True)
class Metafile(MetafileType):
    class Meta:
        name = "metafile"


@dataclass(kw_only=True)
class Metronome(MetronomeType):
    class Meta:
        name = "metronome"


@dataclass(kw_only=True)
class MetronomeNote(MetronomeNoteType):
    class Meta:
        name = "metronome-note"


@dataclass(kw_only=True)
class MetronomeRelation(MetronomeRelationType):
    class Meta:
        name = "metronome-relation"


@dataclass(kw_only=True)
class MetronomeFontFace(MetronomeFontFaceType):
    class Meta:
        name = "metronomeFontFace"


@dataclass(kw_only=True)
class MetronomeFontSize(MetronomeFontSizeType):
    class Meta:
        name = "metronomeFontSize"


@dataclass(kw_only=True)
class MetronomeFontStyle(MetronomeFontStyleType):
    class Meta:
        name = "metronomeFontStyle"


@dataclass(kw_only=True)
class MetronomeFramePadding(MetronomeFramePaddingType):
    class Meta:
        name = "metronomeFramePadding"


@dataclass(kw_only=True)
class MetronomeFrameWidth(MetronomeFrameWidthType):
    class Meta:
        name = "metronomeFrameWidth"


@dataclass(kw_only=True)
class Mi(MiType):
    class Meta:
        name = "mi"


@dataclass(kw_only=True)
class MidiBank(MidiBankType):
    class Meta:
        name = "midi-bank"


@dataclass(kw_only=True)
class MidiChannel1(MidiChannelType1):
    class Meta:
        name = "midi-channel"


@dataclass(kw_only=True)
class MidiDevice(MidiDeviceType):
    class Meta:
        name = "midi-device"


@dataclass(kw_only=True)
class MidiInstrument(MidiInstrumentType):
    class Meta:
        name = "midi-instrument"


@dataclass(kw_only=True)
class MidiProgram1(MidiProgramType1):
    class Meta:
        name = "midi-program"


@dataclass(kw_only=True)
class MidiUnpitched(MidiUnpitchedType):
    class Meta:
        name = "midi-unpitched"


@dataclass(kw_only=True)
class MidiChannel2(MidiChannelType2):
    class Meta:
        name = "midiChannel"


@dataclass(kw_only=True)
class MidiPort(MidiPortType):
    class Meta:
        name = "midiPort"


@dataclass(kw_only=True)
class MidiProgram2(MidiProgramType2):
    class Meta:
        name = "midiProgram"


@dataclass(kw_only=True)
class Millimeters(MillimetersType):
    class Meta:
        name = "millimeters"


@dataclass(kw_only=True)
class MinDistance(MinDistanceType):
    class Meta:
        name = "minDistance"


@dataclass(kw_only=True)
class MinEmptyMeasures(MinEmptyMeasuresType):
    class Meta:
        name = "minEmptyMeasures"


@dataclass(kw_only=True)
class MinHarmonyDistance(MinHarmonyDistanceType):
    class Meta:
        name = "minHarmonyDistance"


@dataclass(kw_only=True)
class MinMmrestWidth(MinMmrestWidthType):
    class Meta:
        name = "minMMRestWidth"


@dataclass(kw_only=True)
class MinMeasureWidth(MinMeasureWidthType):
    class Meta:
        name = "minMeasureWidth"


@dataclass(kw_only=True)
class MinNoteDistance(MinNoteDistanceType):
    class Meta:
        name = "minNoteDistance"


@dataclass(kw_only=True)
class MinPitch(MinPitchType):
    class Meta:
        name = "minPitch"


@dataclass(kw_only=True)
class MinPitchA(MinPitchAtype):
    class Meta:
        name = "minPitchA"


@dataclass(kw_only=True)
class MinPitchP(MinPitchPtype):
    class Meta:
        name = "minPitchP"


@dataclass(kw_only=True)
class MinSystemDistance(MinSystemDistanceType):
    class Meta:
        name = "minSystemDistance"


@dataclass(kw_only=True)
class MinimStyle(MinimStyleType):
    class Meta:
        name = "minimStyle"


@dataclass(kw_only=True)
class Mirror(MirrorType):
    class Meta:
        name = "mirror"


@dataclass(kw_only=True)
class Miscellaneous(MiscellaneousType):
    class Meta:
        name = "miscellaneous"


@dataclass(kw_only=True)
class MmRestNumberPos(MmRestNumberPosType):
    class Meta:
        name = "mmRestNumberPos"


@dataclass(kw_only=True)
class MmRestRangeBracketType(MmRestRangeBracketTypeType):
    class Meta:
        name = "mmRestRangeBracketType"


@dataclass(kw_only=True)
class MmRestRangeFontSize(MmRestRangeFontSizeType):
    class Meta:
        name = "mmRestRangeFontSize"


@dataclass(kw_only=True)
class MmRestRangeVplacement(MmRestRangeVplacementType):
    class Meta:
        name = "mmRestRangeVPlacement"


@dataclass(kw_only=True)
class MmRestShowMeasureNumberRange(MmRestShowMeasureNumberRangeType):
    class Meta:
        name = "mmRestShowMeasureNumberRange"


@dataclass(kw_only=True)
class Mode(ModeType):
    class Meta:
        name = "mode"


@dataclass(kw_only=True)
class Mordent(MordentType):
    class Meta:
        name = "mordent"


@dataclass(kw_only=True)
class MoreElements(MoreElementsType):
    class Meta:
        name = "moreElements"


@dataclass(kw_only=True)
class Move(MoveType):
    class Meta:
        name = "move"


@dataclass(kw_only=True)
class MovementNumber1(MovementNumberType1):
    class Meta:
        name = "movement-number"


@dataclass(kw_only=True)
class MovementTitle1(MovementTitleType1):
    class Meta:
        name = "movement-title"


@dataclass(kw_only=True)
class MovementNumber2(MovementNumberType2):
    class Meta:
        name = "movementNumber"


@dataclass(kw_only=True)
class MovementTitle2(MovementTitleType2):
    class Meta:
        name = "movementTitle"


@dataclass(kw_only=True)
class MultiMeasureRest(MultiMeasureRestType):
    class Meta:
        name = "multiMeasureRest"


@dataclass(kw_only=True)
class MultipleRest(MultipleRestType):
    class Meta:
        name = "multiple-rest"


@dataclass(kw_only=True)
class MusicFont(MusicFontType):
    class Meta:
        name = "music-font"


@dataclass(kw_only=True)
class MusicXmlid(MusicXmlidType):
    class Meta:
        name = "musicXMLid"


@dataclass(kw_only=True)
class MusicalSymbolFont(MusicalSymbolFontType):
    class Meta:
        name = "musicalSymbolFont"


@dataclass(kw_only=True)
class MusicalTextFont(MusicalTextFontType):
    class Meta:
        name = "musicalTextFont"


@dataclass(kw_only=True)
class Mute(MuteType):
    class Meta:
        name = "mute"


@dataclass(kw_only=True)
class NashvilleNumberFontFace(NashvilleNumberFontFaceType):
    class Meta:
        name = "nashvilleNumberFontFace"


@dataclass(kw_only=True)
class NashvilleNumberFontSize(NashvilleNumberFontSizeType):
    class Meta:
        name = "nashvilleNumberFontSize"


@dataclass(kw_only=True)
class Natural(NaturalType):
    class Meta:
        name = "natural"


@dataclass(kw_only=True)
class NeverHide(NeverHideType):
    class Meta:
        name = "neverHide"


@dataclass(kw_only=True)
class No(NoType):
    class Meta:
        name = "no"


@dataclass(kw_only=True)
class NoOffset(NoOffsetType):
    class Meta:
        name = "noOffset"


@dataclass(kw_only=True)
class NoStem(NoStemType):
    class Meta:
        name = "noStem"


@dataclass(kw_only=True)
class Nom(NomType):
    class Meta:
        name = "nom"


@dataclass(kw_only=True)
class Nom1(Nom1Type):
    class Meta:
        name = "nom1"


@dataclass(kw_only=True)
class Nom2(Nom2Type):
    class Meta:
        name = "nom2"


@dataclass(kw_only=True)
class Nom3(Nom3Type):
    class Meta:
        name = "nom3"


@dataclass(kw_only=True)
class Nom4(Nom4Type):
    class Meta:
        name = "nom4"


@dataclass(kw_only=True)
class NonArpeggiate(NonArpeggiateType):
    class Meta:
        name = "non-arpeggiate"


@dataclass(kw_only=True)
class Normal(NormalType1):
    class Meta:
        name = "normal"


@dataclass(kw_only=True)
class NormalDot(NormalDotType):
    class Meta:
        name = "normal-dot"


@dataclass(kw_only=True)
class NormalNotes1(NormalNotesType1):
    class Meta:
        name = "normal-notes"


@dataclass(kw_only=True)
class NormalType(NormalTypeType):
    class Meta:
        name = "normal-type"


@dataclass(kw_only=True)
class NormalNotes2(NormalNotesType2):
    class Meta:
        name = "normalNotes"


@dataclass(kw_only=True)
class Notation(NotationType):
    class Meta:
        name = "notation"


@dataclass(kw_only=True)
class Notations(NotationsType):
    class Meta:
        name = "notations"


@dataclass(kw_only=True)
class NoteOff2(NoteOffType2):
    class Meta:
        name = "note-off"


@dataclass(kw_only=True)
class NoteOn2(NoteOnType2):
    class Meta:
        name = "note-on"


@dataclass(kw_only=True)
class NoteBarDistance(NoteBarDistanceType):
    class Meta:
        name = "noteBarDistance"


@dataclass(kw_only=True)
class NoteObjects(NoteObjectsType):
    class Meta:
        name = "noteObjects"


@dataclass(kw_only=True)
class Note2(NoteType2):
    class Meta:
        name = "note"


@dataclass(kw_only=True)
class Notehead(NoteheadType):
    class Meta:
        name = "notehead"


@dataclass(kw_only=True)
class NoteheadScheme(NoteheadSchemeType):
    class Meta:
        name = "noteheadScheme"


@dataclass(kw_only=True)
class Notelines(NotelinesType):
    class Meta:
        name = "notelines"


@dataclass(kw_only=True)
class Notes(NotesType):
    class Meta:
        name = "notes"


@dataclass(kw_only=True)
class NumberType(NumberTypeType):
    class Meta:
        name = "numberType"


@dataclass(kw_only=True)
class NumbersOnly(NumbersOnlyType):
    class Meta:
        name = "numbersOnly"


@dataclass(kw_only=True)
class O1(O1Type):
    class Meta:
        name = "o1"


@dataclass(kw_only=True)
class O2(O2Type):
    class Meta:
        name = "o2"


@dataclass(kw_only=True)
class O3(O3Type):
    class Meta:
        name = "o3"


@dataclass(kw_only=True)
class O4(O4Type):
    class Meta:
        name = "o4"


@dataclass(kw_only=True)
class Octave(OctaveType):
    class Meta:
        name = "octave"


@dataclass(kw_only=True)
class OctaveChange(OctaveChangeType):
    class Meta:
        name = "octave-change"


@dataclass(kw_only=True)
class OctaveShift(OctaveShiftType):
    class Meta:
        name = "octave-shift"


@dataclass(kw_only=True)
class OddFooter(OddFooterType):
    class Meta:
        name = "oddFooter"


@dataclass(kw_only=True)
class OddFooterC(OddFooterCtype):
    class Meta:
        name = "oddFooterC"


@dataclass(kw_only=True)
class OddFooterL(OddFooterLtype):
    class Meta:
        name = "oddFooterL"


@dataclass(kw_only=True)
class OddFooterR(OddFooterRtype):
    class Meta:
        name = "oddFooterR"


@dataclass(kw_only=True)
class OddHeader(OddHeaderType):
    class Meta:
        name = "oddHeader"


@dataclass(kw_only=True)
class OddHeaderC(OddHeaderCtype):
    class Meta:
        name = "oddHeaderC"


@dataclass(kw_only=True)
class OddHeaderL(OddHeaderLtype):
    class Meta:
        name = "oddHeaderL"


@dataclass(kw_only=True)
class OddHeaderR(OddHeaderRtype):
    class Meta:
        name = "oddHeaderR"


@dataclass(kw_only=True)
class Off1(Off1Type):
    class Meta:
        name = "off1"


@dataclass(kw_only=True)
class Off2(Off2Type):
    class Meta:
        name = "off2"


@dataclass(kw_only=True)
class OffTimeOffset(OffTimeOffsetType):
    class Meta:
        name = "offTimeOffset"


@dataclass(kw_only=True)
class OffTimeType(OffTimeTypeType):
    class Meta:
        name = "offTimeType"


@dataclass(kw_only=True)
class Offset(OffsetType1):
    class Meta:
        name = "offset"


@dataclass(kw_only=True)
class OffsetType(OffsetTypeType):
    class Meta:
        name = "offsetType"


@dataclass(kw_only=True)
class OnLines(OnLinesType):
    class Meta:
        name = "onLines"


@dataclass(kw_only=True)
class OnNote(OnNoteType):
    class Meta:
        name = "onNote"


@dataclass(kw_only=True)
class OnTimeOffset(OnTimeOffsetType):
    class Meta:
        name = "onTimeOffset"


@dataclass(kw_only=True)
class OnTimeType(OnTimeTypeType):
    class Meta:
        name = "onTimeType"


@dataclass(kw_only=True)
class Ontime(OntimeType1):
    class Meta:
        name = "ontime"


@dataclass(kw_only=True)
class OpenString(OpenStringType):
    class Meta:
        name = "open-string"


@dataclass(kw_only=True)
class Orientation(OrientationType):
    class Meta:
        name = "orientation"


@dataclass(kw_only=True)
class OrnamentStyle(OrnamentStyleType):
    class Meta:
        name = "ornamentStyle"


@dataclass(kw_only=True)
class Ornaments(OrnamentsType):
    class Meta:
        name = "ornaments"


@dataclass(kw_only=True)
class OtherDynamics(OtherDynamicsType):
    class Meta:
        name = "other-dynamics"


@dataclass(kw_only=True)
class OttavaFontFace(OttavaFontFaceType):
    class Meta:
        name = "ottavaFontFace"


@dataclass(kw_only=True)
class OttavaFontItalic(OttavaFontItalicType):
    class Meta:
        name = "ottavaFontItalic"


@dataclass(kw_only=True)
class OttavaFontSize(OttavaFontSizeType):
    class Meta:
        name = "ottavaFontSize"


@dataclass(kw_only=True)
class OttavaFontStyle(OttavaFontStyleType):
    class Meta:
        name = "ottavaFontStyle"


@dataclass(kw_only=True)
class OttavaFramePadding(OttavaFramePaddingType):
    class Meta:
        name = "ottavaFramePadding"


@dataclass(kw_only=True)
class OttavaFrameWidth(OttavaFrameWidthType):
    class Meta:
        name = "ottavaFrameWidth"


@dataclass(kw_only=True)
class OttavaHook(OttavaHookType):
    class Meta:
        name = "ottavaHook"


@dataclass(kw_only=True)
class OttavaHookAbove(OttavaHookAboveType):
    class Meta:
        name = "ottavaHookAbove"


@dataclass(kw_only=True)
class OttavaHookBelow(OttavaHookBelowType):
    class Meta:
        name = "ottavaHookBelow"


@dataclass(kw_only=True)
class OttavaLineWidth(OttavaLineWidthType):
    class Meta:
        name = "ottavaLineWidth"


@dataclass(kw_only=True)
class P1(P1Type):
    class Meta:
        name = "p1"


@dataclass(kw_only=True)
class P2(P2Type):
    class Meta:
        name = "p2"


@dataclass(kw_only=True)
class PPitchRange(PPitchRangeType):
    class Meta:
        name = "pPitchRange"


@dataclass(kw_only=True)
class PaddingWidth(PaddingWidthType):
    class Meta:
        name = "paddingWidth"


@dataclass(kw_only=True)
class PaddingWidthS(PaddingWidthStype):
    class Meta:
        name = "paddingWidthS"


@dataclass(kw_only=True)
class PageHeight1(PageHeightType1):
    class Meta:
        name = "page-height"


@dataclass(kw_only=True)
class PageOffset(PageOffsetType):
    class Meta:
        name = "page-offset"


@dataclass(kw_only=True)
class PageWidth1(PageWidthType1):
    class Meta:
        name = "page-width"


@dataclass(kw_only=True)
class PageEvenBottomMargin(PageEvenBottomMarginType):
    class Meta:
        name = "pageEvenBottomMargin"


@dataclass(kw_only=True)
class PageEvenLeftMargin(PageEvenLeftMarginType):
    class Meta:
        name = "pageEvenLeftMargin"


@dataclass(kw_only=True)
class PageEvenTopMargin(PageEvenTopMarginType):
    class Meta:
        name = "pageEvenTopMargin"


@dataclass(kw_only=True)
class PageFillLimit(PageFillLimitType):
    class Meta:
        name = "pageFillLimit"


@dataclass(kw_only=True)
class PageFormat(PageFormatType):
    class Meta:
        name = "pageFormat"


@dataclass(kw_only=True)
class PageHeight2(PageHeightType2):
    class Meta:
        name = "pageHeight"


@dataclass(kw_only=True)
class PageNumberOddEven(PageNumberOddEvenType):
    class Meta:
        name = "pageNumberOddEven"


@dataclass(kw_only=True)
class PageObjects(PageObjectsType):
    class Meta:
        name = "pageObjects"


@dataclass(kw_only=True)
class PageOddBottomMargin(PageOddBottomMarginType):
    class Meta:
        name = "pageOddBottomMargin"


@dataclass(kw_only=True)
class PageOddLeftMargin(PageOddLeftMarginType):
    class Meta:
        name = "pageOddLeftMargin"


@dataclass(kw_only=True)
class PageOddTopMargin(PageOddTopMarginType):
    class Meta:
        name = "pageOddTopMargin"


@dataclass(kw_only=True)
class PagePrintableWidth(PagePrintableWidthType):
    class Meta:
        name = "pagePrintableWidth"


@dataclass(kw_only=True)
class PageTwosided(PageTwosidedType):
    class Meta:
        name = "pageTwosided"


@dataclass(kw_only=True)
class PageWidth2(PageWidthType2):
    class Meta:
        name = "pageWidth"


@dataclass(kw_only=True)
class Page2(PageType2):
    class Meta:
        name = "page"


@dataclass(kw_only=True)
class Pages(PagesType):
    class Meta:
        name = "pages"


@dataclass(kw_only=True)
class PalmMuteFontFace(PalmMuteFontFaceType):
    class Meta:
        name = "palmMuteFontFace"


@dataclass(kw_only=True)
class Pan(PanType):
    class Meta:
        name = "pan"


@dataclass(kw_only=True)
class ParenthesisRoundClosed(ParenthesisRoundClosedType):
    class Meta:
        name = "parenthesisRoundClosed"


@dataclass(kw_only=True)
class ParenthesisRoundOpen(ParenthesisRoundOpenType):
    class Meta:
        name = "parenthesisRoundOpen"


@dataclass(kw_only=True)
class ParenthesisSquareClosed(ParenthesisSquareClosedType):
    class Meta:
        name = "parenthesisSquareClosed"


@dataclass(kw_only=True)
class ParenthesisSquareOpen(ParenthesisSquareOpenType):
    class Meta:
        name = "parenthesisSquareOpen"


@dataclass(kw_only=True)
class PartAbbreviation(PartAbbreviationType):
    class Meta:
        name = "part-abbreviation"


@dataclass(kw_only=True)
class PartAbbreviationDisplay(PartAbbreviationDisplayType):
    class Meta:
        name = "part-abbreviation-display"


@dataclass(kw_only=True)
class PartGroup(PartGroupType):
    class Meta:
        name = "part-group"


@dataclass(kw_only=True)
class PartList(PartListType):
    class Meta:
        name = "part-list"


@dataclass(kw_only=True)
class PartName(PartNameType):
    class Meta:
        name = "part-name"


@dataclass(kw_only=True)
class PartNameDisplay(PartNameDisplayType):
    class Meta:
        name = "part-name-display"


@dataclass(kw_only=True)
class PartInstrumentFontFace(PartInstrumentFontFaceType):
    class Meta:
        name = "partInstrumentFontFace"


@dataclass(kw_only=True)
class PartInstrumentFontSize(PartInstrumentFontSizeType):
    class Meta:
        name = "partInstrumentFontSize"


@dataclass(kw_only=True)
class PartInstrumentFramePadding(PartInstrumentFramePaddingType):
    class Meta:
        name = "partInstrumentFramePadding"


@dataclass(kw_only=True)
class PartInstrumentFrameRound(PartInstrumentFrameRoundType):
    class Meta:
        name = "partInstrumentFrameRound"


@dataclass(kw_only=True)
class PartInstrumentFrameWidth(PartInstrumentFrameWidthType):
    class Meta:
        name = "partInstrumentFrameWidth"


@dataclass(kw_only=True)
class Part2(PartType2):
    class Meta:
        name = "part"


@dataclass(kw_only=True)
class Path2(PathType2):
    class Meta:
        name = "path"


@dataclass(kw_only=True)
class Pause(PauseType):
    class Meta:
        name = "pause"


@dataclass(kw_only=True)
class PedalFontFace(PedalFontFaceType):
    class Meta:
        name = "pedalFontFace"


@dataclass(kw_only=True)
class PedalFramePadding(PedalFramePaddingType):
    class Meta:
        name = "pedalFramePadding"


@dataclass(kw_only=True)
class PedalFrameWidth(PedalFrameWidthType):
    class Meta:
        name = "pedalFrameWidth"


@dataclass(kw_only=True)
class PedalLineWidth(PedalLineWidthType):
    class Meta:
        name = "pedalLineWidth"


@dataclass(kw_only=True)
class PedalPosBelow(PedalPosBelowType):
    class Meta:
        name = "pedalPosBelow"


@dataclass(kw_only=True)
class PedalY(PedalYtype):
    class Meta:
        name = "pedalY"


@dataclass(kw_only=True)
class Pedal2(PedalType2):
    class Meta:
        name = "pedal"


@dataclass(kw_only=True)
class PerMinute(PerMinuteType):
    class Meta:
        name = "per-minute"


@dataclass(kw_only=True)
class Pitch(PitchType):
    class Meta:
        name = "pitch"


@dataclass(kw_only=True)
class Placement(PlacementType):
    class Meta:
        name = "placement"


@dataclass(kw_only=True)
class Platform(PlatformType):
    class Meta:
        name = "platform"


@dataclass(kw_only=True)
class Play(PlayType):
    class Meta:
        name = "play"


@dataclass(kw_only=True)
class PlayMode(PlayModeType):
    class Meta:
        name = "playMode"


@dataclass(kw_only=True)
class PlayRepeats(PlayRepeatsType):
    class Meta:
        name = "playRepeats"


@dataclass(kw_only=True)
class PlayUntil(PlayUntilType):
    class Meta:
        name = "playUntil"


@dataclass(kw_only=True)
class PlaybackVoice1(PlaybackVoice1Type):
    class Meta:
        name = "playbackVoice1"


@dataclass(kw_only=True)
class PlaybackVoice2(PlaybackVoice2Type):
    class Meta:
        name = "playbackVoice2"


@dataclass(kw_only=True)
class PlaybackVoice3(PlaybackVoice3Type):
    class Meta:
        name = "playbackVoice3"


@dataclass(kw_only=True)
class PlaybackVoice4(PlaybackVoice4Type):
    class Meta:
        name = "playbackVoice4"


@dataclass(kw_only=True)
class Plop(PlopType):
    class Meta:
        name = "plop"


@dataclass(kw_only=True)
class Pluck(PluckType):
    class Meta:
        name = "pluck"


@dataclass(kw_only=True)
class Poet(PoetType):
    class Meta:
        name = "poet"


@dataclass(kw_only=True)
class Point(PointType):
    class Meta:
        name = "point"


@dataclass(kw_only=True)
class Polygon(PolygonType):
    class Meta:
        name = "polygon"


@dataclass(kw_only=True)
class Pos(PosType):
    class Meta:
        name = "pos"


@dataclass(kw_only=True)
class PreferSharpFlat(PreferSharpFlatType):
    class Meta:
        name = "preferSharpFlat"


@dataclass(kw_only=True)
class Prefix(PrefixType):
    class Meta:
        name = "prefix"


@dataclass(kw_only=True)
class Print(PrintType):
    class Meta:
        name = "print"


@dataclass(kw_only=True)
class ProgramRevision(ProgramRevisionType):
    class Meta:
        name = "programRevision"


@dataclass(kw_only=True)
class ProgramVersion(ProgramVersionType):
    class Meta:
        name = "programVersion"


@dataclass(kw_only=True)
class Program2(ProgramType2):
    class Meta:
        name = "program"


@dataclass(kw_only=True)
class PropertyDistance(PropertyDistanceType):
    class Meta:
        name = "propertyDistance"


@dataclass(kw_only=True)
class PropertyDistanceHead(PropertyDistanceHeadType):
    class Meta:
        name = "propertyDistanceHead"


@dataclass(kw_only=True)
class PropertyDistanceStem(PropertyDistanceStemType):
    class Meta:
        name = "propertyDistanceStem"


@dataclass(kw_only=True)
class Quarter(QuarterType):
    class Meta:
        name = "quarter"


@dataclass(kw_only=True)
class Re(ReType):
    class Meta:
        name = "re"


@dataclass(kw_only=True)
class Rectangle(RectangleType):
    class Meta:
        name = "rectangle"


@dataclass(kw_only=True)
class Ref(RefType):
    class Meta:
        name = "ref"


@dataclass(kw_only=True)
class Rehearsal(RehearsalType):
    class Meta:
        name = "rehearsal"


@dataclass(kw_only=True)
class RehearsalMarkAlign(RehearsalMarkAlignType):
    class Meta:
        name = "rehearsalMarkAlign"


@dataclass(kw_only=True)
class RehearsalMarkFontBold(RehearsalMarkFontBoldType):
    class Meta:
        name = "rehearsalMarkFontBold"


@dataclass(kw_only=True)
class RehearsalMarkFontFace(RehearsalMarkFontFaceType):
    class Meta:
        name = "rehearsalMarkFontFace"


@dataclass(kw_only=True)
class RehearsalMarkFontSize(RehearsalMarkFontSizeType):
    class Meta:
        name = "rehearsalMarkFontSize"


@dataclass(kw_only=True)
class RehearsalMarkFramePadding(RehearsalMarkFramePaddingType):
    class Meta:
        name = "rehearsalMarkFramePadding"


@dataclass(kw_only=True)
class RehearsalMarkFrameRound(RehearsalMarkFrameRoundType):
    class Meta:
        name = "rehearsalMarkFrameRound"


@dataclass(kw_only=True)
class RehearsalMarkFrameWidth(RehearsalMarkFrameWidthType):
    class Meta:
        name = "rehearsalMarkFrameWidth"


@dataclass(kw_only=True)
class RelTempo(RelTempoType):
    class Meta:
        name = "relTempo"


@dataclass(kw_only=True)
class Render(RenderType):
    class Meta:
        name = "render"


@dataclass(kw_only=True)
class RenderBase(RenderBaseType):
    class Meta:
        name = "renderBase"


@dataclass(kw_only=True)
class RenderFunction(RenderFunctionType):
    class Meta:
        name = "renderFunction"


@dataclass(kw_only=True)
class RenderRoot(RenderRootType):
    class Meta:
        name = "renderRoot"


@dataclass(kw_only=True)
class Repeat(RepeatType):
    class Meta:
        name = "repeat"


@dataclass(kw_only=True)
class RepeatBarTips(RepeatBarTipsType):
    class Meta:
        name = "repeatBarTips"


@dataclass(kw_only=True)
class RepeatBarlineDotSeparation(RepeatBarlineDotSeparationType):
    class Meta:
        name = "repeatBarlineDotSeparation"


@dataclass(kw_only=True)
class RepeatLeftAlign(RepeatLeftAlignType):
    class Meta:
        name = "repeatLeftAlign"


@dataclass(kw_only=True)
class RepeatLeftFontFace(RepeatLeftFontFaceType):
    class Meta:
        name = "repeatLeftFontFace"


@dataclass(kw_only=True)
class RepeatLeftFontSize(RepeatLeftFontSizeType):
    class Meta:
        name = "repeatLeftFontSize"


@dataclass(kw_only=True)
class RepeatLeftFramePadding(RepeatLeftFramePaddingType):
    class Meta:
        name = "repeatLeftFramePadding"


@dataclass(kw_only=True)
class RepeatLeftFrameRound(RepeatLeftFrameRoundType):
    class Meta:
        name = "repeatLeftFrameRound"


@dataclass(kw_only=True)
class RepeatLeftFrameWidth(RepeatLeftFrameWidthType):
    class Meta:
        name = "repeatLeftFrameWidth"


@dataclass(kw_only=True)
class RepeatRightAlign(RepeatRightAlignType):
    class Meta:
        name = "repeatRightAlign"


@dataclass(kw_only=True)
class RepeatRightFontFace(RepeatRightFontFaceType):
    class Meta:
        name = "repeatRightFontFace"


@dataclass(kw_only=True)
class RepeatRightFontSize(RepeatRightFontSizeType):
    class Meta:
        name = "repeatRightFontSize"


@dataclass(kw_only=True)
class RepeatRightFramePadding(RepeatRightFramePaddingType):
    class Meta:
        name = "repeatRightFramePadding"


@dataclass(kw_only=True)
class RepeatRightFrameRound(RepeatRightFrameRoundType):
    class Meta:
        name = "repeatRightFrameRound"


@dataclass(kw_only=True)
class RepeatRightFrameWidth(RepeatRightFrameWidthType):
    class Meta:
        name = "repeatRightFrameWidth"


@dataclass(kw_only=True)
class Rest2(RestType2):
    class Meta:
        name = "rest"


@dataclass(kw_only=True)
class Reverb(ReverbType):
    class Meta:
        name = "reverb"


@dataclass(kw_only=True)
class Revision2(RevisionType2):
    class Meta:
        name = "revision"


@dataclass(kw_only=True)
class RhGuitarFingeringFontFace(RhGuitarFingeringFontFaceType):
    class Meta:
        name = "rhGuitarFingeringFontFace"


@dataclass(kw_only=True)
class RhGuitarFingeringFontSize(RhGuitarFingeringFontSizeType):
    class Meta:
        name = "rhGuitarFingeringFontSize"


@dataclass(kw_only=True)
class RhGuitarFingeringFontStyle(RhGuitarFingeringFontStyleType):
    class Meta:
        name = "rhGuitarFingeringFontStyle"


@dataclass(kw_only=True)
class RhGuitarFingeringFramePadding(RhGuitarFingeringFramePaddingType):
    class Meta:
        name = "rhGuitarFingeringFramePadding"


@dataclass(kw_only=True)
class RhGuitarFingeringFrameRound(RhGuitarFingeringFrameRoundType):
    class Meta:
        name = "rhGuitarFingeringFrameRound"


@dataclass(kw_only=True)
class RhGuitarFingeringFrameWidth(RhGuitarFingeringFrameWidthType):
    class Meta:
        name = "rhGuitarFingeringFrameWidth"


@dataclass(kw_only=True)
class RichText(RichTextType):
    class Meta:
        name = "richText"


@dataclass(kw_only=True)
class RightMargin1(RightMarginType1):
    class Meta:
        name = "right-margin"


@dataclass(kw_only=True)
class RightMargin2(RightMarginType2):
    class Meta:
        name = "rightMargin"


@dataclass(kw_only=True)
class RightParen(RightParenType):
    class Meta:
        name = "rightParen"


@dataclass(kw_only=True)
class Rights(RightsType):
    class Meta:
        name = "rights"


@dataclass(kw_only=True)
class Role(RoleType):
    class Meta:
        name = "role"


@dataclass(kw_only=True)
class Root(RootType):
    class Meta:
        name = "root"


@dataclass(kw_only=True)
class RootAlter(RootAlterType):
    class Meta:
        name = "root-alter"


@dataclass(kw_only=True)
class RootStep(RootStepType):
    class Meta:
        name = "root-step"


@dataclass(kw_only=True)
class RootCase(RootCaseType):
    class Meta:
        name = "rootCase"


@dataclass(kw_only=True)
class Rootfile(RootfileType):
    class Meta:
        name = "rootfile"


@dataclass(kw_only=True)
class Rootfiles(RootfilesType):
    class Meta:
        name = "rootfiles"


@dataclass(kw_only=True)
class RunTable(RunTableType):
    class Meta:
        name = "run-table"


@dataclass(kw_only=True)
class Runs(RunsType):
    class Meta:
        name = "runs"


@dataclass(kw_only=True)
class Rxoffset(RxoffsetType):
    class Meta:
        name = "rxoffset"


@dataclass(kw_only=True)
class Ryoffset(RyoffsetType):
    class Meta:
        name = "ryoffset"


@dataclass(kw_only=True)
class S(SType):
    class Meta:
        name = "s"


@dataclass(kw_only=True)
class Scaling(ScalingType):
    class Meta:
        name = "scaling"


@dataclass(kw_only=True)
class Scoop(ScoopType):
    class Meta:
        name = "scoop"


@dataclass(kw_only=True)
class ScoreInstrument(ScoreInstrumentType):
    class Meta:
        name = "score-instrument"


@dataclass(kw_only=True)
class ScorePart(ScorePartType):
    class Meta:
        name = "score-part"


@dataclass(kw_only=True)
class ScorePartwise(ScorePartwiseType):
    class Meta:
        name = "score-partwise"


@dataclass(kw_only=True)
class Score2(ScoreType2):
    class Meta:
        name = "score"


@dataclass(kw_only=True)
class SectionPause(SectionPauseType):
    class Meta:
        name = "sectionPause"


@dataclass(kw_only=True)
class SegDelta(SegDeltaType):
    class Meta:
        name = "segDelta"


@dataclass(kw_only=True)
class Segno(SegnoType):
    class Meta:
        name = "segno"


@dataclass(kw_only=True)
class Selected(SelectedType):
    class Meta:
        name = "selected"


@dataclass(kw_only=True)
class Seq(SeqType):
    class Meta:
        name = "seq"


@dataclass(kw_only=True)
class Sharp(SharpType):
    class Meta:
        name = "sharp"


@dataclass(kw_only=True)
class Sheet(SheetType):
    class Meta:
        name = "sheet"


@dataclass(kw_only=True)
class ShortName1(ShortNameType1):
    class Meta:
        name = "short-name"


@dataclass(kw_only=True)
class ShortInstrumentFontFace(ShortInstrumentFontFaceType):
    class Meta:
        name = "shortInstrumentFontFace"


@dataclass(kw_only=True)
class ShortInstrumentFontSize(ShortInstrumentFontSizeType):
    class Meta:
        name = "shortInstrumentFontSize"


@dataclass(kw_only=True)
class ShortInstrumentFramePadding(ShortInstrumentFramePaddingType):
    class Meta:
        name = "shortInstrumentFramePadding"


@dataclass(kw_only=True)
class ShortInstrumentFrameWidth(ShortInstrumentFrameWidthType):
    class Meta:
        name = "shortInstrumentFrameWidth"


@dataclass(kw_only=True)
class ShortStemProgression(ShortStemProgressionType):
    class Meta:
        name = "shortStemProgression"


@dataclass(kw_only=True)
class Shortcut2(ShortcutType2):
    class Meta:
        name = "shortcut"


@dataclass(kw_only=True)
class ShortenStem(ShortenStemType):
    class Meta:
        name = "shortenStem"


@dataclass(kw_only=True)
class ShortestStem(ShortestStemType):
    class Meta:
        name = "shortestStem"


@dataclass(kw_only=True)
class Show(ShowType):
    class Meta:
        name = "show"


@dataclass(kw_only=True)
class ShowBackTied(ShowBackTiedType):
    class Meta:
        name = "showBackTied"


@dataclass(kw_only=True)
class ShowCourtesy(ShowCourtesyType):
    class Meta:
        name = "showCourtesy"


@dataclass(kw_only=True)
class ShowCourtesyClef(ShowCourtesyClefType):
    class Meta:
        name = "showCourtesyClef"


@dataclass(kw_only=True)
class ShowCourtesySig(ShowCourtesySigType):
    class Meta:
        name = "showCourtesySig"


@dataclass(kw_only=True)
class ShowFooter(ShowFooterType):
    class Meta:
        name = "showFooter"


@dataclass(kw_only=True)
class ShowFrames(ShowFramesType):
    class Meta:
        name = "showFrames"


@dataclass(kw_only=True)
class ShowHeader(ShowHeaderType):
    class Meta:
        name = "showHeader"


@dataclass(kw_only=True)
class ShowIfSystemEmpty(ShowIfSystemEmptyType):
    class Meta:
        name = "showIfSystemEmpty"


@dataclass(kw_only=True)
class ShowInvisible(ShowInvisibleType):
    class Meta:
        name = "showInvisible"


@dataclass(kw_only=True)
class ShowMargins(ShowMarginsType):
    class Meta:
        name = "showMargins"


@dataclass(kw_only=True)
class ShowMeasureNumber(ShowMeasureNumberType):
    class Meta:
        name = "showMeasureNumber"


@dataclass(kw_only=True)
class ShowMeasureNumberOne(ShowMeasureNumberOneType):
    class Meta:
        name = "showMeasureNumberOne"


@dataclass(kw_only=True)
class ShowNaturals(ShowNaturalsType):
    class Meta:
        name = "showNaturals"


@dataclass(kw_only=True)
class ShowNut(ShowNutType):
    class Meta:
        name = "showNut"


@dataclass(kw_only=True)
class ShowOmr(ShowOmrType):
    class Meta:
        name = "showOmr"


@dataclass(kw_only=True)
class ShowPageNumber(ShowPageNumberType):
    class Meta:
        name = "showPageNumber"


@dataclass(kw_only=True)
class ShowPageNumberOne(ShowPageNumberOneType):
    class Meta:
        name = "showPageNumberOne"


@dataclass(kw_only=True)
class ShowRests(ShowRestsType):
    class Meta:
        name = "showRests"


@dataclass(kw_only=True)
class ShowTabFingering(ShowTabFingeringType):
    class Meta:
        name = "showTabFingering"


@dataclass(kw_only=True)
class ShowUnprintable(ShowUnprintableType):
    class Meta:
        name = "showUnprintable"


@dataclass(kw_only=True)
class SigD(SigDtype):
    class Meta:
        name = "sigD"


@dataclass(kw_only=True)
class SigN1(SigNtype1):
    class Meta:
        name = "sigN"


@dataclass(kw_only=True)
class Sign2(SignType2):
    class Meta:
        name = "sign"


@dataclass(kw_only=True)
class SingleNoteDynamics(SingleNoteDynamicsType):
    class Meta:
        name = "singleNoteDynamics"


@dataclass(kw_only=True)
class Size(SizeType):
    class Meta:
        name = "size"


@dataclass(kw_only=True)
class SizeIsSpatium(SizeIsSpatiumType):
    class Meta:
        name = "sizeIsSpatium"


@dataclass(kw_only=True)
class SizeIsSpatiumDependent(SizeIsSpatiumDependentType):
    class Meta:
        name = "sizeIsSpatiumDependent"


@dataclass(kw_only=True)
class Slash(SlashType):
    class Meta:
        name = "slash"


@dataclass(kw_only=True)
class SlashStyle(SlashStyleType):
    class Meta:
        name = "slashStyle"


@dataclass(kw_only=True)
class Slashed(SlashedType):
    class Meta:
        name = "slashed"


@dataclass(kw_only=True)
class Slide(SlideType):
    class Meta:
        name = "slide"


@dataclass(kw_only=True)
class SlurEndWidth(SlurEndWidthType):
    class Meta:
        name = "slurEndWidth"


@dataclass(kw_only=True)
class SlurGateTime(SlurGateTimeType):
    class Meta:
        name = "slurGateTime"


@dataclass(kw_only=True)
class SlurMidWidth(SlurMidWidthType):
    class Meta:
        name = "slurMidWidth"


@dataclass(kw_only=True)
class Slur2(SlurType2):
    class Meta:
        name = "slur"


@dataclass(kw_only=True)
class Small(SmallType):
    class Meta:
        name = "small"


@dataclass(kw_only=True)
class SmallClefMag(SmallClefMagType):
    class Meta:
        name = "smallClefMag"


@dataclass(kw_only=True)
class SmallNoteMag(SmallNoteMagType):
    class Meta:
        name = "smallNoteMag"


@dataclass(kw_only=True)
class SmallStaff(SmallStaffType):
    class Meta:
        name = "smallStaff"


@dataclass(kw_only=True)
class SmallStaffMag(SmallStaffMagType):
    class Meta:
        name = "smallStaffMag"


@dataclass(kw_only=True)
class So(SoType):
    class Meta:
        name = "so"


@dataclass(kw_only=True)
class Software(SoftwareType):
    class Meta:
        name = "software"


@dataclass(kw_only=True)
class Solo(SoloType):
    class Meta:
        name = "solo"


@dataclass(kw_only=True)
class Soloist(SoloistType):
    class Meta:
        name = "soloist"


@dataclass(kw_only=True)
class Soloists(SoloistsType):
    class Meta:
        name = "soloists"


@dataclass(kw_only=True)
class Sound(SoundType):
    class Meta:
        name = "sound"


@dataclass(kw_only=True)
class Source(SourceType):
    class Meta:
        name = "source"


@dataclass(kw_only=True)
class Space(SpaceType):
    class Meta:
        name = "space"


@dataclass(kw_only=True)
class Spacing(SpacingType):
    class Meta:
        name = "spacing"


@dataclass(kw_only=True)
class Span(SpanType):
    class Meta:
        name = "span"


@dataclass(kw_only=True)
class SpanFromOffset(SpanFromOffsetType):
    class Meta:
        name = "spanFromOffset"


@dataclass(kw_only=True)
class SpanToOffset(SpanToOffsetType):
    class Meta:
        name = "spanToOffset"


@dataclass(kw_only=True)
class SpatiumSizeDependent(SpatiumSizeDependentType):
    class Meta:
        name = "spatiumSizeDependent"


@dataclass(kw_only=True)
class Spatium2(SpatiumType2):
    class Meta:
        name = "spatium"


@dataclass(kw_only=True)
class Square(SquareType):
    class Meta:
        name = "square"


@dataclass(kw_only=True)
class StaccatoGateTime(StaccatoGateTimeType):
    class Meta:
        name = "staccatoGateTime"


@dataclass(kw_only=True)
class Stack(StackType):
    class Meta:
        name = "stack"


@dataclass(kw_only=True)
class StaffDetails(StaffDetailsType):
    class Meta:
        name = "staff-details"


@dataclass(kw_only=True)
class StaffDistance1(StaffDistanceType1):
    class Meta:
        name = "staff-distance"


@dataclass(kw_only=True)
class StaffLayout1(StaffLayoutType1):
    class Meta:
        name = "staff-layout"


@dataclass(kw_only=True)
class StaffLines1(StaffLinesType1):
    class Meta:
        name = "staff-lines"


@dataclass(kw_only=True)
class StaffTuning(StaffTuningType):
    class Meta:
        name = "staff-tuning"


@dataclass(kw_only=True)
class StaffAlign(StaffAlignType):
    class Meta:
        name = "staffAlign"


@dataclass(kw_only=True)
class StaffDistance2(StaffDistanceType2):
    class Meta:
        name = "staffDistance"


@dataclass(kw_only=True)
class StaffFontFace(StaffFontFaceType):
    class Meta:
        name = "staffFontFace"


@dataclass(kw_only=True)
class StaffFontItalic(StaffFontItalicType):
    class Meta:
        name = "staffFontItalic"


@dataclass(kw_only=True)
class StaffFontSize(StaffFontSizeType):
    class Meta:
        name = "staffFontSize"


@dataclass(kw_only=True)
class StaffFramePadding(StaffFramePaddingType):
    class Meta:
        name = "staffFramePadding"


@dataclass(kw_only=True)
class StaffFrameRound(StaffFrameRoundType):
    class Meta:
        name = "staffFrameRound"


@dataclass(kw_only=True)
class StaffFrameWidth(StaffFrameWidthType):
    class Meta:
        name = "staffFrameWidth"


@dataclass(kw_only=True)
class StaffLayout2(StaffLayoutType2):
    class Meta:
        name = "staffLayout"


@dataclass(kw_only=True)
class StaffLineWidth(StaffLineWidthType):
    class Meta:
        name = "staffLineWidth"


@dataclass(kw_only=True)
class StaffLines2(StaffLinesType2):
    class Meta:
        name = "staffLines"


@dataclass(kw_only=True)
class StaffLowerBorder(StaffLowerBorderType):
    class Meta:
        name = "staffLowerBorder"


@dataclass(kw_only=True)
class StaffMove(StaffMoveType):
    class Meta:
        name = "staffMove"


@dataclass(kw_only=True)
class StaffOffset(StaffOffsetType):
    class Meta:
        name = "staffOffset"


@dataclass(kw_only=True)
class StaffPlacement(StaffPlacementType):
    class Meta:
        name = "staffPlacement"


@dataclass(kw_only=True)
class StaffPosAbove(StaffPosAboveType):
    class Meta:
        name = "staffPosAbove"


@dataclass(kw_only=True)
class StaffPosBelow(StaffPosBelowType):
    class Meta:
        name = "staffPosBelow"


@dataclass(kw_only=True)
class StaffTextMinDistance(StaffTextMinDistanceType):
    class Meta:
        name = "staffTextMinDistance"


@dataclass(kw_only=True)
class StaffTextPosAbove(StaffTextPosAboveType):
    class Meta:
        name = "staffTextPosAbove"


@dataclass(kw_only=True)
class StaffUpperBorder(StaffUpperBorderType):
    class Meta:
        name = "staffUpperBorder"


@dataclass(kw_only=True)
class Staff2(StaffType3):
    class Meta:
        name = "staff"


@dataclass(kw_only=True)
class Stafflines3(StafflinesType3):
    class Meta:
        name = "stafflines"


@dataclass(kw_only=True)
class Stafftype4(StafftypeType2):
    class Meta:
        name = "stafftype"


@dataclass(kw_only=True)
class StartBarlineMultiple(StartBarlineMultipleType):
    class Meta:
        name = "startBarlineMultiple"


@dataclass(kw_only=True)
class StartBarlineSingle(StartBarlineSingleType):
    class Meta:
        name = "startBarlineSingle"


@dataclass(kw_only=True)
class StartRepeat(StartRepeatType):
    class Meta:
        name = "startRepeat"


@dataclass(kw_only=True)
class StartTrack(StartTrackType):
    class Meta:
        name = "startTrack"


@dataclass(kw_only=True)
class StartWithLongNames(StartWithLongNamesType):
    class Meta:
        name = "startWithLongNames"


@dataclass(kw_only=True)
class StartWithMeasureOne(StartWithMeasureOneType):
    class Meta:
        name = "startWithMeasureOne"


@dataclass(kw_only=True)
class Staves(StavesType):
    class Meta:
        name = "staves"


@dataclass(kw_only=True)
class Std(StdType):
    class Meta:
        name = "std"


@dataclass(kw_only=True)
class StemDir(StemDirType):
    class Meta:
        name = "stemDir"


@dataclass(kw_only=True)
class StemDir1(StemDir1Type):
    class Meta:
        name = "stemDir1"


@dataclass(kw_only=True)
class StemDir2(StemDir2Type):
    class Meta:
        name = "stemDir2"


@dataclass(kw_only=True)
class StemDir3(StemDir3Type):
    class Meta:
        name = "stemDir3"


@dataclass(kw_only=True)
class StemDir4(StemDir4Type):
    class Meta:
        name = "stemDir4"


@dataclass(kw_only=True)
class StemHeight(StemHeightType):
    class Meta:
        name = "stemHeight"


@dataclass(kw_only=True)
class StemWidth(StemWidthType):
    class Meta:
        name = "stemWidth"


@dataclass(kw_only=True)
class Stem2(StemType2):
    class Meta:
        name = "stem"


@dataclass(kw_only=True)
class Stemless(StemlessType):
    class Meta:
        name = "stemless"


@dataclass(kw_only=True)
class StemsDown(StemsDownType):
    class Meta:
        name = "stemsDown"


@dataclass(kw_only=True)
class StemsThrough(StemsThroughType):
    class Meta:
        name = "stemsThrough"


@dataclass(kw_only=True)
class Step(StepType):
    class Meta:
        name = "step"


@dataclass(kw_only=True)
class StepOffset(StepOffsetType):
    class Meta:
        name = "stepOffset"


@dataclass(kw_only=True)
class StickingFontFace(StickingFontFaceType):
    class Meta:
        name = "stickingFontFace"


@dataclass(kw_only=True)
class Straight(StraightType):
    class Meta:
        name = "straight"


@dataclass(kw_only=True)
class Stretch(StretchType):
    class Meta:
        name = "stretch"


@dataclass(kw_only=True)
class StretchD(StretchDtype):
    class Meta:
        name = "stretchD"


@dataclass(kw_only=True)
class StretchN(StretchNtype):
    class Meta:
        name = "stretchN"


@dataclass(kw_only=True)
class StringNumberFontFace(StringNumberFontFaceType):
    class Meta:
        name = "stringNumberFontFace"


@dataclass(kw_only=True)
class StringNumberFontSize(StringNumberFontSizeType):
    class Meta:
        name = "stringNumberFontSize"


@dataclass(kw_only=True)
class StringNumberOffset(StringNumberOffsetType):
    class Meta:
        name = "stringNumberOffset"


@dataclass(kw_only=True)
class Strings(StringsType):
    class Meta:
        name = "strings"


@dataclass(kw_only=True)
class StrokeStyle(StrokeStyleType):
    class Meta:
        name = "strokeStyle"


@dataclass(kw_only=True)
class StrongAccent(StrongAccentType):
    class Meta:
        name = "strong-accent"


@dataclass(kw_only=True)
class Style2(StyleType2):
    class Meta:
        name = "style"


@dataclass(kw_only=True)
class SubTitleFontFace(SubTitleFontFaceType):
    class Meta:
        name = "subTitleFontFace"


@dataclass(kw_only=True)
class SubTitleFontSize(SubTitleFontSizeType):
    class Meta:
        name = "subTitleFontSize"


@dataclass(kw_only=True)
class SubTitleFontSpatiumDependent(SubTitleFontSpatiumDependentType):
    class Meta:
        name = "subTitleFontSpatiumDependent"


@dataclass(kw_only=True)
class SubTitleFramePadding(SubTitleFramePaddingType):
    class Meta:
        name = "subTitleFramePadding"


@dataclass(kw_only=True)
class SubTitleFrameRound(SubTitleFrameRoundType):
    class Meta:
        name = "subTitleFrameRound"


@dataclass(kw_only=True)
class SubTitleFrameWidth(SubTitleFrameWidthType):
    class Meta:
        name = "subTitleFrameWidth"


@dataclass(kw_only=True)
class Subtype(SubtypeType):
    class Meta:
        name = "subtype"


@dataclass(kw_only=True)
class Suffix(SuffixType):
    class Meta:
        name = "suffix"


@dataclass(kw_only=True)
class Sup(SupType):
    class Meta:
        name = "sup"


@dataclass(kw_only=True)
class Supports(SupportsType):
    class Meta:
        name = "supports"


@dataclass(kw_only=True)
class SwingRatio(SwingRatioType):
    class Meta:
        name = "swingRatio"


@dataclass(kw_only=True)
class SwingUnit(SwingUnitType):
    class Meta:
        name = "swingUnit"


@dataclass(kw_only=True)
class Swing2(SwingType2):
    class Meta:
        name = "swing"


@dataclass(kw_only=True)
class Syllabic(SyllabicType):
    class Meta:
        name = "syllabic"


@dataclass(kw_only=True)
class Sym(SymType):
    class Meta:
        name = "sym"


@dataclass(kw_only=True)
class SymbolRepeat(SymbolRepeatType):
    class Meta:
        name = "symbolRepeat"


@dataclass(kw_only=True)
class Symbol2(SymbolType2):
    class Meta:
        name = "symbol"


@dataclass(kw_only=True)
class Synti(SyntiType):
    class Meta:
        name = "synti"


@dataclass(kw_only=True)
class SysInitBarLineType(SysInitBarLineTypeType):
    class Meta:
        name = "sysInitBarLineType"


@dataclass(kw_only=True)
class Sysex(SysexType):
    class Meta:
        name = "sysex"


@dataclass(kw_only=True)
class SystemDistance1(SystemDistanceType1):
    class Meta:
        name = "system-distance"


@dataclass(kw_only=True)
class SystemDividers(SystemDividersType):
    class Meta:
        name = "system-dividers"


@dataclass(kw_only=True)
class SystemLayout(SystemLayoutType):
    class Meta:
        name = "system-layout"


@dataclass(kw_only=True)
class SystemMargins(SystemMarginsType):
    class Meta:
        name = "system-margins"


@dataclass(kw_only=True)
class SystemAlign(SystemAlignType):
    class Meta:
        name = "systemAlign"


@dataclass(kw_only=True)
class SystemDistance2(SystemDistanceType2):
    class Meta:
        name = "systemDistance"


@dataclass(kw_only=True)
class SystemFlag(SystemFlagType):
    class Meta:
        name = "systemFlag"


@dataclass(kw_only=True)
class SystemFontFace(SystemFontFaceType):
    class Meta:
        name = "systemFontFace"


@dataclass(kw_only=True)
class SystemFontSize(SystemFontSizeType):
    class Meta:
        name = "systemFontSize"


@dataclass(kw_only=True)
class SystemFrameDistance(SystemFrameDistanceType):
    class Meta:
        name = "systemFrameDistance"


@dataclass(kw_only=True)
class SystemFramePadding(SystemFramePaddingType):
    class Meta:
        name = "systemFramePadding"


@dataclass(kw_only=True)
class SystemFrameRound(SystemFrameRoundType):
    class Meta:
        name = "systemFrameRound"


@dataclass(kw_only=True)
class SystemFrameWidth(SystemFrameWidthType):
    class Meta:
        name = "systemFrameWidth"


@dataclass(kw_only=True)
class SystemOffset(SystemOffsetType):
    class Meta:
        name = "systemOffset"


@dataclass(kw_only=True)
class System2(SystemType2):
    class Meta:
        name = "system"


@dataclass(kw_only=True)
class Systems(SystemsType):
    class Meta:
        name = "systems"


@dataclass(kw_only=True)
class Tab(TabType):
    class Meta:
        name = "tab"


@dataclass(kw_only=True)
class Tag(TagType):
    class Meta:
        name = "tag"


@dataclass(kw_only=True)
class Technical(TechnicalType):
    class Meta:
        name = "technical"


@dataclass(kw_only=True)
class TempoFontBold(TempoFontBoldType):
    class Meta:
        name = "tempoFontBold"


@dataclass(kw_only=True)
class TempoFontFace(TempoFontFaceType):
    class Meta:
        name = "tempoFontFace"


@dataclass(kw_only=True)
class TempoFontSize(TempoFontSizeType):
    class Meta:
        name = "tempoFontSize"


@dataclass(kw_only=True)
class TempoFontStyle(TempoFontStyleType):
    class Meta:
        name = "tempoFontStyle"


@dataclass(kw_only=True)
class TempoFramePadding(TempoFramePaddingType):
    class Meta:
        name = "tempoFramePadding"


@dataclass(kw_only=True)
class TempoFrameRound(TempoFrameRoundType):
    class Meta:
        name = "tempoFrameRound"


@dataclass(kw_only=True)
class TempoFrameWidth(TempoFrameWidthType):
    class Meta:
        name = "tempoFrameWidth"


@dataclass(kw_only=True)
class TempoOffset(TempoOffsetType):
    class Meta:
        name = "tempoOffset"


@dataclass(kw_only=True)
class TempoPosAbove(TempoPosAboveType):
    class Meta:
        name = "tempoPosAbove"


@dataclass(kw_only=True)
class Tempo2(TempoType2):
    class Meta:
        name = "tempo"


@dataclass(kw_only=True)
class Tenths(TenthsType):
    class Meta:
        name = "tenths"


@dataclass(kw_only=True)
class TextD(TextDtype):
    class Meta:
        name = "textD"


@dataclass(kw_only=True)
class TextLineFontFace(TextLineFontFaceType):
    class Meta:
        name = "textLineFontFace"


@dataclass(kw_only=True)
class TextLineFontSize(TextLineFontSizeType):
    class Meta:
        name = "textLineFontSize"


@dataclass(kw_only=True)
class TextLineFramePadding(TextLineFramePaddingType):
    class Meta:
        name = "textLineFramePadding"


@dataclass(kw_only=True)
class TextLineFrameWidth(TextLineFrameWidthType):
    class Meta:
        name = "textLineFrameWidth"


@dataclass(kw_only=True)
class TextLineTextAlign(TextLineTextAlignType):
    class Meta:
        name = "textLineTextAlign"


@dataclass(kw_only=True)
class TextN(TextNtype):
    class Meta:
        name = "textN"


@dataclass(kw_only=True)
class Ti(TiType):
    class Meta:
        name = "ti"


@dataclass(kw_only=True)
class Tick(TickType):
    class Meta:
        name = "tick"


@dataclass(kw_only=True)
class Tick2(Tick2Type):
    class Meta:
        name = "tick2"


@dataclass(kw_only=True)
class TickOffset(TickOffsetType):
    class Meta:
        name = "tickOffset"


@dataclass(kw_only=True)
class Ticklen(TicklenType):
    class Meta:
        name = "ticklen"


@dataclass(kw_only=True)
class Ticks(TicksType):
    class Meta:
        name = "ticks"


@dataclass(kw_only=True)
class TicksF(TicksFType):
    class Meta:
        name = "ticks_f"


@dataclass(kw_only=True)
class Tie2(TieType2):
    class Meta:
        name = "tie"


@dataclass(kw_only=True)
class Tied(TiedType):
    class Meta:
        name = "tied"


@dataclass(kw_only=True)
class Time(TimeType):
    class Meta:
        name = "time"


@dataclass(kw_only=True)
class TimeModification(TimeModificationType):
    class Meta:
        name = "time-modification"


@dataclass(kw_only=True)
class TimeSign(TimeSignType):
    class Meta:
        name = "timeSign"


@dataclass(kw_only=True)
class TimeStretch(TimeStretchType):
    class Meta:
        name = "timeStretch"


@dataclass(kw_only=True)
class TimesigLeftMargin(TimesigLeftMarginType):
    class Meta:
        name = "timesigLeftMargin"


@dataclass(kw_only=True)
class Timesig2(TimesigType2):
    class Meta:
        name = "timesig"


@dataclass(kw_only=True)
class Title(TitleType):
    class Meta:
        name = "title"


@dataclass(kw_only=True)
class TitleFontFace(TitleFontFaceType):
    class Meta:
        name = "titleFontFace"


@dataclass(kw_only=True)
class TitleFontSize(TitleFontSizeType):
    class Meta:
        name = "titleFontSize"


@dataclass(kw_only=True)
class TitleFontSpatiumDependent(TitleFontSpatiumDependentType):
    class Meta:
        name = "titleFontSpatiumDependent"


@dataclass(kw_only=True)
class TitleFontStyle(TitleFontStyleType):
    class Meta:
        name = "titleFontStyle"


@dataclass(kw_only=True)
class TitleFramePadding(TitleFramePaddingType):
    class Meta:
        name = "titleFramePadding"


@dataclass(kw_only=True)
class TitleFrameRound(TitleFrameRoundType):
    class Meta:
        name = "titleFrameRound"


@dataclass(kw_only=True)
class TitleFrameWidth(TitleFrameWidthType):
    class Meta:
        name = "titleFrameWidth"


@dataclass(kw_only=True)
class Token(TokenType):
    class Meta:
        name = "token"


@dataclass(kw_only=True)
class TopMargin1(TopMarginType1):
    class Meta:
        name = "top-margin"


@dataclass(kw_only=True)
class TopSystemDistance(TopSystemDistanceType):
    class Meta:
        name = "top-system-distance"


@dataclass(kw_only=True)
class TopAccidental(TopAccidentalType):
    class Meta:
        name = "topAccidental"


@dataclass(kw_only=True)
class TopGap(TopGapType):
    class Meta:
        name = "topGap"


@dataclass(kw_only=True)
class TopMargin2(TopMarginType2):
    class Meta:
        name = "topMargin"


@dataclass(kw_only=True)
class TopPitch(TopPitchType):
    class Meta:
        name = "topPitch"


@dataclass(kw_only=True)
class TopTpc(TopTpcType):
    class Meta:
        name = "topTpc"


@dataclass(kw_only=True)
class Tpc(TpcType):
    class Meta:
        name = "tpc"


@dataclass(kw_only=True)
class Tpc2(Tpc2Type):
    class Meta:
        name = "tpc2"


@dataclass(kw_only=True)
class Track2(Track2Type):
    class Meta:
        name = "track2"


@dataclass(kw_only=True)
class TrackName2(TrackNameType2):
    class Meta:
        name = "trackName"


@dataclass(kw_only=True)
class TrackOffset(TrackOffsetType):
    class Meta:
        name = "trackOffset"


@dataclass(kw_only=True)
class Track3(TrackType2):
    class Meta:
        name = "track"


@dataclass(kw_only=True)
class TrailingSpace(TrailingSpaceType):
    class Meta:
        name = "trailingSpace"


@dataclass(kw_only=True)
class Translator(TranslatorType):
    class Meta:
        name = "translator"


@dataclass(kw_only=True)
class TranslatorAlign(TranslatorAlignType):
    class Meta:
        name = "translatorAlign"


@dataclass(kw_only=True)
class TranslatorFontFace(TranslatorFontFaceType):
    class Meta:
        name = "translatorFontFace"


@dataclass(kw_only=True)
class TranslatorFontSize(TranslatorFontSizeType):
    class Meta:
        name = "translatorFontSize"


@dataclass(kw_only=True)
class TranslatorFramePadding(TranslatorFramePaddingType):
    class Meta:
        name = "translatorFramePadding"


@dataclass(kw_only=True)
class TranslatorFrameWidth(TranslatorFrameWidthType):
    class Meta:
        name = "translatorFrameWidth"


@dataclass(kw_only=True)
class Transposable(TransposableType):
    class Meta:
        name = "transposable"


@dataclass(kw_only=True)
class Transpose(TransposeType):
    class Meta:
        name = "transpose"


@dataclass(kw_only=True)
class TransposeChromatic(TransposeChromaticType):
    class Meta:
        name = "transposeChromatic"


@dataclass(kw_only=True)
class TransposeDiatonic(TransposeDiatonicType):
    class Meta:
        name = "transposeDiatonic"


@dataclass(kw_only=True)
class TransposingClef(TransposingClefType1):
    class Meta:
        name = "transposingClef"


@dataclass(kw_only=True)
class TransposingClefType(TransposingClefTypeType):
    class Meta:
        name = "transposingClefType"


@dataclass(kw_only=True)
class Transposition(TranspositionType):
    class Meta:
        name = "transposition"


@dataclass(kw_only=True)
class Tremolo2(TremoloType2):
    class Meta:
        name = "tremolo"


@dataclass(kw_only=True)
class Triangle(TriangleType):
    class Meta:
        name = "triangle"


@dataclass(kw_only=True)
class TrillMark(TrillMarkType):
    class Meta:
        name = "trill-mark"


@dataclass(kw_only=True)
class TrillPosAbove(TrillPosAboveType):
    class Meta:
        name = "trillPosAbove"


@dataclass(kw_only=True)
class Trill2(TrillType2):
    class Meta:
        name = "trill"


@dataclass(kw_only=True)
class Tuning(TuningType):
    class Meta:
        name = "tuning"


@dataclass(kw_only=True)
class TuningAlter(TuningAlterType):
    class Meta:
        name = "tuning-alter"


@dataclass(kw_only=True)
class TuningOctave(TuningOctaveType):
    class Meta:
        name = "tuning-octave"


@dataclass(kw_only=True)
class TuningStep(TuningStepType):
    class Meta:
        name = "tuning-step"


@dataclass(kw_only=True)
class TupletActual(TupletActualType):
    class Meta:
        name = "tuplet-actual"


@dataclass(kw_only=True)
class TupletDot(TupletDotType):
    class Meta:
        name = "tuplet-dot"


@dataclass(kw_only=True)
class TupletNormal(TupletNormalType):
    class Meta:
        name = "tuplet-normal"


@dataclass(kw_only=True)
class TupletNumber(TupletNumberType):
    class Meta:
        name = "tuplet-number"


@dataclass(kw_only=True)
class TupletType(TupletTypeType):
    class Meta:
        name = "tuplet-type"


@dataclass(kw_only=True)
class TupletBracketHookHeight(TupletBracketHookHeightType):
    class Meta:
        name = "tupletBracketHookHeight"


@dataclass(kw_only=True)
class TupletBracketWidth(TupletBracketWidthType):
    class Meta:
        name = "tupletBracketWidth"


@dataclass(kw_only=True)
class TupletFontFace(TupletFontFaceType):
    class Meta:
        name = "tupletFontFace"


@dataclass(kw_only=True)
class TupletFontSize(TupletFontSizeType):
    class Meta:
        name = "tupletFontSize"


@dataclass(kw_only=True)
class TupletFontStyle(TupletFontStyleType):
    class Meta:
        name = "tupletFontStyle"


@dataclass(kw_only=True)
class TupletFramePadding(TupletFramePaddingType):
    class Meta:
        name = "tupletFramePadding"


@dataclass(kw_only=True)
class TupletFrameWidth(TupletFrameWidthType):
    class Meta:
        name = "tupletFrameWidth"


@dataclass(kw_only=True)
class TupletNoteLeftDistance(TupletNoteLeftDistanceType):
    class Meta:
        name = "tupletNoteLeftDistance"


@dataclass(kw_only=True)
class TupletOufOfStaff(TupletOufOfStaffType):
    class Meta:
        name = "tupletOufOfStaff"


@dataclass(kw_only=True)
class TupletStemLeftDistance(TupletStemLeftDistanceType):
    class Meta:
        name = "tupletStemLeftDistance"


@dataclass(kw_only=True)
class TupletVheadDistance(TupletVheadDistanceType):
    class Meta:
        name = "tupletVHeadDistance"


@dataclass(kw_only=True)
class TupletVstemDistance(TupletVstemDistanceType):
    class Meta:
        name = "tupletVStemDistance"


@dataclass(kw_only=True)
class Tuplet2(TupletType2):
    class Meta:
        name = "tuplet"


@dataclass(kw_only=True)
class Turn(TurnType):
    class Meta:
        name = "turn"


@dataclass(kw_only=True)
class Type(TypeType):
    class Meta:
        name = "type"


@dataclass(kw_only=True)
class Underline(UnderlineType):
    class Meta:
        name = "underline"


@dataclass(kw_only=True)
class Unpitched(UnpitchedType):
    class Meta:
        name = "unpitched"


@dataclass(kw_only=True)
class Unsorted(UnsortedType):
    class Meta:
        name = "unsorted"


@dataclass(kw_only=True)
class Up(UpType):
    class Meta:
        name = "up"


@dataclass(kw_only=True)
class UpsideDown(UpsideDownType):
    class Meta:
        name = "upsideDown"


@dataclass(kw_only=True)
class UseDrumset(UseDrumsetType):
    class Meta:
        name = "useDrumset"


@dataclass(kw_only=True)
class UseFrenchNoteNames(UseFrenchNoteNamesType):
    class Meta:
        name = "useFrenchNoteNames"


@dataclass(kw_only=True)
class UseFullGermanNoteNames(UseFullGermanNoteNamesType):
    class Meta:
        name = "useFullGermanNoteNames"


@dataclass(kw_only=True)
class UseGermanNoteNames(UseGermanNoteNamesType):
    class Meta:
        name = "useGermanNoteNames"


@dataclass(kw_only=True)
class UseNumbers(UseNumbersType):
    class Meta:
        name = "useNumbers"


@dataclass(kw_only=True)
class UsePre36Defaults(UsePre36DefaultsType):
    class Meta:
        name = "usePre_3_6_defaults"


@dataclass(kw_only=True)
class UseSolfeggioNoteNames(UseSolfeggioNoteNamesType):
    class Meta:
        name = "useSolfeggioNoteNames"


@dataclass(kw_only=True)
class UseStandardNoteNames(UseStandardNoteNamesType):
    class Meta:
        name = "useStandardNoteNames"


@dataclass(kw_only=True)
class UseTablature(UseTablatureType):
    class Meta:
        name = "useTablature"


@dataclass(kw_only=True)
class UseTextLine(UseTextLineType):
    class Meta:
        name = "useTextLine"


@dataclass(kw_only=True)
class User10FontFace(User10FontFaceType):
    class Meta:
        name = "user10FontFace"


@dataclass(kw_only=True)
class User11FontFace(User11FontFaceType):
    class Meta:
        name = "user11FontFace"


@dataclass(kw_only=True)
class User12FontFace(User12FontFaceType):
    class Meta:
        name = "user12FontFace"


@dataclass(kw_only=True)
class User1Align(User1AlignType):
    class Meta:
        name = "user1Align"


@dataclass(kw_only=True)
class User1FontBold(User1FontBoldType):
    class Meta:
        name = "user1FontBold"


@dataclass(kw_only=True)
class User1FontFace(User1FontFaceType):
    class Meta:
        name = "user1FontFace"


@dataclass(kw_only=True)
class User1FontSize(User1FontSizeType):
    class Meta:
        name = "user1FontSize"


@dataclass(kw_only=True)
class User1FontSpatiumDependent(User1FontSpatiumDependentType):
    class Meta:
        name = "user1FontSpatiumDependent"


@dataclass(kw_only=True)
class User1FramePadding(User1FramePaddingType):
    class Meta:
        name = "user1FramePadding"


@dataclass(kw_only=True)
class User1FrameWidth(User1FrameWidthType):
    class Meta:
        name = "user1FrameWidth"


@dataclass(kw_only=True)
class User1Name(User1NameType):
    class Meta:
        name = "user1Name"


@dataclass(kw_only=True)
class User2Align(User2AlignType):
    class Meta:
        name = "user2Align"


@dataclass(kw_only=True)
class User2FontFace(User2FontFaceType):
    class Meta:
        name = "user2FontFace"


@dataclass(kw_only=True)
class User2FontSize(User2FontSizeType):
    class Meta:
        name = "user2FontSize"


@dataclass(kw_only=True)
class User2FontSpatiumDependent(User2FontSpatiumDependentType):
    class Meta:
        name = "user2FontSpatiumDependent"


@dataclass(kw_only=True)
class User2FontStyle(User2FontStyleType):
    class Meta:
        name = "user2FontStyle"


@dataclass(kw_only=True)
class User2FramePadding(User2FramePaddingType):
    class Meta:
        name = "user2FramePadding"


@dataclass(kw_only=True)
class User2FrameWidth(User2FrameWidthType):
    class Meta:
        name = "user2FrameWidth"


@dataclass(kw_only=True)
class User2Name(User2NameType):
    class Meta:
        name = "user2Name"


@dataclass(kw_only=True)
class User3Align(User3AlignType):
    class Meta:
        name = "user3Align"


@dataclass(kw_only=True)
class User3FontFace(User3FontFaceType):
    class Meta:
        name = "user3FontFace"


@dataclass(kw_only=True)
class User3FontSize(User3FontSizeType):
    class Meta:
        name = "user3FontSize"


@dataclass(kw_only=True)
class User3FontSpatiumDependent(User3FontSpatiumDependentType):
    class Meta:
        name = "user3FontSpatiumDependent"


@dataclass(kw_only=True)
class User3FramePadding(User3FramePaddingType):
    class Meta:
        name = "user3FramePadding"


@dataclass(kw_only=True)
class User3FrameWidth(User3FrameWidthType):
    class Meta:
        name = "user3FrameWidth"


@dataclass(kw_only=True)
class User3Name(User3NameType):
    class Meta:
        name = "user3Name"


@dataclass(kw_only=True)
class User4Align(User4AlignType):
    class Meta:
        name = "user4Align"


@dataclass(kw_only=True)
class User4FontFace(User4FontFaceType):
    class Meta:
        name = "user4FontFace"


@dataclass(kw_only=True)
class User4FontSize(User4FontSizeType):
    class Meta:
        name = "user4FontSize"


@dataclass(kw_only=True)
class User4FontSpatiumDependent(User4FontSpatiumDependentType):
    class Meta:
        name = "user4FontSpatiumDependent"


@dataclass(kw_only=True)
class User4FramePadding(User4FramePaddingType):
    class Meta:
        name = "user4FramePadding"


@dataclass(kw_only=True)
class User4FrameWidth(User4FrameWidthType):
    class Meta:
        name = "user4FrameWidth"


@dataclass(kw_only=True)
class User4Name(User4NameType):
    class Meta:
        name = "user4Name"


@dataclass(kw_only=True)
class User5Align(User5AlignType):
    class Meta:
        name = "user5Align"


@dataclass(kw_only=True)
class User5FontFace(User5FontFaceType):
    class Meta:
        name = "user5FontFace"


@dataclass(kw_only=True)
class User5FontSize(User5FontSizeType):
    class Meta:
        name = "user5FontSize"


@dataclass(kw_only=True)
class User5FontSpatiumDependent(User5FontSpatiumDependentType):
    class Meta:
        name = "user5FontSpatiumDependent"


@dataclass(kw_only=True)
class User5FramePadding(User5FramePaddingType):
    class Meta:
        name = "user5FramePadding"


@dataclass(kw_only=True)
class User5FrameWidth(User5FrameWidthType):
    class Meta:
        name = "user5FrameWidth"


@dataclass(kw_only=True)
class User5Name(User5NameType):
    class Meta:
        name = "user5Name"


@dataclass(kw_only=True)
class User6Align(User6AlignType):
    class Meta:
        name = "user6Align"


@dataclass(kw_only=True)
class User6FontFace(User6FontFaceType):
    class Meta:
        name = "user6FontFace"


@dataclass(kw_only=True)
class User6FontSize(User6FontSizeType):
    class Meta:
        name = "user6FontSize"


@dataclass(kw_only=True)
class User6FontSpatiumDependent(User6FontSpatiumDependentType):
    class Meta:
        name = "user6FontSpatiumDependent"


@dataclass(kw_only=True)
class User6FontStyle(User6FontStyleType):
    class Meta:
        name = "user6FontStyle"


@dataclass(kw_only=True)
class User6FramePadding(User6FramePaddingType):
    class Meta:
        name = "user6FramePadding"


@dataclass(kw_only=True)
class User6FrameWidth(User6FrameWidthType):
    class Meta:
        name = "user6FrameWidth"


@dataclass(kw_only=True)
class User6Name(User6NameType):
    class Meta:
        name = "user6Name"


@dataclass(kw_only=True)
class User7Align(User7AlignType):
    class Meta:
        name = "user7Align"


@dataclass(kw_only=True)
class User7FontFace(User7FontFaceType):
    class Meta:
        name = "user7FontFace"


@dataclass(kw_only=True)
class User7FontSize(User7FontSizeType):
    class Meta:
        name = "user7FontSize"


@dataclass(kw_only=True)
class User7FontSpatiumDependent(User7FontSpatiumDependentType):
    class Meta:
        name = "user7FontSpatiumDependent"


@dataclass(kw_only=True)
class User7FontStyle(User7FontStyleType):
    class Meta:
        name = "user7FontStyle"


@dataclass(kw_only=True)
class User7FramePadding(User7FramePaddingType):
    class Meta:
        name = "user7FramePadding"


@dataclass(kw_only=True)
class User7FrameWidth(User7FrameWidthType):
    class Meta:
        name = "user7FrameWidth"


@dataclass(kw_only=True)
class User7Name(User7NameType):
    class Meta:
        name = "user7Name"


@dataclass(kw_only=True)
class User8FontFace(User8FontFaceType):
    class Meta:
        name = "user8FontFace"


@dataclass(kw_only=True)
class User9FontFace(User9FontFaceType):
    class Meta:
        name = "user9FontFace"


@dataclass(kw_only=True)
class UserAccidental(UserAccidentalType):
    class Meta:
        name = "userAccidental"


@dataclass(kw_only=True)
class UserLen(UserLenType):
    class Meta:
        name = "userLen"


@dataclass(kw_only=True)
class UserLen1(UserLen1Type):
    class Meta:
        name = "userLen1"


@dataclass(kw_only=True)
class UserLen2(UserLen2Type):
    class Meta:
        name = "userLen2"


@dataclass(kw_only=True)
class Val(ValType):
    class Meta:
        name = "val"


@dataclass(kw_only=True)
class Valign(ValignType):
    class Meta:
        name = "valign"


@dataclass(kw_only=True)
class Variant(VariantType):
    class Meta:
        name = "variant"


@dataclass(kw_only=True)
class Variants(VariantsType):
    class Meta:
        name = "variants"


@dataclass(kw_only=True)
class VeloChange(VeloChangeType):
    class Meta:
        name = "veloChange"


@dataclass(kw_only=True)
class VeloChangeMethod(VeloChangeMethodType):
    class Meta:
        name = "veloChangeMethod"


@dataclass(kw_only=True)
class VeloChangeSpeed(VeloChangeSpeedType):
    class Meta:
        name = "veloChangeSpeed"


@dataclass(kw_only=True)
class VeloType(VeloTypeType):
    class Meta:
        name = "veloType"


@dataclass(kw_only=True)
class Velocity(VelocityType):
    class Meta:
        name = "velocity"


@dataclass(kw_only=True)
class Verse(VerseType):
    class Meta:
        name = "verse"


@dataclass(kw_only=True)
class Version(VersionType):
    class Meta:
        name = "version"


@dataclass(kw_only=True)
class Vertical(VerticalType):
    class Meta:
        name = "vertical"


@dataclass(kw_only=True)
class VerticalPos(VerticalPosType):
    class Meta:
        name = "verticalPos"


@dataclass(kw_only=True)
class VirtualInstrument(VirtualInstrumentType):
    class Meta:
        name = "virtual-instrument"


@dataclass(kw_only=True)
class VirtualLibrary(VirtualLibraryType):
    class Meta:
        name = "virtual-library"


@dataclass(kw_only=True)
class VirtualName(VirtualNameType):
    class Meta:
        name = "virtual-name"


@dataclass(kw_only=True)
class Visible(VisibleType):
    class Meta:
        name = "visible"


@dataclass(kw_only=True)
class VoiceOffset(VoiceOffsetType):
    class Meta:
        name = "voiceOffset"


@dataclass(kw_only=True)
class Voices(VoicesType):
    class Meta:
        name = "voices"


@dataclass(kw_only=True)
class Voicing(VoicingType):
    class Meta:
        name = "voicing"


@dataclass(kw_only=True)
class VoltaFontBold(VoltaFontBoldType):
    class Meta:
        name = "voltaFontBold"


@dataclass(kw_only=True)
class VoltaFontFace(VoltaFontFaceType):
    class Meta:
        name = "voltaFontFace"


@dataclass(kw_only=True)
class VoltaFontSize(VoltaFontSizeType):
    class Meta:
        name = "voltaFontSize"


@dataclass(kw_only=True)
class VoltaFramePadding(VoltaFramePaddingType):
    class Meta:
        name = "voltaFramePadding"


@dataclass(kw_only=True)
class VoltaFrameWidth(VoltaFrameWidthType):
    class Meta:
        name = "voltaFrameWidth"


@dataclass(kw_only=True)
class VoltaLineWidth(VoltaLineWidthType):
    class Meta:
        name = "voltaLineWidth"


@dataclass(kw_only=True)
class VoltaPosAbove(VoltaPosAboveType):
    class Meta:
        name = "voltaPosAbove"


@dataclass(kw_only=True)
class VoltaY(VoltaYtype):
    class Meta:
        name = "voltaY"


@dataclass(kw_only=True)
class Volta2(VoltaType2):
    class Meta:
        name = "volta"


@dataclass(kw_only=True)
class Volume(VolumeType):
    class Meta:
        name = "volume"


@dataclass(kw_only=True)
class Vspacer(VspacerType):
    class Meta:
        name = "vspacer"


@dataclass(kw_only=True)
class VspacerDown(VspacerDownType):
    class Meta:
        name = "vspacerDown"


@dataclass(kw_only=True)
class VspacerFixed(VspacerFixedType):
    class Meta:
        name = "vspacerFixed"


@dataclass(kw_only=True)
class VspacerUp(VspacerUpType):
    class Meta:
        name = "vspacerUp"


@dataclass(kw_only=True)
class WavyLine1(WavyLineType1):
    class Meta:
        name = "wavy-line"


@dataclass(kw_only=True)
class WavyLine2(WavyLineType2):
    class Meta:
        name = "wavyLine"


@dataclass(kw_only=True)
class Wedge(WedgeType):
    class Meta:
        name = "wedge"


@dataclass(kw_only=True)
class Whole(WholeType):
    class Meta:
        name = "whole"


@dataclass(kw_only=True)
class Width(WidthType):
    class Meta:
        name = "width"


@dataclass(kw_only=True)
class WordFont(WordFontType):
    class Meta:
        name = "word-font"


@dataclass(kw_only=True)
class Words(WordsType):
    class Meta:
        name = "words"


@dataclass(kw_only=True)
class Work(WorkType):
    class Meta:
        name = "work"


@dataclass(kw_only=True)
class WorkNumber1(WorkNumberType1):
    class Meta:
        name = "work-number"


@dataclass(kw_only=True)
class WorkTitle1(WorkTitleType1):
    class Meta:
        name = "work-title"


@dataclass(kw_only=True)
class WorkNumber2(WorkNumberType2):
    class Meta:
        name = "workNumber"


@dataclass(kw_only=True)
class WorkTitle2(WorkTitleType2):
    class Meta:
        name = "workTitle"


@dataclass(kw_only=True)
class X(XType):
    class Meta:
        name = "x"


@dataclass(kw_only=True)
class Xml(XmlType):
    class Meta:
        name = "xml"


@dataclass(kw_only=True)
class Xoff(XoffType):
    class Meta:
        name = "xoff"


@dataclass(kw_only=True)
class Xoffset(XoffsetType):
    class Meta:
        name = "xoffset"


@dataclass(kw_only=True)
class Y(YType):
    class Meta:
        name = "y"


@dataclass(kw_only=True)
class Y1(Y1Type):
    class Meta:
        name = "y1"


@dataclass(kw_only=True)
class Y2(Y2Type):
    class Meta:
        name = "y2"


@dataclass(kw_only=True)
class Yoff(YoffType):
    class Meta:
        name = "yoff"


@dataclass(kw_only=True)
class Yoffset(YoffsetType):
    class Meta:
        name = "yoffset"


@dataclass(kw_only=True)
class Z(ZType):
    class Meta:
        name = "z"


@dataclass(kw_only=True)
class ZeroBeamValue(ZeroBeamValueType):
    class Meta:
        name = "zeroBeamValue"


@dataclass(kw_only=True)
class AccidentalType1:
    class Meta:
        name = "AccidentalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bracket",
                    "type": Bracket,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "role",
                    "type": Role,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ChannelType1:
    class Meta:
        name = "ChannelType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "controller",
                    "type": Controller,
                },
                {
                    "name": "midiChannel",
                    "type": MidiChannel2,
                },
                {
                    "name": "midiPort",
                    "type": MidiPort,
                },
                {
                    "name": "mute",
                    "type": Mute,
                },
                {
                    "name": "program",
                    "type": Program2,
                },
                {
                    "name": "solo",
                    "type": Solo,
                },
                {
                    "name": "synti",
                    "type": Synti,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class EventType1:
    class Meta:
        name = "EventType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "len",
                    "type": Len,
                },
                {
                    "name": "ontime",
                    "type": Ontime,
                },
                {
                    "name": "pitch",
                    "type": Pitch,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FiguredBassItemType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "brackets",
                    "type": Brackets,
                },
                {
                    "name": "continuationLine",
                    "type": ContinuationLine,
                },
                {
                    "name": "digit",
                    "type": Digit,
                },
                {
                    "name": "prefix",
                    "type": Prefix,
                },
                {
                    "name": "suffix",
                    "type": Suffix,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FluidType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "val",
                    "type": Val,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FragmentType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "y1",
                    "type": Y1,
                },
                {
                    "name": "y2",
                    "type": Y2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class GroupsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Node",
                    "type": Node,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ImageType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Image",
                    "type": ForwardRef("Image"),
                },
                {
                    "name": "linkPath",
                    "type": LinkPath,
                },
                {
                    "name": "path",
                    "type": Path2,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "z",
                    "type": Z,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class LayoutBreakType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "pause",
                    "type": Pause,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class MidiActionType:
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "controller",
                    "type": Controller,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class NoteDotType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PageType1:
    class Meta:
        name = "PageType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "System",
                    "type": System1,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SegmentType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "color",
                    "type": Color,
                },
                {
                    "name": "leadingSpace",
                    "type": LeadingSpace,
                },
                {
                    "name": "minDistance",
                    "type": MinDistance,
                },
                {
                    "name": "off1",
                    "type": Off1,
                },
                {
                    "name": "off2",
                    "type": Off2,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "selected",
                    "type": Selected,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SlurSegmentType:
    no: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "autoplace",
                    "type": Autoplace,
                },
                {
                    "name": "color",
                    "type": Color,
                },
                {
                    "name": "o1",
                    "type": O1,
                },
                {
                    "name": "o2",
                    "type": O2,
                },
                {
                    "name": "o3",
                    "type": O3,
                },
                {
                    "name": "o4",
                    "type": O4,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class StemType1:
    class Meta:
        name = "StemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "userLen",
                    "type": UserLen,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SyntiSettingsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "f",
                    "type": F,
                },
                {
                    "name": "s",
                    "type": S,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TieSegmentType:
    no: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "o1",
                    "type": O1,
                },
                {
                    "name": "o2",
                    "type": O2,
                },
                {
                    "name": "o3",
                    "type": O3,
                },
                {
                    "name": "o4",
                    "type": O4,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TremoloBarType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "point",
                    "type": Point,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Zita1Type:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "val",
                    "type": Val,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CleflistType:
    class Meta:
        name = "cleflistType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "clef",
                    "type": Clef2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FontType:
    class Meta:
        name = "fontType"

    face: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    family: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    size: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "mag",
                    "type": Mag2,
                },
                {
                    "name": "sym",
                    "type": Sym,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class HeadType1:
    class Meta:
        name = "headType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "meta",
                    "type": Meta2,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class InstrumentType2:
    class Meta:
        name = "instrumentType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "family",
                    "type": Family2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class KeylistType:
    class Meta:
        name = "keylistType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "key",
                    "type": Key2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class LocationType:
    class Meta:
        name = "locationType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "fractions",
                    "type": Fractions,
                },
                {
                    "name": "grace",
                    "type": Grace,
                },
                {
                    "name": "measures",
                    "type": Measures,
                },
                {
                    "name": "notes",
                    "type": Notes,
                },
                {
                    "name": "staves",
                    "type": Staves,
                },
                {
                    "name": "voices",
                    "type": Voices,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class MasterType:
    class Meta:
        name = "masterType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "val",
                    "type": Val,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class NoteheadsType:
    class Meta:
        name = "noteheadsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "breve",
                    "type": Breve,
                },
                {
                    "name": "half",
                    "type": Half,
                },
                {
                    "name": "quarter",
                    "type": Quarter,
                },
                {
                    "name": "whole",
                    "type": Whole,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PType:
    class Meta:
        name = "pType"

    align: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Span,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PageMarginsType:
    class Meta:
        name = "page-marginsType"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bottom-margin",
                    "type": BottomMargin1,
                },
                {
                    "name": "left-margin",
                    "type": LeftMargin1,
                },
                {
                    "name": "right-margin",
                    "type": RightMargin1,
                },
                {
                    "name": "top-margin",
                    "type": TopMargin1,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SectionType:
    class Meta:
        name = "sectionType"

    bar_line_span: None | str = field(
        default=None,
        metadata={
            "name": "barLineSpan",
            "type": "Attribute",
        },
    )
    brackets: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    show_system_markings: None | str = field(
        default=None,
        metadata={
            "name": "showSystemMarkings",
            "type": "Attribute",
        },
    )
    thin_brackets: None | str = field(
        default=None,
        metadata={
            "name": "thinBrackets",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "family",
                    "type": Family2,
                },
                {
                    "name": "unsorted",
                    "type": Unsorted,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SigType:
    class Meta:
        name = "sigType"

    tick: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "denom",
                    "type": Denom,
                },
                {
                    "name": "nom",
                    "type": Nom,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class StringType:
    class Meta:
        name = "stringType"

    no: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "dot",
                    "type": Dot,
                },
                {
                    "name": "marker",
                    "type": Marker2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TempolistType:
    class Meta:
        name = "tempolistType"

    fix: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "tempo",
                    "type": Tempo2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Accidental1(AccidentalType1):
    class Meta:
        name = "Accidental"


@dataclass(kw_only=True)
class Channel1(ChannelType1):
    class Meta:
        name = "Channel"


@dataclass(kw_only=True)
class Event1(EventType1):
    class Meta:
        name = "Event"


@dataclass(kw_only=True)
class FiguredBassItem(FiguredBassItemType):
    pass


@dataclass(kw_only=True)
class Fluid(FluidType):
    pass


@dataclass(kw_only=True)
class Fragment(FragmentType):
    pass


@dataclass(kw_only=True)
class Groups(GroupsType):
    pass


@dataclass(kw_only=True)
class Image(ImageType):
    pass


@dataclass(kw_only=True)
class LayoutBreak(LayoutBreakType):
    pass


@dataclass(kw_only=True)
class MidiAction(MidiActionType):
    pass


@dataclass(kw_only=True)
class NoteDot(NoteDotType):
    pass


@dataclass(kw_only=True)
class Page1(PageType1):
    class Meta:
        name = "Page"


@dataclass(kw_only=True)
class Segment(SegmentType):
    pass


@dataclass(kw_only=True)
class SlurSegment(SlurSegmentType):
    pass


@dataclass(kw_only=True)
class Stem1(StemType1):
    class Meta:
        name = "Stem"


@dataclass(kw_only=True)
class SyntiSettings(SyntiSettingsType):
    pass


@dataclass(kw_only=True)
class TieSegment(TieSegmentType):
    pass


@dataclass(kw_only=True)
class TremoloBar(TremoloBarType):
    pass


@dataclass(kw_only=True)
class Zita1(Zita1Type):
    pass


@dataclass(kw_only=True)
class Cleflist(CleflistType):
    class Meta:
        name = "cleflist"


@dataclass(kw_only=True)
class Font(FontType):
    class Meta:
        name = "font"


@dataclass(kw_only=True)
class Head(HeadType1):
    class Meta:
        name = "head"


@dataclass(kw_only=True)
class Instrument2(InstrumentType2):
    class Meta:
        name = "instrument"


@dataclass(kw_only=True)
class Keylist(KeylistType):
    class Meta:
        name = "keylist"


@dataclass(kw_only=True)
class Location(LocationType):
    class Meta:
        name = "location"


@dataclass(kw_only=True)
class Master(MasterType):
    class Meta:
        name = "master"


@dataclass(kw_only=True)
class Noteheads(NoteheadsType):
    class Meta:
        name = "noteheads"


@dataclass(kw_only=True)
class P(PType):
    class Meta:
        name = "p"


@dataclass(kw_only=True)
class PageMargins(PageMarginsType):
    class Meta:
        name = "page-margins"


@dataclass(kw_only=True)
class Section(SectionType):
    class Meta:
        name = "section"


@dataclass(kw_only=True)
class Sig(SigType):
    class Meta:
        name = "sig"


@dataclass(kw_only=True)
class String(StringType):
    class Meta:
        name = "string"


@dataclass(kw_only=True)
class Tempolist(TempolistType):
    class Meta:
        name = "tempolist"


@dataclass(kw_only=True)
class BeamType1:
    class Meta:
        name = "BeamType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Fragment",
                    "type": Fragment,
                },
                {
                    "name": "StemDirection",
                    "type": StemDirection,
                },
                {
                    "name": "distribute",
                    "type": Distribute,
                },
                {
                    "name": "l1",
                    "type": L1,
                },
                {
                    "name": "l2",
                    "type": L2,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class EventsType1:
    class Meta:
        name = "EventsType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Event",
                    "type": Event1,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PageListType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Page",
                    "type": Page1,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class StringDataType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "frets",
                    "type": Frets,
                },
                {
                    "name": "string",
                    "type": String,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SynthesizerType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Fluid",
                    "type": Fluid,
                },
                {
                    "name": "Zerberus",
                    "type": Zerberus,
                },
                {
                    "name": "Zita1",
                    "type": Zita1,
                },
                {
                    "name": "f",
                    "type": F,
                },
                {
                    "name": "master",
                    "type": Master,
                },
                {
                    "name": "s",
                    "type": S,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TablatureType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "frets",
                    "type": Frets,
                },
                {
                    "name": "string",
                    "type": String,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TrillType1:
    class Meta:
        name = "TrillType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Accidental",
                    "type": Accidental1,
                },
                {
                    "name": "Segment",
                    "type": Segment,
                },
                {
                    "name": "lineWidth",
                    "type": LineWidth,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "ornamentStyle",
                    "type": OrnamentStyle,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class BType:
    class Meta:
        name = "bType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "font",
                    "type": Font,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class BottomAccidentalType:
    class Meta:
        name = "bottomAccidentalType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Accidental",
                    "type": Accidental1,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FretDiagramType2:
    class Meta:
        name = "fretDiagramType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "string",
                    "type": String,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class IType:
    class Meta:
        name = "iType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "font",
                    "type": Font,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class LinkedType:
    class Meta:
        name = "linkedType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "indexDiff",
                    "type": IndexDiff,
                },
                {
                    "name": "location",
                    "type": Location,
                },
                {
                    "name": "score",
                    "type": Score2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class NextType:
    class Meta:
        name = "nextType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "location",
                    "type": Location,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PageLayoutType:
    class Meta:
        name = "page-layoutType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "page-height",
                    "type": PageHeight1,
                },
                {
                    "name": "page-margins",
                    "type": PageMargins,
                },
                {
                    "name": "page-offset",
                    "type": PageOffset,
                },
                {
                    "name": "page-width",
                    "type": PageWidth1,
                },
                {
                    "name": "pageFormat",
                    "type": PageFormat,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PrevType:
    class Meta:
        name = "prevType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "location",
                    "type": Location,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SiglistType:
    class Meta:
        name = "siglistType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sig",
                    "type": Sig,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TdType:
    class Meta:
        name = "tdType"

    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "p",
                    "type": P,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Beam1(BeamType1):
    class Meta:
        name = "Beam"


@dataclass(kw_only=True)
class Events1(EventsType1):
    class Meta:
        name = "Events"


@dataclass(kw_only=True)
class PageList(PageListType):
    pass


@dataclass(kw_only=True)
class StringData(StringDataType):
    pass


@dataclass(kw_only=True)
class Synthesizer(SynthesizerType):
    pass


@dataclass(kw_only=True)
class Tablature(TablatureType):
    pass


@dataclass(kw_only=True)
class Trill1(TrillType1):
    class Meta:
        name = "Trill"


@dataclass(kw_only=True)
class B(BType):
    class Meta:
        name = "b"


@dataclass(kw_only=True)
class BottomAccidental(BottomAccidentalType):
    class Meta:
        name = "bottomAccidental"


@dataclass(kw_only=True)
class FretDiagram2(FretDiagramType2):
    class Meta:
        name = "fretDiagram"


@dataclass(kw_only=True)
class I(IType):
    class Meta:
        name = "i"


@dataclass(kw_only=True)
class Linked(LinkedType):
    class Meta:
        name = "linked"


@dataclass(kw_only=True)
class Next(NextType):
    class Meta:
        name = "next"


@dataclass(kw_only=True)
class PageLayout(PageLayoutType):
    class Meta:
        name = "page-layout"


@dataclass(kw_only=True)
class Prev(PrevType):
    class Meta:
        name = "prev"


@dataclass(kw_only=True)
class Siglist(SiglistType):
    class Meta:
        name = "siglist"


@dataclass(kw_only=True)
class Td(TdType):
    class Meta:
        name = "td"


@dataclass(kw_only=True)
class AmbitusType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bottomAccidental",
                    "type": BottomAccidental,
                },
                {
                    "name": "bottomPitch",
                    "type": BottomPitch,
                },
                {
                    "name": "bottomTpc",
                    "type": BottomTpc,
                },
                {
                    "name": "color",
                    "type": Color,
                },
                {
                    "name": "head",
                    "type": Head,
                },
                {
                    "name": "headType",
                    "type": HeadType1,
                },
                {
                    "name": "mirror",
                    "type": Mirror,
                },
                {
                    "name": "topPitch",
                    "type": TopPitch,
                },
                {
                    "name": "topTpc",
                    "type": TopTpc,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ArpeggioType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "span",
                    "type": Span,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "timeStretch",
                    "type": TimeStretch,
                },
                {
                    "name": "userLen1",
                    "type": UserLen1,
                },
                {
                    "name": "userLen2",
                    "type": UserLen2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ArticulationType1:
    class Meta:
        name = "ArticulationType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "anchor",
                    "type": Anchor,
                },
                {
                    "name": "color",
                    "type": Color,
                },
                {
                    "name": "direction",
                    "type": Direction,
                },
                {
                    "name": "gateTime",
                    "type": GateTime,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "ornamentStyle",
                    "type": OrnamentStyle,
                },
                {
                    "name": "play",
                    "type": Play,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "timeStretch",
                    "type": TimeStretch,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
                {
                    "name": "velocity",
                    "type": Velocity,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class BendType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "family",
                    "type": Family2,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "play",
                    "type": Play,
                },
                {
                    "name": "point",
                    "type": Point,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class BreathType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "pause",
                    "type": Pause,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "symbol",
                    "type": Symbol2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ChordLineType1:
    class Meta:
        name = "ChordLineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "straight",
                    "type": Straight,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ClefType1:
    class Meta:
        name = "ClefType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "concertClefType",
                    "type": ConcertClefType1,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "showCourtesyClef",
                    "type": ShowCourtesyClef,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "transposingClefType",
                    "type": TransposingClefType1,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FermataType1:
    class Meta:
        name = "FermataType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "placement",
                    "type": Placement,
                },
                {
                    "name": "play",
                    "type": Play,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "timeStretch",
                    "type": TimeStretch,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class KeySigType1:
    class Meta:
        name = "KeySigType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "accidental",
                    "type": Accidental2,
                },
                {
                    "name": "custom",
                    "type": Custom,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "mode",
                    "type": Mode,
                },
                {
                    "name": "showCourtesySig",
                    "type": ShowCourtesySig,
                },
                {
                    "name": "showNaturals",
                    "type": ShowNaturals,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PalmMuteType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class RepeatMeasureType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "duration",
                    "type": Duration,
                },
                {
                    "name": "durationType",
                    "type": DurationType1,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SlurType1:
    class Meta:
        name = "SlurType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    number: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "SlurSegment",
                    "type": SlurSegment,
                },
                {
                    "name": "color",
                    "type": Color,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "lineType",
                    "type": LineType1,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
                {
                    "name": "up",
                    "type": Up,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TieType1:
    class Meta:
        name = "TieType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "TieSegment",
                    "type": TieSegment,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
                {
                    "name": "up",
                    "type": Up,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TimeSigType1:
    class Meta:
        name = "TimeSigType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Groups",
                    "type": Groups,
                },
                {
                    "name": "den",
                    "type": Den,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "nom1",
                    "type": Nom1,
                },
                {
                    "name": "showCourtesy",
                    "type": ShowCourtesy,
                },
                {
                    "name": "showCourtesySig",
                    "type": ShowCourtesySig,
                },
                {
                    "name": "sigD",
                    "type": SigD,
                },
                {
                    "name": "sigN",
                    "type": SigN1,
                },
                {
                    "name": "stretchD",
                    "type": StretchD,
                },
                {
                    "name": "stretchN",
                    "type": StretchN,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TremoloType1:
    class Meta:
        name = "TremoloType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class VibratoType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TextType2:
    class Meta:
        name = "textType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "font",
                    "type": Font,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "sym",
                    "type": Sym,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TrType:
    class Meta:
        name = "trType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "td",
                    "type": Td,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Ambitus(AmbitusType):
    pass


@dataclass(kw_only=True)
class Arpeggio(ArpeggioType):
    pass


@dataclass(kw_only=True)
class Articulation1(ArticulationType1):
    class Meta:
        name = "Articulation"


@dataclass(kw_only=True)
class Bend(BendType):
    pass


@dataclass(kw_only=True)
class Breath(BreathType):
    pass


@dataclass(kw_only=True)
class ChordLine1(ChordLineType1):
    class Meta:
        name = "ChordLine"


@dataclass(kw_only=True)
class Clef1(ClefType1):
    class Meta:
        name = "Clef"


@dataclass(kw_only=True)
class Fermata1(FermataType1):
    class Meta:
        name = "Fermata"


@dataclass(kw_only=True)
class KeySig1(KeySigType1):
    class Meta:
        name = "KeySig"


@dataclass(kw_only=True)
class PalmMute(PalmMuteType):
    pass


@dataclass(kw_only=True)
class RepeatMeasure(RepeatMeasureType):
    pass


@dataclass(kw_only=True)
class Slur1(SlurType1):
    class Meta:
        name = "Slur"


@dataclass(kw_only=True)
class Tie1(TieType1):
    class Meta:
        name = "Tie"


@dataclass(kw_only=True)
class TimeSig1(TimeSigType1):
    class Meta:
        name = "TimeSig"


@dataclass(kw_only=True)
class Tremolo1(TremoloType1):
    class Meta:
        name = "Tremolo"


@dataclass(kw_only=True)
class Vibrato(VibratoType):
    pass


@dataclass(kw_only=True)
class Text2(TextType2):
    class Meta:
        name = "text"


@dataclass(kw_only=True)
class Tr(TrType):
    class Meta:
        name = "tr"


@dataclass(kw_only=True)
class DynamicType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "autoplace",
                    "type": Autoplace,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "placement",
                    "type": Placement,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
                {
                    "name": "veloChange",
                    "type": VeloChange,
                },
                {
                    "name": "veloChangeSpeed",
                    "type": VeloChangeSpeed,
                },
                {
                    "name": "velocity",
                    "type": Velocity,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FiguredBassType1:
    class Meta:
        name = "FiguredBassType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "FiguredBassItem",
                    "type": FiguredBassItem,
                },
                {
                    "name": "onNote",
                    "type": OnNote,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
                {
                    "name": "ticks",
                    "type": Ticks,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FingeringType1:
    class Meta:
        name = "FingeringType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "autoplace",
                    "type": Autoplace,
                },
                {
                    "name": "family",
                    "type": Family2,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "minDistance",
                    "type": MinDistance,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class GlissandoType1:
    class Meta:
        name = "GlissandoType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "anchor",
                    "type": Anchor,
                },
                {
                    "name": "diagonal",
                    "type": Diagonal,
                },
                {
                    "name": "glissandoStyle",
                    "type": GlissandoStyle,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "lineWidth",
                    "type": LineWidth,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "play",
                    "type": Play,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class MeasureNumberType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "text",
                    "type": Text2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class RehearsalMarkType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "halign",
                    "type": Halign,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "minDistance",
                    "type": MinDistance,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
                {
                    "name": "xoffset",
                    "type": Xoffset,
                },
                {
                    "name": "yoffset",
                    "type": Yoffset,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class StickingType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "text",
                    "type": Text2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SystemTextType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "minDistance",
                    "type": MinDistance,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "swing",
                    "type": Swing2,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TableType:
    class Meta:
        name = "tableType"

    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "tr",
                    "type": Tr,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Dynamic(DynamicType):
    pass


@dataclass(kw_only=True)
class FiguredBass1(FiguredBassType1):
    class Meta:
        name = "FiguredBass"


@dataclass(kw_only=True)
class Fingering1(FingeringType1):
    class Meta:
        name = "Fingering"


@dataclass(kw_only=True)
class Glissando1(GlissandoType1):
    class Meta:
        name = "Glissando"


@dataclass(kw_only=True)
class MeasureNumber(MeasureNumberType):
    pass


@dataclass(kw_only=True)
class RehearsalMark(RehearsalMarkType):
    pass


@dataclass(kw_only=True)
class Sticking(StickingType):
    pass


@dataclass(kw_only=True)
class SystemText(SystemTextType):
    pass


@dataclass(kw_only=True)
class Table(TableType):
    class Meta:
        name = "table"


@dataclass(kw_only=True)
class BodyType:
    class Meta:
        name = "bodyType"

    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "p",
                    "type": P,
                },
                {
                    "name": "table",
                    "type": Table,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Body(BodyType):
    class Meta:
        name = "body"


@dataclass(kw_only=True)
class HtmlType:
    class Meta:
        name = "htmlType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "body",
                    "type": Body,
                },
                {
                    "name": "head",
                    "type": Head,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Html(HtmlType):
    class Meta:
        name = "html"


@dataclass(kw_only=True)
class HtmlDataType:
    class Meta:
        name = "html-dataType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "html",
                    "type": Html,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class LongNameType:
    class Meta:
        name = "longNameType"

    pos: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "font",
                    "type": Font,
                },
                {
                    "name": "html",
                    "type": Html,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class HtmlData(HtmlDataType):
    class Meta:
        name = "html-data"


@dataclass(kw_only=True)
class LongName(LongNameType):
    class Meta:
        name = "longName"


@dataclass(kw_only=True)
class JumpType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "continueAt",
                    "type": ContinueAt,
                },
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "jumpTo",
                    "type": JumpTo,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "playRepeats",
                    "type": PlayRepeats,
                },
                {
                    "name": "playUntil",
                    "type": PlayUntil,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "systemFlag",
                    "type": SystemFlag,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class LyricsType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "align",
                    "type": Align,
                },
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "halign",
                    "type": Halign,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "no",
                    "type": No,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "syllabic",
                    "type": Syllabic,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "ticks",
                    "type": Ticks,
                },
                {
                    "name": "ticks_f",
                    "type": TicksF,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class MarkerType1:
    class Meta:
        name = "MarkerType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "label",
                    "type": Label,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "rxoffset",
                    "type": Rxoffset,
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "systemFlag",
                    "type": SystemFlag,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class NumberType1:
    class Meta:
        name = "NumberType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class StaffTextType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "MidiAction",
                    "type": MidiAction,
                },
                {
                    "name": "align",
                    "type": Align,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "channelSwitch",
                    "type": ChannelSwitch,
                },
                {
                    "name": "color",
                    "type": Color,
                },
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "framePadding",
                    "type": FramePadding,
                },
                {
                    "name": "frameWidth",
                    "type": FrameWidth,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "minDistance",
                    "type": MinDistance,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "placement",
                    "type": Placement,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "selected",
                    "type": Selected,
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "swing",
                    "type": Swing2,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TempoType1:
    class Meta:
        name = "TempoType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "family",
                    "type": Family2,
                },
                {
                    "name": "followText",
                    "type": FollowText,
                },
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "minDistance",
                    "type": MinDistance,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "systemFlag",
                    "type": SystemFlag,
                },
                {
                    "name": "tempo",
                    "type": Tempo2,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TextType1:
    class Meta:
        name = "TextType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "align",
                    "type": Align,
                },
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "layoutOffset",
                    "type": LayoutOffset,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "rxoffset",
                    "type": Rxoffset,
                },
                {
                    "name": "ryoffset",
                    "type": Ryoffset,
                },
                {
                    "name": "selected",
                    "type": Selected,
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "spatiumSizeDependent",
                    "type": SpatiumSizeDependent,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
                {
                    "name": "valign",
                    "type": Valign,
                },
                {
                    "name": "xoffset",
                    "type": Xoffset,
                },
                {
                    "name": "yoffset",
                    "type": Yoffset,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class BeginTextType:
    class Meta:
        name = "beginTextType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ContinueTextType:
    class Meta:
        name = "continueTextType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CopyrightType:
    class Meta:
        name = "copyrightType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class NameType:
    class Meta:
        name = "nameType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ShortNameType2:
    class Meta:
        name = "shortNameType"

    pos: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "font",
                    "type": Font,
                },
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "html",
                    "type": Html,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Jump(JumpType):
    pass


@dataclass(kw_only=True)
class Lyrics(LyricsType):
    pass


@dataclass(kw_only=True)
class Marker1(MarkerType1):
    class Meta:
        name = "Marker"


@dataclass(kw_only=True)
class Number(NumberType1):
    pass


@dataclass(kw_only=True)
class StaffText(StaffTextType):
    pass


@dataclass(kw_only=True)
class Tempo1(TempoType1):
    class Meta:
        name = "Tempo"


@dataclass(kw_only=True)
class Text1(TextType1):
    class Meta:
        name = "Text"


@dataclass(kw_only=True)
class BeginText(BeginTextType):
    class Meta:
        name = "beginText"


@dataclass(kw_only=True)
class ContinueText(ContinueTextType):
    class Meta:
        name = "continueText"


@dataclass(kw_only=True)
class Copyright(CopyrightType):
    class Meta:
        name = "copyright"


@dataclass(kw_only=True)
class Name(NameType):
    class Meta:
        name = "name"


@dataclass(kw_only=True)
class ShortName2(ShortNameType2):
    class Meta:
        name = "shortName"


@dataclass(kw_only=True)
class DrumType:
    pitch: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "head",
                    "type": Head,
                },
                {
                    "name": "line",
                    "type": Line,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "noteheads",
                    "type": Noteheads,
                },
                {
                    "name": "shortcut",
                    "type": Shortcut2,
                },
                {
                    "name": "stem",
                    "type": Stem2,
                },
                {
                    "name": "voice",
                    "type": ForwardRef("Voice"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class HboxType:
    class Meta:
        name = "HBoxType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "LayoutBreak",
                    "type": LayoutBreak,
                },
                {
                    "name": "Text",
                    "type": Text1,
                },
                {
                    "name": "bottomMargin",
                    "type": BottomMargin2,
                },
                {
                    "name": "boxAutoSize",
                    "type": BoxAutoSize,
                },
                {
                    "name": "leftMargin",
                    "type": LeftMargin2,
                },
                {
                    "name": "rightMargin",
                    "type": RightMargin2,
                },
                {
                    "name": "topMargin",
                    "type": TopMargin2,
                },
                {
                    "name": "width",
                    "type": Width,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class HairPinType:
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Segment",
                    "type": Segment,
                },
                {
                    "name": "beginFontFace",
                    "type": BeginFontFace,
                },
                {
                    "name": "beginFontSize",
                    "type": BeginFontSize,
                },
                {
                    "name": "beginText",
                    "type": BeginText,
                },
                {
                    "name": "beginTextAlign",
                    "type": BeginTextAlign,
                },
                {
                    "name": "continueText",
                    "type": ContinueText,
                },
                {
                    "name": "endText",
                    "type": EndText,
                },
                {
                    "name": "endTextAlign",
                    "type": EndTextAlign,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "placement",
                    "type": Placement,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "tick2",
                    "type": Tick2,
                },
                {
                    "name": "veloChange",
                    "type": VeloChange,
                },
                {
                    "name": "veloChangeMethod",
                    "type": VeloChangeMethod,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class HarmonyType1:
    class Meta:
        name = "HarmonyType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "align",
                    "type": Align,
                },
                {
                    "name": "base",
                    "type": Base,
                },
                {
                    "name": "baseCase",
                    "type": BaseCase,
                },
                {
                    "name": "extension",
                    "type": Extension,
                },
                {
                    "name": "frame",
                    "type": Frame,
                },
                {
                    "name": "frameType",
                    "type": FrameType1,
                },
                {
                    "name": "function",
                    "type": Function,
                },
                {
                    "name": "harmonyDuration",
                    "type": HarmonyDuration,
                },
                {
                    "name": "harmonyType",
                    "type": HarmonyType2,
                },
                {
                    "name": "harmonyVoiceLiteral",
                    "type": HarmonyVoiceLiteral,
                },
                {
                    "name": "harmonyVoicing",
                    "type": HarmonyVoicing,
                },
                {
                    "name": "html-data",
                    "type": HtmlData,
                },
                {
                    "name": "leftParen",
                    "type": LeftParen,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "minDistance",
                    "type": MinDistance,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "rightParen",
                    "type": RightParen,
                },
                {
                    "name": "root",
                    "type": Root,
                },
                {
                    "name": "rootCase",
                    "type": RootCase,
                },
                {
                    "name": "style",
                    "type": Style2,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class LetRingType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Segment",
                    "type": Segment,
                },
                {
                    "name": "beginText",
                    "type": BeginText,
                },
                {
                    "name": "dashGapLength",
                    "type": DashGapLength,
                },
                {
                    "name": "endHookHeight",
                    "type": EndHookHeight,
                },
                {
                    "name": "endHookType",
                    "type": EndHookType1,
                },
                {
                    "name": "lineStyle",
                    "type": LineStyle,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class OrderType:
    customised: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    customized: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "family",
                    "type": Family2,
                },
                {
                    "name": "instrument",
                    "type": Instrument2,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "section",
                    "type": Section,
                },
                {
                    "name": "soloists",
                    "type": Soloists,
                },
                {
                    "name": "unsorted",
                    "type": Unsorted,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class OttavaType:
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Segment",
                    "type": Segment,
                },
                {
                    "name": "beginText",
                    "type": BeginText,
                },
                {
                    "name": "continueText",
                    "type": ContinueText,
                },
                {
                    "name": "endHookHeight",
                    "type": EndHookHeight,
                },
                {
                    "name": "lineStyle",
                    "type": LineStyle,
                },
                {
                    "name": "lineWidth",
                    "type": LineWidth,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PedalType1:
    class Meta:
        name = "PedalType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Segment",
                    "type": Segment,
                },
                {
                    "name": "beginHook",
                    "type": BeginHook,
                },
                {
                    "name": "beginHookHeight",
                    "type": BeginHookHeight,
                },
                {
                    "name": "beginHookType",
                    "type": BeginHookType1,
                },
                {
                    "name": "beginSymbol",
                    "type": BeginSymbol,
                },
                {
                    "name": "beginSymbolOffset",
                    "type": BeginSymbolOffset,
                },
                {
                    "name": "beginText",
                    "type": BeginText,
                },
                {
                    "name": "beginTextPlace",
                    "type": BeginTextPlace,
                },
                {
                    "name": "color",
                    "type": Color,
                },
                {
                    "name": "continueText",
                    "type": ContinueText,
                },
                {
                    "name": "continueTextPlace",
                    "type": ContinueTextPlace,
                },
                {
                    "name": "diagonal",
                    "type": Diagonal,
                },
                {
                    "name": "endHook",
                    "type": EndHook,
                },
                {
                    "name": "endHookHeight",
                    "type": EndHookHeight,
                },
                {
                    "name": "endHookType",
                    "type": EndHookType1,
                },
                {
                    "name": "endText",
                    "type": EndText,
                },
                {
                    "name": "lineColor",
                    "type": LineColor,
                },
                {
                    "name": "lineStyle",
                    "type": LineStyle,
                },
                {
                    "name": "lineVisible",
                    "type": LineVisible,
                },
                {
                    "name": "lineWidth",
                    "type": LineWidth,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "tick2",
                    "type": Tick2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class StaffTypeType1:
    class Meta:
        name = "StaffTypeType"

    group: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    idx: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "barlines",
                    "type": Barlines,
                },
                {
                    "name": "clef",
                    "type": Clef2,
                },
                {
                    "name": "durationFontName",
                    "type": DurationFontName,
                },
                {
                    "name": "durationFontSize",
                    "type": DurationFontSize,
                },
                {
                    "name": "durationFontY",
                    "type": DurationFontY,
                },
                {
                    "name": "durations",
                    "type": Durations,
                },
                {
                    "name": "fretFontName",
                    "type": FretFontName,
                },
                {
                    "name": "fretFontSize",
                    "type": FretFontSize,
                },
                {
                    "name": "fretFontY",
                    "type": FretFontY,
                },
                {
                    "name": "invisible",
                    "type": Invisible,
                },
                {
                    "name": "keysig",
                    "type": Keysig2,
                },
                {
                    "name": "lineDistance",
                    "type": LineDistance,
                },
                {
                    "name": "lines",
                    "type": Lines,
                },
                {
                    "name": "linesThrough",
                    "type": LinesThrough,
                },
                {
                    "name": "minimStyle",
                    "type": MinimStyle,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "onLines",
                    "type": OnLines,
                },
                {
                    "name": "showRests",
                    "type": ShowRests,
                },
                {
                    "name": "showTabFingering",
                    "type": ShowTabFingering,
                },
                {
                    "name": "slashStyle",
                    "type": SlashStyle,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "stemless",
                    "type": Stemless,
                },
                {
                    "name": "stemsDown",
                    "type": StemsDown,
                },
                {
                    "name": "stemsThrough",
                    "type": StemsThrough,
                },
                {
                    "name": "timesig",
                    "type": Timesig2,
                },
                {
                    "name": "upsideDown",
                    "type": UpsideDown,
                },
                {
                    "name": "useNumbers",
                    "type": UseNumbers,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SymbolType1:
    class Meta:
        name = "SymbolType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "font",
                    "type": Font,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TboxType:
    class Meta:
        name = "TBoxType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "LayoutBreak",
                    "type": LayoutBreak,
                },
                {
                    "name": "Text",
                    "type": Text1,
                },
                {
                    "name": "bottomGap",
                    "type": BottomGap,
                },
                {
                    "name": "bottomMargin",
                    "type": BottomMargin2,
                },
                {
                    "name": "height",
                    "type": Height,
                },
                {
                    "name": "leftMargin",
                    "type": LeftMargin2,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "rightMargin",
                    "type": RightMargin2,
                },
                {
                    "name": "topGap",
                    "type": TopGap,
                },
                {
                    "name": "topMargin",
                    "type": TopMargin2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TextLineType:
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    system: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Segment",
                    "type": Segment,
                },
                {
                    "name": "beginHookHeight",
                    "type": BeginHookHeight,
                },
                {
                    "name": "beginHookType",
                    "type": BeginHookType1,
                },
                {
                    "name": "beginText",
                    "type": BeginText,
                },
                {
                    "name": "beginTextPlace",
                    "type": BeginTextPlace,
                },
                {
                    "name": "continueText",
                    "type": ContinueText,
                },
                {
                    "name": "continueTextPlace",
                    "type": ContinueTextPlace,
                },
                {
                    "name": "dashGapLength",
                    "type": DashGapLength,
                },
                {
                    "name": "dashLineLength",
                    "type": DashLineLength,
                },
                {
                    "name": "diagonal",
                    "type": Diagonal,
                },
                {
                    "name": "endHook",
                    "type": EndHook,
                },
                {
                    "name": "endHookHeight",
                    "type": EndHookHeight,
                },
                {
                    "name": "endHookType",
                    "type": EndHookType1,
                },
                {
                    "name": "endText",
                    "type": EndText,
                },
                {
                    "name": "endTextAlign",
                    "type": EndTextAlign,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "lineColor",
                    "type": LineColor,
                },
                {
                    "name": "lineStyle",
                    "type": LineStyle,
                },
                {
                    "name": "lineVisible",
                    "type": LineVisible,
                },
                {
                    "name": "lineWidth",
                    "type": LineWidth,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "tick2",
                    "type": Tick2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TextStyleType:
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "align",
                    "type": Align,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "circle",
                    "type": Circle,
                },
                {
                    "name": "family",
                    "type": Family2,
                },
                {
                    "name": "foregroundColor",
                    "type": ForegroundColor,
                },
                {
                    "name": "frameColor",
                    "type": FrameColor,
                },
                {
                    "name": "frameRound",
                    "type": FrameRound,
                },
                {
                    "name": "frameWidth",
                    "type": FrameWidth,
                },
                {
                    "name": "frameWidthS",
                    "type": FrameWidthS,
                },
                {
                    "name": "halign",
                    "type": Halign,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "offsetType",
                    "type": OffsetType1,
                },
                {
                    "name": "paddingWidth",
                    "type": PaddingWidth,
                },
                {
                    "name": "paddingWidthS",
                    "type": PaddingWidthS,
                },
                {
                    "name": "rxoffset",
                    "type": Rxoffset,
                },
                {
                    "name": "ryoffset",
                    "type": Ryoffset,
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "sizeIsSpatiumDependent",
                    "type": SizeIsSpatiumDependent,
                },
                {
                    "name": "systemFlag",
                    "type": SystemFlag,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "valign",
                    "type": Valign,
                },
                {
                    "name": "xoffset",
                    "type": Xoffset,
                },
                {
                    "name": "yoffset",
                    "type": Yoffset,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TupletType1:
    class Meta:
        name = "TupletType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Number",
                    "type": Number,
                },
                {
                    "name": "Tuplet",
                    "type": ForwardRef("Tuplet1"),
                },
                {
                    "name": "actualNotes",
                    "type": ActualNotes2,
                },
                {
                    "name": "autoplace",
                    "type": Autoplace,
                },
                {
                    "name": "baseDots",
                    "type": BaseDots,
                },
                {
                    "name": "baseNote",
                    "type": BaseNote,
                },
                {
                    "name": "bracketType",
                    "type": BracketType1,
                },
                {
                    "name": "direction",
                    "type": Direction,
                },
                {
                    "name": "family",
                    "type": Family2,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "lineWidth",
                    "type": LineWidth,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "normalNotes",
                    "type": NormalNotes2,
                },
                {
                    "name": "numberType",
                    "type": NumberType,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "p1",
                    "type": P1,
                },
                {
                    "name": "p2",
                    "type": P2,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class VboxType:
    class Meta:
        name = "VBoxType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Image",
                    "type": Image,
                },
                {
                    "name": "LayoutBreak",
                    "type": LayoutBreak,
                },
                {
                    "name": "Text",
                    "type": Text1,
                },
                {
                    "name": "bottomGap",
                    "type": BottomGap,
                },
                {
                    "name": "bottomMargin",
                    "type": BottomMargin2,
                },
                {
                    "name": "boxAutoSize",
                    "type": BoxAutoSize,
                },
                {
                    "name": "height",
                    "type": Height,
                },
                {
                    "name": "leftMargin",
                    "type": LeftMargin2,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "rightMargin",
                    "type": RightMargin2,
                },
                {
                    "name": "topGap",
                    "type": TopGap,
                },
                {
                    "name": "topMargin",
                    "type": TopMargin2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class VoltaType1:
    class Meta:
        name = "VoltaType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Segment",
                    "type": Segment,
                },
                {
                    "name": "anchor",
                    "type": Anchor,
                },
                {
                    "name": "beginFontStyle",
                    "type": BeginFontStyle,
                },
                {
                    "name": "beginText",
                    "type": BeginText,
                },
                {
                    "name": "endHook",
                    "type": EndHook,
                },
                {
                    "name": "endHookType",
                    "type": EndHookType1,
                },
                {
                    "name": "endings",
                    "type": Endings,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "tick2",
                    "type": Tick2,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ChordType2:
    class Meta:
        name = "chordType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "degree",
                    "type": Degree,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "render",
                    "type": Render,
                },
                {
                    "name": "voicing",
                    "type": Voicing,
                },
                {
                    "name": "xml",
                    "type": Xml,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Drum(DrumType):
    pass


@dataclass(kw_only=True)
class Hbox(HboxType):
    class Meta:
        name = "HBox"


@dataclass(kw_only=True)
class HairPin(HairPinType):
    pass


@dataclass(kw_only=True)
class Harmony1(HarmonyType1):
    class Meta:
        name = "Harmony"


@dataclass(kw_only=True)
class LetRing(LetRingType):
    pass


@dataclass(kw_only=True)
class Order(OrderType):
    pass


@dataclass(kw_only=True)
class Ottava(OttavaType):
    pass


@dataclass(kw_only=True)
class Pedal1(PedalType1):
    class Meta:
        name = "Pedal"


@dataclass(kw_only=True)
class StaffType2(StaffTypeType1):
    class Meta:
        name = "StaffType"


@dataclass(kw_only=True)
class Symbol1(SymbolType1):
    class Meta:
        name = "Symbol"


@dataclass(kw_only=True)
class Tbox(TboxType):
    class Meta:
        name = "TBox"


@dataclass(kw_only=True)
class TextLine(TextLineType):
    pass


@dataclass(kw_only=True)
class TextStyle(TextStyleType):
    pass


@dataclass(kw_only=True)
class Tuplet1(TupletType1):
    class Meta:
        name = "Tuplet"


@dataclass(kw_only=True)
class Vbox(VboxType):
    class Meta:
        name = "VBox"


@dataclass(kw_only=True)
class Volta1(VoltaType1):
    class Meta:
        name = "Volta"


@dataclass(kw_only=True)
class Chord2(ChordType2):
    class Meta:
        name = "chord"


@dataclass(kw_only=True)
class BarLineType1:
    class Meta:
        name = "BarLineType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Symbol",
                    "type": Symbol1,
                },
                {
                    "name": "autoplace",
                    "type": Autoplace,
                },
                {
                    "name": "color",
                    "type": Color,
                },
                {
                    "name": "customSubtype",
                    "type": CustomSubtype,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "span",
                    "type": Span,
                },
                {
                    "name": "spanFromOffset",
                    "type": SpanFromOffset,
                },
                {
                    "name": "spanToOffset",
                    "type": SpanToOffset,
                },
                {
                    "name": "subtype",
                    "type": Subtype,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ChordListType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "chord",
                    "type": Chord2,
                },
                {
                    "name": "font",
                    "type": Font,
                },
                {
                    "name": "renderBase",
                    "type": RenderBase,
                },
                {
                    "name": "renderRoot",
                    "type": RenderRoot,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FretDiagramType1:
    class Meta:
        name = "FretDiagramType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Harmony",
                    "type": Harmony1,
                },
                {
                    "name": "fretDiagram",
                    "type": FretDiagram2,
                },
                {
                    "name": "frets",
                    "type": Frets,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "string",
                    "type": String,
                },
                {
                    "name": "strings",
                    "type": Strings,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class InstrumentType1:
    class Meta:
        name = "InstrumentType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Articulation",
                    "type": Articulation1,
                },
                {
                    "name": "Channel",
                    "type": Channel1,
                },
                {
                    "name": "Drum",
                    "type": Drum,
                },
                {
                    "name": "MidiAction",
                    "type": MidiAction,
                },
                {
                    "name": "StringData",
                    "type": StringData,
                },
                {
                    "name": "Tablature",
                    "type": Tablature,
                },
                {
                    "name": "clef",
                    "type": Clef2,
                },
                {
                    "name": "concertClef",
                    "type": ConcertClef,
                },
                {
                    "name": "instrumentId",
                    "type": InstrumentId,
                },
                {
                    "name": "longName",
                    "type": LongName,
                },
                {
                    "name": "maxPitchA",
                    "type": MaxPitchA,
                },
                {
                    "name": "maxPitchP",
                    "type": MaxPitchP,
                },
                {
                    "name": "minPitchA",
                    "type": MinPitchA,
                },
                {
                    "name": "minPitchP",
                    "type": MinPitchP,
                },
                {
                    "name": "shortName",
                    "type": ShortName2,
                },
                {
                    "name": "singleNoteDynamics",
                    "type": SingleNoteDynamics,
                },
                {
                    "name": "trackName",
                    "type": TrackName2,
                },
                {
                    "name": "transposeChromatic",
                    "type": TransposeChromatic,
                },
                {
                    "name": "transposeDiatonic",
                    "type": TransposeDiatonic,
                },
                {
                    "name": "transposingClef",
                    "type": TransposingClef,
                },
                {
                    "name": "useDrumset",
                    "type": UseDrumset,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class RestType1:
    class Meta:
        name = "RestType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Articulation",
                    "type": Articulation1,
                },
                {
                    "name": "Beam",
                    "type": Beam1,
                },
                {
                    "name": "BeamMode",
                    "type": BeamMode,
                },
                {
                    "name": "Lyrics",
                    "type": Lyrics,
                },
                {
                    "name": "NoteDot",
                    "type": NoteDot,
                },
                {
                    "name": "Symbol",
                    "type": Symbol1,
                },
                {
                    "name": "Tuplet",
                    "type": Tuplet1,
                },
                {
                    "name": "dots",
                    "type": Dots,
                },
                {
                    "name": "duration",
                    "type": Duration,
                },
                {
                    "name": "durationType",
                    "type": DurationType1,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "selected",
                    "type": Selected,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "ticklen",
                    "type": Ticklen,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SpannerType:
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Glissando",
                    "type": Glissando1,
                },
                {
                    "name": "HairPin",
                    "type": HairPin,
                },
                {
                    "name": "LetRing",
                    "type": LetRing,
                },
                {
                    "name": "Ottava",
                    "type": Ottava,
                },
                {
                    "name": "PalmMute",
                    "type": PalmMute,
                },
                {
                    "name": "Pedal",
                    "type": Pedal1,
                },
                {
                    "name": "Slur",
                    "type": Slur1,
                },
                {
                    "name": "TextLine",
                    "type": TextLine,
                },
                {
                    "name": "Tie",
                    "type": Tie1,
                },
                {
                    "name": "Trill",
                    "type": Trill1,
                },
                {
                    "name": "Vibrato",
                    "type": Vibrato,
                },
                {
                    "name": "Volta",
                    "type": Volta1,
                },
                {
                    "name": "next",
                    "type": Next,
                },
                {
                    "name": "prev",
                    "type": Prev,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class BarLine1(BarLineType1):
    class Meta:
        name = "BarLine"


@dataclass(kw_only=True)
class ChordList(ChordListType):
    pass


@dataclass(kw_only=True)
class FretDiagram1(FretDiagramType1):
    class Meta:
        name = "FretDiagram"


@dataclass(kw_only=True)
class Instrument1(InstrumentType1):
    class Meta:
        name = "Instrument"


@dataclass(kw_only=True)
class Rest1(RestType1):
    class Meta:
        name = "Rest"


@dataclass(kw_only=True)
class Spanner(SpannerType):
    pass


@dataclass(kw_only=True)
class InstrumentChangeType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Instrument",
                    "type": Instrument1,
                },
                {
                    "name": "init",
                    "type": Init,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "text",
                    "type": Text2,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class NoteType1:
    class Meta:
        name = "NoteType"

    pitch: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tpc: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Accidental",
                    "type": Accidental1,
                },
                {
                    "name": "Bend",
                    "type": Bend,
                },
                {
                    "name": "Events",
                    "type": Events1,
                },
                {
                    "name": "Fingering",
                    "type": Fingering1,
                },
                {
                    "name": "Glissando",
                    "type": Glissando1,
                },
                {
                    "name": "Image",
                    "type": Image,
                },
                {
                    "name": "NoteDot",
                    "type": NoteDot,
                },
                {
                    "name": "Spanner",
                    "type": Spanner,
                },
                {
                    "name": "Symbol",
                    "type": Symbol1,
                },
                {
                    "name": "Text",
                    "type": Text1,
                },
                {
                    "name": "Tie",
                    "type": Tie1,
                },
                {
                    "name": "color",
                    "type": Color,
                },
                {
                    "name": "dotPosition",
                    "type": DotPosition,
                },
                {
                    "name": "endSpanner",
                    "type": EndSpanner,
                },
                {
                    "name": "fixed",
                    "type": Fixed,
                },
                {
                    "name": "fixedLine",
                    "type": FixedLine,
                },
                {
                    "name": "fret",
                    "type": Fret,
                },
                {
                    "name": "ghost",
                    "type": Ghost,
                },
                {
                    "name": "head",
                    "type": Head,
                },
                {
                    "name": "headType",
                    "type": HeadType1,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "mirror",
                    "type": Mirror,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "pitch",
                    "type": Pitch,
                },
                {
                    "name": "play",
                    "type": Play,
                },
                {
                    "name": "pos",
                    "type": Pos,
                },
                {
                    "name": "selected",
                    "type": Selected,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "string",
                    "type": String,
                },
                {
                    "name": "tpc",
                    "type": Tpc,
                },
                {
                    "name": "tpc2",
                    "type": Tpc2,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
                {
                    "name": "userAccidental",
                    "type": UserAccidental,
                },
                {
                    "name": "veloType",
                    "type": VeloType,
                },
                {
                    "name": "velocity",
                    "type": Velocity,
                },
                {
                    "name": "visible",
                    "type": Visible,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class StyleType1:
    class Meta:
        name = "StyleType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ArpeggioHiddenInStdIfTab",
                    "type": ArpeggioHiddenInStdIfTab,
                },
                {
                    "name": "ArpeggioHookLen",
                    "type": ArpeggioHookLen,
                },
                {
                    "name": "ArpeggioLineWidth",
                    "type": ArpeggioLineWidth,
                },
                {
                    "name": "ArpeggioNoteDistance",
                    "type": ArpeggioNoteDistance,
                },
                {
                    "name": "ChordList",
                    "type": ChordList,
                },
                {
                    "name": "DfermataAnchor",
                    "type": DfermataAnchor,
                },
                {
                    "name": "DlongfermataAnchor",
                    "type": DlongfermataAnchor,
                },
                {
                    "name": "DmarcatoAnchor",
                    "type": DmarcatoAnchor,
                },
                {
                    "name": "DownMordentAnchor",
                    "type": DownMordentAnchor,
                },
                {
                    "name": "DownbowAnchor",
                    "type": DownbowAnchor,
                },
                {
                    "name": "DportatoAnchor",
                    "type": DportatoAnchor,
                },
                {
                    "name": "DshortfermataAnchor",
                    "type": DshortfermataAnchor,
                },
                {
                    "name": "DstaccatissimoAnchor",
                    "type": DstaccatissimoAnchor,
                },
                {
                    "name": "DverylongfermataAnchor",
                    "type": DverylongfermataAnchor,
                },
                {
                    "name": "EspressivoAnchor",
                    "type": EspressivoAnchor,
                },
                {
                    "name": "FixMeasureNumbers",
                    "type": FixMeasureNumbers,
                },
                {
                    "name": "FixMeasureWidth",
                    "type": FixMeasureWidth,
                },
                {
                    "name": "MordentAnchor",
                    "type": MordentAnchor,
                },
                {
                    "name": "OuvertAnchor",
                    "type": OuvertAnchor,
                },
                {
                    "name": "PlusstopAnchor",
                    "type": PlusstopAnchor,
                },
                {
                    "name": "PrallAnchor",
                    "type": PrallAnchor,
                },
                {
                    "name": "PrallMordentAnchor",
                    "type": PrallMordentAnchor,
                },
                {
                    "name": "PrallPrallAnchor",
                    "type": PrallPrallAnchor,
                },
                {
                    "name": "SforzatoaccentAnchor",
                    "type": SforzatoaccentAnchor,
                },
                {
                    "name": "SnappizzicatorAnchor",
                    "type": SnappizzicatorAnchor,
                },
                {
                    "name": "Spatium",
                    "type": Spatium1,
                },
                {
                    "name": "StaccatoAnchor",
                    "type": StaccatoAnchor,
                },
                {
                    "name": "TenutoAnchor",
                    "type": TenutoAnchor,
                },
                {
                    "name": "TextStyle",
                    "type": TextStyle,
                },
                {
                    "name": "ThumbAnchor",
                    "type": ThumbAnchor,
                },
                {
                    "name": "TrillAnchor",
                    "type": TrillAnchor,
                },
                {
                    "name": "TurnAnchor",
                    "type": TurnAnchor,
                },
                {
                    "name": "UfermataAnchor",
                    "type": UfermataAnchor,
                },
                {
                    "name": "UlongfermataAnchor",
                    "type": UlongfermataAnchor,
                },
                {
                    "name": "UmarcatoAnchor",
                    "type": UmarcatoAnchor,
                },
                {
                    "name": "UpMordentAnchor",
                    "type": UpMordentAnchor,
                },
                {
                    "name": "UpPrallAnchor",
                    "type": UpPrallAnchor,
                },
                {
                    "name": "UpbowAnchor",
                    "type": UpbowAnchor,
                },
                {
                    "name": "UportatoAnchor",
                    "type": UportatoAnchor,
                },
                {
                    "name": "UshortfermataAnchor",
                    "type": UshortfermataAnchor,
                },
                {
                    "name": "UstaccatissimoAnchor",
                    "type": UstaccatissimoAnchor,
                },
                {
                    "name": "UverylongfermataAnchor",
                    "type": UverylongfermataAnchor,
                },
                {
                    "name": "accidentalDistance",
                    "type": AccidentalDistance,
                },
                {
                    "name": "accidentalNoteDistance",
                    "type": AccidentalNoteDistance,
                },
                {
                    "name": "akkoladeDistance",
                    "type": AkkoladeDistance,
                },
                {
                    "name": "allCapsNoteNames",
                    "type": AllCapsNoteNames,
                },
                {
                    "name": "alwaysShowBracketsWhenEmptyStavesAreHidden",
                    "type": AlwaysShowBracketsWhenEmptyStavesAreHidden,
                },
                {
                    "name": "automaticCapitalization",
                    "type": AutomaticCapitalization,
                },
                {
                    "name": "barAccidentalDistance",
                    "type": BarAccidentalDistance,
                },
                {
                    "name": "barGraceDistance",
                    "type": BarGraceDistance,
                },
                {
                    "name": "barNoteDistance",
                    "type": BarNoteDistance,
                },
                {
                    "name": "barWidth",
                    "type": BarWidth,
                },
                {
                    "name": "beamDistance",
                    "type": BeamDistance,
                },
                {
                    "name": "beamMaxSlope",
                    "type": BeamMaxSlope,
                },
                {
                    "name": "beamMinLen",
                    "type": BeamMinLen,
                },
                {
                    "name": "beamMinSlope",
                    "type": BeamMinSlope,
                },
                {
                    "name": "beamWidth",
                    "type": BeamWidth,
                },
                {
                    "name": "beginRepeatLeftMargin",
                    "type": BeginRepeatLeftMargin,
                },
                {
                    "name": "bendAlign",
                    "type": BendAlign,
                },
                {
                    "name": "bendFontFace",
                    "type": BendFontFace,
                },
                {
                    "name": "bendFontSize",
                    "type": BendFontSize,
                },
                {
                    "name": "bendFramePadding",
                    "type": BendFramePadding,
                },
                {
                    "name": "bendFrameWidth",
                    "type": BendFrameWidth,
                },
                {
                    "name": "bracketDistance",
                    "type": BracketDistance,
                },
                {
                    "name": "bracketWidth",
                    "type": BracketWidth,
                },
                {
                    "name": "chordDescriptionFile",
                    "type": ChordDescriptionFile,
                },
                {
                    "name": "chordExtensionAdjust",
                    "type": ChordExtensionAdjust,
                },
                {
                    "name": "chordExtensionMag",
                    "type": ChordExtensionMag,
                },
                {
                    "name": "chordModifierAdjust",
                    "type": ChordModifierAdjust,
                },
                {
                    "name": "chordModifierMag",
                    "type": ChordModifierMag,
                },
                {
                    "name": "chordNamesUseJazzFont",
                    "type": ChordNamesUseJazzFont,
                },
                {
                    "name": "chordStyle",
                    "type": ChordStyle,
                },
                {
                    "name": "chordSymbolAAlign",
                    "type": ChordSymbolAalign,
                },
                {
                    "name": "chordSymbolAFontFace",
                    "type": ChordSymbolAfontFace,
                },
                {
                    "name": "chordSymbolAFontSize",
                    "type": ChordSymbolAfontSize,
                },
                {
                    "name": "chordSymbolAFontStyle",
                    "type": ChordSymbolAfontStyle,
                },
                {
                    "name": "chordSymbolAFramePadding",
                    "type": ChordSymbolAframePadding,
                },
                {
                    "name": "chordSymbolAFrameWidth",
                    "type": ChordSymbolAframeWidth,
                },
                {
                    "name": "chordSymbolBAlign",
                    "type": ChordSymbolBalign,
                },
                {
                    "name": "chordSymbolBFontFace",
                    "type": ChordSymbolBfontFace,
                },
                {
                    "name": "chordSymbolBFontSize",
                    "type": ChordSymbolBfontSize,
                },
                {
                    "name": "chordSymbolBPosAbove",
                    "type": ChordSymbolBposAbove,
                },
                {
                    "name": "chordSymbolPosAbove",
                    "type": ChordSymbolPosAbove,
                },
                {
                    "name": "chordsXmlFile",
                    "type": ChordsXmlFile,
                },
                {
                    "name": "clefBarlineDistance",
                    "type": ClefBarlineDistance,
                },
                {
                    "name": "clefKeyRightMargin",
                    "type": ClefKeyRightMargin,
                },
                {
                    "name": "clefLeftMargin",
                    "type": ClefLeftMargin,
                },
                {
                    "name": "composerFontFace",
                    "type": ComposerFontFace,
                },
                {
                    "name": "composerFontSize",
                    "type": ComposerFontSize,
                },
                {
                    "name": "composerFontSpatiumDependent",
                    "type": ComposerFontSpatiumDependent,
                },
                {
                    "name": "composerFontStyle",
                    "type": ComposerFontStyle,
                },
                {
                    "name": "composerFramePadding",
                    "type": ComposerFramePadding,
                },
                {
                    "name": "composerFrameRound",
                    "type": ComposerFrameRound,
                },
                {
                    "name": "composerFrameWidth",
                    "type": ComposerFrameWidth,
                },
                {
                    "name": "concertPitch",
                    "type": ConcertPitch,
                },
                {
                    "name": "createMultiMeasureRests",
                    "type": CreateMultiMeasureRests,
                },
                {
                    "name": "crossMeasureValues",
                    "type": CrossMeasureValues,
                },
                {
                    "name": "defaultAlign",
                    "type": DefaultAlign,
                },
                {
                    "name": "defaultFontFace",
                    "type": DefaultFontFace,
                },
                {
                    "name": "defaultFontSpatiumDependent",
                    "type": DefaultFontSpatiumDependent,
                },
                {
                    "name": "defaultFramePadding",
                    "type": DefaultFramePadding,
                },
                {
                    "name": "defaultFrameRound",
                    "type": DefaultFrameRound,
                },
                {
                    "name": "defaultFrameWidth",
                    "type": DefaultFrameWidth,
                },
                {
                    "name": "defaultOffset",
                    "type": DefaultOffset,
                },
                {
                    "name": "defaultsVersion",
                    "type": DefaultsVersion,
                },
                {
                    "name": "dividerLeft",
                    "type": DividerLeft,
                },
                {
                    "name": "dontHidStavesInFirstSystm",
                    "type": DontHidStavesInFirstSystm,
                },
                {
                    "name": "dotDotDistance",
                    "type": DotDotDistance,
                },
                {
                    "name": "dotNoteDistance",
                    "type": DotNoteDistance,
                },
                {
                    "name": "doubleBarDistance",
                    "type": DoubleBarDistance,
                },
                {
                    "name": "doubleBarWidth",
                    "type": DoubleBarWidth,
                },
                {
                    "name": "dynamicsFontFace",
                    "type": DynamicsFontFace,
                },
                {
                    "name": "dynamicsFontItalic",
                    "type": DynamicsFontItalic,
                },
                {
                    "name": "dynamicsFontSize",
                    "type": DynamicsFontSize,
                },
                {
                    "name": "dynamicsFontStyle",
                    "type": DynamicsFontStyle,
                },
                {
                    "name": "dynamicsFramePadding",
                    "type": DynamicsFramePadding,
                },
                {
                    "name": "dynamicsFrameWidth",
                    "type": DynamicsFrameWidth,
                },
                {
                    "name": "dynamicsPosAbove",
                    "type": DynamicsPosAbove,
                },
                {
                    "name": "dynamicsPosBelow",
                    "type": DynamicsPosBelow,
                },
                {
                    "name": "enableIndentationOnFirstSystem",
                    "type": EnableIndentationOnFirstSystem,
                },
                {
                    "name": "enableVerticalSpread",
                    "type": EnableVerticalSpread,
                },
                {
                    "name": "endBarDistance",
                    "type": EndBarDistance,
                },
                {
                    "name": "endBarWidth",
                    "type": EndBarWidth,
                },
                {
                    "name": "evenFooterC",
                    "type": EvenFooterC,
                },
                {
                    "name": "evenFooterL",
                    "type": EvenFooterL,
                },
                {
                    "name": "evenFooterR",
                    "type": EvenFooterR,
                },
                {
                    "name": "evenHeaderC",
                    "type": EvenHeaderC,
                },
                {
                    "name": "evenHeaderL",
                    "type": EvenHeaderL,
                },
                {
                    "name": "evenHeaderR",
                    "type": EvenHeaderR,
                },
                {
                    "name": "expressionFontFace",
                    "type": ExpressionFontFace,
                },
                {
                    "name": "expressionFontSize",
                    "type": ExpressionFontSize,
                },
                {
                    "name": "expressionFramePadding",
                    "type": ExpressionFramePadding,
                },
                {
                    "name": "expressionFrameWidth",
                    "type": ExpressionFrameWidth,
                },
                {
                    "name": "fermataPosAbove",
                    "type": FermataPosAbove,
                },
                {
                    "name": "fermataPosBelow",
                    "type": FermataPosBelow,
                },
                {
                    "name": "figuredBassFontFace",
                    "type": FiguredBassFontFace,
                },
                {
                    "name": "fingeringFontFace",
                    "type": FingeringFontFace,
                },
                {
                    "name": "fingeringFontSize",
                    "type": FingeringFontSize,
                },
                {
                    "name": "fingeringFramePadding",
                    "type": FingeringFramePadding,
                },
                {
                    "name": "fingeringFrameRound",
                    "type": FingeringFrameRound,
                },
                {
                    "name": "fingeringFrameWidth",
                    "type": FingeringFrameWidth,
                },
                {
                    "name": "footerAlign",
                    "type": FooterAlign,
                },
                {
                    "name": "footerFontFace",
                    "type": FooterFontFace,
                },
                {
                    "name": "footerFontSize",
                    "type": FooterFontSize,
                },
                {
                    "name": "footerFramePadding",
                    "type": FooterFramePadding,
                },
                {
                    "name": "footerFrameWidth",
                    "type": FooterFrameWidth,
                },
                {
                    "name": "footerOddEven",
                    "type": FooterOddEven,
                },
                {
                    "name": "frameAlign",
                    "type": FrameAlign,
                },
                {
                    "name": "frameFontFace",
                    "type": FrameFontFace,
                },
                {
                    "name": "frameFontSize",
                    "type": FrameFontSize,
                },
                {
                    "name": "frameFontSpatiumDependent",
                    "type": FrameFontSpatiumDependent,
                },
                {
                    "name": "frameFramePadding",
                    "type": FrameFramePadding,
                },
                {
                    "name": "frameFrameWidth",
                    "type": FrameFrameWidth,
                },
                {
                    "name": "frameSystemDistance",
                    "type": FrameSystemDistance,
                },
                {
                    "name": "gateTime",
                    "type": GateTime,
                },
                {
                    "name": "genClef",
                    "type": GenClef,
                },
                {
                    "name": "genCourtesyClef",
                    "type": GenCourtesyClef,
                },
                {
                    "name": "genCourtesyKeysig",
                    "type": GenCourtesyKeysig,
                },
                {
                    "name": "genCourtesyTimesig",
                    "type": GenCourtesyTimesig,
                },
                {
                    "name": "genKeysig",
                    "type": GenKeysig,
                },
                {
                    "name": "genTimesig",
                    "type": GenTimesig,
                },
                {
                    "name": "glissandoAlign",
                    "type": GlissandoAlign,
                },
                {
                    "name": "glissandoFontFace",
                    "type": GlissandoFontFace,
                },
                {
                    "name": "glissandoFontSize",
                    "type": GlissandoFontSize,
                },
                {
                    "name": "glissandoFramePadding",
                    "type": GlissandoFramePadding,
                },
                {
                    "name": "glissandoFrameWidth",
                    "type": GlissandoFrameWidth,
                },
                {
                    "name": "graceNoteMag",
                    "type": GraceNoteMag,
                },
                {
                    "name": "hairpinContHeight",
                    "type": HairpinContHeight,
                },
                {
                    "name": "hairpinFontFace",
                    "type": HairpinFontFace,
                },
                {
                    "name": "hairpinFontSize",
                    "type": HairpinFontSize,
                },
                {
                    "name": "hairpinFramePadding",
                    "type": HairpinFramePadding,
                },
                {
                    "name": "hairpinFrameWidth",
                    "type": HairpinFrameWidth,
                },
                {
                    "name": "hairpinHeight",
                    "type": HairpinHeight,
                },
                {
                    "name": "hairpinWidth",
                    "type": HairpinWidth,
                },
                {
                    "name": "harmonyFretDist",
                    "type": HarmonyFretDist,
                },
                {
                    "name": "harmonyPlay",
                    "type": HarmonyPlay,
                },
                {
                    "name": "harmonyY",
                    "type": HarmonyY,
                },
                {
                    "name": "headerAlign",
                    "type": HeaderAlign,
                },
                {
                    "name": "headerFirstPage",
                    "type": HeaderFirstPage,
                },
                {
                    "name": "headerFontBold",
                    "type": HeaderFontBold,
                },
                {
                    "name": "headerFontFace",
                    "type": HeaderFontFace,
                },
                {
                    "name": "headerFontSize",
                    "type": HeaderFontSize,
                },
                {
                    "name": "headerFontStyle",
                    "type": HeaderFontStyle,
                },
                {
                    "name": "headerFramePadding",
                    "type": HeaderFramePadding,
                },
                {
                    "name": "headerFrameWidth",
                    "type": HeaderFrameWidth,
                },
                {
                    "name": "hideEmptyStaves",
                    "type": HideEmptyStaves,
                },
                {
                    "name": "hideInstrumentNameIfOneInstrument",
                    "type": HideInstrumentNameIfOneInstrument,
                },
                {
                    "name": "instrumentChangeAlign",
                    "type": InstrumentChangeAlign,
                },
                {
                    "name": "instrumentChangeFontFace",
                    "type": InstrumentChangeFontFace,
                },
                {
                    "name": "instrumentChangeFontSize",
                    "type": InstrumentChangeFontSize,
                },
                {
                    "name": "instrumentChangeFramePadding",
                    "type": InstrumentChangeFramePadding,
                },
                {
                    "name": "instrumentChangeFrameWidth",
                    "type": InstrumentChangeFrameWidth,
                },
                {
                    "name": "keySigNaturals",
                    "type": KeySigNaturals,
                },
                {
                    "name": "keysigLeftMargin",
                    "type": KeysigLeftMargin,
                },
                {
                    "name": "lastSystemFillLimit",
                    "type": LastSystemFillLimit,
                },
                {
                    "name": "ledgerLineLength",
                    "type": LedgerLineLength,
                },
                {
                    "name": "ledgerLineWidth",
                    "type": LedgerLineWidth,
                },
                {
                    "name": "letRingFontFace",
                    "type": LetRingFontFace,
                },
                {
                    "name": "lhGuitarFingeringFontFace",
                    "type": LhGuitarFingeringFontFace,
                },
                {
                    "name": "lhGuitarFingeringFontSize",
                    "type": LhGuitarFingeringFontSize,
                },
                {
                    "name": "lhGuitarFingeringFramePadding",
                    "type": LhGuitarFingeringFramePadding,
                },
                {
                    "name": "lhGuitarFingeringFrameRound",
                    "type": LhGuitarFingeringFrameRound,
                },
                {
                    "name": "lhGuitarFingeringFrameWidth",
                    "type": LhGuitarFingeringFrameWidth,
                },
                {
                    "name": "longInstrumentAlign",
                    "type": LongInstrumentAlign,
                },
                {
                    "name": "longInstrumentFontFace",
                    "type": LongInstrumentFontFace,
                },
                {
                    "name": "longInstrumentFontSize",
                    "type": LongInstrumentFontSize,
                },
                {
                    "name": "longInstrumentFramePadding",
                    "type": LongInstrumentFramePadding,
                },
                {
                    "name": "longInstrumentFrameWidth",
                    "type": LongInstrumentFrameWidth,
                },
                {
                    "name": "lowerCaseBassNotes",
                    "type": LowerCaseBassNotes,
                },
                {
                    "name": "lowerCaseMinorChords",
                    "type": LowerCaseMinorChords,
                },
                {
                    "name": "lyricistFontFace",
                    "type": LyricistFontFace,
                },
                {
                    "name": "lyricistFontSize",
                    "type": LyricistFontSize,
                },
                {
                    "name": "lyricistFramePadding",
                    "type": LyricistFramePadding,
                },
                {
                    "name": "lyricistFrameRound",
                    "type": LyricistFrameRound,
                },
                {
                    "name": "lyricistFrameWidth",
                    "type": LyricistFrameWidth,
                },
                {
                    "name": "lyricsDashForce",
                    "type": LyricsDashForce,
                },
                {
                    "name": "lyricsDashYposRatio",
                    "type": LyricsDashYposRatio,
                },
                {
                    "name": "lyricsDistance",
                    "type": LyricsDistance,
                },
                {
                    "name": "lyricsEvenFontFace",
                    "type": LyricsEvenFontFace,
                },
                {
                    "name": "lyricsEvenFontSize",
                    "type": LyricsEvenFontSize,
                },
                {
                    "name": "lyricsEvenFramePadding",
                    "type": LyricsEvenFramePadding,
                },
                {
                    "name": "lyricsEvenFrameWidth",
                    "type": LyricsEvenFrameWidth,
                },
                {
                    "name": "lyricsEvenOffset",
                    "type": LyricsEvenOffset,
                },
                {
                    "name": "lyricsLineThickness",
                    "type": LyricsLineThickness,
                },
                {
                    "name": "lyricsMinBottomDistance",
                    "type": LyricsMinBottomDistance,
                },
                {
                    "name": "lyricsMinDistance",
                    "type": LyricsMinDistance,
                },
                {
                    "name": "lyricsOddFontFace",
                    "type": LyricsOddFontFace,
                },
                {
                    "name": "lyricsOddFontSize",
                    "type": LyricsOddFontSize,
                },
                {
                    "name": "lyricsOddFramePadding",
                    "type": LyricsOddFramePadding,
                },
                {
                    "name": "lyricsOddFrameWidth",
                    "type": LyricsOddFrameWidth,
                },
                {
                    "name": "lyricsOddOffset",
                    "type": LyricsOddOffset,
                },
                {
                    "name": "lyricsPosBelow",
                    "type": LyricsPosBelow,
                },
                {
                    "name": "maxChordShiftAbove",
                    "type": MaxChordShiftAbove,
                },
                {
                    "name": "maxChordShiftBelow",
                    "type": MaxChordShiftBelow,
                },
                {
                    "name": "maxFretShiftAbove",
                    "type": MaxFretShiftAbove,
                },
                {
                    "name": "maxFretShiftBelow",
                    "type": MaxFretShiftBelow,
                },
                {
                    "name": "maxHarmonyBarDistance",
                    "type": MaxHarmonyBarDistance,
                },
                {
                    "name": "maxPageFillSpread",
                    "type": MaxPageFillSpread,
                },
                {
                    "name": "maxSystemDistance",
                    "type": MaxSystemDistance,
                },
                {
                    "name": "measureNumberAlign",
                    "type": MeasureNumberAlign,
                },
                {
                    "name": "measureNumberAllStaffs",
                    "type": MeasureNumberAllStaffs,
                },
                {
                    "name": "measureNumberFontFace",
                    "type": MeasureNumberFontFace,
                },
                {
                    "name": "measureNumberFontSize",
                    "type": MeasureNumberFontSize,
                },
                {
                    "name": "measureNumberFontSpatiumDependent",
                    "type": MeasureNumberFontSpatiumDependent,
                },
                {
                    "name": "measureNumberFontStyle",
                    "type": MeasureNumberFontStyle,
                },
                {
                    "name": "measureNumberFramePadding",
                    "type": MeasureNumberFramePadding,
                },
                {
                    "name": "measureNumberFrameWidth",
                    "type": MeasureNumberFrameWidth,
                },
                {
                    "name": "measureNumberHPlacement",
                    "type": MeasureNumberHplacement,
                },
                {
                    "name": "measureNumberInterval",
                    "type": MeasureNumberInterval,
                },
                {
                    "name": "measureNumberOffset",
                    "type": MeasureNumberOffset,
                },
                {
                    "name": "measureNumberPosAbove",
                    "type": MeasureNumberPosAbove,
                },
                {
                    "name": "measureNumberPosBelow",
                    "type": MeasureNumberPosBelow,
                },
                {
                    "name": "measureNumberSystem",
                    "type": MeasureNumberSystem,
                },
                {
                    "name": "measureNumberVPlacement",
                    "type": MeasureNumberVplacement,
                },
                {
                    "name": "measureSpacing",
                    "type": MeasureSpacing,
                },
                {
                    "name": "metronomeFontFace",
                    "type": MetronomeFontFace,
                },
                {
                    "name": "metronomeFontSize",
                    "type": MetronomeFontSize,
                },
                {
                    "name": "metronomeFontStyle",
                    "type": MetronomeFontStyle,
                },
                {
                    "name": "metronomeFramePadding",
                    "type": MetronomeFramePadding,
                },
                {
                    "name": "metronomeFrameWidth",
                    "type": MetronomeFrameWidth,
                },
                {
                    "name": "minEmptyMeasures",
                    "type": MinEmptyMeasures,
                },
                {
                    "name": "minHarmonyDistance",
                    "type": MinHarmonyDistance,
                },
                {
                    "name": "minMMRestWidth",
                    "type": MinMmrestWidth,
                },
                {
                    "name": "minMeasureWidth",
                    "type": MinMeasureWidth,
                },
                {
                    "name": "minNoteDistance",
                    "type": MinNoteDistance,
                },
                {
                    "name": "minSystemDistance",
                    "type": MinSystemDistance,
                },
                {
                    "name": "mmRestNumberPos",
                    "type": MmRestNumberPos,
                },
                {
                    "name": "mmRestRangeBracketType",
                    "type": MmRestRangeBracketType,
                },
                {
                    "name": "mmRestRangeFontSize",
                    "type": MmRestRangeFontSize,
                },
                {
                    "name": "mmRestRangeVPlacement",
                    "type": MmRestRangeVplacement,
                },
                {
                    "name": "mmRestShowMeasureNumberRange",
                    "type": MmRestShowMeasureNumberRange,
                },
                {
                    "name": "musicalSymbolFont",
                    "type": MusicalSymbolFont,
                },
                {
                    "name": "musicalTextFont",
                    "type": MusicalTextFont,
                },
                {
                    "name": "nashvilleNumberFontFace",
                    "type": NashvilleNumberFontFace,
                },
                {
                    "name": "nashvilleNumberFontSize",
                    "type": NashvilleNumberFontSize,
                },
                {
                    "name": "noteBarDistance",
                    "type": NoteBarDistance,
                },
                {
                    "name": "oddFooterC",
                    "type": OddFooterC,
                },
                {
                    "name": "oddFooterL",
                    "type": OddFooterL,
                },
                {
                    "name": "oddFooterR",
                    "type": OddFooterR,
                },
                {
                    "name": "oddHeaderC",
                    "type": OddHeaderC,
                },
                {
                    "name": "oddHeaderL",
                    "type": OddHeaderL,
                },
                {
                    "name": "oddHeaderR",
                    "type": OddHeaderR,
                },
                {
                    "name": "ottavaFontFace",
                    "type": OttavaFontFace,
                },
                {
                    "name": "ottavaFontItalic",
                    "type": OttavaFontItalic,
                },
                {
                    "name": "ottavaFontSize",
                    "type": OttavaFontSize,
                },
                {
                    "name": "ottavaFontStyle",
                    "type": OttavaFontStyle,
                },
                {
                    "name": "ottavaFramePadding",
                    "type": OttavaFramePadding,
                },
                {
                    "name": "ottavaFrameWidth",
                    "type": OttavaFrameWidth,
                },
                {
                    "name": "ottavaHook",
                    "type": OttavaHook,
                },
                {
                    "name": "ottavaHookAbove",
                    "type": OttavaHookAbove,
                },
                {
                    "name": "ottavaHookBelow",
                    "type": OttavaHookBelow,
                },
                {
                    "name": "ottavaLineWidth",
                    "type": OttavaLineWidth,
                },
                {
                    "name": "page-layout",
                    "type": PageLayout,
                },
                {
                    "name": "pageEvenBottomMargin",
                    "type": PageEvenBottomMargin,
                },
                {
                    "name": "pageEvenLeftMargin",
                    "type": PageEvenLeftMargin,
                },
                {
                    "name": "pageEvenTopMargin",
                    "type": PageEvenTopMargin,
                },
                {
                    "name": "pageFillLimit",
                    "type": PageFillLimit,
                },
                {
                    "name": "pageHeight",
                    "type": PageHeight2,
                },
                {
                    "name": "pageNumberOddEven",
                    "type": PageNumberOddEven,
                },
                {
                    "name": "pageOddBottomMargin",
                    "type": PageOddBottomMargin,
                },
                {
                    "name": "pageOddLeftMargin",
                    "type": PageOddLeftMargin,
                },
                {
                    "name": "pageOddTopMargin",
                    "type": PageOddTopMargin,
                },
                {
                    "name": "pagePrintableWidth",
                    "type": PagePrintableWidth,
                },
                {
                    "name": "pageTwosided",
                    "type": PageTwosided,
                },
                {
                    "name": "pageWidth",
                    "type": PageWidth2,
                },
                {
                    "name": "palmMuteFontFace",
                    "type": PalmMuteFontFace,
                },
                {
                    "name": "partInstrumentFontFace",
                    "type": PartInstrumentFontFace,
                },
                {
                    "name": "partInstrumentFontSize",
                    "type": PartInstrumentFontSize,
                },
                {
                    "name": "partInstrumentFramePadding",
                    "type": PartInstrumentFramePadding,
                },
                {
                    "name": "partInstrumentFrameRound",
                    "type": PartInstrumentFrameRound,
                },
                {
                    "name": "partInstrumentFrameWidth",
                    "type": PartInstrumentFrameWidth,
                },
                {
                    "name": "pedalFontFace",
                    "type": PedalFontFace,
                },
                {
                    "name": "pedalFramePadding",
                    "type": PedalFramePadding,
                },
                {
                    "name": "pedalFrameWidth",
                    "type": PedalFrameWidth,
                },
                {
                    "name": "pedalLineWidth",
                    "type": PedalLineWidth,
                },
                {
                    "name": "pedalPosBelow",
                    "type": PedalPosBelow,
                },
                {
                    "name": "pedalY",
                    "type": PedalY,
                },
                {
                    "name": "propertyDistance",
                    "type": PropertyDistance,
                },
                {
                    "name": "propertyDistanceHead",
                    "type": PropertyDistanceHead,
                },
                {
                    "name": "propertyDistanceStem",
                    "type": PropertyDistanceStem,
                },
                {
                    "name": "rehearsalMarkAlign",
                    "type": RehearsalMarkAlign,
                },
                {
                    "name": "rehearsalMarkFontBold",
                    "type": RehearsalMarkFontBold,
                },
                {
                    "name": "rehearsalMarkFontFace",
                    "type": RehearsalMarkFontFace,
                },
                {
                    "name": "rehearsalMarkFontSize",
                    "type": RehearsalMarkFontSize,
                },
                {
                    "name": "rehearsalMarkFramePadding",
                    "type": RehearsalMarkFramePadding,
                },
                {
                    "name": "rehearsalMarkFrameRound",
                    "type": RehearsalMarkFrameRound,
                },
                {
                    "name": "rehearsalMarkFrameWidth",
                    "type": RehearsalMarkFrameWidth,
                },
                {
                    "name": "repeatBarTips",
                    "type": RepeatBarTips,
                },
                {
                    "name": "repeatBarlineDotSeparation",
                    "type": RepeatBarlineDotSeparation,
                },
                {
                    "name": "repeatLeftAlign",
                    "type": RepeatLeftAlign,
                },
                {
                    "name": "repeatLeftFontFace",
                    "type": RepeatLeftFontFace,
                },
                {
                    "name": "repeatLeftFontSize",
                    "type": RepeatLeftFontSize,
                },
                {
                    "name": "repeatLeftFramePadding",
                    "type": RepeatLeftFramePadding,
                },
                {
                    "name": "repeatLeftFrameRound",
                    "type": RepeatLeftFrameRound,
                },
                {
                    "name": "repeatLeftFrameWidth",
                    "type": RepeatLeftFrameWidth,
                },
                {
                    "name": "repeatRightAlign",
                    "type": RepeatRightAlign,
                },
                {
                    "name": "repeatRightFontFace",
                    "type": RepeatRightFontFace,
                },
                {
                    "name": "repeatRightFontSize",
                    "type": RepeatRightFontSize,
                },
                {
                    "name": "repeatRightFramePadding",
                    "type": RepeatRightFramePadding,
                },
                {
                    "name": "repeatRightFrameRound",
                    "type": RepeatRightFrameRound,
                },
                {
                    "name": "repeatRightFrameWidth",
                    "type": RepeatRightFrameWidth,
                },
                {
                    "name": "rhGuitarFingeringFontFace",
                    "type": RhGuitarFingeringFontFace,
                },
                {
                    "name": "rhGuitarFingeringFontSize",
                    "type": RhGuitarFingeringFontSize,
                },
                {
                    "name": "rhGuitarFingeringFontStyle",
                    "type": RhGuitarFingeringFontStyle,
                },
                {
                    "name": "rhGuitarFingeringFramePadding",
                    "type": RhGuitarFingeringFramePadding,
                },
                {
                    "name": "rhGuitarFingeringFrameRound",
                    "type": RhGuitarFingeringFrameRound,
                },
                {
                    "name": "rhGuitarFingeringFrameWidth",
                    "type": RhGuitarFingeringFrameWidth,
                },
                {
                    "name": "sectionPause",
                    "type": SectionPause,
                },
                {
                    "name": "shortInstrumentFontFace",
                    "type": ShortInstrumentFontFace,
                },
                {
                    "name": "shortInstrumentFontSize",
                    "type": ShortInstrumentFontSize,
                },
                {
                    "name": "shortInstrumentFramePadding",
                    "type": ShortInstrumentFramePadding,
                },
                {
                    "name": "shortInstrumentFrameWidth",
                    "type": ShortInstrumentFrameWidth,
                },
                {
                    "name": "shortStemProgression",
                    "type": ShortStemProgression,
                },
                {
                    "name": "shortenStem",
                    "type": ShortenStem,
                },
                {
                    "name": "shortestStem",
                    "type": ShortestStem,
                },
                {
                    "name": "showFooter",
                    "type": ShowFooter,
                },
                {
                    "name": "showHeader",
                    "type": ShowHeader,
                },
                {
                    "name": "showMeasureNumber",
                    "type": ShowMeasureNumber,
                },
                {
                    "name": "showMeasureNumberOne",
                    "type": ShowMeasureNumberOne,
                },
                {
                    "name": "showPageNumber",
                    "type": ShowPageNumber,
                },
                {
                    "name": "showPageNumberOne",
                    "type": ShowPageNumberOne,
                },
                {
                    "name": "slurEndWidth",
                    "type": SlurEndWidth,
                },
                {
                    "name": "slurGateTime",
                    "type": SlurGateTime,
                },
                {
                    "name": "slurMidWidth",
                    "type": SlurMidWidth,
                },
                {
                    "name": "smallClefMag",
                    "type": SmallClefMag,
                },
                {
                    "name": "smallNoteMag",
                    "type": SmallNoteMag,
                },
                {
                    "name": "smallStaffMag",
                    "type": SmallStaffMag,
                },
                {
                    "name": "staccatoGateTime",
                    "type": StaccatoGateTime,
                },
                {
                    "name": "staffAlign",
                    "type": StaffAlign,
                },
                {
                    "name": "staffDistance",
                    "type": StaffDistance2,
                },
                {
                    "name": "staffFontFace",
                    "type": StaffFontFace,
                },
                {
                    "name": "staffFontItalic",
                    "type": StaffFontItalic,
                },
                {
                    "name": "staffFontSize",
                    "type": StaffFontSize,
                },
                {
                    "name": "staffFramePadding",
                    "type": StaffFramePadding,
                },
                {
                    "name": "staffFrameRound",
                    "type": StaffFrameRound,
                },
                {
                    "name": "staffFrameWidth",
                    "type": StaffFrameWidth,
                },
                {
                    "name": "staffLineWidth",
                    "type": StaffLineWidth,
                },
                {
                    "name": "staffLowerBorder",
                    "type": StaffLowerBorder,
                },
                {
                    "name": "staffOffset",
                    "type": StaffOffset,
                },
                {
                    "name": "staffPlacement",
                    "type": StaffPlacement,
                },
                {
                    "name": "staffPosAbove",
                    "type": StaffPosAbove,
                },
                {
                    "name": "staffPosBelow",
                    "type": StaffPosBelow,
                },
                {
                    "name": "staffTextMinDistance",
                    "type": StaffTextMinDistance,
                },
                {
                    "name": "staffTextPosAbove",
                    "type": StaffTextPosAbove,
                },
                {
                    "name": "staffUpperBorder",
                    "type": StaffUpperBorder,
                },
                {
                    "name": "startBarlineMultiple",
                    "type": StartBarlineMultiple,
                },
                {
                    "name": "startBarlineSingle",
                    "type": StartBarlineSingle,
                },
                {
                    "name": "stemDir1",
                    "type": StemDir1,
                },
                {
                    "name": "stemDir2",
                    "type": StemDir2,
                },
                {
                    "name": "stemDir3",
                    "type": StemDir3,
                },
                {
                    "name": "stemDir4",
                    "type": StemDir4,
                },
                {
                    "name": "stemWidth",
                    "type": StemWidth,
                },
                {
                    "name": "stickingFontFace",
                    "type": StickingFontFace,
                },
                {
                    "name": "stringNumberFontFace",
                    "type": StringNumberFontFace,
                },
                {
                    "name": "stringNumberFontSize",
                    "type": StringNumberFontSize,
                },
                {
                    "name": "stringNumberOffset",
                    "type": StringNumberOffset,
                },
                {
                    "name": "subTitleFontFace",
                    "type": SubTitleFontFace,
                },
                {
                    "name": "subTitleFontSize",
                    "type": SubTitleFontSize,
                },
                {
                    "name": "subTitleFontSpatiumDependent",
                    "type": SubTitleFontSpatiumDependent,
                },
                {
                    "name": "subTitleFramePadding",
                    "type": SubTitleFramePadding,
                },
                {
                    "name": "subTitleFrameRound",
                    "type": SubTitleFrameRound,
                },
                {
                    "name": "subTitleFrameWidth",
                    "type": SubTitleFrameWidth,
                },
                {
                    "name": "swingRatio",
                    "type": SwingRatio,
                },
                {
                    "name": "swingUnit",
                    "type": SwingUnit,
                },
                {
                    "name": "systemAlign",
                    "type": SystemAlign,
                },
                {
                    "name": "systemDistance",
                    "type": SystemDistance2,
                },
                {
                    "name": "systemFontFace",
                    "type": SystemFontFace,
                },
                {
                    "name": "systemFontSize",
                    "type": SystemFontSize,
                },
                {
                    "name": "systemFrameDistance",
                    "type": SystemFrameDistance,
                },
                {
                    "name": "systemFramePadding",
                    "type": SystemFramePadding,
                },
                {
                    "name": "systemFrameRound",
                    "type": SystemFrameRound,
                },
                {
                    "name": "systemFrameWidth",
                    "type": SystemFrameWidth,
                },
                {
                    "name": "systemOffset",
                    "type": SystemOffset,
                },
                {
                    "name": "tempoFontBold",
                    "type": TempoFontBold,
                },
                {
                    "name": "tempoFontFace",
                    "type": TempoFontFace,
                },
                {
                    "name": "tempoFontSize",
                    "type": TempoFontSize,
                },
                {
                    "name": "tempoFontStyle",
                    "type": TempoFontStyle,
                },
                {
                    "name": "tempoFramePadding",
                    "type": TempoFramePadding,
                },
                {
                    "name": "tempoFrameRound",
                    "type": TempoFrameRound,
                },
                {
                    "name": "tempoFrameWidth",
                    "type": TempoFrameWidth,
                },
                {
                    "name": "tempoPosAbove",
                    "type": TempoPosAbove,
                },
                {
                    "name": "textLineFontFace",
                    "type": TextLineFontFace,
                },
                {
                    "name": "textLineFontSize",
                    "type": TextLineFontSize,
                },
                {
                    "name": "textLineFramePadding",
                    "type": TextLineFramePadding,
                },
                {
                    "name": "textLineFrameWidth",
                    "type": TextLineFrameWidth,
                },
                {
                    "name": "textLineTextAlign",
                    "type": TextLineTextAlign,
                },
                {
                    "name": "timesigLeftMargin",
                    "type": TimesigLeftMargin,
                },
                {
                    "name": "titleFontFace",
                    "type": TitleFontFace,
                },
                {
                    "name": "titleFontSize",
                    "type": TitleFontSize,
                },
                {
                    "name": "titleFontSpatiumDependent",
                    "type": TitleFontSpatiumDependent,
                },
                {
                    "name": "titleFontStyle",
                    "type": TitleFontStyle,
                },
                {
                    "name": "titleFramePadding",
                    "type": TitleFramePadding,
                },
                {
                    "name": "titleFrameRound",
                    "type": TitleFrameRound,
                },
                {
                    "name": "titleFrameWidth",
                    "type": TitleFrameWidth,
                },
                {
                    "name": "translatorAlign",
                    "type": TranslatorAlign,
                },
                {
                    "name": "translatorFontFace",
                    "type": TranslatorFontFace,
                },
                {
                    "name": "translatorFontSize",
                    "type": TranslatorFontSize,
                },
                {
                    "name": "translatorFramePadding",
                    "type": TranslatorFramePadding,
                },
                {
                    "name": "translatorFrameWidth",
                    "type": TranslatorFrameWidth,
                },
                {
                    "name": "trillPosAbove",
                    "type": TrillPosAbove,
                },
                {
                    "name": "tupletBracketHookHeight",
                    "type": TupletBracketHookHeight,
                },
                {
                    "name": "tupletBracketWidth",
                    "type": TupletBracketWidth,
                },
                {
                    "name": "tupletFontFace",
                    "type": TupletFontFace,
                },
                {
                    "name": "tupletFontSize",
                    "type": TupletFontSize,
                },
                {
                    "name": "tupletFontStyle",
                    "type": TupletFontStyle,
                },
                {
                    "name": "tupletFramePadding",
                    "type": TupletFramePadding,
                },
                {
                    "name": "tupletFrameWidth",
                    "type": TupletFrameWidth,
                },
                {
                    "name": "tupletNoteLeftDistance",
                    "type": TupletNoteLeftDistance,
                },
                {
                    "name": "tupletOufOfStaff",
                    "type": TupletOufOfStaff,
                },
                {
                    "name": "tupletStemLeftDistance",
                    "type": TupletStemLeftDistance,
                },
                {
                    "name": "tupletVHeadDistance",
                    "type": TupletVheadDistance,
                },
                {
                    "name": "tupletVStemDistance",
                    "type": TupletVstemDistance,
                },
                {
                    "name": "useFrenchNoteNames",
                    "type": UseFrenchNoteNames,
                },
                {
                    "name": "useFullGermanNoteNames",
                    "type": UseFullGermanNoteNames,
                },
                {
                    "name": "useGermanNoteNames",
                    "type": UseGermanNoteNames,
                },
                {
                    "name": "usePre_3_6_defaults",
                    "type": UsePre36Defaults,
                },
                {
                    "name": "useSolfeggioNoteNames",
                    "type": UseSolfeggioNoteNames,
                },
                {
                    "name": "useStandardNoteNames",
                    "type": UseStandardNoteNames,
                },
                {
                    "name": "user10FontFace",
                    "type": User10FontFace,
                },
                {
                    "name": "user11FontFace",
                    "type": User11FontFace,
                },
                {
                    "name": "user12FontFace",
                    "type": User12FontFace,
                },
                {
                    "name": "user1Align",
                    "type": User1Align,
                },
                {
                    "name": "user1FontBold",
                    "type": User1FontBold,
                },
                {
                    "name": "user1FontFace",
                    "type": User1FontFace,
                },
                {
                    "name": "user1FontSize",
                    "type": User1FontSize,
                },
                {
                    "name": "user1FontSpatiumDependent",
                    "type": User1FontSpatiumDependent,
                },
                {
                    "name": "user1FramePadding",
                    "type": User1FramePadding,
                },
                {
                    "name": "user1FrameWidth",
                    "type": User1FrameWidth,
                },
                {
                    "name": "user1Name",
                    "type": User1Name,
                },
                {
                    "name": "user2Align",
                    "type": User2Align,
                },
                {
                    "name": "user2FontFace",
                    "type": User2FontFace,
                },
                {
                    "name": "user2FontSize",
                    "type": User2FontSize,
                },
                {
                    "name": "user2FontSpatiumDependent",
                    "type": User2FontSpatiumDependent,
                },
                {
                    "name": "user2FontStyle",
                    "type": User2FontStyle,
                },
                {
                    "name": "user2FramePadding",
                    "type": User2FramePadding,
                },
                {
                    "name": "user2FrameWidth",
                    "type": User2FrameWidth,
                },
                {
                    "name": "user2Name",
                    "type": User2Name,
                },
                {
                    "name": "user3Align",
                    "type": User3Align,
                },
                {
                    "name": "user3FontFace",
                    "type": User3FontFace,
                },
                {
                    "name": "user3FontSize",
                    "type": User3FontSize,
                },
                {
                    "name": "user3FontSpatiumDependent",
                    "type": User3FontSpatiumDependent,
                },
                {
                    "name": "user3FramePadding",
                    "type": User3FramePadding,
                },
                {
                    "name": "user3FrameWidth",
                    "type": User3FrameWidth,
                },
                {
                    "name": "user3Name",
                    "type": User3Name,
                },
                {
                    "name": "user4Align",
                    "type": User4Align,
                },
                {
                    "name": "user4FontFace",
                    "type": User4FontFace,
                },
                {
                    "name": "user4FontSize",
                    "type": User4FontSize,
                },
                {
                    "name": "user4FontSpatiumDependent",
                    "type": User4FontSpatiumDependent,
                },
                {
                    "name": "user4FramePadding",
                    "type": User4FramePadding,
                },
                {
                    "name": "user4FrameWidth",
                    "type": User4FrameWidth,
                },
                {
                    "name": "user4Name",
                    "type": User4Name,
                },
                {
                    "name": "user5Align",
                    "type": User5Align,
                },
                {
                    "name": "user5FontFace",
                    "type": User5FontFace,
                },
                {
                    "name": "user5FontSize",
                    "type": User5FontSize,
                },
                {
                    "name": "user5FontSpatiumDependent",
                    "type": User5FontSpatiumDependent,
                },
                {
                    "name": "user5FramePadding",
                    "type": User5FramePadding,
                },
                {
                    "name": "user5FrameWidth",
                    "type": User5FrameWidth,
                },
                {
                    "name": "user5Name",
                    "type": User5Name,
                },
                {
                    "name": "user6Align",
                    "type": User6Align,
                },
                {
                    "name": "user6FontFace",
                    "type": User6FontFace,
                },
                {
                    "name": "user6FontSize",
                    "type": User6FontSize,
                },
                {
                    "name": "user6FontSpatiumDependent",
                    "type": User6FontSpatiumDependent,
                },
                {
                    "name": "user6FontStyle",
                    "type": User6FontStyle,
                },
                {
                    "name": "user6FramePadding",
                    "type": User6FramePadding,
                },
                {
                    "name": "user6FrameWidth",
                    "type": User6FrameWidth,
                },
                {
                    "name": "user6Name",
                    "type": User6Name,
                },
                {
                    "name": "user7Align",
                    "type": User7Align,
                },
                {
                    "name": "user7FontFace",
                    "type": User7FontFace,
                },
                {
                    "name": "user7FontSize",
                    "type": User7FontSize,
                },
                {
                    "name": "user7FontSpatiumDependent",
                    "type": User7FontSpatiumDependent,
                },
                {
                    "name": "user7FontStyle",
                    "type": User7FontStyle,
                },
                {
                    "name": "user7FramePadding",
                    "type": User7FramePadding,
                },
                {
                    "name": "user7FrameWidth",
                    "type": User7FrameWidth,
                },
                {
                    "name": "user7Name",
                    "type": User7Name,
                },
                {
                    "name": "user8FontFace",
                    "type": User8FontFace,
                },
                {
                    "name": "user9FontFace",
                    "type": User9FontFace,
                },
                {
                    "name": "voltaFontBold",
                    "type": VoltaFontBold,
                },
                {
                    "name": "voltaFontFace",
                    "type": VoltaFontFace,
                },
                {
                    "name": "voltaFontSize",
                    "type": VoltaFontSize,
                },
                {
                    "name": "voltaFramePadding",
                    "type": VoltaFramePadding,
                },
                {
                    "name": "voltaFrameWidth",
                    "type": VoltaFrameWidth,
                },
                {
                    "name": "voltaLineWidth",
                    "type": VoltaLineWidth,
                },
                {
                    "name": "voltaPosAbove",
                    "type": VoltaPosAbove,
                },
                {
                    "name": "voltaY",
                    "type": VoltaY,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class InstrumentChange(InstrumentChangeType):
    pass


@dataclass(kw_only=True)
class Note1(NoteType1):
    class Meta:
        name = "Note"


@dataclass(kw_only=True)
class Style1(StyleType1):
    class Meta:
        name = "Style"


@dataclass(kw_only=True)
class ChordType1:
    class Meta:
        name = "ChordType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Arpeggio",
                    "type": Arpeggio,
                },
                {
                    "name": "Articulation",
                    "type": Articulation1,
                },
                {
                    "name": "Beam",
                    "type": Beam1,
                },
                {
                    "name": "BeamMode",
                    "type": BeamMode,
                },
                {
                    "name": "ChordLine",
                    "type": ChordLine1,
                },
                {
                    "name": "Lyrics",
                    "type": Lyrics,
                },
                {
                    "name": "Note",
                    "type": Note1,
                },
                {
                    "name": "Slur",
                    "type": Slur1,
                },
                {
                    "name": "Spanner",
                    "type": Spanner,
                },
                {
                    "name": "Stem",
                    "type": Stem1,
                },
                {
                    "name": "StemDirection",
                    "type": StemDirection,
                },
                {
                    "name": "Tremolo",
                    "type": Tremolo1,
                },
                {
                    "name": "Tuplet",
                    "type": Tuplet1,
                },
                {
                    "name": "acciaccatura",
                    "type": Acciaccatura,
                },
                {
                    "name": "appoggiatura",
                    "type": Appoggiatura,
                },
                {
                    "name": "dots",
                    "type": Dots,
                },
                {
                    "name": "duration",
                    "type": Duration,
                },
                {
                    "name": "durationType",
                    "type": DurationType1,
                },
                {
                    "name": "grace16",
                    "type": Grace16,
                },
                {
                    "name": "grace16after",
                    "type": Grace16After,
                },
                {
                    "name": "grace32",
                    "type": Grace32,
                },
                {
                    "name": "grace32after",
                    "type": Grace32After,
                },
                {
                    "name": "grace4",
                    "type": Grace4,
                },
                {
                    "name": "grace8after",
                    "type": Grace8After,
                },
                {
                    "name": "lid",
                    "type": Lid,
                },
                {
                    "name": "linked",
                    "type": Linked,
                },
                {
                    "name": "linkedMain",
                    "type": LinkedMain,
                },
                {
                    "name": "move",
                    "type": Move,
                },
                {
                    "name": "noStem",
                    "type": NoStem,
                },
                {
                    "name": "offset",
                    "type": Offset,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "staffMove",
                    "type": StaffMove,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "ticklen",
                    "type": Ticklen,
                },
                {
                    "name": "track",
                    "type": Track3,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Chord1(ChordType1):
    class Meta:
        name = "Chord"


@dataclass(kw_only=True)
class VoiceType:
    class Meta:
        name = "voiceType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Ambitus",
                    "type": Ambitus,
                },
                {
                    "name": "BarLine",
                    "type": BarLine1,
                },
                {
                    "name": "Beam",
                    "type": Beam1,
                },
                {
                    "name": "Breath",
                    "type": Breath,
                },
                {
                    "name": "Chord",
                    "type": Chord1,
                },
                {
                    "name": "Clef",
                    "type": Clef1,
                },
                {
                    "name": "Dynamic",
                    "type": Dynamic,
                },
                {
                    "name": "Fermata",
                    "type": Fermata1,
                },
                {
                    "name": "FiguredBass",
                    "type": FiguredBass1,
                },
                {
                    "name": "FretDiagram",
                    "type": FretDiagram1,
                },
                {
                    "name": "Harmony",
                    "type": Harmony1,
                },
                {
                    "name": "InstrumentChange",
                    "type": InstrumentChange,
                },
                {
                    "name": "KeySig",
                    "type": KeySig1,
                },
                {
                    "name": "RehearsalMark",
                    "type": RehearsalMark,
                },
                {
                    "name": "RepeatMeasure",
                    "type": RepeatMeasure,
                },
                {
                    "name": "Rest",
                    "type": Rest1,
                },
                {
                    "name": "Segment",
                    "type": Segment,
                },
                {
                    "name": "Spanner",
                    "type": Spanner,
                },
                {
                    "name": "StaffText",
                    "type": StaffText,
                },
                {
                    "name": "Sticking",
                    "type": Sticking,
                },
                {
                    "name": "Symbol",
                    "type": Symbol1,
                },
                {
                    "name": "SystemText",
                    "type": SystemText,
                },
                {
                    "name": "Tempo",
                    "type": Tempo1,
                },
                {
                    "name": "TimeSig",
                    "type": TimeSig1,
                },
                {
                    "name": "TremoloBar",
                    "type": TremoloBar,
                },
                {
                    "name": "Tuplet",
                    "type": Tuplet1,
                },
                {
                    "name": "endTuplet",
                    "type": EndTuplet,
                },
                {
                    "name": "location",
                    "type": Location,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Voice(VoiceType):
    class Meta:
        name = "voice"


@dataclass(kw_only=True)
class MeasureType1:
    class Meta:
        name = "MeasureType"

    len: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    number: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Ambitus",
                    "type": Ambitus,
                },
                {
                    "name": "BarLine",
                    "type": BarLine1,
                },
                {
                    "name": "Beam",
                    "type": Beam1,
                },
                {
                    "name": "Breath",
                    "type": Breath,
                },
                {
                    "name": "Chord",
                    "type": Chord1,
                },
                {
                    "name": "Clef",
                    "type": Clef1,
                },
                {
                    "name": "Dynamic",
                    "type": Dynamic,
                },
                {
                    "name": "FretDiagram",
                    "type": FretDiagram1,
                },
                {
                    "name": "HairPin",
                    "type": HairPin,
                },
                {
                    "name": "Harmony",
                    "type": Harmony1,
                },
                {
                    "name": "Jump",
                    "type": Jump,
                },
                {
                    "name": "KeySig",
                    "type": KeySig1,
                },
                {
                    "name": "LayoutBreak",
                    "type": LayoutBreak,
                },
                {
                    "name": "Lyrics",
                    "type": Lyrics,
                },
                {
                    "name": "Marker",
                    "type": Marker1,
                },
                {
                    "name": "MeasureNumber",
                    "type": MeasureNumber,
                },
                {
                    "name": "Ottava",
                    "type": Ottava,
                },
                {
                    "name": "Pedal",
                    "type": Pedal1,
                },
                {
                    "name": "RehearsalMark",
                    "type": RehearsalMark,
                },
                {
                    "name": "RepeatMeasure",
                    "type": RepeatMeasure,
                },
                {
                    "name": "Rest",
                    "type": Rest1,
                },
                {
                    "name": "Slur",
                    "type": Slur1,
                },
                {
                    "name": "StaffText",
                    "type": StaffText,
                },
                {
                    "name": "StaffTypeChange",
                    "type": ForwardRef("StaffTypeChange"),
                },
                {
                    "name": "Symbol",
                    "type": Symbol1,
                },
                {
                    "name": "Tempo",
                    "type": Tempo1,
                },
                {
                    "name": "Text",
                    "type": Text1,
                },
                {
                    "name": "TextLine",
                    "type": TextLine,
                },
                {
                    "name": "TimeSig",
                    "type": TimeSig1,
                },
                {
                    "name": "TremoloBar",
                    "type": TremoloBar,
                },
                {
                    "name": "Trill",
                    "type": Trill1,
                },
                {
                    "name": "Tuplet",
                    "type": Tuplet1,
                },
                {
                    "name": "Volta",
                    "type": Volta1,
                },
                {
                    "name": "breakMultiMeasureRest",
                    "type": BreakMultiMeasureRest,
                },
                {
                    "name": "endRepeat",
                    "type": EndRepeat,
                },
                {
                    "name": "endSpanner",
                    "type": EndSpanner,
                },
                {
                    "name": "irregular",
                    "type": Irregular,
                },
                {
                    "name": "move",
                    "type": Move,
                },
                {
                    "name": "multiMeasureRest",
                    "type": MultiMeasureRest,
                },
                {
                    "name": "noOffset",
                    "type": NoOffset,
                },
                {
                    "name": "slashStyle",
                    "type": SlashStyle,
                },
                {
                    "name": "startRepeat",
                    "type": StartRepeat,
                },
                {
                    "name": "stemless",
                    "type": Stemless,
                },
                {
                    "name": "stretch",
                    "type": Stretch,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "voice",
                    "type": Voice,
                },
                {
                    "name": "vspacerDown",
                    "type": VspacerDown,
                },
                {
                    "name": "vspacerFixed",
                    "type": VspacerFixed,
                },
                {
                    "name": "vspacerUp",
                    "type": VspacerUp,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Measure1(MeasureType1):
    class Meta:
        name = "Measure"


@dataclass(kw_only=True)
class StaffType1:
    class Meta:
        name = "StaffType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "HBox",
                    "type": Hbox,
                },
                {
                    "name": "Measure",
                    "type": Measure1,
                },
                {
                    "name": "StaffType",
                    "type": StaffType2,
                },
                {
                    "name": "TBox",
                    "type": Tbox,
                },
                {
                    "name": "VBox",
                    "type": Vbox,
                },
                {
                    "name": "barLineSpan",
                    "type": BarLineSpan1,
                },
                {
                    "name": "barLineSpanFrom",
                    "type": BarLineSpanFrom,
                },
                {
                    "name": "barLineSpanTo",
                    "type": BarLineSpanTo,
                },
                {
                    "name": "bracket",
                    "type": Bracket,
                },
                {
                    "name": "cleflist",
                    "type": Cleflist,
                },
                {
                    "name": "cutaway",
                    "type": Cutaway,
                },
                {
                    "name": "defaultClef",
                    "type": DefaultClef,
                },
                {
                    "name": "defaultConcertClef",
                    "type": DefaultConcertClef,
                },
                {
                    "name": "defaultTransposingClef",
                    "type": DefaultTransposingClef,
                },
                {
                    "name": "distOffset",
                    "type": DistOffset,
                },
                {
                    "name": "hideSystemBarLine",
                    "type": HideSystemBarLine,
                },
                {
                    "name": "hideWhenEmpty",
                    "type": HideWhenEmpty,
                },
                {
                    "name": "invisible",
                    "type": Invisible,
                },
                {
                    "name": "keylist",
                    "type": Keylist,
                },
                {
                    "name": "lines",
                    "type": Lines,
                },
                {
                    "name": "linkedTo",
                    "type": LinkedTo,
                },
                {
                    "name": "mag",
                    "type": Mag2,
                },
                {
                    "name": "mergeMatchingRests",
                    "type": MergeMatchingRests,
                },
                {
                    "name": "playbackVoice2",
                    "type": PlaybackVoice2,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "tick",
                    "type": Tick,
                },
                {
                    "name": "type",
                    "type": Type,
                },
                {
                    "name": "useTablature",
                    "type": UseTablature,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class StaffTypeChangeType:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "StaffType",
                    "type": StaffType1,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Staff1(StaffType1):
    class Meta:
        name = "Staff"


@dataclass(kw_only=True)
class PartType1:
    class Meta:
        name = "PartType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Instrument",
                    "type": Instrument1,
                },
                {
                    "name": "Staff",
                    "type": Staff1,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "preferSharpFlat",
                    "type": PreferSharpFlat,
                },
                {
                    "name": "shortName",
                    "type": ShortName2,
                },
                {
                    "name": "show",
                    "type": Show,
                },
                {
                    "name": "soloist",
                    "type": Soloist,
                },
                {
                    "name": "trackName",
                    "type": TrackName2,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class StaffTypeChange(StaffTypeChangeType):
    pass


@dataclass(kw_only=True)
class Part1(PartType1):
    class Meta:
        name = "Part"


@dataclass(kw_only=True)
class ScoreType1:
    class Meta:
        name = "ScoreType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Division",
                    "type": Division1,
                },
                {
                    "name": "LayerTag",
                    "type": LayerTag,
                },
                {
                    "name": "Order",
                    "type": Order,
                },
                {
                    "name": "PageList",
                    "type": PageList,
                },
                {
                    "name": "Part",
                    "type": Part1,
                },
                {
                    "name": "Score",
                    "type": ForwardRef("Score1"),
                },
                {
                    "name": "Spatium",
                    "type": Spatium1,
                },
                {
                    "name": "Staff",
                    "type": Staff1,
                },
                {
                    "name": "StaffType",
                    "type": StaffType1,
                },
                {
                    "name": "Style",
                    "type": Style1,
                },
                {
                    "name": "Synthesizer",
                    "type": Synthesizer,
                },
                {
                    "name": "SyntiSettings",
                    "type": SyntiSettings,
                },
                {
                    "name": "Tracklist",
                    "type": Tracklist,
                },
                {
                    "name": "currentLayer",
                    "type": CurrentLayer,
                },
                {
                    "name": "cursorTrack",
                    "type": CursorTrack,
                },
                {
                    "name": "layoutMode",
                    "type": LayoutMode,
                },
                {
                    "name": "metaTag",
                    "type": MetaTag,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "page-layout",
                    "type": PageLayout,
                },
                {
                    "name": "showFrames",
                    "type": ShowFrames,
                },
                {
                    "name": "showInvisible",
                    "type": ShowInvisible,
                },
                {
                    "name": "showMargins",
                    "type": ShowMargins,
                },
                {
                    "name": "showUnprintable",
                    "type": ShowUnprintable,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Score1(ScoreType1):
    class Meta:
        name = "Score"


@dataclass(kw_only=True)
class MuseScoreType:
    class Meta:
        name = "museScoreType"

    version: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Division",
                    "type": Division1,
                },
                {
                    "name": "HairPin",
                    "type": HairPin,
                },
                {
                    "name": "Mag",
                    "type": Mag1,
                },
                {
                    "name": "Part",
                    "type": Part1,
                },
                {
                    "name": "Pedal",
                    "type": Pedal1,
                },
                {
                    "name": "Score",
                    "type": Score1,
                },
                {
                    "name": "Slur",
                    "type": Slur1,
                },
                {
                    "name": "Spatium",
                    "type": Spatium1,
                },
                {
                    "name": "Staff",
                    "type": Staff1,
                },
                {
                    "name": "Style",
                    "type": Style1,
                },
                {
                    "name": "TextLine",
                    "type": TextLine,
                },
                {
                    "name": "TextStyle",
                    "type": TextStyle,
                },
                {
                    "name": "Volta",
                    "type": Volta1,
                },
                {
                    "name": "copyright",
                    "type": Copyright,
                },
                {
                    "name": "cursorTrack",
                    "type": CursorTrack,
                },
                {
                    "name": "movement-title",
                    "type": MovementTitle1,
                },
                {
                    "name": "page-layout",
                    "type": PageLayout,
                },
                {
                    "name": "programRevision",
                    "type": ProgramRevision,
                },
                {
                    "name": "programVersion",
                    "type": ProgramVersion,
                },
                {
                    "name": "showFrames",
                    "type": ShowFrames,
                },
                {
                    "name": "showInvisible",
                    "type": ShowInvisible,
                },
                {
                    "name": "siglist",
                    "type": Siglist,
                },
                {
                    "name": "tempolist",
                    "type": Tempolist,
                },
                {
                    "name": "xoff",
                    "type": Xoff,
                },
                {
                    "name": "yoff",
                    "type": Yoff,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class MuseScore(MuseScoreType):
    class Meta:
        name = "museScore"
