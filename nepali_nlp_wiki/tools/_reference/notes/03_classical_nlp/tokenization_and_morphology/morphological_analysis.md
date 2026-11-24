# Morphological Analysis

> [!IMPORTANT] Gist
> Morphology is the study of how words are formed from smaller meaningful units called **morphemes**. While stemming simply chops words, morphological analysis identifies the functional and semantic role of each part.

## 1. Morphemes: The Atoms of Meaning
- **Free Morphemes**: Can stand alone as a word (e.g., `cat`, `walk`).
- **Bound Morphemes**: Must be attached to others (e.g., `-s`, `un-`, `-ed`).
    - **Prefixes**: `un-`, `pre-`, `re-`
    - **Suffixes**: `-ing`, `-ly`, `-tion`
    - **Infixes**: Inserted inside a root (rare in English, common in Tagalog or Arabic).

## 2. Derivational vs. Inflectional
- **Inflectional Morphology**: Modifies a word's grammatical form without changing its core meaning or category (e.g., `walk` $\rightarrow$ `walking`, `walks`, `walked`).
- **Derivational Morphology**: Creates new words with different meanings or categories (e.g., `happy` (Adj) $\rightarrow$ `happiness` (Noun), `unhappy` (Opposite)).

## 3. Computational Approaches
- **Finite-State Transducers (FST)**: A mathematical model for mapping surface forms (e.g., `cats`) to lexical forms (e.g., `cat + N + PL`).
- **Two-Level Morphology**: Distinguishes between the *Lexical* level (abstract representation) and the *Surface* level (what is actually written).
- **Subword Modeling**: Modern neural models use BPE or WordPiece to approximate morphology without explicit linguistic rules.

## 4. Why It Matters
- **Low-Resource Languages**: Crucial for languages like Nepali, where a single verb can have hundreds of inflected forms.
- **Search & Retrieval**: Lemmatization (morphological) is superior to stemming (rule-based chopping) for accuracy.
- **Machine Translation**: Understanding that "played" is "play + past tense" helps in translating to languages with different tense systems.

---

#classical #morphology #linguistics #fst #lemmatization
