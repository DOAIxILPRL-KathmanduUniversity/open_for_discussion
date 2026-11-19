#!/usr/bin/env python3
"""
Build nepali_papers/abstract.csv: all Devanagari (Nepali-language) articles
from every harvested source, with abstracts where available.

NepJOL's initial harvest dropped abstracts, so they are backfilled from the
NepJOL OAI-PMH endpoint and cached in .nepjol_abstract_cache.jsonl (resumable).
https://huggingface.co/datasets/DOAIxILPRL-KU/OCR_Planned_Evaluation/tree/main has the the queue to make suitably
"""
import csv
import html
import json
import os
import re
import sys
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

DIR = Path(__file__).resolve().parent
ROOT = DIR.parent
OUT = DIR / "abstract.csv"
CACHE = DIR / ".nepjol_abstract_cache.jsonl"

DEV = re.compile(r"[\u0900-\u097F]")
TAG = re.compile(r"<[^>]+>")

SOURCES = [
    ("NepJOL", ROOT / "nepjol/articles.jsonl"),
    ("TUCL eLibrary", ROOT / "tucl_elibrary/articles.jsonl"),
    ("MUCL DSpace", ROOT / "mucl_dspace/articles.jsonl"),
    ("NCIT Journal", ROOT / "ncit_journal/articles.jsonl"),
    ("IOEGC Conference", ROOT / "ioegc_conference/articles.jsonl"),
    ("Jagriti Journal", ROOT / "jagriti_journal/articles.jsonl"),
    ("Curated NLP papers", ROOT / "curated_nlp_papers.jsonl"),
]

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; research metadata harvester)"}
WORKERS = 8
TIMEOUT = 30


def is_nepali(rec):
    return bool(DEV.search(rec.get("title") or "") or DEV.search(rec.get("abstract") or ""))


def load_cache():
    cache = {}
    if CACHE.exists():
        for line in CACHE.open(encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            cache[r["oai_id"]] = r.get("abstract")
    return cache


def fetch_abstract(rec):
    """Return (oai_id, abstract_or_None) for one NepJOL record."""
    oai_id = rec["oai_id"]
    url = (
        f"https://www.nepjol.info/index.php/{rec['journal_path']}/oai"
        f"?verb=GetRecord&metadataPrefix=oai_dc&identifier={oai_id}"
    )
    for attempt in range(4):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            if resp.status_code == 200:
                break
            time.sleep(2 * (attempt + 1))
        except Exception:
            time.sleep(2 * (attempt + 1))
    else:
        return oai_id, None

    descriptions = []
    for raw in re.findall(r"<dc:description[^>]*>(.*?)</dc:description>", resp.text, re.S):
        text = html.unescape(TAG.sub(" ", raw)).strip()
        text = re.sub(r"\s+", " ", text)
        if text and "available in full text" not in text.lower():
            descriptions.append(text)
    abstract = max(descriptions, key=len) if descriptions else None
    if abstract and len(abstract) < 80:  # too short to be an abstract
        abstract = None
    return oai_id, abstract


def backfill_nepjol(records, cache):
    todo = [r for r in records if r["oai_id"] not in cache]
    if not todo:
        print(f"[cache] all {len(records)} NepJOL records already cached", flush=True)
        return cache

    print(f"[backfill] fetching abstracts for {len(todo)} NepJOL articles "
          f"({len(records) - len(todo)} cached)", flush=True)
    started = time.time()
    done = 0
    with CACHE.open("a", encoding="utf-8") as cache_file, \
            ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(fetch_abstract, r): r for r in todo}
        for fut in as_completed(futures):
            oai_id, abstract = fut.result()
            cache[oai_id] = abstract
            cache_file.write(json.dumps({"oai_id": oai_id, "abstract": abstract},
                                        ensure_ascii=False) + "\n")
            done += 1
            if done % 100 == 0 or done == len(todo):
                cache_file.flush()
                rate = done / max(time.time() - started, 1)
                eta = (len(todo) - done) / max(rate, 0.01)
                print(f"  {done}/{len(todo)}  {rate:.1f}/s  eta {eta/60:.1f} min",
                      flush=True)
    return cache


def norm_title(title):
    title = unicodedata.normalize("NFKC", title or "").lower()
    return re.sub(r"[^\w\u0900-\u097F]+", "", title)


def collect(cache):
    rows, seen, stats = [], set(), {}
    for source, path in SOURCES:
        if not path.exists():
            continue
        matched = kept = 0
        for line in path.open(encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if not is_nepali(rec):
                continue
            matched += 1

            title = (rec.get("title") or "").strip()
            abstract = (rec.get("abstract") or "").strip()
            if source == "NepJOL":
                abstract = (cache.get(rec.get("oai_id")) or abstract).strip()

            doi = (rec.get("doi") or "").strip()
            url = (rec.get("url") or "").strip()
            rid = (rec.get("id") or rec.get("oai_id") or url or doi or title).strip()

            keys = []
            if doi:
                keys.append("doi:" + doi.lower())
            if url:
                keys.append("url:" + url.rstrip("/").lower())
            if title:
                keys.append("t:" + norm_title(title))
            if any(k in seen for k in keys):
                continue
            seen.update(keys)
            kept += 1

            authors = rec.get("authors") or []
            if isinstance(authors, str):
                authors = [authors]
            rows.append({
                "source": source,
                "id": rid,
                "title": title,
                "authors": "; ".join(a.strip() for a in authors if a and a.strip()),
                "date": (rec.get("date") or rec.get("published") or "").strip(),
                "doi": doi,
                "url": url,
                "abstract": abstract,
                "has_abstract": "yes" if abstract else "no",
            })
        stats[source] = (matched, kept)

    rows.sort(key=lambda r: (r["source"], r["date"] or "", r["title"]))
    return rows, stats


def write_csv(rows):
    cols = ["source", "id", "title", "authors", "date", "doi", "url",
            "abstract", "has_abstract"]
    with OUT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)


def main():
    cache = load_cache()

    nepjol = []
    for line in (ROOT / "nepjol/articles.jsonl").open(encoding="utf-8"):
        rec = json.loads(line)
        if is_nepali(rec):
            nepjol.append(rec)
    cache = backfill_nepjol(nepjol, cache)

    rows, stats = collect(cache)
    write_csv(rows)

    print(f"\n[written] {OUT}  ({OUT.stat().st_size/1e6:.1f} MB)")
    print(f"[rows] {len(rows)}")
    for source, (matched, kept) in stats.items():
        print(f"  {source:20} matched {matched:5}  kept {kept:5}")
    with_abs = sum(1 for r in rows if r["abstract"])
    print(f"[abstracts] {with_abs}/{len(rows)} ({with_abs/len(rows)*100:.1f}%)")


if __name__ == "__main__":
    main()
