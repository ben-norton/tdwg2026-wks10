# DwC archive master list
> build_dwc_archive_master_list_20260916T114937.md
> 2026-09-16
> geoda-transformation-pipeline

## How this file was produced

| | |
|---|---|
| Script | `src/mapping/build_dwc_archive_master_list.py` |
| Command | `python src/mapping/build_dwc_archive_master_list.py --out schemas/dwc/sources/dwc_archive_merged.csv` |
| Run | 2026-09-16 11:49:37 |
| Mode | write |
| Output | `schemas/dwc/sources/dwc_archive_merged.csv` |
| Reproduce | re-running the command above rewrites the same file |

## Inputs

| List | File | Rows read | Rows kept |
|---|---|---|---|
| `dwc_term_versions` | `schemas/dwc/sources/dwc_term_versions.csv` | 1415 | 362 |
| `minext-term-list` | `schemas/dwc/sources/minext-term-list.csv` | 47 | 47 |

## Counts

| | |
|---|---|
| Status kept | `recommended` |
| Darwin Core rows dropped by status | 1053 |
| Output rows | 409 |
| Output columns | 27 |

Darwin Core rows by status, before filtering:

| Status | Rows |
|---|---|
| superseded | 779 |
| recommended | 362 |
| deprecated | 274 |

## How the columns were merged

Rows are **stacked, not joined**. The two lists overlap on almost nothing —
the MinExt terms are proposed additions rather than annotations of existing
Darwin Core terms — so every output row comes from exactly one input and
`term_list` names which.

Columns are the union of the two headers: `term_list` first, then Darwin Core's in
their own order, then the MinExt columns Darwin Core does not already have.

| | Columns |
|---|---|
| Shared by both, merged into one each | `term`, `label`, `class_name`, `definition`, `examples`, `usage_note`, `rdf_type` |
| MinExt only | `class_ns_name`, `material_scope`, `source`, `datatype`, `is_required`, `note`, `editorial_note`, `namespace`, `namespace_iri`, `term_created`, `term_modified`, `document_modified`, `last_published` |
| Invented by this script | `term_list` |

A shared name keeps its Darwin Core position and is filled from whichever
file the row came from.

Both lists name the term itself `term`, so every row carries its term in
that one column — the Darwin Core list having been renamed from
`term_localName` to match.

## Terms appearing on more than one row

64 term names are carried by more than one row. This is expected and is
**not** duplication: Darwin Core publishes many terms twice, once for a
literal value (`dwc/terms/X`) and once for an IRI value (`dwc/iri/X`).
They are distinct terms with distinct `term_iri` values and both are kept.

| Term | Rows |
|---|---|
| `assayType` | 2 |
| `assertionBy` | 2 |
| `assertionType` | 2 |
| `assertionUnit` | 2 |
| `assertionValue` | 2 |
| `behavior` | 2 |
| `caste` | 2 |
| `dataGeneralizations` | 2 |
| `degreeOfEstablishment` | 2 |
| `discipline` | 2 |
| `disposition` | 2 |
| `establishmentMeans` | 2 |
| `eventCategory` | 2 |
| `eventType` | 2 |
| `fieldNotes` | 2 |
| … | *(49 more)* |

## Notes

- The MinExt list has no `status` column, so nothing filters it; it is
  carried whole.
- Written `utf-8-sig` with CRLF line endings, matching the inputs.
- The write is atomic: the file is built beside itself and moved into place,
  so a failed run cannot leave a half-written master list.

