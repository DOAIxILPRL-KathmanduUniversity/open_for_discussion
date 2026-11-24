"""
🇳🇵 NEPALI LEMMATIZER INFERENCE (mT5-base)
------------------------------------------
Batch processing script for lemmatizing Nepali text using sunilregmi/nepali-lemmatizerV1.
Optimized for GPU execution and pandas-based datasets.

Dependencies: pip install sentencepiece transformers pandas tqdm torch
"""

import torch
import pandas as pd
from transformers import MT5ForConditionalGeneration, T5Tokenizer
from tqdm.auto import tqdm

# --- CONFIGURATION ---
MODEL_NAME = "sunilregmi/nepali-lemmatizerV1-mt5-base"
MAX_LENGTH = 10
INPUT_CSV  = 'overstemming_test.csv'
OUTPUT_CSV = 'overstemming_test_modeloutput.csv'

# Initialize tqdm for pandas
tqdm.pandas()

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

def load_model():
    print(f"Loading {MODEL_NAME}...")
    tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME, use_fast=False)
    model = MT5ForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)
    return model, tokenizer

def lemmatize(word, model, tokenizer):
    input_text = f"lemmatize: {word}"
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=MAX_LENGTH)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def process_file(file_path, output_path):
    model, tokenizer = load_model()
    
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Creating a sample...")
        df = pd.DataFrame({'word': ["छ", "खऱन्छु", "गएको", "डेखेको", "गर्दैछ", "बजाइरहेको"]})
    
    print('Processing lemmatization...')
    df['lemma'] = df['word'].astype(str).progress_apply(lambda x: lemmatize(x, model, tokenizer))
    
    df.to_csv(output_path, index=False)
    print(f'Results saved to {output_path}')
    return df

if __name__ == "__main__":
    process_file(INPUT_CSV, OUTPUT_CSV)
