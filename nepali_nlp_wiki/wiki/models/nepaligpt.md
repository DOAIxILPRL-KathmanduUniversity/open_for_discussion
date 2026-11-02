---
okf_version: "0.2"
type: "model"
title: "NepaliGPT"
description: "Open-weights generative autoregressive language model for Nepali, pre-trained and instruction-tuned on Devanagari text corpora."
status: "active"
version: "2.0.0"
timestamp: "2026-11-02T11:50:00Z"
architecture: "Llama-derived / GPT"
parameters: "1B"
license: "Apache-2.0 / Open Weights"
source_url: "https://huggingface.co/universalml/NepaliGPT"
paper_url: "https://arxiv.org/abs/2405.00690"
tags:
  - generative-ai
  - nepali-gpt
  - llm
  - causal-lm
---

# NepaliGPT

## Overview
**NepaliGPT** is an open-weights generative language model series designed to generate, summarize, and answer questions in standard Devanagari Nepali. Developed to overcome the English-skewed tokenization and low generation quality of general LLMs, it leverages continuous pre-training on diverse Nepali web crawls, literature, and news datasets.

## Key Implementations & Checkpoints
- **`universalml/NepaliGPT-2.0`**: 1 Billion parameter generative model instruction-tuned for bilingual Nepali and English task execution.
- **`universalml/NepaliGPT`**: Baseline foundation weights trained with RoPE embeddings and Unsloth acceleration.
- **Evaluation**: Benchmarked on over 4,000 native Nepali QA pairs evaluating causal coherence, lexical diversity, and question accuracy.

## Connected Entities
- **Papers**: [Language Modeling Papers](wiki/papers/language_modeling_papers.md)
- **Metrics**: [NLP Evaluation Metrics](wiki/concepts/nlp_evaluation_metrics.md)
- **Datasets**: [Monolingual Text Datasets](wiki/datasets/monolingual_text_datasets.md)

