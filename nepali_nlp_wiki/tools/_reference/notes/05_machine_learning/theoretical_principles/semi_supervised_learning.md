# Semi-Supervised Learning in NLP

> [!IMPORTANT] Gist
> Semi-supervised learning (SSL) aims to improve model performance by exploiting the marginal distribution of large amounts of unlabeled data, which is often abundant, to complement a small set of labeled data (Søgaard, 2013).

## 1. The Motivation: Data Sparsity
In NLP, the number of features ($m$) often exceeds the number of data points ($n$). SSL helps bridge this gap by learning the underlying structure of the feature space from unlabeled text.

## 2. Wrapper Methods
These methods use a base classifier iteratively to "label" unlabeled data.
- **Self-training**: A classifier is trained on labeled data, then used to predict labels for unlabeled data. The most confident predictions are added to the training set, and the process repeats.
- **Co-training**: Requires two "independent" views of the data (e.g., words in a document vs. anchor text of links to it). Two classifiers are trained on different views and "teach" each other by adding their most confident predictions to the other's training set.
- **Tri-training**: Uses three classifiers. If two classifiers agree on a label for an unlabeled instance, it is added to the training set of the third.

## 3. Clusters-as-Features
Using unsupervised learning to create features for a supervised model.
- **Brown Clustering**: Hierarchical clustering of words based on context. The cluster ID (or a prefix of its bitstring) is used as a feature in tasks like POS tagging or NER.
- **Word Embeddings**: Using pre-trained vectors (Word2Vec, GloVe) as features or initialization for neural networks.

## 4. Graph-Based Semi-Supervised Learning
- **Label Propagation**: Modeling the data as a graph where nodes are instances and edges represent similarity. Labels are "propagated" from labeled nodes to their neighbors based on edge weights.
- **Manifold Assumption**: The intuition that data points on the same "low-dimensional manifold" (cluster/structure) should share the same label.

## 5. Soft Self-training & EM
- **Expectation-Maximization (EM)**: Treating labels of unlabeled data as "hidden variables." The E-step estimates labels, and the M-step updates model parameters to maximize likelihood.

---

#ml #semi-supervised #self-training #co-training #clusters #em
