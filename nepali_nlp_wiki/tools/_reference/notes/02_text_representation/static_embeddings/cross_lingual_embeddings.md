# Masterclass: Cross-Lingual Word Embeddings (CLWE)

> [!IMPORTANT] Gist
> Cross-lingual embeddings map words from different languages into a shared vector space, allowing a model trained on high-resource data (Hindi) to generalize to low-resource data (Nepali).

## 1. The Alignment Problem
Monolingual embeddings (like Word2Vec or FastText) are language-specific. "Apple" (English) and "स्याउ" (Nepali) will have completely different coordinates. CLWE solves this by:
1.  **Shared Vocabulary**: Training on a concatenated corpus (rarely effective for distant languages).
2.  **Mapping/Alignment**: Learning a transformation matrix $W$ such that $Source \cdot W \approx Target$.

## 2. Technical Implementation: VecMap
For the Hindi-Nepali alignment, we employ **VecMap**, a state-of-the-art framework for semi-supervised embedding mapping.

### The Mapping Process
1.  **Seed Dictionary**: A small dictionary (`hi-ne.dic`) is used as a supervised signal.
2.  **Orthogonal Mapping**: VecMap learns an orthogonal transformation that minimizes the distance between dictionary pairs.
3.  **Iterative Refinement**: The mapping is iteratively refined by inducing a new dictionary from the current alignment and retraining.

### Retrieval Evaluation (CSLS)
Standard nearest-neighbor retrieval suffers from the **Hubness Problem** (some vectors appear as neighbors to many others). We use **Cross-Domain Similarity Local Scaling (CSLS)** to penalize hubs and improve translation accuracy.

## 3. Hindi-Nepali Case Study
Using aligned FastText embeddings, we can perform **Lemma Filtering** to create a high-fidelity semantic bridge.

### Lemma Filtering Strategy
For many tasks (MT, IR), inflected forms (e.g., "doing", "did") add noise. Filtering embeddings to only include **Lemmas** (root forms like "do") provides:
- **Reduced Noise**: Focusing on core semantic concepts.
- **Improved Performance**: Smaller, higher-density vector files that are easier to load and search.

### Workflow
1.  **Download**: Pull aligned `.vec` files from HuggingFace.
2.  **Filter**: Intersect the vocabulary with a pre-validated list of unique lemmas.
3.  **Validate**: Ensure the vector headers (word count, dimensions) are correctly updated to maintain compatibility with tools like `gensim`.

## 3. Key Findings
- **Hindi Coverage**: ~52k lemmas filtered from a larger set of 78k.
- **Nepali Coverage**: ~34k lemmas filtered from 113k.
- **Result**: A shared Hi-Ne space where root concepts are perfectly aligned for cross-lingual transfer.

---

## 4. Semantic Enrichment: WordNet & ImageNet Mappings
Beyond simple word pairs, we can enrich our shared vector space using lexical databases like **WordNet**.

### WordNet Definition Extraction
By mapping WordNet IDs (e.g., `n02084071` for "dog") to their definitions, we add a semantic layer to the embeddings. 
- **Method**: Use NLTK's `wordnet.synset_from_pos_and_offset(pos, offset)` to retrieve human-readable definitions.

### Cross-Lingual Similarity Search
Using aligned **English-Nepali embeddings**, we can automatically find the best Nepali equivalent for an English WordNet entry:
1.  **Preprocessing**: Clean the English term (remove parentheses, handle synonyms).
2.  **Cosine Similarity**: Calculate the distance between the English vector and all Nepali vectors.
3.  **Batch Processing**: To avoid $O(N^2)$ memory errors during large-scale mapping (e.g., all of ImageNet), process words in **batches of 5,000**.

---

**Notebooks**: 
- [cross_lingual_filter.py](notebooks/cross_lingual_filter.py) (Filtering)
- [wordnet_enrichment.py](notebooks/wordnet_enrichment.py) (Batched Similarity Search)

#clwe #embeddings #hindi #nepali #alignment #nlp-engineering #wordnet
