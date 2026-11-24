# Text Classification with Naive Bayes (Food vs. Travel)

> [!IMPORTANT] Gist
> This module demonstrates a simple yet effective text classifier using Multinomial Naive Bayes. It categorizes Nepali sentences into two classes: **खाना (Food)** and **यात्रा (Travel)**, utilizing additive smoothing to handle unseen tokens.

## 1. Feature Extraction: Bag-of-Words
We use `CountVectorizer` to convert Nepali text into numerical feature vectors.
- **Vocabulary**: The set of unique words in the training corpus.
- **OOV Handling**: Words in the test set not found in the training vocabulary are ignored by the vectorizer.

## 2. Multinomial Naive Bayes
- **The Zero-Frequency Problem**: If a word is never seen in a class during training, $P(\text{word}|\text{class}) = 0$, which makes the entire sentence probability zero.
- **Laplace Smoothing ($\alpha=1.0$)**: We add a pseudo-count of 1 to every word in the vocabulary to ensure non-zero probabilities for all terms.

## 3. Visualization: Word Clouds
To understand the "semantic fingerprint" of each class, we generate word clouds.
- **Font Requirement**: Must use a Devanagari `.ttf` font (e.g., Noto Sans).
- **Frequency Mapping**: `WordCloud().generate_from_frequencies(Counter(tokens))`.

---

**Notebook**: [nepali_text_classification_nb.py](notebooks/nepali_text_classification_nb.py)

#nepali-nlp #classification #naive-bayes #wordcloud #scikit-learn #tokenization
