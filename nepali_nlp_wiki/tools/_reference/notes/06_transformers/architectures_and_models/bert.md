# BERT

## BERT (Devlin et al., 2019)
- Bidirectional Encoder Representations from Transformers
- Pre-train on MLM (Masked Language Model) + NSP (Next Sentence Prediction)
- Fine-tune on downstream tasks

## Pre-training Objectives
- **MLM**: mask 15% of tokens, predict them
- **NSP**: binary — is sentence B the actual next sentence?

## Key Properties
- Bidirectional context (unlike left-to-right GPT)
- Contextual embeddings (unlike static Word2Vec)
- Base (110M) and Large (340M) variants

## The inflection Point: NLP's ImageNet Moment (2018)
- **ImageNet Moment**: 2018 is cited as the "ImageNet moment" for NLP, where large-scale pre-training on unlabeled data (ELMo, BERT, GPT-2) revolutionized performance across tasks, mirroring the 2012 breakthrough in Computer Vision (Ruder, 2018; Azunre et al., 2021).
- **ELMo (Embeddings from Language Models)**: A precursor to BERT that introduced **contextualized embeddings** using a bi-directional LSTM. Unlike static embeddings (Word2Vec), ELMo computes a linear interpolation of internal hidden states to capture sentential context (Peters et al., 2018; Zhang et al., 2021).

## Fine-tuning Paradigm
- Add task-specific head on top of [CLS] or token outputs
- Classification, NER, QA all with same backbone

## Domain-Adapted Variants
- **ClinicalBERT**: pre-trained on clinical notes from MIMIC-III; superior performance on clinical NER, relation extraction, and text classification (Huang et al., 2025)
- **BioBERT**: pre-trained on PubMed abstracts + PMC full-text articles; improves biomedical NER, RE, and QA over base BERT (Lee et al., 2020)
- **BioGPT**: generative biomedical model; supports multimodal fusion combining text with imaging data (Saha et al., 2026)
- Domain adaptation via continued pre-training on in-domain corpora is now a standard recipe for specializing transformers (Cho et al., 2024)

## Clinical Word Embeddings
- Biomedical language modeling produces clinical word embeddings that capture domain-specific semantic relationships (Chiu et al., 2016)
- These embeddings map clinical concepts to standardized vocabularies (SNOMED CT, UMLS), enabling interoperability across systems (Névéol et al., 2018)

---

#transformers #bert #deep-learning
