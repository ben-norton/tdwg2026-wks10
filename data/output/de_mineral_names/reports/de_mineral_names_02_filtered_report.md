# de_mineral_names_02_filtered filter report
> 2026-09-29 17:09:58

## Provenance
- Script: `src/transform/filter_by_exclusion_list.py`
- Command: `python src/transform/filter_by_exclusion_list.py --exclusion-list de_mineral_names_exclusion_list.csv --input data/output/de_mineral_names/de_mineral_names_01.csv`
- Specification: `docs/transformations/de_mineral_names_transformations.md`
- Input: `data/output/de_mineral_names/de_mineral_names_01.csv`
- Exclusion list: `src/config/de_mineral_names_exclusion_list.csv` (32 values)
- Single exclusions: `data/output/de_mineral_names/single_exclusions.csv` (3 values)
- Output: `data/output/de_mineral_names/de_mineral_names_02_filtered.csv`
- Time elapsed: 0.020 s
- Python 3.14.4, pandas 3.0.6

## Description
Removed rows whose `Mineral_Summary` value, trimmed, exactly matches a full-value exclusion or a value in single_exclusions.csv. Then deleted each substring exclusion from the remaining values, in list order, and dropped rows left empty. Finally dropped duplicate values (case-insensitive, first occurrence kept). No other change is made to values.

## Statistics
| | input | output |
|---|---:|---:|
| Records | 2190 | 2158 |
| Columns | 1 | 1 |
| Unique values | 2190 | 2158 |
| Empty values | 0 | 0 |
| Duplicate values | 0 | 0 |

- Records removed: 32
- Records removed by single exclusions only: 0
- Exclusion values with no match in the input: 0
- Values changed by substring exclusions: 0
- Records dropped because substring exclusions left them empty: 0
- Duplicate records dropped after exclusion: 0

## Removed values
- 1M
- 2M
- 2M1
- 2M2
- allgemein
- diskred
- feinkristallin
- Fenster- u Zepter-
- GALIANT Gadolinium Gallium Granat
- Gemenge
- Mineral nicht bestimmt
- Mineralgemenge
- Mineralgruppe
- Mischkristall
- Neotyp
- Noch abklären
- ohne Namen
- organisches Mineral
- Polytyp 2H
- Polytyp 3R
- Polytyp unbestimmt
- Prov
- s Objektbem
- s Objektbemerkung
- Sb
- sekundäres Uranmineral
- sl
- synth
- unbestimmt
- undef Eisenhydroxid
- undefiniert
- ungen def Mn-Hydr
