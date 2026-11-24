# Challenges in Nepali NLP

## Data Scarcity
- Limited parallel corpora
- Few annotated datasets (NER, POS, sentiment)
- Wikipedia corpus is small compared to English

## Script & Encoding
- Devanagari script — conjuncts, vowel marks
- Unicode normalization critical (NFC vs NFD)
- Multiple encoding standards historically

## Morphological Complexity
- Agglutinative tendencies
- Rich verb inflection (tense, aspect, person, number, formality)
- Postpositions instead of prepositions

## Tokenization
- No clear word boundaries in some compounds
- Clitics and particles
- Need specialized tokenizers

## Social & Ethical Challenges

### Linguistic Taboos & Euphemisms
- **Complexity**: Offensive terms are often rooted in socio-cultural contexts (caste, kinship).
- **Research**: A corpus of >1000 taboo terms reveals that **Politics**, **Race**, and **Animal metaphors** are the primary categories for offensive language in Nepal.
- **Euphemisms**: 12 distinct strategies used by speakers to navigate taboos, complicating automated detection.

### Politico-Economic Bias
- **Economic Bias**: Smaller, Nepali-specific LMs (e.g., NepBERTa) show right-leaning economic and authoritarian social biases.
- **Generative Trends**: Larger multilingual models (GPT-4o, Gemini) tend toward left-libertarian stances.
- **Benchmark**: Political Compass Test (PCT) translated into Nepali for bias quantification.

### Gender & Cultural Bias
- **Gendered Inflections**: Nepali verbs change with gender, which often leads to coreference errors and occupational stereotyping in MT.
- **Formality levels**: Misalignment between high-resource anchors and Nepali-specific honorifics (*tā*, *timi*, *tapāi*).

---

#nepali #challenges #bias #ethics #taboos
