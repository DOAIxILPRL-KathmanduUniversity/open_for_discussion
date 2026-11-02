---
okf_version: "0.2"
type: "dataset"
title: "Nepali Text Summarization Datasets"
description: "Curated collection of article-summary pairs for abstractive and extractive summarization in the Nepali language."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
modality: "text"
task: "summarization"
language:
  - "ne"
script: "Devanagari"
tags:
  - summarization
  - generation
  - abstractive
---

# Nepali Text Summarization Datasets

## Overview
Summarization benchmarks pair complete Nepali news or encyclopedic articles with human-written or editorially condensed reference summaries, evaluating sequence-to-sequence model capabilities (such as mT5, BART, or fine-tuned LLMs).

## Curated Datasets

| Dataset | Type | Source & Scope |
| :--- | :--- | :--- |
| **XL-Sum (Nepali Sub-corpus)** | Abstractive | Sourced from BBC Nepali news articles; released as part of the ACL 2021 44-language multilingual abstractive summarization benchmark. Available on [GitHub: csebuetnlp/xl-sum](https://github.com/csebuetnlp/xl-sum). |
| **NEPHEAD News-Headline Corpus** | Headline Generation / Abstractive | 261,101 filtered article-headline pairs derived from the NepBERTa news crawl for extreme summarization and headline prediction in Devanagari script. Available on [Hugging Face: dsunil](https://huggingface.co/datasets/dsunil/NEPHEAD). |
| **Dhakal Nepali News Summarization Dataset** | Extractive / Lead | 50,000+ national news articles paired with editorial headlines and lead synopsis paragraphs. Available on [Kaggle: dhakal2444](https://www.kaggle.com/datasets/dhakal2444/nepali-news-dataset). |
| **ICISCT 2025 Nepali Abstractive News Benchmark** | Abstractive | Benchmarked corpus evaluating mT5, Gemma, and LLaMA fine-tuning on domain-specific Nepali governance and economic reporting. Documented in [IEEE ICISCT](https://doi.org/10.1109/icisct68600.2025.11441581). |
| **Nepali News Headline & Summary Corpus** | Headline / Lead Paragraph | Curated article-lead and article-headline pairs gathered from major Nepali digital publications for sequence-to-sequence training. |
| **Sarry971 Text Summarizer Corpus** | Extractive / Graph | Graph-based and transformer-assisted summarization dataset for Nepali news. Available on [GitHub](https://github.com/sarry971/Nepali-Text-Summarizer-). |

## Interconnected Graph Nodes
- **Datasets**: [Monolingual Text Datasets](wiki/datasets/monolingual_text_datasets.md)
- **Institutions**: [ILPRL](wiki/institutions/ilprl.md)

