# Case Study: Nepali Grammar Checker Architecture

> [!IMPORTANT] Gist
> Based on the research by **Bal Krishna Bal & Prajol Shrestha**, a Nepali grammar checker follows a modular pipeline architecture. Each module processes the text and passes its output to the next, similar to an assembly line.

## 1. The Pipeline Architecture (Modular Design)
The system consists of 7 critical stages:
1.  **Tokenizer**: Splitting the stream into sentences and words.
2.  **Morphological Analyzer**: Deconstructing words into roots and affixes.
3.  **POS Tagger**: Assigning parts-of-speech (Noun, Verb, Adj) based on context.
4.  **Chunker & Parser**: Grouping words into phrases (Noun Phrases, Verb Phrases).
5.  **Grammatical Relation Finder**: Identifying Subject, Object, and Verb roles.
6.  **Syntax Checker**: Verifying agreements (Gender, Number, Person).
7.  **Suggestions Module**: Proposing corrections for detected errors.

## 2. Agreement Logic: Subject-Verb-Agreement
In Nepali, the verb must agree with the subject in **Gender (Linga)**, **Number (Vachana)**, and **Person (Purush)**.
- **Example Error**: `केटी घर जान्छ ।`
    - Subject: `केटी` (Feminine)
    - Verb: `जान्छ` (Masculine)
    - **Correction**: `जान्छे` (Feminine)

## 3. Implementation Strategy
- **Rule-Based**: Hardcoded grammatical rules (if-then-else) for high precision.
- **Lexicon Dependency**: Requires a high-fidelity dictionary with gender/number metadata for each noun.

---

**Notebook**: [nepali_grammar_checker_pipeline.py](notebooks/nepali_grammar_checker_pipeline.py)

#nepali-nlp #grammar #pipeline #syntax #morphology #linguistics
