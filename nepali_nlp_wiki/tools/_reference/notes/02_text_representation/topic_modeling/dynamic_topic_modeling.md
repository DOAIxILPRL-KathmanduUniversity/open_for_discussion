# Dynamic Topic Modeling (DTM)

> [!IMPORTANT] Gist
> Topic modeling is moving beyond static snapshots to track how technological concepts and innovation trends evolve over time in temporal archives like patents (Appl. Sci. 2025).

## 1. From Static to Dynamic
- **LDA (Latent Dirichlet Allocation)**: Traditional static modeling that assumes independent topics and relies on word frequency.
- **BERTopic**: A modern approach combining BERT embeddings, UMAP dimensionality reduction, and HDBSCAN clustering to find semantic topics.
- **DTM Evolution**: Adapting and refining assessments as new documents are added, allowing the identification of evolving trends in rapidly changing fields like 6G.

## 2. DTM Workflow for Patents
- **Noise Reduction**: Leveraging LLMs for prompt-based summarization of dense patent data before modeling.
- **Domain-Specific Embedding**: Using SBERT pre-trained on patent data to capture precise technological semantics.
- **Time-Aware Features**: Capturing the evolution of topic distributions across periods to visualize technological shifts.

## 3. Weak Signal Analysis
- **Emerging Topics**: Identifying "weak signals"—early signs of emerging trends that indicate potential but unconfirmed technological breakthroughs.
- **Interpretability**: DTM-based weak signal analysis makes the evolution of innovation more interpretable than traditional methods.

---

#text-representation #topic-modeling #dtm #bertopic #patents #weak-signals
