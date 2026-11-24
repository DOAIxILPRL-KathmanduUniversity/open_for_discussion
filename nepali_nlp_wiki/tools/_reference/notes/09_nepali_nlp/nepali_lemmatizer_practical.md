# Practical: Nepali Lemmatizer Inference (mT5)

> [!IMPORTANT] Gist
> Modern Nepali lemmatization leverages the **mT5-base** transformer architecture to generate the root form of a word. This approach outperforms rule-based stemmers by understanding linguistic context and irregular inflections.

## 1. Model Overview
- **Model Name**: `sunilregmi/nepali-lemmatizerV1-mt5-base`
- **Architecture**: mT5 (Multilingual Text-to-Text Transfer Transformer).
- **Task**: Text-to-Text (Input: "lemmatize: {word}" → Output: "{lemma}").

## 2. Inference Pipeline
To run high-speed inference on a dataset, the pipeline follows these steps:
1.  **Prefix Injection**: Every input must be prefixed with `lemmatize: `.
2.  **GPU Acceleration**: Using `torch.device("cuda")` is recommended for batch processing large CSV files.
3.  **Beam Search / Greedy Decoding**: The model generates the lemma token-by-token.

## 3. Comparative Performance (The Over-stemming Test)
Transformers are particularly good at avoiding "over-stemming" (where the stemmer cuts off too much, changing the word's meaning).

| Inflected Word | Rule-based Stemmer | mT5 Lemmatizer |
| :--- | :--- | :--- |
| बजाइरहेको | बजा | बजाउनु |
| गएको | ग | जानु |
| गर्दैछ | गर् | गर्नु |

---

**Notebook**: [nepali_lemmatizer_inference.py](notebooks/nepali_lemmatizer_inference.py) (GPU-enabled Batch Processing)

#nepali #lemmatization #mt5 #transformers #huggingface #gpu-inference
