# Masterclass: Fast OPF and Contingency Analysis via DNN

> [!IMPORTANT] Gist
> This module explores the application of Deep Neural Networks (DNN) to solve Optimal Power Flow (OPF) and contingency analysis for the IEEE 30-bus system. It achieves a 5x speedup over traditional MATPOWER solvers while maintaining high regression accuracy.

## 1. System Architecture: PQS Framework
The framework predicts physical quantities from power demand (Load $P, Q$) and system status ($S$):
- **Inputs**: $P_{load}, Q_{load}$ (per bus) + Contingency Status (Line/Gen outages).
- **Outputs**: $P_g, Q_g, V, \theta, \text{Line Flow}$.

## 2. Hyperparameter Tuning (Optuna)
Bayesian Optimization is used to find the optimal architecture:
- **Layers**: 2-4 Hidden Layers.
- **Activation**: `selu` (Self-Normalizing Linear Units) for better gradient flow in deep architectures.
- **Regularization**: Batch Normalization and Dropout (0.1 - 0.5).

## 3. Training & Performance
- **K-Fold Cross Validation**: Used to ensure model robustness across different load profiles.
- **Speedup**: DNN prediction time (~milliseconds) vs. traditional MATPOWER (~2.5s).
- **R² Score**: Typically $> 0.98$ for voltage and power generation predictions.

---

**Notebook**: [power_system_dnn_opf.py](notebooks/power_system_dnn_opf.py) (Hyperparameter Tuning & Training)

#engineering #power-systems #deep-learning #opf #contingency-analysis #optuna
