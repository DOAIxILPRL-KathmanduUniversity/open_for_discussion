# Masterclass: Regression & Gradient Optimization

> [!IMPORTANT] Gist
> Linear regression is the bedrock of predictive modeling. Moving from the exact mathematical solution (LSM) to iterative optimization (Gradient Descent) is the bridge between classical statistics and modern Deep Learning.

## 1. The Normal Equation (LSM)
The **Least Squares Method (LSM)** provides an analytical solution to find the weights $\theta$ that minimize the Mean Squared Error (MSE):
$$\theta = (X^T X)^{-1} X^T y$$
- **Pros**: One-step calculation, exact solution.
- **Cons**: Computationally expensive for large datasets ($O(n^3)$ complexity for matrix inversion).

## 2. Gradient Descent (GD) Variants
When datasets are massive (millions of rows), we use iterative optimization.

### A. Batch Gradient Descent
Uses the **entire dataset** to compute the gradient at each step.
- **Pros**: Stable convergence.
- **Cons**: Very slow for large $N$.

### B. Stochastic Gradient Descent (SGD)
Uses **one random sample** per step.
- **Pros**: Extremely fast, can jump out of local minima.
- **Cons**: Noisy convergence path; requires learning rate decay.

### C. Mini-batch Gradient Descent
The industry standard. Uses a **small batch** (e.g., 32, 64) per step.
- **Pros**: Balances stability of Batch GD with speed of SGD. Leverages hardware (vectorization).

## 3. The Pro Workflow: From Data to Submission

### A. Feature Engineering & Preprocessing
1.  **Imputation**: Handling missing values (Mean/Median).
2.  **Polynomial Expansion**: Modeling non-linear relationships by creating $x^2, x^3$ features.
3.  **Scaling**: Standardizing features (Mean 0, Std 1). **Crucial for GD convergence.**
4.  **Encoding**: Converting categorical variables (Cut, Hue, Purity) into One-Hot vectors.

### B. Hyperparameter Tuning (XGBoost & MLP)
To find the "optimal" model, we use **GridSearchCV**:
- Systematically searches through combinations (e.g., `max_depth`, `learning_rate`).
- Uses **K-Fold Cross-Validation** to ensure the model generalizes across different data splits.

### C. Ensemble & Neural Regressors
- **Ridge**: Linear regression with $L2$ regularization to prevent overfitting.
- **Random Forest**: Non-linear tree-based ensemble.
- **MLP (Multi-Layer Perceptron)**: A neural network approach for capturing complex, non-linear patterns.

---

**Notebook**: [regression_masterclass.py](notebooks/regression_masterclass.py) (LSM vs GD vs XGBoost vs MLP)

#regression #optimization #gradient-descent #feature-engineering #xgboost #neural-networks
