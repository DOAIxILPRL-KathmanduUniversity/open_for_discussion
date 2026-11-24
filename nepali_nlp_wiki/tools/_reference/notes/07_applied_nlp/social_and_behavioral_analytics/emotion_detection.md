# Emotion Detection

> [!IMPORTANT] Gist
> Emotion detection extends sentiment analysis by mapping text to specific categorical labels (e.g., Ekman’s six basic emotions) or continuous dimensions (Valence-Arousal-Dominance). The core challenge lies in disambiguating context-dependent semantics, sarcasm, and negation which simple rule-based models often fail to capture (Cavicchio, 2025).

## 🎓 Lecturer's Overview: Why It Matters
While sentiment analysis tells us if a review is "good" or "bad," emotion detection captures the **nuance** of the human experience. Understanding if a user is *angry* versus *sad* allows for significantly more tailored responses in customer service or mental health monitoring.

### The Complexity of Language
Language is rarely literal. Consider these pedagogical hurdles:
- **Sarcasm**: "Great, another Monday morning!" (Positive word `great` used for negative emotion).
- **Ambiguity**: "I'm feeling blue about the clear blue sky." (Emotion `blue` vs. Color `blue`).
- **Mixed Emotions**: "I’m somewhat happy with the performance, but it could be better."

## 🔬 Researcher's Synthesis: Theoretical Models

### 1. Categorical Models
Distills emotions into discrete buckets.
- **Ekman's Model**: Anger, Disgust, Fear, Joy, Sadness, Surprise.
- **Plutchik's Wheel**: 8 primary emotions with binary scoring (Mohammad & Turney, 2013).

### 2. Dimensional Models (VAD)
Maps emotions onto a continuous multidimensional space:
- **Valence**: Positive vs. Negative spectrum.
- **Arousal**: Level of activation (Excited vs. Calm).
- **Dominance**: Level of control/influence over the situation.
- **Expectancy Tension**: A proposed new dimension related to anticipation and surprise (Grgić et al., 2022).

## Methods of Detection

### Rule-Based Systems
- **Lexical Affinity**: Assigns a probability score to words based on their association with emotions.
- **Pros**: Easy to implement, highly interpretable.
- **Cons**: Manual labor (time-intensive), poor generalization, fails on sarcasm/negation.

### Machine Learning (Supervised)
- **Features**: Tokenization, stemming, and **Emotion-Aware Word Embeddings** (integrating lexicons like NRC into vectors).
- **Classifiers**: SVM, Naive Bayes, Random Forest, and LSTMs.
- **Note**: Supervised models adapt over time but require expensive annotated datasets.

### Machine Learning (Unsupervised)
- **Clustering**: Grouping sentences with similar word usage patterns.
- **Dimensionality Reduction**: Using **LSA**, **NMF**, or **PCA** to find latent emotional structures in unlabeled data.

## 🛠️ Practice-Based Scaffolding: Disambiguation
To improve accuracy, modern systems pair lexical methods with:
1. **Syntactic Parsing**: Understanding the relationship between modifiers and targets.
2. **Context-Sensitive Analysis**: Differentiating "blue sky" from "feeling blue."
3. **Sentiment Embeddings**: Using vectors that explicitly encode polarity (Tang et al., 2016).

---

## ## Check for Understanding
1. Why does the "Bag of Words" approach often fail for emotion detection in social media text?
2. How does the VAD model differ from Ekman's categorical model in terms of data representation?

---

**Notebook**: [emotion_classification_lab.py](notebooks/emotion_classification_lab.py)

#applied #sentiment #emotion #classification
