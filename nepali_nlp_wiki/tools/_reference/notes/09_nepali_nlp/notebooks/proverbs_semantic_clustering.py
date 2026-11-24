import numpy as np
import torch
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from transformers import AutoModel, AutoTokenizer

# --- 1. MODEL INITIALIZATION ---
MODEL_NAME = "google/muril-base-cased"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME)

# --- 2. DATA (MOCK REPRESENTATION) ---
# In a real scenario, this would load the full JSON structure provided in the request
proverbs = [
    "लोग्ने स्वास्नीको झगडा, परालको आगो ।",
    "गृहिणी बिनाको घर भूतको डेरा ।",
    "ठेस नलागी आमाबाबु सम्झिँदैन ।",
    "मर्दका दसवटी हुन्छन्।",
    "आफै बोक्सी, आफै धामी ।"
]
categories = ["Family", "Women", "Parents", "Polygamy", "Superstition"]

# --- 3. EMBEDDING GENERATION ---
def get_embeddings(texts):
    encoded = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        output = model(**encoded)
    return output.last_hidden_state.mean(dim=1).numpy()

embeddings = get_embeddings(proverbs)

# --- 4. PCA & CLUSTERING ---
pca = PCA(n_components=2)
reduced = pca.fit_transform(embeddings)

kmeans = KMeans(n_clusters=len(set(categories)), random_state=0)
clusters = kmeans.fit_predict(embeddings)

# --- 5. VISUALIZATION ---
def plot_semantic_space(reduced_data, categories):
    plt.figure(figsize=(10, 7))
    for i, category in enumerate(categories):
        plt.scatter(reduced_data[i, 0], reduced_data[i, 1], label=category)
        plt.annotate(category, (reduced_data[i, 0], reduced_data[i, 1]))
    plt.title("Semantic Space of Nepali Proverbs (MURIL + PCA)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_semantic_space(reduced, categories)
