"""
🌐 CROSS-LINGUAL EMBEDDING FILTER (Hi-Ne)
------------------------------------------
Downloads aligned Hindi-Nepali embeddings and filters them using lemma lists.
Produces high-density, lemma-only vector files for cross-lingual transfer.

Dependencies: pip install huggingface_hub
"""

import os
from huggingface_hub import snapshot_download

# --- CONFIGURATION ---
REPO_ID = "sundeepdwd/hi-ne-aligned-embeddings"
LOCAL_DIR = "hi-ne-aligned-embeddings"
OUTPUT_DIR = 'aligned_lemma_only'

HI_LEMMAS_FILE = 'hindi_single_lemmas.txt'
NE_LEMMAS_FILE = 'newnepali_single_lemmas.txt'

def download_embeddings():
    if not os.path.exists(LOCAL_DIR):
        print(f"Downloading {REPO_ID}...")
        snapshot_download(repo_id=REPO_ID, local_dir=LOCAL_DIR, repo_type="dataset")

def load_lemmas(file_path):
    lemmas = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                lemma = line.strip()
                if lemma: lemmas.add(lemma)
        print(f"Loaded {len(lemmas)} lemmas from {file_path}")
    except FileNotFoundError:
        print(f"Warning: {file_path} not found.")
    return lemmas

def filter_vec(input_path, output_path, lemma_set):
    count = 0
    if not os.path.exists(input_path):
        print(f"Error: {input_path} missing.")
        return
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        
        # Handle Header
        first_line = infile.readline()
        if first_line:
            parts = first_line.strip().split()
            if len(parts) == 2 and parts[0].isdigit():
                outfile.write(first_line) # Simple header passthrough
            else:
                # Process if first line is a word
                word = parts[0]
                if word in lemma_set:
                    outfile.write(first_line)
                    count += 1

        for line in infile:
            word = line.split(' ', 1)[0]
            if word in lemma_set:
                outfile.write(line)
                count += 1
                
    print(f"Saved {count} filtered vectors to {output_path}")

def main():
    download_embeddings()
    
    hi_lemmas = load_lemmas(HI_LEMMAS_FILE)
    ne_lemmas = load_lemmas(NE_LEMMAS_FILE)
    
    filter_vec(f'{LOCAL_DIR}/aligned/hi_mapped.vec', f'{OUTPUT_DIR}/hi_lemma_only.vec', hi_lemmas)
    filter_vec(f'{LOCAL_DIR}/aligned/ne_mapped.vec', f'{OUTPUT_DIR}/ne_lemma_only.vec', ne_lemmas)

if __name__ == "__main__":
    main()
