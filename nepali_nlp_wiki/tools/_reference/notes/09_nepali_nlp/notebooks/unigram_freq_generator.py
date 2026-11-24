from polyglot_tokenizer import Tokenizer
from collections import Counter
from tqdm import tqdm
import csv

# --- CONFIG ---
FILE_PATH = '/content/clean_date_categories.csv'
LINE_COUNT = 28084653  # pre-calculated with !wc -l
OUTPUT_PATH = 'unigram_frequencies.csv'

# --- PROCESSING ---
tk_ne = Tokenizer(lang='ne')
unigram_frequencies = Counter()

def generate_unigrams():
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            for line in tqdm(f, total=LINE_COUNT, desc="Tokenizing Large Corpus"):
                tokens = tk_ne.tokenize(line.strip())
                unigram_frequencies.update(tokens)
        
        # Export
        with open(OUTPUT_PATH, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['token', 'frequency'])
            for token, freq in unigram_frequencies.items():
                writer.writerow([token, freq])
        print(f"Success: Exported to {OUTPUT_PATH}")
    except FileNotFoundError:
        print(f"Error: {FILE_PATH} not found.")

if __name__ == "__main__":
    # generate_unigrams()
    pass
