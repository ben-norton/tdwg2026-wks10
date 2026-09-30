# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Materials for the TDWG 2026 workshop **WKS10: Geological Collections with Darwin Core — Compound
Specimen Model and Mineralogy Extension**. It is mostly data, specifications and presentation
material; the code is a handful of standalone pandas scripts that transform sample geology
datasets into the compound specimen model. There is no build, lint config or test suite.

## Running scripts

- Environment: Python ≥ 3.13 with pandas, declared in `pyproject.toml` and managed with `uv`
  (`package = false`: the scripts are not an installable package). `init.bat` activates the
  venv `.venv-tdwg2026-wks10` (Windows); `uv sync` targets `.venv` unless
  `UV_PROJECT_ENVIRONMENT=.venv-tdwg2026-wks10` is set.
- Every script runs from the repository root, takes optional `--input` / `--output`, and
  defaults to the correct files under `data/output/<dataset>/`:

```
python src/transform/de_locations_transform.py
python src/transform/de_locations_translate.py
python src/transform/mineral_samples_compound_transform.py
python src/transform/de_mineral_names_dedupe.py
python src/transform/fr_mineral_names_transform.py
python src/transform/filter_by_exclusion_list.py --exclusion-list de_mineral_names_exclusion_list.csv [--input <dataset>_NN.csv]
python src/extract/wiktionary_minerals.py --lang-code fr --lang-name French   # writes data/authorities/mineral_names/
python src/build/build_de_mineral_names_exclusion_list.py [--source PATH] [--exclusion-list FILENAME]
python src/build/build_fr_mineral_names_exclusion_list.py [--source PATH] [--exclusion-list FILENAME]
```

`src/extract/wiktionary_minerals.py` builds `<code>_minerals_wikidata.csv` authority lists from
Wiktionary; `src/load/` is an empty placeholder. `src/config/` holds exclusion lists, written by the `src/build/` scripts
(shared rule engine `exclusion_list_builder.py`); pass one to `filter_by_exclusion_list.py` by filename.

## Project conventions (`docs/specifications/project_specifications.md`)

- **Stepwise, versioned outputs.** Each transformation reads `<dataset>_NN` and writes a new file
  numbered `NN + 1` (two digits): `dataset_00.csv` → `dataset_01.csv`. Never overwrite the
  source step. `_00` files in `data/output/` are the untouched copies of `data/input/`.
- **Every time a `src/` script runs it must generate a report** in the `reports/` subdirectory
  of its output folder: `data/output/<dataset>/reports/<output stem>_report.md`. The report
  contains at least: the command run, the script run, timestamp, time elapsed, input file(s),
  output file(s), the specification followed, a short description of what the run did, and
  basic statistics for both the input and the output (number of records, columns, unique /
  empty / duplicate values, rows added or removed). Also record Python/pandas versions. New
  scripts should follow the `write_report()` pattern in the existing ones.
- Each script implements a written recipe in `docs/transformations/<dataset>_transformations.md`
  and cites it in its docstring and report. Update the recipe when the transform changes.
- Paths are resolved from `REPO_ROOT = Path(__file__).resolve().parents[2]`.

## Data layout

- `data/input/` — raw source datasets (German/French mineral names, German locations, mineral samples).
- `data/output/<dataset>/` — the versioned steps; their run reports are in `data/output/<dataset>/reports/`.
- `data/authorities/` — lookup lists used by the transforms: GADM-derived geopolitical
  divisions (`countries.csv`, `first_order_divisions.csv`, `second_order_divisions.csv`, keyed
  on `name`) and mineral names/varieties.
- `schemas/compound_specimens/` — the target template, vertical template and data dictionary
  (with per-row-class requirement columns) for compound specimen files.
- `schemas/dwc/sources/` — Darwin Core and Mineralogy Extension (MinExt) term lists.
- `docs/samples/demo_compound_specimens_data.csv` — invented `DEMO-*` example of the model,
  with a `template_note` column explaining each row.

## The compound specimen model

The central concept, specified in `docs/specifications/compound_specimen_data_model.md`
(definitions §2.1, required-name rules §6.3). Read the spec before changing anything that emits or
validates this shape.

- One table, **one row per part**, self-joined on `parent.id = child.is_part_of`.
- `is_part_of` alone classifies a row: empty → **specimen row**; non-empty → **part row**.
  A specimen row that some part references is a **compound specimen**, otherwise a **simple
  specimen**. Parts may nest (a part with an `id` that other parts reference).
- `id` on a specimen row is the catalog number. Leaf parts leave `id` empty; a referenced
  (intermediate) part must carry one, never derived from a row ordinal.
- Names: `cataloged_name` is required on specimen rows and empty on parts;
  `authoritative_name` is required on parts and simple specimens and **may be empty on a
  compound specimen row**. `material_category` is required on every row and set independently
  per row (never copied from parent to part).
- Locality and other specimen properties live on the specimen row only.
- Catalog numbers are unique only within a collection, so `collection_code` travels with `id`.

§8–§12 of the spec describe this repository's transform, its output, and open deviations
(D-01…D-07) such as the main part repeated as a part row in `mineral_samples_02.tsv`.

## Known staleness

`mineral_samples_compound_transform.py` and its report still cite pre-rename paths
(`docs/specifications/compound_model_specification.md`,
`compound_specimen_data_model_specification.md`, `docs/samples/compound_specimen_template.csv`,
`docs/samples/demo_compound_specimen_data.csv`). Its output columns predate
`material_subcategory` in the schema.
