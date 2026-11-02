---
okf_version: "0.2"
type: "concept"
title: "Languages of Nepal & Ethno-Linguistic NLP Landscape"
description: "Comprehensive sociolinguistic and computational catalog of national, regional, and indigenous languages of Nepal spanning Indo-Aryan and Sino-Tibetan families, their scripts, speaker populations, and low-resource NLP readiness."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T11:45:00Z"
tags:
  - languages-of-nepal
  - low-resource-languages
  - maithili
  - bhojpuri
  - tharu
  - tamang
  - limbu
  - doteli
---

# Languages of Nepal & Ethno-Linguistic NLP Landscape

## Overview
According to the National Census of Nepal, over 120 distinct mother tongues are spoken across the country, belonging predominantly to two major linguistic families: **Indo-Aryan** (part of the Indo-European family) and **Sino-Tibetan** (Tibeto-Burman). While standard Nepali (`ne`) possesses the largest digital presence, several regional languages have substantial speaker populations, unique morphosyntactic structures, and growing digital initiatives.

---

## 1. Major Indo-Aryan Languages of Nepal

| Language | ISO 639-3 | Primary Region | Traditional & Modern Script | Key Linguistic Characteristics & NLP Context |
| :--- | :--- | :--- | :--- | :--- |
| **Maithili (मैथिली)** | `mai` | Southeastern Terai (Mithila / Madhesh Province) | Mithilakshar (Tirhuta), Kaithi; contemporarily Devanagari | Second most spoken language in Nepal (~11.6%). Features complex honorific agreement on verbs, non-nominative subjects, and substantial parallel corpora (e.g. MaithiliMT). |
| **Bhojpuri (भोजपुरी)** | `bho` | Central & Western Terai (Parsa, Bara, Rautahat) | Kaithi historically; Devanagari contemporarily | Third most spoken language in Nepal. Rich oral folklore, verbal aspect markers, and growing coverage in multilingual models (e.g. IndicTrans2, NLLB). |
| **Tharu (थारू)** | `the`, `thl`, `thq` | Terai Belt (Chitwan, Dang, Kailali, Kanchanpur) | Devanagari | Dialect continuum (Dangaura, Rana, Chitwania). Highly distinct phonology, nasalization contrasts, and severely underrepresented in computational tokenizers. |
| **Doteli (डोटेली)** | `dty` | Far-Western Province (Sudurpashchim) | Devanagari | Closely related to Khas/Nepali with conservative archaisms, distinctive personal pronouns, and unique nominal case postpositions. Has active Wikimedia edition. |
| **Angika (अङ्गिका)** | `anp` | Eastern Terai (Morang, Jhapa border) | Kaithi / Devanagari | Intermediate between Maithili and Bengali with unique verbal tense morphology. |
| **Magahi (मगही)** | `mag` | Southern Border settlements | Kaithi / Devanagari | Eastern Indo-Aryan language related to Bhojpuri, characterized by person-clitic verbal agreement. |

---

## 2. Major Sino-Tibetan (Tibeto-Burman) Languages of Nepal

| Language | ISO 639-3 | Primary Region | Script | Computational & Typological Features |
| :--- | :--- | :--- | :--- | :--- |
| **Nepal Bhasa / Newar** | `new` | Kathmandu Valley & diaspora | Prachalit (Nepal Lipi), Ranjana, Devanagari | Egophoric (conjunct/disjunct) verb agreement, split-ergativity, elaborate classifier system. See full dedicated node: [Newar Computational Linguistics](wiki/concepts/newa_computational_linguistics.md). |
| **Tamang (तामाङ)** | `taj` | Central Hill districts surrounding Kathmandu Valley | Sambhota (Tibetan-derived), Tamyig, Devanagari | Tonal pitch-accent language with rich agglutinative morphology. Covered in the NepTam parallel corpus (`ilprl-docse/NepTam-A-Nepali-Tamang-Parallel-Corpus`). |
| **Magar (मगर)** | `mgp` (Dhut), `kip` (Kham) | Western & Central Hills (Palpa, Rolpa, Tanahun) | Magar Akkha Lipi, Devanagari | Split into Magar Dhut and Kham Magar; complex pronominal prefixation and verbal person agreement. |
| **Gurung (गुरुङ / तमु क्यी)** | `gvr` | Gandaki Province (Kaski, Lamjung, Syangja) | Khe Phri (Tamu Lipi), Devanagari | Tonal syllable structure with prefixal and suffixal compounding. |
| **Limbu (याक्थुङ्बा)** | `lif` | Eastern Hills (Panchthar, Taplejung, Ilam) | **Sirijunga Script** (Unicode block `U+1900`–`U+194F`), Devanagari | Complex bipersonal verbal inflection (prefixal & suffixal agreement with subject and object), dual number, and distinctive indigenous Sirijunga typography. |
| **Sherpa (शेर्पा)** | `xsr` | Solukhumbu & High Himalayan zone | Sambhota, Devanagari | Direct tonal relative of Classical Tibetan; oral dialectal variations across high alpine valleys. |

---

## 3. Indigenous Writing Systems & Scripts of Nepal

- **Devanagari (`Deva`, U+0900–U+097F)**: Universal national orthography used for official administrative texts, press, and contemporary publications across Nepali, Maithili, Bhojpuri, and Newar.
- **Prachalit / Nepal Lipi (`Newa`, U+11400–U+1147F)**: Primary historical script of the Kathmandu Valley for Classical Newari inscriptions and palm-leaf manuscripts.
- **Rañjanā Lipi**: High-status calligraphic and sacred Buddhist script used across Nepal, Tibet, and East Asia for epigraphy and Dharani scriptures.
- **Sirijunga Script (`Limb`, U+1900–U+194F)**: Indigenous abugida for writing the Limbu language, featuring distinctive subjoined glottal markers and vowel signs.

---

## Connected Graph Nodes
- **Newar Foundations**: [Newar Computational Linguistics](wiki/concepts/newa_computational_linguistics.md)
- **Devanagari Foundations**: [Devanagari NLP Foundations](wiki/concepts/devanagari_nlp.md)
- **Toolkits**: [Nepali NLP Python Libraries](wiki/concepts/nepali_nlp_libraries.md)
- **Datasets**: [Translation Datasets](wiki/datasets/translation_datasets.md)

