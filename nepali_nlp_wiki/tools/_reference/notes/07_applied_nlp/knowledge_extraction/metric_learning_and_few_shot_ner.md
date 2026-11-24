# Metric Learning & Few-Shot NER

> [!IMPORTANT] Gist
> Few-shot Named Entity Recognition (NER) identifies new entities with minimal examples. Modern methods collaborate between Small Language Models (SLMs) for speed and Large Language Models (LLMs) for high-reasoning refinement (Appl. Sci. 2025).

## 1. Metric Learning-Based NER
- **Cosine Similarity as Confidence**: Using an SLM (like LACNER) to compute semantic embeddings of query and support samples.
- **Thresholding ($\theta$)**: Samples with a confidence score below a certain threshold are flagged for re-prediction by a larger model.
- **Confidence Formula**: $conf(x_{test}) = \max_{support} CosineSimilarity(h_{test}, h_{sup})$.

## 2. SLM-LLM Collaboration
- **Phase 1: Preliminary Prediction**: The SLM generates a ranked list of potential labels.
- **Phase 2: Filtering & Scoping**: The candidate word is filtered based on confidence. The label scope is restricted (e.g., Top-N labels) to reduce the LLM's cognitive burden.
- **Phase 3: LLM Re-prediction**: The LLM uses its extensive world knowledge to refine low-confidence entities.

## 3. Label Filtering Strategies
- **Retain Top-N Labels**: Only provide the LLM with the most likely labels predicted by the SLM.
- **Retain Unique Labels**: Ensure diversity in the candidate set while including a "None" option to handle non-entities.

---

#applied-nlp #ner #metric-learning #slm-llm-collaboration #few-shot-learning
