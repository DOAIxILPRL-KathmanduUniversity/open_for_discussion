---
okf_version: "0.2"
type: "dataset"
title: "Nepali Sentiment Analysis Datasets"
description: "Curated collection of annotated subjective text datasets, polarity labels, and review datasets in Nepali."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
modality: "text"
task: "sentiment-analysis"
language:
  - "ne"
script: "Devanagari"
tags:
  - sentiment-analysis
  - polarity
  - classification
---

# Nepali Sentiment Analysis Datasets

## Overview
Sentiment analysis corpora in Nepali provide gold-standard annotations of polarity (positive, negative, neutral) and subjectivity across news editorials, social media commentary, and entertainment reviews.

## Curated Datasets

| Dataset | Domain | Classes | Description & Source |
| :--- | :--- | :--- | :--- |
| **NepCov19Tweets (Nepali COVID-19 Tweets)** | Social Media (Twitter/X) | Positive / Negative / Neutral | Large-scale dataset of ~39,000+ Nepali tweets annotated for sentiment polarity and pandemic public sentiment modeling. Available on [Hugging Face](https://huggingface.co/datasets/raygx/NepCov19TweetsPlus2) and [Kaggle](https://www.kaggle.com/). |
| **NepEMO (Nepali Multi-Label Emotion Dataset)** | Social media & literature | 6 Basic Emotions + Neutral | Fine-grained multi-label emotion dataset annotating joy, anger, sadness, fear, surprise, and love in colloquial Devanagari text (arXiv:2512.22823). |
| **Nepali Tourism Reviews & Sentiment** | Travel & Hospitality | Positive / Negative / Neutral | User feedback and review comments scraped from tourism portals and TripAdvisor for destination sentiment analysis. Available on [Hugging Face](https://huggingface.co/datasets/Safal08/nepali-tourism-comments). |
| **Nepali Sentiment Movie Reviews** | Cinema Reviews | Positive / Negative | User reviews scraped from movie blogs and social commentary platforms with binary sentiment annotations. |
| **Nepali Subjective News Editorials** | Media / Politics | Polarity & Strength | Annotated editorial segments from national daily newspapers evaluating socio-political events. |
| **Nepal Border Sentiment Dataset** | Geopolitics / Public Opinion | Positive / Negative / Neutral | Annotated social media and YouTube comments on Nepal-India border disputes (Lipulekh, Kalapani) for tracking public geopolitical sentiment. Available on [Kaggle: samirasharma](https://www.kaggle.com/datasets/samirasharma/nepal-border-sentiment-dataset). |
| **Romanized Nepali Sentiment Analysis Dataset** | Informal Latin Script Social Text | Binary / 3-class | Labeled dataset of phonetic Romanized comments from social platforms for evaluating classifiers without transliteration preprocessing. Available on [Kaggle](https://www.kaggle.com/). |
| **NowaLab Nepali Sentiment Dataset** | Social Text | Positive / Negative / Neutral | Open-source sentiment corpus developed for testing baseline classification models. Available on [GitHub: nowalab](https://github.com/nowalab/nepali-sentiment-analysis). |

## Interconnected Graph Nodes
- **Papers**: [Sentiment Analysis Papers](wiki/papers/sentiment_papers.md)
- **Models**: [NepaliBERT](wiki/models/nepalibert.md)

