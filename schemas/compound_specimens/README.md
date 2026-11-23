# Compound Specimens Schema
> README.md
> 2026-09-28
> tdwg2026-wks10

A template for recording simple and compound specimens in one self-referencing table, one row
per part, joined by `parent.id = child.is_part_of`. Built from the sample
`docs/samples/demo_compound_specimens_data.csv`; the model and its rules are in
`docs/specifications/compound_specimen_data_model_specification.md`.

| File | Contents |
|---|---|
| `compound_specimens_template.csv` | Header row to fill in (UTF-8 with BOM) |
| `compound_specimens_template_vertical.csv` | The same columns, one per line |
| `compound_specimens_dictionary.csv` | Definition, examples, datatype, Darwin Core mapping and the requirement per row class for each column |

## Row classes

`is_part_of` decides the class (spec §5):

| Class | `id` | `is_part_of` |
|---|---|---|
| simple specimen | catalog number | empty, and no row points at this `id` |
| compound specimen | catalog number | empty, and at least one row points at this `id` |
| specimen part | empty, unless another part points at it | the parent's `id` |

## Required names

| Class | `cataloged_name` | `authoritative_name` |
|---|---|---|
| simple specimen | REQUIRED | REQUIRED |
| compound specimen | REQUIRED | optional |
| specimen part | empty | REQUIRED |

`material_category`, `collection_code` and `institution_code` are required on every row. See
the dictionary's `simple_specimen`, `compound_specimen` and `specimen_part` columns for the
rest. Save the file as UTF-8.
