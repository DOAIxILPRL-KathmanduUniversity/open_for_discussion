"""
Experiment 07: AttributeRuler (Morphological Rules)
Explores: Setting POS, morphology, and lemmas via pattern rules
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang.ne import Nepali

nlp = Nepali()

print("=" * 60)
print("EXPERIMENT 07: ATTRIBUTE RULER")
print("=" * 60)

# --- A. Add AttributeRuler ---
ruler = nlp.add_pipe("attribute_ruler")

# --- B. Define Nepali-specific morphological rules ---
patterns = [
    # Ergative case: words ending in ले
    {
        "patterns": [[{"TEXT": {"REGEX": ".*ले$"}}]],
        "attrs": {"POS": "NOUN", "MORPH": "Case=Erg"},
    },
    # Locative case: words ending in मा
    {
        "patterns": [[{"TEXT": {"REGEX": ".*मा$"}}]],
        "attrs": {"POS": "NOUN", "MORPH": "Case=Loc"},
    },
    # Genitive case: words ending in को
    {
        "patterns": [[{"TEXT": {"REGEX": ".*को$"}}]],
        "attrs": {"POS": "NOUN", "MORPH": "Case=Gen"},
    },
    # Dative case: words ending in लाई
    {
        "patterns": [[{"TEXT": {"REGEX": ".*लाई$"}}]],
        "attrs": {"POS": "NOUN", "MORPH": "Case=Dat"},
    },
    # Ablative case: words ending in बाट
    {
        "patterns": [[{"TEXT": {"REGEX": ".*बाट$"}}]],
        "attrs": {"POS": "NOUN", "MORPH": "Case=Abl"},
    },
    # Plural marker: words ending in हरू
    {
        "patterns": [[{"TEXT": {"REGEX": ".*हरू$"}}]],
        "attrs": {"MORPH": "Number=Plur"},
    },
    # Common verbs
    {
        "patterns": [[{"TEXT": {"REGEX": "^(हो|छ|छन्|थियो|थिए|हुन्)$"}}]],
        "attrs": {"POS": "AUX"},
    },
    # Postpositions as standalone
    {
        "patterns": [[{"TEXT": {"REGEX": "^(मा|को|ले|लाई|बाट|सँग|सित|तिर|भित्र|बाहिर|माथि|तल)$"}}]],
        "attrs": {"POS": "ADP"},
    },
    # Pronouns
    {
        "patterns": [[{"TEXT": {"REGEX": "^(म|तिमी|ऊ|हामी|तपाईं|उनी|उनीहरू|यो|त्यो)$"}}]],
        "attrs": {"POS": "PRON"},
    },
    # Conjunctions
    {
        "patterns": [[{"TEXT": {"REGEX": "^(र|तर|वा|अथवा|किनभने)$"}}]],
        "attrs": {"POS": "CCONJ"},
    },
]

for p in patterns:
    ruler.add(**p)

# --- C. Test morphological assignment ---
print("\n--- A. Morphological Case Marking ---")
text = "रामले घरमा रोटी खायो।"
doc = nlp(text)
print(f"  Text: '{text}'")
print(f"  {'Token':<15} {'POS':<8} {'Morph'}")
print(f"  {'-'*40}")
for t in doc:
    print(f"  {t.text:<15} {t.pos_:<8} {t.morph}")

# --- D. Test on varied sentences ---
print("\n--- B. Full Morphological Analysis ---")
test_texts = [
    "सीतालाई रामले फूल दियो।",
    "विद्यार्थीहरू विद्यालयमा पढ्छन्।",
    "हामी नेपालको राजधानीबाट आयौँ।",
    "तपाईं र म सँगै जानेछौँ।",
]
for text in test_texts:
    doc = nlp(text)
    print(f"\n  '{text}'")
    for t in doc:
        if t.pos_ or str(t.morph):
            print(f"    {t.text:<18} POS={t.pos_:<6} MORPH={t.morph}")
