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
| **Datasets** | [`wiki/datasets/`](wiki/datasets/) | Concept-wise curated datasets (e.g. `speech_datasets.md`, `translation_datasets.md`, `sentiment_datasets.md`). |
| **Research Papers** | [`wiki/papers/`](wiki/papers/) | Concept-wise curated research literature & bibliography (e.g. `speech_papers.md`, `translation_papers.md`). |
| **Models** | [`wiki/models/`](wiki/models/) | Significant pre-trained architectures, checkpoints, and embeddings (e.g. `nepalibert.md`, `nepberta.md`). |
| **Concepts** | [`wiki/concepts/`](wiki/concepts/) | Core NLP concepts, linguistics, tokenization, morphology, and task definitions. |
| **Institutions** | [`wiki/institutions/`](wiki/institutions/) | Labs, academic centers, and organizations driving Nepali NLP (e.g. ILPRL, NAAMII). |
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
