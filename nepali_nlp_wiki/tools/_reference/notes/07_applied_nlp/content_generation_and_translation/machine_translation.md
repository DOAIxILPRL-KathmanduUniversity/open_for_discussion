# Machine Translation & Translation Theory

> [!IMPORTANT] Gist
> Machine Translation (MT) focuses on the computational transfer of meaning, while Translation Theory (e.g., **Skopos Theory**) emphasizes the communicative purpose and cultural adaptation of the text. Integrating these perspectives allows for "functionally loyal" translations (Nord, 2005).

## 1. Generational Evolution
MT has traversed four paradigms of ambiguity resolution:
1. **RBMT (Rule-Based)**: Using bilingual dictionaries and grammar rules (Interlingua, Transfer).
2. **EBMT (Example-Based)**: Using analogous past translations.
3. **SMT (Statistical)**: Modeling translation as a noisy channel problem $P(T|S) \propto P(S|T)P(T)$ (e.g., IBM Models, Phrase-Based SMT).
4. **NMT (Neural)**: End-to-end learning via Encoder-Decoder and Transformers.

## The Vauquois Triangle
A visualization of MT depth:
- **Direct**: Word-for-word substitution (base).
- **Transfer**: Syntactic/Semantic mapping between specific languages (middle).
- **Interlingua**: Mapping to a universal language-neutral representation (apex).

## 3. Key Concepts
- Parallel corpora for training.
- **Beam Search**: A heuristic search algorithm used for decoding.
- **BPE Tokenization**: A data-driven subword method for handling an open vocabulary.

## 4. Language Typology & Word Order
Most world languages follow specific structural patterns:
- **SOV (Subject-Object-Verb)**: Most common (e.g., Japanese, Korean, Nepali, Hindi).
- **SVO (Subject-Verb-Object)**: Second most common (e.g., English, Chinese, Spanish).
- **VSO (Verb-Subject-Object)**: Found in Arabic and Irish.

## 5. Evaluation Metrics
- BLEU score (n-gram precision).
- COMET, BLEURT (learned metrics).
- chrF for character-level matching.

## 6. Machine Translation for Related Languages
Specialized techniques exploit the linguistic similarity between related pairs (Kunchukuttan & Bhattacharyya, 2022).
- **Subword-level SMT**: Using units like **Orthographic Syllables** (C*V) or **BPE** to overcome vocabulary sparsity. Subwords allow the model to learn mappings between similar stems and suffixes that word-level models would miss.
- **Pivot-based SMT**: Using a high-resource related language as a "bridge."
    - **Pivoting via Subwords**: Significant performance gains are achieved when the pivot language also uses subword units, reducing the bottleneck of OOV words in the source-pivot-target chain.
- **Multilingual NMT**: A single model trained on many related languages (e.g., Indic mBART) can outperform bilingual models by sharing morphological and syntactic knowledge across the "family."

## 7. Indic-Specific Architectures
- **Anusaaraka**: A "language-access" system focusing on word-level transparency between Indian languages.
- **Sampark**: A project involving multiple Indian IITs to build a unified machine translation framework for major Indian languages.
- **Nepali-Hindi Case Study**: Leveraging IndoWordNet (IWN) to bridge the synset gap (11k vs 40k) for statistical paraphrasing and translation. By aligning Nepali lexical resources with the Hindi WordNet pivot, models can achieve higher BLEU scores through improved context-aware semantic mapping (see [IndoWordNet Extension](../../09_nepali_nlp/indowordnet_extension.md)).

---

#applied #mt
