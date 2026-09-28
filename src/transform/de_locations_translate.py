"""Translate German countries, first order divisions, and second order divisions to English.

Adds a third column 'location_en' to de_locations_01.csv and saves as de_locations_02.csv.
Named places are left blank/empty in location_en.

Input:  data/output/de_locations/de_locations_01.csv
Output: data/output/de_locations/de_locations_02.csv
        data/output/de_locations/de_locations_02_report.md

Usage:
    python src/transform/de_locations_translate.py [--input PATH] [--output PATH]
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"
OUTPUT_DIR = DATA_DIR / "output" / "de_locations"

DEFAULT_INPUT = OUTPUT_DIR / "de_locations_01.csv"
DEFAULT_OUTPUT = OUTPUT_DIR / "de_locations_02.csv"

# Translation mappings for German language countries, first order divisions,
# and second order divisions (exonyms, descriptors, and parenthetical notes).
TRANSLATIONS = {
    # Countries
    "France (Kolonie)": "France (Colony)",
    "Germany (5330.4/3402.6 Koord.dt.)": "Germany (5330.4/3402.6 German coord.)",
    "Germany (5334.9/3396.6 Koord.dt.)": "Germany (5334.9/3396.6 German coord.)",
    "Germany (5335.5/3396.0 Koord.dt.)": "Germany (5335.5/3396.0 German coord.)",
    "Guinea (französisch)": "Guinea (French)",
    "Italy (432.8/5093.1 Koord.it.)": "Italy (432.8/5093.1 Italian coord.)",
    "Italy (440.3/5103.7 Koord.it.)": "Italy (440.3/5103.7 Italian coord.)",
    "Italy (445.5/5102.5 Koord.it.)": "Italy (445.5/5102.5 Italian coord.)",
    "Italy (588.9/5145.1 Koord.it.)": "Italy (588.9/5145.1 Italian coord.)",
    "Italy (589.55/5143.4 Koord.it.)": "Italy (589.55/5143.4 Italian coord.)",
    "Italy (597.7/5143.6 Koord.it.)": "Italy (597.7/5143.6 Italian coord.)",
    "Italy (603.4/5139.2 Koord.it.)": "Italy (603.4/5139.2 Italian coord.)",
    "Italy (603.4/5140.0 Koord.it.)": "Italy (603.4/5140.0 Italian coord.)",
    "Italy (604.1/5146.1 Koord.it.)": "Italy (604.1/5146.1 Italian coord.)",
    "Italy (604.21/5143.85 Koord.it.)": "Italy (604.21/5143.85 Italian coord.)",
    "Italy (605.5/5148.4 Koord.it.)": "Italy (605.5/5148.4 Italian coord.)",
    "Italy (eher Boarezzo)": "Italy (rather Boarezzo)",
    "Namibia (Fund 1984)": "Namibia (Found 1984)",
    "Switzerland (italienische Seite)": "Switzerland (Italian side)",
    "Switzerland (Kalkalpen!)": "Switzerland (Limestone Alps!)",
    "Switzerland (oder Afrika)": "Switzerland (or Africa)",
    "Switzerland (oder Kienberg abklären!!)": "Switzerland (or check Kienberg!!)",
    "Zimbabwe (Rhodesien)": "Zimbabwe (Rhodesia)",

    # First Order Divisions
    "Ararat (Gipfel)": "Ararat (Peak)",
    "Basel-Landschaft": "Basel-Country",
    "Basel-Stadt": "Basel-City",
    "Cluj (Klausenberg)": "Cluj (Klausenburg)",
    "Corse (Korsika)": "Corsica (Corsica)",
    "Jura (Gebirge)": "Jura (Mountains)",
    "Karlovy Vary (Karlsbad)": "Karlovy Vary (Carlsbad)",
    "Kärnten": "Carinthia",
    "Liège (Lüttich)": "Liège (Liege)",
    "Maramures (Komitat Maramaros)": "Maramures (Maramaros County)",
    "Niederösterreich": "Lower Austria",
    "Nouvelle-Calédonie (Neukaledonien/SW-Pazifik)": "New Caledonia (New Caledonia/SW Pacific)",
    "Steiermark": "Styria",
    "Tirol": "Tyrol",
    "Tirol (Italy od. Austria)": "Tyrol (Italy or Austria)",
    "Zürich": "Zurich",
    "uri": "Uri",

    # Second Order Divisions
    "(angeblich Hungary) Franklin": "(allegedly Hungary) Franklin",
    "Bodensee": "Lake Constance",
    "Braunschweig": "Brunswick",
    "Konstanz": "Constance",
    "Lake Superior (Canada od. USA)": "Lake Superior (Canada or USA)",
    "München": "Munich",
    "Nürnberg": "Nuremberg",
    "Südliche Weinstrasse": "Southern Wine Route",
    "Wunsiedel im Fichtelgebirge": "Wunsiedel in the Fichtel Mountains",
}


def translate_location(location, rank):
    """Translate German countries, FODs, and SODs, leaving namedPlace blank."""
    if rank == "namedPlace":
        return ""
    return TRANSLATIONS.get(location, location)


def transform(input_path, output_path):
    source = pd.read_csv(input_path, dtype=str, keep_default_na=False)
    source_rows = len(source)

    # Add location_en column
    source["location_en"] = [
        translate_location(loc, rank)
        for loc, rank in zip(source["location"], source["division_rank"])
    ]

    # Save to output CSV
    output_path.parent.mkdir(parents=True, exist_ok=True)
    source.to_csv(output_path, index=False, encoding="utf-8")

    # Collect statistics
    translated_mask = (source["division_rank"] != "namedPlace") & (
        source["location"] != source["location_en"]
    )
    translated_df = source[translated_mask]

    return {
        "source_rows": source_rows,
        "translated_rows": len(translated_df),
        "translated_df": translated_df,
        "result": source,
    }


def write_report(input_path, output_path, stats, started):
    result = stats["result"]
    translated_df = stats["translated_df"]

    rank_counts = result["division_rank"].value_counts()
    populated_counts = result[result["location_en"] != ""]["division_rank"].value_counts()
    translated_counts = translated_df["division_rank"].value_counts()

    # Distinct translations table
    unique_translations = (
        translated_df.groupby(["division_rank", "location", "location_en"])
        .size()
        .reset_index(name="count")
        .sort_values(by=["division_rank", "count"], ascending=[True, False])
    )

    def rel(path):
        return path.resolve().relative_to(REPO_ROOT).as_posix()

    lines = [
        "# de_locations_02 translation report",
        f"> {started:%Y-%m-%d %H:%M:%S}",
        "",
        "## Provenance",
        f"- Script: `{rel(Path(__file__))}`",
        f"- Command: `python {' '.join(sys.argv)}`",
        f"- Specification: `docs/transformations/de_locations_transformations.md`",
        f"- Input: `{rel(input_path)}`",
        f"- Output: `{rel(output_path)}`",
        f"- Python {sys.version.split()[0]}, pandas {pd.__version__}",
        "",
        "## Summary",
        f"- Total rows: {stats['source_rows']}",
        f"- Geopolitical division rows populated in `location_en`: {stats['source_rows'] - (result['location_en'] == '').sum()}",
        f"- Named places left blank in `location_en`: {(result['location_en'] == '').sum()}",
        f"- Total rows translated from German: {stats['translated_rows']}",
        f"- Distinct translation mappings applied: {len(unique_translations)}",
        "",
        "| division_rank | total rows | populated in location_en | translated from German |",
        "|---|---:|---:|---:|",
    ]
    for rank in ["Country", "First Order Division", "Second Order Division", "namedPlace"]:
        total = rank_counts.get(rank, 0)
        pop = populated_counts.get(rank, 0)
        trans = translated_counts.get(rank, 0)
        lines.append(f"| {rank} | {total} | {pop} | {trans} |")

    lines += [
        "",
        "## Translated Entities",
        "| division_rank | location (German / original) | location_en (English) | occurrences |",
        "|---|---|---|---:|",
    ]
    for _, row in unique_translations.iterrows():
        lines.append(
            f"| {row['division_rank']} | {row['location']} | {row['location_en']} | {row['count']} |"
        )

    lines.append("")
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

    print(f"Wrote {stats['source_rows']} rows to {args.output}")
    print(f"Translated {stats['translated_rows']} rows across {len(stats['translated_df'].drop_duplicates(['location']))} unique entities")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
