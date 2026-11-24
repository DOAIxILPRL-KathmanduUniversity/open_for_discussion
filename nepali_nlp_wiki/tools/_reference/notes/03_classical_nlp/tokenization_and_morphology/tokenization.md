# Tokenization

## What & Why
- Splitting text into meaningful units (tokens)
- Foundation of every NLP pipeline

## Approaches
- **Whitespace** — naive, fails on punctuation
- **Rule-based** — regex, language-specific rules
- **Subword** — BPE, WordPiece, Unigram (modern standard)
- **Character-level** — fine-grained, large sequences
- **Dictionary-based** — FMM, BMM (used for continuous scripts like Devanagari)

### Dictionary-based Segmentation (Maximum Matching)
For scripts where words are not always clearly separated by whitespace, we use **Maximum Matching** algorithms:

1.  **Forward Maximum Matching (FMM)**:
    - Starts at the beginning of the string.
    - Scans forward to find the longest possible word that exists in the dictionary.
    - *Greedy Approach*: Assumes longer words are more likely to be correct.

2.  **Backward Maximum Matching (BMM)**:
    - Starts at the end of the string.
    - Scans backward to find the longest word.
    - *Often more accurate*: Language-specific nuances (like Devanagari compound words) are often better captured from right-to-left.

3.  **The Bi-directional Method**: If FMM and BMM produce different counts, the one with fewer tokens is typically preferred.

## Sentence Splitting Challenges
Identifying sentence boundaries is non-trivial due to:
- **Abbreviations**: "U.S.", "St.", "mln" confuse simple period-based splitters.
- **Capitalization**: Not all sentences start with capitals (e.g., quotations, numbers), and not all capitals start sentences (e.g., "The U.S. Flag").
- **Social Media**: Lack of formal punctuation requires extracting "ideas" rather than formal boundaries.

## Treebank Tokenizer Rules
The `TreebankWordTokenizer` (NLTK standard) follows Penn Treebank rules:
- **Contractions**: Splits "don't" $\rightarrow$ "do n't" and "they'll" $\rightarrow$ "they 'll".
- **Punctuation**: Treats most punctuation characters as separate tokens.
- **Quotes**: Splits off commas and single quotes when followed by whitespace.
- **Periods**: Separates periods that appear at the end of a line.

## Tools
- `nltk.word_tokenize()`
- `spacy.nlp()` — includes sentence segmentation
- HuggingFace `tokenizers` library (fast BPE/WordPiece)

## Domain-Specific Tokenization Challenges
- Clinical text contains abbreviations, acronyms, and domain-specific terms requiring specialized tokenizers (Chapman et al., 2011)
- Temporal expressions, medication dosages, and lab values need dedicated parsing beyond standard tokenization (Savova et al., 2010)
- Domain preprocessing must include normalization against standardized vocabularies like SNOMED CT, ICD-10, and UMLS (Bodenreider, 2004)
- ~80% of EHR data is unstructured text, making tokenization the critical first step in clinical NLP pipelines (Wang et al., 2018)

## Language-Specific Tools & Global Writing Systems
- **MeCab**: Japanese tokenization/POS (Kudo et al., 2004).
- **Diversity of Writing Systems**: NLP pipelines must adapt to different script architectures (Thomas, 2020):
    - **Alphabets**: Every sound (vowel and consonant) has a symbol (e.g., Latin, Greek).
    - **Abjads**: Primarily consonants are written; vowels are inferred (e.g., Arabic, Hebrew).
    - **Abugidas**: Consonants carry a default vowel; other vowels are marked with diacritics (e.g., Ge'ez/Amharic, Devanagari/Hindi/Nepali).
    - **Syllabaries**: Each symbol represents a whole syllable (e.g., Japanese Katakana/Hiragana, Cherokee).
    - **Logographs**: Each symbol represents a whole word or morpheme (e.g., Chinese characters/Hanzi).

---

#classical #preprocessing
