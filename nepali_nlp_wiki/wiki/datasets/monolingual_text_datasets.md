---
okf_version: "0.2"
type: "dataset"
title: "Nepali Monolingual & Pre-training Text Datasets"
description: "Curated collection of large-scale unannotated Nepali text corpora, web crawls, and Wikipedia dumps used for pre-training language models and word embeddings."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
modality: "text"
task: "pre-training"
language:
  - "ne"
script: "Devanagari"
tags:
  - pre-training
  - monolingual
  - web-crawl
  - language-modeling
---

# Nepali Monolingual & Pre-training Text Datasets

## Overview
Monolingual raw text corpora are the primary ingredient for self-supervised pre-training (Masked Language Modeling, Causal Language Modeling) of models like NepaliBERT and NepBERTa, as well as static embedding vectors (FastText, Word2Vec).

## Curated Corpora

| Corpus | Size / Tokens | Extraction Source & Description |
| :--- | :--- | :--- |
| **OSCAR (Open Super-large Crawled ALMAnaCH) Nepali** | Tens of Millions of Tokens | Cleaned and deduplicated Common Crawl slice filtered specifically for Nepali Devanagari text. Available on [Hugging Face](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201) and [Kaggle](https://www.kaggle.com/datasets/hsebarp/oscar-corpus-nepali). |
| **Nepali Wikipedia Database Dump** | 30,000+ Articles | Complete snapshot of Nepali Wikipedia articles encompassing encyclopedic prose, history, science, and geography. Available via [Wikimedia Dumps](https://dumps.wikimedia.org/newiki/) and [Kaggle](https://www.kaggle.com/datasets/disisbig/nepali-wikipedia-articles). |
| **A Large Scale Nepali Text Corpus (Rabindra Lamsal)** | 90+ Million Words | Landmark curated web crawl across national news, literature, sports, and health, widely used for pretraining transformer language models. Hosted on [IEEE DataPort](https://ieee-dataport.org/open-access/large-scale-nepali-text-corpus) (DOI: `10.21227/jxrd-d245`). |
| **mC4 / C4 Multilingual (Nepali Slice)** | Multi-Gigabyte Web Corpus | AllenAI multilingual colossal clean crawled corpus containing web pages filtered with language identification. |
| **IRIIS-RESEARCH Nepali Text Corpus** | 6.39M Articles / 10.1 GB | Massive open pretraining corpus scraped from major portals, blogs, and national media, used to train foundational models like `RoBERTa_Nepali_125M`. Available on [Hugging Face](https://huggingface.co/datasets/IRIIS-RESEARCH/Nepali-Text-Corpus). |
| **Silytics Nepali Text Corpus** | Multi-Million Tokens | Curated news and digital article corpus cleaned for tokenization and masked language modeling. Available on [Hugging Face](https://huggingface.co/datasets/silytics/Nepali-Text-Corpus). |
| **Boredoom17 Nepali-Corpus (Nepali-Flow)** | 7.17M Rows | Aggregated pretraining corpus incorporating Wikipedia, deduplicated news, and cleaned colloquial conversational text. Available on [Hugging Face](https://huggingface.co/datasets/Boredoom17/Nepali-Corpus). |
| **Boredoom17 Nepali-Flow-Roman** | 307,000+ Sentences | Unfiltered social media commentary collected from YouTube entirely in Romanized Latin script for training informal colloquial language models. Available on [Hugging Face](https://huggingface.co/datasets/Boredoom17/Nepali-Flow-Roman). |
| **neBrahma Nepali Pretrain Corpus** | ~2 Billion Tokens | Highly cleaned, deduplicated, and orthographically normalized pretraining corpus designed for training Nepali foundational language models. Available on [Hugging Face](https://huggingface.co/datasets/tonibirat/neBrahma-Nepali-Pretrain-Corpus). |
| **Titung Nepali Books Text Corpus** | Thousands of Books | Full-text digital corpus converted from open Nepali literature, history, and academic publications. Available on [Hugging Face](https://huggingface.co/datasets/Titung/nepali-books-text-corpus-full). |
| **Himalaya AI Nepali Corpus Compile** | Multi-Million Sentences | Aggregated Nepali web texts compiled for instruction tuning and foundation pretraining. Available on [Hugging Face](https://huggingface.co/datasets/himalaya-ai/nepali-corpus-compile). |
| **Nepali Religious & Philosophical Text Corpora** | Full Holy Texts | Digitized canonical texts: structured Devanagari Bible corpus on [Hugging Face: lilgoose777](https://huggingface.co/datasets/lilgoose777/nepali-bible-corpus) and translated Bhagavad Gita on [Hugging Face: dineshkarki](https://huggingface.co/datasets/dineshkarki/bhagavad-gita-nepali). |
| **Team-Naya NLP-Doko** | 350,000 Sentences | Open sentence-level Nepali text corpus scraped and sanitized from news feeds and blogs. Available on [GitHub](https://github.com/Team-Naya/nlp-doko). |
| **Universal Dependencies Nepali-BK (`UD_Nepali-BK`)** | 100k+ Tokens | Standardized CoNLL-U syntactic treebank annotating morphological features, parts of speech, and head-dependency relations. Available on [GitHub](https://github.com/UniversalDependencies/UD_Nepali-BK). |

## Regional & Sister Language Pretraining Corpora

| Language | Corpus | Size / Format | Description / Source |
| :--- | :--- | :--- | :--- |
| **Bhojpuri** | BhojpuriCorpus | Multi-million words | Monolingual pretraining corpus for Bhojpuri compiled from literary, cultural, and web sources. Available on [Hugging Face](https://huggingface.co/datasets/Satyam810/BhojpuriCorpus). |
| **Maithili** | MaithiliCorpus | 100k+ Sentences | Curated open pretraining corpus covering contemporary Tirhuta and Devanagari Maithili literature and journalism. Available on [Hugging Face](https://huggingface.co/datasets/AiventraLab/maithili-corpus) and [Kamal Maithili Corpus](https://huggingface.co/datasets/kamal-018/Maithili-Corpus). |
| **Purvanchal Group** | Bhojpuri-Magahi-Maithili Resources | Lexicons & Texts | Multi-language comparative linguistic resource containing text corpora, morphological analyzer dictionaries, and POS annotations. Available on [GitHub](https://github.com/singhakr/Bhojpuri-Magahi-and-Maithili-Linguistic-Resources). |

## Civic, Legal & Institutional Open Portals

| Institution / Archive | Resource Focus | Access Link |
| :--- | :--- | :--- |
| **Nepal Law Commission** | Acts, regulations, ordnances, constitutional text, and Muluki Samhita | [lawcommission.gov.np](http://www.lawcommission.gov.np) |
| **Department of Printing (Mudran Bibhag)** | Official Nepal Gazette (*Nepal Rajpatra*) digitized archive since 1951 | [rajpatra.dop.gov.np](http://rajpatra.dop.gov.np) |
| **Supreme Court of Nepal** | Precedent verdicts (*Najar*), full judgment transcripts, Supreme Court bulletin (*Nirnaya Sangraha*) | [supremecourt.gov.np](https://supremecourt.gov.np) |
| **Open Data Nepal** | Civil society open data platform archiving census tables, economic reports, and municipal data | [opendatanepal.com](https://opendatanepal.com) |

## Interconnected Graph Nodes
- **Models**: [NepaliBERT](wiki/models/nepalibert.md), [NepBERTa](wiki/models/nepberta.md), [NPVec1 Embeddings](wiki/models/npvec1_embeddings.md)
- **Papers**: [Language Modeling Papers](wiki/papers/language_modeling_papers.md)

