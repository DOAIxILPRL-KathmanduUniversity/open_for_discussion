# Masterclass: Nepali Sentiment Analysis (Case Studies)

> [!IMPORTANT] Gist
> This module compares two distinct paradigms for analyzing Nepali opinions in news and social media: **Rule-Based Lexicons** and **Transformer Fine-tuning**.

## 1. Case Study: Rule-Based Strength Analysis
Based on the research of **Bal Krishna Bal & Patrick Saint-Dizier**, we explore how linguistic constructs determine opinion intensity.
- **Polarity Lexicon**: Mapping words to sentiment scores (e.g., `राम्रो`: +1, `भ्रष्टाचार`: -1.5).
- **Intensifier Logic**:
    - **Amplifiers** (शक्ति बढाउने): `एकदमै` (2.0x).
    - **Downtoners** (शक्ति घटाउने): `अलि` (0.5x).
- **Equation**: $\text{Score} = \text{Base Polarity} \times \text{Intensifier Multiplier}$.

## 2. Case Study: Transformer Fine-tuning (MuRIL)
Utilizing `google/muril-base-cased` to classify sentiment across three classes: **Negative (0), Positive (1), Neutral (2)**.
- **Dataset**: `Shushant/NepaliSentiment`.
- **Methodology**: 3-epoch fine-tuning on sequence classification heads.
- **Evaluation**: Utilizing Confusion Matrices to identify semantic "confusion zones" between Neutral and Positive sentiments.

## 3. Comparative Analysis
| Feature | Rule-Based | Transformer |
| :--- | :--- | :--- |
| **Interpretability** | High (Transparent rules) | Low (Black box) |
| **Data Requirement** | Low (Expert lexicons) | High (Labeled datasets) |
| **Nuance Capture** | Fixed (Hand-coded) | High (Context-aware) |
| **Sarcasm Handling** | Poor | Moderate |

---

**Notebooks**: 
- [sentiment_lexicon_strength.py](notebooks/sentiment_lexicon_strength.py)
- [sentiment_transformer_finetuning.py](notebooks/sentiment_transformer_finetuning.py)

#nepali-nlp #sentiment-analysis #lexicon #transformers #muril #pedagogy
