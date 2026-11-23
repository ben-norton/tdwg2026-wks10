"""Extract mineral names and their English glosses from a Wiktionary "<lang>:Minerals" category.

Implements docs/transformations/wiktionary_minerals_extraction.md.

Steps:
    1. List every page in Category:<code>:Minerals (English Wiktionary API).
    2. Fetch each page's wikitext and keep the section for the language (e.g. ==French==).
    3. Read the English name from the definition lines, labelled mineral/mineralogy/geology/
       gemstone/rock lines first. A line counts only if it starts with a link to the English term
       (prose definitions such as "any mineral containing silver" are skipped). A line that is
       {{synonym of|<code>|X}} or {{l|<code>|X}} takes the English name of X. OVERRIDES wins.
    4. Write <code>_mineral_name, en_mineral_name, wikidata_uri (the entry URL with a #<Language>
       anchor), sorted by name.

Output: data/authorities/mineral_names/<code>_minerals_wikidata.csv
        data/authorities/mineral_names/reports/<code>_minerals_wikidata_report.md

Usage:
    python src/extract/wiktionary_minerals.py --lang-code fr --lang-name French [--output PATH]
"""

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "data" / "authorities" / "mineral_names"
SPECIFICATION = "docs/transformations/wiktionary_minerals_extraction.md"

API = "https://en.wiktionary.org/w/api.php"
USER_AGENT = "tdwg2026-wks10/0.1 (https://github.com/ben-norton/tdwg2026-wks10)"
BATCH = 50

PREFERRED_LABELS = re.compile(r"\{\{(?:lb|lbl|label|tlb)\|[a-z-]+\|[^}]*\b(mineral|mineralogy|geology|gemstone|gemstones|rock|rocks|petrology)\b")
# A definition that starts with [[term]], [[term|shown]], [[#English|term]] or {{l|en|term}}
LEADING_LINK = re.compile(r"^\[\[(?:([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?|#[^\]|]*\|([^\]]+))\]\]|^\{\{l\|en\|([^}|]+)")
# A definition that points to another entry in the same language
SYNONYM = re.compile(r"^\{\{(?:synonym of|syn of|alternative form of|alt form|l)\|(?P<code>[a-z-]+)\|(?P<target>[^}|]+)")
# Senses where the first leading link is not the mineral name; checked by hand
OVERRIDES = {
    ("fr", "écume de mer"): "meerschaum",  # first sense is 'seafoam'; the mineral sense is the second
    ("fr", "pyrite"): "pyrite",  # 'the metallic mineral {{l|en|pyrite}}'; target of xanthopyrite
}


def api(params):
    params = {**params, "format": "json", "formatversion": "2"}
    request = urllib.request.Request(f"{API}?{urllib.parse.urlencode(params)}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def category_members(code):
    titles, params = [], {"action": "query", "list": "categorymembers", "cmtitle": f"Category:{code}:Minerals",
                          "cmlimit": "500", "cmtype": "page", "cmnamespace": "0"}
    while True:
        data = api(params)
        titles += [m["title"] for m in data["query"]["categorymembers"]]
        if "continue" not in data:
            return titles
        params.update(data["continue"])


def wikitexts(titles):
    texts = {}
    for i in range(0, len(titles), BATCH):
        data = api({"action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main",
                    "titles": "|".join(titles[i:i + BATCH])})
        for page in data["query"]["pages"]:
            revisions = page.get("revisions")
            texts[page["title"]] = revisions[0]["slots"]["main"]["content"] if revisions else ""
        time.sleep(0.5)
    return texts


def language_section(text, lang_name):
    match = re.search(rf"^=={re.escape(lang_name)}==\s*$", text, re.M)
    if not match:
        return ""
    end = re.search(r"^==[^=].*==\s*$", text[match.end():], re.M)
    return text[match.end():match.end() + end.start()] if end else text[match.end():]


def english_gloss(section, code):
    """Return (gloss, synonym target, definition line) from the preferred definition line."""
    senses = [line for line in section.splitlines() if re.match(r"^#(?![:*#])", line)]
    ordered = [s for s in senses if PREFERRED_LABELS.search(s)] + senses
    for sense in ordered:
        body = re.sub(r"\{\{(?:lb|lbl|label|tlb|q|qualifier|gloss|sense|C|c|cat|topics|top)\|[^}]*\}\}", "", sense[1:]).strip()
        link = LEADING_LINK.match(body)
        if link:
            return next(g for g in link.groups() if g).strip(), "", sense
        synonym = SYNONYM.match(body)
        if synonym and synonym["code"] == code:
            return "", synonym["target"].strip(), sense
    return "", "", ordered[0] if ordered else ""


def sort_key(name):
    decomposed = unicodedata.normalize("NFKD", name)
    return "".join(c for c in decomposed if not unicodedata.combining(c)).casefold()


def extract(code, lang_name):
    titles = category_members(code)
    texts = wikitexts(titles)
    parsed = {t: english_gloss(language_section(texts.get(t, ""), lang_name), code) for t in titles}

    # Synonym targets outside the category are fetched once
    outside = sorted({target for _, target, _ in parsed.values() if target and target not in parsed})
    for title, text in wikitexts(outside).items():
        parsed[title] = english_gloss(language_section(text, lang_name), code)

    # Overrides apply to category pages and synonym targets alike
    overridden = []
    for (lang, title), gloss in OVERRIDES.items():
        if lang == code and title in parsed:
            parsed[title] = (gloss, "", parsed[title][2])
            overridden.append((title, gloss))

    rows, missing, synonyms = [], [], []
    for title in titles:
        gloss, target, sense = parsed[title]
        if target:
            gloss = parsed.get(target, ("", "", ""))[0] if target != title else ""
            synonyms.append((title, target, gloss))
        if not gloss:
            missing.append((title, sense))
        rows.append({
            f"{code}_mineral_name": title,
            "en_mineral_name": gloss[:1].upper() + gloss[1:],
            "wikidata_uri": f"https://en.wiktionary.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}#{lang_name}",
        })
    result = pd.DataFrame(rows)
    result = result.iloc[sorted(range(len(result)), key=lambda i: sort_key(result.iat[i, 0]))]
    return {"titles": titles, "result": result.reset_index(drop=True), "missing": missing,
            "synonyms": synonyms, "overridden": overridden}


def write_report(output_path, code, lang_name, stats, started, elapsed):
    result = stats["result"]
    same = (result[f"{code}_mineral_name"].str.casefold() == result["en_mineral_name"].str.casefold()).sum()

    def rel(path):
        return path.resolve().relative_to(REPO_ROOT).as_posix()

    lines = [
        f"# {output_path.stem} extraction report",
        f"> {started:%Y-%m-%d %H:%M:%S}",
        "",
        "## Provenance",
        f"- Script: `{rel(Path(__file__))}`",
        f"- Command: `python {' '.join(sys.argv)}`",
        f"- Specification: `{SPECIFICATION}`",
        f"- Input: https://en.wiktionary.org/wiki/Category:{code}:Minerals (MediaWiki API, retrieved {started:%Y-%m-%d})",
        f"- Output: `{rel(output_path)}`",
        f"- Time elapsed: {elapsed:.1f} s",
        f"- Python {sys.version.split()[0]}, pandas {pd.__version__}",
        "",
        "## Description",
        f"Listed the pages in Category:{code}:Minerals, read the =={lang_name}== section of each, and took the "
        "English term that begins the first mineral/geology definition (or the first definition), "
        "following 'synonym of' links to the target entry.",
        "",
        "## Statistics",
        "| | count |",
        "|---|---:|",
        f"| Input: category pages | {len(stats['titles'])} |",
        f"| Output: records | {len(result)} |",
        f"| Output: columns | {len(result.columns)} |",
        f"| Output: records with an English name | {(result['en_mineral_name'] != '').sum()} |",
        f"| Output: records without an English name | {len(stats['missing'])} |",
        f"| Output: English name taken from a synonym | {sum(1 for *_, g in stats['synonyms'] if g)} |",
        f"| Output: English name set by override | {len(stats['overridden'])} |",
        f"| Output: English name equals {lang_name} name (ignoring case) | {same} |",
        f"| Output: duplicate {code}_mineral_name values | {result[f'{code}_mineral_name'].duplicated().sum()} |",
        "",
        "## Records without an English name",
    ]
    lines += [f"- {title}: `{sense or 'no definition line'}`" for title, sense in stats["missing"]] or ["None."]
    lines += ["", "## English names taken from a synonym", "| name | synonym of | en_mineral_name |", "|---|---|---|"]
    lines += [f"| {title} | {target} | {gloss} |" for title, target, gloss in stats["synonyms"]]
    lines += ["", "## Overrides"]
    lines += [f"- {title} → {gloss}" for title, gloss in stats["overridden"]] or ["None."]

    report_path = output_path.parent / "reports" / f"{output_path.stem}_report.md"
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--lang-code", required=True, help="Wiktionary language code, e.g. fr")
    parser.add_argument("--lang-name", required=True, help="Language section heading, e.g. French")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = args.output or OUTPUT_DIR / f"{args.lang_code}_minerals_wikidata.csv"

    started = datetime.now()
    timer = time.perf_counter()
    stats = extract(args.lang_code, args.lang_name)
    output.parent.mkdir(parents=True, exist_ok=True)
    stats["result"].to_csv(output, index=False, encoding="utf-8")
    elapsed = time.perf_counter() - timer
    report_path = write_report(output, args.lang_code, args.lang_name, stats, started, elapsed)

    print(f"Wrote {len(stats['result'])} rows to {output}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
