# Text Classification

## Problem
- Assign one or more labels to a text document
- Spam detection, topic classification, intent recognition

## Classical Approaches
- Naive Bayes + TF-IDF (strong baseline)
- SVM with n-gram features
- Logistic regression

## Deep Learning
- CNN for text (Kim, 2014)
- BERT fine-tuning (current standard)

## Ensemble Methods
Combining multiple models to improve accuracy and robustness (Ghavami, 2020).
- **Vote-based Schema**: Majority voting among several classifiers.
- **Accuracy-based Schema**: Weighting model votes based on their individual validation performance.
- **Diversity-based Schema**: Combining models with different "views" (e.g., one on TF-IDF, one on BERT, one on CNN).
- **Bagging & Boosting**: Using Random Forest or Gradient Boosting (XGBoost/LightGBM) on high-level linguistic features.

## Feature Engineering & Normalization
- **Regex Generalization**: Replacing specific dates, amounts, and numbers with common tokens (e.g., `datepp`, `moneypp`) to reduce sparsity and improve robustness.
- **Handling Multi-class Imbalance**: Using **Stratified Splits** to ensure minor classes are represented in training/testing.
- **Identifying Issue Lines**: In conversational data (chats/emails), the intent is often buried. Identifying the "Issue Line"—the specific sentence where the user states the problem (usually following a greeting)—drastically improves the signal-to-noise ratio.

## Evaluation
- Accuracy, Precision, Recall, F1
- Macro vs. micro averaging for multi-class

## Automated Coding (Classification at Scale)
- Assigning standardized codes (ICD-10, SNOMED-CT, CPT) to free-text documents is a multi-label classification task (Farkas and Szarvas, 2008)
- NLP-based coding reduces manual coding time by up to 70% while improving consistency (Stanfill et al., 2010)
- Combines NER (entity extraction) with classification (code assignment) in a pipeline architecture (Shek et al., 2021)

---

**Notebook**: [classification_pipeline.py](notebooks/classification_pipeline.py)

#applied #classification
