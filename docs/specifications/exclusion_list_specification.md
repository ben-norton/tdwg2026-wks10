# Exclusion List Specification
> 2026-09-29
> exclusion_list_specification.md
> tdwg2026-wks10

General criteria for identifying values to exclude from a dataset column. Criteria for a specific
domain extend these criteria (e.g. `mineral_names_exclusion_list_specification.md`).

## 1. File location
- Store every exclusion list in `src/config/`.
- Name it `<dataset>_exclusion_list.csv`, where `<dataset>` is the target file's dataset name
  (`de_mineral_names_01.csv` → `de_mineral_names_exclusion_list.csv`).
- Columns: the value column, `match`, `category`, `meaning`. `match` is `full` (remove the row whose
  whole value equals the entry) or `substring` (a regular expression whose matches are deleted from
  values). Exclusions only remove text. Replacements, splitting and reformatting belong in the
  dataset's value transformations, not in the exclusion list.
- Optional: `single_exclusions.csv` in the same folder as the target file. It holds a header row,
  then one value per row, for one-off exclusions that no rule covers. The build scripts always
  check for it and add its values to the list verbatim, with the category `single exclusion`. The
  filter also reads it. If the file does not exist, both skip it.

## 2. Criteria
The **target entity** is the kind of thing the target column is meant to hold: a mineral name, a
place name, a taxon name, and so on.

### 2.0 Before testing a value
Strip uncertainty qualifiers, then test what remains against §2.1 and §2.2:
- question marks in any form: `?`, `???`, `(?)`, `(Ce?)` → `(Ce)`;
- uncertainty words, given per language by each build script (e.g. `fraglich`, `vermutlich`,
  `probable`, `peut-être`, `cf.`, `aff.`).

A value that is only an uncertainty qualifier (e.g. `???`) is excluded as a qualifier. The list
records the original value, because the filter matches values exactly.

### 2.1 Exclude a value when
The **entire** value is not a name or instance of the target entity. The value falls into one of
these classes:

| Class | Criterion |
|---|---|
| Qualifier | A word or abbreviation that describes an entity (status, certainty, scope, form, origin) but names none. |
| Annotation | A catalogue note or placeholder: undetermined, unnamed, to be checked, see elsewhere, or a generic term for a group, mixture or unspecified entity. |
| Code or designation | A code, symbol or designation that classifies an entity but is not its name. |
| Acronym or symbol | An acronym, abbreviation or symbol used instead of the name. |

### 2.2 Do not exclude a value when
- It contains a valid name together with a qualifier, code or note. The name is still needed.
- It names the target entity at a broader or narrower level than expected (a group, a class, a variety).
- It is a synonym, a variant spelling, an older name or a trade name of the target entity.
- It names something outside the target entity that is still a real material or object. That is a
  scope decision, not an exclusion.
- It is vague but still identifies a substance or object.
- Its status is uncertain. Flag it for review instead of excluding it.
