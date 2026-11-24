# Tokenizer Deep Dive

## Why Subword Tokenization?
- Word-level: huge vocab, OOV problem
- Character-level: tiny vocab, very long sequences
- Subword: sweet spot — handles unseen words gracefully

## Algorithms
- **BPE** (Sennrich et al., 2016) — merge most frequent pairs
- **WordPiece** (used by BERT) — maximize likelihood
- **Unigram** (Kudo, 2018) — probabilistic, prune from large vocab
- **SentencePiece** — language-agnostic, treats input as raw Unicode

## Practical Considerations
- Vocab size tradeoff (32K–64K typical)
- Special tokens: [CLS], [SEP], [PAD], [MASK]
- Pre-tokenization matters for non-Latin scripts

---

**Notebook**: [huggingface_finetune.py](notebooks/huggingface_finetune.py)

#transformers #tokenization
