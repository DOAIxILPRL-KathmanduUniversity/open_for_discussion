import json
import random
import torch
import editdistance
from datasets import load_dataset
from transformers import (AutoTokenizer, AutoModelForSeq2SeqLM, 
                          Seq2SeqTrainer, Seq2SeqTrainingArguments, 
                          EarlyStoppingCallback)
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# --- 1. CONFIG & DATA ---
MODEL_NAME = "google/mt5-base"
TRAIN_FILE = "train_split.jsonl"
VALID_FILE = "valid_split.jsonl"
OUTPUT_DIR = "./mt5-lemmatizer"
MAX_LENGTH = 32

def split_txt_to_jsonl(txt_file, train_file, test_file, train_ratio=0.8):
    with open(txt_file, "r", encoding="utf-8") as f:
        data = []
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                data.append({"input": parts[0].strip(), "output": parts[1].strip()})
    random.seed(42)
    random.shuffle(data)
    split_idx = int(len(data) * train_ratio)
    for fname, d in [(train_file, data[:split_idx]), (test_file, data[split_idx:])]:
        with open(fname, "w", encoding="utf-8") as out:
            for rec in d: out.write(json.dumps(rec, ensure_ascii=False) + "\n")

# --- 2. PREPROCESSING ---
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def preprocess_word_level(batch):
    inputs = ["lemmatize: ▁" + " ▁".join(x.split()) for x in batch["input"]]
    outputs = ["▁" + " ▁".join(x.split()) for x in batch["output"]]
    model_inputs = tokenizer(inputs, max_length=MAX_LENGTH, padding="max_length", truncation=True)
    labels = tokenizer(outputs, max_length=MAX_LENGTH, padding="max_length", truncation=True)
    model_inputs["labels"] = [[(t if t != tokenizer.pad_token_id else -100) for t in l] for l in labels["input_ids"]]
    return model_inputs

# --- 3. METRICS ---
def compute_metrics(eval_preds):
    preds, labels = eval_preds
    decoded_preds = tokenizer.batch_decode(torch.tensor(preds).long(), skip_special_tokens=True)
    labels_corrected = [[(t if t != -100 else tokenizer.pad_token_id) for t in l] for l in labels]
    decoded_labels = tokenizer.batch_decode(torch.tensor(labels_corrected).long(), skip_special_tokens=True)
    
    total_ed, total_chars = 0, 0
    for p, l in zip(decoded_preds, decoded_labels):
        total_ed += editdistance.eval(p, l)
        total_chars += len(l)
    
    return {
        "accuracy": sum(p == l for p, l in zip(decoded_preds, decoded_labels)) / len(decoded_preds),
        "cer": total_ed / total_chars if total_chars > 0 else 0.0
    }

# --- 4. TRAINER ---
if __name__ == "__main__":
    # Note: Requires gold_lemma_final.txt to exist
    # split_txt_to_jsonl("gold_lemma_final.txt", TRAIN_FILE, VALID_FILE)
    dataset = load_dataset("json", data_files={"train": TRAIN_FILE, "validation": VALID_FILE})
    tokenized_word = dataset.map(preprocess_word_level, batched=True)
    
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    args = Seq2SeqTrainingArguments(
        output_dir=OUTPUT_DIR, eval_strategy="steps", eval_steps=500,
        learning_rate=1e-5, per_device_train_batch_size=8, num_train_epochs=5,
        predict_with_generate=True, load_best_model_at_end=True, metric_for_best_model="cer",
        greater_is_better=False, report_to="none"
    )
    
    trainer = Seq2SeqTrainer(
        model=model, args=args, train_dataset=tokenized_word["train"],
        eval_dataset=tokenized_word["validation"], tokenizer=tokenizer,
        compute_metrics=compute_metrics, callbacks=[EarlyStoppingCallback(early_stopping_patience=3)]
    )
    # trainer.train()
