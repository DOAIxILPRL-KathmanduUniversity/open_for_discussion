"""
Experiment 01: Tokenization Deep-Dive
Explores: Tokenizer, Token, Doc, Purnabiram handling, whitespace tokens
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang.ne import Nepali

nlp = Nepali()

print("=" * 60)
print("EXPERIMENT 01: TOKENIZATION")
print("=" * 60)

# --- A. Basic tokenization ---
text = "रामले भात खायो।"
doc = nlp(text)
print("\n--- A. Basic Token Attributes ---")
print(f"{'Text':<15} {'i':>3} {'idx':>4} {'len':>4} {'is_alpha':>9} {'is_punct':>9} {'is_space':>9}")
print("-" * 65)
for t in doc:
    print(f"{t.text:<15} {t.i:>3} {t.idx:>4} {len(t):>4} {t.is_alpha:>9} {t.is_punct:>9} {t.is_space:>9}")

# --- B. Purnabiram vs Latin period ---
print("\n--- B. Purnabiram (।) vs Period (.) ---")
ne_sent = "यो वाक्य हो।"
en_sent = "This is a sentence."
doc_ne = nlp(ne_sent)
doc_en = nlp(en_sent)
print(f"Nepali tokens: {[t.text for t in doc_ne]}")
print(f"English tokens: {[t.text for t in doc_en]}")

# --- C. Abbreviation preservation ---
print("\n--- C. Abbreviation Tokenization ---")
abbrev_text = "डा. हरि, प्रा.डा. शर्मा, वि.सं. २०८०"
doc_ab = nlp(abbrev_text)
print(f"Tokens: {[t.text for t in doc_ab]}")

# --- D. Mixed script ---
print("\n--- D. Mixed Devanagari + Latin ---")
mixed = "नेपालमा Python सिक्नु राम्रो छ।"
doc_mix = nlp(mixed)
for t in doc_mix:
    print(f"  '{t.text}' → is_alpha={t.is_alpha}, like_num={t.like_num}")

# --- E. Edge cases ---
print("\n--- E. Edge Cases ---")
edges = ["", " ", "।", "  रामले  ", "१२३", "abc123"]
for e in edges:
    doc_e = nlp(e)
    print(f"  Input: {repr(e):>20} → tokens={[t.text for t in doc_e]}")
