# Information Theory & Deep Learning

> [!IMPORTANT] Gist
> Information theory provides the mathematical tools to analyze how deep neural networks process information. The core principle is the **Information Bottleneck**, which optimizes the trade-off between compressing the input and preserving the information relevant for the target task (Yang et al., 2025).

## 1. The Information Bottleneck (IB) Principle
The IB principle formulates representation learning as a constrained optimization problem:
$$\min_{Z} I(X; Z) - \beta I(Y; Z)$$
- **$I(X; Z)$**: Compression. Minimize the mutual information between the input $X$ and the representation $Z$ (removing noise).
- **$I(Y; Z)$**: Prediction. Maximize the mutual information between the representation $Z$ and the target $Y$ (preserving relevant signals).
- **$\beta$**: A trade-off parameter.

## 2. Self-Supervised Learning (SSL) & InfoMax
SSL leverages information-theoretic objectives to learn without labels:
- **InfoMax Principle**: Maximizing the mutual information between different "views" of the same data (e.g., two crops of an image).
- **Siamese Networks**: Joint embedding architectures that use contrastive losses to implement InfoMax.
- **MINE (Mutual Information Neural Estimator)**: A neural network-based estimator for mutual information, allowing for the direct optimization of information-theoretic bounds in high-dimensional spaces.

## 3. Self-Supervised Information-Theoretic Framework
A unified framework for SSL involves multiple encoders and decoders (Shwartz-Ziv & LeCun, 2024):
- **Encoder $E$**: Mapping input $X$ to representation $Z$.
- **Predictive Encoder $E'$**: Learning to predict $Z$ from a different view $X'$.
- **Compression vs. Invariance**: The trade-off between making $Z$ compact and making it invariant to data augmentations.

## 4. Applications in Deep Learning
- **Generalization Bounds**: Using mutual information to provide tighter theoretical bounds on a model's ability to generalize to unseen data.
- **Generative Models**: Using information-theoretic losses (e.g., in GANs) to ensure the generated samples cover the full distribution of the data.
- **Feature Selection**: Identifying which input features contribute most to the mutual information with the target.

---

#ml #information-theory #bottleneck #ssl #infomax #representation
