# Logistic Regression

> [!IMPORTANT] Gist
> Logistic Regression is a fundamental machine learning algorithm for binary classification. It maps input features to a probability between 0 and 1 using the **Sigmoid function**.

## 1. The Sigmoid Function
Maps any real-valued number into the range $[0, 1]$.
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

## 2. Classification Logic
For an input $x$, we compute a weighted sum $z = w \cdot x + b$.
- $P(y=1|x) = \sigma(w \cdot x + b)$
- If $P > 0.5$, classify as 1.

## 3. Learning: Cross-Entropy Loss
Measures the performance of a classification model whose output is a probability.
$$L_{CE}(\hat{y}, y) = -[y \log \hat{y} + (1-y) \log(1-\hat{y})]$$

## 4. Optimization: Gradient Descent
An iterative optimization algorithm used to minimize the loss function by updating weights $w$ in the direction of the steepest descent (negative gradient).

---

#foundations #ml #classification #math
