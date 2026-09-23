# WKS10 - Sample Datasets

## Sample Datasets

Each dataset has one input file in `data/input/` and one output folder in `data/output/`.

| # | Dataset | Input file | Output folder |
| --- | --- | --- | --- |
| 1 | German Mineral Names | `data/input/de_mineral_names.csv` | `data/output/de_mineral_names/` |
| 2 | French Mineral Names | `data/input/fr_mineral_names.csv` | `data/output/fr_mineral_names/` |
| 3 | German Localities | `data/input/de_locations_verbatim.csv` | `data/output/de_locations/` |
| 4 | Peabody Compound Specimens | `data/input/mineral_samples.tsv` | `data/output/ypm_compound_specimens/` |

**Reference authorities** (in `data/authorities/`):

| File | Contents |
| --- | --- |
| `mineral_names/mineral_names_en.tsv` | English mineral names with Strunz (mindat) numbers |
| `mineral_names/varieties_en.csv` | Variety names and the mineral each is a variety of |
| `geopolitical/geopolitical_divisions.csv` | Countries, first-order and second-order divisions (`name`, `division_rank`) |

---

### Dataset 1: German Mineral Names

| Attribute | Description |
| --- | --- |
| **Input** | `data/input/de_mineral_names.csv` |
| **Output** | `data/output/de_mineral_names/` |
| **Form** | CSV (UTF-8 with BOM) with a single column, `Mineral_Summary`, of mineral names in German |
| **Task** | Translate the mineral names from German to English |
| **Reference authority** | `mineral_names_en.tsv` |
| **Skills demonstrated** | Profiling a simple dataset, translation, reconciliation against a mineral authority, reporting |

**Profile:**
- 2,191 names, all unique, none blank
- 1,748 end in the German suffix *-it* (e.g., *Glaukosphaerit*, *Hämatit*)
- 67 carry a rare-earth or chemical suffix, e.g., *Monazit-(Ce)*, *Xenotim-(Y)*
- Non-mineral or unresolved entries, e.g., *unbestimmt*, *undefiniert*, *undef Eisenhydroxid*
- German names that don't follow the suffix rule, e.g., *Quarz*, *Schwefel*, *Kupfer*, *Rotgültigerz*

**Suggested steps:**

1. Profile the list: count values and find duplicates, qualifiers and non-mineral entries.
2. Define the target, for example `name_de`, `name_en`, and a match status or authority reference.
3. Supply context, such as the mineral-name authority and German mineral-name conventions (e.g., the *-it* → *-ite* suffix).
4. Generate the script, run it, and review the report of unmatched and ambiguous names.

---

### Dataset 2: French Mineral Names

| Attribute | Description |
| --- | --- |
| **Input** | `data/input/fr_mineral_names.csv` |
| **Output** | `data/output/fr_mineral_names/` |
| **Form** | CSV with two columns: `mineral_name` (French) and `strunz_number` |
| **Task** | Translate the mineral names from French to English and check the Strunz numbers |
| **Reference authority** | `mineral_names_en.tsv` (names and Strunz numbers) |

**Profile:**
- 21,460 rows, one per specimen, so names repeat: 3,664 distinct names (e.g., *Quartz* 993, *Calcite* 593, *Fluorite* 292)
- 162 rows have no name, and 5,782 have no Strunz number
- Accented French forms, e.g., *Spodumène*, *Hématite*, *Sphalérite*, *Réalgar*
- 405 distinct values record synonyms with `=`, e.g., *Allevardite = Rectorite*
- 63 contain `?` (uncertain identifications), e.g., *Actinolite-tremolite?*
- 16 combine minerals with `/`, e.g., *Adulaire/titanite*
- Inconsistent rare-earth suffixes, e.g., *Aeschynite (Ce)* and *Aeschynite-(Ce)*
- Non-mineral entries and notes, e.g., *à identifier*, *Acétate de Cu et Ca*, *> 10 éch. Cassiterite, Etc. (Liste)*

**Suggested steps:**

1. Profile the list: reduce to distinct names with counts, and flag blanks, qualifiers, synonyms and notes.
2. Define the target, for example `name_fr`, `name_en`, `strunz_number`, and a match status.
3. Supply context: the mineral-name authority and French conventions (e.g., accents, *-ine*/*-ite* endings).
4. Generate the script, run it, and review the report of unmatched names and Strunz numbers that disagree with the authority.

---

### Dataset 3: German Localities

| Attribute | Description |
| --- | --- |
| **Input** | `data/input/de_locations_verbatim.csv` |
| **Output** | `data/output/de_locations/` |
| **Form** | CSV with `catalog_number` and `location`: comma-separated geopolitical entities and place names (verbatim locality strings) |
| **Task** | Split, categorize and translate locality strings into a structured place hierarchy |
| **Reference authority** | `geopolitical_divisions.csv`; GADM (administrative boundaries) |

**Profile of the locality data:**
- 14,092 records, each with a unique catalog number and locality string
- Mixed languages, mostly English and German (e.g., *Zypern*, *Totes Meer*, *Lothringen*, *zw. Paphos und Limasol*)
- Comma-separated values, 1–9 per record (most have 3 or 4)
- The order of levels (place → division → country) is generally consistent, with the country last
- Most common countries: Switzerland (4,308), Germany (1,998), USA (1,149), Italy (953), France (729)
- Historical country names, e.g., *Czechoslovakia*, *Zaire (Congo)*
- Contains uncertainty qualifiers, e.g., *near*, *bei*, *?*
- Limited use of controlled vocabularies
- Metric to record: number of parsed values compared with verbatim values

**Transformation workflow:**
1. **Can the values be categorized?** Define categories, identify external authorities, then process.
2. Create columns based on the categories.
3. Split the values into those columns.
4. Transpose the values into two columns: `label` and `rank`.
5. Address unresolved values.
6. Ask whether anything else can be automated or refined.
7. Categorize values by language.
8. Translate to English, keeping the original, for example `label_en`, `label_de` and `rank`.

**Context to provide to Claude:**
- A stepwise set of instructions
- The geopolitical authority and a reference to GADM
- Definitions of **country, first-order division, second-order division, township and named place**
- A defined **place hierarchy**

---

### Dataset 4: Convert Peabody Records into the Compound Model

| Attribute | Description |
| --- | --- |
| **Input** | `data/input/mineral_samples.tsv` |
| **Output** | `data/output/ypm_compound_specimens/` |
| **Task** | Stack multi-mineral specimen records into parent specimens and specimen parts |
| **Transformations** | `docs/transformations/mineral_sample_transformations.md` |
| **Target template** | `docs/samples/compound_specimen_template.csv`; `schemas/import_schema/import_template.csv` |

Sample records from the Yale Peabody Museum, Mineralogy & Meteoritics, already reduced to multi-mineral specimens and prepared by the transforms in `mineral_sample_transformations.md`.

**Profile:**

| Attribute | Value |
| --- | --- |
| Format | Tab-separated (TSV), UTF-8 |
| Records | 67 catalog records (`MIN.xxxxxx`), each with 2–5 minerals |
| Columns | 19 |
| Collection | Mineralogy & Meteoritics (all records) |
| Countries | 9, mostly USA (56), then Canada (3) and Denmark (2) |
| Divisions | Mostly Connecticut (43) and New Jersey (7); 2 records have no second-order division |
| Measurements | One per record: width (27), weight (22), length (13), height (2), depth (2), length (max.) (1) |

**Columns:**

| Field(s) | Role in the compound model |
| --- | --- |
| `irn`, `catalog_number` | Parent specimen identifier |
| `cataloged_name` | Parent name: `mineral_name_1` as catalogued, including any variety (e.g., *Corundum var. ruby*) |
| `mineral_name_1` … `_5` | **Part names.** These are the component minerals to stack. |
| `variety_name_1` … `_4` | Variety of the matching `mineral_name` (e.g., `mineral_name_2` = *Sodalite*, `variety_name_2` = *hackmanite*) |
| `measurement_type/value/unit` | Measurement of the whole specimen (stays on the parent) |
| `country`, `first_order_division`, `second_order_division` | Locality of the parent |
| `collection_name` | Collection of the parent |

**Parts per record:**

| Minerals per record | Records |
| ------------------- | ------- |
| 2                   | 12      |
| 3                   | 12      |
| 4                   | 30      |
| 5                   | 13      |
| **Total parts**     | **245** |

**Worked example: MIN.058343**

Source (one row):
`MIN.058343: Beryl, Tourmaline, Muscovite, Quartz: USA. Connecticut. Middlesex County.`

Target (stacked):

| catalog_number | is_part_of_catalog_number | cataloged_name | authoritative_name | verbatim_name |
| -------------- | ------------------------- | -------------- | ------------------ | ------------- |
| MIN.058343     | *(none; parent)*          | Beryl          |                    |               |
|                | MIN.058343                |                | Beryl              |               |
|                | MIN.058343                |                | Tourmaline         |               |
|                | MIN.058343                |                | Muscovite          |               |
|                | MIN.058343                |                | Quartz             |               |

Part records have no `catalog_number`; they point to the parent through `is_part_of_catalog_number`. Where a mineral has a variety, the part's `verbatim_name` holds it.

**Data-quality issues for participants to find:**

- The measurement type varies between records, and one value is "length (max.)".
- Measurement units vary (centimeters, grams).
- Generic names sit alongside species, e.g., *Mica* and *Garnet*.
- Two records have no second-order division.

**Steps (compound specimen model procedure):**

1. Identify the part-name fields (`mineral_name_1…5` paired with `variety_name_1…4`).
2. Create one parent record per catalog number, with `cataloged_name`, locality, collection and measurement.
3. Transpose the repeating columns into part records, with `authoritative_name` from `mineral_name_x` and `verbatim_name` from `variety_name_x`.
4. Set `is_part_of_catalog_number` on each part to the parent's `catalog_number`.
5. Stack the dataset, then generate a report with counts of parents and parts, names unmatched in the mineral authority, and anomalies.

---
