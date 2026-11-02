---
okf_version: "0.2"
type: "dataset"
title: "Nepali Machine Translation & Parallel Datasets"
description: "Curated collection of parallel text corpora and evaluation benchmarks for English-Nepali, Nepali-Hindi, and regional multilingual translation."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
modality: "parallel_text"
task: "machine-translation"
language:
  - "ne"
  - "en"
  - "hi"
script: "Devanagari"
tags:
  - machine-translation
  - parallel-corpus
  - low-resource
---

# Nepali Machine Translation & Parallel Datasets

## Overview
Parallel corpora connect Nepali utterances with paired equivalents in English, Hindi, and regional languages for training and evaluating Statistical (SMT) and Neural Machine Translation (NMT) models.

## Curated Parallel Corpora

| Dataset | Language Pair | Size / Format | Description & Source |
| :--- | :--- | :--- | :--- |
| **FLORES-101 / FLORES-200** | en-ne, multi | 1,012 multi-way parallel sentences | Meta AI benchmark designed to measure translation quality across low-resource languages. |
| **WMT19 News Translation Task** | en-ne | ~50k parallel sentences | Official benchmark dataset for low-resource translation released for WMT19 shared task. |
| **PAN Localization Parallel Corpus** | ur-ne-en | 10k+ sentence pairs | Parallel and POS-tagged multilingual corpus constructed by the PAN Localization project. |
| **CCAligned / OPUS English-Nepali** | en-ne | Multi-million parallel pairs | Web-crawled, sentence-aligned parallel corpus available openly on the OPUS multilingual repository. Available via [OPUS](https://opus.nlpl.eu/). |
| **English to Nepali Translation Dataset (Kaggle)** | en-ne | 150k+ sentence pairs | Aggregated bilingual translation pairs filtered from open translation repositories for fine-tuning seq2seq models. Hosted on [Kaggle](https://www.kaggle.com/). |
| **Roman to Nepali Transliteration Dataset** | Roman-ne (Devanagari) | Sentence-aligned parallel text | Direct phonetic transliteration corpus mapping Romanized informal sentences to standard Devanagari orthography. Available on [Hugging Face: rajeshrai577](https://huggingface.co/datasets/rajeshrai577/roman-to-nepali-dataset). |
| **NepTam (Nepali-Tamang Parallel Corpus)** | ne-taj | NepTam20K (Gold) + NepTam80K (Synthetic) | Kathmandu University (ILPRL) multi-domain parallel corpus across health, agriculture, education, and culture presented at LREC. | [GitHub: ilprl/NepTam](https://github.com/ilprl/NepTam-A-Nepali-Tamang-Parallel-Corpus-and-Baseline-Machine-Translation-Experiments) |
| **MaithiliMT Multi-Domain Parallel Corpus** | mai-hi, mai-en | Sentence-aligned parallel texts | Open-source multi-domain parallel machine translation benchmark for the Maithili language. | [GitHub: MaithiliMT](https://github.com/MaithiliMT) |
| **Alpaca Nepali SFT (Instruction Tuning)** | ne | 10k-50k instructions | Alpaca-style instruction following dataset translated and adapted for supervised fine-tuning (SFT) of Nepali LLMs. | [Hugging Face](https://huggingface.co/datasets/Saugatkafley/alpaca-nepali-sft) |

## Interconnected Graph Nodes
- **Papers**: [Machine Translation Papers](wiki/papers/translation_papers.md)
- **Institutions**: [ILPRL](wiki/institutions/ilprl.md)

