"""Remove rows whose value appears in an exclusion list stored in src/config.

Implements the filter step in docs/transformations/de_mineral_names_transformations.md; works on
any dataset that follows the <dataset>_NN naming convention.

Steps:
    1. Read the target file and the exclusion list src/config/<--exclusion-list>. If the target's
       folder contains single_exclusions.csv, add its values too (a header row, then one value per
       row); if it does not exist, skip it.
    2. Match on the exclusion list's first column against the target column of the same name
       (or the target's first column if no column has that name). Values are compared exactly
       after trimming whitespace.
    3. Drop rows whose value matches a full-value exclusion (match = full, or no match column).
    4. Delete substring exclusions (match = substring; a regular expression) from the remaining
       values, in list order, then trim the ends. Rows left empty are dropped. This step only
       removes text; it never replaces, splits or reformats values.
    5. Drop duplicate values left by the exclusions: compared case-insensitively after trimming,
       first occurrence kept.
    6. Write <dataset>_<NN + 1>_filtered.<ext>.

Input:  data/output/de_mineral_names/de_mineral_names_01.csv
        src/config/de_mineral_names_exclusion_list.csv
Output: data/output/de_mineral_names/de_mineral_names_02_filtered.csv
        data/output/de_mineral_names/reports/de_mineral_names_02_filtered_report.md

Usage:
    python src/transform/filter_by_exclusion_list.py --exclusion-list FILENAME
        [--input PATH] [--output PATH] [--column NAME]

    FILENAME is the name of a file in src/config, e.g. de_mineral_names_exclusion_list.csv.
"""

import argparse
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = REPO_ROOT / "data" / "output" / "de_mineral_names" / "de_mineral_names_01.csv"
CONFIG_DIR = REPO_ROOT / "src" / "config"
SPECIFICATION = "docs/transformations/de_mineral_names_transformations.md"
SINGLE_EXCLUSIONS_NAME = "single_exclusions.csv"

STEP_NUMBER = re.compile(r"^(?P<base>.+)_(?P<step>\d{2})$")


def output_path_for(input_path):
    """de_mineral_names_01.csv -> de_mineral_names_02_filtered.csv"""
    match = STEP_NUMBER.match(input_path.stem)
    if not match:
        raise SystemExit(f"Input name must end in _NN (two digits): {input_path.name}")
    step = int(match["step"]) + 1
    return input_path.with_name(f"{match['base']}_{step:02d}_filtered{input_path.suffix}")


def exclusion_list_path(name):
    """Resolve a bare filename to src/config/<name>; list the available files if it is missing."""
    if Path(name).name != name:
        raise SystemExit(f"--exclusion-list takes a filename in {CONFIG_DIR}, not a path: {name}")
    path = CONFIG_DIR / name
    if not path.is_file():
        available = ", ".join(sorted(p.name for p in CONFIG_DIR.glob("*.csv"))) or "none"
        raise SystemExit(f"Exclusion list not found: {path}\nAvailable: {available}")
    return path


def read_table(path):
    sep = "\t" if path.suffix.lower() == ".tsv" else ","
    return pd.read_csv(path, sep=sep, dtype=str, keep_default_na=False, encoding="utf-8-sig")


def read_single_exclusions(path):
    """One value per row after a header row (any name); only the first column is read."""
    values = pd.read_csv(path, usecols=[0], dtype=str, keep_default_na=False, encoding="utf-8-sig")
    return set(values.iloc[:, 0].str.strip()) - {""}


def profile(df, column):
    values = df[column].str.strip()
    return {
        "records": len(df),
        "columns": len(df.columns),
        "unique": values.nunique(),
        "empty": int((values == "").sum()),
        "duplicates": int(values.duplicated().sum()),
    }


def transform(input_path, output_path, exclusion_path, column):
    # 1. Read the target and the exclusion list
    source = read_table(input_path)
    exclusions = read_table(exclusion_path)

    # 2. Choose the column to match and build the set of excluded values
    exclusion_column = exclusions.columns[0]
    if column is None:
        column = exclusion_column if exclusion_column in source.columns else source.columns[0]
    is_substring = (exclusions["match"].str.strip() == "substring") if "match" in exclusions else False
    listed = set(exclusions.loc[~is_substring, exclusion_column].str.strip()) - {""}
    substrings = list(exclusions.loc[is_substring, exclusion_column]) if "match" in exclusions else []

    # Optional single_exclusions.csv beside the target file
    single_path = input_path.parent / SINGLE_EXCLUSIONS_NAME
    single = read_single_exclusions(single_path) if single_path.is_file() else set()
    excluded = listed | single

    # 3. Drop rows matching a full-value exclusion
    values = source[column].str.strip()
    matched = values.isin(excluded)
    result = source[~matched].copy()

    # 4. Delete substring exclusions in list order; drop rows left empty
    before = result[column].copy()
    substring_counts = {}
    for pattern in substrings:
        substring_counts[pattern] = int(result[column].str.contains(pattern, regex=True).sum())
        result[column] = result[column].str.replace(pattern, "", regex=True)
    result[column] = result[column].str.strip()
    changed = result[column] != before.str.strip()
    substring_changes = pd.DataFrame({"before": before[changed], "after": result.loc[changed, column]})
    emptied = result[column] == ""
    result = result[~emptied]

    # 5. Drop duplicate values (case-insensitive, first occurrence kept)
    duplicated = result[column].str.casefold().duplicated()
    duplicates = result.loc[duplicated, column]
    result = result[~duplicated]

    sep = "\t" if output_path.suffix.lower() == ".tsv" else ","
    result.to_csv(output_path, sep=sep, index=False, encoding="utf-8-sig")

    return {
        "source": source,
        "result": result,
        "removed": source[matched],
        "substrings": substrings,
        "substring_counts": substring_counts,
        "substring_changes": substring_changes,
        "emptied": int(emptied.sum()),
        "duplicates": duplicates,
        "column": column,
        "exclusion_path": exclusion_path,
        "exclusion_count": len(listed),
        "listed": listed,
        "single_path": single_path,
        "single_found": single_path.is_file(),
        "single": single,
        "unmatched_exclusions": sorted(excluded - set(values), key=str.casefold),
    }


def write_report(input_path, output_path, stats, started, elapsed):
    column = stats["column"]
    before = profile(stats["source"], column)
    after = profile(stats["result"], column)

    def rel(path):
        path = path.resolve()
        return path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else path.as_posix()

    lines = [
        f"# {output_path.stem} filter report",
        f"> {started:%Y-%m-%d %H:%M:%S}",
        "",
        "## Provenance",
        f"- Script: `{rel(Path(__file__))}`",
        f"- Command: `python {' '.join(sys.argv)}`",
        f"- Specification: `{SPECIFICATION}`",
        f"- Input: `{rel(input_path)}`",
        f"- Exclusion list: `{rel(stats['exclusion_path'])}` ({stats['exclusion_count']} values)",
        f"- Single exclusions: `{rel(stats['single_path'])}` ({len(stats['single'])} values)"
        if stats["single_found"] else f"- Single exclusions: `{rel(stats['single_path'])}` not found, skipped",
        f"- Output: `{rel(output_path)}`",
        f"- Time elapsed: {elapsed:.3f} s",
        f"- Python {sys.version.split()[0]}, pandas {pd.__version__}",
        "",
        "## Description",
        f"Removed rows whose `{column}` value, trimmed, exactly matches a full-value exclusion or a value in "
        "single_exclusions.csv. Then deleted each substring exclusion from the remaining values, in list "
        "order, and dropped rows left empty. Finally dropped duplicate values (case-insensitive, first "
        "occurrence kept). No other change is made to values.",
        "",
        "## Statistics",
        "| | input | output |",
        "|---|---:|---:|",
        f"| Records | {before['records']} | {after['records']} |",
        f"| Columns | {before['columns']} | {after['columns']} |",
        f"| Unique values | {before['unique']} | {after['unique']} |",
        f"| Empty values | {before['empty']} | {after['empty']} |",
        f"| Duplicate values | {before['duplicates']} | {after['duplicates']} |",
        "",
        f"- Records removed: {len(stats['removed'])}",
        f"- Records removed by single exclusions only: "
        f"{stats['removed'][column].str.strip().isin(stats['single'] - stats['listed']).sum()}",
        f"- Exclusion values with no match in the input: {len(stats['unmatched_exclusions'])}",
        f"- Values changed by substring exclusions: {len(stats['substring_changes'])}",
        f"- Records dropped because substring exclusions left them empty: {stats['emptied']}",
        f"- Duplicate records dropped after exclusion: {len(stats['duplicates'])}",
        "",
        "## Removed values",
    ]
    single_only = stats["single"] - stats["listed"]
    lines += [f"- {value}" + (" (single_exclusions.csv)" if value.strip() in single_only else "")
              for value in stats["removed"][column]] or ["None."]
    if stats["substrings"]:
        lines += ["", "## Substring exclusions (applied in this order)", "| pattern | values affected |", "|---|---:|"]
        lines += [f"| `{pattern}` | {stats['substring_counts'][pattern]} |" for pattern in stats["substrings"]]
        lines += ["", "## Values changed by substring exclusions", "| before | after |", "|---|---|"]
        lines += [f"| {r.before} | {r.after} |" for r in stats["substring_changes"].itertuples()]
    if stats["unmatched_exclusions"]:
        lines += ["", "## Exclusion values not found in the input"]
        lines += [f"- {value}" for value in stats["unmatched_exclusions"]]

    report_path = output_path.parent / "reports" / f"{output_path.stem}_report.md"
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--exclusion-list", required=True, metavar="FILENAME",
        help=f"name of the exclusion list file in {CONFIG_DIR.relative_to(REPO_ROOT).as_posix()}",
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, help="default: <dataset>_<NN + 1>_filtered.<ext>")
    parser.add_argument("--column", help="target column to match (default: see Steps)")
    args = parser.parse_args()
    exclusion_path = exclusion_list_path(args.exclusion_list)
    output = args.output or output_path_for(args.input)

    started = datetime.now()
    timer = time.perf_counter()
    stats = transform(args.input, output, exclusion_path, args.column)
    elapsed = time.perf_counter() - timer
    report_path = write_report(args.input, output, stats, started, elapsed)

    print(f"Removed {len(stats['removed'])} rows; wrote {len(stats['result'])} rows to {output}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
