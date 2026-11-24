# Research: Named Entity Recognition & Dependency Parsing for Nepali

> [!IMPORTANT] Gist
> Nepali NER and Parsing have transitioned from rule-based hybrid systems to graph-based neural architectures, with standardized benchmarks like Nep-gLUE providing consistency.

## 1. Named Entity Recognition (NER)

### Datasets
- **EverestNER**: >93,000 words. Complex/Inconsistent labels (challenging for models).
- **Nepali_NER**: >11,000 words. Smaller but higher label consistency (better performance).

### Evolution of Models
- **Semi-Hybrid & Statistical (2014)**:
    - **Bam & Shahi (2014)**: NER for Nepali Text using SVM.
    - **Dey et al. (2014)**: A Semi-Hybrid approach integrating rule-based and statistical methods.
- **Contemporary Neural Approaches (2019-2022)**:
    - **Singh et al. (2019)**: NER using deep architectures.
    - **Bal et al. (2019)**: NER using updated feature engineering for Devanagari.
    - **Niraula & Chapagain (2022)**: Comprehensive study on NER datasets and algorithms, evaluating SOTA transformer models.
- **Gender Prediction & Named Entities**: Character-level tokenization. Explicitly encoding the **final character** (e.g., "◌ा") boosted traditional ML accuracy by 10%. DeBERTa reached 87.2% accuracy on gender prediction from names.

### Masterclass: Semi-Supervised Co-Training for NER
When labeled data is scarce, we can leverage **Co-Training**. This algorithm uses two independent "views" of the data to teach each other.

1.  **View 1: Morphology (The Word Itself)**: Features like character n-grams and suffixes (e.g., "◌ा", "◌ी").
2.  **View 2: Context (Neighboring Words)**: Features like the previous word and next word (e.g., "{prev} _ {next}").

**The Loop**:
- Train Classifier A on View 1 and Classifier B on View 2 using a small seed of labeled data.
- Each classifier predicts labels for an unlabeled pool.
- The most **confident** predictions (e.g., for `B-LOC`) from View A are added to the training set of View B, and vice versa.
- Repeat until the unlabeled pool is exhausted or performance plateaus.

---

**Notebook**: [nepali_ner_cotraining.py](notebooks/nepali_ner_cotraining.py) (Semi-supervised BIO tagging)

## 2. Dependency Parsing

### The First Treebank (2022)
- **Methodology**: **Annotation Projection**. 1,050 sentences translated from Bengali (KGPBenTreebank).
- **Mapping**: Bengali annotations (POS/Relations) projected to Nepali via word-alignment, with manual fixes for divergence (e.g., complex predicates, negation).
- **State-of-the-art**: BiLSTM encoder with a **Biaffine Attention decoder**.
- **Results**: LAS 66.1%, UAS 81.2%.

### Universal Dependencies (UD) Mapping: Technical Blueprint
Modern Nepali parsing relies on mapping the **Nepali Treebank (NDT)** to **UD v2.0**. This involves handling one-to-many and many-to-one correspondences through specific condition logic.

#### A. POS Tag Mapping Rules
| NDT Tag | UD Tag | Condition / Note |
| :--- | :--- | :--- |
| **PWH** | `PRON`, `ADJ`, `ADV` | Lexical check: 'कहिल्यै' (ADV), 'कति' (ADJ), else PRON. |
| **JQ** | `NUM`, `DET` | `NUM` for cardinals, `DET` for quantifiers ('धेरै', 'थोरै'). |
| **JINT, PWH, AMN, ALC** | `ADV` | Many-to-one mapping for intensifiers and locative adverbs. |

#### B. Dependency Relation (DepRel) Mapping
| NDT DepRel | UD DepRel | Contextual Condition |
| :--- | :--- | :--- |
| `k1g, k1e, k1p, k1s, k1a` | `nsubj` | Subject forms (General, Experiencer, Passive, etc.) |
| `k2m, k2u, k2t` | `obj` | Direct objects (Purposive, Transitive, etc.) |
| `nmod_adj` | `amod` | Standard adjectival modifier. |
| `nmod_adj` | `nummod` | For numeric values. |
| `nmod_adj` | `det:nummod` | Quantifiers agreeing in case with the noun. |
| `nmod_adj` | `flat` | Flat MWEs (dates, monetary expressions). |
| `lwg_cont` | `case` | If associated with a **Noun**. |
| `lwg_cont` | `aux` | If associated with a **Verb** (complex postpositions). |
| `neg` | `aux` | If tagged as `VAUX` (Auxiliary Verb). |
| `neg` | `fixed` | If tagged as `CX` (Particle). |

#### C. Structural Transformation Logic
1.  **Copula Re-rooting**: In NDT, the copular verb is the head. In UD, the **predicative nominal/adjective** becomes the head, and the verb becomes a `cop` dependent.
2.  **Flat Multiword Expressions (MWE)**: NDT uses a head-last approach for names. UD enforces a **head-first** principle (the first element is the head, others are `flat` dependents).
3.  **Passive Mapping**: If the parent node has TAM (Tense, Aspect, Modality) features like 'यो' or 'ए', the relation is mapped to `nsubj:pass`.

#### D. Mapping Condition Types
- **Lexical**: Mapping based on specific lemma (e.g., 'कसरी' → `ADV`).
- **Contextual**: Mapping based on attachment (Noun-attached `lwg_cont` → `case`).
- **Morphological**: Mapping based on TAM features (Subject → `nsubj:pass`).


---

#nepali #ner #dependency-parsing #universal-dependencies #bilstm #biaffine #transformers
