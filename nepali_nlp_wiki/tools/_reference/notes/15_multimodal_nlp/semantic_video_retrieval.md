# Case Study: Semantic Video Retrieval in Nepali (Himal VRS)

> [!IMPORTANT] Gist
> Project AISP 322 establishes **Himal VRS**, a semantic video retrieval system for Nepali. It moves beyond keyword matching to capture semantic intent using cross-modal contrastive learning (CLIP-based).

## 1. The Dataset: Nep-VTR
The project created **Nep-VTR**, the first standardized benchmark for Nepali video-text retrieval:
- **Volume**: ~100,000 video clips.
- **Categories**: 
    - Traditional Music (Deuda, Teej, Gaura, etc.)
    - Contemporary Media (Herne Katha, OSR Digital)
    - Sports (Cricket, Volleyball)
    - Benchmark Sets (MSVD, MSR-VTT)
- **Annotation**: 850 high-quality human-annotated video-caption pairs.

## 2. Model Architectures
The system evaluates several state-of-the-art multimodal frameworks:
- **X-CLIP / CLIP4Clip**: Used as the core dual-encoder architecture.
- **Baseline Encoders**: **mCLIP** (XLM-RoBERTa based) showed the strongest text-to-video alignment compared to JinaCLIP or Qwen.
- **Optimization**: Fine-tuned using MSVD (~2,000 pairs) with **InfoNCE loss**.

## 3. Training Strategies
| Strategy | Description |
| :--- | :--- |
| **Method 1** | Frozen encoder; only projection layers trained. |
| **Method 2** | Fine-tuning projection layers from X-CLIP/CLIP4Clip checkpoints. |
| **Method 3** | End-to-end fine-tuning of encoder and projection layers. |

**Top Performance**: **X-CLIP (Method 2)** with XLM-RoBERTa text encoder achieved **R@1: 25.0%** and **MRR: 0.27** on the MSVD test set.

## 4. System Implementation & Features
- **Backend**: FastAPI with **FAISS Indexing** for sub-millisecond retrieval.
- **Search Capabilities**:
    - **Standard Search**: Natural language queries in Nepali.
    - **YouTube URL Search**: Navigates directly to the most relevant segment of a long video via timestamp.
    - **Video-to-Text Search**: Generating descriptions for retrieved clips.
- **Feedback Loop**: Implements the **Rocchio Algorithm** to refine query embeddings based on user "Likes/Unlikes."

## 5. Deployment: Himal VRS
A React-based web interface demonstrating practical applicability in education, cultural preservation, and media production.

---

#multimodal-ai #video-retrieval #clip #x-clip #nepali #himal-vrs #faiss #contrastive-learning
