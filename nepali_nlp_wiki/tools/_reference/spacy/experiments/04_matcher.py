"""
Experiment 04: Matcher & PhraseMatcher
Explores: Token-level pattern matching, phrase matching for Nepali NER-style extraction
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang.ne import Nepali
from spacy.matcher import Matcher, PhraseMatcher

nlp = Nepali()

print("=" * 60)
print("EXPERIMENT 04: MATCHER & PHRASEMATCHER")
print("=" * 60)

# --- A. Token Matcher: Find postposition patterns ---
print("\n--- A. Token Matcher (Postposition Pattern) ---")
matcher = Matcher(nlp.vocab)
# Pattern: any word ending in "ले" (ergative case marker)
matcher.add("ERGATIVE", [[{"TEXT": {"REGEX": ".*ले$"}}]])
# Pattern: any word ending in "मा" (locative case marker)
matcher.add("LOCATIVE", [[{"TEXT": {"REGEX": ".*मा$"}}]])

text = "रामले काठमाडौँमा भात खायो। सीताले पोखरामा रोटी खाइन्।"
doc = nlp(text)
matches = matcher(doc)
for match_id, start, end in matches:
    label = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(f"  [{label}] '{span.text}' (tokens {start}-{end})")

# --- B. PhraseMatcher: Named Entity detection ---
print("\n--- B. PhraseMatcher (Place Names) ---")
phrase_matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
places = ["काठमाडौँ", "पोखरा", "लुम्बिनी", "जनकपुर", "भक्तपुर",
          "ललितपुर", "वीरगञ्ज", "धरान", "विराटनगर", "हेटौँडा"]
patterns = [nlp.make_doc(p) for p in places]
phrase_matcher.add("PLACE", patterns)

texts = [
    "काठमाडौँ नेपालको राजधानी हो।",
    "पोखरा र लुम्बिनी पर्यटकीय शहर हुन्।",
    "भक्तपुर दरबार स्क्वायर प्रसिद्ध छ।",
    "विराटनगर पूर्वी नेपालको ठूलो शहर हो।"
]
for t in texts:
    doc = nlp(t)
    matches = phrase_matcher(doc)
    found = [doc[start:end].text for _, start, end in matches]
    print(f"  '{t[:40]}...' → places: {found}")

# --- C. Multi-token patterns ---
print("\n--- C. Multi-Token Pattern (Adjective + Noun heuristic) ---")
adj_noun = Matcher(nlp.vocab)
# Heuristic: word ending in ो/ी + next word (likely adj+noun in Nepali)
adj_noun.add("ADJ_NOUN", [
    [{"TEXT": {"REGEX": ".*[ोी]$"}}, {"IS_ALPHA": True}]
])
text2 = "ठूलो शहर, सानो गाउँ, राम्रो मान्छे, नयाँ किताब"
doc2 = nlp(text2)
matches2 = adj_noun(doc2)
for _, start, end in matches2:
    print(f"  '{doc2[start:end].text}'")

# --- D. Overlapping matches ---
print("\n--- D. Pattern with Context ---")
verb_pattern = Matcher(nlp.vocab)
# Find: [anything] + "गर्नु" family
verb_pattern.add("GARNU_COMPOUND", [
    [{"IS_ALPHA": True}, {"TEXT": {"REGEX": "^गर्.*"}}]
])
text3 = "काम गर्नुपर्छ। मद्दत गर्नुहोस्। अध्ययन गर्दै छु।"
doc3 = nlp(text3)
matches3 = verb_pattern(doc3)
for _, start, end in matches3:
    print(f"  Compound verb: '{doc3[start:end].text}'")
