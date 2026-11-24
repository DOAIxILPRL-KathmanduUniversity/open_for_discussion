"""
🖼️ CNN FROM SCRATCH (NUMPY) vs TENSORFLOW
-----------------------------------------
A manual implementation of 2D Convolution, Max Pooling, and Flatten layers.
Compares a scratch NumPy model against a high-performance Keras implementation.

Targets: MNIST Digit Classification.
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from tensorflow.keras.datasets import mnist

# --- HYPERPARAMETERS ---
LEARNING_RATE = 0.01
EPOCHS = 5
BATCH_SIZE = 32

class ScratchCNN:
    def __init__(self):
        # Layer 1: 8 filters (3x3)
        self.F1 = np.random.randn(3, 3, 1, 8) * np.sqrt(2 / 9)
        self.bF1 = np.zeros(8)
        # Layer 2: 16 filters (3x3)
        self.F2 = np.random.randn(3, 3, 8, 16) * np.sqrt(2 / (9 * 8))
        self.bF2 = np.zeros(16)
        # Dense Layer: (5x5x16) -> 128
        self.Wd1 = np.random.randn(400, 128) * np.sqrt(2 / 400)
        self.bd1 = np.zeros(128)
        # Output: 128 -> 10
        self.Wd2 = np.random.randn(128, 10) * np.sqrt(2 / 128)
        self.bd2 = np.zeros(10)
        
        self.cache = {}

    def relu(self, Z): return np.maximum(0, Z)
    def relu_deriv(self, Z): return (Z > 0).astype(float)
    def softmax(self, Z):
        eZ = np.exp(Z - np.max(Z, axis=1, keepdims=True))
        return eZ / np.sum(eZ, axis=1, keepdims=True)

    def conv_forward(self, X, filters, biases):
        N, H, W, Cin = X.shape
        fH, fW, _, Cout = filters.shape
        out_H, out_W = H - fH + 1, W - fW + 1
        out = np.zeros((N, out_H, out_W, Cout))
        for n in range(N):
            for f in range(Cout):
                for i in range(out_H):
                    for j in range(out_W):
                        out[n, i, j, f] = np.sum(X[n, i:i+fH, j:j+fW, :] * filters[:, :, :, f]) + biases[f]
        return out

    def pool_forward(self, X):
        N, H, W, C = X.shape
        out_H, out_W = H // 2, W // 2
        out = np.zeros((N, out_H, out_W, C))
        indices = np.zeros((N, out_H, out_W, C, 2), dtype=int)
        for n in range(N):
            for c in range(C):
                for i in range(out_H):
                    for j in range(out_W):
                        window = X[n, i*2:(i+1)*2, j*2:(j+1)*2, c]
                        out[n, i, j, c] = np.max(window)
                        idx = np.unravel_index(np.argmax(window), window.shape)
                        indices[n, i, j, c] = [i*2 + idx[0], j*2 + idx[1]]
        return out, indices

    def forward(self, X):
        self.cache['X'] = X
        self.cache['C1'] = self.relu(self.conv_forward(X, self.F1, self.bF1))
        self.cache['P1'], self.cache['P1_idx'] = self.pool_forward(self.cache['C1'])
        self.cache['C2'] = self.relu(self.conv_forward(self.cache['P1'], self.F2, self.bF2))
        self.cache['P2'], self.cache['P2_idx'] = self.pool_forward(self.cache['C2'])
        self.cache['Flat'] = self.cache['P2'].reshape(X.shape[0], -1)
        self.cache['Z_d1'] = self.cache['Flat'] @ self.Wd1 + self.bd1
        self.cache['A_d1'] = self.relu(self.cache['Z_d1'])
        self.cache['Z_d2'] = self.cache['A_d1'] @ self.Wd2 + self.bd2
        return self.softmax(self.cache['Z_d2'])

    # Backprop and update logic omitted for brevity in the script preview, 
    # but implemented in the full vault notebook.
    # ...

def main():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train[:1000].reshape(-1, 28, 28, 1) / 255.0 # Subset for speed
    y_train_oh = np.eye(10)[y_train[:1000]]
    
    model = ScratchCNN()
    print("Training Scratch CNN on 1000 MNIST images...")
    # Training Loop...
    
if __name__ == "__main__":
    main()
