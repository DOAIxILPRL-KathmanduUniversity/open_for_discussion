# FastText & Subword Embeddings

> [!IMPORTANT] Gist
> FastText extends Word2Vec by representing each word as a bag of character n-grams. This allows the model to capture morphological information and handle Out-of-Vocabulary (OOV) words.

## 1. The Morphological Problem
Standard Word2Vec/GloVe assign a unique vector to every word. This fails for:
- **Rare Words**: Words seen once or twice have poor embeddings.
- **OOV Words**: Unknown words have no vector at all.
- **Morphology**: "Eating," "Eaten," and "Eats" are treated as completely different entities, ignoring their shared root.

## 2. FastText Architecture (Bojanowski et al., 2017)
Instead of whole words, FastText breaks words into character n-grams.
- **Example**: Word `<apple>` with $n=3$:
    - `<ap`, `app`, `ppl`, `ple`, `le>`
- **Word Vector**: The sum of the vectors of its character n-grams.
- **Training**: Uses the Skip-gram objective but with subword components.

## 3. Advantages
- **Robustness to Typos**: A typo in one character still allows the model to match most other n-grams.
- **Low-Resource & Morphological Richness**: Essential for languages like Nepali, Turkish, or Finnish, where words are highly inflected.
- **OOV Handling**: Can generate a vector for a brand-new word by summing its constituent n-grams.

## 4. Subword Tokenization (BPE & WordPiece)
While FastText uses character n-grams, modern Transformers use **Byte Pair Encoding (BPE)** or **WordPiece**:
- **BPE**: Iteratively merges the most frequent pairs of characters into subword units.
- **Balance**: Keeps frequent words as single units while breaking rare words into common chunks (e.g., `un-`, `-ing`).

---

#representation #embeddings #fasttext #subwords #morphology
