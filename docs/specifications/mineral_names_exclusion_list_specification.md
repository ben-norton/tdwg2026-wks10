# Mineral Names Exclusion List Specification
> 2026-09-29
> mineral_names_exclusion_list_specification.md
> tdwg2026-wks10

Criteria for identifying values to exclude from mineral name datasets. This specification extends
`exclusion_list_specification.md`. The target entity is a **mineral name**, which includes mineral
species, groups, varieties and traditional names.

## 1. File location
- `src/config/<dataset>_exclusion_list.csv`
- German mineral names: `src/config/de_mineral_names_exclusion_list.csv`
- French mineral names: `src/config/fr_mineral_names_exclusion_list.csv`

Build scripts: `src/build/build_de_mineral_names_exclusion_list.py` and
`src/build/build_fr_mineral_names_exclusion_list.py`. Each one encodes these criteria as rules and
writes the list to `src/config/`.

## 2. Criteria

### 2.1 Exclude a value when
The **entire** value is not a mineral name and falls into one of these categories:

| category | Criterion | Examples |
|---|---|---|
| `polytype designation` | A polytype symbol on its own, with or without the word for polytype. | `1M`, `2M1`, `Polytyp 3R`, `Polytyp unbestimmt` |
| `qualifier` | Describes a mineral name (status, colour, texture, habit, scope, origin) but names no material. | `allgemein`, `diskred`, `feinkristallin`, `Fenster- u Zepter-`, `Neotyp`, `sl`, `synth`, `vert clair` |
| `annotation` | A catalogue note or placeholder, a generic term for a mixture, group or unspecified mineral, or a value that belongs in another field (e.g. a locality). | `unbestimmt`, `ohne Namen`, `Noch abklären`, `s Objektbemerkung`, `Gemenge`, `Mineralgruppe`, `sekundäres Uranmineral`, `A analyser`, `Inconnu`, `The Storr, Skye, Scotland, Uk` |
| `acronym` | An acronym or chemical symbol used instead of a mineral name. | `Sb` |

### 2.2 Dataset rules
A dataset's transformation recipe may add whole-value exclusion rules, including values listed
verbatim, e.g. rules E1–E4 in `docs/transformations/fr_mineral_names_transformations.md`. These
rules take precedence over §2.3. Their entries use the category `recipe rule` unless they fit a
category in §2.1.

### 2.3 Do not exclude a value when it is
| Case | Examples |
|---|---|
| A mineral name with a qualifier or polytype | `Olivin allgemein`, `Dickit 2M1`, `Rauchquarz-Gwindel` |
| A variety, gem name or trade name | `Amethyst`, `Edelopal`, `Sagenit` |
| A habit term used as a specimen name | `Gwindel` |
| A chemical class name | `Karbonat`, `Phosphat`, `Sulfosalz`, `Cu-Sulfid`, `Mn-Silikat` |
| A non-mineral geological or organic material | `Bitumen`, `Erdoel`, `Perlen`, `Kolm` |
| A named synthetic material | `YAG Yttrium-Aluminium-Granat` |
| A vague description that still names a substance | `undef Eisenhydroxid`, `ungen def Mn-Hydr`, `Mn-Au-Oxidphase`, `Pt-Au-phase` |
| Uncertain | Flag it for review instead of excluding it. |
