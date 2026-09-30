# de_locations transformation report
> 2026-09-24 13:48:43

## Provenance
- Script: `src/transform/de_locations_transform.py`
- Command: `python src/transform/de_locations_transform.py`
- Specification: `docs/transformations/de_locations_transformations.md`
- Input: `data/output/de_locations/de_locations_verbatim_00.csv`
- Output: `data/output/de_locations/de_locations_01.csv`
- Intermediate: `data/output/de_locations/de_locations_transposed.csv`
- Authorities: `data/authorities/geopolitical/countries.csv`, `data/authorities/geopolitical/first_order_divisions.csv`, `data/authorities/geopolitical/second_order_divisions.csv`
- Python 3.13.2, pandas 3.0.3

## Summary
- Source records: 14092
- Rows after transposing comma separated values: 47201
- Unique location values: 15860

| division_rank | rows | unique values |
|---|---:|---:|
| namedPlace | 25348 | 14325 |
| Country | 11497 | 284 |
| First Order Division | 7239 | 536 |
| Second Order Division | 3117 | 715 |

## Notes
- Matching is case-insensitive and ignores diacritics; parenthetical aliases such as `(Karlsbad)` are dropped when the full value does not match.
- When a name exists at more than one level the highest rank is used (Country > First Order Division > Second Order Division).
- Values not found in the authorities are labeled `namedPlace`.

## Most frequent namedPlace values
| location | rows |
|---|---:|
| Grisons | 881 |
| Czechoslovakia | 257 |
| Bohemia | 151 |
| USSR | 150 |
| Tujetsch | 148 |
| Bavaria | 141 |
| Saxony | 134 |
| Eifel | 114 |
| Freiburg | 110 |
| Binn | 109 |
| Silenen | 100 |
| Russia | 97 |
| Schwarzwald | 85 |
| St. Gallen | 80 |
| Guttannen | 79 |
| Ural | 76 |
| Tschechische Republik | 74 |
| Rhineland-Palatinate | 71 |
| Hesse | 68 |
| Zermatt | 68 |
| Oberwald | 67 |
| Airolo | 60 |
| Göschenen | 59 |
| Westfalen | 55 |
| Kaiserstuhl | 54 |
