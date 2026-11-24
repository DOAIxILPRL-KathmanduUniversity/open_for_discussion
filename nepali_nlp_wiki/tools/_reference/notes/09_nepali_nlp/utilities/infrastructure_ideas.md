# NLP Infrastructure & Utility Ideas

This document distills the core architectural patterns from the legacy `ai_studio_data/scripts` archive into actionable ideas for the Sovereign Nepali Registry.

## 1. Human-in-the-Loop (HITL) Annotation
**Source**: `annotate.ipynb`

### The Idea
Instead of manual data entry, use an **Interactive Verification Loop**. A model (like mBART or Gemini) makes a "prediction" (e.g., a lemma), and the human only needs to click "Correct" or "Incorrect".

### Key Components
- **Persistence Layer**: Save every single click to a TSV/JSONL file immediately to prevent data loss.
- **State Awareness**: Keep a `set()` of `annotated_words` to automatically skip items already processed.
- **UI (Jupyter/Gradio)**: A simple interface showing the `Word` -> `Model Prediction` -> `Actions`.

---

## 2. Managed Ingestion API (The Cockpit Pattern)
**Source**: `cockpit_lemma.py`

### The Idea
Wrap all data uploads in a robust **Ingestion Class** that handles the "dirty work" of network communication.

### Implementation Features
- **Retry Logic**: Automatically log failed uploads and provide a `retry_failed()` method to resync later.
- **Collection Awareness**: Use a unified headers/auth structure for interacting with the `aitalim.com` cockpit.
- **DataFrame Integration**: Always provide a `.data()` method to pull existing registry items into a Pandas DataFrame for local analysis.

---

## 3. Linguistic Evaluation Engine
**Source**: `evaluation_metrics.ipynb`

### The Idea
Move beyond simple accuracy. Use **Rank-Based Metrics** for low-resource languages where the model might provide multiple valid candidates.

### Essential Metrics
- **Top-k Accuracy**: Check if the "Gold Lemma" exists within the model's top $N$ guesses.
- **Mean Average Precision (MAP)**: Penalize the model if the correct answer is low in the ranking.
- **IR Accuracy**: Measure the improvement in search results when using Lemmatized vs. Raw text.
