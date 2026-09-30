# de_mineral_names Transformations
> 2026-09-29 · tdwg2026-wks10 · implemented by `src/transform/de_mineral_names_dedupe.py`

## Input
- File: `data/output/de_mineral_names/de_mineral_names_00.csv` (UTF-8 with BOM)
- One column, `Mineral_Summary`: one German mineral name per row.

## Steps
1. Trim leading and trailing whitespace. Drop empty values.
2. Remove duplicates. Two names are duplicates when they are equal after casefolding
   (`Unbestimmt` = `unbestimmt`). Keep the first occurrence in source order.
3. Sort alphabetically, ignoring case and diacritics (`Hämatit` sorts with `Hamatit`, not after `Z`).
   Break ties by the unmodified name.
4. Output: `de_mineral_names_01.csv` (column `Mineral_Summary`, UTF-8 with BOM).

Each run writes a report, `reports/de_mineral_names_01_report.md`.

## Exclusion list criteria
The rules for building `src/config/de_mineral_names_exclusion_list.csv` are specified in
`docs/specifications/de_mineral_names_exclusion_list_specification.md`.

## Filter by exclusion list
Implemented by `src/transform/filter_by_exclusion_list.py` (generic; works for any `<dataset>_NN` file).

- Input: `de_mineral_names_01.csv` and an exclusion list passed by filename with `--exclusion-list`
  (here `de_mineral_names_exclusion_list.csv`). Exclusion lists are always stored in `src/config/`. The
  list's first column holds the values to remove. Other columns (`category`, `meaning`) are documentation.
- Match the exclusion list's first column against the target column with the same name
  (`Mineral_Summary`), or the target's first column if none has that name. Compare exact values after
  trimming whitespace. Matching is case-sensitive.
- Drop every matching row.
- Output: `de_mineral_names_02_filtered.csv`, which is the input step number + 1 with the suffix `_filtered`.
  The report is `reports/de_mineral_names_02_filtered_report.md` and lists removed values and any exclusion
  values not found in the input.
