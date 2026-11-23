# de_mineral_names Exclusion List Specification
> 2026-09-29
> de_mineral_names_exclusion_list_specification.md
> tdwg2026-wks10

## 1. Purpose
This specification defines which values from the German mineral names dataset go into the
exclusion list, and what format the list must follow. A listed value is a row that is not a mineral
name: a qualifier, an abbreviation, an acronym or a catalogue annotation.
`src/transform/filter_by_exclusion_list.py` removes the listed values from the dataset.

The key words MUST, MUST NOT and SHOULD follow RFC 2119.

## 2. Scope
| Item | Value |
|---|---|
| Exclusion list | `src/config/de_mineral_names_exclusion_list.csv` |
| Target file | `data/output/de_mineral_names/de_mineral_names_01.csv`, column `Mineral_Summary` |
| Filtered output | `data/output/de_mineral_names/de_mineral_names_02_filtered.csv` |
| Transformation recipe | `docs/transformations/de_mineral_names_transformations.md` |

History: the list was first saved as `exclusion_list.csv` in the same folder as the target file. It
was then moved to `src/config/`, where all exclusion lists are stored, and renamed.

## 3. Method
1. Review every value in the target file by hand.
2. Test each value against §4 (include) and §5 (do not include). §5 takes precedence.
3. Add each qualifying value to the list following §6, with its category and meaning.
4. Run the filter:
   `python src/transform/filter_by_exclusion_list.py --exclusion-list de_mineral_names_exclusion_list.csv`
   Then check the report (§7).

## 4. Inclusion criteria
Include a value only if the **entire** value is not a mineral name. It MUST belong to exactly one
of these categories:

| category | Criterion | Examples |
|---|---|---|
| `polytype designation` | A polytype symbol on its own, with or without the word `Polytyp`. | `1M`, `2M`, `2M1`, `2M2`, `Polytyp 2H`, `Polytyp 3R`, `Polytyp unbestimmt` |
| `qualifier` | A word or abbreviation that describes a name (status, texture, habit, scope or origin) but names no material. | `allgemein`, `diskred`, `feinkristallin`, `Fenster- u Zepter-`, `Neotyp`, `sl`, `synth` |
| `annotation` | A catalogue note or placeholder, or a generic term for a mixture, a group or an unspecified mineral. Notes and placeholders cover undetermined, unnamed, to be checked, and cross-references. | `unbestimmt`, `undefiniert`, `Mineral nicht bestimmt`, `ohne Namen`, `Noch abklären`, `s Objektbem`, `s Objektbemerkung`, `Prov`, `Gemenge`, `Mineralgemenge`, `Mineralgruppe`, `Mischkristall`, `organisches Mineral`, `sekundäres Uranmineral` |
| `acronym` | An acronym or chemical symbol used instead of a name. | `Sb` (the name `Antimon` is listed separately) |

## 5. Exclusion criteria (values that stay in the data)
The list MUST NOT include:

| Case | Reason | Examples |
|---|---|---|
| A mineral name combined with a qualifier | The name part is still needed. | `Olivin allgemein`, `Dickit 2M1`, `Rauchquarz-Gwindel` |
| Varieties, gem names and trade names | They name a material. | `Amethyst`, `Edelopal`, `Sagenit` |
| Habit terms used as specimen names | Collections use them as material names. | `Gwindel` |
| Chemical class names | They name a class of material. | `Karbonat`, `Phosphat`, `Sulfosalz`, `Cu-Sulfid`, `Mn-Silikat` |
| Non-mineral materials | They name a material. | `Bitumen`, `Erdoel`, `Perlen`, `Kolm` |
| Named synthetic materials | They name a material. | `YAG Yttrium-Aluminium-Granat` |
| Vague descriptions that still name a substance | They carry material information. | `undef Eisenhydroxid`, `ungen def Mn-Hydr`, `Mn-Au-Oxidphase`, `Pt-Au-phase`, `Mn-Ferro-Ferri-Win` |
| Uncertain values | Removing data cannot be undone downstream. Flag the value for review instead. | — |

## 6. File format
- **Location:** `src/config/`. Pass the list to the filter by filename only.
- **Encoding:** UTF-8 with BOM, comma-separated, with a header row.
- **Columns:**

| Column | Required | Content |
|---|---|---|
| `Mineral_Summary` | yes | The value to exclude. The filter matches only on this first column. |
| `category` | yes | One of `polytype designation`, `qualifier`, `annotation`, `acronym` (§4). |
| `meaning` | yes | A short English gloss of the value. |

- **Exact values:** each value MUST be copied exactly from the target file. The filter trims
  whitespace, but it is case-sensitive, so every case or spelling variant needs its own row.
- **Unique:** each value MUST appear only once.
- **Sort order:** rows SHOULD be sorted by `Mineral_Summary`, ignoring case.

## 7. Validation
The filter report (`reports/de_mineral_names_02_filtered_report.md`) MUST show:
- `Exclusion values with no match in the input: 0`. An unmatched entry is a typo or a stale
  value. Correct it or remove it.
- `Records removed` equal to the number of rows in the list.

## 8. Current list (2026-09-29)
29 values: 7 `polytype designation`, 7 `qualifier`, 14 `annotation`, 1 `acronym`. Filtering
`de_mineral_names_01.csv` (2,190 rows) gives `de_mineral_names_02_filtered.csv` (2,161 rows).
