---
okf_version: "0.2"
type: "model"
title: "NPVec1 & Nepali Word Embeddings"
description: "Dense static vector embeddings (Word2Vec, FastText, ELMo) trained on large Nepali news corpora for semantic similarity and shallow representation."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
tags:
  - word2vec
  - fasttext
  - embeddings
  - vector-space
dimensions: 300
---

# NPVec1 & Nepali Word Embeddings

## Overview
Before the emergence of contextual transformer models (NepaliBERT, NepBERTa), static word vectors served as the primary neural representation for lexical semantics in Nepali.

## Primary Implementations
1. **NPVec1**: Continuous Bag of Words (CBOW) and Skip-gram Word2Vec embeddings trained on millions of tokens from national Nepali news portals.
2. **FastText Nepali Vectors**: Subword n-gram embeddings released by Meta AI, allowing representation of inflected and compound Nepali words through sub-morphemic chunks.
3. **NowaLab Nepali Word Embeddings**: Open-source 300-dimensional embeddings distributed for academic experimentation.

## Connected Entities
- **Datasets**: [Monolingual Text Datasets](wiki/datasets/monolingual_text_datasets.md)
- **Papers**: [Language Modeling Papers](wiki/papers/language_modeling_papers.md)

