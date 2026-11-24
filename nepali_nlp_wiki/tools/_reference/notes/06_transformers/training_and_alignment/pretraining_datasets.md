# Pre-training Datasets

> [!IMPORTANT] Gist
> Modern Large Language Models (LLMs) are only as good as the massive, curated datasets they are pre-trained on. This module catalogs the primary corpora used by BERT, GPT, and T5 (Aßenmacher et al., 2025).

## 1. BERT Training Data
- **BookCorpus**: 11,038 unpublished books across 16 genres (Romance, Sci-Fi, Fantasy). ~1 billion words.
- **English Wikipedia**: Text-only extraction (excluding tables/lists). ~2.5 billion words.
- **Why?**: BERT requires document-level context to learn long-range dependencies, rather than shuffled sentence-level data.

## 2. GPT-3 Training Data (OpenAI)
| Dataset | Tokens | Weight in Training |
| :--- | :--- | :--- |
| **Common Crawl (Filtered)** | 410 Billion | 60% |
| **WebText2** | 19 Billion | 22% |
| **Books1 & Books2** | 67 Billion | 16% |
| **Wikipedia** | 3 Billion | 3% |

- **Curation Strategy**: OpenAI used a classifier to prioritize high-quality documents (using WebText as a proxy for quality) and applied fuzzy deduplication to prevent overfitting.

## 3. Google T5: Colossal Clean Crawled Corpus (C4)
The C4 dataset is a refined version of Common Crawl using aggressive heuristics:
- **Quality Filters**: Only keep lines ending in terminal punctuation; remove pages with "dirty" words; remove code snippets (e.g., `{` or `Javascript`).
- **Deduplication**: Discard all but one instance of any three-sentence span that appears more than once.
- **Language Detection**: Using `langdetect` to ensure >99% probability of being English.

## 4. Resources for Finding Datasets
- **Papers With Code**: Real-time leaderboards and code for state-of-the-art models.
- **The Big Bad NLP Database (Quantum Stat)**: A central repository with over 500 NLP datasets across various tasks and languages.

---

#transformers #llms #datasets #pretraining #bert #gpt3 #t5
