"""
🔍 CORPUS ANALYSIS MASTERCLASS (NLTK & NEPALI NEWS)
--------------------------------------------------
Exploratory analysis of the Nepali News Dataset (Agriculture category).
Demonstrates Concordance, Distributional Similarity, and Common Contexts.

Dependencies: pip install nltk kagglehub
"""

import nltk
import kagglehub
import os

# --- 1. DATA ACQUISITION ---
def download_nepali_news():
    print("Downloading Nepali News Dataset from Kaggle...")
    path = kagglehub.dataset_download("ashokpant/nepali-news-dataset-large")
    # Path to Agriculture category
    base_dir = f"{path}/nepali_news_dataset_20_categories_large/nepali_news_dataset_20_categories_large/Agriculture"
    return base_dir

# --- 2. ANALYSIS ENGINE ---
def analyze_corpus(agriculture_dir):
    # Load first few files
    raw_text = ""
    for i in range(1, 6):
        file_path = f"{agriculture_dir}/{i}.txt"
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_text += f.read() + "\n"
    
    print("Tokenizing...")
    tokens = nltk.word_tokenize(raw_text)
    doc = nltk.Text(tokens)
    
    print("\n--- 1. Concordance for 'खेती' (Farming) ---")
    doc.concordance("खेती")
    
    print("\n--- 2. Words similar to 'छ' (is) ---")
    doc.similar("छ", num=5)
    
    print("\n--- 3. Common Contexts for ['खेती', 'सुरु'] ---")
    doc.common_contexts(["खेती", "सुरु"])

if __name__ == "__main__":
    # nltk.download('punkt')
    # ag_dir = download_nepali_news()
    # analyze_corpus(ag_dir)
    print("Corpus Analysis Engine Ready.")
