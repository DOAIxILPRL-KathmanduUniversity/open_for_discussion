# N-gram Models

## Key Ideas
- P(word | previous n-1 words) — Markov assumption
- Unigram, bigram, trigram
- Estimated from corpus counts with smoothing

## Smoothing Techniques
- Add-k (Laplace)
- Kneser-Ney (state of the art for n-grams)
- Backoff and interpolation

## Applications
- Spell checking, autocomplete, speech recognition
- Baseline language model

---

**Notebook**: [ngram_playground.py](notebooks/ngram_playground.py)

#lm #classical
