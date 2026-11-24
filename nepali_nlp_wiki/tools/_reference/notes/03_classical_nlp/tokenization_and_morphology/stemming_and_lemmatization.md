# Stemming & Lemmatization

## Stemming
- Chop suffixes heuristically (Porter, Snowball)
- Fast but crude — "studies" → "studi"
- Language-dependent rules

## Lemmatization
- Reduce to dictionary form using morphological analysis
- "studies" → "study", "better" → "good"
- Needs POS info for accuracy

## When to Use Which
- **Stemming**: Best for Search Engines (IR) and speed-critical tasks where crude heuristic normalization is acceptable.
- **Lemmatization**: Best for high-precision downstream NLP tasks (Sentiment Analysis, QA) where semantic accuracy is paramount.

## Hybrid Stemming (Advanced)
For morphologically rich languages like Nepali, a two-stage **Hybrid Stemmer** (2013 research) provides superior accuracy:
1.  **Rule-Based Stripping**: Initial suffix/prefix removal using longest-match and incremental heuristics (~150 suffixes).
2.  **Edit Distance Correction**: The stripped word is compared against a root-word database (e.g., ~700 entries). If the **Edit Distance** is below a threshold (e.g., 0.50), the known root is selected.
3.  **Impact**: Improves recall from 68.4% (pure rules) to **72.1%** (hybrid).

## Common Pitfalls (Cuantum, 2024)
- **Over-stemming**: Cutting too much from a word, resulting in different words having the same stem (e.g., "university" and "universe" → "univers").
- **Under-stemming**: Not cutting enough, leaving words that should have the same stem with different ones (e.g., "data" and "datum" remaining distinct).
- **Limitations**: Both techniques struggle with **proper nouns** (NER), acronyms, and irregular verbs if the POS tagger or morphological dictionary is incomplete.

---

#classical #morphology
