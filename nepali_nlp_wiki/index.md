---
okf_version: "0.2"
title: "Nepali NLP & Computational Linguistics Open Knowledge Wiki"
description: "Structured, compounding knowledge graph of Nepali NLP models, corpora, benchmarks, scripts, and research institutions following Google Open Knowledge Format (OKF) and Karpathy's LLM-wiki paradigm."
type: "bundle"
version: "1.0.0"
timestamp: "2026-11-01T20:00:00Z"
status: "active"
tags:
  - nepali-nlp
  - low-resource-languages
  - open-knowledge-format
  - knowledge-graph
---

# Nepali NLP & Computational Linguistics Open Knowledge Wiki

Welcome to the **Nepali NLP Open Knowledge Wiki**, a compounding, entity-first research graph documenting models, datasets, benchmarks, and institutions in Nepali Natural Language Processing.

Structured according to Google's **Open Knowledge Format (OKF v0.2)** and inspired by **Andrej Karpathy's LLM Wiki pattern**, this repository treats the filesystem as a portable, self-documenting graph where every node is a validated Markdown document with YAML frontmatter.

---

## 🏛️ Knowledge Graph Sections

| Section | Directory | Description |
| :--- | :--- | :--- |
| **Datasets** | [`wiki/datasets/`](wiki/datasets/) | Annotated datasets, instruction pairs, translation parallel texts, and speech corpora. |
| **Research Papers** | [`wiki/papers/`](wiki/papers/) | Indexed academic papers (NepJOL, ACL, arXiv, KU repository) with citations and DOIs. |
| **Concepts** | [`wiki/concepts/`](wiki/concepts/) | Core linguistic and computational NLP principles (e.g. Devanagari Tokenization, Romanized Nepali, Stemming). |
| **Models** | [`wiki/models/`](wiki/models/) | Pretrained transformers, language models, ASR, TTS, and OCR architectures (e.g. NepaliBERT, NepBERTa). |
| **Corpora** | [`wiki/corpora/`](wiki/corpora/) | Monolingual, parallel, speech, and OCR datasets for low-resource Nepali NLP. |
| **Benchmarks** | [`wiki/benchmarks/`](wiki/benchmarks/) | Standardized evaluation suites, tasks, and leaderboards (e.g. Nep-gLUE, Nepali XNLI). |
| **Institutions** | [`wiki/institutions/`](wiki/institutions/) | Labs, academic centers, and organizations driving Nepali NLP (e.g. ILPRL, NAAMII, Language Technology Kendra). |
| **Sources** | [`wiki/sources/`](wiki/sources/) | Synthesis cards for referenced literature, journal articles, and conference proceedings. |
| **Raw Vault** | [`raw/`](raw/) | Immutable ingest directory for incoming source documents, PDFs, and notes. |

---

## 🛠️ CLI Operations & Tools

The repository includes a standalone Python CLI toolkit [`tools/wiki_cli.py`](tools/wiki_cli.py):

```bash
# Validate entire graph against OKF schema and check broken/orphan links
python3 tools/wiki_cli.py lint

# Synthesize and ingest a raw note/paper into structured OKF entities
python3 tools/wiki_cli.py ingest raw/sample_paper.txt

# Query the knowledge graph using keyword and semantic graph search
python3 tools/wiki_cli.py query "transformer language models"

# Rebuild the master graph summary and relationship matrix
python3 tools/wiki_cli.py index
```

See [`.agent`](.agent) for operational guidelines governing agent curation, schema validation, and synthesis workflows.
