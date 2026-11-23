# de_locations_02 translation report
> 2026-09-24 14:03:17

## Provenance
- Script: `src/transform/de_locations_translate.py`
- Command: `python src/transform/de_locations_translate.py`
- Specification: `docs/transformations/de_locations_transformations.md`
- Input: `data/output/de_locations/de_locations_01.csv`
- Output: `data/output/de_locations/de_locations_02.csv`
- Python 3.13.2, pandas 3.0.3

## Summary
- Total rows: 47201
- Geopolitical division rows populated in `location_en`: 21853
- Named places left blank in `location_en`: 25348
- Total rows translated from German: 632
- Distinct translation mappings applied: 49

| division_rank | total rows | populated in location_en | translated from German |
|---|---:|---:|---:|
| Country | 11497 | 11497 | 23 |
| First Order Division | 7239 | 7239 | 588 |
| Second Order Division | 3117 | 3117 | 21 |
| namedPlace | 25348 | 0 | 0 |

## Translated Entities
| division_rank | location (German / original) | location_en (English) | occurrences |
|---|---|---|---:|
| Country | France (Kolonie) | France (Colony) | 1 |
| Country | Germany (5330.4/3402.6 Koord.dt.) | Germany (5330.4/3402.6 German coord.) | 1 |
| Country | Germany (5334.9/3396.6 Koord.dt.) | Germany (5334.9/3396.6 German coord.) | 1 |
| Country | Germany (5335.5/3396.0 Koord.dt.) | Germany (5335.5/3396.0 German coord.) | 1 |
| Country | Guinea (französisch) | Guinea (French) | 1 |
| Country | Italy (432.8/5093.1 Koord.it.) | Italy (432.8/5093.1 Italian coord.) | 1 |
| Country | Italy (440.3/5103.7 Koord.it.) | Italy (440.3/5103.7 Italian coord.) | 1 |
| Country | Italy (445.5/5102.5 Koord.it.) | Italy (445.5/5102.5 Italian coord.) | 1 |
| Country | Italy (588.9/5145.1 Koord.it.) | Italy (588.9/5145.1 Italian coord.) | 1 |
| Country | Italy (589.55/5143.4 Koord.it.) | Italy (589.55/5143.4 Italian coord.) | 1 |
| Country | Italy (597.7/5143.6 Koord.it.) | Italy (597.7/5143.6 Italian coord.) | 1 |
| Country | Italy (603.4/5139.2 Koord.it.) | Italy (603.4/5139.2 Italian coord.) | 1 |
| Country | Italy (603.4/5140.0 Koord.it.) | Italy (603.4/5140.0 Italian coord.) | 1 |
| Country | Italy (604.1/5146.1 Koord.it.) | Italy (604.1/5146.1 Italian coord.) | 1 |
| Country | Italy (604.21/5143.85 Koord.it.) | Italy (604.21/5143.85 Italian coord.) | 1 |
| Country | Italy (605.5/5148.4 Koord.it.) | Italy (605.5/5148.4 Italian coord.) | 1 |
| Country | Italy (eher Boarezzo) | Italy (rather Boarezzo) | 1 |
| Country | Namibia (Fund 1984) | Namibia (Found 1984) | 1 |
| Country | Switzerland (Kalkalpen!) | Switzerland (Limestone Alps!) | 1 |
| Country | Switzerland (italienische Seite) | Switzerland (Italian side) | 1 |
| Country | Switzerland (oder Afrika) | Switzerland (or Africa) | 1 |
| Country | Switzerland (oder Kienberg abklären!!) | Switzerland (or check Kienberg!!) | 1 |
| Country | Zimbabwe (Rhodesien) | Zimbabwe (Rhodesia) | 1 |
| First Order Division | Basel-Landschaft | Basel-Country | 266 |
| First Order Division | Tirol | Tyrol | 122 |
| First Order Division | Kärnten | Carinthia | 66 |
| First Order Division | Basel-Stadt | Basel-City | 55 |
| First Order Division | Steiermark | Styria | 39 |
| First Order Division | Zürich | Zurich | 21 |
| First Order Division | Corse (Korsika) | Corsica (Corsica) | 4 |
| First Order Division | Karlovy Vary (Karlsbad) | Karlovy Vary (Carlsbad) | 4 |
| First Order Division | Liège (Lüttich) | Liège (Liege) | 2 |
| First Order Division | Niederösterreich | Lower Austria | 2 |
| First Order Division | Ararat (Gipfel) | Ararat (Peak) | 1 |
| First Order Division | Cluj (Klausenberg) | Cluj (Klausenburg) | 1 |
| First Order Division | Jura (Gebirge) | Jura (Mountains) | 1 |
| First Order Division | Maramures (Komitat Maramaros) | Maramures (Maramaros County) | 1 |
| First Order Division | Nouvelle-Calédonie (Neukaledonien/SW-Pazifik) | New Caledonia (New Caledonia/SW Pacific) | 1 |
| First Order Division | Tirol (Italy od. Austria) | Tyrol (Italy or Austria) | 1 |
| First Order Division | uri | Uri | 1 |
| Second Order Division | Konstanz | Constance | 10 |
| Second Order Division | Lake Superior (Canada od. USA) | Lake Superior (Canada or USA) | 3 |
| Second Order Division | Braunschweig | Brunswick | 2 |
| Second Order Division | (angeblich Hungary) Franklin | (allegedly Hungary) Franklin | 1 |
| Second Order Division | Bodensee | Lake Constance | 1 |
| Second Order Division | München | Munich | 1 |
| Second Order Division | Nürnberg | Nuremberg | 1 |
| Second Order Division | Südliche Weinstrasse | Southern Wine Route | 1 |
| Second Order Division | Wunsiedel im Fichtelgebirge | Wunsiedel in the Fichtel Mountains | 1 |

