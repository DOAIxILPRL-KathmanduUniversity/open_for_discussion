import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM
from tqdm.auto import tqdm

# --- 1. CONFIG ---
MODEL = "google/muril-base-cased"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForMaskedLM.from_pretrained(MODEL)

def generate_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)
    return outputs.hidden_states[-1].mean(dim=1).squeeze().numpy()

if __name__ == "__main__":
    # Example: "आकाश means space"
    embed = generate_embedding("आकाश means space")
    print(f"Embedding Shape: {embed.shape}")
