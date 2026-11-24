# Project: Extending IndoWordNet for Nepali-Hindi Translation

> [!NOTE] Implementation Context
> This project (Code No: AISP 222, KU Department of AI, 2024) focuses on bridging the resource gap between Hindi and Nepali lexical knowledge bases to improve translation and paraphrasing accuracy.

## 1. The Core Disparity
WordNets are semantic lexicons modeled after Princeton WordNet. While IndoWordNet (IWN) links 18 languages, the coverage is highly uneven:
- **Hindi WordNet**: ~40,371 synsets.
- **Nepali WordNet**: ~11,713 synsets.

## 2. Methodology: Leveraging Linguistic Similarity
Since Nepali and Hindi are closely related (Indo-Aryan, Devanagari script, high lexical overlap), the project utilizes a **Cross-Lingual Alignment** strategy.

### A. Data Collection & Preparation
- **Bilingual Corpora**: 2.8 million Hindi-Nepali sentence pairs (Samanaantar, BPCC from OPUS).
- **Trilingual Corpus**: 284,000 pairs (Hindi, English, Nepali) after cleaning/normalization.
- **Preprocessing**: Morfessor-based morphological parsing (Unsupervised, Semi-supervised with 5k labels, Supervised with 10k labels).

### B. WordNet Development Workflow
1.  **Alignment Tools**: 
    - **Word2Word**: Trained on trilingual data; results improved after Morfessor parsing.
    - **VecMap**: Cross-lingual alignment using CBOW/Skip-gram; faced issues with embedding mapping (e.g., mapping "Bharat" to "Nepal").
2.  **Synset Expansion**: Manually mined 117,000 Nepali synset pairs (synonyms and glosses from dictionary).
3.  **Lexical Relations**: Established within IWN/Princeton framework; cross-lingual links implemented via Word2Word.

### C. NLP Tool Integration
- **Morphological Analysis**: Fully unsupervised lemmatizer (Morfessor) and Hunspell-based spellchecking.
- **NER Datasets**: Explored Ebiquity, Danfe, and Everest NER (implementation pending).
- **POS Tagging**: Utilized NNC Corpus; explored INception tool for active learning.

## 3. Translation & Paraphrasing System
- **Statistical Machine Translation (SMT)**: Phrase-based and syntax-based models underperformed due to lack of morphology understanding and OOV issues.
- **Neural Machine Translation (NMT)**: IndicTrans2 (320M and 1B parameters) outperformed statistical methods by handling OOV words more robustly.
- **Paraphrasing Module**: Employed Word2Vec and BERT models for contextual nuances.

## 4. Evaluation & Results
- **YOLOv11**: Evaluated for classification tasks (n variant: 81% top-1; x variant: 92% top-1).
- **Accuracy**: DenseNet121 achieved ~88% accuracy on IAPS dataset.
- **Limitations**: Data quality in parallel corpora, morphological complexity, and computational resource constraints (e.g., 64GB RAM requirement for INception full integration).

## 5. Technical Stack
- **Backend**: Python 3.9+ (NLTK-like API).
- **Database**: Supabase for storing wordnet and corpus data.
- **Deployment**: Flask-based application for real-time processing.

## 6. Key References
- **Miller, G. A. (1995)**: WordNet: A Lexical Database for English.
- **Panjwani et al. (2018)**: *pyiwn*: A Python-based API to access Indian Language WordNets.
- **Bal & Shrestha (2004)**: A Morphological Analyzer and a stemmer for Nepali.
- **Madan Puraskar Pustakalaya (2008)**: Nepali Spell Checking Dictionary.

---

#nepali #indic #indowordnet #wordnet #translation #smt #nmt #research-proposal
