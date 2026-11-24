from transformers import AutoTokenizer, BertConfig, BertForMaskedLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset, Dataset
from itertools import islice

# --- 1. CONFIG ---
tokenizer = AutoTokenizer.from_pretrained("CohleM/bert-nepali-tokenizer")
config = BertConfig(
    num_hidden_layers=6, vocab_size=tokenizer.vocab_size,
    hidden_size=768, num_attention_heads=12, max_position_embeddings=256
)
model = BertForMaskedLM(config)

# --- 2. DATA ---
streamed = load_dataset("IRIIS-RESEARCH/Nepali-Text-Corpus", split="train", streaming=True)
dataset = Dataset.from_list(list(islice(streamed, 1000))) # Reduced for demo

def tokenize(batch):
    return tokenizer(batch["Article"], truncation=True, max_length=256)

tokenized = dataset.map(tokenize, batched=True)
collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

# --- 3. TRAIN ---
args = TrainingArguments(
    output_dir="./bert-nepali", num_train_epochs=1, 
    per_device_train_batch_size=4, eval_strategy="no"
)
trainer = Trainer(model=model, args=args, train_dataset=tokenized, data_collator=collator)
# trainer.train()
