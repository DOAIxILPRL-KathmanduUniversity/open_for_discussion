---
okf_version: "0.2"
type: dataset
title: "Nepali Question Answering & Instruction Tuning Datasets"
description: "Curated collection of public Question Answering (QA), reading comprehension, medical/legal query-response benchmarks, and instruction tuning (SFT) corpora for Nepali and regional languages."
status: stable
version: 1.0.0
timestamp: "2026-11-02T12:05:00+05:45"
domain:
  - natural-language-understanding
  - question-answering
  - instruction-tuning
  - supervised-fine-tuning
languages:
  - nepali
  - english
  - tharu
format:
  - json
  - parquet
  - csv
licenses:
  - Apache-2.0
  - MIT
  - CC-BY-SA-4.0
sources:
  - "https://huggingface.co/datasets/Yunika/Nepali-QA"
  - "https://huggingface.co/datasets/Bibek1129/nepali_SQuAD"
  - "https://huggingface.co/datasets/dineshkarki/textbooks-qa-nepali"
  - "https://huggingface.co/datasets/chhatramani/nepal-legal-qa-benchmark_v1"
  - "https://huggingface.co/datasets/NepaliAI/Nepali-Health-QA"
  - "https://huggingface.co/datasets/Bibek-Poudel/ENG_NEP_MED_PARALLEL"
  - "https://huggingface.co/datasets/Saugatkafley/alpaca-nepali-sft"
  - "https://huggingface.co/datasets/ashokpoudel/English-Nepali-Translation-Instruction-Dataset"
  - "https://huggingface.co/datasets/prajwal-panth/tharu-chat"
  - "https://www.kaggle.com/datasets/chhatramaniyadav/nepal-constitution-qa-dataset-en"
---

# Nepali Question Answering & Instruction Tuning Datasets

This node catalogs public, verifiable question answering benchmarks, reading comprehension corpora, domain-specific retrieval-augmented generation (RAG) testbeds, and supervised fine-tuning (SFT) datasets for Nepali LLM development.

## 1. General & Reading Comprehension Benchmarks

| Dataset | Split / Volume | Format | Description / Source |
| :--- | :--- | :--- | :--- |
| **Nepali Belebele QA** | Multi-choice QA | Parquet | Devanagari translation and localization of Meta's Belebele benchmark for cross-lingual reading comprehension evaluation. Available on [Hugging Face](https://huggingface.co/datasets/Yunika/Nepali-QA). |
| **Nepali SQuAD** | 10k+ context-Q-A pairs | JSON | Translated and quality-filtered Stanford Question Answering Dataset (SQuAD) into native Devanagari text for span extraction models. Available on [Hugging Face](https://huggingface.co/datasets/Bibek1129/nepali_SQuAD). |
| **IndicDialogue Dataset (Mendeley Data)** | Multi-turn conversational dialogues | JSONL / SRT | Subtitle-derived conversational dialogue corpus covering 10 Indic languages including Nepali, curated for small and large language model instruction tuning. Archived on [Mendeley Data](https://doi.org/10.17632/wcb4bxbyxx.2) (DOI: `10.17632/wcb4bxbyxx.2`). |
| **Nepali Textbook QA** | Primary & secondary curricula | JSON / Parquet | Question-answer pairs extracted and aligned from government-issued Nepali school textbooks (curriculum-aligned reading evaluation). Available on [Hugging Face](https://huggingface.co/datasets/dineshkarki/textbooks-qa-nepali). |
| **NLUE QA Suite** | Standardized evaluation | Parquet | Standardized question answering and natural language inference splits of the Nepali Language Understanding Evaluation benchmark. Published in IJCNLP 2025 and hosted on [Hugging Face](https://huggingface.co/datasets/IRIIS-RESEARCH/NLUE). |

## 2. Domain-Specific (Legal & Medical) QA Benchmarks

| Dataset | Domain | Focus Area | Description / Source |
| :--- | :--- | :--- | :--- |
| **Nepal Legal QA Benchmark** | Constitutional & Statutory Law | Statutes, Muluki Ain, Legal RAG | Curated questions and authoritative legal provisions covering the Constitution of Nepal, Civil and Criminal Codes (Muluki Samhita). Benchmarks legal retrieval and generative grounding. Available on [Hugging Face](https://huggingface.co/datasets/chhatramani/nepal-legal-qa-benchmark_v1). |
| **Nepal Constitution Dataset** | Constitutional Framework | 308 Articles, parts, schedules | Complete structured text of the Constitution of Nepal (2072) segmented by parts, article numbers, and titles. Available on [Hugging Face: ranjitraut](https://huggingface.co/datasets/ranjitraut/nepal-constitution-dataset). |
| **Nepal Constitution Instruction QA** | Constitutional Law | 308 Articles, fundamental rights | Instruction-formatted pairs testing constitutional question answering. Available on [Hugging Face: nordenxgt](https://huggingface.co/datasets/nordenxgt/nepal-constitution-instruction-dataset) and [Kaggle](https://www.kaggle.com/datasets/chhatramaniyadav/nepal-constitution-qa-dataset-en). |
| **Nepal Kanoon Patrika (NKP) Precedents** | Case Law & Jurisprudence | Supreme Court judgments | Digitized archive of monthly precedent law reports (*Nirnaya*) published by the Supreme Court of Nepal since 1958. Accessible via [nkp.gov.np](http://nkp.gov.np). |
| **Nepali Health QA** | Healthcare & Clinical Guidance | Maternal care, public health | Culturally adapted medical queries with doctor-verified explanations in Devanagari script. Maintained on [Hugging Face: NepaliAI](https://huggingface.co/datasets/NepaliAI/Nepali-Health-QA) and [Kaggle](https://www.kaggle.com/). |
| **English-Nepali Medical Parallel QA** | Medical Consultation | Bilingual clinical dialogues | Sentence-aligned medical consultation pairs designed for cross-lingual health inquiry retrieval. Available on [Hugging Face](https://huggingface.co/datasets/Bibek-Poudel/ENG_NEP_MED_PARALLEL). |

## 3. Supervised Fine-Tuning (SFT) & Instruction Tuning Datasets

| Dataset | Volume / Modality | Tasks Covered | Description / Source |
| :--- | :--- | :--- | :--- |
| **Alpaca Nepali SFT** | 52,000 instructions | Multi-turn reasoning, summarization, extraction | Complete Nepali localization of Stanford Alpaca's instruction following dataset, translated and orthographically normalized for fine-tuning generative LLMs. Available on [Hugging Face](https://huggingface.co/datasets/Saugatkafley/alpaca-nepali-sft). |
| **Translation Instruction SFT** | 100k+ pairs | Controlled translation, formality, domain shift | Instruction-formatted English-to-Nepali and Nepali-to-English translation prompts designed to teach generative models translation constraints. Available on [Hugging Face](https://huggingface.co/datasets/ashokpoudel/English-Nepali-Translation-Instruction-Dataset). |
| **TharuChat Instruction Dataset** | Multi-dialect Tharu | Dialect conversational QA | Multi-dialect Tharu conversational instruction dataset bridging regional Western Tharu varieties with standard Devanagari instruction tuning. Available on [Hugging Face](https://huggingface.co/datasets/prajwal-panth/tharu-chat). |

## Related Vault Nodes
- [[monolingual_text_datasets]]
- [[translation_datasets]]
- [[nlp_evaluation_metrics]]
- [[nepaligpt]]

