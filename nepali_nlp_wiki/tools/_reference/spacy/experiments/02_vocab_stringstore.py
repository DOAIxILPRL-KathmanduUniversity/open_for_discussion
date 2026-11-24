"""
Experiment 02: Vocab, StringStore & Lexeme
Explores: Vocab, StringStore (hash mapping), Lexeme objects, lexical attributes
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang.ne import Nepali

nlp = Nepali()

print("=" * 60)
print("EXPERIMENT 02: VOCAB & STRINGSTORE")
print("=" * 60)

# --- A. StringStore: String ↔ Hash mapping ---
print("\n--- A. StringStore (String ↔ Hash) ---")
words = ["नेपाल", "काठमाडौँ", "राम", "हिमाल", "भाषा"]
for w in words:
    h = nlp.vocab.strings.add(w)
    print(f"  '{w}' → hash={h} → back='{nlp.vocab.strings[h]}'")

# --- B. Lexeme: word-type (no context) ---
print("\n--- B. Lexeme Attributes ---")
doc = nlp("रामले घरमा रोटी खायो। तपाईं कहाँ हुनुहुन्छ?")
print(f"{'Text':<15} {'is_stop':>8} {'like_num':>9} {'norm_':>12} {'is_alpha':>9}")
print("-" * 55)
for t in doc:
    lex = nlp.vocab[t.text]
    print(f"{t.text:<15} {lex.is_stop:>8} {lex.like_num:>9} {t.norm_:>12} {lex.is_alpha:>9}")

# --- C. Vocab size growth ---
print("\n--- C. Vocab Growth ---")
print(f"  Vocab size before processing: {len(nlp.vocab)}")
texts = [
    "सगरमाथा संसारको सबैभन्दा अग्लो हिमाल हो।",
    "गौतम बुद्धको जन्मस्थल लुम्बिनी हो।",
    "नेपालको राजधानी काठमाडौँ हो।"
]
for t in texts:
    nlp(t)
print(f"  Vocab size after processing:  {len(nlp.vocab)}")

# --- D. Check if word exists in vocab ---
print("\n--- D. Word Existence Check ---")
check_words = ["नेपाल", "xyzabc", "काठमाडौँ", "xyznonsense"]
for w in check_words:
    has = nlp.vocab.strings[w] if w in nlp.vocab.strings else None
    print(f"  '{w}' in vocab: {has is not None}")
