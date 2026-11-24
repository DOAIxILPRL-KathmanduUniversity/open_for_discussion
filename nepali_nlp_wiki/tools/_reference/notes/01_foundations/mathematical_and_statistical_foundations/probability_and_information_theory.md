# Probability & Information Theory: Quantifying Uncertainty

> [!IMPORTANT] Gist
> Deep learning is inherently probabilistic. We deal with noise in data, random initialization, and models that output likelihoods. Information theory provides the tools to measure "surprise," "entropy," and the efficiency of data representation (Ghayoumi, 2026).

## 1. Probability Theory
- **Conditional Probability**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$. Essential for Language Models (predicting $w_t$ given $w_{t-1}$).
- **Bayes' Theorem**: $P(\theta|D) = \frac{P(D|\theta)P(\theta)}{P(D)}$. The foundation of Bayesian inference, allowing us to update beliefs as new data arrives.
- **Distributions**:
    - **Normal (Gaussian)**: Common assumption for weight initialization and noise.
    - **Multinomial**: Used for classification tasks (Softmax outputs).
    - **Bernoulli**: Used for binary classification and Dropout (turning neurons on/off).

## 2. Information Theory
Quantifying how much information is contained in a signal.
- **Self-Information**: $I(x) = -\log P(x)$. Rare events have higher information/surprise.
- **Entropy ($H$)**: The average amount of information in a distribution. $H(P) = -\sum P(x) \log P(x)$.
- **Cross-Entropy ($H(P, Q)$)**: Measures the difference between the true distribution $P$ and predicted distribution $Q$.
    - **Standard Loss Function**: Cross-entropy is the standard loss for classification and language modeling.
- **KL Divergence ($D_{KL}$)**: Measures how one probability distribution diverges from a second, expected distribution. Used in Variational Autoencoders (VAEs).
- **Mutual Information**: Measures how much information is shared between two variables. Useful for feature selection and understanding representation learning.

## 3. Uncertainty in Deep Learning
- **Aleatoric Uncertainty**: Uncertainty in the data (noise).
- **Epistemic Uncertainty**: Uncertainty in the model parameters (lack of data).
- **Bayesian Neural Networks**: Instead of fixed weights, weights are represented as probability distributions.

---

#foundations #probability #information-theory #entropy #cross-entropy #bayesian
