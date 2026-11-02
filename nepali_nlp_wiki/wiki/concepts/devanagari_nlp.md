---
okf_version: "0.2"
type: "concept"
title: "Devanagari NLP Foundations"
description: "Core computational linguistics concepts, character encodings, and Unicode tokenization challenges for Nepali text written in Devanagari script."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
tags:
  - nepali-nlp
  - devanagari
  - tokenization
  - linguistics
---

# Devanagari NLP Foundations

## Linguistic Overview
Nepali is an Indo-Aryan language written in the **Devanagari script** (Unicode block `U+0900` to `U+097F`). Unlike Latin script, Devanagari is an abugida where consonants inherit an inherent vowel (/a/) unless modified by diacritics (matras), halanta (virama), or conjuncts.

## Key Computational Challenges
1. **Complex Conjuncts & Halanta**: Syllable boundaries and conjunct characters (e.g. क्ष, त्र, ज्ञ) complicate standard character-level tokenization.
2. **Compound Words & Clitics**: Postpositions (e.g. -मा, -को, -ले) are frequently written either fused to nouns or spaced inconsistently.
3. **Spelling Variations & Free Orthography**: Alternate spellings for sibilants (श, ष, स) and vowel lengths (इ/ई, उ/ऊ) require normalization pipelines.
4. **Encoding Inconsistencies**: Legacy legacy ASCII fonts (Preeti, Kantipur) require font conversion to standard Unicode.

## Related Entities
- **Toolkits & Libraries**: [Nepali NLP Python Libraries](wiki/concepts/nepali_nlp_libraries.md)
- **Datasets**: [Monolingual Text Datasets](wiki/datasets/monolingual_text_datasets.md)
- **Papers**: [Morphology & POS Tagging Papers](wiki/papers/morphology_pos_papers.md)

