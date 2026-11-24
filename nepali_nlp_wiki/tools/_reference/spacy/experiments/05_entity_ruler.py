"""
Experiment 05: Rule-Based NER with EntityRuler
Explores: EntityRuler, pattern-based entity extraction, entity spans
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang.ne import Nepali

nlp = Nepali()

print("=" * 60)
print("EXPERIMENT 05: ENTITY RULER (Rule-Based NER)")
print("=" * 60)

# --- A. Add EntityRuler to blank pipeline ---
ruler = nlp.add_pipe("entity_ruler")

# --- B. Define patterns ---
patterns = [
    # PERSON patterns
    {"label": "PERSON", "pattern": "राम"},
    {"label": "PERSON", "pattern": "सीता"},
    {"label": "PERSON", "pattern": "हरि"},
    {"label": "PERSON", "pattern": "गीता"},
    {"label": "PERSON", "pattern": "बराक ओबामा"},
    {"label": "PERSON", "pattern": "गौतम बुद्ध"},
    {"label": "PERSON", "pattern": "पृथ्वी नारायण शाह"},
    
    # GPE (Geo-Political Entity) patterns
    {"label": "GPE", "pattern": "नेपाल"},
    {"label": "GPE", "pattern": "काठमाडौँ"},
    {"label": "GPE", "pattern": "पोखरा"},
    {"label": "GPE", "pattern": "लुम्बिनी"},
    {"label": "GPE", "pattern": "भारत"},
    {"label": "GPE", "pattern": "चीन"},
    {"label": "GPE", "pattern": "जापान"},
    
    # ORG patterns
    {"label": "ORG", "pattern": "नेपाल सरकार"},
    {"label": "ORG", "pattern": "त्रिभुवन विश्वविद्यालय"},
    {"label": "ORG", "pattern": "नेपाल राष्ट्र बैंक"},
    {"label": "ORG", "pattern": "एप्पल"},
    {"label": "ORG", "pattern": "फेसबुक"},
    
    # DATE patterns (token-based)
    {"label": "DATE", "pattern": [{"TEXT": "वि.सं."}, {"LIKE_NUM": True}]},
    {"label": "DATE", "pattern": [{"TEXT": "ई.सं."}, {"LIKE_NUM": True}]},
    
    # MONEY patterns
    {"label": "MONEY", "pattern": [{"TEXT": {"REGEX": "^रु\\.?$"}}, {"LIKE_NUM": True}]},
    
    # LOCATION (natural features)
    {"label": "LOC", "pattern": "सगरमाथा"},
    {"label": "LOC", "pattern": "कोशी नदी"},
    {"label": "LOC", "pattern": "हिमालय"},
]

ruler.add_patterns(patterns)

# --- C. Test on varied sentences ---
print("\n--- Entity Extraction Results ---")
test_texts = [
    "रामले काठमाडौँमा भात खायो।",
    "गौतम बुद्धको जन्मस्थल लुम्बिनी हो।",
    "नेपाल सरकारले नयाँ नीति जारी गर्यो।",
    "वि.सं. २०८० मा त्रिभुवन विश्वविद्यालयमा भर्ना खुल्यो।",
    "रु. ५०० मा दुई किलो चामल आउँछ।",
    "पृथ्वी नारायण शाह नेपालका एकीकरणकर्ता हुन्।",
    "एप्पलले अमेरिकी स्टार्टअप किन्दै छ।",
    "सगरमाथा संसारको सबैभन्दा अग्लो हिमाल हो।",
    "बराक ओबामा अमेरिकाका पूर्व राष्ट्रपति हुन्।",
    "नेपाल राष्ट्र बैंकले ब्याजदर बढायो।"
]

for text in test_texts:
    doc = nlp(text)
    if doc.ents:
        ents = [(e.text, e.label_) for e in doc.ents]
        print(f"  '{text[:50]}...'")
        for ent_text, ent_label in ents:
            print(f"    → [{ent_label}] {ent_text}")
    else:
        print(f"  '{text[:50]}...' → (no entities)")
    print()

# --- D. Entity statistics ---
print("--- D. Entity Statistics ---")
all_ents = []
for text in test_texts:
    doc = nlp(text)
    all_ents.extend([(e.text, e.label_) for e in doc.ents])

from collections import Counter
label_counts = Counter(label for _, label in all_ents)
print(f"  Total entities found: {len(all_ents)}")
for label, count in label_counts.most_common():
    print(f"    {label}: {count}")
