---
okf_version: "0.2"
type: "concept"
title: "Nepali NLP Python Libraries & Toolkits"
description: "Curated catalog of publicly available, installable Python packages and open-source toolkits for Nepali text processing, tokenization, stemming, font conversion, and speech."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T11:00:00Z"
tags:
  - python-libraries
  - pip-packages
  - open-source-tools
  - nepali-nlp
---

# Nepali NLP Python Libraries & Toolkits

This catalog documents open-source, publicly accessible Python libraries that install out-of-the-box (via PyPI or GitHub) for Nepali computational linguistics workflows.

---

## 1. Tokenizers & Preprocessing Libraries

### `nepalitokenizers`
- **PyPI**: [`pip install nepalitokenizers`](https://pypi.org/project/nepalitokenizers/)
- **GitHub**: [`basnetsoyuj/nepali-tokenizers`](https://github.com/basnetsoyuj/nepali-tokenizers)
- **Features**: Pre-trained WordPiece and SentencePiece (Unigram) tokenizers tailored for Devanagari script; Hugging Face `tokenizers` backend.

### `nepalikit`
- **PyPI**: [`pip install nepalikit`](https://pypi.org/project/nepalikit/)
- **GitHub**: [`prabhashj07/nepalikit`](https://github.com/prabhashj07/nepalikit)
- **Features**: Rule-based Devanagari tokenization, sentence segmenter, stopword remover, and suffix-stripping morphological stemmer.

### `indic-nlp-library`
- **PyPI**: [`pip install indic-nlp-library`](https://pypi.org/project/indic-nlp-library/)
- **GitHub**: [`anoopkunchukuttan/indic_nlp_library`](https://github.com/anoopkunchukuttan/indic_nlp_library)
- **Features**: Broad Indic language toolkit; Devanagari Unicode script normalizer, syllabifier, text segmenter, and Indian language transliteration.

---

## 2. General NLP & Stemmers

### `nepali-stemmer`
- **PyPI**: [`pip install nepali-stemmer`](https://pypi.org/project/nepali-stemmer/)
- **GitHub**: [`oya163/nepali-stemmer`](https://github.com/oya163/nepali-stemmer)
- **Features**: Lightweight, rule-based suffix stripper specifically designed for Nepali noun/verb postpositions without external heavy neural dependencies.

### `Nepali_nlp`
- **PyPI**: [`pip install Nepali-nlp`](https://pypi.org/project/Nepali-nlp/)
- **GitHub**: [`sushil79g/Nepali_nlp`](https://github.com/sushil79g/Nepali_nlp)
- **Features**: High-level wrapper for Nepali word embeddings loading, news classification baselines, tokenization, and Unicode-to-Preeti conversion.

---

## 3. Font Converters & Unicode Normalizers

### `nepali-converter`
- **PyPI**: [`pip install nepali-converter`](https://pypi.org/project/nepali-converter/)
- **GitHub**: [`nepalibhasha/nepali-fonts`](https://github.com/nepalibhasha/nepali-fonts)
- **Features**: CLI and Python API converting legacy non-Unicode fonts (Preeti, Kantipur, Sagarmatha) to standard Devanagari Unicode.

### `npttf2utf`
- **PyPI**: [`pip install npttf2utf`](https://pypi.org/project/npttf2utf/)
- **GitHub**: [`casualsnek/npttf2utf`](https://github.com/casualsnek/npttf2utf)
- **Features**: Bidirectional ASCII TrueType font to Devanagari Unicode converter with auto-detection for `.txt` and `.docx` files.

---

## 4. Speech Synthesis (TTS) & ASR Libraries

### `supernova-teraitts`
- **PyPI**: [`pip install supernova-teraitts`](https://pypi.org/project/supernova-teraitts/)
- **Features**: Python wrapper interfacing with XTTS-v2 fine-tuned checkpoints (`Oshara/xtts-v2-nepali`) for native Nepali voice synthesis and cloning.

### `pytesseract` (with Nepali Language Model)
- **PyPI**: [`pip install pytesseract`](https://pypi.org/project/pytesseract/)
- **Prerequisite**: Tesseract OCR with `nep.traineddata`
- **Features**: Document and image OCR directly emitting standardized Devanagari Unicode strings.

---

## Connected Graph Nodes
- **Concepts**: [Devanagari NLP Foundations](wiki/concepts/devanagari_nlp.md)
- **Datasets**: [Nepali Speech Datasets](wiki/datasets/speech_datasets.md), [Morphology Datasets](wiki/datasets/morphology_pos_datasets.md)
- **Papers**: [Speech Processing Papers](wiki/papers/speech_papers.md), [OCR Papers](wiki/papers/ocr_papers.md)

