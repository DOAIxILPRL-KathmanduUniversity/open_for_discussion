# Case Study: Sentiment Analysis in Nepali

> [!IMPORTANT] Gist
> Nepali sentiment analysis faces unique challenges: morphologically rich inflections, inconsistent Romanization in social media, and prevalent code-mixing (English-Nepali).

## 1. Key Datasets

### NepSA (Aspect-Based Abusive Sentiment)
- **Source**: 3,068 YouTube comments from "News & Politics" channels.
- **Task**: Targeted Aspect-Based Sentiment Analysis (TABSA).
- **Features**: Capture code-mixed/code-switched text.
- **Top Model**: Multilingual BERT for extraction (F1: 57.98%); BiLSTM for classification (F1: 81.60%).

### NepCov19Tweets
- **Size**: 33,247 tweets.
- **Task**: 3-class sentiment (Positive, Neutral, Negative).
- **Innovation**: Hybrid feature representation combining BoW, fastText, and domain-specific probability features.
- **Top Model**: **Multi-channel CNN (MCNN)** with multiple kernel sizes (1, 2, 3, 4) — 71.3% accuracy.

### Romanized Nepali Reviews
- **Focus**: E-commerce customer feedback (32,817 reviews).
- **Technique**: **Soundex Stemming** used to handle phonetic spelling variations (e.g., 'ramro' vs 'raamro').
- **Result**: Fine-tuned BERT outperformed traditional ML (79% accuracy).

### TikNep
- **Domain**: TikTok comments.
- **Multi-task**: Annotated for Sentiment, Hate-Offense, Political Stance, and Topic.

## 2. Research Landscape & Methodology
The field has matured from lexicon-based approaches to sophisticated neural models:

- **Foundational Works (2014-2016)**:
    - **Yadav & Pant (2014)**: Machine learning for movie reviews.
    - **Gupta et al. (2015)**: Bootstrapping for labeled data generation.
    - **Thapa et al. (2016)**: Subjective text classification.
- **Lexical & Machine Learning (2020)**:
    - **Piryani et al. (2020)**: Comparative study of ML vs. Lexicon-based approaches.
    - **Tamrakar et al. (2020)**: Aspect-based sentiment using SVM and Naive Bayes.
    - **Bal et al. (2020)**: Named-Entity based sentiment analysis for news media.
- **Deep Learning Era (2021-2022)**:
    - **Sitaula et al. (2021)**: Deep learning for COVID-19 tweet sentiment.
    - **Sitaula & Shahi (2022)**: Multi-channel CNN (MCNN) using hybrid features to capture local and global semantic patterns.
    - **Singh et al. (2020)**: Aspect-based abusive detection in social media.
| Feature Type | Description |
| :--- | :--- |
| **Syntactic** | Bag-of-Words (BoW) for top-100 tokens. |
| **Semantic** | 300-D fastText embeddings (averaged). |
| **Phonetic** | Soundex/Soundex-like normalization for Romanized text. |
| **Domain-specific** | Probability features based on class frequency. |

## 3. Challenges
- **Linguistic Taboos**: Offensive terms unique to Nepali socio-cultural context (caste, kinship).
- **Code-Mixing**: High frequency of English words in Romanized Nepali.
- **Over-Lemmatization**: Stemmers often destroy neologisms (e.g., political slangs like "झोले").

---

#nepali #sentiment-analysis #social-media #bert #cnn #mcnn #romanized-nepali
