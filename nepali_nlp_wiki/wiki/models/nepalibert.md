---
okf_version: "0.2"
type: "model"
title: "NepaliBERT"
description: "A monolingual BERT base model pre-trained on Nepali textual corpora for downstream natural language understanding tasks."
status: "active"
version: "1.0.0"
timestamp: "2026-11-01T20:25:00Z"
authors:
  - "Rajan Dawadi"
  - "Suresh Pokharel"
organization: "Kathmandu University / NAAMII"
tags:
  - masked-language-model
  - bert
  - transformer
  - nepali-nlp
parameters: "110M"
vocab_size: 32000
source_url: "https://huggingface.co/Rajan/NepaliBERT"
license: "MIT"
---

# NepaliBERT

## Overview
**NepaliBERT** is a Transformer-based masked language model (BERT-Base architecture) trained specifically on Nepali text data, enabling fine-tuning for token classification (NER, POS), sentence classification (sentiment analysis), and sequence-to-sequence adaptations.

## Architecture
- **Base Architecture**: 12 layers, 768 hidden dimensions, 12 attention heads.
- **Tokenizer**: Custom WordPiece / Byte-Pair Encoding trained on tokenized Nepali Devanagari text.

## Related Entities
- **Institutions**: [NAAMII](wiki/institutions/naamii.md), [Kathmandu University](wiki/institutions/ku.md)
- **Concepts**: [Pre-training](wiki/concepts/pretraining.md), [Masked Language Modeling](wiki/concepts/mlm.md)
- **Corpora**: [Nepali News Corpus](wiki/corpora/nepali_news.md)

