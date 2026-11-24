# Pre-training BERT for Nepali (Masked LM)

> [!IMPORTANT] Gist
> Scaling the Sovereign Nepali Intelligence Registry requires custom language models. This module details the pre-training of a 6-layer BERT architecture from scratch using a massive Devanagari corpus.

## 1. Architectural Configuration
Instead of using the full 12-layer `bert-base`, we utilize a compact **6-layer configuration** to balance performance and computational overhead (approx. 100M parameters).
- **Vocab Size**: 50k+ (aligned with `CohleM/bert-nepali-tokenizer`).
- **Hidden Size**: 768.
- **Max Position Embeddings**: 256 (optimized for shorter context segments).

## 2. Dataset: Nepali Text Corpus
We utilize the `IRIIS-RESEARCH/Nepali-Text-Corpus`, a high-density collection of news articles and academic texts.
- **Streaming**: Data is streamed using `datasets` to handle large volumes without RAM overflow.
- **Preprocessing**: Truncation and padding to 256 tokens.

## 3. Masked Language Modeling (MLM)
- **Probability**: 15% of tokens are masked.
- **Training Strategy**: Epoch-based evaluation with `DataCollatorForLanguageModeling`.
- **Target**: Learning the bidirectional representation of Devanagari syntax.

---

**Notebook**: [nepali_bert_pretraining.py](notebooks/nepali_bert_pretraining.py)

#nepali-nlp #bert #pretraining #transformers #mlm #devanagari
