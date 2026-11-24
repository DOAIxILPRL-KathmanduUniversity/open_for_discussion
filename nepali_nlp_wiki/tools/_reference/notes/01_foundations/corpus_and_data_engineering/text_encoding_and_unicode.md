# Text Encoding & Unicode

> [!IMPORTANT] Gist
> To process language, computers must represent characters as numbers. **Unicode** provides a unique number for every character across all scripts, while **UTF-8** is the dominant variable-width encoding used to store these numbers efficiently (Jurafsky & Martin, 2026).

## 1. Characters and Code Points
- **Unicode**: A computing industry standard for the consistent encoding, representation, and handling of text.
- **Code Point**: A numerical value assigned to a character (e.g., `U+0041` for 'A').

## 2. UTF-8 Encoding
- Variable-width character encoding (1 to 4 bytes).
- Backward compatible with ASCII.
- Dominant on the web (~98% of websites).

## 3. Subword Tokenization: Byte-Pair Encoding (BPE)
BPE is the standard algorithm for modern LLM tokenizers (GPT, Llama).
- **Intuition**: Iteratively merge the most frequent pair of adjacent characters/tokens into a single new token.
- **Why?**: It handles the "out-of-vocabulary" problem by breaking unknown words into known subword units (e.g., "unfriendly" → "un" + "friendly").
- See [[03_classical_nlp/tokenization]] for more on BPE.

---

#foundations #unicode #encoding #tokenization
