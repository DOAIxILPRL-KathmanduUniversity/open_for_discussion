# E-commerce & Product Search

> [!IMPORTANT] Gist
> Product search differs from web search because it involves highly structured data, distinct user intent (transactional), and a massive "vocabulary mismatch" between user queries and product catalogs.

## 1. The Challenges of E-commerce IR
- **Vocabulary Mismatch**: User searches for "running shoes," but the product is titled "Gel-Nimbus 25."
- **Entity Density**: Queries are often lists of attributes (e.g., "red cotton t-shirt size M").
- **Cold Start**: New products have no historical clicks or behavioral data.
- **Dynamic Catalog**: Prices, inventory, and trends change in real-time.

## 2. Technical Components
- **Product NER**: Extracting attributes (`Brand`, `Color`, `Material`, `Size`) from unstructured titles and descriptions.
- **Semantic Search (Dense Retrieval)**: Using bi-encoders (like Sentence-BERT) to map queries and products into a shared vector space, allowing for "conceptual" matching.
- **Query Rewriting & Expansion**:
    - **Spell Correction**: Critical for mobile shopping.
    - **Synonym Expansion**: Mapping "sneakers" $\leftrightarrow$ "trainers."
- **Learning to Rank (LTR)**: Using Pointwise/Pairwise models to rank products based on a combination of relevance, price, popularity, and margin.

## 3. Personalization & Context
- **User Histoy**: If a user frequently buys premium brands, "relevance" should skew toward higher price points.
- **Temporal Context**: Searching for "jacket" in December vs. July.

## 4. Evaluation Metrics
- **CTR (Click-Through Rate)**: Do users click?
- **CVR (Conversion Rate)**: Do users buy?
- **NDCG @ K**: Is the most relevant product at the top?
- **Revenue per Search (RPS)**: The ultimate business metric.

---

#applied #industry #ecommerce #ir #ltr #product-search
