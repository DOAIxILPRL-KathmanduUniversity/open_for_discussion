# Monitoring & Data Drift in NLP

> [!IMPORTANT] Gist
> NLP models are not static. Once deployed, their performance degrades as the world (and language) changes. Monitoring is the process of detecting "drift" and ensuring the model remains reliable.

## 1. Types of Drift
- **Concept Drift**: The relationship between input and output changes.
    - *Example*: Before 2020, "corona" mostly meant beer or sun. After 2020, the primary sentiment and context shifted to a virus.
- **Data Drift (Feature Drift)**: The distribution of the input data changes.
    - *Example*: A toxicity model trained on formal news comments is deployed on a gaming chat (slang, abbreviations).
- **Label Drift**: The distribution of the labels in the real world changes.

## 2. Detecting Drift
- **Statistical Tests**: Using Kolmogorov-Smirnov (KS) or Population Stability Index (PSI) to compare the distribution of word frequencies or embedding clusters between training and production.
- **Proxy Metrics**: If ground truth labels are unavailable in real-time, monitor model **Confidence** or **Embedding Variance**.
- **Outlier Detection**: Identifying inputs that fall into "empty" regions of the training vector space.

## 3. NLP Observability
- **Semantic Monitoring**: Visualizing production embeddings in 2D (using UMAP or t-SNE) to spot new clusters of topics or languages.
- **Topological Data Analysis (TDA)**: Detecting shifts in the "shape" of the data manifold.
- **Feedback Loops**: Sampling low-confidence predictions for human re-annotation to create a "golden set" for continuous evaluation.

## 4. Retraining Strategies
- **Passive Retraining**: Retraining on a fixed schedule (e.g., every month).
- **Active Retraining**: Triggering a new training run only when drift metrics cross a specific threshold.
- **Online Learning**: Updating the model incrementally as new data arrives (rare for large LLMs due to stability issues).

---

#deployment #mlops #observability #drift #lifecycle
