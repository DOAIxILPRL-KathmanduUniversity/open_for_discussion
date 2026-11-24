# Collocations & PMI

> [!IMPORTANT] Gist
> Individual words often combine to form multi-word expressions (collocations) where the meaning is more than the sum of its parts. **Pointwise Mutual Information (PMI)** is a statistical measure used to identify these phrases by comparing the probability of words occurring together versus their individual probabilities (Church & Hanks, 1990).

## 1. Probabilistic Foundations (Hovy, 2020)
PMI is built on basic probability theory:
- **Joint Probability $P(w_1, w_2)$**: The likelihood of both words occurring together.
- **Conditional Probability $P(w_1 | w_2)$**: The likelihood of $w_1$ occurring given that $w_2$ has already occurred.
- **Independence**: If $w_1$ and $w_2$ are independent, $P(w_1, w_2) = P(w_1)P(w_2)$, and $\text{PMI} = \log(1) = 0$.

## 2. Pointwise Mutual Information (PMI)
PMI measures the strength of association between two words $w_1$ and $w_2$.
$$\text{PMI}(w_1, w_2) = \log \frac{P(w_1, w_2)}{P(w_1)P(w_2)}$$

- **Intuition**: If two words appear together more often than expected by chance, the PMI is positive.
- **Example**: "Los Angeles" has a much higher PMI than "Los" or "Angeles" individually.

## 2. Normalized PMI (NPMI)
To keep values between -1 and 1:
- **1**: Words always occur together.
- **0**: Words occur independently.
- **-1**: Words never occur together.

## 3. Applications in Content Representation
- Identifying multi-word features (e.g., "hurricane katrina," "lake erie") before vectorization.
- Reducing noise in bag-of-words models by treating collocations as single tokens.

---

#representation #collocations #pmi #content
