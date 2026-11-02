---
okf_version: "0.2"
type: "dataset"
title: "Nepali Text & News Classification Datasets"
description: "Curated collection of labeled Nepali corpora for multi-class document categorization, topic modeling, and SMS spam filtering."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
modality: "text"
task: "text-classification"
language:
  - "ne"
script: "Devanagari"
tags:
  - classification
  - news
  - topic-modeling
---

# Nepali Text & News Classification Datasets

## Overview
Document classification benchmarks test the ability of machine learning models and fine-tuned transformers to categorize Nepali texts into categorical categories (politics, sports, economy, entertainment, etc.).

## Curated Datasets

| Dataset | Categories | Task | Description & Source |
| :--- | :--- | :--- | :--- |
| **16NepaliNews Classification Corpus** | 16 Topics | Topic Categorization | Standard benchmark containing thousands of articles scraped from Nepali portals classified into 16 distinct domain categories. Widely mirrored on GitHub and Hugging Face. |
| **Ashok Pant Nepali News Dataset (Large)** | Multi-Class | Domain Classification | Large-scale news dataset partitioned across specialized topics including Agriculture, Politics, Business, Sports, and Technology. Hosted on [Kaggle](https://www.kaggle.com/datasets/ashokpant/nepali-news-dataset). |
| **Setopati Fresh Nepali News Dataset** | Multi-topic | Media Classification | Continuous scraper corpus of recent news articles with editorial category labels and timestamps from Setopati. Available on [Kaggle: sanjaybhandari](https://www.kaggle.com/datasets/sanjaybhandari/setopati-fresh-nepali-news-dataset). |
| **NaBI (Nepali Bias & Information Dataset)** | 4 Classes | Content Moderation & Safety | Gold-standard annotated corpus for detecting Bias, Misinformation, Hate Speech, and Neutral text in colloquial Nepali and news comments. Available on [Hugging Face: Utkarsha666/NaBI](https://huggingface.co/datasets/Utkarsha666/NaBI). |
| **Code-Switched Customer Support Intents** | Multi-intent | Conversational Intent Detection | 10k+ annotated customer support queries in Nepali, English, and Romanized code-mixing for training intent routers. Available on [Kaggle: sarveshchhetri](https://www.kaggle.com/datasets/sarveshchhetri/nepali-english-code-switched-support-intents). |
| **NeCCo (Nepali Cultural Commonsense Benchmark)** | Multi-choice reasoning | Cultural Reasoning / NLU | Grounded multiple-choice benchmark evaluating understanding of indigenous Nepali cultural festivals, cuisine, kinship terms, and social practices. Hosted on [GitHub: nepali-nlp/necco-benchmark](https://github.com/nepali-nlp/necco-benchmark). |
| **Nepali 20 Newsgroups (`np20ng`)** | 20 Classes | News Topic Categorization | Localized equivalent of the 20 Newsgroups benchmark for evaluating document classifiers across specialized topical categories. Available on [Hugging Face: Suyogyart/np20ng](https://huggingface.co/datasets/Suyogyart/np20ng). |
| **Spandyie Nepali News Classification Dataset** | 10 Categories | Multi-Class News Classification | Standardized news split categorized into politics, sports, education, economy, technology, and entertainment. Available on [Hugging Face: spandyie/nepali-news-dataset](https://huggingface.co/datasets/spandyie/nepali-news-dataset). |
| **Zaxis018 Nepali News Classification Corpus** | Multi-topic | Text Categorization | Preprocessed news text pipeline and dataset for training TF-IDF, Word2Vec, and BERT classifiers. Available on [GitHub: Zaxis018/Nepali-News-classification](https://github.com/Zaxis018/Nepali-News-classification). |
| **iNLTK Nepali News Dataset** | Multi-class | Headline / Article Classification | Curated corpus distributed via the Natural Language Toolkit for Indic Languages (iNLTK). Available on [Kaggle](https://www.kaggle.com/). |
| **Nepali Mobile SMS Spam Dataset** | 2 (Ham / Spam) | SMS Filtering | Collection of mobile SMS messages received in Nepal annotated for spam detection and message filtering. |

## Interconnected Graph Nodes
- **Papers**: [Text Classification Papers](wiki/papers/classification_papers.md)
- **Models**: [NepaliBERT](wiki/models/nepalibert.md), [NepBERTa](wiki/models/nepberta.md)

