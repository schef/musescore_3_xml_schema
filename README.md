# MuseScore 3 XML Schema

Generates a strict XSD for MuseScore 3.6.2 MSCX files from the MuseScore
source tree based on example files. The schema only allows elements and
attributes observed in the examples; unknown structure will fail validation.

## Generate the schema

```bash
python3 generate_schema.py \
  --mscore-root /home/schef/git/MuseScore \
  --examples /home/schef/git/musescore_3_xml_schema/examples_features \
  --output /home/schef/git/musescore_3_xml_schema/musescore-3.6.2.xsd
```

## Extend the schema when validation fails

1. Add the failing `.mscx` file to `/home/schef/git/musescore_3_xml_schema/examples_features`.
2. Regenerate the XSD:

```bash
python3 generate_schema.py \
  --mscore-root /home/schef/git/MuseScore \
  --examples /home/schef/git/musescore_3_xml_schema/examples_features \
  --output /home/schef/git/musescore_3_xml_schema/musescore-3.6.2.xsd
```

3. Re-validate:

```bash
python3 /home/schef/git/musescore_3_xml_schema/validator.py \
  --xsd /home/schef/git/musescore_3_xml_schema/musescore-3.6.2.xsd \
  --dir /home/schef/git/musescore_3_xml_schema/examples_features
```

Notes:
- Only well-formed XML files are used to extend the schema.
- Invalid XML files are skipped during generation and will still fail validation.

## Generate Python classes with xsdata

```bash
xsdata generate \
  --package musescore_schema \
  /home/schef/git/musescore_3_xml_schema/musescore-3.6.2.xsd
```

## Create a new MSCX from scratch (Typer)

```bash
python3 /home/schef/git/musescore_3_xml_schema/musescore_cli.py \
  /home/schef/git/musescore_3_xml_schema/out/new-score.mscx \
  --title "My Score" \
  --composer "Composer Name" \
  --measures 8 \
  --time-sig 4/4 \
  --key-sig 0
```

## Create a new MSCX using xsdata

This CLI uses xsdata-generated dataclasses from `/home/schef/git/musescore_3_xml_schema/musescore_schema`.

```bash
python3 /home/schef/git/musescore_3_xml_schema/musescore_xsdata_cli.py \
  /home/schef/git/musescore_3_xml_schema/out/new-score-xsdata.mscx \
  --title "My Score" \
  --composer "Composer Name" \
  --measures 8 \
  --time-sig 4/4 \
  --key-sig 0
```

## Amazing Grace demo (melody, lyrics, harmony)

```bash
python3 /home/schef/git/musescore_3_xml_schema/musescore_xsdata_cli.py amazing-grace \
  /home/schef/git/musescore_3_xml_schema/out/amazing-grace.mscz
```

## Python library (xsdata)

Example usage (cleaner API):

```python
from musescorelib import new_document, save_mscx, load_mscx

doc = new_document(title="My Song", composer="Me", measures=0)
voice = doc.score.staff(1).measure(1).voice(1)
voice.add_time_sig(4, 4)
voice.add_key_sig(0)
voice.add_harmony("C")
voice.add_note("C4", "quarter", lyric="La")
voice.add_note("D4", "quarter", lyric="la")
voice.add_note("E4", "quarter", lyric="la")
save_mscx(doc, "out/my-song.mscx")

doc2 = load_mscx("out/my-song.mscx")
print(doc2.count_measures())
print(doc2.count_lyrics())

events = doc2.harmony_events()
for event in events:
    print(event.measure_index, event.beat, event.root_tpc, event.text)
```

To create a compressed MSCZ instead, use a `.mscz` output path:

```bash
python3 /home/schef/git/musescore_3_xml_schema/musescore_xsdata_cli.py \
  /home/schef/git/musescore_3_xml_schema/out/new-score-xsdata.mscz \
  --title "My Score" \
  --composer "Composer Name" \
  --measures 8 \
  --time-sig 4/4 \
  --key-sig 0
```

## Validate MSCX files

```bash
python3 /home/schef/git/musescore_3_xml_schema/validator.py \
  --xsd /home/schef/git/musescore_3_xml_schema/musescore-3.6.2.xsd \
  --dir /home/schef/git/musescore_3_xml_schema/examples_features
```

## Update examples manifest and coverage

```bash
python3 /home/schef/git/musescore_3_xml_schema/update_examples_manifest.py
python3 /home/schef/git/musescore_3_xml_schema/report_examples_coverage.py
```
