# French Language Mineral Name Transformations
> fr_mineral_names_transformations.md  
> 2026-09-29  
> tdwg2026-wks10  

Purpose: Instructions to transform the fr_mineral_names input file.

# Process
1. Drop the `strunz_number` column.
2. Rename `mineral_name` to `fr_mineral_name`.
3. Drop duplicate values: trim whitespace, drop empty values, compare case-insensitively, and keep
   the first occurrence.
4. Sort alphabetically, ignoring case and diacritics.
5. Save as `fr_mineral_names_01.csv`.
6. **Exclusions.** Build the exclusion list, then filter. Removal only (rules E and X below).
   ```
   python src/build/build_fr_mineral_names_exclusion_list.py --source data/output/fr_mineral_names/fr_mineral_names_01.csv --exclusion-list fr_mineral_names_exclusion_list.csv
   python src/transform/filter_by_exclusion_list.py --exclusion-list fr_mineral_names_exclusion_list.csv --input data/output/fr_mineral_names/fr_mineral_names_01.csv
   ```
   Output: `fr_mineral_names_02_filtered.csv`.
7. **Value transformations.** Reformat values (rules T below). Output: `fr_mineral_names_03.csv`.

Steps 1–5: `python src/transform/fr_mineral_names_transform.py` (report `reports/fr_mineral_names_01_report.md`).
Step 7 is not implemented yet.

## Exclusions (step 6)
Exclusions only **remove** text. They either remove a whole value (a row) or delete a substring
from a value. They never replace text, split values, change case or otherwise reformat. The
exclusion list (`src/config/fr_mineral_names_exclusion_list.csv`) has a `match` column: `full` or
`substring`.

### Full-value exclusions (E rules, `match = full`)
The rule must match the **entire** value. The row is removed. These rules apply in addition to the
general criteria in `docs/specifications/mineral_names_exclusion_list_specification.md` and take
precedence over them.

| Rule | Removes | Pattern (whole value) | Values in the data |
|---|---|---|---|
| E1 | Lot notes: a sample count followed by a list of names | `> N Éch. …` | `> 10 Éch. Cassiterite, Etc. (Liste)`, `> 10 Éch. Magnétite, Grenat, Scheelite`, `> 20 Éch. Recherche Agardite-Ce, Etc. (Liste)`, `> 5 Éch. Magnetite, Etc.` |
| E2 | To-be-checked placeholders | `à` / `a` + `analyser`, `identifier`, `déterminer`, `vérifier`, `préciser` | `A analyser`, `à identifier` |
| E3 | Organic-acid salts named by composition | `Acétate`, `Formiate`, `Oxalate`, `Tartrate`, `Urate` or `Citrate` + ` de ` + element symbols | `Acétate de Cu`, `Formiate de Ca`, `Oxalate de K`, `Tartrate de K`, `Urate de K`, … |
| E4 | Individual values that no pattern covers, listed verbatim | exact value | `(Carbonate-)cyanotrichite` |
| — | One-off values from `data/output/fr_mineral_names/single_exclusions.csv` | exact value | `Sulfate de K et Al`, `Us Gypsum Mine, Empire, Nv`, … |

### Substring exclusions (X rules, `match = substring`)
Applied after the full-value exclusions, in this order. The matched text is deleted and the value's
ends are trimmed. A row left empty is removed.

After the exclusions, the filter drops duplicate values: compared case-insensitively, first
occurrence kept. Substring deletions make many values identical (`Pennine = Clinochlore` →
`Pennine`).

| Rule | Deletes | Before | After |
|---|---|---|---|
| X1 | ` = ` and everything after it | `Acmite = Aegirine` | `Acmite` |
| X2 | ` de ` and everything after it | `Sulfate hydraté de Ni,Mg` | `Sulfate hydraté` |
| X3 | the word `synthétique` | `Béryl synthétique` | `Béryl` |
| X4 | question marks: `?`, `??`, `(?)` | `Monazite-(Ce?)`, `Cacoxenite ???` | `Monazite-(Ce)`, `Cacoxenite` |

X2 also cuts these names short. Decide whether they are exceptions: `Oeil de tigre`,
`Oeil de faucon`, `Produits de Geyser`, `Dendrites de Mn`, `Fluorite recouvert de Quartz`,
`Alun de potassium`. Forms written with `d'` (`Sulfate d'Al et K`) are not matched by X2.

## Value transformations (step 7)
Reformatting only. These rules change the form of a value and are **not** part of the exclusion
step. Apply them to `fr_mineral_names_02_filtered.csv` in this order.

| Rule | Action | Before | After |
|---|---|---|---|
| T1 | Split a single-quoted name into its own row, and remove the quotes. A lone trailing quote is removed. | `Clinochlore'Kotschubeite'`<br>`Albite'` | `Clinochlore` + `Kotschubeite`<br>`Albite` |
| T2 | Capitalize the first letter of each value. | `muscovite` | `Muscovite` |
| T3 | Collapse repeated spaces, drop any duplicates this creates, and sort (as in step 4). | `Natrolite  aragonite` | `Natrolite aragonite` |
