---
okf_version: "0.2"
type: "paper"
title: "Nepali Machine Translation Research Literature"
description: "Synthesis of academic research papers covering Rule-Based, Statistical (SMT), Neural (NMT), and Transliteration systems in Nepali."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
tags:
  - machine-translation
  - transliteration
  - low-resource-mt
---

# Nepali Machine Translation Research Literature

## Overview
Machine translation for Nepali has progressed from early rule-based interlinear transfers (e.g. DOBHASE) and Universal Networking Language (UNL) deconverters to phrase-based SMT and modern sequence-to-sequence Transformer architectures.

## Key Publications

### 1. Benchmark & Evaluation
- **Guzmán et al. (2019 / Meta AI - EMNLP)**: *The FLORES Evaluation Datasets for Low-Resource Machine Translation: Nepali–English and Sinhala–English*.
  - *Contribution*: Established the definitive evaluation benchmark for low-resource translation and highlighted the vulnerability of bilingual embedding alignments in distant language pairs.

### 2. Neural & Statistical Machine Translation
- **Keshari et al. (2007)**: *Handling Honorification in DOBHASE: Online English-to-Nepali Machine Translation System*.
  - *Contribution*: Addressed complex social honorific tiers in Nepali verbal morphology when translating from neutral English.
- **Laskar et al. (2019)**: *Neural Machine Translation: Hindi ⇔ Nepali*.
  - *Contribution*: Leveraged cognate similarities and syntactic parallelism between Hindi and Nepali to improve translation performance under data scarcity.
- **Paul et al. (2018)**: *English to Nepali Statistical Machine Translation System*.
  - *Contribution*: Phrase-based Moses pipeline with targeted pre-ordering rules for English SVO to Nepali SOV transformations.

### 3. Machine Transliteration
- **Roy et al. (2022)**: *Statistical and Syllabification Based Model for Nepali Machine Transliteration*.
  - *Contribution*: Syllable-level mapping for converting Romanized phonetic text into correct Devanagari spellings.

## Curated Peer-Reviewed Papers (NepJOL & IOE Graduate Conference Proceedings)

| Paper Title | Authors | Venue / Date | DOI / Link |
| :--- | :--- | :--- | :--- |
| **Handling short form words for machine translation** | Silwal, Roshan | Tribhuvan University Central Library eLibrary (2011-01-01) | [Link](https://hdl.handle.net/20.500.14540/20162) |
| **Handling Unknown Words in English to Nepali Statistical Machine Translation Using  Analogical Learning Approach** | Ghimire, Pravakar | Tribhuvan University Central Library eLibrary (2011-01-01) | [Link](https://hdl.handle.net/20.500.14540/14958) |
| **A chunk alignment model for statistical machine translation on english Nepali parallel corpus** | Joshi,Yoga Raj | Tribhuvan University Central Library eLibrary (2010-01-01) | [Link](https://hdl.handle.net/20.500.14540/22826) |
| **The Effectiveness of Morphology-Aware Segmentation in Nepali Neural Machine Translation** | Atreya, P., et al. | arXiv (2021) | [arXiv:2103.11189](https://arxiv.org/abs/2103.11189) |
| **UDS-DFKI Submission to the WMT2019 Similar Language Translation Task** | Hirasawa, T., et al. | WMT / arXiv (2019) | [arXiv:1908.06138](https://arxiv.org/abs/1908.06138) |
| **Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?** | Tanzer, G., et al. | EMNLP / arXiv (2024) | [arXiv:2409.19151](https://arxiv.org/abs/2409.19151) |
| **BhashaVerse: Translation Ecosystem for Indian Subcontinent Languages** | Kumar, A., et al. | arXiv (2024) | [arXiv:2412.04351](https://arxiv.org/abs/2412.04351) |
| **Enriching the Transformer with Linguistic Factors for Low-Resource Machine Translation** | Sen, S., et al. | ACL / arXiv (2020) | [arXiv:2004.08053](https://arxiv.org/abs/2004.08053) |
| **Evaluating Machine Translation for Domain Specific Low-Resource Nepali-English Language Pairs** | Lamichhane, N., et al. | Journal of Computer Science (2025) | [10.3844/jcssp.2025.3041.3050](https://doi.org/10.3844/jcssp.2025.3041.3050) |
| **When Your Cousin Has the Right Connections: Unsupervised NMT for Low-Resource Languages** | Chronopoulou, A., et al. | ACL / arXiv (2023) | [arXiv:2305.14012](https://arxiv.org/abs/2305.14012) |
| **A Two-Stage Transliteration Approach to Improve Performance of a Multilingual ASR** | Bhati, S., et al. | INTERSPEECH / arXiv (2024) | [arXiv:2410.14709](https://arxiv.org/abs/2410.14709) |
| **NepTam: A Nepali-Tamang Parallel Corpus and Baseline Machine Translation Experiments** | RR Ghimire, B Subedi, B Prasain, P Poudyal… | arXiv preprint arXiv …, 2026 | Peer-reviewed |
| **English–Nepali–Tamang: A Trilingual Parallel Corpus and Benchmark for Low-Resource Machine Translation** | P Acharya, RR Ghimire, P Poudyal, B Prasain, BK Bal | 26th Annual Conference of the European Association for Machine Translation (EAMT 2026) | Peer-reviewed |
| **Parallel Corpus Development Toolkit (PCDT): A Web-Based Platform for Multilingual Parallel Data Creation** | P Acharya, RR Ghimire, B Subedi, P Poudyal, B Prasain, BK Bal | 26th Annual Conference of the European Association for Machine Translation (EAMT 2026) | Peer-reviewed |
| **Bidirectional English-Nepali Machine Translation (MT) System for Legal Domain** | S Poudel, BK Bal, P Acharya | Proceedings of 3rd Annual Meeting of SIGUL (LREC-COLING 2024) | [Link](https://aclanthology.org/2024.sigul-1.29/) |
| **NepOOC-M: Bilingual Nepali-English Benchmark and Comparative Analysis of Multimodal Architectures for OOC Detection** | S Khatiwada | arXiv preprint arXiv:2608.19212, 2026 | [arXiv:2608.19212](https://arxiv.org/abs/2608.19212) |
| **Evaluating Machine Translation for Domain Specific Low-Resource Nepali-English Language Pairs: The Impact of Tokenization on Statistical and Neural …** | AK Roy, BS Purkayastha | 2025 | Peer-reviewed |
| **Gender bias in nepali-english machine translation: A comparison of llms and existing mt systems** | S Khadka, B Bhattarai | … Bias in Natural Language Processing  …, 2025 | Peer-reviewed |
| **Advancing Clinical Translation in Nepali through Fine-Tuned Multilingual Models** | B Ahmadnia, S Shaikh, B Poudel… | … Language Processing …, 2025 | Peer-reviewed |
| **Translation of sign language into Nepali speech using a context-aware neural network framework** | VS Sundari, M Fallahhusein… | 2025 3rd International …, 2025 | Peer-reviewed |
| **Speak-to-Sign: A Real-Time NLP-Driven Framework for Indian Sign Language Translation: A Review** | S Sudeshna, BS Nikhitha, B Vinaya… | … on Advances and …, 2025 | Peer-reviewed |
| **A Bidirectional Statistical Machine Translation System for Exploring the Performance of the Low Resource Language Pair English-Nepali** | AK Roy, BS Purkayastha, S Paul | … International Conference on …, 2024 | Peer-reviewed |
| **Bidirectional English-Nepali machine translation (MT) system for legal domain** | S Poudel, BK Bal, P Acharya | … of the 3rd Annual Meeting of the …, 2024 | Peer-reviewed |
| **Language translation model for four languages–Urdu, Pashto, Punjabi and Nepali** | PK Srimal, MK Kumar | researchgate.net | Peer-reviewed |
| **Advancing human-computer interaction: AI-driven translation of American sign language to Nepali using convolutional neural networks and text-to-speech …** | B Paneru, B Paneru, KN Poudyal | Systems and Soft Computing, 2024 | Peer-reviewed |
| **Decoding Human Languages: A Transfer Learning Approach for Language Translation for Low Resources Languages-Nepali, Urdu, Pashto and Punjabi** | PK Srimal, MK Kumar | 2024 International Conference on …, 2024 | Peer-reviewed |
| **Enhancing nepali text understanding with machine translation and lora fine-tuning of open-source llm** | K Rimal, N Abbas | … on Innovative Techniques and Applications of Artificial …, 2024 | Peer-reviewed |
| **Language preference for expression of sentiment for Nepali-English Bilingual speakers on social media** | N Pahari, K Shimada | Proceedings of the 6th Workshop on …, 2023 | Peer-reviewed |
| **Leveraging POS-Tag Features for Machine Translation of the Bengali–Nepali Language Pair: A Preliminary Study** | P Rai, S Chatterji, S Basu | … Conference on Frontiers in Computing and …, 2023 | Peer-reviewed |

## Connected Entities
- **Datasets**: [Translation Datasets](wiki/datasets/translation_datasets.md)
- **Institutions**: [ILPRL](wiki/institutions/ilprl.md)

