Overview
A compound specimen is comprised of one to many specimen parts

## Definitions
Compound Specimen: A collection object comprised of one or more discernible parts, called specimen parts, unified by physical attachment. The object's identity is determined by its specimen parts, which are distinguished from one another within a specific context.

Specimen Part: A physically discernible, proximal portion of a compound specimen that carries a single determination and belongs to a single material category, distinguished from the rest of the parent specimen by its physical and chemical exclusivity.

Specimen Name: Refers to any name assigned to a specimen at the object level (before atomization into specimen parts). Specimen names are often written as compound terms, a concatenation of multiple informal and formal identifiers.

Authoritative Name: A name assigned by an authoritative body based on a defined set of unambiguous criteria and belonging to a formal nomenclature

Cataloged Name: The unstructured name of a geological material for general, storage, curatorial, and/or presentation purposes.


## Data Model
Compound Specimen records have NULL values for is_part_of and the id is IN the set of is_part_of.
Specimen Parts: id = NULL (or catalog_number = NULL), is_part_of = SELECT id FROM table (The is_part_of value exists in the list of values in the id column)
The relationship between a compound specimen and its parts is defined by a self-join, id = is_part_of




