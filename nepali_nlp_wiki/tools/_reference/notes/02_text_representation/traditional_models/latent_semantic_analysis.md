# Latent Semantic Analysis (LSA)

> [!IMPORTANT] Gist
> LSA is a technique in NLP for discovering latent (hidden) topics and relationships between terms and documents by transforming them into a lower-dimensional "Latent Semantic Space" (Deerwester et al., 1990).

## How It Works
1. **Vector Space Model (VSM)**: Represent text as vectors where dimensions correspond to term frequency (often weighted by **TF-IDF**).
2. **Similarity Measure**: Use **Cosine Similarity** to determine document relatedness ($1.0 = \text{identical}$, $0.0 = \text{orthogonal/no overlap}$).
3. **Dimensionality Reduction**: Apply **Singular Value Decomposition (SVD)** or **Principal Component Analysis (PCA)** to reduce the high-dimensional matrix, filtering out noise and capturing underlying concepts.

## Noise Reduction Techniques
In emotion detection and topic modeling, LSA is often paired with alternative dimensionality reduction methods (Cavicchio, 2025):
- **NMF (Non-negative Matrix Factorization)**: Effective for noise reduction; often outperforms LSA in categorical emotion classification.
- **LDA (Latent Dirichlet Allocation)**: A probabilistic generative model that assumes documents are mixtures of topics and topics are mixtures of words. It is the most popular unsupervised algorithm for topic discovery.
- **PCA (Principal Component Analysis)**: Extracts orthogonal dimensions.

## Topic Modeling vs. Text Classification
| Feature | Topic Modeling | Text Classification |
| :--- | :--- | :--- |
| **Learning** | Unsupervised | Supervised |
| **Output** | Discovering latent topics | Assigning predefined categories |
| **Labels** | Not required | Required (Gold Standard) |
| **Goal** | Exploratory discovery | Predictive labeling |

---

#representation #unsupervised #lsa #pca #nmf
