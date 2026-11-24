"""
🧠 MLP FROM SCRATCH (NUMPY)
---------------------------
A pedagogical implementation of a 3-layer neural network.
Targets: Iris Dataset classification (4 features -> 3 classes).

Logic: Forward Pass -> Cross Entropy -> Backpropagation -> Gradient Descent
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# --- HYPERPARAMETERS ---
INPUT_SIZE    = 4
HIDDEN1_SIZE  = 64
HIDDEN2_SIZE  = 32
OUTPUT_SIZE   = 3
LEARNING_RATE = 0.01
EPOCHS        = 1000

class MLP:
    def __init__(self):
        # He Initialization
        self.W1 = np.random.randn(INPUT_SIZE, HIDDEN1_SIZE) * np.sqrt(2 / INPUT_SIZE)
        self.b1 = np.zeros((1, HIDDEN1_SIZE))
        self.W2 = np.random.randn(HIDDEN1_SIZE, HIDDEN2_SIZE) * np.sqrt(2 / HIDDEN1_SIZE)
        self.b2 = np.zeros((1, HIDDEN2_SIZE))
        self.W3 = np.random.randn(HIDDEN2_SIZE, OUTPUT_SIZE) * np.sqrt(2 / HIDDEN2_SIZE)
        self.b3 = np.zeros((1, OUTPUT_SIZE))
        
        self.cache = {}

    def relu(self, Z):
        return np.maximum(0, Z)

    def relu_derivative(self, Z):
        return (Z > 0).astype(float)

    def softmax(self, Z):
        exp_Z = np.exp(Z - np.max(Z, axis=1, keepdims=True))
        return exp_Z / np.sum(exp_Z, axis=1, keepdims=True)

    def forward(self, X):
        self.cache['Z1'] = X @ self.W1 + self.b1
        self.cache['A1'] = self.relu(self.cache['Z1'])
        
        self.cache['Z2'] = self.cache['A1'] @ self.W2 + self.b2
        self.cache['A2'] = self.relu(self.cache['Z2'])
        
        self.cache['Z3'] = self.cache['A2'] @ self.W3 + self.b3
        self.cache['A3'] = self.softmax(self.cache['Z3'])
        return self.cache['A3']

    def compute_loss(self, y_true):
        n = y_true.shape[0]
        y_pred = np.clip(self.cache['A3'], 1e-9, 1 - 1e-9)
        return -np.sum(y_true * np.log(y_pred)) / n

    def backward(self, X, y_true):
        n = y_true.shape[0]
        
        # Output Layer
        dZ3 = (self.cache['A3'] - y_true) / n
        dW3 = self.cache['A2'].T @ dZ3
        db3 = np.sum(dZ3, axis=0, keepdims=True)
        
        # Hidden Layer 2
        dA2 = dZ3 @ self.W3.T
        dZ2 = dA2 * self.relu_derivative(self.cache['Z2'])
        dW2 = self.cache['A1'].T @ dZ2
        db2 = np.sum(dZ2, axis=0, keepdims=True)
        
        # Hidden Layer 1
        dA1 = dZ2 @ self.W2.T
        dZ1 = dA1 * self.relu_derivative(self.cache['Z1'])
        dW1 = X.T @ dZ1
        db1 = np.sum(dZ1, axis=0, keepdims=True)
        
        return dW1, db1, dW2, db2, dW3, db3

    def update(self, grads):
        dW1, db1, dW2, db2, dW3, db3 = grads
        self.W1 -= LEARNING_RATE * dW1
        self.b1 -= LEARNING_RATE * db1
        self.W2 -= LEARNING_RATE * dW2
        self.b2 -= LEARNING_RATE * db2
        self.W3 -= LEARNING_RATE * dW3
        self.b3 -= LEARNING_RATE * db3

def run_training():
    # 1. Data Prep
    iris = load_iris()
    X = (iris.data - iris.data.min(axis=0)) / (iris.data.max(axis=0) - iris.data.min(axis=0))
    y = OneHotEncoder(sparse_output=False).fit_transform(iris.target.reshape(-1, 1))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 2. Model Init
    model = MLP()
    loss_history = []

    # 3. Training Loop
    for epoch in range(EPOCHS):
        model.forward(X_train)
        loss = model.compute_loss(y_train)
        loss_history.append(loss)
        
        grads = model.backward(X_train, y_train)
        model.update(grads)

        if epoch % 100 == 0:
            print(f"Epoch {epoch:4d} | Loss: {loss:.4f}")

    return model, loss_history

if __name__ == "__main__":
    model, history = run_training()
    plt.plot(history)
    plt.title("MLP Training Loss")
    plt.show()
