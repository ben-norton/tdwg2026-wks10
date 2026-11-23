# fr_mineral_names_exclusion_list build report
> 2026-09-29 16:15:46

## Provenance
- Script: `src/build/build_fr_mineral_names_exclusion_list.py`
- Command: `python src/build/build_fr_mineral_names_exclusion_list.py --source data/output/fr_mineral_names/fr_mineral_names_01.csv --exclusion-list fr_mineral_names_exclusion_list.csv`
- Specifications: `docs/specifications/exclusion_list_specification.md`, `docs/specifications/mineral_names_exclusion_list_specification.md`
- Input: `data/output/fr_mineral_names/fr_mineral_names_01.csv` (column `fr_mineral_name`)
- Single exclusions: `data/output/fr_mineral_names/single_exclusions.csv` (70 values)
- Output: `src/config/fr_mineral_names_exclusion_list.csv`
- Time elapsed: 0.060 s
- Python 3.14.4, pandas 3.0.3

## Description
Tested every distinct trimmed value against the specification's rules. A value is listed only if the whole value matches a rule; values that contain a name plus a qualifier are kept. Values in single_exclusions.csv are added verbatim.

## Statistics
| | count |
|---|---:|
| Input: records | 3653 |
| Input: columns | 1 |
| Input: distinct non-empty values | 3652 |
| Input: empty values (not listed; not a value) | 0 |
| Input: distinct values with an uncertainty qualifier | 63 |
| Output: full-value exclusions | 89 |
| Output: substring exclusions | 4 |
| Output: exclusion values matched after stripping uncertainty | 0 |
| Output: values added from single_exclusions.csv | 70 |
| single_exclusions.csv values a rule already lists | 0 |
| single_exclusions.csv values not in the input | 0 |
| Input records those values cover | 89 |

| category | values |
|---|---:|
| single exclusion | 70 |
| recipe rule | 10 |
| annotation | 8 |
| qualifier | 1 |

## Substring exclusions (applied in this order)
| pattern | meaning | input records affected |
|---|---|---:|
| `\s+=\s.*$` | X1: ' = ' and everything after it | 401 |
| `\s+de\s.*$` | X2: ' de ' and everything after it | 166 |
| `(?i)\s*\bsynth[ée]tique\b` | X3: the word 'synthétique' | 2 |
| `\s*\(\s*\?+\s*\)|\s*\?+` | X4: question marks: '?', '??', '(?)' | 63 |

## Uncertainty qualifiers stripped before matching
`\(\s*\?+\s*\)|\?+|(?<!\w)probable(ment)?(?!\w)|(?<!\w)peut-être(?!\w)|(?<!\w)douteux(?!\w)|(?<!\w)douteuse(?!\w)|(?<!\w)incertaine?(?!\w)|(?<!\w)possible(ment)?(?!\w)|(?<!\w)cf\.(?!\w)|(?<!\w)aff\.(?!\w)|(?<!\w)prob\.(?!\w)`

## Full-value exclusions
| fr_mineral_name | category | meaning |
|---|---|---|
| (Carbonate-)cyanotrichite | recipe rule | listed in the recipe (E4) |
| > 10 Éch. Cassiterite, Etc. (Liste) | annotation | lot note: more than 10 samples (E1) |
| > 10 Éch. Magnétite, Grenat, Scheelite | annotation | lot note: more than 10 samples (E1) |
| > 20 Éch. Recherche Agardite-Ce, Etc. (Liste) | annotation | lot note: more than 20 samples (E1) |
| > 5 Éch. Magnetite, Etc. | annotation | lot note: more than 5 samples (E1) |
| A analyser | annotation | to be checked: A analyser (E2) |
| à identifier | annotation | to be checked: à identifier (E2) |
| Acétate de Cu | recipe rule | organic-acid salt: Acétate (E3) |
| Acétate de Cu et Ca | recipe rule | organic-acid salt: Acétate (E3) |
| Acétate de Cu et Sr | recipe rule | organic-acid salt: Acétate (E3) |
| Alurgite = Mg, Fe, Mn Muscovite | single exclusion | listed in single_exclusions.csv |
| Amalgame [pas une espèce] | single exclusion | listed in single_exclusions.csv |
| Amazonite = Microcline | single exclusion | listed in single_exclusions.csv |
| Amber (2 Éch.) | single exclusion | listed in single_exclusions.csv |
| Amianthus=Tremolite, Actinolite, Chrysotile, etc | single exclusion | listed in single_exclusions.csv |
| Analcime (-1c,-1q,-1o,-1m) | single exclusion | listed in single_exclusions.csv |
| Argent (-3c,-2h,-4h) | single exclusion | listed in single_exclusions.csv |
| Argent (-3c,-2h,-4h) 'Amalgam' | single exclusion | listed in single_exclusions.csv |
| Argent (-3c,-2h,-4h) 'Kongsbergite' | single exclusion | listed in single_exclusions.csv |
| Formiate de Ca | recipe rule | organic-acid salt: Formiate (E3) |
| Formiate de Cd | recipe rule | organic-acid salt: Formiate (E3) |
| Inconnu | annotation | unknown / undetermined |
| Oxalate de K | recipe rule | organic-acid salt: Oxalate (E3) |
| Sulfate d'Al et Cr | single exclusion | listed in single_exclusions.csv |
| Sulfate d'Al et de Tl | single exclusion | listed in single_exclusions.csv |
| Sulfate d'Al et K | single exclusion | listed in single_exclusions.csv |
| Sulfate d'Al et NH4 | single exclusion | listed in single_exclusions.csv |
| Sulfate d'Al et Tl | single exclusion | listed in single_exclusions.csv |
| Sulfate d'Al, Cr et NH4 | single exclusion | listed in single_exclusions.csv |
| Sulfate d'in et Cs | single exclusion | listed in single_exclusions.csv |
| Sulfate de Ca | single exclusion | listed in single_exclusions.csv |
| Sulfate de Cd | single exclusion | listed in single_exclusions.csv |
| Sulfate de Co | single exclusion | listed in single_exclusions.csv |
| Sulfate de Co et de Tl | single exclusion | listed in single_exclusions.csv |
| Sulfate de Co et K | single exclusion | listed in single_exclusions.csv |
| Sulfate de Co et NH4 | single exclusion | listed in single_exclusions.csv |
| Sulfate de Cr et de NH4 | single exclusion | listed in single_exclusions.csv |
| Sulfate de Cr et K | single exclusion | listed in single_exclusions.csv |
| Sulfate de Cr, Al et Rb | single exclusion | listed in single_exclusions.csv |
| Sulfate de Cs et Al | single exclusion | listed in single_exclusions.csv |
| Sulfate de Cs et de Cr | single exclusion | listed in single_exclusions.csv |
| Sulfate de Cu | single exclusion | listed in single_exclusions.csv |
| Sulfate de Cu et Cr | single exclusion | listed in single_exclusions.csv |
| Sulfate de K | single exclusion | listed in single_exclusions.csv |
| Sulfate de K Et Al | single exclusion | listed in single_exclusions.csv |
| Sulfate de K et Al hydraté | single exclusion | listed in single_exclusions.csv |
| Sulfate de K et Cr | single exclusion | listed in single_exclusions.csv |
| Sulfate de K et Cr hydraté | single exclusion | listed in single_exclusions.csv |
| Sulfate de K et d'Al | single exclusion | listed in single_exclusions.csv |
| Sulfate de K et Li | single exclusion | listed in single_exclusions.csv |
| Sulfate de K, Cr et NH4 | single exclusion | listed in single_exclusions.csv |
| Sulfate de K, Fe et Cr | single exclusion | listed in single_exclusions.csv |
| Sulfate de Mg | single exclusion | listed in single_exclusions.csv |
| Sulfate de Mg et K | single exclusion | listed in single_exclusions.csv |
| Sulfate de N | single exclusion | listed in single_exclusions.csv |
| Sulfate de NH4 | single exclusion | listed in single_exclusions.csv |
| Sulfate de NH4 et d'Al | single exclusion | listed in single_exclusions.csv |
| Sulfate de NH4 et de Cu | single exclusion | listed in single_exclusions.csv |
| Sulfate de NH4 et de Fe | single exclusion | listed in single_exclusions.csv |
| Sulfate de NH4 et de Zn | single exclusion | listed in single_exclusions.csv |
| Sulfate de NH4 et Fe | single exclusion | listed in single_exclusions.csv |
| Sulfate de NH4 et K | single exclusion | listed in single_exclusions.csv |
| Sulfate de Ni | single exclusion | listed in single_exclusions.csv |
| Sulfate de Ni et K | single exclusion | listed in single_exclusions.csv |
| Sulfate de Ni et NH4 | single exclusion | listed in single_exclusions.csv |
| Sulfate de Ni et Rb | single exclusion | listed in single_exclusions.csv |
| Sulfate de Ni hydraté | single exclusion | listed in single_exclusions.csv |
| Sulfate de Ni, Cr et NH4 | single exclusion | listed in single_exclusions.csv |
| Sulfate de Rb et In | single exclusion | listed in single_exclusions.csv |
| Sulfate de Tl et Cr | single exclusion | listed in single_exclusions.csv |
| Sulfate de Tl et de Cr | single exclusion | listed in single_exclusions.csv |
| Sulfate de Tl, Cr et Al | single exclusion | listed in single_exclusions.csv |
| Sulfate de Zn et K | single exclusion | listed in single_exclusions.csv |
| Sulfate de Zn et NH4 | single exclusion | listed in single_exclusions.csv |
| Sulfate hydraté de Co,Cu,Zn,Mg,K | single exclusion | listed in single_exclusions.csv |
| Sulfate hydraté de Fe et NH4 | single exclusion | listed in single_exclusions.csv |
| Sulfate hydraté de Mg et NH4 | single exclusion | listed in single_exclusions.csv |
| Sulfate hydraté de Ni,Cu,Co,Zn | single exclusion | listed in single_exclusions.csv |
| Sulfate hydraté de Ni,Mg | single exclusion | listed in single_exclusions.csv |
| Sulfite de Sr | single exclusion | listed in single_exclusions.csv |
| Sulfure de Cd | single exclusion | listed in single_exclusions.csv |
| Sulfure de Na | single exclusion | listed in single_exclusions.csv |
| Tartrate de K | recipe rule | organic-acid salt: Tartrate (E3) |
| Tartrate de K et Na | recipe rule | organic-acid salt: Tartrate (E3) |
| The Storr, Skye, Scotland, Uk | annotation | locality recorded in the name field |
| Tungstenite (-2h,-3r) | single exclusion | listed in single_exclusions.csv |
| Urate de K | recipe rule | organic-acid salt: Urate (E3) |
| Us Gypsum Mine, Empire, Nv | single exclusion | listed in single_exclusions.csv |
| vert clair | qualifier | colour: vert clair |
