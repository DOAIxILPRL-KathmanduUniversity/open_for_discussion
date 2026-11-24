# Semantic Analysis of Nepali Proverbs (Ukhan)

> [!IMPORTANT] Gist
> This study analyzes the semantic space of Nepali proverbs (Ukhan) related to women, utilizing **MURIL** (Multilingual Representations for Indian Languages) embeddings and clustering techniques. It explores how traditional gender roles are encoded in linguistic metaphors.

## 1. Embedding Strategy: MURIL
Traditional Devanagari embeddings often struggle with the idiomatic nature of proverbs. We utilize `google/muril-base-cased` to capture the contextual semantics:
- **Mean Pooling**: Sentence embeddings are derived by taking the mean of the last hidden states.
- **Cross-Lingual Alignment**: MURIL's training on 17 Indian languages (including Nepali) ensures high-fidelity representation of Devanagari syntax.

## 2. Dimensionality Reduction & Clustering
To visualize the "thematic clusters" of proverbs, we apply:
- **K-Means Clustering**: Grouping proverbs into thematic categories (e.g., *Family Life*, *Polygamy*, *Widowhood*).
- **PCA (Principal Component Analysis)**: Reducing 768-dimensional embeddings into 2D and 3D space for visual inspection.
- **Principal Component Analysis**: Identifying the underlying "axes" of semantic variance. For example, PC1 might distinguish between *Domesticity* and *Social Taboos*.

## 3. Thematic Categories
The analysis covers several culturally significant bins:
- **पारिवारिक जीवन (Family Life)**: Proverbs like "लोग्ने स्वास्नीको झगडा, परालको आगो" (straw fire).
- **आमा (Motherhood)**: Highlighting the indispensable nurturing role.
- **बहुविवाह (Polygamy)**: Reflecting both patriarchal glorification and internal domestic strife.

---

**Notebook**: [proverbs_semantic_clustering.py](notebooks/proverbs_semantic_clustering.py)

#nepali-nlp #linguistics #muril #embeddings #pca #proverbs #humanities
