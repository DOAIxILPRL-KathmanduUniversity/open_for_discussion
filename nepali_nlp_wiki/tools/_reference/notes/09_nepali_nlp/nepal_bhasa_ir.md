# Case Study: Information Retrieval in Nepal Bhasa (Newari)

> [!IMPORTANT] Gist
> Nepal Bhasa (Newari) is a Sino-Tibetan language with over 1.3 million speakers but is digitally under-resourced. Project AISP 322 (2026) establishes the first standardized Information Retrieval (IR) benchmark for the language, leveraging dense embeddings and transfer learning.

## 1. The Corpus
A curated dataset of **80,000 documents** aggregated from:
- **Nepal Mandal (50%)**: Focused on cultural and historical texts.
- **Wikipedia (50%)**: General-domain knowledge.
- **Normalization**: NFC composition for Devanagari Unicode, rule-based stemming (Snowball-inspired), and frequency-derived stopword filtering.

## 2. Methodology & Models
The project evaluated the transition from lexical (sparse) to semantic (dense) retrieval:
- **Sparse Baseline**: TF-IDF with BM25 negative sampling.
- **Dense Embeddings**:
    - **MuRIL**: Fine-tuned on Nepal Bhasa documents.
    - **Alibaba GTE**: Evaluated for multilingual transfer.
- **Training**: Contrastive learning (InfoNCE loss) with hard negative sampling via BM25.
- **Indexing**: FAISS (Facebook AI Similarity Search) for sub-millisecond retrieval across the 80k corpus.

## 3. Performance Metrics
Evaluation on 500 manually annotated test queries:
| Model | MAP | MRR | Recall@10 | Acc@1 |
| :--- | :--- | :--- | :--- | :--- |
| **TF-IDF** | 0.5678 | 0.5678 | 0.6767 | 0.5067 |
| **Fine-tuned MuRIL** | **0.8321** | **0.8321** | **0.8933** | **0.7900** |
| **Alibaba GTE** | 0.8006 | 0.8006 | 0.8867 | 0.7333 |

**Key Finding**: Fine-tuning MuRIL provided a **46.5% absolute improvement** over the TF-IDF baseline.

## 4. Cross-Lingual Capabilities
- **Task**: Retrieving English documents using Newari queries (NEW-EN).
- **Result**: MLM-enhanced MuRIL reduced the performance gap significantly compared to vanilla MuRIL (MRR gap reduced from 55.1% to 35.5%).
- **Insight**: Masked Language Modeling (MLM) on the in-domain corpus is critical for aligning semantic spaces in low-resource cross-lingual tasks.

## 5. Supplementary Resources
- **POS-Tagged Corpus**: 15,000 words in CoLLu format.
- **Construction**: Synthetic generation via few-shot prompting (Gemini) on seed annotated sentences.

## 6. Ablation Analysis (Impact on MAP)
- **Stopword Removal**: +8.0%
- **Devanagari Normalization**: +6.0%
- **Stemming**: +5.0%

---

#nepal-bhasa #newari #information-retrieval #low-resource #muril #faiss #contrastive-learning #nlp
