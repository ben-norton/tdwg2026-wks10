# Project Specifications
> 2026-09-24
> project_specifications.md
> tdwg2026-wks10

1. Generate a summary report everytime a script is run against a dataset in the data/input or data/output directory. The
report should summarize the results of the query, provide the command used to run the script, the timestamp, and any other
generally important information for provenance.
2. Transformations are done in a stepwise fashion where each time a script is run, a 
new version of an output dataset is created with two-digit number + 1 of the source file.
Example: a transformation is run against dataset_00.csv. The result is named: dataset_01.csv.
3. 


