# Bidirectional LSTM (Bi-LSTM)

Bidirectional LSTMs process the input sequence in both forward and backward directions, allowing the model to capture both preceding and succeeding context for each token (Schuster & Paliwal, 1997).

## Architecture

A Bi-LSTM consists of two independent LSTMs:
1. **Forward LSTM**: Processes the sequence from $x_1$ to $x_n$, generating hidden states $\overrightarrow{h}_i$.
2. **Backward LSTM**: Processes the sequence from $x_n$ to $x_1$, generating hidden states $\overleftarrow{h}_i$.

The output for each timestep $i$ is the concatenation of these two states:
$$h_i = [\overrightarrow{h}_i : \overleftarrow{h}_i]$$

## Mathematical Formulation

For each timestep $i$:
$$\overrightarrow{h}_i = \text{LSTM}_{fwd}(x_i, \overrightarrow{h}_{i-1})$$
$$\overleftarrow{h}_i = \text{LSTM}_{bwd}(x_i, \overleftarrow{h}_{i+1})$$
$$y_i = g(W \cdot h_i + b)$$

Where:
- $x_i$ is the input vector (embedding).
- $h_i \in \mathbb{R}^{2 \cdot d_{hidden}}$ if each LSTM has $d_{hidden}$ units.
- $g$ is an activation function (typically softmax for classification tasks).

## Applications in NLP

### 1. POS Tagging
Bi-LSTMs are the standard architecture for neural POS tagging. They provide a rich representation of the word's context, which is crucial for disambiguating grammatical categories.
- Zero-shot POS tagging with pre-trained Bi-LSTMs reaches high accuracy on diverse languages (Author et al., Year).
- See [[03_classical_nlp/pos_tagging]] for task details.

### 2. Named Entity Recognition
Often combined with a CRF layer (BiLSTM-CRF) to model entity label dependencies.
- Achieves 91.2 F1 on CoNLL-2003 (Lample et al., 2016).
- Using **Word + Stem embeddings** in Bi-LSTMs mitigates data sparsity in low-resource languages like Kazakh (Hayinaer et al., 2025).
- See [[03_classical_nlp/named_entity_recognition]] for task details.

---

**Notebook**: [bilstm_pos_lab.py](notebooks/bilstm_pos_lab.py)

#sequence #deep-learning #bilstm
