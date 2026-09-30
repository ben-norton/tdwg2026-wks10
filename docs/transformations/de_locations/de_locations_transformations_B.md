# de_locations Transformation — Version B (split to columns, context-aware ranking)
> 2026-09-24 · tdwg2026-wks10 · not yet implemented as a script

## Input
- File: `data/output/de_locations/de_locations_verbatim_00.csv`
- Columns: `catalog_number`, `location`
- `location` is a quoted, comma-separated list of place names ordered from finest (left) to coarsest (right). The rightmost name is normally a country. Example: `"Fleimstal, Tirol, Italy"`.
- Names mix German and English.

## Reference data
GADM-derived authority files in `data/authorities/geopolitical/` (`countries.csv`, `first_order_divisions.csv`, `second_order_divisions.csv`), matched on column `name`.

## Steps
1. Drop column `catalog_number`.
2. Remove all `"` characters from `location`.
3. Keep one row per source record:
   - Column 1, `verbatim_location_name`: the full, unsplit string from step 2.
   - Then split the string on `,` into separate columns, one name per column, trimmed, in the original left-to-right order. The number of columns is the largest name count in any row. Leave unused cells empty.
4. Write the result to `de_locations_rows_to_columns.csv`.
5. Assign a rank to each name:
   - Look the name up in the authority files.
   - Use its position in the row as context. The rightmost name is the coarsest, and ranks get finer from right to left. When a name matches several ranks, or none, choose the rank that fits its position between its neighbours.
   - Allowed ranks: `Country`, `First Order Division`, `Second Order Division`, `Municipality`, `namedPlace`.
   - Output: `de_locations_01.csv`, two columns `location`, `division_rank`, with one row per distinct name.
6. Add column `location_en` to `de_locations_01.csv`:
   - `Country`, `First Order Division`, `Second Order Division`: English form of the name. Copy the name unchanged if it is already English.
   - `Municipality`, `namedPlace`: leave empty.
   - Output: `de_locations_02.csv` (columns `location`, `division_rank`, `location_en`).

Each output also gets a provenance report, `reports/<output stem>_report.md`.

## Rank definitions
- **Country**: sovereign state.
- **First Order Division**: the main subnational administrative unit of a country (e.g. state, province, region).
- **Second Order Division**: a subdivision of a first order division, two levels below country (e.g. county, district).
- **Municipality**: the full, unabbreviated name of the administrative unit (city, town, municipality) that is the next level below a second order division and that contains the location. Do not use it for a nearby place that does not contain the location.
- **namedPlace**: any other named geographic entity (locality, mountain, island, mine, valley).
