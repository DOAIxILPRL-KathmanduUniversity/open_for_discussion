---
okf_version: "0.2"
type: "dataset"
title: "Nepali Morphology & Part-of-Speech Datasets"
description: "Curated collection of morphosyntactically categorized corpora and token-level Part-of-Speech (POS) tagged datasets for Nepali."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
modality: "text"
task: "pos-tagging"
language:
  - "ne"
script: "Devanagari"
tags:
  - pos-tagging
  - morphology
  - syntax
---

# Nepali Morphology & Part-of-Speech Datasets

## Overview
Due to rich verbal inflection and agglutinative suffixation in Nepali, standardized POS tagsets and morphologically segmented corpora are foundational for tokenizers, chunkers, and dependency parsers.

## Curated Corpora & Tagsets

| Corpus / Resource | Tagset Scheme | Description & Research Context |
| :--- | :--- | :--- |
| **Nelralec Corpus (Bhasha Sanchar)** | Nelralec Tagset (NT-01) | Landmark annotated contemporary Nepali corpus created by Lancaster University, Tribhuvan University, and partners. |
| **PAN Localization POS Tagged Corpus** | BIS / Penn-style adaptation | 100k+ word tagged corpus developed for training early statistical POS models (HMM, CRF, SVM). |
| **Fine-Grained Nepali POS Tagged Dataset** | Extended Fine-Grained Schema | Multi-tiered morphosyntactic annotations developed at Kathmandu University for sub-category disambiguation. |

## Interconnected Graph Nodes
- **Papers**: [Morphology & POS Tagging Papers](wiki/papers/morphology_pos_papers.md)
- **Concepts**: [Devanagari NLP Foundations](wiki/concepts/devanagari_nlp.md)
- **Institutions**: [ILPRL](wiki/institutions/ilprl.md)

