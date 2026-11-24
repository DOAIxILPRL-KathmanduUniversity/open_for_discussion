# Large-Scale Unigram Frequency Generation

> [!IMPORTANT] Gist
> Processing massive corpora (e.g., 28M+ lines of NepBERTa data) requires memory-efficient tokenization and frequency counting. This module implements a high-performance pipeline using `polyglot-tokenizer` and Python's `collections.Counter`.

## 1. Tokenization with Polyglot
The `polyglot-tokenizer` is optimized for Devanagari script, handling punctuation and whitespace consistently. 
```python
from polyglot_tokenizer import Tokenizer
tk_ne = Tokenizer(lang='ne')
tokens = tk_ne.tokenize("नमस्ते, तपाईंलाई कस्तो छ?")
```

## 2. Iterative Counting (Low Memory)
To process millions of lines without crashing the environment, we use a streaming file reader and update the `Counter` incrementally.
- **tqdm**: Used for progress tracking during the multi-million line iteration.
- **line_count**: Pre-calculated using `wc -l` to provide accurate ETA for tqdm.

```python
unigram_frequencies = Counter()
with open(file_path, 'r', encoding='utf-8') as f:
    for line in tqdm(f, total=line_count, desc="Tokenizing"):
        tokens = tk_ne.tokenize(line.strip())
        unigram_frequencies.update(tokens)
```

## 3. Storage & Export
The resulting unigram frequencies are exported to a CSV for downstream tasks like vocabulary filtering or pre-training.
- **token**: The Devanagari unigram.
- **frequency**: Total occurrences in the corpus.

---

**Notebook**: [unigram_freq_generator.py](notebooks/unigram_freq_generator.py)

#nepali-nlp #tokenization #polyglot #big-data #unigram #corpus-processing
