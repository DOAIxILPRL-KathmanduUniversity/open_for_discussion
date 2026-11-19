#!/usr/bin/env python3
"""Progress report for the Nepali→English parallel corpus."""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

DIR = Path(__file__).resolve().parent

rows = list(csv.DictReader((DIR / "manifest.csv").open(encoding="utf-8")))
done = [r for r in rows if (DIR / r["json_file"]).exists()]

per_source = Counter(r["source"] for r in rows)
done_source = Counter(r["source"] for r in done)
flavours = Counter(r["informal_flavour"] for r in done)
words = 0
for r in done:
    d = json.loads((DIR / r["json_file"]).read_text(encoding="utf-8"))
    words += len(d["american_english"].split())

print(f"papers eligible : {len(rows)}")
print(f"papers translated: {len(done)}")
print(f"remaining        : {len(rows) - len(done)}")
print(f"English words    : ~{words:,} (US variants only)")
print("\nby source:")
for source, n in per_source.most_common():
    print(f"  {source:20} {done_source[source]:4}/{n}")
print("\ninformal flavours used:")
for flavour, n in flavours.most_common():
    print(f"  {flavour:22} {n}")
