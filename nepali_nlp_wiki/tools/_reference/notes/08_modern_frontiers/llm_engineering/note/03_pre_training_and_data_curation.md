# LLM Pre-Training & Data Curation

> [!IMPORTANT] Gist
> The quality of an LLM is a direct reflection of its training data. Production-grade models require massive, diverse, and rigorously cleaned datasets to move beyond "garbage in, garbage out" (Pai, 2025).

## 1. LLM Scaling Laws
Understanding the relationship between compute, data, and model size:
- **Kaplan et al. (OpenAI, 2020)**: Proposed a power-law where model size is more important than data size. Larger models are more sample-efficient.
- **Hoffmann et al. (Chinchilla, DeepMind, 2022)**: Corrected the laws, showing that for every doubling of model parameters, the training data must also double to be "compute-optimal."
- **Underpopulated Models**: A common pitfall where the parameter count is disproportionately high compared to the data size, leading to undertrained weights (Raaijmakers, 2025).
- **Current Trend**: Training smaller models (SLMs) on significantly more data (trillions of tokens) to optimize for inference efficiency.

## 2. Pre-Training Ingredients
### Popular Datasets
- **Common Crawl / C4**: Massive web scrapes, cleaned for quality.
- **The Pile (EleutherAI)**: 825GB of diverse data including PubMed, GitHub, and StackExchange.
- **FineWeb (HuggingFace)**: 15 trillion tokens from Common Crawl, rigorously filtered.
- **FineWeb-Edu**: A subset focused on high-educational-value content.

### Synthetic Data (The "Phi" Revolution)
When human-generated data is insufficient or noisy, LLMs are used to generate synthetic textbooks and reasoning paths:
- **phi-1.5**: Trained on 20B synthetic tokens (Microsoft).
- **Cosmopedia**: 30 million synthetic textbooks and blog posts generated via Mistral (HuggingFace).

## 3. Data Preprocessing Pipeline
1. **Extraction & Boilerplate Removal**: Using tools like `jusText`, `Trafilatura`, or custom HTML parsers to strip menu text and ads while preserving content structure.
2. **Language Identification**: Filtering for specific languages (e.g., English > 0.99 probability).
3. **Deduplication**: Removing near-duplicate documents to prevent the model from over-memorizing specific patterns.
4. **Decontamination**: Ensuring that benchmark test questions (MMLU, ARC) are not present in the training set.
5. **PII Removal**: Detecting and stripping Personally Identifiable Information.

## 4. Implementation: Working with Text Data
Practical steps for preparing data for Stage 2 Pre-training (Raschka, 2025):

1.  **Tokenization Methods (Alammar & Grootendorst, 2024)**:
    - **Word Tokens**: Simple but results in huge vocabularies and "Out-of-Vocabulary" (OOV) errors.
    - **Character Tokens**: Solves OOV but makes the model's job harder (learning to spell) and reduces effective context length.
    - **Subword Tokens (BPE, WordPiece)**: The industry standard. Balances vocabulary size and expressivity.
    - **Byte Tokens**: Tokenization-free encoding (e.g., ByT5). Native handling of all UTF-8 characters without OOV.

2.  **Tokenizer Design Choices**:
    - **Vocabulary Size**: Typically 30k (BERT) to 100k+ (GPT-4). Larger vocabularies represent text with fewer tokens but require more embedding memory.
    - **Special Tokens**: 
        - `[CLS]` / `<s>`: Start of text/Classification.
        - `[SEP]` / `</s>`: End of text/Separator.
        - `[MASK]`: Masking for training.
        - `[UNK]`: Fallback for unknown tokens.
        - **Chat Tokens**: `<|user|>`, `<|assistant|>`, `<|system|>` (Phi-3/Llama-3).
    - **Domain Adaptation**: Code-focused tokenizers (StarCoder) use specific whitespace/tab tokens to preserve indentation.

3.  **Token ID Mapping**: Converting tokens into unique integers.
4.  **Sliding Window Sampling**: Generating training pairs $(x, y)$ where $x$ is the input context and $y$ is the input shifted by one token (next-token prediction).
    - *Example*: `[The, quick, brown, fox]` $\rightarrow$ `x: [The, quick, brown], y: [quick, brown, fox]`.
5.  **Token & Positional Embeddings**: Converting IDs into dense vectors and adding positional information to compensate for the transformer's lack of inherent sequence order.

## 5. Grounding and Meaning
- **Form vs. Meaning**: LLMs learn the "form" of language (statistical distribution of tokens). True "grounding" requires connecting this form to real-world communicative intent or multimodal signals (Pai, 2025).
- **Ambiguity**: Modern LLMs still struggle with linguistic ambiguity (e.g., "WWE's John Cena surprises Make-A-Wish 7-year-old with cancer").

## 6. Training on a Shoestring Budget (Leblanc, 2024)
When hardware resources are limited, these PyTorch-native techniques optimize memory and compute:
- **Gradient Accumulation**: Updates parameters every $N$ batches instead of every batch. This simulates a larger batch size on hardware with low VRAM.
- **Mixed Precision (FP16)**: Reduces memory usage and doubles speed on modern GPUs by performing math in 16-bit half-precision.
- **Knowledge Distillation**: Training a small "student" model to mimic a larger "teacher" model's outputs (Attention Transfer or Hint Learning).
- **Pruning & Quantization**: Removing less important weights and converting weights to 8-bit integers (`int8`) to minimize footprint and enable edge deployment.

---

#llm-engineering #scaling-laws #chinchilla #synthetic-data #data-curation #phi-1.5 #cosmopedia
