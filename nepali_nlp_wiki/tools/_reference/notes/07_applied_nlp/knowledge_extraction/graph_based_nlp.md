# Graph-Based Natural Language Processing

> [!IMPORTANT] Gist
> Graph theory provides a unified framework for many NLP tasks by modeling language units (words, sentences, documents) as vertices and their relationships as edges. This allows the application of robust network algorithms like **Random Walks**, **PageRank**, and **Spectral Clustering** (Mihalcea & Radev, 2011).

## 1. Language Networks
Text can be represented as different types of networks:
- **Co-occurrence Networks**: Vertices are words; edges connect words that appear within a specific window (e.g., $N=2$).
- **Syntactic Dependency Networks**: Vertices are words; edges are syntactic relations (Subject, Object, etc.).
- **Semantic Networks**: Vertices are concepts; edges are semantic relations (Synonymy, Hyponymy) from resources like WordNet.
- **Similarity Networks**: Vertices are sentences or documents; edges are weighted by their semantic similarity (e.g., Cosine similarity of vectors).

## 2. Key Algorithms
- **Random Walks & Graph Ranking**:
    - **PageRank**: Measures the "importance" of a node based on the number and quality of links to it.
    - **HITS (Hyperlink-Induced Topic Search)**: Identifies **Hubs** (nodes pointing to many authorities) and **Authorities** (nodes pointed to by many hubs).
- **Centrality Measures**:
    - **Closeness Centrality**: How close a node is to all other nodes.
    - **Betweenness Centrality**: How often a node lies on the shortest path between other nodes (critical for identifying "structural holes").
- **Spectral Methods**: Using the **Laplacian Matrix** of a graph for dimensionality reduction and clustering (e.g., the Fiedler method).

## 3. Core Applications
- **Word Sense Disambiguation (WSD)**: Modeling senses as a graph and using PageRank to find the most "central" sense in a context.
- **Keyword Extraction (TextRank)**: Modeling word co-occurrences as a graph; the highest-ranked vertices are chosen as keywords.
- **Summarization (LexRank)**: Modeling sentence similarity as a graph; the most central sentences are extracted for the summary.
- **Text Clustering**: Using min-cut algorithms or random walks to partition a document similarity graph into topical clusters.

## 4. Graph-Based Information Retrieval
- **Link Analysis**: Improving search results by analyzing the hyperlink structure of the web (PageRank).
- **Document Reranking**: Using induced similarity links between documents in a retrieval set to rerank them based on their "graph centrality" relative to the query.

## 5. Advanced Graph Structures (Bengfort et al., 2018)
- **Social Graphs**: Extracting relationships between entities mentioned in text (e.g., a "Social Graph" of characters in a novel or authors in a research field).
- **Graph-Based Thesaurus**: Modeling words and their synonyms/antonyms as a graph to perform fuzzy searches or expand queries.
- **Entity Resolution (ER)**: The task of identifying which mentions in a text refer to the same real-world entity. 
    - **Blocking**: A technique to reduce the number of comparisons by only comparing entities that share a common "block" (e.g., the same last name or a similar fuzzy hash).
    - **Graph Resolution**: Using the surrounding link structure (who else is this entity connected to?) to resolve ambiguous names (e.g., "Jordan" $\to$ "Michael Jordan" if the graph shows "Bulls" and "Basketball" connections).

---

#graph-theory #pagerank #textrank #lexrank #network-analysis #semantics
