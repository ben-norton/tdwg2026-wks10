# de_mineral_names transformation report
> 2026-09-29 08:13:06

## Provenance
- Script: `src/transform/de_mineral_names_dedupe.py`
- Command: `python src/transform/de_mineral_names_dedupe.py`
- Specification: `docs/transformations/de_mineral_names_transformations.md`
- Input: `data/output/de_mineral_names/de_mineral_names_00.csv`
- Output: `data/output/de_mineral_names/de_mineral_names_01.csv`
- Time elapsed: 0.024 s
- Python 3.14.4, pandas 3.0.6

## Description
Trimmed whitespace, removed empty values and case-insensitive duplicate mineral names (first occurrence kept), and sorted the names alphabetically ignoring case and diacritics.

## Statistics
| | input | output |
|---|---:|---:|
| Records | 2191 | 2190 |
| Columns | 1 | 1 |
| Unique values (exact) | 2191 | 2190 |
| Unique values (case-insensitive) | 2190 | 2190 |
| Empty values | 0 | 0 |

- Records removed: 1 (0 empty, 1 duplicate)

## Duplicates removed
| removed | kept |
|---|---|
| Unbestimmt | unbestimmt |
