# Machine Transliteration

> [!IMPORTANT] Gist
> Transliteration is the process of transforming text from one script to another while preserving the sound (phonetic structure). It is critical for handling named entities, technical terms, and cross-script information retrieval (Kunchukuttan & Bhattacharyya, 2022).

## 1. The Transliteration Task
Unlike translation, which preserves meaning, transliteration preserves **sound**.
- **Source**: "Khan" (Roman)
- **Target**: "खान" (Devanagari)
- **Challenge**: The "One-to-Many" mapping problem. A single character in the source script can map to multiple phonetically distinct characters in the target script depending on context.

## 2. Methodologies
### A. Rule-Based
- **Hand-crafted Grapheme-to-Phoneme (G2P) rules**.
- Limited by the complexity of phonological irregularities and "borrowed" words.

### B. Statistical (SMT-based)
- Treating transliteration as a "translation" problem at the character level.
- **Character-level SMT**: Learning alignments between character sequences.

### C. Neural Transliteration
- **Sequence-to-Sequence (Seq2Seq)**: Using LSTMs or Transformers to map source character sequences to target character sequences.
- **Multilingual Neural Transliteration**: Training on multiple language pairs (e.g., Hindi-English, Marathi-English, Bengali-English) to share the "script-to-script" knowledge.
- **Zeroshot Transliteration**: The ability of a multilingual model to transliterate between a language pair it has never seen during training (e.g., Punjabi to Tamil) by leveraging the shared phonetic space.

## 3. Unsupervised Transliteration
When no parallel "name" lists exist, models can learn from monolingual corpora.
- **Orthographic Similarity**: Using the fact that related languages often have similar grapheme-to-phoneme mappings.
- **Linguistically Informed Priors**: Injecting phonetic knowledge (e.g., which consonants are similar) into the learning process to guide the unsupervised alignment.

## 4. Evaluation Metrics
- **ACC (Top-1 Accuracy)**: Does the model's top prediction match the gold standard?
- **Mean F-Score**: Measuring the character-level overlap (edit distance) between the predicted and gold strings.
- **MRR (Mean Reciprocal Rank)**: Assessing where the correct transliteration appears in the top $N$ results.

---

#applied #transliteration #zeroshot #multilingual #phonetics
