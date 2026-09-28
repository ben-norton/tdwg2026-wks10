"""Transform mineral samples into the compound specimen model.

Follows docs/transformations/mineral_sample_transformations.md and
docs/specifications/compound_model_specification.md, with
docs/samples/compound_specimen_template.csv and
docs/samples/demo_compound_specimen_data.csv as the target shape.

Each source record becomes:
    - one specimen row: id = catalog_number, is_part_of empty, cataloged_name,
      and the main part (mineral_name_1) in authoritative_name;
    - one part row per distinct mineral_name_1-5: id empty,
      is_part_of = catalog_number, authoritative_name = mineral_name_x and
      verbatim_name = variety_name_x where present.
The self-join is id = is_part_of. Locality stays on the specimen row only.

Input:  data/output/mineral_samples/mineral_samples_00.tsv
Output: data/output/mineral_samples/mineral_samples_02.tsv
        data/output/mineral_samples/mineral_samples_02_report.md

Usage:
    python src/transform/mineral_samples_compound_transform.py [--input PATH] [--output PATH]
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "data" / "output" / "mineral_samples"
MINERAL_AUTHORITY = REPO_ROOT / "data" / "authorities" / "mineral_names" / "mineral_names_en.tsv"

DEFAULT_INPUT = OUTPUT_DIR / "mineral_samples_00.tsv"
DEFAULT_OUTPUT = OUTPUT_DIR / "mineral_samples_02.tsv"

COLLECTION_CODE = "DEMO-C"
INSTITUTION_CODE = "DEMO"
DEFAULT_CATEGORY = "Mineral"
# Names in the mineral columns that are not minerals.
CATEGORY_OVERRIDES = {
    "Lujavrite": "Rock",
    "Carpites sp.": "Fossil",
}

MINERAL_COLUMNS = [f"mineral_name_{i}" for i in range(1, 6)]
VARIETY_COLUMNS = {f"mineral_name_{i}": f"variety_name_{i}" for i in range(1, 5)}
LOCALITY_COLUMNS = ["country", "first_order_division", "second_order_division"]

OUTPUT_COLUMNS = [
    "id",
    "is_part_of",
    "material_category",
    "cataloged_name",
    "authoritative_name",
    "verbatim_name",
    "collection_code",
    "institution_code",
    *LOCALITY_COLUMNS,
]


def category_for(name):
    return CATEGORY_OVERRIDES.get(name, DEFAULT_CATEGORY)


def build_rows(source):
    rows = []
    duplicates = []
    for record in source.to_dict("records"):
        catalog_number = record["catalog_number"]
        main_name = record["mineral_name_1"]

        rows.append({
            "id": catalog_number,
            "is_part_of": "",
            "material_category": category_for(main_name),
            "cataloged_name": record["cataloged_name"],
            "authoritative_name": main_name,
            "verbatim_name": record["variety_name_1"],
            "collection_code": COLLECTION_CODE,
            "institution_code": INSTITUTION_CODE,
            **{col: record[col] for col in LOCALITY_COLUMNS},
        })

        # A part is an instance of a type: repeated sibling names become one part.
        seen = set()
        for column in MINERAL_COLUMNS:
            name = record[column]
            if not name:
                continue
            variety = record.get(VARIETY_COLUMNS.get(column), "")
            if (name, variety) in seen:
                duplicates.append((catalog_number, name))
                continue
            seen.add((name, variety))
            rows.append({
                "id": "",
                "is_part_of": catalog_number,
                "material_category": category_for(name),
                "cataloged_name": "",
                "authoritative_name": name,
                "verbatim_name": variety,
                "collection_code": COLLECTION_CODE,
                "institution_code": INSTITUTION_CODE,
                **{col: "" for col in LOCALITY_COLUMNS},
            })

    return pd.DataFrame(rows, columns=OUTPUT_COLUMNS), duplicates


def validate(result):
    """Checks from compound_specimen_data_model_specification.md section 11."""
    specimens = result[result["is_part_of"] == ""]
    parts = result[result["is_part_of"] != ""]
    referenced = set(parts["is_part_of"])
    return {
        "Specimen rows without id": int((specimens["id"] == "").sum()),
        "Duplicate specimen ids": int(specimens["id"].duplicated().sum()),
        "Part rows carrying an id": int((parts["id"] != "").sum()),
        "Part rows whose is_part_of matches no specimen id": int(
            (~parts["is_part_of"].isin(set(specimens["id"]))).sum()
        ),
        "Rows missing authoritative_name": int((result["authoritative_name"] == "").sum()),
        "Rows missing material_category": int((result["material_category"] == "").sum()),
        "Simple specimens": int((~specimens["id"].isin(referenced)).sum()),
        "Compound specimens": int(specimens["id"].isin(referenced).sum()),
    }


def write_report(input_path, output_path, source, result, duplicates, checks, started):
    def rel(path):
        return path.resolve().relative_to(REPO_ROOT).as_posix()

    authority = set(
        pd.read_csv(MINERAL_AUTHORITY, sep="\t", dtype=str)["name"].str.casefold()
    )
    names = sorted({n for n in result["authoritative_name"] if n})
    unmatched = [n for n in names if n.casefold() not in authority]
    parts = result[result["is_part_of"] != ""]

    lines = [
        "# mineral_samples compound model transformation report",
        f"> {started:%Y-%m-%d %H:%M:%S}",
        "",
        "## Provenance",
        f"- Script: `{rel(Path(__file__))}`",
        f"- Command: `python {' '.join(sys.argv)}`",
        "- Specifications: `docs/transformations/mineral_sample_transformations.md`, "
        "`docs/specifications/compound_model_specification.md`, "
        "`docs/specifications/compound_specimen_data_model_specification.md`",
        "- Targets: `docs/samples/compound_specimen_template.csv`, "
        "`docs/samples/demo_compound_specimen_data.csv`",
        f"- Input: `{rel(input_path)}`",
        f"- Output: `{rel(output_path)}`",
        f"- Python {sys.version.split()[0]}, pandas {pd.__version__}",
        "",
        "## Summary",
        f"- Source records: {len(source)}",
        f"- Output rows: {len(result)}",
        f"- Specimen rows: {len(result) - len(parts)}",
        f"- Part rows: {len(parts)}",
        f"- Part rows with a verbatim_name (variety): {int((parts['verbatim_name'] != '').sum())}",
        "",
        "| material_category | part rows |",
        "|---|---:|",
    ]
    for category, count in parts["material_category"].value_counts().items():
        lines.append(f"| {category} | {count} |")

    lines += ["", "## Validation", "| check | count |", "|---|---:|"]
    lines += [f"| {check} | {count} |" for check, count in checks.items()]

    lines += ["", "## Notes"]
    lines.append(
        "- The main part (mineral_name_1) is named on the specimen row and also "
        "listed as a part row, matching demo_compound_specimen_data.csv."
    )
    lines.append(
        "- Category overrides: "
        + ", ".join(f"`{n}` → {c}" for n, c in CATEGORY_OVERRIDES.items())
        + f"; all other names are {DEFAULT_CATEGORY}."
    )
    if duplicates:
        lines.append(
            "- Repeated sibling names merged into one part: "
            + ", ".join(f"{cat} ({name})" for cat, name in duplicates)
        )
    lines.append(
        "- Names not found in `data/authorities/mineral_names/mineral_names_en.tsv`: "
        + ", ".join(unmatched)
    )

    report_path = output_path.with_name(f"{output_path.stem}_report.md")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    started = datetime.now()
    source = pd.read_csv(args.input, sep="\t", dtype=str, keep_default_na=False)
    source = source.apply(lambda col: col.str.strip())

    result, duplicates = build_rows(source)
    result.to_csv(args.output, sep="\t", index=False, encoding="utf-8")

    checks = validate(result)
    report_path = write_report(
        args.input, args.output, source, result, duplicates, checks, started
    )

    print(f"Wrote {len(result)} rows to {args.output}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
