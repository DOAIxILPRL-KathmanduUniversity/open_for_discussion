---
okf_version: "0.2"
type: "dataset"
title: "Dataset Title or Name"
description: "Concise summary of dataset purpose, composition, size, and source."
status: "active" # active | deprecated | draft
version: "1.0.0"
timestamp: "YYYY-MM-DDTHH:MM:SSZ"
modality: "text" # text | speech | audio | multimodal | parallel_text
task: "sentiment-analysis" # token-classification | translation | summarization | qa | etc.
language:
  - "ne" # ISO 639-1 code(s)
script: "Devanagari"
license: "CC-BY-4.0"
num_samples: 10000
source_url: "https://huggingface.co/datasets/..."
paper: "wiki/papers/paper_filename.md"
tags:
  - nepali-nlp
  - dataset
  - low-resource
---

# Dataset Name

## Overview
Detailed description of the dataset, origin, curation methodology, and domain.

## Schema & Format
- **Format**: JSONL / CSV / Parquet / CoNLL
- **Fields**:
  - `id`: unique record ID
  - `text`: Nepali utterance or document
  - `label`: annotated target

## Split & Statistics
- Train: X samples
- Validation: Y samples
- Test: Z samples

## Related Entities
- **Research Paper**: [Paper Title](wiki/papers/paper_filename.md)
- **Associated Models**: [Model Name](wiki/models/model_filename.md)
- **Institution / Authors**: [Institution](wiki/institutions/institution_filename.md)

