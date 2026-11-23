# Wiktionary Minerals Extraction
> 2026-09-29 · tdwg2026-wks10 · implemented by `src/extract/wiktionary_minerals.py`

Builds a lookup of mineral names in one language paired with their English names, from an English
Wiktionary category. It produces the same three-column shape as
`data/authorities/mineral_names/de_minerals_wikidata.csv`, which came from `Category:de:Minerals`.
That file was built before this script existed, and no record of how it was made survives.

## Run
```
python src/extract/wiktionary_minerals.py --lang-code fr --lang-name French
```
- `--lang-code`: the Wiktionary language code in the category name (`Category:fr:Minerals`).
- `--lang-name`: the heading of the language section on each page (`==French==`).
- Output: `data/authorities/mineral_names/<code>_minerals_wikidata.csv`.
- Report: `data/authorities/mineral_names/reports/<code>_minerals_wikidata_report.md`.

## Input
- `https://en.wiktionary.org/wiki/Category:<code>:Minerals`, read through the MediaWiki API
  (`list=categorymembers`, then page wikitext in batches of 50). The script identifies itself with a
  User-Agent header and pauses 0.5 s between batches.
- Only main-namespace pages are read. Subcategories are not followed.

## Steps
1. List every page in the category.
2. For each page, keep only the `==<Language>==` section.
3. Collect the definition lines (`# …`, not `#:` / `#*`). Lines labelled mineral, mineralogy,
   geology, gemstone, rock or petrology (`{{lb|…}}` / `{{tlb|…}}`) are checked first, then the rest.
4. Remove label, qualifier and category templates from the start of each line. Then take the first
   line that matches one of these, in this order:
   - It starts with an English link: `[[term]]`, `[[term|shown]]`, `[[#English|term]]` or `{{l|en|term}}`.
     The English name is the term.
   - It is `{{synonym of|<code>|X}}`, `{{alternative form of|<code>|X}}` or `{{l|<code>|X}}`. The English
     name is the English name of entry X. X is fetched if it is not in the category, and a
     self-reference gives no name.
   - Prose definitions (`any [[mineral]] containing [[silver]]`, `a blue variety of [[vesuvianite]]`)
     give no English name. Leave `en_mineral_name` empty.
5. Apply `OVERRIDES` in the script. These are hand-checked names for entries where rule 4 picks the
   wrong sense or can't read the definition. Each override is listed in the report.
6. Write the rows sorted by name, ignoring case and diacritics, as UTF-8.

## Output columns
| Column | Content |
|---|---|
| `<code>_mineral_name` | The page title as written on Wiktionary (French names are lowercase, e.g. `hématite`). |
| `en_mineral_name` | English name, first letter capitalised. Empty when step 4 finds none. |
| `wikidata_uri` | The Wiktionary entry URL with a `#<Language>` anchor. The column name matches `de_minerals_wikidata.csv`. The values are Wiktionary URLs, not Wikidata IRIs. |

## Current French result (2026-09-29)
- 206 pages, 199 with an English name.
- 19 English names came from a synonym entry.
- 2 overrides: `écume de mer` → meerschaum, and `pyrite` → pyrite (pyrite is the synonym target of
  `xanthopyrite`).
- 7 left empty because their definitions are prose: `argyride`, `cyprine`, `mellite`,
  `xylocryptite`, `zeuxite`, `zincosite`, `zoroche`.
