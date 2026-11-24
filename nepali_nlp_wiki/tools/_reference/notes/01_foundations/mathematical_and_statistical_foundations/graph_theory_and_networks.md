# Graph Theory & Network Science in NLP

> [!IMPORTANT] Gist
> Text is not just a linear sequence; it is a network of relationships. Graph theory provides the tools to model dependencies, social networks, and knowledge structures using nodes and edges (Ghayoumi, 2026).

## 1. Graph Fundamentals
- **Nodes ($V$) & Edges ($E$)**: Representing entities and their relationships.
- **Adjacency Matrix ($A$)**: A matrix representation where $A_{ij} = 1$ if there is an edge between node $i$ and $j$.
- **Degree Matrix ($D$)**: A diagonal matrix representing the number of connections for each node.
- **Graph Laplacian ($L = D - A$)**: A fundamental matrix for spectral analysis of graphs.

## 2. Graph Neural Networks (GNNs)
- **Message Passing**: Nodes update their state by aggregating information from their neighbors.
- **Graph Convolutions (GCNs)**: Generalizing the convolution operator from grids (images) to irregular structures (graphs).
- **Attention on Graphs (GATs)**: Using attention mechanisms to weigh the importance of different neighbors.

## 3. Applications in NLP
- **Knowledge Graphs**: Representing factual relationships (e.g., "Paris" IS_CAPITAL_OF "France").
- **Dependency Parsing**: Representing the grammatical structure of a sentence as a tree (directed acyclic graph).
- **Lexical Networks**: WordNet and other semantic networks that link words by synonymy, hyponymy, etc.
- **Social Network Analysis**: Identifying communities and influence in large text corpora from social media.

---

#foundations #graph-theory #gnns #knowledge-graphs #network-science
