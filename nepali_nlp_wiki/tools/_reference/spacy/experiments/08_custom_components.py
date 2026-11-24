"""
Experiment 08: Custom Pipeline Components
Explores: @Language.component, @Language.factory, pipeline ordering, component data flow
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang.ne import Nepali
from spacy.language import Language
from spacy.tokens import Doc, Token

nlp = Nepali()

print("=" * 60)
print("EXPERIMENT 08: CUSTOM PIPELINE COMPONENTS")
print("=" * 60)

# --- A. Simple stateless component ---
@Language.component("nepali_debug_logger")
def debug_logger(doc):
    """Logs basic stats about each doc passing through the pipeline."""
    devanagari_count = sum(1 for t in doc if any('\u0900' <= c <= '\u097F' for c in t.text))
    print(f"  [DEBUG] tokens={len(doc)}, devanagari={devanagari_count}")
    return doc

# --- B. Factory-based component (with config) ---
@Language.factory("nepali_postposition_tagger", default_config={"case_map": {}})
class PostpositionTagger:
    """Tags tokens with Nepali case information based on suffix patterns."""
    
    def __init__(self, nlp, name, case_map):
        self.case_map = case_map or {
            "ले": "ERG",   # Ergative
            "मा": "LOC",   # Locative
            "को": "GEN",   # Genitive
            "लाई": "DAT",  # Dative
            "बाट": "ABL",  # Ablative
            "सँग": "COM",  # Comitative
        }
        if not Token.has_extension("case"):
            Token.set_extension("case", default="NOM")
    
    def __call__(self, doc):
        for token in doc:
            for suffix, case in self.case_map.items():
                if token.text.endswith(suffix) and len(token.text) > len(suffix):
                    token._.case = case
                    break
        return doc

# --- C. Word-frequency counter component ---
@Language.factory("nepali_freq_counter", default_config={"top_n": 5})
class FreqCounter:
    """Attaches token frequency data to the Doc."""
    
    def __init__(self, nlp, name, top_n):
        self.top_n = top_n
        self.global_counts = {}
        if not Doc.has_extension("word_freqs"):
            Doc.set_extension("word_freqs", default=None)
    
    def __call__(self, doc):
        from collections import Counter
        counts = Counter(t.text for t in doc if t.is_alpha)
        doc._.word_freqs = counts.most_common(self.top_n)
        # Update global
        for t in doc:
            if t.is_alpha:
                self.global_counts[t.text] = self.global_counts.get(t.text, 0) + 1
        return doc

# --- D. Assemble the pipeline ---
nlp.add_pipe("nepali_debug_logger", first=True)
nlp.add_pipe("nepali_postposition_tagger", after="nepali_debug_logger")
nlp.add_pipe("nepali_freq_counter", last=True)

print("\n--- A. Pipeline Overview ---")
print(f"  Components: {nlp.pipe_names}")

# --- E. Process texts ---
print("\n--- B. Processing Texts ---")
texts = [
    "रामले काठमाडौँमा भात खायो।",
    "सीतालाई रामले फूल दियो।",
    "हामी पोखराबाट आयौँ।",
    "उनीसँग म कुरा गरें।",
]

for text in texts:
    print(f"\n  Input: '{text}'")
    doc = nlp(text)
    
    # Show case tags
    case_tagged = [(t.text, t._.case) for t in doc if t._.case != "NOM"]
    if case_tagged:
        print(f"  Cases: {case_tagged}")
    
    # Show word frequencies
    print(f"  Top words: {doc._.word_freqs}")

# --- F. Inspect global frequency ---
print("\n--- C. Global Frequency Table ---")
freq_comp = nlp.get_pipe("nepali_freq_counter")
sorted_global = sorted(freq_comp.global_counts.items(), key=lambda x: -x[1])[:10]
print(f"  {'Word':<15} {'Count':>5}")
print(f"  {'-'*20}")
for word, count in sorted_global:
    print(f"  {word:<15} {count:>5}")
