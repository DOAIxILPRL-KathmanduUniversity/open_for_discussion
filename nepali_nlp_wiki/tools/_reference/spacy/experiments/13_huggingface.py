"""
Experiment 13: HuggingFace Pipeline Integration
Explores: Using HF transformers as spaCy pipeline components (token classification for NER)
Adapted from: spacy-huggingface-pipelines/spacy_huggingface_pipelines/token_classification.py

NOTE: This experiment requires `transformers` and `torch` to be installed.
      Run: uv pip install transformers torch
      If not available, the experiment will print the architecture pattern instead.
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lang.ne import Nepali
from spacy.language import Language
from spacy.tokens import Doc, SpanGroup
from spacy.pipeline import Pipe

print("=" * 60)
print("EXPERIMENT 13: HUGGINGFACE PIPELINE INTEGRATION")
print("=" * 60)

# --- A. Architecture Pattern (always works) ---
print("\n--- A. HF Integration Architecture ---")
print("""
  The spacy-huggingface-pipelines library provides two components:
  
  1. hf_token_pipe  → Token classification (NER, POS)
     - Wraps: transformers.pipeline("token-classification")
     - Can annotate: ents, pos, spans, tag
     
  2. hf_text_pipe   → Text classification (Sentiment, Topic)
     - Wraps: transformers.pipeline("text-classification")
     - Can annotate: doc.cats
  
  Usage pattern:
    nlp = spacy.blank("ne")
    nlp.add_pipe("hf_token_pipe", config={
        "model": "Davlan/bert-base-multilingual-cased-ner-hrl",
        "aggregation_strategy": "average",
        "annotate": "ents",
    })
    doc = nlp("काठमाडौँ नेपालको राजधानी हो।")
""")

# --- B. Try live integration ---
print("--- B. Live Integration Attempt ---")
try:
    from transformers import pipeline as hf_pipeline
    
    print("  ✅ transformers found, testing multilingual NER...")
    
    # Use a multilingual NER model
    ner = hf_pipeline(
        "token-classification",
        model="Davlan/bert-base-multilingual-cased-ner-hrl",
        aggregation_strategy="average",
    )
    
    nepali_texts = [
        "काठमाडौँ नेपालको राजधानी हो।",
        "गौतम बुद्धको जन्मस्थल लुम्बिनी हो।",
        "राम र सीता अयोध्या गए।",
    ]
    
    for text in nepali_texts:
        results = ner(text)
        print(f"\n  '{text}'")
        if results:
            for r in results:
                print(f"    → [{r['entity_group']}] '{r['word']}' (score: {r['score']:.3f})")
        else:
            print(f"    → (no entities detected)")

except ImportError:
    print("  ⚠ transformers not installed. Showing mock output instead.")
    print("  Install with: uv pip install transformers torch")
    print()
    print("  Mock output for 'काठमाडौँ नेपालको राजधानी हो।':")
    print("    → [LOC] 'काठमाडौँ' (score: 0.95)")
    print("    → [LOC] 'नेपाल' (score: 0.89)")

# --- C. Custom wrapper pattern ---
print("\n--- C. Custom Wrapper Pattern ---")
print("""
  To build your own HF-spaCy bridge (like in the repo):
  
  @Language.factory("my_hf_ner")
  class MyHFNER(Pipe):
      def __init__(self, nlp, name, model_name):
          self.hf_pipe = hf_pipeline("ner", model=model_name)
      
      def __call__(self, doc):
          results = self.hf_pipe(doc.text)
          spans = SpanGroup(doc)
          for r in results:
              span = doc.char_span(r["start"], r["end"], label=r["entity_group"])
              if span:
                  spans.append(span)
          doc.ents = list(spans)
          return doc
""")
