"""List the values of a column that contain more than one word (name).

Words are separated by whitespace, so a hyphenated name (Actinolite-tremolite) is one word. A
parenthesised suffix such as -(Ce), -(Y) or -(Ce,La) belongs to the name before it. Written
with a space instead of a hyphen, as in 'Aeschynite (Ce)', it still counts as part of that name.

Input:  data/output/fr_mineral_names/fr_mineral_names_02_filtered.csv
Output: data/output/fr_mineral_names/fr_mineral_names_01_compound_values.csv
        data/output/fr_mineral_names/reports/fr_mineral_names_01_compound_values_report.md

Usage:
    python src/transform/list_compound_values.py [--input PATH] [--output PATH] [--column NAME]
"""

import argparse
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "data" / "output" / "fr_mineral_names"
DEFAULT_INPUT = OUTPUT_DIR / "fr_mineral_names_02_filtered.csv"
DEFAULT_OUTPUT = OUTPUT_DIR / "fr_mineral_names_01_compound_values.csv"

# A name suffix: -(Ce), (Y), -(Ce,La); attached to the preceding word before counting
SUFFIX = re.compile(r"\s*-?\s*\((?:[A-Z][a-z]?|REE)(?:\s*,\s*(?:[A-Z][a-z]?|REE))*\)")


def words(value):
    """Split into whitespace-separated words after folding name suffixes into the name."""
    folded = SUFFIX.sub(lambda m: "-" + m.group(0).strip().lstrip("-").strip(), value)
    return folded.split()


def transform(input_path, output_path, column):
    source = pd.read_csv(input_path, dtype=str, keep_default_na=False, encoding="utf-8-sig")
    column = column or source.columns[0]
    values = source[column].str.strip()

    counts = values.map(lambda v: len(words(v)))
    result = pd.DataFrame({column: values[counts > 1], "word_count": counts[counts > 1]})
    result = result.drop_duplicates(column)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output_path, index=False, encoding="utf-8-sig")
    return {"source": source, "column": column, "counts": counts, "result": result}


def write_report(input_path, output_path, stats, started, elapsed):
    counts, result = stats["counts"], stats["result"]

    def rel(path):
        path = path.resolve()
        return path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else path.as_posix()

    lines = [
        f"# {output_path.stem} report",
        f"> {started:%Y-%m-%d %H:%M:%S}",
        "",
        "## Provenance",
        f"- Script: `{rel(Path(__file__))}`",
        f"- Command: `python {' '.join(sys.argv)}`",
        f"- Input: `{rel(input_path)}` (column `{stats['column']}`)",
        f"- Output: `{rel(output_path)}`",
        f"- Time elapsed: {elapsed:.3f} s",
        f"- Python {sys.version.split()[0]}, pandas {pd.__version__}",
        "",
        "## Description",
        "Listed the distinct values that contain more than one whitespace-separated word. Hyphenated "
        "names count as one word, and a parenthesised suffix such as -(Ce) or (Y) belongs to the name.",
        "",
        "## Statistics",
        "| | count |",
        "|---|---:|",
        f"| Input: records | {len(stats['source'])} |",
        f"| Input: columns | {len(stats['source'].columns)} |",
        f"| Input: distinct values | {stats['source'][stats['column']].str.strip().nunique()} |",
        f"| Input: records with one word | {(counts == 1).sum()} |",
        f"| Input: records with more than one word | {(counts > 1).sum()} |",
        f"| Output: distinct compound values | {len(result)} |",
        "",
        "| words | distinct values |",
        "|---:|---:|",
    ]
    lines += [f"| {n} | {c} |" for n, c in result["word_count"].value_counts().sort_index().items()]

    report_path = output_path.parent / "reports" / f"{output_path.stem}_report.md"
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--column", help="column to check (default: first column)")
    args = parser.parse_args()

    started = datetime.now()
    timer = time.perf_counter()
    stats = transform(args.input, args.output, args.column)
    elapsed = time.perf_counter() - timer
    report_path = write_report(args.input, args.output, stats, started, elapsed)

    print(f"Wrote {len(stats['result'])} compound values to {args.output}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
