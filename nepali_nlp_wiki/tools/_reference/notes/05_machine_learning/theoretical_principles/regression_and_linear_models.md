# Regression & The Linear Model Foundation

> [!IMPORTANT] Gist
> The linear model is the "tie that binds" all data science, from simple t-tests to complex neural networks. It posits that a target can be explained as a weighted sum (linear combination) of features plus an error term (Clark & Berry, 2026).

## 1. The Core Equation
The linear model is expressed mathematically as:
$$y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \dots + \beta_nx_n + \epsilon$$
- **$\beta_0$ (Intercept)**: The baseline value when all features are zero.
- **$\beta_n$ (Coefficients/Weights)**: The direction and magnitude of the relationship for each feature.
- **$\epsilon$ (Error/Residual)**: The part of the target the model cannot explain.

### Matrix Representation
For efficiency, models are often represented in matrix form:
$$y = X\beta + \epsilon$$
Where $X$ is the design matrix (including a column of ones for the intercept), $\beta$ is the vector of weights, and $y$ is the target vector.

## 2. Prediction vs. Explanation
Models serve two primary (and sometimes conflicting) goals:
- **Prediction ($\hat{y}$)**: Focusing on the model's output for new data. Utility is measured by error metrics (RMSE, MAE).
- **Explanation (Inference)**: Focusing on the coefficients ($\beta$). Utility is measured by the interpretation of feature-target relationships and statistical significance (p-values, Confidence Intervals).

## 3. Estimating Uncertainty
A point prediction ($\hat{y}$) is insufficient for high-stakes decisions. We must quantify uncertainty:
- **Confidence Intervals (CI)**: Range for the *mean* prediction (how certain are we about the average?).
- **Prediction Intervals (PI)**: Range for an *individual* observation. These are always wider as they account for the variance of the mean plus the inherent noise ($\epsilon$).

## 4. Transition to Complexity
The linear model serves as the building block for advanced architectures:
- **GLMs**: Adding a **Link Function** (e.g., Logit, Log) allows the model to predict categorical or count data.
- **Neural Networks**: Stacking multiple "layers" of linear combinations with non-linear activation functions allows for capturing complex, non-linear relationships.
- **Regularization**: Adding penalties (L1/Lasso, L2/Ridge) to the objective function prevents over-fitting by "shrinking" coefficients.

---

#foundations #ml #regression #prediction #inference #uncertainty
