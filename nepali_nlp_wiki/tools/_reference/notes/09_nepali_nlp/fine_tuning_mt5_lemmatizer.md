# Fine-tuning mT5 for Nepali Lemmatization

> [!IMPORTANT] Gist
> This module details the process of fine-tuning the `google/mt5-base` transformer for high-fidelity Nepali lemmatization. It implements specialized word-boundary tokenization and multi-metric evaluation (CER, BLEU, Morphological Coverage).

## 1. Data Preparation Pipeline
The pipeline transforms raw word-lemma pairs into a structured `JSONL` format suitable for `Seq2Seq` tasks.
- **Cleaning**: Stripping punctuation and whitespace.
- **Task Prefixing**: Prepending `lemmatize: ` to inputs to guide the model's multi-task capabilities.
- **Word-Level Tokenization**: Utilizing the `▁` (SentencePiece word boundary) to keep tokens distinct during the lemmatization process.

## 2. Training Strategy
- **Base Model**: `google/mt5-base`
- **Optimizer**: AdamW with `learning_rate=1e-5` and `EarlyStopping` (patience=3).
- **Evaluation Metric**: Character Error Rate (CER) is prioritized over Accuracy to capture "near-misses" in morphological inflections.

## 3. Evaluation Metrics
We use a suite of custom metrics to evaluate linguistic accuracy:
- **CER (Character Error Rate)**: Normalized Levenshtein distance.
- **Morphological Coverage**: A proxy metric checking suffix match rates (last 3 characters).
- **BLEU (Char-level)**: Measuring the overlap of character n-grams.

---

**Notebook**: [mt5_lemmatizer_finetuning.py](notebooks/mt5_lemmatizer_finetuning.py)

#nepali-nlp #transformers #mt5 #lemmatization #fine-tuning #huggingface
