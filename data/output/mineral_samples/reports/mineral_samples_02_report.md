# mineral_samples compound model transformation report
> 2026-09-24 13:59:29

## Provenance
- Script: `src/transform/mineral_samples_compound_transform.py`
- Command: `python src/transform/mineral_samples_compound_transform.py`
- Specifications: `docs/transformations/mineral_sample_transformations.md`, `docs/specifications/compound_model_specification.md`, `docs/specifications/compound_specimen_data_model_specification.md`
- Targets: `docs/samples/compound_specimen_template.csv`, `docs/samples/demo_compound_specimen_data.csv`
- Input: `data/output/mineral_samples/mineral_samples_00.tsv`
- Output: `data/output/mineral_samples/mineral_samples_02.tsv`
- Python 3.13.2, pandas 3.0.3

## Summary
- Source records: 67
- Output rows: 311
- Specimen rows: 67
- Part rows: 244
- Part rows with a verbatim_name (variety): 5

| material_category | part rows |
|---|---:|
| Mineral | 242 |
| Rock | 1 |
| Fossil | 1 |

## Validation
| check | count |
|---|---:|
| Specimen rows without id | 0 |
| Duplicate specimen ids | 0 |
| Part rows carrying an id | 0 |
| Part rows whose is_part_of matches no specimen id | 0 |
| Rows missing authoritative_name | 0 |
| Rows missing material_category | 0 |
| Simple specimens | 0 |
| Compound specimens | 67 |

## Notes
- The main part (mineral_name_1) is named on the specimen row and also listed as a part row, matching demo_compound_specimen_data.csv.
- Category overrides: `Lujavrite` → Rock, `Carpites sp.` → Fossil; all other names are Mineral.
- Repeated sibling names merged into one part: MIN.104139 (Quartz)
- Names not found in `data/authorities/mineral_names/mineral_names_en.tsv`: Apophyllite, Biotite, Carpites sp., Chlorite, Garnet, Garnet group, Heulandite, Lepidolite, Lujavrite, Mica, Scapolite, Serpentine Lizardite, Stilbite, Tourmaline, Willemite, Zincite, Zincolibethenite, Zircon, Zoisite
