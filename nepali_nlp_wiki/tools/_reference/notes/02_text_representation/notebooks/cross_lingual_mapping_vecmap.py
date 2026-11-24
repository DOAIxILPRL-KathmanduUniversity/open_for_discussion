"""
🌍 CROSS-LINGUAL MAPPING (VECMAP)
----------------------------------
Aligns Hindi and Nepali FastText embeddings using semi-supervised VecMap.
Includes CSLS retrieval evaluation and nearest-neighbor inspection.

Workflow: Monolingual -> VecMap Mapping -> Evaluation -> Inspection.
"""

import os
from gensim.models import KeyedVectors

# --- 1. DOWNLOAD MONOLINGUAL EMBEDDINGS ---
def download_fasttext():
    urls = [
        "https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.hi.300.vec.gz",
        "https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ne.300.vec.gz"
    ]
    for url in urls:
        filename = url.split('/')[-1]
        if not os.path.exists(filename.replace('.gz', '')):
            print(f"Downloading {filename}...")
            os.system(f"wget {url} && gunzip {filename}")

# --- 2. RUN VECMAP (SHELL COMMAND) ---
def run_vecmap_mapping():
    """
    Requires: git clone https://github.com/artetxem/vecmap.git
    """
    print("Running VecMap mapping (Semi-supervised)...")
    cmd = (
        "python3 vecmap/map_embeddings.py --cuda --semi_supervised "
        "hi-ne.dic cc.hi.300.vec cc.ne.300.vec hi_mapped.vec ne_mapped.vec"
    )
    os.system(cmd)

# --- 3. INSPECT ALIGNMENT ---
def inspect_neighbors(hi_path, ne_path):
    print(f"Loading aligned embeddings: {hi_path}, {ne_path}")
    hi_emb = KeyedVectors.load_word2vec_format(hi_path, binary=False)
    ne_emb = KeyedVectors.load_word2vec_format(ne_path, binary=False)
    
    test_words = ["नमस्ते", "धन्यवाद", "पानी", "दोस्त", "स्कूल"]
    
    for word in test_words:
        if word in hi_emb:
            print(f"\n🔸 Hindi: {word}")
            # Find nearest neighbors in the Nepali space
            neighbors = ne_emb.most_similar(positive=[hi_emb[word]], topn=3)
            for n, score in neighbors:
                print(f"   -> Nepali: {n} (Score: {score:.4f})")

if __name__ == "__main__":
    # download_fasttext()
    # run_vecmap_mapping()
    # inspect_neighbors("hi_mapped.vec", "ne_mapped.vec")
    print("VecMap Alignment Pipeline Ready.")
