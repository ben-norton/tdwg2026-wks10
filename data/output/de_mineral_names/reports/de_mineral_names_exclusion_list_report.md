# de_mineral_names_exclusion_list build report
> 2026-09-29 17:09:18

## Provenance
- Script: `src/build/build_de_mineral_names_exclusion_list.py`
- Command: `python src/build/build_de_mineral_names_exclusion_list.py --source data/output/de_mineral_names/de_mineral_names_01.csv --exclusion-list de_mineral_names_exclusion_list.csv`
- Specifications: `docs/specifications/exclusion_list_specification.md`, `docs/specifications/mineral_names_exclusion_list_specification.md`
- Input: `data/output/de_mineral_names/de_mineral_names_01.csv` (column `Mineral_Summary`)
- Single exclusions: `data/output/de_mineral_names/single_exclusions.csv` (3 values)
- Output: `src/config/de_mineral_names_exclusion_list.csv`
- Time elapsed: 0.026 s
- Python 3.14.4, pandas 3.0.6

## Description
Tested every distinct trimmed value against the specification's rules. A value is listed only if the whole value matches a rule; values that contain a name plus a qualifier are kept. Values in single_exclusions.csv are added verbatim.

## Statistics
| | count |
|---|---:|
| Input: records | 2190 |
| Input: columns | 1 |
| Input: distinct non-empty values | 2190 |
| Input: empty values (not listed; not a value) | 0 |
| Input: distinct values with an uncertainty qualifier | 0 |
| Output: full-value exclusions | 32 |
| Output: substring exclusions | 0 |
| Output: exclusion values matched after stripping uncertainty | 0 |
| Output: values added from single_exclusions.csv | 3 |
| single_exclusions.csv values a rule already lists | 0 |
| single_exclusions.csv values not in the input | 0 |
| Input records those values cover | 32 |

| category | values |
|---|---:|
| annotation | 14 |
| polytype designation | 7 |
| qualifier | 7 |
| single exclusion | 3 |
| acronym | 1 |

## Uncertainty qualifiers stripped before matching
`\(\s*\?+\s*\)|\?+|(?<!\w)fraglich(?!\w)|(?<!\w)vermutlich(?!\w)|(?<!\w)wahrscheinlich(?!\w)|(?<!\w)möglicherweise(?!\w)|(?<!\w)evtl\.?(?!\w)|(?<!\w)cf\.(?!\w)|(?<!\w)aff\.(?!\w)|(?<!\w)prob\.(?!\w)`

## Full-value exclusions
| Mineral_Summary | category | meaning |
|---|---|---|
| 1M | polytype designation | polytype symbol 1M |
| 2M | polytype designation | polytype symbol 2M |
| 2M1 | polytype designation | polytype symbol 2M1 |
| 2M2 | polytype designation | polytype symbol 2M2 |
| allgemein | qualifier | general / unspecified |
| diskred | qualifier | discredited |
| feinkristallin | qualifier | fine- / coarse-crystalline (texture) |
| Fenster- u Zepter- | qualifier | window and sceptre (crystal habit) |
| GALIANT Gadolinium Gallium Granat | single exclusion | listed in single_exclusions.csv |
| Gemenge | annotation | mixture |
| Mineral nicht bestimmt | annotation | mineral not determined |
| Mineralgemenge | annotation | mixture |
| Mineralgruppe | annotation | mineral group |
| Mischkristall | annotation | solid solution / mixed crystal |
| Neotyp | qualifier | type status |
| Noch abklären | annotation | still to be clarified |
| ohne Namen | annotation | without name |
| organisches Mineral | annotation | organic mineral (generic description) |
| Polytyp 2H | polytype designation | polytype 2H |
| Polytyp 3R | polytype designation | polytype 3R |
| Polytyp unbestimmt | polytype designation | polytype undetermined |
| Prov | annotation | abbreviation, probably provisional or provenance |
| s Objektbem | annotation | see object remark |
| s Objektbemerkung | annotation | see object remark |
| Sb | acronym | chemical symbol Sb |
| sekundäres Uranmineral | annotation | sekundäres Uran mineral (generic description) |
| sl | qualifier | sensu lato / sensu stricto (abbreviation) |
| synth | qualifier | synthetic |
| unbestimmt | annotation | undetermined / undefined / unknown |
| undef Eisenhydroxid | single exclusion | listed in single_exclusions.csv |
| undefiniert | annotation | undetermined / undefined / unknown |
| ungen def Mn-Hydr | single exclusion | listed in single_exclusions.csv |
