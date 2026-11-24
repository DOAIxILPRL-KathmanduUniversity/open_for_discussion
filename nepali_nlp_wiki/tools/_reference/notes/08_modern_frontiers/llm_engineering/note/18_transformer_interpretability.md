# Transformer Interpretability & Visualization

> [!IMPORTANT] Gist
> To "shatter the black box," we must use visualization and attribution tools to understand how attention heads and neurons contribute to specific outputs (Rothman, 2024).

## 1. Visualizing Attention
Attention is the core of the transformer. Understanding it requires looking at "where" the model is looking.
- **BertViz**: A tool for visualizing attention heads in models like BERT, GPT-2, and T5. It allows users to see which tokens are "attending" to others across different layers.
- **Head View**: Displays attention patterns for all heads in a single layer.
- **Model View**: Shows a birds-eye view of all layers and heads simultaneously.

## 2. Feature Attribution & Model Explanations
Beyond just attention, we need to know "why" a model made a specific prediction.
- **SHAP (SHapley Additive exPlanations)**: A game-theoretic approach to explain the output of any machine learning model. In transformers, it helps identify which tokens were most influential in a classification or generation task.
- **LIME (Local Interpretable Model-agnostic Explanations)**: Approximates the transformer with a simpler, local linear model to explain individual predictions.
- **LIT (Language Interpretability Tool)**: A Google-developed toolkit for probing NLP models, including PCA (Principal Component Analysis) of embeddings and counterfactual analysis.

## 3. Mechanistic Interpretability & Dictionary Learning
- **Neuron Analysis**: OpenAI has pioneered using LLMs (GPT-4) to explain the behavior of individual neurons in smaller models (GPT-2).
- **Dictionary Learning**: Decomposing complex transformer activations into sparse, interpretable "features" (e.g., a "legal language" feature or an "uppercase" feature).

## 4. Token-ID Mapping & Quality Control
A transformer's behavior is dictated by its tokenizer.
- **Token-ID Display**: Building custom functions to see how a string is decomposed (e.g., "The cat sat" $\rightarrow$ `[101, 1996, 4937, 2931, 102]`).
- **Noisy Relationships**: Identifying rare words that are fragmented into too many sub-tokens, which can degrade performance in domain-specific tasks (Legal, Medical).

---

#interpretability #bertviz #shap #lime #lit #dictionary-learning #tokenization #black-box
