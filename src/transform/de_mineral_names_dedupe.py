"""Remove duplicate German mineral names and sort them alphabetically.

Implements docs/transformations/de_mineral_names_transformations.md.

Steps:
    1. Trim whitespace and drop empty values.
    2. Remove duplicates, compared case-insensitively; keep the first occurrence.
    3. Sort alphabetically, ignoring case and diacritics.

Input:  data/output/de_mineral_names/de_mineral_names_00.csv
Output: data/output/de_mineral_names/de_mineral_names_01.csv
        data/output/de_mineral_names/reports/de_mineral_names_01_report.md

Usage:
    python src/transform/de_mineral_names_dedupe.py [--input PATH] [--output PATH]
"""

import argparse
import sys
import time
import unicodedata
from datetime import datetime
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "data" / "output" / "de_mineral_names"

DEFAULT_INPUT = OUTPUT_DIR / "de_mineral_names_00.csv"
DEFAULT_OUTPUT = OUTPUT_DIR / "de_mineral_names_01.csv"
SPECIFICATION = "docs/transformations/de_mineral_names_transformations.md"
COLUMN = "Mineral_Summary"


def sort_key(name):
    """Casefold and strip diacritics so 'Hämatit' sorts next to 'Hamatit'."""
    decomposed = unicodedata.normalize("NFKD", name)
    return "".join(c for c in decomposed if not unicodedata.combining(c)).casefold()


def profile(df):
    """Basic statistics for the report."""
    values = df[COLUMN]
    return {
        "records": len(df),
        "columns": len(df.columns),
        "unique_exact": values.nunique(),
        "unique_casefold": values.str.strip().str.casefold().nunique(),
        "empty": int((values.str.strip() == "").sum()),
    }


def transform(input_path, output_path):
    source = pd.read_csv(input_path, dtype=str, keep_default_na=False, encoding="utf-8-sig")

    # 1. Trim whitespace and drop empty values
    names = source[COLUMN].str.strip()
    names = names[names != ""]

    # 2. Remove case-insensitive duplicates, keeping the first occurrence
    keys = names.str.casefold()
    duplicates = names[keys.duplicated()]
    names = names[~keys.duplicated()]

    # 3. Sort ignoring case and diacritics, ties broken by the raw name
    result = pd.DataFrame({COLUMN: sorted(names, key=lambda n: (sort_key(n), n))})

    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output_path, index=False, encoding="utf-8-sig")

    return {"source": source, "result": result, "duplicates": duplicates}


def write_report(input_path, output_path, stats, started, elapsed):
    before = profile(stats["source"])
    after = profile(stats["result"])
    duplicates = stats["duplicates"]

    def rel(path):
        return path.resolve().relative_to(REPO_ROOT).as_posix()

    lines = [
        "# de_mineral_names transformation report",
        f"> {started:%Y-%m-%d %H:%M:%S}",
        "",
        "## Provenance",
        f"- Script: `{rel(Path(__file__))}`",
        f"- Command: `python {' '.join(sys.argv)}`",
        f"- Specification: `{SPECIFICATION}`",
        f"- Input: `{rel(input_path)}`",
        f"- Output: `{rel(output_path)}`",
        f"- Time elapsed: {elapsed:.3f} s",
        f"- Python {sys.version.split()[0]}, pandas {pd.__version__}",
        "",
        "## Description",
        "Trimmed whitespace, removed empty values and case-insensitive duplicate mineral names "
        "(first occurrence kept), and sorted the names alphabetically ignoring case and diacritics.",
        "",
        "## Statistics",
        "| | input | output |",
        "|---|---:|---:|",
        f"| Records | {before['records']} | {after['records']} |",
        f"| Columns | {before['columns']} | {after['columns']} |",
        f"| Unique values (exact) | {before['unique_exact']} | {after['unique_exact']} |",
        f"| Unique values (case-insensitive) | {before['unique_casefold']} | {after['unique_casefold']} |",
        f"| Empty values | {before['empty']} | {after['empty']} |",
        "",
        f"- Records removed: {before['records'] - after['records']} "
        f"({before['empty']} empty, {len(duplicates)} duplicate)",
        "",
        "## Duplicates removed",
    ]
    if duplicates.empty:
        lines.append("None.")
    else:
        lines += ["| removed | kept |", "|---|---|"]
        kept = {n.casefold(): n for n in stats["result"][COLUMN]}
        lines += [f"| {name} | {kept[name.casefold()]} |" for name in duplicates]

    report_path = output_path.parent / "reports" / f"{output_path.stem}_report.md"
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    started = datetime.now()
    timer = time.perf_counter()
    stats = transform(args.input, args.output)
    elapsed = time.perf_counter() - timer
    report_path = write_report(args.input, args.output, stats, started, elapsed)

    print(f"Wrote {len(stats['result'])} rows to {args.output}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
