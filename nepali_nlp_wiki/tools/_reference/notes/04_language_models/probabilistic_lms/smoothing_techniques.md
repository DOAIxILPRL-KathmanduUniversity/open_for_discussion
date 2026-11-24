# Smoothing Techniques

> [!IMPORTANT] Gist
> In language modeling, "Zero Probability" is a fatal error. Smoothing redistributes probability mass from seen words to unseen words (the "long tail") to ensure the model remains robust to OOV tokens.

## 1. The Sparsity Problem
In an N-gram model, if a specific sequence (e.g., "the quick purple") never appeared in the training set, $P(\text{purple} | \text{the quick}) = 0$. This causes the entire sentence probability to crash to zero.

## 2. Basic Smoothing
- **Laplace Smoothing (Add-One)**: Add 1 to all counts. Simple but over-estimates the probability of rare events.
- **Lidstone Smoothing (Add-$\alpha$)**: Add a small fraction $\alpha$ (e.g., 0.1).

## 3. Backoff and Interpolation
- **Backoff (Katz)**: If a trigram count is zero, look at the bigram. If bigram is zero, look at the unigram.
- **Interpolation (Jelinek-Mercer)**: Always combine information from all levels:
    - $P_{interp} = \lambda_1 P(w_3|w_1w_2) + \lambda_2 P(w_3|w_2) + \lambda_3 P(w_3)$

## 4. Kneser-Ney Smoothing (The Standard)
The most sophisticated approach for N-grams. It considers the **diversity** of contexts.
- **Observation**: The word "Francisco" is common but only follows "San." In a general context, it shouldn't have a high unigram probability.
- **Continuation Probability**: $P_{KN}$ favors words that appear in many different contexts over words that appear frequently but only in one specific context.

## 5. Neural Smoothing
Modern neural models don't use explicit count-based smoothing. Instead, they use:
- **Dropout**: Randomly silencing neurons to prevent overfitting to specific sequences.
- **Label Smoothing**: Softening the target labels (e.g., target 0.9 for the correct word and 0.01 for others) to prevent the model from becoming too overconfident.

---

#language-models #smoothing #probability #kneser-ney #sparsity
