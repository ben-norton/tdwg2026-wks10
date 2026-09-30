# fr_mineral_names transformation report
> 2026-09-29 15:39:06

## Provenance
- Script: `src/transform/fr_mineral_names_transform.py`
- Command: `python src/transform/fr_mineral_names_transform.py`
- Specification: `docs/transformations/fr_mineral_names_transformations.md` (steps 1-5)
- Input: `data/output/fr_mineral_names/fr_mineral_names_00.csv`
- Output: `data/output/fr_mineral_names/fr_mineral_names_01.csv`
- Time elapsed: 0.025 s
- Python 3.14.4, pandas 3.0.3

## Description
Dropped `strunz_number`, renamed `mineral_name` to `fr_mineral_name`, trimmed whitespace, removed empty values and case-insensitive duplicates (first occurrence kept), and sorted alphabetically ignoring case and diacritics.

## Statistics
| | input (`mineral_name`) | output (`fr_mineral_name`) |
|---|---:|---:|
| Records | 21460 | 3653 |
| Columns | 2 | 1 |
| Unique values (exact, trimmed) | 3661 | 3653 |
| Unique values (case-insensitive) | 3654 | 3653 |
| Empty values | 162 | 0 |

- Records removed: 17807
  - empty: 162
  - exact duplicates (after trimming): 17638
  - case-only duplicates: 7

## Case-only duplicates removed
| removed | kept |
|---|---|
| WIllemite | Willemite |
| Cobalto-adamite | Cobalto-Adamite |
| Mcgillite | McGillite |
| Sulfate de K Et Cr | Sulfate de K et Cr |
| Sulfate de K et Al | Sulfate de K Et Al |
| dolomite | Dolomite |
| calzirtite | Calzirtite |
