# Topic Modeling (LSA & LDiA)

> [!IMPORTANT] Gist
> Topic modeling is an unsupervised technique that discovers the abstract "topics" that occur in a collection of documents. It moves from word counts to "topic scores," revealing latent semantic structures.

## 1. Latent Semantic Analysis (LSA)
LSA uses **Singular Value Decomposition (SVD)** to reduce the dimensionality of the TF-IDF matrix.
- **The Process**:
    - Build a Term-Document Matrix $A$.
    - Decompose $A$ into $U \Sigma V^T$.
    - **Truncated SVD**: Keep only the top $k$ singular values to filter out noise and capture latent concepts.
- **Goal**: Words that are semantically related (but different) will be mapped to the same topic vector.
- **Limitations**: SVD results are hard to interpret (negative values) and assume a Gaussian distribution of words.

## 2. Latent Dirichlet Allocation (LDiA)
LDiA is a generative probabilistic model that treats each document as a mixture of topics and each topic as a mixture of words.
- **The Dirichlet Prior**: Controls how many topics are likely in a document and how many words are likely in a topic.
- **The Process**: Uses Gibbs Sampling or Variational Inference to find the set of topics that most likely generated the corpus.
- **Interpretability**: Unlike LSA, LDiA results are probability distributions (non-negative), making the "top words" for a topic highly interpretable.

## 3. Distance & Similarity in Topic Space
Once documents are represented as topic vectors, we use **Cosine Similarity** to find:
- **Semantic Search**: Finding documents that talk about the same *concept* even if they share no words.
- **Clustering**: Grouping documents with similar topic mixtures.

## 4. Steering with Feedback (Linear Discriminant Analysis)
While LDiA is unsupervised, we can use **Linear Discriminant Analysis (LDA)**—the supervised counterpart—to "steer" the model toward specific categories (e.g., Spam vs. Ham) using labeled data (Lane et al., 2019).

---

#language-models #topic-modeling #lsa #ldia #svd #unsupervised
