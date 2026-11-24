# Architecture: Modular Nepali Grammar Checker

> [!IMPORTANT] Gist
> A comprehensive Nepali grammar checker requires a deeply rooted linguistic pipeline, transitioning from morphological analysis to feature-structure based agreement checking (SOV patterns).

## 1. The Pipeline Architecture

| Module | Purpose |
| :--- | :--- |
| **1. Tokenizer** | Splits paragraphs → sentences → words. |
| **2. Morphological Analyzer** | Identifies root words and affixes; performs initial (ambiguous) POS tagging. |
| **3. POS Tagger** | Resolves ambiguities using contextual rules (e.g., adjective precedes noun). |
| **4. Chunker & Parser** | Identifies phrases (Noun Phrase, Verb Phrase) using Context-Free Grammar (CFG) for Nepali. |
| **5. Grammatical Relation Finder** | Assigns roles (**Subject, Object, Verb**) based on Paninian Karaka theory. |
| **6. Syntax Checker** | Verifies **SOV** patterns and Subject-Verb agreement features. |
| **7. Suggestion Engine** | Generates corrections for detected syntactic violations. |

## 2. Key Linguistic Components
- **Agreement Mapping**: Handling complex agreement in gender, number, person, and **formality** (Honorifics).
- **Case Marking**: Correctly identifying `le` (ergative), `laai` (accusative), etc., and their impact on sentence structure.
- **Lexical Resources**: Dependent on high-quality lexicons, word-breaking rules, and feature-structure grammars.

---

#nepali #grammar-checker #architecture #parsing #morphology #paninian-grammar
