# de_locations Transformation — Version A (transpose to rows)
> 2026-09-24 · tdwg2026-wks10 · implemented by `src/transform/de_locations_transform.py` (steps 1–5) and `src/transform/de_locations_translate.py` (step 6)

## Input
- File: `data/output/de_locations/de_locations_verbatim_00.csv`
- Columns: `catalog_number`, `location`
- `location` is a quoted, comma-separated list of place names ordered from finest (left) to coarsest (right). The rightmost name is normally a country. Example: `"Fleimstal, Tirol, Italy"`.
- Names mix German and English.

## Reference data
GADM-derived authority files in `data/authorities/geopolitical/`, matched on column `name`:
- `countries.csv` → `Country`
- `first_order_divisions.csv` → `First Order Division`
- `second_order_divisions.csv` → `Second Order Division`
* GADM should be used as a reference, but not the sole authority. Location names may be interpreted such as abbreviated names

## Steps
1. Drop column `catalog_number`.
2. Remove all `"` characters from `location`.
3. Split `location` on `,` into one row per name. Trim whitespace. Drop empty values.
4. Write the result to `de_locations_transposed.csv` (column `location`).
5. Add column `division_rank` and assign each name a rank:
   - Match rule: casefold, strip diacritics and collapse whitespace on both sides. Try the full value first, then the value with parenthetical text removed.
   - If the name appears in more than one authority file, the higher rank wins (Country > First Order Division > Second Order Division).
   - No match → `namedPlace`.
   - Output: `de_locations_01.csv` (columns `location`, `division_rank`).
6. Add column `location_en`:
   - `Country`, `First Order Division`, `Second Order Division`: English form of the name. Copy the name unchanged if it is already English.
   - `namedPlace`: leave empty.
   - Output: `de_locations_02.csv` (columns `location`, `division_rank`, `location_en`).

Each output also gets a provenance report, `reports/<output stem>_report.md`.

## Rank definitions
- **Country**: sovereign state.
- **First Order Division**: the main subnational administrative unit of a country (e.g. state, province, region).
- **Second Order Division**: a subdivision of a first order division, two levels below country (e.g. county, district).
- **namedPlace**: any other named geographic entity (locality, mountain, island, mine, valley). Also used for every value that no authority file matches.

## Known limitation
Step 3 removes each name's position in its original list, so step 5 has no hierarchical context to work with. Ambiguous or non-standard names, including many countries, end up as `namedPlace`. Version B fixes this.
