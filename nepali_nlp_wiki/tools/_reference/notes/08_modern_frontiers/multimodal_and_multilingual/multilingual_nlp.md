# Multilingual NLP

## Challenges
- Script diversity (Latin, Devanagari, CJK, Arabic)
- Morphological complexity varies hugely
- Low-resource languages lack data

## Multilingual Models
- mBERT (104 languages)
- XLM-RoBERTa
- NLLB (No Language Left Behind) for MT

## Cross-lingual Transfer
- Train on English, evaluate on Nepali
- Shared subword vocabulary enables transfer
- Zero-shot cross-lingual classification

## Tokenization Issues
- BPE undertrained on low-resource scripts
- "Fertility" — tokens per word varies by language
- SentencePiece helps with raw Unicode handling

## Agglutinative Language Challenges
- **Kazakh**: High data sparsity due to complex morphology where one word can contain multiple stems and suffixes (e.g., a single word meaning "Together with our classmates").
- Solution: Use **Stem-level embeddings** in addition to word-level to capture subword semantics (Hayinaer et al., 2025).

## Lexical Complexity in L2 Writing
- Studies on L2 learners (e.g., Chinese learners of Japanese) show that **Lexical Density** typically converges to native levels at advanced stages, but **Lexical Sophistication** (use of low-frequency words) may remain significantly higher in learners due to native language transfer (Zhong & Yang, 2025).

---

#modern #multilingual
