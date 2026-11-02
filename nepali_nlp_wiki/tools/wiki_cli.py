#!/usr/bin/env python3
"""
OKF v0.2 / LLM-Wiki CLI Tool
Provides linting, schema validation, link graph verification, querying,
and dataset/paper catalog importing for Open Knowledge Format (OKF) markdown knowledge bases.
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple

WIKI_ROOT = Path(__file__).resolve().parent.parent

# Recognized OKF node types
VALID_TYPES = {
    "bundle", "concept", "model", "dataset", "paper",
    "institution", "tool", "person", "pipeline"
}

REQUIRED_FRONTMATTER = ["type", "title", "description", "status", "version", "timestamp"]

def parse_frontmatter(file_path: Path) -> Tuple[Dict, str]:
    """Extract YAML frontmatter and markdown body from file."""
    content = file_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}, content
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    
    fm_str = parts[1]
    body = parts[2]
    
    try:
        import yaml
        data = yaml.safe_load(fm_str) or {}
    except Exception:
        # Fallback simple parser
        data = {}
        for line in fm_str.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                data[k.strip()] = v.strip().strip('"').strip("'")
    return data, body

def find_markdown_links(content: str) -> List[str]:
    """Find relative markdown links and standard wikilinks."""
    links = []
    # [Text](path/to/file.md)
    md_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for _, target in md_links:
        if not target.startswith(("http://", "https://", "#", "mailto:")):
            target = target.split("#")[0]
            if target:
                links.append(target)
    # Wikilinks [[target]]
    wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    for target in wikilinks:
        links.append(target.strip())
    return links

def cmd_lint(args) -> int:
    """Validate all OKF nodes in index.md and wiki/."""
    errors = []
    warnings = []
    files_checked = 0
    
    # 1. Check index.md
    index_file = WIKI_ROOT / "index.md"
    if not index_file.exists():
        errors.append("Missing root index.md")
    else:
        files_checked += 1
        fm, _ = parse_frontmatter(index_file)
        if fm.get("type") != "bundle":
            errors.append("index.md frontmatter 'type' must be 'bundle'")
    
    # 2. Collect all wiki nodes
    wiki_dir = WIKI_ROOT / "wiki"
    all_nodes: Dict[str, Path] = {}
    node_targets: Set[str] = set()

    for p in wiki_dir.rglob("*.md"):
        files_checked += 1
        rel = p.relative_to(WIKI_ROOT)
        all_nodes[str(rel)] = p
        node_targets.add(p.name)
        node_targets.add(p.stem)

    # 3. Validate each node
    for rel_path, file_path in all_nodes.items():
        fm, body = parse_frontmatter(file_path)
        
        for req in REQUIRED_FRONTMATTER:
            if req not in fm:
                errors.append(f"{rel_path}: Missing required frontmatter key '{req}'")
        
        node_type = fm.get("type")
        if node_type and node_type not in VALID_TYPES:
            warnings.append(f"{rel_path}: Non-standard node type '{node_type}'")
        
        links = find_markdown_links(body)
        for link in links:
            target_path = (file_path.parent / link).resolve()
            if not target_path.exists():
                stem_match = (link.endswith(".md") and link in node_targets) or (link in node_targets)
                if not stem_match and not (WIKI_ROOT / link).exists():
                    warnings.append(f"{rel_path}: Unresolved link '{link}'")

    print("=" * 60)
    print(f"OKF Wiki Linter Report: {files_checked} files inspected")
    print("=" * 60)
    
    if errors:
        print(f"\n❌ {len(errors)} ERRORS:")
        for err in errors:
            print(f"  - {err}")
    
    if warnings:
        print(f"\n⚠️  {len(warnings)} WARNINGS:")
        for warn in warnings:
            print(f"  - {warn}")
            
    if not errors and not warnings:
        print("\n✅ All OKF nodes conform to schema. No broken links detected.")
        return 0
    return 1 if errors else 0

def cmd_query(args) -> int:
    """Search wiki nodes by query string, type, or tags."""
    query = (args.query or "").lower()
    target_type = (args.type or "").lower()
    
    wiki_dir = WIKI_ROOT / "wiki"
    matches = []
    
    for p in sorted(wiki_dir.rglob("*.md")):
        fm, body = parse_frontmatter(p)
        node_type = str(fm.get("type", "")).lower()
        title = str(fm.get("title", p.stem))
        desc = str(fm.get("description", ""))
        tags = [str(t).lower() for t in fm.get("tags", [])] if isinstance(fm.get("tags"), list) else []
        
        if target_type and target_type != node_type:
            continue
            
        full_text = f"{title} {desc} {' '.join(tags)} {body}".lower()
        if not query or query in full_text:
            rel = p.relative_to(WIKI_ROOT)
            matches.append((rel, node_type, title, desc))
            
    print(f"Found {len(matches)} matching node(s):")
    for rel, ntype, title, desc in matches:
        print(f"\n• [{ntype.upper()}] {title}")
        print(f"  Path: {rel}")
        if desc:
            print(f"  Summary: {desc}")
    return 0

def cmd_stats(args) -> int:
    """Display graph node statistics by category."""
    wiki_dir = WIKI_ROOT / "wiki"
    counts = {}
    total_nodes = 0
    
    for p in wiki_dir.rglob("*.md"):
        fm, _ = parse_frontmatter(p)
        ntype = fm.get("type", "untyped")
        counts[ntype] = counts.get(ntype, 0) + 1
        total_nodes += 1
        
    print("=" * 40)
    print("Nepali NLP OKF Wiki Statistics")
    print("=" * 40)
    print(f"Total compiled nodes: {total_nodes}")
    for ntype, count in sorted(counts.items()):
        print(f"  - {ntype:15s}: {count}")
    return 0

def cmd_import_catalog(args) -> int:
    """Import datasets and papers from a JSONL catalog into OKF markdown nodes."""
    catalog_path = Path(args.catalog_file)
    if not catalog_path.exists():
        print(f"Error: Catalog file not found: {catalog_path}")
        return 1
        
    datasets_dir = WIKI_ROOT / "wiki" / "datasets"
    papers_dir = WIKI_ROOT / "wiki" / "papers"
    datasets_dir.mkdir(parents=True, exist_ok=True)
    papers_dir.mkdir(parents=True, exist_ok=True)
    
    count = 0
    with open(catalog_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entry = json.loads(line)
            
            # Case 1: Research Paper entry (NepJOL / Academic paper schema)
            if "doi" in entry or "journal_name" in entry or ("authors" in entry and "task" not in entry):
                title = entry.get("title", "Untitled Paper")
                clean_title = re.sub(r'[^a-zA-Z0-9_\-\s]', '', title).strip().replace(" ", "_").lower()[:50]
                slug = clean_title or f"paper_{entry.get('oai_id', 'unknown').split('/')[-1]}"
                out_path = papers_dir / f"{slug}.md"
                
                authors = entry.get("authors", [])
                date_val = entry.get("date") or "2026-01-01"
                journal = entry.get("journal_name") or "Academic Venue"
                url = entry.get("url") or ""
                doi = entry.get("doi") or ""
                
                authors_str = "\n".join([f'  - "{a}"' for a in authors]) if authors else '  - "Unknown Author"'
                iso_timestamp = f"{date_val}T00:00:00Z" if isinstance(date_val, str) and len(date_val) == 10 else "2026-01-01T00:00:00Z"
                
                md_content = f"""---
okf_version: "0.2"
type: "paper"
title: {json.dumps(title)}
description: {json.dumps(f"Research publication in {journal} ({date_val})")}
status: "active"
version: "1.0.0"
timestamp: "{iso_timestamp}"
authors:
{authors_str}
venue: {json.dumps(journal)}
doi: {json.dumps(doi)}
url: {json.dumps(url)}
tags:
  - nepali-nlp
  - research-paper
---

# {title}

## Summary
- **Venue**: {journal}
- **Date**: {date_val}
- **URL**: [{url}]({url})
- **DOI**: {doi}
"""
                out_path.write_text(md_content, encoding="utf-8")
                count += 1
                
            # Case 2: Dataset entry (catalog schema)
            elif "task" in entry or "modality" in entry or "num_samples" in entry or "max_rows" in entry:
                name = entry.get("name") or entry.get("id") or "dataset"
                slug = entry.get("id") or name.replace("/", "_").replace("-", "_").lower()
                slug = re.sub(r'[^a-zA-Z0-9_]', '', slug)
                out_path = datasets_dir / f"{slug}.md"
                
                task_tag = entry.get('task', 'task').split('/')[-1]
                md_content = f"""---
okf_version: "0.2"
type: "dataset"
title: {json.dumps(name)}
description: {json.dumps(f"Nepali dataset for {entry.get('task', 'nlp')} ({entry.get('modality', 'text')})")}
status: "active"
version: "1.0.0"
timestamp: "2026-11-01T00:00:00Z"
modality: {json.dumps(entry.get('modality', 'text'))}
task: {json.dumps(entry.get('task', 'general-nlp'))}
language:
  - {json.dumps(entry.get('language', 'ne'))}
script: {json.dumps(entry.get('script', 'Devanagari'))}
license: {json.dumps(entry.get('license', 'unknown'))}
num_samples: {entry.get('max_rows') or 0}
tags:
  - nepali-nlp
  - dataset
  - {task_tag}
---

# {name}

## Details
- **Task**: `{entry.get('task', 'N/A')}`
- **Modality**: `{entry.get('modality', 'text')}`
- **License**: `{entry.get('license', 'N/A')}`
- **Estimated Rows / Size**: `{entry.get('max_rows', 'N/A')}` samples
"""
                out_path.write_text(md_content, encoding="utf-8")
                count += 1
                
    print(f"Successfully imported {count} items into OKF wiki graph.")
    return 0

def cmd_import_catalog(args) -> int:
    """Import datasets and papers from a JSONL catalog into OKF markdown nodes."""
    catalog_path = Path(args.catalog_file)
    if not catalog_path.exists():
        print(f"Error: Catalog file not found: {catalog_path}")
        return 1
        
    datasets_dir = WIKI_ROOT / "wiki" / "datasets"
    papers_dir = WIKI_ROOT / "wiki" / "papers"
    datasets_dir.mkdir(parents=True, exist_ok=True)
    papers_dir.mkdir(parents=True, exist_ok=True)
    
    count = 0
    with open(catalog_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entry = json.loads(line)
            
            # Case 1: Research Paper entry (NepJOL / Academic paper schema)
            if "doi" in entry or "journal_name" in entry or ("authors" in entry and "task" not in entry):
                title = entry.get("title", "Untitled Paper")
                clean_title = re.sub(r'[^a-zA-Z0-9_\-\s]', '', title).strip().replace(" ", "_").lower()[:50]
                slug = clean_title or f"paper_{entry.get('oai_id', 'unknown').split('/')[-1]}"
                out_path = papers_dir / f"{slug}.md"
                
                authors = entry.get("authors", [])
                date_val = entry.get("date") or "2026-01-01"
                journal = entry.get("journal_name") or "Academic Venue"
                url = entry.get("url") or ""
                doi = entry.get("doi") or ""
                
                authors_str = "\n".join([f'  - "{a}"' for a in authors]) if authors else '  - "Unknown Author"'
                iso_timestamp = f"{date_val}T00:00:00Z" if isinstance(date_val, str) and len(date_val) == 10 else "2026-01-01T00:00:00Z"
                
                md_content = f"""---
okf_version: "0.2"
type: "paper"
title: {json.dumps(title)}
description: {json.dumps(f"Research publication in {journal} ({date_val})")}
status: "active"
version: "1.0.0"
timestamp: "{iso_timestamp}"
authors:
{authors_str}
venue: {json.dumps(journal)}
doi: {json.dumps(doi)}
url: {json.dumps(url)}
tags:
  - nepali-nlp
  - research-paper
---

# {title}

## Summary
- **Venue**: {journal}
- **Date**: {date_val}
- **URL**: [{url}]({url})
- **DOI**: {doi}
"""
                out_path.write_text(md_content, encoding="utf-8")
                count += 1
                
            # Case 2: Dataset entry (catalog schema)
            elif "task" in entry or "modality" in entry or "num_samples" in entry or "max_rows" in entry:
                name = entry.get("name") or entry.get("id") or "dataset"
                slug = entry.get("id") or name.replace("/", "_").replace("-", "_").lower()
                slug = re.sub(r'[^a-zA-Z0-9_]', '', slug)
                out_path = datasets_dir / f"{slug}.md"
                
                task_tag = entry.get('task', 'task').split('/')[-1]
                md_content = f"""---
okf_version: "0.2"
type: "dataset"
title: {json.dumps(name)}
description: {json.dumps(f"Nepali dataset for {entry.get('task', 'nlp')} ({entry.get('modality', 'text')})")}
status: "active"
version: "1.0.0"
timestamp: "2026-11-01T00:00:00Z"
modality: {json.dumps(entry.get('modality', 'text'))}
task: {json.dumps(entry.get('task', 'general-nlp'))}
language:
  - {json.dumps(entry.get('language', 'ne'))}
script: {json.dumps(entry.get('script', 'Devanagari'))}
license: {json.dumps(entry.get('license', 'unknown'))}
num_samples: {entry.get('max_rows') or 0}
tags:
  - nepali-nlp
  - dataset
  - {task_tag}
---

# {name}

## Details
- **Task**: `{entry.get('task', 'N/A')}`
- **Modality**: `{entry.get('modality', 'text')}`
- **License**: `{entry.get('license', 'N/A')}`
- **Estimated Rows / Size**: `{entry.get('max_rows', 'N/A')}` samples
"""
                out_path.write_text(md_content, encoding="utf-8")
                count += 1
                
    print(f"Successfully imported {count} items into OKF wiki graph.")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Nepali NLP OKF Wiki CLI Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # lint
    p_lint = subparsers.add_parser("lint", help="Lint wiki frontmatter and markdown links")
    p_lint.set_defaults(func=cmd_lint)
    
    # query
    p_query = subparsers.add_parser("query", help="Query nodes by keyword or type")
    p_query.add_argument("query", nargs="?", default="", help="Search query string")
    p_query.add_argument("--type", help="Filter by node type (concept, model, dataset, paper, etc.)")
    p_query.set_defaults(func=cmd_query)
    
    # stats
    p_stats = subparsers.add_parser("stats", help="Show wiki knowledge graph stats")
    p_stats.set_defaults(func=cmd_stats)
    
    # import-catalog
    p_import = subparsers.add_parser("import-catalog", help="Import papers or datasets from JSONL into OKF nodes")
    p_import.add_argument("catalog_file", help="Path to JSONL catalog file")
    p_import.set_defaults(func=cmd_import_catalog)
    
    args = parser.parse_args()
    sys.exit(args.func(args))

if __name__ == "__main__":
    main()
