# fr_mineral_names_01_compound_values report
> 2026-09-29 16:16:56

## Provenance
- Script: `src/transform/list_compound_values.py`
- Command: `python src/transform/list_compound_values.py`
- Input: `data/output/fr_mineral_names/fr_mineral_names_02_filtered.csv` (column `fr_mineral_name`)
- Output: `data/output/fr_mineral_names/fr_mineral_names_01_compound_values.csv`
- Time elapsed: 0.017 s
- Python 3.14.4, pandas 3.0.3

## Description
Listed the distinct values that contain more than one whitespace-separated word. Hyphenated names count as one word, and a parenthesised suffix such as -(Ce) or (Y) belongs to the name.

## Statistics
| | count |
|---|---:|
| Input: records | 3407 |
| Input: columns | 1 |
| Input: distinct values | 3407 |
| Input: records with one word | 3164 |
| Input: records with more than one word | 243 |
| Output: distinct compound values | 243 |

| words | distinct values |
|---:|---:|
| 2 | 161 |
| 3 | 52 |
| 4 | 17 |
| 5 | 12 |
| 6 | 1 |
