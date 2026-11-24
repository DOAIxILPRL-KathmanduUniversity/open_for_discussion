# Annotator Reliability

> [!IMPORTANT] Gist
> Manual annotations must be precise and reproducible. Annotator reliability measures the level of agreement between human raters to ensure the "Gold Standard" dataset is consistent and objective.

## Cohen's Kappa ($\kappa$)
The Kappa statistic measures inter-rater agreement for categorical items while accounting for the agreement occurring by chance (Cavicchio, 2025).

### Mathematical Formulation
$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

Where:
- $p_o$: The relative observed agreement among raters.
- $p_e$: The hypothetical probability of chance agreement.

### Interpretation
- **1.0**: Perfect agreement.
- **0.0**: Agreement no better than chance.
- **< 0**: Disagreement (worse than chance).

## Why It Matters in NLP
In tasks like **Emotion Detection**, different humans may interpret the same sentence differently due to subjective bias. A high Kappa score validates that the emotion categories assigned to a dataset are reliable and can be used to train a machine learning model.

---

#evaluation #reliability #metrics
