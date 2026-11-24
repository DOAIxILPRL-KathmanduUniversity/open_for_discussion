# Masterclass: Convolutional Neural Network (CNN) From Scratch

> [!IMPORTANT] Gist
> Implementing a CNN from scratch reveals the "spatial intelligence" of the model. It requires manual implementation of 2D Convolution kernels, Max Pooling with index routing, and gradient unflattening.

## 1. CNN Architecture Breakdown

The implemented network follows a classic LeNet-style architecture for MNIST digit classification:

1.  **Input**: 28×28×1 (Grayscale images).
2.  **Conv Layer 1**: 8 filters (3×3), ReLU → (26×26×8).
3.  **MaxPool 1**: 2×2 window → (13×13×8).
4.  **Conv Layer 2**: 16 filters (3×3), ReLU → (11×11×16).
5.  **MaxPool 2**: 2×2 window → (5×5×16).
6.  **Flatten**: Unroll spatial features into a 400-dim vector.
7.  **Dense Layers**: 128 neurons (ReLU) → 10 neurons (Softmax).

## 2. Core Operations: The Math

### A. 2D Convolution (Forward)
For each filter $k$, the output at $(i, j)$ is the sum of element-wise multiplication of the filter and the local image patch:
$$O_{i,j,k} = \sum_{m,n,c} X_{i+m, j+n, c} \cdot F_{m,n,c,k} + b_k$$
This operation acts as a **feature detector** (edges, corners, textures).

### B. Max Pooling (Forward & Backward)
*   **Forward**: Takes the maximum value in a $2 \times 2$ window.
*   **Backward**: Only the "winning" pixel (the max) receives the gradient. We must cache the **indices** of these max values to route the error signal correctly during backpropagation.

### C. The Backward Pass (Conv Layer)
Backpropagating through a convolution is itself a convolution (often called a "transposed" or "dilated" convolution logic). We calculate:
*   $dF$: The gradient of the filters (how the filter weights should change).
*   $dX$: The gradient of the input (to pass back to previous layers).

## 3. Comparison: Scratch vs. TensorFlow

| Feature | Scratch (NumPy) | TensorFlow (Keras) |
| :--- | :--- | :--- |
| **Speed** | Very slow ($O(N^4)$ nested loops) | High-speed C++/CUDA kernels |
| **Learning Rate** | Manual tuning required | Adaptive (Adam Optimizer) |
| **Accuracy** | ~90-95% (on subset) | ~98-99% (on full dataset) |
| **Purpose** | Pedagogical / Mechanics | Production / Scaling |

---

**Notebook**: [cnn_from_scratch.py](notebooks/cnn_from_scratch.py) (NumPy Implementation vs TF)

#cnn #computer-vision #backpropagation #scratch-implementation #numpy #mnist
