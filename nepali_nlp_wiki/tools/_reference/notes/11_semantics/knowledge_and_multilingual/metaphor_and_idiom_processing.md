# Metaphor & Idiom Processing

> [!IMPORTANT] Gist
> Natural language is non-literal. Metaphors (conceptual mappings) and Idioms (fixed multi-word expressions) pose a significant challenge for NLP models that rely on the compositional sum of word meanings.

## 1. The Literal vs. Non-Literal Gap
- **Literal**: "The window is broken" (The physical object is shattered).
- **Metaphorical**: "He broke my heart" (Emotional pain described via physical damage).
- **Idiomatic**: "He kicked the bucket" (Meaning = died; has nothing to do with kicking or buckets).

## 2. Idiom Detection (MWEs)
**Multi-Word Expressions (MWEs)** are phrases where the meaning is non-compositional.
- **Statistical Identification**: Using Pointwise Mutual Information (PMI) to find words that appear together more often than by chance.
- **Syntactic Fixedness**: Literal phrases allow transformation (e.g., "The cat chased the mouse" $\rightarrow$ "The mouse was chased by the cat"). Idioms often don't ("He kicked the bucket" $\neq$ "The bucket was kicked by him" in the sense of dying).

## 3. Metaphor Identification
Metaphors involve mapping a **Source Domain** (concrete) to a **Target Domain** (abstract).
- **Selectional Preference Violation**: A metaphor often violates the expected properties of a verb's argument.
    - *Example*: "Drink the information." Information is not a liquid, so "drink" is used metaphorically.
- **Conceptual Mapping (Lakoff & Johnson)**: "ARGUMENT IS WAR," "TIME IS MONEY."
- **Neural Approaches**: Using Transformer embeddings to detect "out-of-context" word usage where a word's vector is far from its neighbors in a literal sense.

## 4. NLP Challenges
- **Translation**: Idioms almost never translate literally (e.g., German "Pech haben" $\rightarrow$ "to have bad luck," not "to have pitch").
*   **Sentiment Analysis**: "This movie is a bomb" (Negative) vs. "This movie is the bomb" (Positive).
- **NLU**: Models must decide when to "stop being literal" and look for abstract mappings.

---

#semantics #metaphor #idioms #mwe #figurative-language
