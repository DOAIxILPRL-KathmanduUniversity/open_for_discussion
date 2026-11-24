# Attention Is All You Need

## The Paper (Vaswani et al., 2017)
- Ditched recurrence entirely
- Self-attention over all positions in parallel
- Multi-head attention for multiple representation subspaces

## Architecture
- Encoder: 6 layers of (self-attention → FFN)
- Decoder: 6 layers of (masked self-attention → cross-attention → FFN)
- Positional encoding: Restoring word order lost in parallel processing using sine/cosine functions.

## RNN vs. LSTM vs. Transformer
| Feature | RNN | LSTM | Transformer |
| :--- | :--- | :--- | :--- |
| **Processing** | Sequential | Sequential | Parallel |
| **Dependencies** | Short-range | Mid-range (Gating) | Long-range (Attention) |
| **Memory** | Hidden State | Cell State | Self-Attention |
| **Training Speed** | Slow | Slow | Fast (GPU parallel) |
| **Problem** | Vanishing Gradient | Computationally Heavy | Memory-intensive ($O(N^2)$) |

## Key Innovations
- Scaled dot-product attention: softmax(QK^T / √d) V
- Multi-head: concat(head₁, ..., head_h) W^O
- Layer normalization + residual connections

## Impact
- Enabled BERT, GPT, and everything since
- Parallelizable → massive scaling

- **Self-Attention**: Allows tokens to interact with each other to find context.
- **Multi-Head Attention (MHSA)**: Multiple sets of Q, K, V matrices running in parallel.
    - **Memory Cost**: MHSA has an $n^2$ memory cost. For a sentence of 10 words, 100 attention weights must be stored (Azunre et al., 2021).
    - **Interpretability**: Attention weights between tokens $x$ and $y$ can be interpreted as "how much are $x$ and $y$ related?"—useful for pronoun resolution (coreference).
- **Visualization**: Attention weights are often visualized as **heatmaps**, providing a window into what the model is "thinking" about when processing a specific token (e.g., seeing a pronoun attend strongly to its antecedent).

### Implementation Gist (NumPy Style)
```python
import numpy as np

# Step 1: Embeddings (3 words, 4 dimensions)
X = np.random.rand(3, 4)

# Step 2: Linear Transformations for Q, K, V
W_q, W_k, W_v = [np.random.rand(4, 4) for _ in range(3)]
Q, K, V = X @ W_q, X @ W_k, X @ W_v

# Step 3: Scaled Dot-Product Attention
scores = (Q @ K.T) / np.sqrt(K.shape[1])
weights = np.exp(scores) / np.sum(np.exp(scores), axis=1, keepdims=True)
output = weights @ V
```

## Scaling Laws
Empirical observations show that LLM performance improves predictably with:
1. **Compute**: Total FLOPs used during training.
2. **Dataset Size**: Number of tokens.
3. **Model Size**: Number of parameters.
- Performance follows a power law; increasing these factors yields diminishing but consistent returns.

## Efficient Attention Variants
To handle long sequences (where standard attention is $O(N^2)$):
- **Sparse Attention**: Tokens only attend to a subset of other tokens (e.g., BigBird).
- **Linear Attention**: Approaches that reduce complexity to $O(N)$ (e.g., Performer).

---

**Notebook**: [transformer_from_scratch.py](notebooks/transformer_from_scratch.py)

#transformers #attention #deep-learning
