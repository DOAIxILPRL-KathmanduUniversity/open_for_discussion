# Information Retrieval (IR)

> [!IMPORTANT] Gist
> IR is the science of searching for documents, information within documents, and metadata about documents. It is the foundation of modern search engines and RAG systems.

## Core Concepts
- **Query**: The user's information need expressed in a specific syntax.
- **Inverted Index**: A mapping from tokens to the documents that contain them (essential for speed).
- **Ranking**: Sorting documents based on relevance to the query.

## Learning to Rank (LTR)
LTR refers to machine learning techniques for training a model in a ranking task. It is the major problem in modern IR and NLP (Li, 2014).
- **Ranking Creation**: Generating a ranked list of offerings for a specific request.
- **Ranking Aggregation**: Merging multiple ranked lists into a single consensus ranking.

### Three Major Approaches
1. **Pointwise Approach**: Treats ranking as a regression or classification problem for individual documents (e.g., predicting a relevance score for each doc).
2. **Pairwise Approach**: Treats ranking as a binary classification of document pairs (e.g., "is Doc A more relevant than Doc B?"). Models include **Ranking SVM**, **RankNet**, and **LambdaRank**.
3. **Listwise Approach**: Focuses on the entire list of documents as the training instance. It optimizes a listwise loss function that directly correlates with IR metrics like **NDCG** or **MAP**. Models include **ListNet**, **AdaRank**, and **LambdaMART**.

## Information Retrieval Models
- **Classical Models**: Boolean, Vector Space Model (VSM), and Probabilistic models.
- **Non-Classical Models**: Logic-based and Situation Theory models.
- **Alternative Models**: Cluster-based, Fuzzy, and Latent Semantic Indexing (LSI).

## Lexical Resources
- **WordNet**: A large lexical database of English (Nouns, verbs, adjectives, and adverbs grouped into synsets).
- **Thesauri & Ontologies**: Structured vocabularies used to represent domain-specific knowledge and improve retrieval precision.

## Semantic Indexing & Ontological Enrichment
Modern IR moves beyond "shallow" keyword matching by integrating deep domain knowledge (Prince & Roche, 2009).
- **Semantic Indexing**: Disambiguating terms at index-time into their semantic types (e.g., distinguishing "Cold" as a disease vs. "Cold" as a temperature) using resources like **UMLS** (Unified Medical Language System).
- **Query Expansion**: Using synonyms and hierarchical relations (Hypernyms/Hyponyms) from ontologies like **MeSH** (Medical Subject Headings) to expand user queries, increasing **recall** without significant query drift.
- **Cross-Language IR**: Inferring "rewriting rules" to translate technical terms between languages, enabling global knowledge integration across heterogeneous document collections.

## 6. Graph-Based IR & Link Analysis
The web and large document collections can be modeled as graphs to improve ranking (Mihalcea & Radev, 2011):
- **PageRank**: A link analysis algorithm that assigns numerical weights to elements of a hyperlinked set (like the WWW) to measure their relative importance.
- **HITS**: Identifies **Authorities** (relevant sources) and **Hubs** (catalogs that link to many authorities).
- **Topic-Sensitive PageRank**: Computing PageRank scores relative to specific topics (e.g., Sports, Medicine) to provide context-aware results.
- **Document Reranking**: Using similarity graphs (where edges connect semantically similar docs) to rerank search results. Documents that are central to the "similarity cluster" are considered more relevant to the core information need.

## 7. Specialized Information Retrieval
- **Mathematical Information Retrieval**: Retrieving formulas and scientific terms using unique indexing that captures **symbolic structure** and context (Dadure et al., 2021). Essential for plagiarism detection in STEM.
- **Blockchain-Integrated IR**: Using decentralized ledgers to store document hashes, ensuring that original data can only be viewed/modified by the owner, preventing intrusion in sensitive business IR (Sheela & Priya, 2021).

## 8. Evaluation in IR
- **MAP** (Mean Average Precision)
- **NDCG** (Normalized Discounted Cumulative Gain)
- **MRR** (Mean Reciprocal Rank)
- **Precision & Recall**: Basic measures of retrieval quality.

---

#applied #ir #search
