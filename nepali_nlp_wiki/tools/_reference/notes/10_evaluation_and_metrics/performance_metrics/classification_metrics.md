# Classification Metrics

> [!IMPORTANT] Gist
> Evaluation metrics quantify model performance by comparing predicted labels against a ground-truth "Gold Standard." The choice of metric depends on class balance and the cost of specific error types (False Positives vs. False Negatives).

## The Confusion Matrix
Foundational to classification evaluation.
- **TP (True Positive)**: Correctly predicted positive.
- **TN (True Negative)**: Correctly predicted negative.
- **FP (False Positive)**: Type I Error (Incorrectly identified positive).
- **FN (False Negative)**: Type II Error (Incorrectly identified negative).

## Core Metrics

### 1. Accuracy
Ratio of correct predictions to total observations.
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
- **When to use**: Balanced datasets where all classes are equally important.
- **Limitation**: Highly misleading for imbalanced data.

### 2. Precision
Ratio of correct positive predictions to total predicted positives. "How many selected items are relevant?"
$$\text{Precision} = \frac{TP}{TP + FP}$$
- **When to use**: When False Positives are costly (e.g., spam filtering).

### 3. Recall (Sensitivity)
Ratio of correct positive predictions to all actual positives. "How many relevant items are selected?"
$$\text{Recall} = \frac{TP}{TP + FN}$$
- **When to use**: When False Negatives are critical (e.g., medical diagnosis, emotion detection).

### 4. F1-Score
The harmonic mean of Precision and Recall.
- **Why harmonic mean?**: It penalizes extreme values. If either Precision or Recall is low, the F1-score drops significantly.

## Generation & Similarity Metrics
- **BLEU (Bilingual Evaluation Understudy)**: Measures n-gram precision for translation; correlates poorly with human judgment but is the industry standard.
- **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**: An alternative to BLEU that focuses on **Recall**; primarily used for text summarization.
- **Perplexity**: Measures how well a probability model predicts a sample. In NLP, it quantifies how "confused" a language model is by a sequence of tokens. Lower perplexity $\rightarrow$ better predictive power.
- **Jaccard Similarity (Jaccard Index)**: Measures the intersection over union of two sets of tokens.
    $$\text{Jaccard}(A, B) = \frac{|A \cap B|}{|A \cup B|}$$
- **Cosine Similarity**: Measures the cosine of the angle between two embedding vectors. Essential for sentence similarity tasks.

---

#evaluation #classification #metrics
