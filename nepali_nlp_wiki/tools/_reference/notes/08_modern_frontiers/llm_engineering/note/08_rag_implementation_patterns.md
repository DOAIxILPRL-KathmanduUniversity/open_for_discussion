# RAG Implementation Patterns (The Cookbook)

> [!NOTE] 
> This module serves as a practical extension to the [RAG Framework](file:///Users/paramanada/Desktop/nlp_notes_for_enthusiast/08_modern_frontiers/llm_engineering/rag.md), providing specific implementation patterns and "recipes" for production-grade systems (Dhyani, 2026).

## 1. Advanced Splitting Patterns (Pai, 2025)
- **Late Chunking**: Performing chunking *after* processing the entire document through the embedding model's encoder, allowing chunks to retain global context.
- **Semantic Chunking**: Using the LLM to identify natural topic transitions and splitting documents where the semantic meaning shifts.
- **Sliding Window Chunking**: Creating overlapping chunks (e.g., `overlap=10%`) to ensure boundary context is preserved.
- **Layout-Aware Chunking**: Respecting document structure (headers, tables, lists) to maintain semantic integrity.

## 2. Embedding Optimization
- **Matryoshka Embeddings**: Models trained to pack the most important information into the first $N$ dimensions, allowing for "nested" vector sizes.
- **Instruction Embeddings**: Prepending task instructions (e.g., "Represent this query for retrieval") to the text before embedding.
- **Binary/Integer Quantization**: Converting high-precision floats to bits or integers for vector database efficiency.

## 3. Vector Scaling & Indexing
- **Page-based Splitting**: Critical for legal or academic documents where citations refer to specific page numbers.

### C. Semantic & Topic-driven Splitting
- **Topic Segmentation**: Using models (e.g., Cross-Encoders) to detect shifts in topic and split only when the context changes significantly.
- **Metadata Grouping**: Grouping small documents (e.g., customer tickets) into logical batches before splitting to maintain cross-document context.

## 2. Vector Store Optimization (FAISS & Chroma)

### A. Approximate Nearest Neighbor (ANN) Indexing
- **HNSW (Hierarchical Navigable Small World)**: A graph-based index for ultra-fast vector search in multi-million document datasets.
- **IVF (Inverted File Index)**: Clustering vectors into Voronoi cells to narrow the search space.

### B. Persistent Storage Patterns
- **Embed-Once-Store-Always**: Ensuring vectors are cached and persisted (e.g., `persist_directory` in Chroma) to avoid expensive re-calculation.
- **Cold vs. Hot Storage**: Partitioning frequently accessed "hot" vectors (current year data) from archival "cold" storage to balance cost and performance.

### C. Performance Tuning
- **Chunk Size Optimization**: Iteratively testing chunk sizes (e.g., 200 vs. 500 tokens) against retrieval accuracy metrics (Hit Rate, MRR).
- **Dimensionality Reduction**: Using PCA or SVD to compress 1536-dim vectors into 384-dim for faster search with minimal accuracy loss.

## 3. High-Precision Generation

### A. Grounded Response Patterns
- **Cited Responses**: Enforcing the LLM to provide citations (e.g., `[Source 1]`) for every factual claim.
- **Confidence Scoring**: Requiring the agent to output a "self-evaluation" score (0.0 - 1.0) on how well the retrieved context answers the query.

### B. Reasoning & Verification
- **Chain-of-Thought (CoT) Retrieval**: The agent explains *why* it chose specific chunks before generating the answer.
- **Critical Verification**: A two-step process where a "verifier" agent checks the output against the retrieved evidence for hallucinations.

### C. Progressive Disclosure
- For complex queries, the agent provides a high-level summary first, then "discloses" deeper technical details as the user asks follow-up questions.

---

#modern-frontiers #rag-recipes #vector-search #llm-engineering #dhyani-cookbook
