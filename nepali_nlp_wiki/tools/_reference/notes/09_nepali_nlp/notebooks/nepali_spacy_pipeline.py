"""
🇳🇵 NEPALI SPACY PIPELINE (Sentencizer + Custom Stemmer)
-------------------------------------------------------
Builds a custom spaCy pipeline for Nepali text.
Includes a custom 'stem' attribute for tokens using nepali-stemmer.

Dependencies: pip install spacy nepali-stemmer
"""

import spacy
from nepali_stemmer.stemmer import NepStemmer

# Initialize Stemmer
nepstem = NepStemmer()

@spacy.Language.component("nepali_stemmer_component")
def nepali_stemmer_component(doc):
    # Ensure custom attribute exists
    if not spacy.tokens.Token.has_extension("stem"):
        spacy.tokens.Token.set_extension("stem", default=None)
    
    for token in doc:
        # Apply stemmer
        res = nepstem.stem(token.text)
        token._.stem = res.split(' ')[0] if res else token.text
    return doc

def build_pipeline():
    print("Initializing blank Nepali model...")
    nlp = spacy.blank("ne")
    
    # 1. Add Sentencizer
    nlp.add_pipe("sentencizer")
    
    # 2. Add Custom Stemmer
    nlp.add_pipe("nepali_stemmer_component", after="sentencizer")
    
    return nlp

def test_pipeline(nlp, text):
    doc = nlp(text)
    print(f"Original Text: {text}\n")
    print(f"{'Token':<15} | {'Stem':<15}")
    print("-" * 32)
    for token in doc:
        print(f"{token.text:<15} | {token._.stem:<15}")

if __name__ == "__main__":
    # nlp = build_pipeline()
    # text = "नेपालको राजधानी काठमाडौं हो। हामीले आज धेरै किताबहरु पढ्यौँ।"
    # test_pipeline(nlp, text)
    print("Nepali spaCy Pipeline Module Ready.")
