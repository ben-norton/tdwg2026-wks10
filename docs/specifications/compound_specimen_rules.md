# Rules for Compound Specimens
> compound_specimen_rules.md  
> 2026-09-28  
> tdwg2026-wks10  


* A simple specimen is a specimen record without any related records based on the self-join id = is_part_of has both an authoritative name and cataloged name
* The root specimen record in a compound specimen must have a cataloged_name
* cataloged_name is only required for the root specimen record in the compound model structure or for simple specimens.
* authoritative_name may be empty on the root specimen record of a compound specimen.

If id is not null and is_part_of is null then cataloged_name is required.
if is_part_of is not null, then authoritative name is required.

