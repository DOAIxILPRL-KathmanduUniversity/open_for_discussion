# Spell & Grammar Checking

> [!IMPORTANT] Gist
> Automated error detection systems use a combination of rule-based, statistical, and neural methods to identify and correct orthographic and syntactic deviations in text.

## 1. Spell Checking
- **Non-word error detection**: Finding strings that don't exist in a dictionary.
- **Isolated-word error correction**: Suggesting candidates using **Minimum Edit Distance** (Levenshtein).
- **Context-dependent correction**: Identifying "their" vs. "there" using N-grams or BERT (Jurafsky & Martin, 2026).

## 2. Grammar Checking
- **Syntax-Based**: Using parsers to find trees that don't satisfy the grammar.
- **Statistics-Based**: Flagging low-probability N-gram sequences.
- **Sequence-to-Sequence (GEC)**: Treating grammar correction as a translation task (Bad Text → Good Text).
- **Back-Translation for GEC**: A technique to generate large datasets by "flipping" a small parallel corpus to train a **Spell-Corruptor**.

## 3. Benchmarking & Reality Check
While commercial systems often claim accuracies above 90%, empirical benchmarking reveals significant gaps (Bernstein et al., 2014):
- **Actual F1 Scores**: Studies on student essays show actual F1 values in the range of **0.25 to 0.35** for both sentence and word-level errors.
- **Error Distribution**: Different systems show uniform rates of missed errors (false negatives) but vary wildly in their distribution of **false positives** (incorrect flags).
- **Human vs. Machine**: Unlike humans who infer intent and provide a "model re-write," machines often struggle with the "Intent Inference" problem—the root cause of many pedagogical misfires in automated tutoring.

## 4. Challenges in Indic Languages
- High morphological complexity (agglutination).
- Lack of standardized large-scale error corpora for languages like Gujarati or Nepali (Panchal & Shah, 2025).
- **Morphology-based Systems**: For low-resource languages like Nepali, spell-checkers often integrate **Hunspell** with custom morphological analyzers to handle complex suffixation/prefixation patterns (see [IndoWordNet Extension](../../09_nepali_nlp/indowordnet_extension.md)).

---

#applied #preprocessing #spellcheck #grammar
