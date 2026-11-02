---
okf_version: "0.2"
type: "model"
title: "NepBERTa"
description: "A monolingual RoBERTa-based language model pre-trained on a large-scale Nepali crawl for downstream classification, token tagging, and language representation."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
authors:
  - "Sandesh Timilsina"
  - "Milan Gautam"
  - "Bikash Bhattarai"
tags:
  - transformer
  - roberta
  - language-model
  - nepali-nlp
parameters: "125M"
architecture: "RoBERTa-Base"
---

# NepBERTa

## Overview
**NepBERTa** is a state-of-the-art Transformer language model trained on over 1.5GB of raw crawled Nepali text. By employing the RoBERTa training paradigm (removing the Next Sentence Prediction objective, dynamic masking, and larger mini-batch training), it offers strong contextual representations for Devanagari text.

## Architecture & Tokenizer
- **Architecture**: 12 layers, 768 hidden dimensions, 12 attention heads.
- **Tokenizer**: Byte-Pair Encoding (BPE) vocabulary constructed to represent common Nepali prefixes and postpositions.

## Connected Entities
- **Papers**: [Language Modeling Papers](wiki/papers/language_modeling_papers.md)
- **Datasets**: [Monolingual Text Datasets](wiki/datasets/monolingual_text_datasets.md), [Classification Datasets](wiki/datasets/classification_datasets.md)
- **Institutions**: [NAAMII](wiki/institutions/naamii.md)

