# fr_minerals_wikidata extraction report
> 2026-09-29 15:12:06

## Provenance
- Script: `src/extract/wiktionary_minerals.py`
- Command: `python src/extract/wiktionary_minerals.py --lang-code fr --lang-name French`
- Specification: `docs/transformations/wiktionary_minerals_extraction.md`
- Input: https://en.wiktionary.org/wiki/Category:fr:Minerals (MediaWiki API, retrieved 2026-09-29)
- Output: `data/authorities/mineral_names/fr_minerals_wikidata.csv`
- Time elapsed: 4.2 s
- Python 3.14.4, pandas 3.0.3

## Description
Listed the pages in Category:fr:Minerals, read the ==French== section of each, and took the English term that begins the first mineral/geology definition (or the first definition), following 'synonym of' links to the target entry.

## Statistics
| | count |
|---|---:|
| Input: category pages | 206 |
| Output: records | 206 |
| Output: columns | 3 |
| Output: records with an English name | 199 |
| Output: records without an English name | 7 |
| Output: English name taken from a synonym | 19 |
| Output: English name set by override | 2 |
| Output: English name equals French name (ignoring case) | 81 |
| Output: duplicate fr_mineral_name values | 0 |

## Records without an English name
- argyride: `# {{lb|fr|mineral}} any [[mineral]] containing [[silver]]`
- cyprine: `# {{lb|fr|mineral}} a blue variety of [[vesuvianite]]`
- mellite: `# {{lb|fr|mineral}} {{l|fr|mellite}}`
- xylocryptite: `# {{lb|fr|mineral}} {{synonym of|fr|mellite}}`
- zeuxite: `# {{lb|fr|mineral}} a form of green [[tourmaline]]`
- zincosite: `# {{lb|fr|mineral}} an [[evaporite]] composed of [[zinc sulfate]]`
- zoroche: `# {{lb|fr|obsolete|mineral}} an [[ore]] of [[silver]]`

## English names taken from a synonym
| name | synonym of | en_mineral_name |
|---|---|---|
| acmite | aegirine | aegirine |
| argyrose | acanthite | acanthite |
| hydrolithe | hydrolite | geyserite |
| mégabasite | wolframite | wolframite |
| mellite | mellite |  |
| monophane | épistilbite | epistilbite |
| paraedrite | rutile | rutile |
| xanthopyrite | pyrite | pyrite |
| xanthotitane | anatase | anatase |
| xaphyllite | tétradymite | tetradymite |
| xylocryptite | mellite |  |
| yanthosiderite | goethite | goethite |
| yarroshite | mélantérite | melanterite |
| yolithe | cordiérite | cordierite |
| ziguéline | cuprite | cuprite |
| zillerthite | actinote | actinolite |
| zinnspat | cassitérite | cassiterite |
| zircolite | corindon | corundum |
| zirlite | gibbsite | gibbsite |
| zurlite | wollastonite | wollastonite |
| zurlonite | wollastonite | wollastonite |

## Overrides
- écume de mer → meerschaum
- pyrite → pyrite
