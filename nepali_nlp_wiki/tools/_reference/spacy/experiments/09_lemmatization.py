"""
Experiment 09: Lemmatization Strategies
Explores: Rule-based lemmatizer, lookup lemmatizer, norm-based stemming comparison
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang.ne import Nepali
from lang.ne.lookups import LOOKUPS

nlp = Nepali()

print("=" * 60)
print("EXPERIMENT 09: LEMMATIZATION STRATEGIES")
print("=" * 60)

# --- A. Norm-based stemming (already in lex_attrs) ---
print("\n--- A. Norm-Based Stemming (Built-in) ---")
words = ["रामले", "घरमा", "केटाहरू", "विद्यालयमा", "नेपालको", "बजारबाट", "मान्छेहरूलाई"]
doc = nlp(" ".join(words))
print(f"  {'Original':<20} {'norm_ (stem)':<20}")
print(f"  {'-'*40}")
for t in doc:
    print(f"  {t.text:<20} {t.norm_:<20}")

# --- B. Lookup-based lemmatization ---
print("\n--- B. Lookup-Based Lemmatization ---")
lemma_table = LOOKUPS["lemma_lookup"]
test_words = ["गरेका", "गरेकी", "गरेको", "जाँदै", "रामले", "काठमाडौँमा", "केटाहरू", "मेरो", "तपाईंले"]
print(f"  {'Word':<20} {'Lookup Lemma':<20} {'norm_ (stem)':<20}")
print(f"  {'-'*60}")
for w in test_words:
    lookup = lemma_table.get(w, "—")
    doc = nlp(w)
    stem = doc[0].norm_ if len(doc) > 0 else "—"
    print(f"  {w:<20} {lookup:<20} {stem:<20}")

# --- C. Hybrid approach: lookup first, fallback to norm ---
print("\n--- C. Hybrid Lemmatizer (Lookup → Norm fallback) ---")
def hybrid_lemmatize(text):
    doc = nlp(text)
    results = []
    for t in doc:
        if t.text in lemma_table:
            results.append((t.text, lemma_table[t.text], "lookup"))
        else:
            results.append((t.text, t.norm_, "norm"))
    return results

sentence = "रामले गरेको कामले नेपालको विद्यार्थीहरूलाई मद्दत गर्यो।"
print(f"  Input: '{sentence}'")
for word, lemma, method in hybrid_lemmatize(sentence):
    print(f"    {word:<22} → {lemma:<15} ({method})")

# --- D. Coverage analysis ---
print("\n--- D. Lookup Coverage Analysis ---")
from lang.ne.examples import sentences
total_tokens = 0
lookup_hits = 0
norm_changes = 0
for s in sentences:
    doc = nlp(s)
    for t in doc:
        if t.is_alpha:
            total_tokens += 1
            if t.text in lemma_table:
                lookup_hits += 1
            if t.norm_ != t.text:
                norm_changes += 1

print(f"  Total alpha tokens:  {total_tokens}")
print(f"  Lookup hits:         {lookup_hits} ({100*lookup_hits/total_tokens:.1f}%)")
print(f"  Norm changes:        {norm_changes} ({100*norm_changes/total_tokens:.1f}%)")
print(f"  Untouched:           {total_tokens - max(lookup_hits, norm_changes)}")
