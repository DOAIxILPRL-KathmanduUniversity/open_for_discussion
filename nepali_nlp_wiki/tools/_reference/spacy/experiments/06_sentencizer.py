"""
Experiment 06: Sentencizer (Rule-Based Sentence Segmentation)
Explores: Sentencizer component, Purnabiram-aware segmentation, custom rules
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang.ne import Nepali

nlp = Nepali()

print("=" * 60)
print("EXPERIMENT 06: SENTENCIZER")
print("=" * 60)

# --- A. Add rule-based sentencizer ---
# The sentencizer uses punctuation to detect sentence boundaries
sentencizer = nlp.add_pipe("sentencizer")

# --- B. Basic sentence detection ---
print("\n--- A. Basic Sentence Detection ---")
text = "नेपाल सुन्दर देश हो। यहाँ हिमालय छ। मान्छेहरू मिलनसार छन्।"
doc = nlp(text)
for i, sent in enumerate(doc.sents):
    print(f"  Sent {i+1}: '{sent.text}' ({len(sent)} tokens)")

# --- C. Purnabiram as sentence boundary ---
print("\n--- B. Purnabiram (।) as Sentence Boundary ---")
text2 = "राम स्कूल गयो। सीताले भात पकाइन्। हरिले किताब पढ्यो।"
doc2 = nlp(text2)
for i, sent in enumerate(doc2.sents):
    print(f"  Sent {i+1}: '{sent.text.strip()}'")

# --- D. Question marks ---
print("\n--- C. Interrogative Sentences ---")
text3 = "तपाईं कहाँ जानुहुन्छ? म काठमाडौँ जान्छु। तिमी कसरी आयौ?"
doc3 = nlp(text3)
for i, sent in enumerate(doc3.sents):
    print(f"  Sent {i+1}: '{sent.text.strip()}'")

# --- E. Paragraph with mixed punctuation ---
print("\n--- D. Complex Paragraph ---")
paragraph = """नेपालको राजधानी काठमाडौँ हो। यो शहर ऐतिहासिक छ; यहाँ धेरै मन्दिरहरू छन्। के तपाईंले पशुपतिनाथ मन्दिर देख्नुभएको छ? यो विश्व सम्पदा सूचीमा छ! लुम्बिनी पनि महत्वपूर्ण छ।"""
doc4 = nlp(paragraph)
for i, sent in enumerate(doc4.sents):
    print(f"  Sent {i+1}: '{sent.text.strip()}'")

# --- F. Sentence-level statistics ---
print("\n--- E. Sentence Statistics ---")
all_texts = [
    "एक। दुई। तीन।",
    "चार, पाँच र छ त एउटै वाक्यमा छन्।",
    "सात? आठ! नौ।"
]
for t in all_texts:
    doc = nlp(t)
    sents = list(doc.sents)
    print(f"  '{t}' → {len(sents)} sentence(s)")
