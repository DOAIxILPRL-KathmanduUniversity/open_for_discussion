# Bayesian Analysis in NLP

> [!IMPORTANT] Gist
> Bayesian NLP moved the field beyond frequentist statistics in the late 1990s, allowing for the incorporation of prior knowledge and enrichment of unsupervised learning (Cohen, 2019).

## 1. Core Bayesian Machinery
- **Generative Modeling**: Defining a story of how the data was produced, including hidden variables.
- **Priors**:
    - **Conjugate Priors**: Priors that, when combined with a specific likelihood, result in a posterior of the same family (e.g., Dirichlet-Multinomial).
    - **Non-Informative Priors**: Jeffreys prior, uniform priors for minimal bias.
- **Inference Techniques**:
    - **Markov Chain Monte Carlo (MCMC)**: Gibbs Sampling (Collapsed and Parallel), Metropolis-Hastings.
    - **Variational Inference (VI)**: Approximating a complex posterior with a simpler distribution (Mean-Field approximation).

## 2. Nonparametric Models
Models that grow in complexity as more data is observed:
- **Dirichlet Process (DP)**:
    - **Stick-Breaking View**: Dividing a "stick" of probability mass into infinitely many pieces.
    - **Chinese Restaurant Process (CRP)**: A metaphor for clustering where customers (data points) sit at tables (clusters).
- **Pitman-Yor Process**: A generalization of the DP that exhibits power-law behavior, essential for modeling the "long tail" of natural language.
- **Hierarchical Dirichlet Process (HDP)**: Shared clusters across multiple groups (e.g., topics across documents in LDA).

## 3. Bayesian Grammars
- **Bayesian HMMs**: Hidden Markov Models with Dirichlet priors on transitions and emissions.
- **Bayesian PCFGs**: Probabilistic Context-Free Grammars where production rules are treated as random variables.
- **Adaptor Grammars**: A framework that allows for "caching" subtrees, enabling the model to learn units of varying complexity (e.g., words, phrases).

## 4. Deep Latent Variable Models
- **Generative Neural Models**: Combining deep networks with latent variables $Z$. The network serves as a strong function approximator to infer $Z$ from data $X$.
- **Variational Autoencoders (VAE)**: Models that use an encoder to approximate the posterior $q(Z|X)$ and a decoder to reconstruct $X$ from $Z$. They maximize the **ELBO (Evidence Lower Bound)** during training.
- **Neural Topic Models**: Extensions of LDA where the distribution of words given a topic is parameterized by a neural network.
- **Amortized Variational Inference (Amortised VI)**: Instead of optimizing variational parameters for each instance, Amortised VI uses a neural network to predict the parameters of the variational distribution directly, enabling faster inference and scaling to massive datasets (Zhang et al., 2021).
- **Gradient-Based EM**: A generalized EM algorithm where the M-step involves optimizing the joint log-likelihood using iterative numerical methods (SGD) instead of closed-form solutions.

---

#bayesian #statistics #mcmc #variational-inference #nonparametric #lda
