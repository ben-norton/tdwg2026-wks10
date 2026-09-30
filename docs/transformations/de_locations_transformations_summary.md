# de_locations Transformations — Summary of Versions A and B
> 2026-09-29 · tdwg2026-wks10
> Recipes: `de_locations_transformations_A.md`, `de_locations_transformations_B.md`

## Version A: context lost, ranks wrong
**Method.** Split each comma-separated location string (`"Charlottesville, Virginia, USA"`) into
one row per name. Rank each name on its own by exact lookup in the GADM authority lists. Any name
not found is ranked `namedPlace`.

**Result** (`de_locations_01.csv`, `de_locations_02.csv`). 14,092 source records became 47,201
rows and 15,860 unique names. Ranks assigned: 25,348 `namedPlace`, 11,497 `Country`, 7,239
`First Order Division`, 3,117 `Second Order Division`.

**Why the ranks are wrong.** Transposing turned each name into an isolated value. That removed the
hierarchy that says the last name in a string is the country. With no context, the only test left
was an exact GADM match, which fails in two ways:

1. **False match: a name matches the wrong GADM entry.** `USA` is not a GADM country name
   (GADM uses `United States`). It does match `Usa`, a city (*Shi*) in Ōita Prefecture, Japan,
   in the second-order division list. All 1,149 `USA` rows were ranked `Second Order Division`.
   `Bolivia`, `Venezuela`, `Taiwan` and `Zaire` were also ranked as first- or second-order
   divisions when they are the country of their record.
2. **No match: the name defaults to `namedPlace`.** Countries whose names differ from GADM were
   ranked `namedPlace`. These include historical names (`Czechoslovakia` 257, `USSR` 150,
   `Yugoslavia` 20, `Rhodesien` 6), German names (`Tschechische Republik` 74,
   `Dominikanische Republik` 12), abbreviations (`Tschech. Republik`) and names with a descriptor
   attached (`Valais Switzerland`, `Ost-Island`).

Of the 14,092 last names in the strings, which should be countries, 11,461 were ranked `Country`,
1,334 `namedPlace`, 1,224 `Second Order Division` and 73 `First Order Division`.

## Version B: context kept (pending)
**Method.** Keep one row per source record. Keep the verbatim string and split it into ordered
columns, so each name keeps its position. Rank each name using GADM together with its position:
the last name is the coarsest, and ranks get finer from right to left. GADM is a reference, not
the only authority. Where GADM gives several ranks for a name, or none, position decides.

**Expected result.** `USA` as the last name in `…, Utah, USA` resolves to `Country` and not to
the Japanese city. Historical and German country names in last position are ranked `Country` even
without a GADM match.

**Status.** Version B has not been implemented. There is no script or output yet, and the results
are to be confirmed when it runs.
