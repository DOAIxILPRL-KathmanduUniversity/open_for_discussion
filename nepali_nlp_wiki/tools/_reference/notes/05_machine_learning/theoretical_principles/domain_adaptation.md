# Domain Adaptation & Learning under Bias

> [!IMPORTANT] Gist
> Domain Adaptation (also known as Transfer Learning) addresses the problem of **Sampling Bias**, where a model trained on a "Source" domain (e.g., News) is applied to a "Target" domain (e.g., Twitter) with a different distribution (Søgaard, 2013).

## 1. Types of Bias in NLP
- **Covariate Shift**: The distribution of features $P(X)$ changes between source and target, but the relationship $P(Y|X)$ remains the same.
- **Concept Drift**: The relationship between features and labels $P(Y|X)$ changes (e.g., the word "apple" means a fruit in a general corpus but a company in a business corpus).

## 2. Strategies for Adaptation
### A. Transferring Data (Importance Weighting)
- **Reweighting**: Giving more weight to source instances that are "similar" to the target domain. This can be estimated by training a domain classifier to predict if an instance belongs to the source or target.

### B. Transferring Features
- **Structural Correspondence Learning (SCL)**: Identifying "pivot features" (features that are frequent and behave similarly in both domains) and learning correlations between non-pivot features and pivots.
- **Changing Representation**: Learning a shared low-dimensional space (e.g., via Autoencoders or adversarial networks) where source and target distributions are indistinguishable.

### C. Transferring Parameters
- **Fine-tuning**: Taking a model pre-trained on a large source corpus and performing additional training on a small amount of labeled target data.

## 3. Adversarial Learning
- **Domain Adversarial Neural Networks (DANN)**: Adding a "domain classifier" branch to a neural network. The main model is trained to minimize label loss while *maximizing* the domain classifier's loss (via a gradient reversal layer), forcing the model to learn features that are "domain-invariant."

## 4. Evaluating under Bias
- **Cross-Domain Evaluation**: Evaluating a model on multiple distinct corpora (e.g., News, Weblogs, Emails) rather than just a single test set.
- **Significance Across Corpora**: Using meta-analysis to determine if an improvement is robust across different data distributions.

---

#ml #domain-adaptation #transfer-learning #bias #adversarial #scl
