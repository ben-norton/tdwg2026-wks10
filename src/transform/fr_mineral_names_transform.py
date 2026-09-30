"""Run steps 1-5 of docs/transformations/fr_mineral_names_transformations.md.

Steps:
    1. Drop the strunz_number column.
    2. Rename mineral_name to fr_mineral_name.
    3. Drop duplicate values: trim whitespace, drop empty values, and remove duplicates compared
       case-insensitively, keeping the first occurrence (as in de_mineral_names_dedupe.py).
    4. Sort alphabetically, ignoring case and diacritics.
    5. Save as fr_mineral_names_01.csv.

Input:  data/output/fr_mineral_names/fr_mineral_names_00.csv
Output: data/output/fr_mineral_names/fr_mineral_names_01.csv
        data/output/fr_mineral_names/reports/fr_mineral_names_01_report.md

Usage:
    python src/transform/fr_mineral_names_transform.py [--input PATH] [--output PATH]
"""

import argparse
import sys
import time
import unicodedata
from datetime import datetime
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "data" / "output" / "fr_mineral_names"

DEFAULT_INPUT = OUTPUT_DIR / "fr_mineral_names_00.csv"
DEFAULT_OUTPUT = OUTPUT_DIR / "fr_mineral_names_01.csv"
SPECIFICATION = "docs/transformations/fr_mineral_names_transformations.md"
SOURCE_COLUMN = "mineral_name"
COLUMN = "fr_mineral_name"


def sort_key(name):
    """Casefold and strip diacritics so 'Galène' sorts next to 'Galene'."""
    decomposed = unicodedata.normalize("NFKD", name)
    return "".join(c for c in decomposed if not unicodedata.combining(c)).casefold()


def profile(df, column):
    values = df[column].str.strip()
    return {
        "records": len(df),
        "columns": len(df.columns),
        "unique_exact": values.nunique(),
        "unique_casefold": values.str.casefold().nunique(),
        "empty": int((values == "").sum()),
    }


def transform(input_path, output_path):
    source = pd.read_csv(input_path, dtype=str, keep_default_na=False, encoding="utf-8-sig")

    # 1. Drop the strunz_number column
    names = source.drop(columns=["strunz_number"])

    # 2. Rename mineral_name to fr_mineral_name
    names = names.rename(columns={SOURCE_COLUMN: COLUMN})

    # 3. Drop duplicate values (trimmed, non-empty, case-insensitive; first occurrence kept)
    values = names[COLUMN].str.strip()
    empty = int((values == "").sum())
    values = values[values != ""]
    keys = values.str.casefold()
    exact_duplicates = int(values.duplicated().sum())
    case_duplicates = values[keys.duplicated() & ~values.duplicated()]
    values = values[~keys.duplicated()]

    # 4. Sort alphabetically, ignoring case and diacritics; ties broken by the raw value
    result = pd.DataFrame({COLUMN: sorted(values, key=lambda n: (sort_key(n), n))})

    # 5. Save as fr_mineral_names_01.csv
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output_path, index=False, encoding="utf-8-sig")

    return {
        "source": source,
        "result": result,
        "empty": empty,
        "exact_duplicates": exact_duplicates,
        "case_duplicates": case_duplicates,
    }


def write_report(input_path, output_path, stats, started, elapsed):
    before = profile(stats["source"], SOURCE_COLUMN)
    after = profile(stats["result"], COLUMN)
    kept = {n.casefold(): n for n in stats["result"][COLUMN]}

    def rel(path):
        return path.resolve().relative_to(REPO_ROOT).as_posix()

    lines = [
        "# fr_mineral_names transformation report",
        f"> {started:%Y-%m-%d %H:%M:%S}",
        "",
        "## Provenance",
        f"- Script: `{rel(Path(__file__))}`",
        f"- Command: `python {' '.join(sys.argv)}`",
        f"- Specification: `{SPECIFICATION}` (steps 1-5)",
        f"- Input: `{rel(input_path)}`",
        f"- Output: `{rel(output_path)}`",
        f"- Time elapsed: {elapsed:.3f} s",
        f"- Python {sys.version.split()[0]}, pandas {pd.__version__}",
        "",
        "## Description",
        "Dropped `strunz_number`, renamed `mineral_name` to `fr_mineral_name`, trimmed whitespace, removed "
        "empty values and case-insensitive duplicates (first occurrence kept), and sorted alphabetically "
        "ignoring case and diacritics.",
        "",
        "## Statistics",
        f"| | input (`{SOURCE_COLUMN}`) | output (`{COLUMN}`) |",
        "|---|---:|---:|",
        f"| Records | {before['records']} | {after['records']} |",
        f"| Columns | {before['columns']} | {after['columns']} |",
        f"| Unique values (exact, trimmed) | {before['unique_exact']} | {after['unique_exact']} |",
        f"| Unique values (case-insensitive) | {before['unique_casefold']} | {after['unique_casefold']} |",
        f"| Empty values | {before['empty']} | {after['empty']} |",
        "",
        f"- Records removed: {before['records'] - after['records']}",
        f"  - empty: {stats['empty']}",
        f"  - exact duplicates (after trimming): {stats['exact_duplicates']}",
        f"  - case-only duplicates: {len(stats['case_duplicates'])}",
        "",
        "## Case-only duplicates removed",
    ]
    if stats["case_duplicates"].empty:
        lines.append("None.")
    else:
        lines += ["| removed | kept |", "|---|---|"]
        lines += [f"| {n} | {kept[n.casefold()]} |" for n in stats["case_duplicates"]]

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
