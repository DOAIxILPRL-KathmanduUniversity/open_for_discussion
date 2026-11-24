# LLM Architecture From Scratch

> [!IMPORTANT] Gist
> Building a Large Language Model (LLM) from scratch requires a systematic, 3-stage approach: **Coding the Architecture** (Stage 1), **Pre-training** on unlabeled data (Stage 2), and **Fine-tuning** for specific tasks (Stage 3). This "no-black-box" methodology ensures deep understanding of the transformer's inner workings (Raschka, 2025).

## 1. The 3-Stage Lifecycle
| Stage | Focus | Data Type | Output |
| :--- | :--- | :--- | :--- |
| **Stage 1** | Architecture & Sampling | Small samples | Implemented GPT Model |
| **Stage 2** | Pre-training | Unlabeled (Massive) | Foundation Model |
| **Stage 3** | Fine-tuning | Labeled (Instruction/Class) | Personal Assistant / Classifier |

## 2. Coding Attention Mechanisms
The heart of the transformer is the Attention mechanism, which allows the model to capture dependencies regardless of distance.

### A. Self-Attention
- **Concept**: Tokens "attend" to all other tokens in the sequence to compute a weighted representation.
- **Process**: Compute Queries ($Q$), Keys ($K$), and Values ($V$) via linear layers.
- **Score**: $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$.

### B. Causal (Masked) Attention
- **Goal**: Ensure the model cannot "see the future" during pre-training.
- **Implementation**: Apply a triangular mask to the attention scores (setting future token scores to $-\infty$ before softmax). This is essential for **Autoregressive Generation**.

### C. Multi-Head Attention
- **Scaling**: Instead of one large attention calculation, split the embedding dimension into multiple "heads."
- **Benefit**: Allows the model to attend to different information subspaces (e.g., syntax vs. semantics) in parallel.

## 3. The GPT Block Components
Beyond attention, the GPT architecture relies on specific stabilizing layers:
- **Layer Normalization (LayerNorm)**: Normalizes activations across the feature dimension (instead of batch dimension), critical for training stability in deep networks.
- **GELU (Gaussian Error Linear Unit)**: A non-linear activation function that provides a smoother gradient than ReLU, widely used in modern LLMs.
- **Shortcut Connections**: Also known as "skip connections" or "residual connections," these allow gradients to flow through deep layers without vanishing, enabling the training of very deep architectures.

## 4. PyTorch Architectural Implementation (Leblanc, 2024)
While custom blocks are standard, PyTorch provides high-level primitives for faster prototyping:
- **`nn.RNN` / `nn.LSTM`**: Sequential processors where internal states carry historical context. LSTMs use "gates" to manage long-term memory.
- **`nn.Transformer`**: A complete Encoder-Decoder suite.
    - **`TransformerEncoderLayer`**: Combines Multi-head Attention + Feedforward + LayerNorm.
- **Implementation Strategy**: Start with simple RNNs to master sequence processing, then transition to LSTMs for longer context, and finally Transformers for global, parallel dependencies.

## 5. Text Data Preparation
- **Byte Pair Encoding (BPE)**: Breaks words into subword units (e.g., "unknownPlace" $\rightarrow$ ["unknown", "Place"]), solving the "out-of-vocabulary" (OOV) problem.
- **Sliding Window Sampling**: Creating input-target pairs by shifting the input by one token.
    - *Input*: "LLMs are" $\rightarrow$ *Target*: "are powerful".

## 6. Decoding Strategies
How the model chooses the next token:
- **Temperature Scaling**: Controls randomness. Higher temperature ($T > 1$) increases diversity; lower temperature ($T < 1$) makes the model more confident/greedy.
- **Top-k Sampling**: Limits the vocabulary to the top $k$ most likely next tokens, preventing the model from choosing highly improbable (junk) tokens.

## 7. Looking Inside the Loop (Alammar & Grootendorst, 2024)
Generative LLMs are **Autoregressive**: they consume their own previous outputs to make future predictions.

### The Autoregressive Generation Cycle
1.  **Input**: A text prompt is tokenized into IDs.
2.  **Forward Pass**: The model processes the token IDs through the Transformer blocks.
3.  **Output**: The model produces a probability distribution over the entire vocabulary for the *next* token.
4.  **Sampling**: One token is selected (via Greedy, Temperature, or Top-k).
5.  **Feedback**: The selected token is appended to the original prompt, and the process repeats (Pass 2, Pass 3, etc.).
6.  **Termination**: The loop stops when an `<|endoftext|>` or `</s>` token is generated or the maximum length is reached.

---

#llm-engineering #raschka-2025 #transformer-architecture #attention #pretraining #finetuning #lora
