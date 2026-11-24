# LLM Application Design Patterns

> [!IMPORTANT] Gist
> Moving from prototype to production requires a holistic approach that integrates LLMs into a broader software ecosystem using robust architectural patterns (Pai, 2025).

## 1. Multi-LLM Architectures
Single-model solutions often fail to balance cost, latency, and performance.
- **LLM Cascades**: Attempting a task with a cheap model (e.g., GPT-4o-mini) and escalating to a more expensive model (e.g., GPT-4o) only if the first fails.
- **Routers**: An "Orchestrator" LLM or classifier that directs queries to task-specialized models (e.g., "Code queries to CodeLlama, Creative writing to Claude").
- **Ensembling & Fusion**: Combining outputs from multiple models to improve factual accuracy.

## 2. Inference-Time Optimization
- **Inference-Time Compute**: Scaling the amount of processing during inference (e.g., o1 model) to solve complex reasoning problems via search and verification.
- **Speculative Decoding**: Using a small model to draft tokens and a large model to verify them, accelerating generation without quality loss.
- **KV Caching**: Storing key-value pairs of previous tokens to avoid re-computing them, crucial for long-context applications.

## 3. Programming Paradigms
- **DSPy (Declarative Self-improving Language Programs)**: Separating the program logic from the prompt instructions. DSPy automatically optimizes prompts and weights based on assertions and feedback.
- **LMQL (Language Model Query Language)**: A programming language for LLM interaction that combines natural language with typed constraints and search.

## 4. The Prototype-to-Production Gap
- **Passive vs. Autonomous Approaches**:
    - **Passive**: LLM generates text on demand.
    - **Autonomous**: Agents that loop through reasoning, tool use, and observation.
- **Guardrails & Verifiers**: Implementing a separate validation layer to check for hallucinations or safety violations *before* showing the output to the user.

## 5. Anatomy of the Loop
A production LLM application is a continuous transformation process (Berryman & Ziegler, 2025):
1.  **User's Problem**: Understanding the raw intent (e.g., "Fix this bug").
2.  **Model Domain Transformation**: Converting the problem into a prompt (adding context, BPE tokens, role history).
3.  **Completion Generation**: The LLM predicts the next tokens.
4.  **User Domain Transformation**: Parsing the raw text back into a useful result (e.g., a code diff, a UI component, or an API call).

## 6. Deployment Flavors
- **Self-hosted**: Using **Ollama**, **vLLM**, or **Hugging Face TGI** for privacy and cost control over open-source models (Llama 3, Mistral).

## 7. Embedding-Based Recommendation Patterns (Alammar & Grootendorst, 2024)
Embeddings are powerful even outside of generative text tasks. By treating non-textual data as "tokens" in a sequence, we can build sophisticated recommendation systems:

### The Song/Playlist Metaphor
- **Tokens as Items**: Treat individual items (e.g., songs, products, videos) as unique tokens.
- **Sentences as Sequences**: Treat user-curated collections (e.g., playlists, purchase history, clickstreams) as sentences.
- **Pattern Matching**: Use **Word2Vec (Skip-gram)** to learn the "meaning" of items based on their neighbors in the sequence.
- **Recommendation**: To recommend an item, simply find the nearest neighbors in the high-dimensional embedding space. If a user likes "Metallica," the system recommends other "Heavy Metal" tokens because they frequently co-occur in the training sequences.

---

#llm-design #architectures #dspy #lmql #inference-optimization #llm-cascades #routers
