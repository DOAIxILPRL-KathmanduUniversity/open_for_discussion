---
type: concept
title: "Classical NLP Foundations & Machine Learning Methods for Nepali"
description: "Foundational classical NLP algorithms, statistical classifiers, sequence models, morphological analyzers, and preprocessing pipelines applied to Nepali text."
status: active
version: "1.0.0"
timestamp: "2026-11-04T20:00:00Z"
tags:
  - classical-nlp
  - statistical-machine-learning
  - hidden-markov-models
  - naive-bayes
  - support-vector-machines
  - tf-idf
  - morphological-parsing
  - ngram-modeling
provenance:
  source: "ILPRL Research, personal notes archive, Bal et al. publications"
  verified_by: "Antigravity AI Curator"
---

# Classical NLP Foundations & Machine Learning Methods for Nepali

Before the advent of deep transformer-based language models like [[nepalibert]] and [[nepberta]], computational linguistic work on the Nepali language relied on formal grammar rules, finite-state automata, statistical sequence taggers, and classical machine learning algorithms. This node synthesizes the core algorithms, mathematical foundations, and implementation pipelines historically employed for Nepali natural language processing.

---

## 1. Text Cleaning & Normalization

Text preprocessing in Devanagari presents distinct challenges compared to Latin scripts due to conjunct consonants, diacritics (matras), virama (halant `्`), nukta (`़`), and zero-width joiners (`ZWJ` U+200D and `ZWNJ` U+200C).

### Preprocessing Pipeline:
1. **Unicode Normalization**: Converting non-standard glyph representations (e.g. legacy Preeti or Kantipur ASCII encodings converted to Unicode) and applying NFC/NFKD normalization.
2. **Punctuation & Noise Stripping**: Removing non-Devanagari symbols while preserving Devanagari punctuation (e.g., Purna Viram `।` U+0964, Deergh Viram `॥` U+0965).
3. **Stop Words Filtering**:
   - Nepali function words such as postpositions (`मा`, `को`, `का`, `की`, `ले`, `लाई`, `बाट`), pronouns (`म`, `हामी`, `उनी`, `यो`, `त्यो`), and auxiliary verbs (`छ`, `थियो`, `हुन्`, `भयो`, `गर्छ`) represent high-frequency tokens with low domain variance.
   - Domain-specific stop lists filter out over 250 common functional words to reduce vocabulary dimensionality for bag-of-words and TF-IDF vectors.
4. **Affix Removal & Stemming**:
   - Rule-based suffix stripping removes inflections:
     - Plural suffixes: `-हरू` (`-harū`)
     - Case markers (vibhakti): `-मा`, `-को`, `-ले`, `-द्वारा`
     - Verbal inflections: `-दै`, `-एर`, `-एका`, `-नु`, `-नेछ`

---

## 2. Morphological Parsing & Stemming

Nepali is a morphologically rich, agglutinative, and inflectional language where words conjugate extensively based on tense, aspect, mood, person, number, gender, and honorific grade (see [[nepali_morphosyntax_and_grammar]]).

### Early Milestones:
- **Bal (2004)**: *A Morphological Analyzer and a Stemmer for Nepali* (Information and Language Processing Research Lab - [[ilprl]]).
- **Hunspell Nepali Integration**: Developed within LTK ([[ltk]]) and ILPRL, constructing affix files (`.aff`) and root dictionaries (`.dic`) for morphological rule expansion, spelling check, and prefix/suffix stripping.
- **Affix Removal Stemmer**: Shrestha (2014) introduced an algorithmic rule-based stemmer that iteratively applies longest-match suffix stripping rules without relying on an exhaustive dictionary, achieving competitive accuracy for document classification and search indexing.

---

## 3. Feature Representations: TF-IDF & N-Gram Modeling

### N-Gram Modeling:
- **Character N-Grams**: Effective for capturing subword morphology and handling misspellings in low-resource Devanagari text.
- **Word N-Grams**:
  - Unigram, bigram, and trigram language models calculate transition probabilities:
    $$P(w_n \mid w_{n-1}, w_{n-2}) = \frac{C(w_{n-2}, w_{n-1}, w_n)}{C(w_{n-2}, w_{n-1})}$$
  - Applied in early mobile predictive keyboards (e.g. *Nepali Unicode Converter with Personalized Text Predictor using N-gram Model*) and statistical POS tagging.

### TF-IDF (Term Frequency-Inverse Document Frequency):
- Transforms normalized Nepali documents into sparse vector spaces:
  $$\text{TF}(t, d) = \frac{f_{t,d}}{\sum_{t' \in d} f_{t',d}}$$
  $$\text{IDF}(t, D) = \log\left(\frac{1 + |D|}{1 + |\{d \in D : t \in d\}|}\right) + 1$$
  $$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$
- Formed the benchmark input feature for early news genre classification on the [[classification_datasets|16NepaliNews Corpus]].

---

## 4. Sequence Modeling: Hidden Markov Models (HMM)

Hidden Markov Models served as the primary statistical paradigm for Part-of-Speech (POS) tagging prior to Conditional Random Fields (CRFs) and neural networks.

### Mathematical Formulation:
- Let $O = (o_1, o_2, \dots, o_T)$ be a sequence of observed Nepali words.
- Let $S = (s_1, s_2, \dots, s_T)$ be the hidden sequence of grammatical tags (e.g., from [[nepalitagsetpos]]).
- The optimal tag sequence $\hat{S}$ is determined via the Viterbi algorithm maximizing:
  $$\hat{S} = \arg\max_S \prod_{t=1}^T P(o_t \mid s_t) P(s_t \mid s_{t-1})$$
  where $P(o_t \mid s_t)$ is the emission probability and $P(s_t \mid s_{t-1})$ is the transition probability estimated from annotated corpora such as Nelralec NT-01 ([[morphology_pos_papers]]).
- **Trigram POS Taggers**: Implemented by open-source initiatives (e.g. `e911/Nepali-POS-Tagger`) leveraging trigram transition probabilities with smoothing techniques (Good-Turing, Witten-Bell) to handle out-of-vocabulary (OOV) tokens.

---

## 5. Supervised Statistical Classifiers

Evaluated extensively in benchmark literature (e.g. *Nepali News Classification using Naïve Bayes, Support Vector Machines and Neural Networks*):

| Classifier | Mechanism | Strengths on Nepali Text | Limitations |
| :--- | :--- | :--- | :--- |
| **Multinomial Naïve Bayes (MNB)** | Conditional word probability with Laplace ($\alpha=1$) smoothing | Fast training, high baseline accuracy with small sample sizes | Assumes word independence; fails to capture long-range contextual semantics |
| **Support Vector Machines (SVM)** | Maximum margin hyperplane in high-dimensional TF-IDF space (linear & RBF kernels) | Robust against overfitting in sparse vocabulary spaces; high precision | Computational scaling with very large training sets; sensitive to kernel hyperparameters |
| **Feedforward Neural Networks (MLP)** | Multi-layer perceptron with backpropagation on dense or bag-of-words features | Learns non-linear interactions between feature tokens | Lacks sequential memory; replaced by RNNs/Transformers for variable-length text |

---

## 6. Related Nodes & Further Reading

- [[devanagari_nlp]]: Devanagari script mechanics, Unicode blocks, and abugida orthography.
- [[nepali_morphosyntax_and_grammar]]: Detailed grammatical categories, vibhakti markers, and syntax rules.
- [[nepali_nlp_libraries]]: Contemporary Python, Dart, and C++ toolkits implementing these routines.
- [[morphology_pos_papers]]: Published literature on Nepali morphological analysis and POS tagging.
- [[classification_papers]]: Research papers evaluating Naive Bayes, SVM, BiLSTM, and Transformers on Nepali benchmarks.
