# Nepali NLP Resources & Datasets

> [!IMPORTANT] Gist
> The ecosystem of Nepali NLP has evolved from small, foundational corpora like the NNC to massive web-scale collections (OSCAR, CC100) and task-specific benchmarks (Nep-gLUE, NLUE).

## 1. Foundational Corpora & General-Purpose Resources

| Dataset Name | Task(s) | Size | Domain | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Nepali National Corpus (NNC)** | Monolingual, POS, MT, Spoken | ~14M words | Mixed (NELRALEC project) | Public |
| **OSCAR (Nepali)** | LLM Pre-training | >100M words | Raw web text (Common Crawl) | Public |
| **np20ng** | Text Classification | >200k docs | News (20 categories) | Public (HF) |
| **Lamsal (2020)** | Monolingual, Embeddings | ~90M words | News articles | Public |
| **CC100-Nepali** | Language Modeling | 393M words | Common Crawl (2018) | Public |
| **Nepali-Dataset** | Fill-Mask | 100k-1M items | General | Public (HF) |
| **FinePDFs (npi_Deva)** | Pre-training / Education | High Volume (PDF-extracted) | Education & Books | Public (HF) |

## 2. Lexical Semantic Resources (WordNet)

| Language | Nouns | Verbs | Adjectives | Adverbs | Total Synsets |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hindi** | 29,807 | 3,687 | 6,336 | 541 | **40,371** |
| **Bengali** | 27,281 | 2,804 | 5,815 | 445 | **36,346** |
| **Sanskrit** | 32,385 | 1,246 | 4,006 | 265 | **37,907** |
| **Marathi** | 23,271 | 3,146 | 5,269 | 539 | **32,226** |
| **Punjabi** | 23,255 | 2,836 | 5,830 | 443 | **32,364** |
| **Gujarati** | 26,503 | 2,805 | 5,828 | 445 | **35,599** |
| **Nepali** | 6,748 | 1,477 | 3,227 | 261 | **11,713** |
| **Urdu** | 22,990 | 2,801 | 5,786 | 443 | **34,280** |

*Note: Statistics represent the 2015 IndoWordNet benchmarks. Hindi serves as the pivot language for the consortium.*

## 3. Parallel Corpora & Machine Translation

| Dataset Name | Task(s) | Size | Language Pair | Status |
| :--- | :--- | :--- | :--- | :--- |
| **NNC Parallel** | Machine Translation | ~4M words | En-Ne | Public |
| **FLORES** | MT Evaluation | ~3k sentences | Multilingual (Wiki) | Public |
| **Tamang-Nepali** | MT | 15,000 pairs | Tamang-Nepali | Public |
| **Hindi-Nepali** | MT / Cross-lingual | 246k sentences | Hi-Ne (Back-translated) | Private |
| **PolyNewsParallel** | MT (Titles) | Not specified | Multilingual News | Public |

## 3. Core NLU & Task-Specific Datasets

| Dataset Name | Primary Task | Domain | Status |
| :--- | :--- | :--- | :--- |
| **NepSA** | Aspect-Abusive Sentiment | YouTube comments | Public |
| **NepCov19Tweets** | Sentiment Analysis | COVID-19 Tweets | Public |
| **Romanized Reviews** | Sentiment Analysis | E-commerce | Private |
| **TikNep** | Multi-task (Hate, Stance) | TikTok comments | Private |
| **EverestNER** | Named Entity Recognition | General (>93k words) | Public |
| **Nepali_NER** | NER (Consistent labels) | General (>11k words) | Public |
| **Dependency Treebank** | Dependency Parsing | UD Standard | Public |
| **Health Q&A** | Clinical NLP | Translated Q&A | Public |

## 4. Multimodal & Generative Datasets

| Dataset Name | Primary Task | Size | Domain |
| :--- | :--- | :--- | :--- |
| **OpenSLR (SLR54)** | ASR Training | ~157k utts | Read speech |
| **OpenSLR (SLR43)** | TTS Training | Multi-speaker | High-quality speech |
| **NSL23** | Sign Language Recognition | Video clips | ASL to Nepali signs |
| **Flickr8k_Nepali** | Image Captioning | >40k pairs | Flickr8k + Ne captions |
| **Video Captioning** | Video Captioning | MSVD translated | Translated MSVD |
| **Structured IE** | Information Extraction | 600 docs | Scanned official notices |

## 5. Standardized Benchmarks

- **Nep-gLUE**: 4 tasks (Classification, Similarity, NER, POS). Concurrently developed with NepBERTa.
- **NLUE**: 12 tasks combined; a comprehensive modern benchmark.
- **DSLNLP Shared Task**: Language ID, Hate Speech for Devanagari script languages.
- **Gender Bias Benchmarks**: Adapted evaluation for Nepali-English MT considering formal/informal levels.
- **Political Compass (PCT)**: 62 statements translated to evaluate model bias.

---

## 6. Research Bibliography (KUAIC Resource Manual 2081)

### Morphological Analysis & Stemming
- **Hardie et al. (2005)**: Nelralec Tagset (NT-01) introduction.
- **Basnet & Pandey (2009)**: Morphological analysis of verbs.
- **Hardie et al. (2009)**: Morphosyntactic categorisation scheme.
- **Balaram Prasain (2011)**: A Computational Analysis of Nepali Morphology (PhD Thesis).
- **Rai & Bhat (2012)**: Building Morphological Analyzer for Nepali.
- **Chhetri et al. (2015)**: Morph Analyser for Noun tokens.
- **Borah et al. (2017)**: Morph Analyzer for Non-Declinable Adjectives.
- **Adhikari & Neupane (2020)**: Vowel-based word splitter for Sanskrit-borrowed words.
- **Bhutia et al. (2021)**: Morph Analyzer of Verbs in Nepali.
- **Bal Krishna Bal**: Morphological Analyzer and Stemmer for Nepali.

### Named Entity Recognition (NER)
- **Bam & Shahi (2014)**: NER using Support Vector Machines.
- **Dey et al. (2014)**: Semi-Hybrid Approach for NER.
- **Bal et al. (2019)**: Named Entity Recognition for Nepali.
- **Singh et al. (2019)**: NER for Nepali Language.
- **Niraula & Chapagain (2022)**: Data Sets and Algorithms for Nepali NER.

### POS Tagging
- **Jaishi (2009)**: HMM Based Probabilistic POS Tagging.
- **Shahi & Dhamala (2013)**: SVM based POS Tagging.
- **Paul et al. (2015)**: Hidden Markov Model (HMM) based POS Tagging.
- **Sinha et al. (2015)**: Hybrid approach for POS tagging.
- **Archit Yajnik (2017, 2018)**: General Regression and ANN Based POS Tagging.
- **Prabha et al. (2018)**: Deep Learning for POS Tagging.
- **Sayami et al. (2019)**: Deep Learning Approaches for POS Tagging.
- **Pradhan & Yajnik (2021)**: Probabilistic and Neural Network Based POS Tagging.
- **Shrestha & Dhakal (2021)**: Fine-grained POS tagging.

### Sentiment Analysis
- **Yadav & Pant (2014)**: Sentiment Analysis on Movie Reviews.
- **Gupta et al. (2015)**: Bootstrap approach for Sentiment Analysis.
- **Thapa et al. (2016)**: Classifying sentiments in subjective texts.
- **Pokharel (2020)**: Twitter Sentiment analysis during COVID-19.
- **Piryani et al. (2020)**: Exploring Machine Learning and Lexicon-based Approaches.
- **Singh et al. (2020)**: Aspect Based Abusive Sentiment Detection.
- **Bal et al. (2020)**: Named-Entity Based Sentiment Analysis of News.
- **Tamrakar et al. (2020)**: Aspect Based Sentiment Analysis (SVM/NB).
- **Sitaula et al. (2021, 2022)**: Deep Learning-Based methods for COVID-19 tweets.
- **Sitaula & Shahi (2022)**: Multi-channel CNN for COVID-19 tweets.

### Speech Recognition (ASR)
- **Ssarma et al. (2017)**: HMM based isolated word recognition.
- **Kjartansson et al. (2018)**: Crowd-Sourced Speech Corpora.
- **Regmi et al. (2019)**: RNN-CTC Model for Speech Recognition.
- **Baral & Shrestha (2020)**: Large Vocabulary Continuous Speech Recognition.
- **Bhatta et al. (2020)**: Speech Recognition using CNN, GRU, and CTC.

---

## Pre-trained Models
- **NepBERTa**: State-of-the-art for NLU tasks (Nep-gLUE benchmark).
- **NepaliBERT**: General purpose BERT.
- **mBERT / XLM-RoBERTa**: Multilingual baselines.
- **Llama 3 (Adapted)**: See [Domain-adaptive Continual Learning](nepali_llm_adaptation.md).

---

#nepali #datasets #resources #benchmark
