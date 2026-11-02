---
okf_version: "0.2"
type: "dataset"
title: "Nepali Lexicons, Dictionaries & WordNet Datasets"
description: "Curated collection of lexical databases, bilingual dictionaries, synset relations, and spellchecking lexicons for Nepali."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
modality: "lexical"
task: "lexical-semantics"
language:
  - "ne"
  - "hi"
  - "en"
script: "Devanagari"
tags:
  - wordnet
  - dictionary
  - lexicon
  - spellchecking
---

# Nepali Lexicons, Dictionaries & WordNet Datasets

## Overview
Lexical semantics and rule-based systems in Nepali rely heavily on standardized dictionaries, machine-readable thesauri, and hierarchical synset graphs like WordNet.

## Curated Lexical Resources

| Resource | Organization / Maintainer | Description & Scope |
| :--- | :--- | :--- |
| **Nepali WordNet (IndoWordNet)** | IIT Bombay, KU, TU | Synset hierarchy linked to the Hindi and English WordNet graphs via synset IDs, providing semantic relations (hypernyms, hyponyms, antonyms). Accessible via [IndoWordNet](http://www.cilt.iitb.ac.in/indowordnet/). |
| **Nepali Brihat Sabdakosh (Digital Corpus)** | Titung / Nepal Academy | Complete digitized machine-readable database of the official comprehensive Nepali dictionary (*Nepali Brihat Sabdakosh*), including 60,000+ headwords, grammatical categories, and definitions. Available on [Hugging Face](https://huggingface.co/datasets/Titung/nepali-brihat-sabdakosh). |
| **SIL International Nepali Dictionaries** | SIL Nepal | Bilingual and multilingual glossaries for Nepali, Newar, and indigenous Himalayan languages. |
| **Hunspell Nepali Dictionary (`th_ne_NP`)** | LibreOffice / Open Source | Morphological dictionary rules and affix definitions used in system spellcheckers. |
| **PAN Localization Thesaurus & Lexicon** | PAN Localization / LTK | Electronic dictionary with inflectional paradigm lists, lemmas, and phonetic spellings developed under the PAN Localization Nepal initiative. |
| **Nepali Spell-Checker Lexical Graph** | Nishant Luitel | Rule-based and affix-stripping lexicon for automated typo correction and normalization. Available on [GitHub](https://github.com/NishantLuitel/Nepali-Spell-Checker). |
| **DACON Diachronic Newar Lexical Corpus** | Cambridge University / CUDL | Lexical database spanning classical Newari palm-leaf texts, Malla epigraphy, and modern varieties. Archived on [Zenodo](https://zenodo.org/records/12887386) and [Cambridge Apollo](https://doi.org/10.17863/cam.111572). |

## Interconnected Graph Nodes
- **Papers**: [WordNet & WSD Papers](wiki/papers/wordnet_wsd_papers.md)
- **Institutions**: [ILPRL](wiki/institutions/ilprl.md), [Language Technology Kendra](wiki/institutions/ltk.md)

