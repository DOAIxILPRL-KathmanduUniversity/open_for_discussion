# Statistical Laws: Zipf and Heaps

> [!IMPORTANT] Gist
> Natural language text is not random; it follows predictable statistical distributions. Understanding these laws is essential for corpus modeling, compression, and vocabulary design.

## 1. Zipf's Law
Zipf's Law states that the frequency of any word is inversely proportional to its rank in the frequency table.
- **The Formula**: $f(w) \propto \frac{1}{rank(w)}$
- **Observation**: The most frequent word (rank 1) occurs twice as often as the second most frequent (rank 2), three times as often as the third, and so on.
- **Implication**:
    - A few "head" words (stopwords like *the, of, and*) account for most of the tokens in a corpus.
    - A massive number of "long-tail" words (Hapax Legomena) appear only once.
    - **Sparsity**: Even in massive corpora, we will always encounter words we haven't seen before.

## 2. Heaps' Law
Heaps' Law describes how the vocabulary size ($V$) grows with the size of the corpus ($N$).
- **The Formula**: $V = k N^{\beta}$
- **Typical Values**: $10 \le k \le 100$ and $0.4 \le \beta \le 0.6$.
- **Observation**: Vocabulary growth is sub-linear. As we process more text, the rate at which we discover new words decreases, but it never stops.
- **Implication**: There is no such thing as a "complete" dictionary for a natural language; the lexicon is open-ended.

## 3. Benford's Law (NLP Context)
While Benford's Law usually applies to the leading digits of numerical data, in NLP, it can be seen in the distribution of word frequencies across different genres or the frequency of certain syntactic structures.

## 4. Why It Matters for NLP
- **Preprocessing**: Justifies the removal of stopwords (Zipf's head) and the handling of OOV words (Zipf's tail).
- **Indexing**: Predicts the size of inverted indexes in Information Retrieval.
- **Efficiency**: Guides subword tokenization (BPE, WordPiece) to capture the most frequent chunks and minimize the "long tail" of unknown characters.

---

#foundations #statistics #zipf #heaps #corpus-linguistics
