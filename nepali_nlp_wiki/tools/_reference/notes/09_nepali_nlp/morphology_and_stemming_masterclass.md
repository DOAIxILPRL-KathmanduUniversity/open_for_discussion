# Masterclass: Nepali Morphology and Stemming

> [!IMPORTANT] Gist
> Nepali is a highly agglutinative language where words are formed by adding multiple suffixes to a root. This module covers rule-based stemming (`Snowball`) and unsupervised morphological segmentation (`Polyglot/Morfessor`).

## 1. Rule-Based Stemming (Snowball)
Stemming reduces words to their base form by stripping common suffixes (e.g., `गरिरहेका` -> `गर`).
- **Tool**: `snowballstemmer.NepaliStemmer`.
- **Strength**: Fast and efficient for IR (Information Retrieval).
- **Weakness**: Often "over-stems" or fails on irregular verbs.

## 2. Unsupervised Morphological Analysis (Polyglot)
Unlike rule-based stemmers, `Polyglot` (using `Morfessor`) learns to segment words into morphemes based on statistical distributions in a large corpus.
- **Task**: `morph2` (Morphemes).
- **Example**: `सरकारका` -> `['सरकार', 'का']`.
- **Advantage**: Captures nuanced grammatical markers (post-positions) that simple stemmers ignore.

## 3. Recursive Morphological Analysis
For words with multiple suffixes (e.g., `किसानहरूले` -> `किसान` + `हरू` + `ले`), a simple one-pass stemmer fails. We implement a **Recursive Suffix Stripper**:
1.  **Longest Match**: Identify the longest valid suffix from the `Affix Rules`.
2.  **Strip & Recurse**: Remove the suffix and repeat the process on the remaining stem until the stem exists in the `Lexicon`.
3.  **Backtracking**: If a path fails, try the next longest suffix.

| Feature | Snowball Stemmer | Polyglot Morph | Recursive Stripper |
| :--- | :--- | :--- | :--- |
| **Logic** | Suffix-stripping rules | Statistical | Recursive Rules |
| **Output** | Single root | List of morphemes | Full Decomposition |
| **Use Case** | Search indexing | Linguistic analysis | Grammar Checking |

---

## 4. Research References
- **Balaram Prasain (2011)**: Established the core computational model for Nepali morphology.
- **Bal Krishna Bal**: Authored the foundational affix-removal stemmer widely used in the community.
- **Hardie et al. (2009)**: Introduced the Nelralec categorisation scheme for morphosyntactic analysis.
- **Adhikari & Neupane (2020)**: Improved performance on Sanskrit-borrowed words using vowel-based splitting.

**Notebook**: [nepali_morphology_stemming.py](notebooks/nepali_morphology_stemming.py)

#nepali-nlp #morphology #stemming #snowball #polyglot #morfessor
