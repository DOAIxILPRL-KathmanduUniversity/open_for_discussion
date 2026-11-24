"""
Experiment 03: Doc, Span & Token Objects
Explores: Doc construction, Span slicing, SpanGroup, Token navigation, custom extensions
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang.ne import Nepali
from spacy.tokens import Doc, Span, Token

nlp = Nepali()

print("=" * 60)
print("EXPERIMENT 03: DOC, SPAN & TOKEN")
print("=" * 60)

# --- A. Doc as container ---
text = "गौतम बुद्धको जन्मस्थल लुम्बिनी हो।"
doc = nlp(text)
print("\n--- A. Doc Properties ---")
print(f"  doc.text     = '{doc.text}'")
print(f"  len(doc)     = {len(doc)}")
print(f"  doc.vocab    = {type(doc.vocab).__name__}")
print(f"  doc.has_annotation('DEP') = {doc.has_annotation('DEP')}")

# --- B. Span slicing ---
print("\n--- B. Span Slicing ---")
span = doc[0:3]  # "गौतम बुद्धको जन्मस्थल"
print(f"  doc[0:3] = '{span.text}'")
print(f"  span.start = {span.start}, span.end = {span.end}")
print(f"  type = {type(span).__name__}")

# --- C. Token navigation ---
print("\n--- C. Token Navigation ---")
for t in doc:
    neighbors = []
    if t.i > 0:
        neighbors.append(f"prev='{doc[t.i-1].text}'")
    if t.i < len(doc) - 1:
        neighbors.append(f"next='{doc[t.i+1].text}'")
    print(f"  [{t.i}] '{t.text}' → {', '.join(neighbors)}")

# --- D. Custom extensions ---
print("\n--- D. Custom Doc/Token Extensions ---")
# Register a custom attribute on Token
if not Token.has_extension("is_devanagari"):
    Token.set_extension("is_devanagari", getter=lambda t: all('\u0900' <= c <= '\u097F' for c in t.text if not c.isspace()))

# Register a custom attribute on Doc
if not Doc.has_extension("devanagari_ratio"):
    Doc.set_extension("devanagari_ratio", getter=lambda d: sum(1 for t in d if t._.is_devanagari) / len(d) if len(d) > 0 else 0)

mixed = nlp("नेपालमा Python र JavaScript सिक्न सजिलो छ।")
print(f"  Text: '{mixed.text}'")
print(f"  Devanagari ratio: {mixed._.devanagari_ratio:.2f}")
for t in mixed:
    print(f"    '{t.text}' → is_devanagari={t._.is_devanagari}")

# --- E. SpanGroup ---
print("\n--- E. SpanGroup ---")
doc2 = nlp("काठमाडौँ लन्डन टोकियो तीनवटा शहर हुन्।")
cities = [doc2[0:1], doc2[1:2], doc2[2:3]]
doc2.spans["cities"] = cities
print(f"  SpanGroup 'cities': {[s.text for s in doc2.spans['cities']]}")
