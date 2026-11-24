# Word2Vec & GloVe

## Word2Vec (Mikolov et al., 2013)
- **CBOW**: predict center word from context
- **Skip-gram**: predict context from center word
- Dense vectors (50–300 dims) capture semantic similarity
- `king - man + woman ≈ queen`

## The Distributional Hypothesis
The foundational concept of word embedding techniques: **"You shall know a word by the company it keeps"** (Firth, 1957).
- Embeddings use statistical co-occurrence data to map linguistic patterns into dense vectors.
- Standard embeddings (Word2Vec, GloVe) are non-contextual; they don't directly account for word order within a sentence (Cavicchio, 2025).

## GloVe (Pennington et al., 2014)
- Global co-occurrence matrix factorization.
- Combines global statistics with local context windows.

## FastText (Bojanowski et al., 2017)
- **Subword Information**: Represents each word as a bag of **character n-grams**.
- **OOV Handling**: Can generate embeddings for "Out-of-Vocabulary" words by summing the vectors of their constituent n-grams.
- **Agglutinative Support**: Particularly effective for morphologically rich languages (Cuantum, 2024).

## Comparison of Static Embeddings
| Feature | Word2Vec | GloVe | FastText |
| :--- | :--- | :--- | :--- |
| **Training** | Local context window | Global co-occurrence | Local + N-grams |
| **Logic** | Predictive (Neural) | Count-based (Factorization) | Predictive (N-gram) |
| **OOV words** | Fails (assigned `<UNK>`) | Fails (assigned `<UNK>`) | **Supported** (via subwords) |
| **Morphology** | Ignored | Ignored | **Captured** |

## Skip-Gram Objective Function
The goal of the Skip-Gram model is to predict surrounding context words given a central word $w_t$. The objective function $L_\theta$ to be minimized is (Mikolov et al., 2013; Hayinaer et al., 2025):

$$L_\theta = -\frac{1}{T} \sum_{t=1}^{T} \sum_{-n \le j \le n, j \ne 0} \log P(w_{t+j} | w_t)$$

Where:
- $T$ is the total number of words in the corpus.
- $n$ is the window size (context radius).
- $P(w_{t+j} | w_t)$ is the probability of context word $w_{t+j}$ occurring given $w_t$.

## Morphological Word Embedding
- In morphologically rich or low-resource languages (e.g., Kazakh), semantic features can be enhanced by training embeddings on both **words** and **stems** (Hayinaer et al., 2025).
- Combining word and stem-level representations helps mitigate the data sparsity problem caused by complex agglutinative suffixation.

---

**Notebook**: [word_vectors_explorer.py](notebooks/word_vectors_explorer.py)

#representation #embeddings #deep-learning
