# Masterclass: Nepali NLP with spaCy

> [!IMPORTANT] Gist
> Modern industrial NLP often requires high-performance pipelines. By combining **spaCy**'s flexible architecture with specialized tools like `nepali-stemmer`, we can build a robust, production-ready pipeline for Nepali text.

## 1. The Blank Pipeline
spaCy doesn't have a native "trained" model for Nepali yet, but we can initialize a `blank("ne")` model and add components.
- **Sentencizer**: Enables sentence boundary detection (e.g., splitting on `।`).
- **Tokenization**: Handles Devanagari script, though complex words may require custom rules.

## 2. Custom Stemming Component
Standard spaCy doesn't provide a Nepali stemmer. We can inject a custom `@spacy.Language.component` to enrich tokens with a `.stem` attribute.

### Implementation Logic
1.  **Extension**: Register a custom attribute `Token.set_extension("stem", default=None)`.
2.  **Processing**: Iterate through doc tokens, pass text to `NepStemmer`, and store the result.
3.  **Order**: Add the component `after="sentencizer"` to ensure tokenization is complete.

## 3. Comparative Tokenization
| Feature | spaCy Blank (ne) | Rule-based (Classical) |
| :--- | :--- | :--- |
| **Punctuation** | Native handling | Manual regex required |
| **Extensibility** | High (Custom components) | Low (Hardcoded) |
| **Speed** | Very High (Cythonized) | Moderate |

---

**Notebook**: [nepali_spacy_pipeline.py](notebooks/nepali_spacy_pipeline.py) (Custom Stemming Pipeline)

#spacy #nepali #stemming #nlp-engineering #pipelines #tokenization
