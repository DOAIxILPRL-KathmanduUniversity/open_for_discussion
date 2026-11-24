# Seq2Seq & Attention

## Seq2Seq (Sutskever et al., 2014)
- Encoder reads input → fixed-length context vector
- Decoder generates output token by token
- Bottleneck: all info compressed into one vector

## Attention (Bahdanau et al., 2015)
- Decoder attends to all encoder hidden states
- Weighted sum based on relevance scores
- Eliminates the information bottleneck

## Search Strategies
- **Beam Search**: Instead of picking the single best token (Greedy), keep $k$ hypotheses at each step.
- **Pruning**: Removing low-probability paths during search to save computation.
- **Exact Search**: Methods like Viterbi for global optimization in sequence labeling.

## Attention Variants
- **QKV Attention**: Query (what I'm looking for), Key (what I have), Value (the actual info).
- **Multi-layer Attention**: Stacking attention mechanisms to capture hierarchical relationships.
- **Hierarchical Attention**: Focusing on words within sentences, and then sentences within documents.

## Scaled Dot-Product Attention
Formally introduced in the Transformer architecture but applicable to sequence models. The similarity between a Query ($Q$), Key ($K$), and Value ($V$) is calculated as (Vaswani et al., 2017; Hayinaer et al., 2025):

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Where:
- $d_k$ is the dimension of the keys, used for scaling to prevent gradient vanishing in the softmax.
- Dot-product similarity is used as the scoring function.

---

**Notebook**: [seq2seq_attention_lab.py](notebooks/seq2seq_attention_lab.py)

#sequence #attention #deep-learning
