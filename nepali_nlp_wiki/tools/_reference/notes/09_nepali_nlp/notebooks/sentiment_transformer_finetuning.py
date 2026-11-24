from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
import numpy as np

# --- 1. CONFIG ---
MODEL = "google/muril-base-cased"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL, num_labels=3)

# --- 2. DATA ---
ds = load_dataset("Shushant/NepaliSentiment")
def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)

# Note: Labels must be mapped to integers (0, 1, 2)
# tokenized = ds.map(preprocess, batched=True)

# --- 3. TRAIN ---
args = TrainingArguments(output_dir="./sentiment-results", num_train_epochs=1)
# trainer = Trainer(model=model, args=args, train_dataset=tokenized["train"])
# trainer.train()
