# Linear Algebra & Tensors: The Engine of Deep Learning

> [!IMPORTANT] Gist
> Linear algebra is the language of deep learning. It allows us to represent data, weights, and operations as structured multi-dimensional arrays (tensors), enabling massive parallelism on hardware like GPUs (Ghayoumi, 2026).

## 1. Tensors: Generalizing Data Structures
A tensor is a multi-dimensional array of numerical values.
- **Scalar (Rank 0)**: A single number (e.g., $c = 5$).
- **Vector (Rank 1)**: An array of numbers (e.g., $[1, 2, 3]$). In NLP, word embeddings are vectors.
- **Matrix (Rank 2)**: A 2D array. Weight matrices in neural networks.
- **Higher-Rank Tensors**: 
    - **Rank 3**: Batch of sequences (Batch Size, Sequence Length, Embedding Dim).
    - **Rank 4**: Batch of images (Batch Size, Height, Width, Channels).

## 2. Core Matrix Operations
- **Matrix Multiplication**: The primary operation in fully connected layers ($z = Wx + b$).
- **Hadamard Product**: Element-wise multiplication ($\odot$), common in GRU/LSTM gating mechanisms.
- **Transpose**: Swapping rows and columns ($A^\top$), used in Attention mechanisms ($QK^\top$).
- **Inverse**: Finding $A^{-1}$ such that $AA^{-1} = I$. Used in some closed-form solutions (e.g., Normal Equation in Linear Regression).

## 3. Matrix Decompositions (Factorization)
Decomposing a complex matrix into simpler parts:
- **LU Decomposition**: Factors $A$ into Lower ($L$) and Upper ($U$) triangular matrices. Efficient for solving systems of linear equations.
- **QR Decomposition**: Factors $A$ into an Orthogonal ($Q$) and Upper triangular ($R$) matrix. Used in eigenvalue algorithms.
- **Singular Value Decomposition (SVD)**: $A = U\Sigma V^\top$.
    - **Application in NLP**: Latent Semantic Analysis (LSA) for dimensionality reduction and noise filtering.
    - **Model Compression**: Approximating weights with low-rank matrices to reduce parameters.

## 4. Eigenvalues and Eigenvectors
For a square matrix $A$, if $Av = \lambda v$, then $v$ is an **eigenvector** and $\lambda$ is an **eigenvalue**.
- **Principal Component Analysis (PCA)**: Uses the eigenvectors of the covariance matrix to project data into a lower-dimensional space while preserving variance.
- **Hessian Analysis**: The eigenvalues of the Hessian matrix (second-order partial derivatives) indicate the **curvature** of the loss landscape, influencing optimization speed.

## 5. Linear Transformations
A linear transformation preserves vector addition and scalar multiplication. In NNs, each layer is a linear transformation followed by a non-linear activation function.
- **Rotation, Scaling, Shearing**: Fundamental geometric operations represented by matrices.
- **Embeddings**: A linear map from discrete token IDs to continuous vector spaces.

---

#foundations #linear-algebra #tensors #matrices #svd #pca
