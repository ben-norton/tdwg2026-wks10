"""Run the transformations in docs/transformations/de_locations_transformations.md.

Steps:
    1. Remove the catalog_number column.
    2. Remove quotation marks.
    3. Transpose comma separated values into rows.
    4. Copy to de_locations_transposed.csv.
    5. Categorize each value by geopolitical rank using the GADM-derived
       authority files and write the rank into the second column.

Input:  data/output/de_locations/de_locations_verbatim_00.csv
Output: data/output/de_locations/de_locations_01.csv
        data/output/de_locations/de_locations_transposed.csv
        data/output/de_locations/de_locations_01_report.md

Usage:
    python src/transform/de_locations_transform.py [--input PATH] [--output PATH]
"""

import argparse
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"
OUTPUT_DIR = DATA_DIR / "output" / "de_locations"
AUTHORITY_DIR = DATA_DIR / "authorities" / "geopolitical"

DEFAULT_INPUT = OUTPUT_DIR / "de_locations_verbatim_00.csv"
DEFAULT_OUTPUT = OUTPUT_DIR / "de_locations_01.csv"
TRANSPOSED_NAME = "de_locations_transposed.csv"

# Checked in order: the highest rank wins when a name appears at several levels.
AUTHORITY_FILES = [
    ("Country", AUTHORITY_DIR / "countries.csv"),
    ("First Order Division", AUTHORITY_DIR / "first_order_divisions.csv"),
    ("Second Order Division", AUTHORITY_DIR / "second_order_divisions.csv"),
]
UNMATCHED_RANK = "namedPlace"

PARENTHETICAL = re.compile(r"\s*\([^)]*\)")


def normalize(name):
    """Casefold and strip diacritics so 'Frederiksvärn' matches 'Frederiksvarn'."""
    decomposed = unicodedata.normalize("NFKD", str(name))
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    return " ".join(stripped.casefold().split())


def load_authorities():
    """Return {normalized name: rank}, keeping the highest rank for duplicates."""
    lookup = {}
    for rank, path in AUTHORITY_FILES:
        names = pd.read_csv(path, dtype=str, keep_default_na=False)["name"]
        for name in names:
            lookup.setdefault(normalize(name), rank)
    return lookup


def categorize(value, lookup):
    """Match the full value, then the value with parenthetical aliases removed."""
    for candidate in (value, PARENTHETICAL.sub("", value)):
        rank = lookup.get(normalize(candidate))
        if rank:
            return rank
    return UNMATCHED_RANK


def transform(input_path, output_path):
    source = pd.read_csv(input_path, dtype=str, keep_default_na=False)
    source_rows = len(source)

    # 1. Remove catalog_number column
    locations = source.drop(columns=["catalog_number"])

    # 2. Remove quotation marks
    locations["location"] = locations["location"].str.replace('"', "", regex=False)

    # 3. Transpose comma separated values into rows
    transposed = locations.assign(location=locations["location"].str.split(","))
    transposed = transposed.explode("location")
    transposed["location"] = transposed["location"].str.strip()
    transposed = transposed[transposed["location"] != ""].reset_index(drop=True)

    # 4. Copy to de_locations_transposed.csv
    transposed_path = output_path.parent / TRANSPOSED_NAME
    transposed.to_csv(transposed_path, index=False, encoding="utf-8")

    # 5. Categorize values by geopolitical rank into the second column
    lookup = load_authorities()
    rank_cache = {v: categorize(v, lookup) for v in transposed["location"].unique()}
    transposed["division_rank"] = transposed["location"].map(rank_cache)
    transposed.to_csv(output_path, index=False, encoding="utf-8")

    return {
        "source_rows": source_rows,
        "transposed_rows": len(transposed),
        "unique_values": len(rank_cache),
        "transposed_path": transposed_path,
        "result": transposed,
    }


def write_report(input_path, output_path, stats, started):
    result = stats["result"]
    rank_counts = result["division_rank"].value_counts()
    unique_ranks = result.drop_duplicates("location")["division_rank"].value_counts()
    unmatched = (
        result[result["division_rank"] == UNMATCHED_RANK]["location"]
        .value_counts()
        .head(25)
    )

    def rel(path):
        return path.resolve().relative_to(REPO_ROOT).as_posix()

    lines = [
        "# de_locations transformation report",
        f"> {started:%Y-%m-%d %H:%M:%S}",
        "",
        "## Provenance",
        f"- Script: `{rel(Path(__file__))}`",
        f"- Command: `python {' '.join(sys.argv)}`",
        f"- Specification: `docs/transformations/de_locations_transformations.md`",
        f"- Input: `{rel(input_path)}`",
        f"- Output: `{rel(output_path)}`",
        f"- Intermediate: `{rel(stats['transposed_path'])}`",
        "- Authorities: "
        + ", ".join(f"`{rel(path)}`" for _, path in AUTHORITY_FILES),
        f"- Python {sys.version.split()[0]}, pandas {pd.__version__}",
        "",
        "## Summary",
        f"- Source records: {stats['source_rows']}",
        f"- Rows after transposing comma separated values: {stats['transposed_rows']}",
        f"- Unique location values: {stats['unique_values']}",
        "",
        "| division_rank | rows | unique values |",
        "|---|---:|---:|",
    ]
    for rank in rank_counts.index:
        lines.append(f"| {rank} | {rank_counts[rank]} | {unique_ranks.get(rank, 0)} |")
    lines += [
        "",
        "## Notes",
        "- Matching is case-insensitive and ignores diacritics; parenthetical "
        "aliases such as `(Karlsbad)` are dropped when the full value does not match.",
        "- When a name exists at more than one level the highest rank is used "
        "(Country > First Order Division > Second Order Division).",
        f"- Values not found in the authorities are labeled `{UNMATCHED_RANK}`.",
        "",
        f"## Most frequent {UNMATCHED_RANK} values",
        "| location | rows |",
        "|---|---:|",
    ]
    lines += [f"| {name} | {count} |" for name, count in unmatched.items()]

    report_path = output_path.with_name(f"{output_path.stem}_report.md")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    started = datetime.now()
    stats = transform(args.input, args.output)
    report_path = write_report(args.input, args.output, stats, started)

    print(f"Wrote {stats['transposed_rows']} rows to {args.output}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
