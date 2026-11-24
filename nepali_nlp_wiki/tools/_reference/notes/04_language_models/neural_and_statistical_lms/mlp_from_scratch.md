# Masterclass: Multi-Layer Perceptron (MLP) From Scratch

> [!IMPORTANT] Gist
> Understanding the "Mechanics of Learning" requires implementing the forward and backward pass manually. This module demonstrates a 3-layer MLP using only `numpy`.

## 1. The Mathematical Blueprint

### Forward Pass (Inference)
For each layer $l$:
1.  **Linear Step**: $Z^{[l]} = A^{[l-1]}W^{[l]} + b^{[l]}$
2.  **Activation (ReLU)**: $A^{[l]} = \max(0, Z^{[l]})$
3.  **Output (Softmax)**: $\hat{y} = \frac{e^{Z^{[L]}}}{\sum e^{Z^{[L]}}}$

### Backward Pass (Learning)
Using the Chain Rule to calculate gradients ($\frac{\partial L}{\partial W}$):
1.  **Output Error**: $dZ^{[L]} = \hat{y} - y_{true}$
2.  **Hidden Error**: $dZ^{[l]} = (dZ^{[l+1]}W^{[l+1]T}) \odot \sigma'(Z^{[l]})$
3.  **Weight Gradient**: $dW^{[l]} = A^{[l-1]T} dZ^{[l]}$
4.  **Bias Gradient**: $db^{[l]} = \sum dZ^{[l]}$

## 2. Implementation Logic

| Phase | Description |
| :--- | :--- |
| **He Initialization** | Scales weights by $\sqrt{2/n_{in}}$ to prevent vanishing gradients in ReLU networks. |
| **Numerical Stability** | Subtracting $\max(Z)$ in Softmax to prevent `exp(Z)` from exploding. |
| **Gradient Clipping** | Implicitly handled by small learning rates, but critical for deeper networks. |
| **Vectorization** | Using Matrix Multiplication (`@`) to process an entire batch of data simultaneously. |

## 3. Training Loop Sequence

1.  **Forward**: Compute predictions and cache intermediate activations ($Z, A$).
2.  **Loss**: Compute Cross-Entropy between predictions and ground truth.
3.  **Backward**: Propagate the error signal from the output layer back to the input.
4.  **Update**: Adjust weights in the direction of the negative gradient: $W = W - \eta dW$.

---

**Notebook**: [mlp_from_scratch.py](notebooks/mlp_from_scratch.py) (Full NumPy Implementation)

#foundations #neural-networks #backpropagation #math #numpy
