# German language locations transformations
> 2026-09-24
> de_locations_transformations.md
> tdwg2026-wks10


Start: data/output/de_locations/de_locations_verbatim_00.csv
1. remove catalog_number column
2. Remove quotation marks
3. Transpose comma separated values into rows.
4. Copy to new file de_locations_transposed.csv
5. Categorize values by geopolitical rank - country, first order division, second order division, placename, township. Use GADM authoritative dataset for reference. EWtner the category into the second column


First Order (Geopolitical/Administrative ) Division: he primary subnational administrative unit into which a sovereign country is divided for governance.
Second Order Divisions: Geopolitical partitions of first order divisions exactly 2 levels below country.
Municipality: The full, unabbreviated name of the next smaller administrative region than county (city, municipality, etc.) in which the dcterms:Location occurs. Do not use this term for a nearby named place that does not contain the actual dcterms:Location.
namedPlace: A spatial object representing any real-world geographical entity or location that can be assigned one or more names that is not a country, first order, or second order geopolitical division




