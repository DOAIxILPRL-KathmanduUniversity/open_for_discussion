"""
Experiment 12: nlp.pipe() Batch Processing & Performance
Explores: Batch processing, memory efficiency, disable/enable components, timing
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time
from lang.ne import Nepali
from lang.ne.examples import sentences

print("=" * 60)
print("EXPERIMENT 12: BATCH PROCESSING & PERFORMANCE")
print("=" * 60)

# --- A. Single-doc vs batch processing ---
nlp = Nepali()

# Multiply sentences for realistic load
corpus = sentences * 50  # 1400 sentences
print(f"\n--- A. Corpus Size: {len(corpus)} sentences ---")

# Method 1: One-by-one
start = time.perf_counter()
for text in corpus:
    doc = nlp(text)
elapsed_single = time.perf_counter() - start
print(f"  Single-doc processing: {elapsed_single:.3f}s")

# Method 2: nlp.pipe (batch)
start = time.perf_counter()
docs = list(nlp.pipe(corpus, batch_size=64))
elapsed_pipe = time.perf_counter() - start
print(f"  nlp.pipe() processing: {elapsed_pipe:.3f}s")
print(f"  Speedup: {elapsed_single/elapsed_pipe:.2f}x")

# --- B. Selective processing with disable ---
print("\n--- B. Selective Component Processing ---")
# Add some components for demonstration
nlp2 = Nepali()
nlp2.add_pipe("sentencizer")

# Process with all components
start = time.perf_counter()
docs_full = list(nlp2.pipe(corpus, batch_size=64))
elapsed_full = time.perf_counter() - start
print(f"  Full pipeline ({nlp2.pipe_names}): {elapsed_full:.3f}s")

# Process with sentencizer disabled
start = time.perf_counter()
docs_lite = list(nlp2.pipe(corpus, batch_size=64, disable=["sentencizer"]))
elapsed_lite = time.perf_counter() - start
print(f"  Tokenizer only (sentencizer disabled): {elapsed_lite:.3f}s")

# --- C. Memory-efficient streaming ---
print("\n--- C. Memory-Efficient Streaming ---")
# Using as_tuples to pass context alongside docs
texts_with_meta = [(s, {"source": "example", "idx": i}) for i, s in enumerate(sentences)]

for doc, ctx in nlp.pipe(texts_with_meta, as_tuples=True):
    if ctx["idx"] < 5:  # Only print first 5
        print(f"  [{ctx['idx']}] {doc.text[:40]}... ({len(doc)} tokens)")

# --- D. Token statistics from batch ---
print("\n--- D. Corpus-Wide Token Statistics ---")
from collections import Counter

token_counts = Counter()
total_tokens = 0
total_alpha = 0
total_stop = 0
total_numeric = 0

for doc in nlp.pipe(sentences):
    for t in doc:
        total_tokens += 1
        token_counts[t.text] += 1
        if t.is_alpha:
            total_alpha += 1
        if t.is_stop:
            total_stop += 1
        if t.like_num:
            total_numeric += 1

print(f"  Total tokens:    {total_tokens}")
print(f"  Alpha tokens:    {total_alpha}")
print(f"  Stop words:      {total_stop} ({100*total_stop/total_tokens:.1f}%)")
print(f"  Numeric tokens:  {total_numeric}")
print(f"  Unique tokens:   {len(token_counts)}")
print(f"\n  Top 15 tokens:")
for word, count in token_counts.most_common(15):
    bar = "█" * count
    print(f"    {word:<15} {count:>3} {bar}")
