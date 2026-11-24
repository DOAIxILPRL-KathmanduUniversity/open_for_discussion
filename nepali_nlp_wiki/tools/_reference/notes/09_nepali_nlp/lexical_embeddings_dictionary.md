# Lexical Embeddings for Nepali Dictionaries

> [!IMPORTANT] Gist
> Mapping the semantic space of traditional Nepali lexicons (Dictionary/WordNet) into vector space using **MuRIL** to enable intelligent semantic search and word sense disambiguation.

## 1. Data Structure
The process involves flattening dictionary entries:
- **Input**: `(id, word, sense)` from a TSV source.
- **Combined Context**: We construct a semantic string: `"[WORD] means [SENSE]"`.

## 2. Embedding Generation (MuRIL)
We use `google/muril-base-cased` for its superior Devanagari representation.
- **Pooling Strategy**: Mean pooling of the last hidden states to generate a fixed 768-dimensional vector for each dictionary entry.
- **Batch Processing**: Utilizing `tqdm` and GPU acceleration to handle tens of thousands of dictionary entries efficiently.

## 3. Applications
- **Semantic Search**: Finding synonyms based on "sense" rather than just surface spelling.
- **Word Sense Disambiguation (WSD)**: Comparing context vectors of a sentence with dictionary entry vectors to find the closest match.
- **Sovereign WordNet**: Building a graph-based representation of the Nepali language where nodes are these lexical embeddings.

---

**Notebook**: [dictionary_embedding_gen.py](notebooks/dictionary_embedding_gen.py)

#nepali-nlp #dictionary #muril #embeddings #lexical-semantics #wsd
