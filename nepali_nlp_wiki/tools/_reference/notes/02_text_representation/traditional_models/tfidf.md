# TF-IDF

## Formula
- **TF(t, d)** = count of term t in document d / total terms in d
- **IDF(t)** = log(N / df(t)) where N = total docs, df = doc frequency
- **TF-IDF** = TF × IDF

## Intuition
- Upweights terms that are frequent in a document but rare across corpus
- Downweights common words (the, is, a)

## Usage
- Document retrieval and ranking
- Feature extraction for classification
- `TfidfVectorizer` in scikit-learn

---

**Notebook**: [bow_tfidf_lab.py](notebooks/bow_tfidf_lab.py)

#representation #classical
