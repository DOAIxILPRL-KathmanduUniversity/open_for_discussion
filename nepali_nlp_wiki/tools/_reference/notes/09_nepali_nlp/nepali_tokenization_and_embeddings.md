# Research: Tokenization & Embeddings for Nepali

> [!IMPORTANT] Gist
> Recent research (2024) challenges the assumption that lower perplexity during pre-training predicts better downstream performance for Nepali. Suffix-aware tokenization and vowel standardization are key to robust representations.

## 1. Tokenization Strategies: Perplexity vs. Performance
A comparative study of six strategies on the OSCAR corpus (1.2GB) revealed significant discrepancies between intrinsic (perplexity) and extrinsic (F1-score) metrics.

| Strategy | Perplexity | Nep-gLUE Performance |
| :--- | :--- | :--- |
| **SentencePiece (BPE)** | Higher | **Best (Avg Score: 0.88)** |
| **Byte-level BPE** | **Lowest** | Lower (Less consistent) |
| **Morpheme-based** | **Lowest** | Best for NER (F1: 0.89) |
| **Word-based** | Highest | Poor on low-freq terms |

**Key Finding**: SentencePiece consistently yields the best results on understanding-based tasks (CPS, CC), while morpheme-based tokenization (Morfessor) excels in morphology-heavy tasks like NER.

## 2. Fine-tuning Small Embeddings (NpVec1)
Instead of training massive models from scratch, fine-tuning small, specialized embeddings (e.g., **NpVec1**: 6 heads, 300-dim) on diverse datasets yields high efficiency.

### Preprocessing Innovations
- **Vowel Sound Standardization**: Normalizing multiple written forms of phonetically identical vowels into a single Unicode form.
*   **Suffix-aware Tokenization**: Explicitly splitting post-positional suffixes to reduce vocabulary sparsity and improve coverage on social media (unregularized) text.
*   **Impact**: Fine-tuning on diverse (News + Social Media) data improved NpVec1 news classification by a **7% F1 margin**.

## 3. Traditional Word Embeddings (GloVe & Word2Vec)
- **GloVe**: Found optimal for news classification when trained on large (116k article) corpora. 200-dimensional embeddings reached **95.36% accuracy** with Bi-LSTM.
- **Word2Vec (CBOW/Skip-gram)**: Struggles with multi-class classification (20+ categories) compared to TF-IDF if the dataset size is moderate, due to averaged document vectors losing specificity.

## 4. Professional Regex Tokenizer (Devanagari Optimized)

For Devanagari, simple space-based splitting is insufficient due to attached punctuation and distinct numerical formats. A hardened tokenizer must handle:
- **Nepali Digits**: `१२,३४५` vs English `12,345`.
- **Danda (।) and Double Danda (॥)**: Sentence terminators.
- **Devanagari Letter Clusters**: Excluding digits and terminators.

```python
import re
NUM = r'[0-9\u0966-\u096F]+(?:[.,][0-9\u0966-\u096F]+)*' 
DEV_WORD = r'[\u0900-\u0963]+' 
TOKEN_RE = re.compile(f'({NUM}|{DEV_WORD}|[\u0964\u0965]|[.,!?;:()])')
```

## 5. Large-Scale Unigram Extraction
When processing massive corpora like **NepBERTa**, we use frequency-based unigram extraction to build the initial vocabulary.

1.  **Extraction**: Scanning Devanagari subsets across multi-GB CSVs.
2.  **Aggregation**: Using `Counter` to rank token occurrences.
3.  **Vocabulary Building**: Exporting `words_only.txt` for subword model training (BPE/WordPiece).

---

#nepali #tokenization #sentencepiece #embeddings #npvec1 #glove #word2vec #nlp-research
