# Mineral Samples Dataset Transformations
> 2026-09-23
> ypm_mineral_sample_transformations.md
> tdwg2026-wks10

Purpose: Transform sample mineral records into the compound specimen model using a self-join.
Summary: Specimen parts are defined in pairs, mineral_name_1-5 and an associated vareity_name_2-4

### Notes
1. Only mineral_name_2-4 have variety names.
2. Every specimen part record has na authoritative_name popularted using mineral_name_2-5. verbatim_name 
stores the variety name where applicable.
3. The compound specimen model join is based on catalog_number, where
minerals.catalog_number = minerals.is_part_of_catalog_number and a
specimen record (minerals.catalog_number) has 1-4 specimen part records.
4. catalog_number is always null for specimen part records
5. is_part_of_catalog_number is always null for specimen records

## Parent Compound Specimens
main_mineral_name = cataloged_name

## Specimen Parts
1. authoritative_name = mineral_name_x where x is number 1-5.
2. verbatim_name = variety_name_x where x corresponds to the associated mineral_name and applicable where
variety_name is not null.

## Transforms
1. Rename main_mineral_name to cataloged_name
2. Set cataloged_name = mineral_name_1 (contains full name with var. where applicable)
3. Create columns variety_name_1 - variety_name_4
4. Populate variety_name where the corresponding mineral_name contains the string var. Populate the associated variety_name with the string after var. Then remove var. x from mineral_name

## Map to compound_specimen_template.csv
* id = catalog_number
* is_part_of = is_part_of_catalog_number
* material_category = 'Mineral'
* collection_code = 'DEMO-C'
* institution_code = 'DEMO'