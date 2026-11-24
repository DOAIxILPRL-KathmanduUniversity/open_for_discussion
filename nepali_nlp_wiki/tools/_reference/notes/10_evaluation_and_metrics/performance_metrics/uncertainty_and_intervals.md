# Quantifying Uncertainty: Intervals & Bounds

> [!IMPORTANT] Gist
> A model without uncertainty bounds is incomplete. Quantifying uncertainty allows us to distinguish between a "solid" prediction and a "lucky guess," which is critical for high-stakes NLP tasks like clinical diagnosis or financial forecasting (Clark & Berry, 2026).

## 1. Types of Uncertainty
- **Aleatoric Uncertainty**: Inherent randomness in the data (noise). Cannot be reduced by more data.
- **Epistemic Uncertainty**: Uncertainty in the model's parameters. Can be reduced by collecting more training data.

## 2. Confidence vs. Prediction Intervals
- **Confidence Intervals (CI)**: Capture the uncertainty of the *estimated mean* $\mathbb{E}[Y|X]$. Used for understanding the "average" effect.
- **Prediction Intervals (PI)**: Capture the uncertainty of a *specific prediction* $\hat{y}$. PI is always wider than CI because it includes aleatoric noise ($\epsilon$):
  $$\text{PI Width} \approx \text{CI Width} + \text{Residual Variance}$$

## 3. Frequentist vs. Bayesian Approaches
- **Standard Frequentist**: Based on standard errors and t-distributions. Fast but relies on strict normality assumptions.
- **Bootstrapping**: Resampling the data with replacement to build an empirical distribution of predictions. Model-agnostic but computationally expensive.
- **Bayesian Posterior**: Uses a "Prior" and "Likelihood" to generate a "Posterior" distribution. Provides a more intuitive "Credible Interval," but requires significant expertise and compute.

## 4. Modern Methods: Conformal Prediction
Conformal prediction is a framework for providing guaranteed coverage for any model (including black-box LLMs):
- **Model Agnostic**: Works with any point-prediction model (SVM, Random Forest, Neural Net).
- **Guaranteed Coverage**: If you specify a 95% confidence level, the generated range will contain the true value at least 95% of the time, regardless of the data distribution.
- **Symmetry**: Does not assume the error distribution is symmetric or normal.

## 5. Application in NLP
- **Hallucination Detection**: Using uncertainty scores (e.g., semantic entropy) to flag when an LLM is "guessing."
- **Active Learning**: Selecting samples with the highest uncertainty for human labeling.
- **Risk Mitigation**: Implementing "I don't know" thresholds for automated customer support agents.

---

#metrics #uncertainty #intervals #conformal #bayesian #bootstrapping
