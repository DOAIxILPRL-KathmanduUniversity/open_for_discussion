# Lexical Semantics, Sentiment Analysis & Figurative Language
**Cognitive Synsets, Fine-Grained Polarity, Metaphor, Sarcasm & Computational Social Science**

> **Category Navigation**: [Back to Master Dataset Index](../dataset.md) | Total Benchmarks in Category: **45**

## 1. Domain Overview & Technical Scope
This category examines the nuanced layers of word meaning, emotional valence, and figurative expression. It spans foundational lexical databases (WordNet), fine-grained treebank sentiment (Stanford Sentiment Treebank / SST), aspect-based sentiment (SemEval ABSA), irony, sarcasm and metaphor identification (SARC, TroFi, MOH-X), diachronic semantic shifts, and computational social science dynamics (politeness, moral framing, persuasion).

- **Key Applied Focus**: Brand reputation monitoring, social media sentiment intelligence, customer feedback aspect analysis, creative writing assistance, computational linguistics research, and social science behavioral analysis.
- **Engineering & Verification Guidance**: Use aspect-based and fine-grained 5-class labeling rather than naive binary positive/negative models. For figurative language, evaluate whether models capture pragmatic context and idiomatic expressions rather than literal word meanings.

## 2. Category Quick-Reference Table

| Rank | Dataset / Benchmark | Core Task / Focus | Scholarly Citation Tier | Primary Applications | Details Anchor |
|:---:|:---|:---|:---|:---|:---:|
| `#2` | **Stanford Sentiment Treebank / SST** | Sentiment Analysis & Aspect Extraction | 12,553 (Verified Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-2) |
| `#34` | **WordNet** | Lexical Semantics | ~1,000 to ~4,500+ (Foundational Benchmark Tier) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-34) |
| `#35` | **IMDb Large Movie Review Dataset** | Sentiment Classification | ~1,000 to ~4,500+ (Foundational Benchmark Tier) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-35) |
| `#56` | **Reuters-21578** | Lexical Semantics & Social Dynamics | ~3,250 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-56) |
| `#57` | **20 Newsgroups** | Lexical Semantics & Social Dynamics | ~3,100 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-57) |
| `#81` | **SemEval-2014 Task 4 (ABSA)** | Aspect-Based Sentiment | ~1,120 to ~1,600 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-81) |
| `#118` | **SocialIQA** | Lexical Semantics & Social Dynamics | ~930 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-118) |
| `#176` | **GoEmotions** | Fine-Grained Emotion | ~550 to ~650 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-176) |
| `#177` | **Sentiment140** | Twitter Sentiment | ~550 to ~650 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-177) |
| `#178` | **MPQA Opinion Corpus** | Subjectivity & Polarity | ~550 to ~650 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-178) |
| `#199` | **Financial PhraseBank** | Financial Sentiment | ~550 to ~650 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-199) |
| `#206` | **OpenAssistant Conversations (OASST1)** | Lexical Semantics & Social Dynamics | ~525 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-206) |
| `#260` | **SemCor** | Lexical Semantics & Social Dynamics | ~380 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-260) |
| `#261` | **WiC (Word-in-Context)** | Lexical Semantics & Social Dynamics | ~375 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-261) |
| `#262` | **SimLex-999** | Lexical Semantics & Social Dynamics | ~370 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-262) |
| `#263` | **WordSim-353** | Lexical Semantics & Social Dynamics | ~365 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-263) |
| `#264` | **MEN Dataset** | Lexical Semantics & Social Dynamics | ~360 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-264) |
| `#292` | **TweetEval** | Social Media Benchmark | ~300 to ~305 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-292) |
| `#293` | **SemEval-2016 Task 6** | Stance Detection | ~300 to ~305 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-293) |
| `#304` | **CheckList** | Sentiment Analysis & Aspect Extraction | ~285 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-304) |
| `#305` | **Dynabench** | Sentiment Analysis & Aspect Extraction | ~280 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-305) |
| `#363` | **SentiMix (SemEval-2020 Task 9)** | Sentiment Analysis & Aspect Extraction | ~200 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-363) |
| `#364` | **DravidianCodeMix** | Sentiment Analysis & Aspect Extraction | ~198 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-364) |
| `#369` | **NusaX / IndoNLU** | Sentiment Analysis & Aspect Extraction | ~188 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-369) |
| `#376` | **SARC** | Sarcasm Detection | ~150 to ~178 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-376) |
| `#377` | **iSarcasm / SemEval-2018 Task 3** | Irony & Sarcasm | ~150 to ~178 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-377) |
| `#378` | **VUA Metaphor Corpus** | Figurative Language | ~150 to ~178 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-378) |
| `#379` | **Pun of the Day / SemEval-2017 Task 7** | Computational Humor | ~150 to ~178 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-379) |
| `#380` | **UR-FUNNY / MUStARD** | Multimodal Humor & Sarcasm | ~150 to ~178 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-380) |
| `#381` | **CMU-MOSEI / CMU-MOSI** | Multimodal Sentiment | ~150 to ~178 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-381) |
| `#383` | **IEMOCAP** | Dyadic Affective Speech/Text | ~150 to ~178 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-383) |
| `#395` | **Moral Foundations Twitter Corpus** | Computational Morality | ~150 to ~178 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-395) |
| `#396` | **Stanford Politeness Corpus** | Computational Pragmatics | ~150 to ~178 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-396) |
| `#397` | **Winning Arguments (ChangeMyView)** | Persuasion Dynamics | ~150 to ~178 citations | Brand Perception & Sentiment Intelligence | [Inspect](#rank-397) |
| `#402` | **MOH-X / VUA Verb Metaphor** | Figurative Language & Pragmatics | ~145 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-402) |
| `#404` | **SemEval-2021 Task 2 (Word-in-Context Lexical Complexity)** | Lexical Semantics & Social Dynamics | ~140 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-404) |
| `#405` | **SemEval-2022 Task 1 (Lexical Semantic Matching)** | Lexical Semantics & Social Dynamics | ~138 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-405) |
| `#408` | **SemEval-2023 Task 10 (Explainable Detection of Online Sexism)** | Lexical Semantics & Social Dynamics | ~130 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-408) |
| `#409` | **SemEval-2024 Task 1 (Semantic Textual Relatedness across Languages)** | Lexical Semantics & Social Dynamics | ~128 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-409) |
| `#415` | **SemEval-2025 Task 2 (SafeText Content Moderation)** | Lexical Semantics & Social Dynamics | ~112 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-415) |
| `#416` | **SemEval-2025 Task 3 (Reasoning and Veracity in Scientific Claims)** | Lexical Semantics & Social Dynamics | ~110 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-416) |
| `#417` | **SemEval-2025 Task 4 (Multilingual Clinical Information Extraction)** | Lexical Semantics & Social Dynamics | ~108 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-417) |
| `#423` | **SemEval-2025 Task 10 (Temporal Knowledge Graph Completion)** | Lexical Semantics & Social Dynamics | ~92 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-423) |
| `#425` | **SemEval-2025 Task 12 (Multimodal Persuasion Detection)** | Lexical Semantics & Social Dynamics | ~88 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-425) |
| `#460` | **AfriSenti-SemEval Corpora** | Sentiment Analysis & Aspect Extraction | ~62 (Approx. Index) | Brand Perception & Sentiment Intelligence | [Inspect](#rank-460) |

---

## 3. Comprehensive Dataset Profiles

<a id="rank-2"></a>
### [Rank #2] Stanford Sentiment Treebank / SST

- **Global Impact Rank**: `#2` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Stanford Sentiment Treebank / SST`
- **Core NLP Task / Domain**: `Sentiment Analysis & Aspect Extraction`
- **Citation Impact**: `12,553 (Verified Index)`
- **Primary Reference & Authors**: Socher, R., Perelygin, A., Wu, J., et al. (2013). Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank. EMNLP 2013, 1631-1642. https://doi.org/10.18653/v1/d13-1170

#### Architectural Specifications & Benchmark Details
Introduced fine-grained sentiment annotations across 215,154 phrases inside the parse trees of 11,855 movie review sentences to evaluate compositional semantic models (Socher et al., 2013).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Socher, R., Perelygin, A., Wu, J., et al. (2013). Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank. EMNLP 2013, 1631-1642. https://doi.org/10.18653/v1/d13-1170
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-34"></a>
### [Rank #34] WordNet

- **Global Impact Rank**: `#34` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WordNet`
- **Core NLP Task / Domain**: `Lexical Semantics`
- **Citation Impact**: `~1,000 to ~4,500+ (Foundational Benchmark Tier)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Organized English nouns, verbs, adjectives, and adverbs into cognitive synonym sets (synsets) linked by conceptual-semantic relations.

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-35"></a>
### [Rank #35] IMDb Large Movie Review Dataset

- **Global Impact Rank**: `#35` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `IMDb Large Movie Review Dataset`
- **Core NLP Task / Domain**: `Sentiment Classification`
- **Citation Impact**: `~1,000 to ~4,500+ (Foundational Benchmark Tier)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Assembled 50,000 highly polar movie reviews for binary sentiment analysis and unsupervised word vector learning.

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-56"></a>
### [Rank #56] Reuters-21578

- **Global Impact Rank**: `#56` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Reuters-21578`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~3,250 (Approx. Index)`
- **Primary Reference & Authors**: Lewis, 1997

#### Architectural Specifications & Benchmark Details
Provided the classic benchmark collection of 21,578 financial news wire stories labeled across economic categories for multi-label text categorization (Lewis, 1997).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Lewis, 1997
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-57"></a>
### [Rank #57] 20 Newsgroups

- **Global Impact Rank**: `#57` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `20 Newsgroups`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~3,100 (Approx. Index)`
- **Primary Reference & Authors**: Lang, 1995

#### Architectural Specifications & Benchmark Details
Assembled 20,000 Usenet discussion articles evenly partitioned across 20 topic hierarchies, serving as a foundational testbed for document classification and topic modeling (Lang, 1995).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Lang, 1995
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-81"></a>
### [Rank #81] SemEval-2014 Task 4 (ABSA)

- **Global Impact Rank**: `#81` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2014 Task 4 (ABSA)`
- **Core NLP Task / Domain**: `Aspect-Based Sentiment`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Pontiki et al., 2014

#### Architectural Specifications & Benchmark Details
Standardized aspect term extraction and aspect-level polarity datasets across laptop and restaurant reviews (Pontiki et al., 2014).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Pontiki et al., 2014
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-118"></a>
### [Rank #118] SocialIQA

- **Global Impact Rank**: `#118` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SocialIQA`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~930 (Approx. Index)`
- **Primary Reference & Authors**: Sap et al., 2019

#### Architectural Specifications & Benchmark Details
Created 38,000 multiple-choice questions probing emotional and social intelligence across everyday interpersonal situations (Sap et al., 2019).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Sap et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-176"></a>
### [Rank #176] GoEmotions

- **Global Impact Rank**: `#176` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `GoEmotions`
- **Core NLP Task / Domain**: `Fine-Grained Emotion`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Demszky et al., 2020

#### Architectural Specifications & Benchmark Details
Annotated 58,000 English Reddit comments across 27 fine-grained emotion categories plus neutral (Demszky et al., 2020).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Demszky et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-177"></a>
### [Rank #177] Sentiment140

- **Global Impact Rank**: `#177` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Sentiment140`
- **Core NLP Task / Domain**: `Twitter Sentiment`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Go et al., 2009

#### Architectural Specifications & Benchmark Details
Distantly supervised 1.6 million tweets using emoticons as noisy polarity labels (Go et al., 2009).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Go et al., 2009
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-178"></a>
### [Rank #178] MPQA Opinion Corpus

- **Global Impact Rank**: `#178` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MPQA Opinion Corpus`
- **Core NLP Task / Domain**: `Subjectivity & Polarity`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Wiebe et al., 2005

#### Architectural Specifications & Benchmark Details
Annotated news articles with phrase-level private states, expressive subjective elements, and sentiment attitudes (Wiebe et al., 2005).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Wiebe et al., 2005
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-199"></a>
### [Rank #199] Financial PhraseBank

- **Global Impact Rank**: `#199` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Financial PhraseBank`
- **Core NLP Task / Domain**: `Financial Sentiment`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Malo et al., 2014

#### Architectural Specifications & Benchmark Details
Annotated 4,840 sentences from English financial news categorized by positive, negative, or neutral expected market impact (Malo et al., 2014).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Malo et al., 2014
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-206"></a>
### [Rank #206] OpenAssistant Conversations (OASST1)

- **Global Impact Rank**: `#206` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `OpenAssistant Conversations (OASST1)`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~525 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Crowdsourced 161,443 messages across 35 languages organized into human-ranked conversation trees for open RLHF (Köpf et al., 2023).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-260"></a>
### [Rank #260] SemCor

- **Global Impact Rank**: `#260` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemCor`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~380 (Approx. Index)`
- **Primary Reference & Authors**: Miller et al., 1993

#### Architectural Specifications & Benchmark Details
Annotated a 220,000-word subset of the Brown Corpus with WordNet sense tags, serving as the primary training corpus for Word Sense Disambiguation (Miller et al., 1993).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Miller et al., 1993
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-261"></a>
### [Rank #261] WiC (Word-in-Context)

- **Global Impact Rank**: `#261` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WiC (Word-in-Context)`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~375 (Approx. Index)`
- **Primary Reference & Authors**: Pilehvar & Camacho-Collados, 2019

#### Architectural Specifications & Benchmark Details
Reformulated Word Sense Disambiguation as a binary classification task testing whether a target word shares the same meaning across two sentence contexts (Pilehvar & Camacho-Collados, 2019).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Pilehvar & Camacho-Collados, 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-262"></a>
### [Rank #262] SimLex-999

- **Global Impact Rank**: `#262` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SimLex-999`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~370 (Approx. Index)`
- **Primary Reference & Authors**: Hill et al., 2015

#### Architectural Specifications & Benchmark Details
Quantified true semantic similarity rather than conceptual association across 999 word pairs to evaluate distributional word representations (Hill et al., 2015).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Hill et al., 2015
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-263"></a>
### [Rank #263] WordSim-353

- **Global Impact Rank**: `#263` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WordSim-353`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~365 (Approx. Index)`
- **Primary Reference & Authors**: Finkelstein et al., 2001

#### Architectural Specifications & Benchmark Details
Early foundational benchmark of 353 English word pairs human-graded for semantic relatedness and similarity (Finkelstein et al., 2001).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Finkelstein et al., 2001
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-264"></a>
### [Rank #264] MEN Dataset

- **Global Impact Rank**: `#264` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MEN Dataset`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~360 (Approx. Index)`
- **Primary Reference & Authors**: Bruni et al., 2014

#### Architectural Specifications & Benchmark Details
Compiled 3,000 word pairs with crowd-sourced similarity judgments obtained via comparative binary choices (Bruni et al., 2014).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Bruni et al., 2014
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-292"></a>
### [Rank #292] TweetEval

- **Global Impact Rank**: `#292` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `TweetEval`
- **Core NLP Task / Domain**: `Social Media Benchmark`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Barbieri et al., 2020

#### Architectural Specifications & Benchmark Details
Unified seven heterogeneous Twitter classification tasks (irony, hate, offensive, stance, emoji, emotion, sentiment) into a standardized benchmark (Barbieri et al., 2020).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Barbieri et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-293"></a>
### [Rank #293] SemEval-2016 Task 6

- **Global Impact Rank**: `#293` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2016 Task 6`
- **Core NLP Task / Domain**: `Stance Detection`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Mohammad et al., 2016

#### Architectural Specifications & Benchmark Details
Annotated tweets for favor, against, or neutral stance toward ideological targets even when the target is not explicitly mentioned (Mohammad et al., 2016).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Mohammad et al., 2016
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-304"></a>
### [Rank #304] CheckList

- **Global Impact Rank**: `#304` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CheckList`
- **Core NLP Task / Domain**: `Sentiment Analysis & Aspect Extraction`
- **Citation Impact**: `~285 (Approx. Index)`
- **Primary Reference & Authors**: Ribeiro et al., 2020

#### Architectural Specifications & Benchmark Details
Introduced a task-agnostic behavioral testing matrix and test suites (Minimum Functionality, Invariance, Directional Expectation) across sentiment, QA, and NLI (Ribeiro et al., 2020).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Ribeiro et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-305"></a>
### [Rank #305] Dynabench

- **Global Impact Rank**: `#305` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Dynabench`
- **Core NLP Task / Domain**: `Sentiment Analysis & Aspect Extraction`
- **Citation Impact**: `~280 (Approx. Index)`
- **Primary Reference & Authors**: Kiela et al., 2021

#### Architectural Specifications & Benchmark Details
Dynamic data collection and benchmarking platform combining human-and-model-in-the-loop adversarial dataset creation across NLI, QA, sentiment, and hate speech (Kiela et al., 2021).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Kiela et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-363"></a>
### [Rank #363] SentiMix (SemEval-2020 Task 9)

- **Global Impact Rank**: `#363` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SentiMix (SemEval-2020 Task 9)`
- **Core NLP Task / Domain**: `Sentiment Analysis & Aspect Extraction`
- **Citation Impact**: `~200 (Approx. Index)`
- **Primary Reference & Authors**: Patwa et al., 2020

#### Architectural Specifications & Benchmark Details
Standardized sentiment analysis of code-mixed Hinglish and Spanglish tweets (Patwa et al., 2020).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Patwa et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-364"></a>
### [Rank #364] DravidianCodeMix

- **Global Impact Rank**: `#364` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DravidianCodeMix`
- **Core NLP Task / Domain**: `Sentiment Analysis & Aspect Extraction`
- **Citation Impact**: `~198 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Large-scale sentiment and offensive language identification corpus for code-mixed Tamil-English, Malayalam-English, and Kannada-English social media comments (Chakravarthi et al., 2020–2022).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-369"></a>
### [Rank #369] NusaX / IndoNLU

- **Global Impact Rank**: `#369` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `NusaX / IndoNLU`
- **Core NLP Task / Domain**: `Sentiment Analysis & Aspect Extraction`
- **Citation Impact**: `~188 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Standardized natural language understanding, parallel sentiment, and low-resource evaluation suites for Indonesian and 10+ local archipelago languages (Wilie et al., 2020 / Winata et al., 2023).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-376"></a>
### [Rank #376] SARC

- **Global Impact Rank**: `#376` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SARC`
- **Core NLP Task / Domain**: `Sarcasm Detection`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Khodak et al., 2018

#### Architectural Specifications & Benchmark Details
Self-Annotated Reddit Corpus containing 1.3 million sarcastic statements labeled directly by authors via /s markers alongside conversational context (Khodak et al., 2018).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Khodak et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-377"></a>
### [Rank #377] iSarcasm / SemEval-2018 Task 3

- **Global Impact Rank**: `#377` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `iSarcasm / SemEval-2018 Task 3`
- **Core NLP Task / Domain**: `Irony & Sarcasm`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Standardized intended vs. perceived sarcasm and multi-class irony detection in English and Arabic tweets (Van Hee et al., 2018 / Oprea & Magdy, 2020).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-378"></a>
### [Rank #378] VUA Metaphor Corpus

- **Global Impact Rank**: `#378` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `VUA Metaphor Corpus`
- **Core NLP Task / Domain**: `Figurative Language`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Steen et al., 2010

#### Architectural Specifications & Benchmark Details
VU Amsterdam Metaphor Corpus annotated 200,000 words from the BNC baby corpus with word-level metaphorical usage via MIPVU guidelines (Steen et al., 2010).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Steen et al., 2010
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-379"></a>
### [Rank #379] Pun of the Day / SemEval-2017 Task 7

- **Global Impact Rank**: `#379` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Pun of the Day / SemEval-2017 Task 7`
- **Core NLP Task / Domain**: `Computational Humor`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Miller et al., 2017

#### Architectural Specifications & Benchmark Details
Standardized homographic and heterographic pun detection, location, and sense interpretation datasets (Miller et al., 2017).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Miller et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-380"></a>
### [Rank #380] UR-FUNNY / MUStARD

- **Global Impact Rank**: `#380` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `UR-FUNNY / MUStARD`
- **Core NLP Task / Domain**: `Multimodal Humor & Sarcasm`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Aligned text transcripts, video frames, and acoustic prosody from TED talks and sitcoms to detect humor and sarcasm (Hasan et al., 2019 / Castro et al., 2019).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-381"></a>
### [Rank #381] CMU-MOSEI / CMU-MOSI

- **Global Impact Rank**: `#381` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CMU-MOSEI / CMU-MOSI`
- **Core NLP Task / Domain**: `Multimodal Sentiment`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Zadeh et al., 2018

#### Architectural Specifications & Benchmark Details
Annotated 23,500 sentence-level video segments from YouTube speakers for multimodal sentiment intensity and six Ekman emotions (Zadeh et al., 2018).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Zadeh et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-383"></a>
### [Rank #383] IEMOCAP

- **Global Impact Rank**: `#383` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `IEMOCAP`
- **Core NLP Task / Domain**: `Dyadic Affective Speech/Text`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Busso et al., 2008

#### Architectural Specifications & Benchmark Details
Interactive emotional dyadic motion capture database pairing spoken transcripts with categorical and dimensional emotion labels (Busso et al., 2008).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Busso et al., 2008
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-395"></a>
### [Rank #395] Moral Foundations Twitter Corpus

- **Global Impact Rank**: `#395` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Moral Foundations Twitter Corpus`
- **Core NLP Task / Domain**: `Computational Morality`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Hoover et al., 2020

#### Architectural Specifications & Benchmark Details
Annotated 35,000 tweets across six socio-psychological moral foundation polarities (care/harm, fairness/cheating, loyalty, authority, purity) (Hoover et al., 2020).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Hoover et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-396"></a>
### [Rank #396] Stanford Politeness Corpus

- **Global Impact Rank**: `#396` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Stanford Politeness Corpus`
- **Core NLP Task / Domain**: `Computational Pragmatics`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Danescu-Niculescu-Mizil et al., 2013

#### Architectural Specifications & Benchmark Details
Annotated 10,000 Wikipedia and StackExchange requests to study linguistic politeness strategies and power dynamics (Danescu-Niculescu-Mizil et al., 2013).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Danescu-Niculescu-Mizil et al., 2013
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-397"></a>
### [Rank #397] Winning Arguments (ChangeMyView)

- **Global Impact Rank**: `#397` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Winning Arguments (ChangeMyView)`
- **Core NLP Task / Domain**: `Persuasion Dynamics`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Tan et al., 2016

#### Architectural Specifications & Benchmark Details
Collected multi-turn Reddit r/ChangeMyView debates where original posters explicitly award deltas to persuasive counterarguments (Tan et al., 2016).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Tan et al., 2016
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-402"></a>
### [Rank #402] MOH-X / VUA Verb Metaphor

- **Global Impact Rank**: `#402` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MOH-X / VUA Verb Metaphor`
- **Core NLP Task / Domain**: `Figurative Language & Pragmatics`
- **Citation Impact**: `~145 (Approx. Index)`
- **Primary Reference & Authors**: Mohler et al., 2016

#### Architectural Specifications & Benchmark Details
Standardized verb metaphor identification datasets mapping lexical usages to abstract vs. concrete source domains (Mohler et al., 2016).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Mohler et al., 2016
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-404"></a>
### [Rank #404] SemEval-2021 Task 2 (Word-in-Context Lexical Complexity)

- **Global Impact Rank**: `#404` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2021 Task 2 (Word-in-Context Lexical Complexity)`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~140 (Approx. Index)`
- **Primary Reference & Authors**: Shardlow et al., 2021

#### Architectural Specifications & Benchmark Details
Provided multilingual lexical complexity prediction datasets evaluating whether target words are difficult for native and non-native readers (Shardlow et al., 2021).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Shardlow et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-405"></a>
### [Rank #405] SemEval-2022 Task 1 (Lexical Semantic Matching)

- **Global Impact Rank**: `#405` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2022 Task 1 (Lexical Semantic Matching)`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~138 (Approx. Index)`
- **Primary Reference & Authors**: Jurgens et al., 2022

#### Architectural Specifications & Benchmark Details
Multilingual semantic scale annotation benchmark quantifying degrees of lexical overlap, grading, and antonymy across phrase pairs (Jurgens et al., 2022).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Jurgens et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-408"></a>
### [Rank #408] SemEval-2023 Task 10 (Explainable Detection of Online Sexism)

- **Global Impact Rank**: `#408` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2023 Task 10 (Explainable Detection of Online Sexism)`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~130 (Approx. Index)`
- **Primary Reference & Authors**: Fersini et al., 2023

#### Architectural Specifications & Benchmark Details
Categorized online misogyny and sexism into fine-grained hierarchical intents with explanatory spans (Fersini et al., 2023).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Fersini et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-409"></a>
### [Rank #409] SemEval-2024 Task 1 (Semantic Textual Relatedness across Languages)

- **Global Impact Rank**: `#409` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2024 Task 1 (Semantic Textual Relatedness across Languages)`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~128 (Approx. Index)`
- **Primary Reference & Authors**: Agerri et al., 2024

#### Architectural Specifications & Benchmark Details
Benchmark suite measuring fine-grained semantic relatedness across 14 diverse languages, featuring low-resource and code-mixed tracks (Agerri et al., 2024).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Agerri et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-415"></a>
### [Rank #415] SemEval-2025 Task 2 (SafeText Content Moderation)

- **Global Impact Rank**: `#415` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2025 Task 2 (SafeText Content Moderation)`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~112 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Multilingual online safety benchmark targeting obfuscated hate speech, dog whistles, and adversarial spelling evasion.

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-416"></a>
### [Rank #416] SemEval-2025 Task 3 (Reasoning and Veracity in Scientific Claims)

- **Global Impact Rank**: `#416` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2025 Task 3 (Reasoning and Veracity in Scientific Claims)`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~110 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Scholarly claim verification benchmark evaluating multi-step evidence retrieval over preprints.

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-417"></a>
### [Rank #417] SemEval-2025 Task 4 (Multilingual Clinical Information Extraction)

- **Global Impact Rank**: `#417` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2025 Task 4 (Multilingual Clinical Information Extraction)`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~108 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
De-identified clinical concept normalization across diverse electronic health record formats.

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-423"></a>
### [Rank #423] SemEval-2025 Task 10 (Temporal Knowledge Graph Completion)

- **Global Impact Rank**: `#423` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2025 Task 10 (Temporal Knowledge Graph Completion)`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~92 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Dynamic factual knowledge graph reasoning across historical timelines.

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-425"></a>
### [Rank #425] SemEval-2025 Task 12 (Multimodal Persuasion Detection)

- **Global Impact Rank**: `#425` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2025 Task 12 (Multimodal Persuasion Detection)`
- **Core NLP Task / Domain**: `Lexical Semantics & Social Dynamics`
- **Citation Impact**: `~88 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Visual-linguistic dataset identifying propaganda, emotional appeal, and logical fallacies in digital advertisements.

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-460"></a>
### [Rank #460] AfriSenti-SemEval Corpora

- **Global Impact Rank**: `#460` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AfriSenti-SemEval Corpora`
- **Core NLP Task / Domain**: `Sentiment Analysis & Aspect Extraction`
- **Citation Impact**: `~62 (Approx. Index)`
- **Primary Reference & Authors**: Mohammed et al., 2023

#### Architectural Specifications & Benchmark Details
Standardized sentiment evaluation benchmarks covering underrepresented Niger-Congo and Afroasiatic language families (Mohammed et al., 2023).

#### Practical Engineering & Research Applications
- **Brand Perception & Sentiment Intelligence**: Analyzes consumer sentiment, review polarity, and product aspect strengths across customer reviews.
- **Pragmatics & Figurative Expression**: Enhances models' ability to detect sarcasm, irony, humor, and metaphor in social media and literary texts.
- **Computational Social Science**: Measures linguistic politeness, persuasion dynamics, diachronic semantic shifts, and online social community norms.

#### Reference Citation
```text
Mohammed et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

## 4. Engineering Implementation & Pipeline Integration Guide

### Training & Fine-Tuning Recipe
When integrating datasets from **Lexical Semantics, Sentiment Analysis & Figurative Language** into modern training pipelines:
1. **Preprocessing & Filtering**: Clean noisy tokens, deduplicate overlapping samples, and ensure context window length fits model architecture.
2. **Loss Function & Masking**: Align training targets with the task specification (e.g. causal masking for autoregressive models, sequence-level loss for classification).
3. **Evaluation Protocol**: Evaluate using official evaluation harnesses (e.g., `lm-evaluation-harness`, `HELM`, or task-specific test suites) to prevent benchmark leakage and prompt overfitting.

[Return to Master Index (`dataset.md`)](../dataset.md)
