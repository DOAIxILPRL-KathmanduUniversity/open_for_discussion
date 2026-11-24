# Efficient Inference & Pruning

> [!IMPORTANT] Gist
> Deploying large models requires reducing computational overhead. Modern techniques focus on speculative decoding, evolutionary pruning, and architecture distillation (2025/2026 Conference Insights).

## 1. Speculative Decoding
- **Multi-candidate Speculative Decoding**: Accelerating inference by generating multiple draft candidates in parallel using a smaller model, which are then verified by the target large model.
- **Reward-Guided Selection**: Choosing the best speculative candidates based on probability and alignment.

## 2. Model Compression & Pruning
- **EvoP (Evolutionary Pruning)**: Using evolutionary algorithms to identify and remove redundant parameters or layers in LLMs without sacrificing significant accuracy.
- **HGNN2KAN**: Distilling complex Hypergraph Neural Networks into **KAN (Kolmogorov-Arnold Networks)** for high-efficiency inference.

## 3. Fundamental Inference Optimization
- **Batching & Padding**: Processing multiple sequences simultaneously requires padding shorter sequences to match the length of the longest in the batch.
- **Masking**: To ensure the model ignores padding tokens during attention and loss calculation, a **mask** is used to zero out the influence of these non-informative tokens (Sato, 2021).
- **Heterogeneity-Based Tuning**: Adjusting fine-tuning strategies based on the inherent diversity and complexity of the training data.

---

#real-world #inference #speculative-decoding #pruning #model-compression #kan
