# Research: Transformer-based Lemmatization for Nepali

> [!IMPORTANT] Gist
> Conventional rule-based or TRIE-based lemmatization for Nepali faces challenges with normalization and over/under-stemming. This research (Regmi et al., 2026) evaluates multilingual transformer models for robust Nepali text normalization.

## 1. Problem Statement
Nepali is morphologically rich. Traditional methods suffer from:
- **Normalization Consistency**: Handling script variations.
- **Unreadable Lemmatized Data**: Rule-based systems often produce non-dictionary stems.
- **Ambiguity**: Over-stemming (removing too much) or under-stemming (leaving inflections).

## 2. Model Comparison & Performance
The study fine-tuned several Seq2Seq models on internet-sourced corpora:

| Model | Accuracy | CER (Character Error Rate) | BLEU |
| :--- | :--- | :--- | :--- |
| **mT5-base** | **96.1%** | **1.1%** | - |
| **mBART-large-50** | 96.0% | 1.6% | 0.986 |
| **mT5-small** | (Lower performance) | - | - |

**Optimized Hyperparameters**:
- **mT5-base**: Best performance with a higher learning rate of **5e-4**.
- **mBART-large-50**: Best with **1e-5** and batch size 16.

## 3. Impact on Downstream Tasks
Lemmatization is a critical preprocessing step that yields measurable gains:
- **Cross-lingual Alignment (Hindi-Nepali)**: Improved from **12.86% to 41.61%** when Nepali words were properly lemmatized.
- **Information Retrieval**: MAP scores increased from **0.71 to 0.90**.

## 4. Key Metrics
- **CER (Character Error Rate)**: Measures precision at the character level.
- **Morphological Coverage**: mBART-large-50 achieved **0.970**, showing high robustness in handling complex inflections.

---

#nepali #lemmatization #transformers #mt5 #mbart #nlp-research #text-normalization
