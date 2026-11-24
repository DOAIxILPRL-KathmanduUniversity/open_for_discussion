"""
Experiment 10: DocBin Serialization
Explores: DocBin for binary storage, round-trip serialization, corpus building
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from lang.ne import Nepali
from lang.ne.examples import sentences
from spacy.tokens import DocBin

nlp = Nepali()

print("=" * 60)
print("EXPERIMENT 10: DOCBIN SERIALIZATION")
print("=" * 60)

# --- A. Create DocBin from example sentences ---
print("\n--- A. Creating DocBin ---")
doc_bin = DocBin()
for text in sentences:
    doc = nlp(text)
    doc_bin.add(doc)
print(f"  Added {len(sentences)} docs to DocBin")

# --- B. Save to disk ---
output_path = os.path.join(PROJECT_ROOT, "corpus", "ne_examples.spacy")
os.makedirs(os.path.join(PROJECT_ROOT, "corpus"), exist_ok=True)
doc_bin.to_disk(output_path)
file_size = os.path.getsize(output_path)
print(f"  Saved to: {output_path}")
print(f"  File size: {file_size} bytes ({file_size/1024:.1f} KB)")

# --- C. Load back from disk ---
print("\n--- B. Loading DocBin Back ---")
doc_bin_loaded = DocBin().from_disk(output_path)
docs = list(doc_bin_loaded.get_docs(nlp.vocab))
print(f"  Loaded {len(docs)} docs")

# --- D. Verify round-trip integrity ---
print("\n--- C. Round-Trip Verification ---")
print(f"  {'Original':<50} {'Loaded':<50} {'Match'}")
print(f"  {'-'*105}")
all_match = True
for orig_text, loaded_doc in zip(sentences, docs):
    match = orig_text == loaded_doc.text
    if not match:
        all_match = False
    print(f"  {orig_text[:48]:<50} {loaded_doc.text[:48]:<50} {'✅' if match else '❌'}")

print(f"\n  Overall: {'ALL PASSED ✅' if all_match else 'SOME FAILED ❌'}")

# --- E. DocBin with annotations (simulate manual annotations) ---
print("\n--- D. DocBin with Entity Annotations ---")
from spacy.tokens import Span

annotated_bin = DocBin(store_user_data=True)

# Manually annotate a few docs
annotated_data = [
    ("रामले काठमाडौँमा भात खायो।", [(0, 4, "PERSON"), (5, 15, "GPE")]),
    ("गौतम बुद्धको जन्म लुम्बिनीमा भयो।", [(0, 11, "PERSON"), (18, 27, "GPE")]),
    ("नेपाल सरकारले नयाँ नीति ल्यायो।", [(0, 13, "ORG")]),
]

for text, ents in annotated_data:
    doc = nlp.make_doc(text)
    spans = []
    for start_char, end_char, label in ents:
        span = doc.char_span(start_char, end_char, label=label)
        if span:
            spans.append(span)
    doc.ents = spans
    annotated_bin.add(doc)

annotated_path = os.path.join(PROJECT_ROOT, "corpus", "ne_annotated.spacy")
annotated_bin.to_disk(annotated_path)
print(f"  Saved {len(annotated_data)} annotated docs to {annotated_path}")

# Verify annotations survived
loaded_ann = DocBin().from_disk(annotated_path)
for doc in loaded_ann.get_docs(nlp.vocab):
    if doc.ents:
        print(f"  '{doc.text[:40]}...' → {[(e.text, e.label_) for e in doc.ents]}")
