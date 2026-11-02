---
okf_version: "0.2"
type: "dataset"
title: "Nepali Named Entity Recognition (NER) Datasets"
description: "Curated collection of token-level annotated datasets identifying proper names, locations, and organizations in Devanagari text."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
modality: "text"
task: "named-entity-recognition"
language:
  - "ne"
script: "Devanagari"
tags:
  - ner
  - token-classification
  - information-extraction
---

# Nepali Named Entity Recognition (NER) Datasets

## Overview
Named Entity Recognition in Nepali presents challenges due to the lack of capitalization cues present in Latin scripts. NER datasets use IOB (Inside, Outside, Beginning) tagging schemes to annotate Persons (PER), Locations (LOC), Organizations (ORG), and Miscellaneous (MISC) entities.

## Curated Datasets

| Dataset | Schema | Size | Description & Source |
| :--- | :--- | :--- | :--- |
| **DanfeNER** | IOB2 (PER, LOC, ORG) | Token-level annotations | Curated named entity benchmark created by NowaLab for evaluating modern deep learning taggers in Nepali. Available on [GitHub: nowalab/DanfeNER](https://github.com/nowalab/DanfeNER). |
| **EverestNER** | IOB2 (PER, LOC, ORG, GEO) | 10k+ Annotated Tokens | Evaluation dataset containing annotated media sentences with diverse local entity mentions and political figures. Available on [GitHub: nowalab/everest-ner](https://github.com/nowalab/everest-ner) and [Hugging Face: xap/everest-ner](https://huggingface.co/datasets/xap/everest-ner). |
| **Setopati Nepali NER** | IOB2 | News corpora | News-domain token-level entity extraction annotations scraped from Setopati daily news articles. Available on [GitHub: oya163/nepali-ner](https://github.com/oya163/nepali-ner). |
| **Dadelani African/Asian Low-Resource NER (Nepali Slice)** | CoNLL IOB | Multi-lingual standardized | Cross-lingual evaluation set for token-level named entity classification. Available on [GitHub: dadelani/nepali-ner](https://github.com/dadelani/nepali-ner). |
| **Merishna Suwal Offensive Language & NER Dataset** | IOB / Multitask | Social Media comments | Multitask annotated dataset identifying target entities and abusive tone in social media threads. Available on [Kaggle](https://www.kaggle.com/datasets/merishnasuwal/offensive-language-ner-and-sentiment-analysis-data). |
| **PAN Localization Nepali NER** | CoNLL Format | News articles | Pioneer annotated NER dataset developed under PAN Localization research initiatives. |

## Interconnected Graph Nodes
- **Papers**: [Named Entity Recognition Papers](wiki/papers/ner_papers.md)
- **Institutions**: [ILPRL](wiki/institutions/ilprl.md)

