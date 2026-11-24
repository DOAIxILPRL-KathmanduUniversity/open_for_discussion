# LLM Foundations & History

> [!IMPORTANT] Gist
> Large Language Models represent the culmination of decades of research into language as a computational phenomenon—transitioning from rule-based systems to statistical models, and finally to deep neural architectures (Raaijmakers, 2025).

## 1. The Three Dimensions of "Large"
What makes a language model "Large"? It is defined by three intersecting scales:
- **Parameter Size**: The number of neural weights (complexity of the network).
- **Data Size**: The volume of tokens the model has been exposed to (knowledge base).
- **Computing Size**: The GPU FLOPS (floating-point operations) required to compute the weights.

> [!NOTE] The Chinchilla Scaling Law
> For every doubling of a model's parameters, the training data should ideally also double. Many modern models are "underfitted" or underpopulated—they have too many parameters for the amount of data they consumed (DeepMind, 2022; Raaijmakers, 2025).

## 2. Evolution of NLP Architectures

| Era | Paradigm | Key Examples | Mechanism |
| :--- | :--- | :--- | :--- |
| **1960s** | Rule-Based | ELIZA | Pattern matching and handwritten rules. |
| **1990s** | Grammar-Based | Q&A (Symantec) | Finicky, rule-based grammar (LISP). |
| **2000s** | Statistical | Markov Chains | Bag-of-Words (vectorizing word counts). |
| **2013** | Dense Neural | Word2Vec, GloVe | Static embeddings (Skip-gram, Negative Sampling). |
| **2018+** | Transformer | BERT, GPT | Contextualized embeddings (Attention-based). |

## 3. The Representation Revolution (Alammar & Grootendorst, 2024)
The history of Language AI is a quest to turn unstructured text into structured numerical representations:

### A. Bag-of-Words (BoW)
- **Mechanism**: Tokenize text, create a vocabulary, and count occurrences.
- **Flaw**: Ignores word order and semantic meaning (treats language as a literal "bag").

### B. Dense Embeddings (Word2Vec)
- **Mechanism**: Predicts neighbors via **Skip-gram** (center word $\rightarrow$ context) or **CBOW** (context $\rightarrow$ center word).
- **Negative Sampling**: A "contrastive" method where the model learns to distinguish true neighbors from random noise (Noise-Contrastive Estimation).
- **Static Nature**: A word like "bank" has the same vector whether it's a financial institution or a river edge.

### C. Contextualized Embeddings (The Inflection Point)
- **Mechanism**: Language models (like BERT or DeBERTa) use **Attention** to assign different vectors to the same word based on its surroundings.
- **Result**: "Bank" becomes two distinct vectors depending on context, enabling high-fidelity reasoning.

## 4. The Path to AI Assistant
An LLM goes through a specific "curriculum" to reach gold-medal status:
1.  **Base Model**: Pre-trained on massive raw text (Predicts the next token).
2.  **Fine-tuned Model**: Trained on instructions (Learns task obedience).
3.  **AI Assistant**: Optimized via **RLHF** (Reinforcement Learning from Human Feedback) to align with human preferences and "reward" systems.

## 4. Invariant vs. Equivariant Learning
- **Invariant Learning**: Most current LLMs need to see millions of instances (data) to learn a concept because their learning process (backpropagation) is "crude" compared to the human brain.
- **Equivariant Learning**: Human-like learning that infers topology (conceptual structure). LLMs are currently inefficient learners compared to humans, requiring roughly 10M-100M words to grasp basic syntax that a child learns with far less stimulus.

---

#llm-history #foundations #scaling-laws #nlp-evolution #ai-assistant #parameters
