# Coreference & Entity Linking

> [!IMPORTANT] Gist
> Coreference resolution identifies all expressions that refer to the same real-world entity. Entity linking (or Disambiguation) connects these mentions to a specific entry in a knowledge base like Wikipedia (Jurafsky Ch 23).

## 1. Coreference Phenomena
- **Anaphora**: A word (often a pronoun) referring back to an antecedent (e.g., "**John** is here. **He** is tall.").
- **Cataphora**: Referring forward (e.g., "In **his** final speech, **the President**...").
- **Winograd Schema**: Sentences where a pronoun is ambiguous and requires world knowledge to resolve (e.g., "The trophy didn't fit in the suitcase because **it** was too large.").

## 2. Coreference Algorithms
- **Neural Mention-Ranking**: The current state-of-the-art. It learns a score for every pair of mentions to determine if they refer to the same entity.
- **Sieve-based Models**: A series of rules (sieves) applied from highest to lowest precision.

## 3. Entity Linking (Disambiguation)
Mapping a mention (e.g., "Apple") to the correct entry in a Knowledge Base.
- **Candidate Generation**: Identifying all possible entities for a string.
- **Candidate Ranking**: Using context similarity and link popularity to find the best match.

## 4. Discourse Coherence
How a text "hangs together."
- **Centering Theory**: A framework for modeling local coherence and salience of entities across sentences (Jurafsky Ch 24).

---

#discourse #coreference #entity-linking
