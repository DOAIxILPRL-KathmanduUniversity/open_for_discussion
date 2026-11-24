# RAG (Retrieval-Augmented Generation)

> [!IMPORTANT] Gist
> RAG transforms LLMs from creative writers into context-aware experts by grounding them in external knowledge bases. This modular architecture bridges the gap between static model training and real-time, factual information retrieval (Dhyani, 2026).

## 1. The Core Pipeline (Dhyani's Recipes)
A production-ready RAG system follows a rigorous sequence of transformations:

### A. Document Ingestion & Loading
- **Heterogeneous Sources**: Loading from PDF, DOCX, TXT, HTML, JSON, CSV, and SQL/APIs.
- **Metadata Enrichment**: Tagging documents with source, author, category, and timestamps for downstream filtering.

### B. Strategic Splitting (Chunking)
- **Structural**: Page-based, table-based, or HTML-tag based splitting.
- **Semantic**: Topic-driven segmentation or recursive character splitting with overlap to maintain contextual continuity.
- **N-Gram Splitting**: Creating overlapping word sequences to improve retrieval granularity.

### C. Representation (Embeddings)
- **Vectorization**: Converting text into high-dimensional numerical vectors (e.g., `all-MiniLM-L6-v2`).
- **Optimization**: Batch embedding for large datasets and persistent storage of vectors to minimize compute costs.

### D. Retrieval Mechanisms
- **Dense Retrieval**: Semantic similarity search using vector distances (Cosine, Euclidean).
- **Keyword/Lexical Search**: BM25 for exact term matching.
- **Hybrid Search**: Combining Dense + Sparse signals to handle both semantic meaning and specific keywords.
- **Metadata Filtering**: Scoping searches to specific subsets (e.g., "Only search documents from 2025").

### E. Generation & Grounding
- **Contextual Prompting**: Injecting retrieved chunks into the LLM prompt.
- **Cited Responses**: Requiring the model to link every claim to a specific source chunk.
- **Chain-of-Thought (CoT)**: Guiding the model to reason through the retrieved context before generating a final answer.

## 2. Advanced Optimization Strategies
- **Re-ranking**: Using a cross-encoder to re-evaluate the top-k results for higher precision (Dhyani, 2026).
- **Dimensionality Reduction**: Compressing vectors for faster indexing in large-scale systems.
- **Query Reformulation**: Using an LLM to rewrite vague user queries into searchable, high-intent prompts.

## 3. Agentic RAG
The "intelligent" evolution where an agent dynamically controls the retrieval loop:
- **Self-Querying**: The agent decides which filters and keywords to apply.
- **Iterative Retrieval**: The agent fetches data, reflects on it, and decides if more information is needed.
- **Adaptive Summarization**: Dynamically adjusting context length based on the complexity of the query.

> [!TIP]
> For specific code recipes, splitting strategies, and optimization patterns, see the **[RAG Implementation Patterns Cookbook](file:///Users/paramanada/Desktop/nlp_notes_for_enthusiast/08_modern_frontiers/llm_engineering/rag_implementation_patterns.md)**.

---

#modern-frontiers #rag #embeddings #vector-stores #agentic-rag #dhyani-cookbook

