# Related & Low-Resource Language NLP

> [!IMPORTANT] Gist
> Related languages (descended from a common ancestor or in geographical proximity) share significant phonological, morphological, and lexical properties. Utilizing these "similarities" is the key to building robust NLP systems for low-resource languages like Nepali, Hindi, and Marathi (Kunchukuttan & Bhattacharyya, 2022).

## 1. Language Relatedness Properties
- **Origins**: Common parent (e.g., Sanskrit for Indic languages) or long-term contact (Sprachbund).
- **Lexical Overlap**:
    - **Tatsam Words**: Words borrowed directly from the parent (e.g., Sanskrit words in Bengali).
    - **Tadbhav Words**: Derived/evolved words (e.g., "Chandra" $\to$ "Chaand").
    - **Cognates**: Words with the same origin and similar sound/meaning across languages.
- **Isomorphism**: Related languages often share word order (SOV for Indic) and morphological structures (postpositions).

## 2. Subword Units for Related Languages
Standard word-level models suffer from data sparsity in low-resource settings. Breaking words into subwords captures shared roots.
- **Orthographic Syllables (OS)**: A linguistic unit defined as $C^*V$ (zero or more consonants followed by the first vowel). 
    - *Example*: "little" $\to$ "li", "ttle".
    - *Benefit*: Captures phonological patterns better than arbitrary subwords.
- **Byte Pair Encoding (BPE)**: A data-driven method that iteratively merges the most frequent pairs of characters/sequences.
    - *Benefit*: Robust to out-of-vocabulary (OOV) words by falling back to character sequences.

## 3. Translation & Transliteration
### A. Script Transfer (Transliteration)
For languages like Hindi and Urdu, which are mutually intelligible but use different scripts (Devanagari vs. Perso-Arabic), NLP often boils down to **transliteration**.
- **Ambiguity**: One-to-many mappings (e.g., "a" in Roman mapping to different vowel lengths in Devanagari).
- **Multilingual Neural Transliteration**: Training a single model on multiple related language pairs to enable **zeroshot** transliteration for unseen pairs.

### B. Pivot-based Translation
If no parallel corpus exists between Language A and Language B, a related Language C (Pivot) is used.
- **Triangulation**: $A \to C$ and $C \to B$.
- **Subword Pivoting**: Using subword units in the pivot language significantly reduces the "bottleneck" effect of OOV words during the transfer.

## 4. Indic NLP Systems
- **Anusaaraka**: A system designed to make one Indian language accessible to another by providing a "near-word-for-word" transfer with grammatical transparency.
- **AnglaBharati**: A machine-aided translation system specifically for English to Indian languages using a pseudo-interlingua approach.
- **IndoWordNet**: A linked lexical knowledge base of wordnets for Indic languages. Current research focuses on extending the Nepali component (~11k synsets) to match Hindi (~40k synsets) by leveraging cross-lingual alignment (see [IndoWordNet Extension](indowordnet_extension.md)).

---

#nepali #indic #related-languages #low-resource #transliteration #subwords
