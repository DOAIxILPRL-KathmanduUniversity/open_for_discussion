#!/usr/bin/env python3
"""Validate every finished translation JSON against the harvested source."""
import csv
import difflib
import json
import re
import sys
from collections import Counter
from pathlib import Path

DIR = Path(__file__).resolve().parent
ROOT = DIR.parent
DEV = re.compile(r"[\u0900-\u097F]")
FIELDS = ("american_english", "british_english", "australian_english", "informal_english")


def main():
    sources = {r["title"]: r for r in
               csv.DictReader((ROOT / "abstract.csv").open(encoding="utf-8-sig"))}
    manifest = {m["paper_id"]: m for m in
                csv.DictReader((DIR / "manifest.csv").open(encoding="utf-8"))}

    files = sorted(p for p in DIR.glob("*.json"))
    problems = []
    flavours = Counter()
    for path in files:
        d = json.loads(path.read_text(encoding="utf-8"))
        pid = d.get("paper_id", path.stem)
        m = manifest.get(pid, {})
        src = sources.get(d.get("title", ""), {})

        if not src:
            problems.append(f"{pid}: title not found in abstract.csv")
            continue
        if d["nepali"] != src["abstract"]:
            problems.append(f"{pid}: nepali text is not byte-identical to source")
        for field in FIELDS:
            if not (d.get(field) or "").strip():
                problems.append(f"{pid}: empty {field}")
        if d.get("informal_flavour") != m.get("informal_flavour"):
            problems.append(f"{pid}: flavour mismatch "
                            f"({d.get('informal_flavour')} vs {m.get('informal_flavour')})")
        flavours[d.get("informal_flavour")] += 1

        us, uk, au = (d.get("american_english", ""), d.get("british_english", ""),
                      d.get("australian_english", ""))
        if us and uk:
            r = difflib.SequenceMatcher(None, us, uk).ratio()
            if r < 0.30:
                problems.append(f"{pid}: US/UK low lexical overlap {r:.2f} (check)")
        # Devanagari leakage (allow some names)
        for field in FIELDS:
            dev = len(DEV.findall(d.get(field, "")))
            if dev > 12:
                problems.append(f"{pid}: {field} has {dev} Devanagari chars")

    print(f"[check] {len(files)} JSON files")
    print(f"[flavours] {dict(flavours)}")
    if problems:
        print(f"[issues] {len(problems)}")
        for p in problems:
            print("  -", p)
        return 1
    print("[result] all files valid: schema, verbatim Nepali, four non-empty variants")
    return 0


if __name__ == "__main__":
    sys.exit(main())
