---
okf_version: "0.2"
type: "model"
title: "Arkios"
description: "A 1.04B-parameter dense bilingual English-Nepali foundation language model pretrained from scratch on 150B tokens with a Devanagari-aware tokenizer."
status: "active"
version: "1.0.0"
timestamp: "2026-11-05T10:00:00Z"
authors:
  - "Sajal Regmi"
  - "Siddhartha Pudasaini"
  - "Chetan Phakami Pun"
tags:
  - foundation-model
  - causal-lm
  - bilingual-model
  - nepali-nlp
  - llm
parameters: "1.04B"
source_url: "https://arxiv.org/abs/2608.30092"
license: "Open Access"
---

# Arkios: Bilingual English-Nepali Foundation Language Model

## Overview
**Arkios** is an open-weights, 1.04B-parameter autoregressive transformer pretrained from scratch on 150 billion tokens of curated bilingual English–Nepali text. Developed with a custom single-file C/CUDA pretraining harness, Arkios directly addresses the severe subword tokenization fragmentation common in standard multilingual LLMs when parsing Devanagari script.

## Key Features & Architecture
- **Parameter Scale**: 1.04B dense parameters.
- **Pretraining Budget**: 150B tokens (balanced bilingual English and Devanagari crawl).
- **Devanagari-Aware Tokenizer**: Solves the combining-mark fragmentation issue (where standard regex pre-tokenizers separate dependent vowel signs / matras from base consonants), achieving a 2.6× to 5.8× compression efficiency gain over standard Llama/Mistral tokenizers on Nepali text.
- **Companion Research**:
  - *Tokenizer Architecture*: [arXiv:2608.26449](https://arxiv.org/abs/2608.26449)
  - *Model Pretraining*: [arXiv:2608.30092](https://arxiv.org/abs/2608.30092)

## Related Entities
- **Concepts**: [[devanagari_nlp]], [[nepali_nlp_libraries]]
- **Papers**: [[language_modeling_papers]]
- **Datasets**: [[monolingual_text_datasets]]

