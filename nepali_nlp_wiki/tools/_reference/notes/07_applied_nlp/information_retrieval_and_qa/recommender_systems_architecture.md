# Deep Learning Recommender Systems

> [!IMPORTANT] Gist
> Modern recommender systems have evolved from simple collaborative filtering to complex deep learning architectures that handle multi-modal features, sequential behaviors, and massive scale. The integration of LLMs as feature encoders and scoring functions represents the "Deep Learning 2.0" era (Wang et al., 2025).

## 1. The Evolution of Recommendation Models
1.  **Collaborative Filtering (CF)**: Finding similar users (UserCF) or similar items (ItemCF).
2.  **Matrix Factorization (MF)**: Decomposing the user-item interaction matrix into latent vectors.
3.  **Feature Interaction Models**:
    *   **Factorization Machines (FM)**: Capturing second-order feature interactions.
    *   **GBDT+LR**: Using decision trees to generate features for a logistic regression model.
4.  **Deep Learning Era**:
    *   **Wide & Deep**: Combining a linear "wide" part (memorization) with a deep "neural" part (generalization).
    *   **DeepFM**: Integrating FM and Deep layers for automatic high-order feature cross.
    *   **Attention-Based (DIN)**: Using attention to weight historical user behaviors based on the target item.
    *   **Sequential (DIEN)**: Modeling the evolution of user interest over time using GRUs.

## 2. Embedding Technology
Embeddings are the foundation of deep recommender systems:
- **Item2vec**: Treating sequences of item interactions as "sentences" to learn item vectors.
- **Graph Embeddings**: Using Random Walks (DeepWalk) or BFS/DFS (Node2vec) on user-item graphs to capture structural information.
- **EGES**: Incorporating side information (e.g., brand, category) into graph embeddings to solve the "Cold Start" problem.

## 3. LLMs in Recommendation
LLMs are transforming recommendation pipelines in four ways:
- **Feature Engineering**: Transforming raw text descriptions into structured features.
- **Feature Encoder**: Using pre-trained Transformers to generate high-quality text/item embeddings.
- **Scoring/Ranking**: Using the LLM directly as a zero-shot or fine-tuned ranking function.
- **Pipeline Controller**: Using the LLM as an agent to orchestrate different recommendation modules.

## 4. Engineering Architecture
- **Retrieval Layer (Recall)**: Fast filtering of millions of items into hundreds using **Locality Sensitive Hashing (LSH)** or Vector Databases.
- **Ranking Layer**: Precisely scoring the filtered items using deep models.
- **Real-Time Performance**: Using **Kappa/Lambda architectures** to process stream data and update user profiles in milliseconds.

---

#applied #recommendation #embeddings #llm #ranking #graph
