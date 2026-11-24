# Authorship Attribution

> [!IMPORTANT] Gist
> Authorship attribution (stylometry) uses quantitative linguistic features to identify the most likely author of a text. This field combines NLP with forensic linguistics and probability theory (Sharp & Delmonte, 2014).

## 1. Key Features for Attribution
Authors have unique "stylistic fingerprints" reflected in their writing patterns:
- **Function Words**: Frequent, low-content words (e.g., *the, and, of*) are often the strongest indicators of authorship. A **Bag-of-Words** approach for function words is more robust than for content words, as function word usage is largely subconscious (Boukhaled & Ganascia, 2014).
- **Sequential Rules**: Analyzing the order of specific word classes or grammatical structures.
- **Punctuation & Syntax**: Frequency of semicolons, average sentence length, and syntactic structure complexity.
- **Lexical Richness**: Type-Token Ratio (TTR) and vocabulary diversity metrics.

## 2. Computational Methods
- **Distance Metrics**: Measuring the delta between the target text's feature vector and known author profiles.
- **Machine Learning**: Classifiers (SVM, Random Forests) trained on balanced corpora of known authors.
- **Sequential Rule Mining**: Identifying recurring patterns of function words that characterize an author's style (Sharp & Delmonte, 2014).

## 3. Challenges
- **Short Texts**: Performance degrades significantly on tweets or short messages.
- **Adversarial Stylometry**: Authors deliberately mimicking or hiding their style (e.g., the Federalist Papers dispute).
- **Imbalanced Corpora**: Having much more text from one author than others in the candidate set.

---

#applied #stylometry #authorship #forensic-linguistics
