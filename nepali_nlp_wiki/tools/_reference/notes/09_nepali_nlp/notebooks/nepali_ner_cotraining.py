"""
🇳🇵 SEMI-SUPERVISED NER CO-TRAINING (Nepali)
--------------------------------------------
Implements the Co-Training algorithm for BIO tagging.
Uses Morphology (Word) and Context (Neighbors) as independent views.

Dataset: ebiquity/cleaned/total.bio (Nepali NER)
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# --- 1. DATA LOADER ---
def load_bio(file_path):
    sentences = []
    current_sent = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                if current_sent: sentences.append(current_sent); current_sent = []
            else:
                parts = line.split()
                if len(parts) >= 2: current_sent.append((parts[0], parts[1]))
    return sentences

# --- 2. VIEW EXTRACTION ---
def get_views(sentences):
    view1_morph = [] # Features: The word itself
    view2_context = [] # Features: Previous + Next word
    labels = []
    for sent in sentences:
        for i in range(len(sent)):
            word, label = sent[i]
            prev = sent[i-1][0] if i > 0 else "<s>"
            nxt = sent[i+1][0] if i < len(sent)-1 else "</s>"
            view1_morph.append(word)
            view2_context.append(f"{prev} {nxt}")
            labels.append(label)
    return view1_morph, view2_context, np.array(labels)

# --- 3. CO-TRAINING LOOP ---
def run_cotraining(l_morph, l_context, l_labels, u_morph, u_context, iterations=5):
    for it in range(iterations):
        print(f"Iteration {it+1}: Labeled samples = {len(l_labels)}")
        
        # Train View 1 (Morphology)
        vec1 = TfidfVectorizer(analyzer='char_wb', ngram_range=(2,4))
        X1 = vec1.fit_transform(l_morph)
        clf1 = RandomForestClassifier(n_estimators=50).fit(X1, l_labels)
        
        # Train View 2 (Context)
        vec2 = TfidfVectorizer(ngram_range=(1,2))
        X2 = vec2.fit_transform(l_context)
        clf2 = RandomForestClassifier(n_estimators=50).fit(X2, l_labels)
        
        # Logic to pick most confident unlabeled samples and add to labeled set...
        # (Simplified for the preview script)
        print("Finding confident labels from unlabeled pool...")

if __name__ == "__main__":
    # path = "total.bio"
    # sents = load_bio(path)
    # Train/Test/Unlabeled split...
    print("NER Co-Training Module Initialized.")
