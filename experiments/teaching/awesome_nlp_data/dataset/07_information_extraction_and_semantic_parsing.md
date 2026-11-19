# Information Extraction, NER & Semantic Parsing
**Named Entity Recognition, Relation Extraction, Coreference, Semantic Role Labeling & Text-to-SQL**

> **Category Navigation**: [Back to Master Dataset Index](../dataset.md) | Total Benchmarks in Category: **64**

## 1. Domain Overview & Technical Scope
This category focuses on transforming unstructured natural language into structured, queryable knowledge graphs, relational databases, and semantic representations. It spans entity recognition (CoNLL-2003, ACE 2005), relation extraction (TACRED, DocRED), predicate-argument structure (PropBank, FrameNet, AMR), coreference resolution (CoNLL-2012), and conversational Text-to-SQL (WikiSQL, Spider, CoSQL).

- **Key Applied Focus**: Enterprise knowledge graph construction, document parsing and intelligence, business intelligence natural language querying (Text-to-SQL), automated contract analysis, and entity linking in search engines.
- **Engineering & Verification Guidance**: When fine-tuning for structured extraction, prefer constrained decoding (e.g., JSON schema grammars or SQL AST parsers) to guarantee syntactic validity. Measure span-level micro-F1 and cross-table execution accuracy (EX) for Text-to-SQL.

## 2. Category Quick-Reference Table

| Rank | Dataset / Benchmark | Core Task / Focus | Scholarly Citation Tier | Primary Applications | Details Anchor |
|:---:|:---|:---|:---|:---|:---:|
| `#6` | **GLUE** | Named Entity Recognition & Linking | 11,720 (Verified Index) | Knowledge Graph Construction | [Inspect](#rank-6) |
| `#8` | **CoNLL-2003 NER** | Named Entity Recognition & Linking | 6,732 (Verified Index) | Knowledge Graph Construction | [Inspect](#rank-8) |
| `#40` | **OntoNotes 5.0** | Coreference & Semantics | ~1,000 to ~4,500+ (Foundational Benchmark Tier) | Knowledge Graph Construction | [Inspect](#rank-40) |
| `#43` | **AG News / Character-Level CNN Benchmarks** | Text Classification | ~1,000 to ~4,500+ (Foundational Benchmark Tier) | Knowledge Graph Construction | [Inspect](#rank-43) |
| `#44` | **FrameNet** | Frame Semantics | ~1,000 to ~4,500+ (Foundational Benchmark Tier) | Knowledge Graph Construction | [Inspect](#rank-44) |
| `#45` | **PropBank** | Semantic Role Labeling | ~1,000 to ~4,500+ (Foundational Benchmark Tier) | Knowledge Graph Construction | [Inspect](#rank-45) |
| `#66` | **WikiSQL** | Text-to-SQL Semantic Parsing | ~2,300 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-66) |
| `#67` | **Spider** | Text-to-SQL Semantic Parsing | ~2,250 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-67) |
| `#68` | **TACRED** | Relation Extraction | ~2,200 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-68) |
| `#69` | **DocRED** | Named Entity Recognition & Linking | ~2,150 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-69) |
| `#74` | **FewRel** | Relation Extraction | ~1,850 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-74) |
| `#75` | **NYT Distant Supervision Corpus** | Relation Extraction | ~1,800 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-75) |
| `#76` | **AMR Bank** | Semantic Parsing & Information Extraction | ~1,750 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-76) |
| `#79` | **AMR 2.0 / SemEval-2016 Meaning Representation** | Semantic Parsing & Information Extraction | ~1,620 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-79) |
| `#80` | **CONLL-2012 Shared Task / Coreference** | Semantic Parsing & Information Extraction | ~1,600 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-80) |
| `#185` | **RealToxicityPrompts** | LLM Safety & Toxicity | ~550 to ~650 citations | Knowledge Graph Construction | [Inspect](#rank-185) |
| `#186` | **ToxiGen** | Implicit Hate Speech | ~550 to ~650 citations | Knowledge Graph Construction | [Inspect](#rank-186) |
| `#195` | **BC5CDR (BioCreative V)** | Biomedical NER & Relation | ~550 to ~650 citations | Knowledge Graph Construction | [Inspect](#rank-195) |
| `#197` | **JNLPBA / GENIA** | Molecular Biology NER | ~550 to ~650 citations | Knowledge Graph Construction | [Inspect](#rank-197) |
| `#227` | **ToTTo** | Table-to-Text Generation | ~425 to ~430 citations | Knowledge Graph Construction | [Inspect](#rank-227) |
| `#233` | **WebNLG** | RDF-to-Text Generation | ~425 to ~430 citations | Knowledge Graph Construction | [Inspect](#rank-233) |
| `#234` | **DART** | Open-Domain Table-to-Text | ~425 to ~430 citations | Knowledge Graph Construction | [Inspect](#rank-234) |
| `#249` | **RAGTruth** | Retrieval-Grounded Hallucination | ~425 to ~430 citations | Knowledge Graph Construction | [Inspect](#rank-249) |
| `#255` | **ConceptNet 5.5** | Semantic Parsing & Information Extraction | ~405 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-255) |
| `#257` | **DBpedia** | Semantic Parsing & Information Extraction | ~395 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-257) |
| `#258` | **Freebase** | Named Entity Recognition & Linking | ~390 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-258) |
| `#259` | **Wikidata5M** | Semantic Parsing & Information Extraction | ~385 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-259) |
| `#271` | **ASAP (Automated Student Assessment Prize)** | Named Entity Recognition & Linking | ~325 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-271) |
| `#272` | **BEA-2019 / W&I+LOCNESS** | Named Entity Recognition & Linking | ~320 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-272) |
| `#273` | **CoNLL-2014 GEC / NUCLE** | Named Entity Recognition & Linking | ~315 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-273) |
| `#279` | **Flickr30k Entities** | Phrase Grounding | ~300 to ~305 citations | Knowledge Graph Construction | [Inspect](#rank-279) |
| `#287` | **i2b2 / n2c2 Clinical Tasks** | Medical Concept Extraction | ~300 to ~305 citations | Knowledge Graph Construction | [Inspect](#rank-287) |
| `#294` | **Persuasive Essays / Stab & Gurevych** | Argument Mining | ~300 to ~305 citations | Knowledge Graph Construction | [Inspect](#rank-294) |
| `#296` | **LITBANK** | Computational Literary NLP | ~300 to ~305 citations | Knowledge Graph Construction | [Inspect](#rank-296) |
| `#298` | **WritingPrompts** | Neural Story Generation | ~300 to ~305 citations | Knowledge Graph Construction | [Inspect](#rank-298) |
| `#309` | **TimeBank** | Relation Extraction | ~265 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-309) |
| `#310` | **TempEval-3** | Relation Extraction | ~262 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-310) |
| `#311` | **MATRES** | Relation Extraction | ~260 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-311) |
| `#316` | **clevr-humans / Compositional Generalization (SCAN)** | Named Entity Recognition & Linking | ~248 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-316) |
| `#317` | **CFQ (Compositional Freebase Questions)** | Named Entity Recognition & Linking | ~246 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-317) |
| `#318` | **COGS** | Named Entity Recognition & Linking | ~244 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-318) |
| `#319` | **GeoQuery** | Text-to-SQL Semantic Parsing | ~242 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-319) |
| `#323` | **MTOP** | Semantic Parsing & Information Extraction | ~232 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-323) |
| `#326` | **Penn Discourse TreeBank (PDTB 2.0/3.0)** | Discourse Parsing | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-326) |
| `#327` | **RST Discourse Treebank (RST-DT)** | Rhetorical Structure | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-327) |
| `#330` | **GAP** | Gender-Balanced Coreference | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-330) |
| `#332` | **WikiCoref / ECB+** | Cross-Document Coreference | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-332) |
| `#333` | **WNUT-17** | Emerging & Rare NER | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-333) |
| `#334` | **Few-NERD** | Few-Shot Fine-Grained NER | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-334) |
| `#335` | **CrossNER** | Cross-Domain NER | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-335) |
| `#336` | **MultiCoNER (v1 / v2)** | Complex Multilingual NER | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-336) |
| `#337` | **AIDA CoNLL-YAGO** | Entity Disambiguation | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-337) |
| `#338` | **BLINK / ZESHEL** | Zero-Shot Entity Linking | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-338) |
| `#339` | **MAVEN** | Massive Event Detection | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-339) |
| `#340` | **RAMS** | Document Event Arguments | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-340) |
| `#341` | **WikiEvents** | End-to-End Document IE | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-341) |
| `#342` | **SciERC** | Scientific Knowledge Graph | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-342) |
| `#347` | **SciNLI** | Scientific Text Entailment | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-347) |
| `#349` | **WANLI** | Worker-and-AI NLI | ~225 to ~228 citations | Knowledge Graph Construction | [Inspect](#rank-349) |
| `#412` | **SemEval-2024 Task 8 (Multigenerational Machine-Generated Text Detection)** | Named Entity Recognition & Linking | ~120 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-412) |
| `#422` | **SemEval-2025 Task 9 (Automated Argument Synthesis)** | Named Entity Recognition & Linking | ~95 (Approx. Index) | Knowledge Graph Construction | [Inspect](#rank-422) |
| `#436` | **CoSQL** | Conversational Text-to-SQL | ~85 to ~88 citations | Knowledge Graph Construction | [Inspect](#rank-436) |
| `#437` | **SParC** | Cross-Domain Semantic Parsing | ~85 to ~88 citations | Knowledge Graph Construction | [Inspect](#rank-437) |
| `#446` | **Mind2Web** | General Web Agent Eval | ~85 to ~88 citations | Knowledge Graph Construction | [Inspect](#rank-446) |

---

## 3. Comprehensive Dataset Profiles

<a id="rank-6"></a>
### [Rank #6] GLUE

- **Global Impact Rank**: `#6` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `GLUE`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `11,720 (Verified Index)`
- **Primary Reference & Authors**: Wang, A., Singh, A., Michael, J., et al. (2018). GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding. EMNLP BlackboxNLP. https://doi.org/10.18653/v1/w18-5446

#### Architectural Specifications & Benchmark Details
The General Language Understanding Evaluation benchmark aggregated nine sentence-level and sentence-pair NLU tasks—alongside a diagnostic suite for linguistic phenomena—into a unified leaderboard platform (Wang et al., 2018).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Wang, A., Singh, A., Michael, J., et al. (2018). GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding. EMNLP BlackboxNLP. https://doi.org/10.18653/v1/w18-5446
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-8"></a>
### [Rank #8] CoNLL-2003 NER

- **Global Impact Rank**: `#8` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CoNLL-2003 NER`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `6,732 (Verified Index)`
- **Primary Reference & Authors**: Sang, E. F. T. K., & De Meulder, F. (2003). Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition. CoNLL-2003. https://doi.org/10.48550/arxiv.cs/0306050

#### Architectural Specifications & Benchmark Details
Defined the benchmark shared task and annotated news wire datasets for language-independent Named Entity Recognition across person, organization, location, and miscellaneous tags (Sang & De Meulder, 2003).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Sang, E. F. T. K., & De Meulder, F. (2003). Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition. CoNLL-2003. https://doi.org/10.48550/arxiv.cs/0306050
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-40"></a>
### [Rank #40] OntoNotes 5.0

- **Global Impact Rank**: `#40` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `OntoNotes 5.0`
- **Core NLP Task / Domain**: `Coreference & Semantics`
- **Citation Impact**: `~1,000 to ~4,500+ (Foundational Benchmark Tier)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Annotated a large multi-genre corpus in English, Chinese, and Arabic with syntax, proposition banks, word sense, and coreference layers.

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-43"></a>
### [Rank #43] AG News / Character-Level CNN Benchmarks

- **Global Impact Rank**: `#43` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AG News / Character-Level CNN Benchmarks`
- **Core NLP Task / Domain**: `Text Classification`
- **Citation Impact**: `~1,000 to ~4,500+ (Foundational Benchmark Tier)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Standardized eight large-scale classification benchmarks including AG News, Sogou News, DBpedia, Yelp Reviews, Yahoo! Answers, and Amazon Reviews.

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-44"></a>
### [Rank #44] FrameNet

- **Global Impact Rank**: `#44` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `FrameNet`
- **Core NLP Task / Domain**: `Frame Semantics`
- **Citation Impact**: `~1,000 to ~4,500+ (Foundational Benchmark Tier)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Built a lexical database of English annotated with semantic frames and frame elements based on Charles Fillmore's frame semantics.

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-45"></a>
### [Rank #45] PropBank

- **Global Impact Rank**: `#45` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `PropBank`
- **Core NLP Task / Domain**: `Semantic Role Labeling`
- **Citation Impact**: `~1,000 to ~4,500+ (Foundational Benchmark Tier)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Added a layer of predicate-argument semantic role annotations onto the syntactic structures of the Penn Treebank.

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-66"></a>
### [Rank #66] WikiSQL

- **Global Impact Rank**: `#66` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WikiSQL`
- **Core NLP Task / Domain**: `Text-to-SQL Semantic Parsing`
- **Citation Impact**: `~2,300 (Approx. Index)`
- **Primary Reference & Authors**: Zhong et al., 2017

#### Architectural Specifications & Benchmark Details
Collected 80,654 hand-annotated natural language questions and SQL queries distributed across 24,241 HTML tables from Wikipedia for cross-table text-to-SQL generation (Zhong et al., 2017).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Zhong et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-67"></a>
### [Rank #67] Spider

- **Global Impact Rank**: `#67` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Spider`
- **Core NLP Task / Domain**: `Text-to-SQL Semantic Parsing`
- **Citation Impact**: `~2,250 (Approx. Index)`
- **Primary Reference & Authors**: Yu et al., 2018

#### Architectural Specifications & Benchmark Details
Introduced a large-scale complex and cross-domain text-to-SQL dataset requiring models to generalize to unseen database schemas and nested SQL clauses (Yu et al., 2018).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Yu et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-68"></a>
### [Rank #68] TACRED

- **Global Impact Rank**: `#68` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `TACRED`
- **Core NLP Task / Domain**: `Relation Extraction`
- **Citation Impact**: `~2,200 (Approx. Index)`
- **Primary Reference & Authors**: Zhang et al., 2017

#### Architectural Specifications & Benchmark Details
The TAC Relation Extraction Dataset annotated 106,264 sentence instances over newswire and web text across 41 TAC KBP relation types (Zhang et al., 2017).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Zhang et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-69"></a>
### [Rank #69] DocRED

- **Global Impact Rank**: `#69` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DocRED`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `~2,150 (Approx. Index)`
- **Primary Reference & Authors**: Yao et al., 2019

#### Architectural Specifications & Benchmark Details
Shifted relation extraction from single sentences to full documents, requiring reading and synthesizing entity interactions across multiple sentences in 5,053 Wikipedia documents (Yao et al., 2019).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Yao et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-74"></a>
### [Rank #74] FewRel

- **Global Impact Rank**: `#74` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `FewRel`
- **Core NLP Task / Domain**: `Relation Extraction`
- **Citation Impact**: `~1,850 (Approx. Index)`
- **Primary Reference & Authors**: Han et al., 2018

#### Architectural Specifications & Benchmark Details
Constructed a 70,000-sentence benchmark across 100 relations derived from Wikipedia and Wikidata specifically to evaluate few-shot relation classification (Han et al., 2018).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Han et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-75"></a>
### [Rank #75] NYT Distant Supervision Corpus

- **Global Impact Rank**: `#75` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `NYT Distant Supervision Corpus`
- **Core NLP Task / Domain**: `Relation Extraction`
- **Citation Impact**: `~1,800 (Approx. Index)`
- **Primary Reference & Authors**: Riedel et al., 2010

#### Architectural Specifications & Benchmark Details
Aligned Freebase relational tuples with New York Times corpus sentences to establish the standard benchmark for distantly supervised relation extraction (Riedel et al., 2010).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Riedel et al., 2010
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-76"></a>
### [Rank #76] AMR Bank

- **Global Impact Rank**: `#76` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AMR Bank`
- **Core NLP Task / Domain**: `Semantic Parsing & Information Extraction`
- **Citation Impact**: `~1,750 (Approx. Index)`
- **Primary Reference & Authors**: Banarescu et al., 2013

#### Architectural Specifications & Benchmark Details
Abstract Meaning Representation paired thousands of English sentences with rooted, directed, acyclic semantic graphs abstracting away surface syntactic idiosyncrasies (Banarescu et al., 2013).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Banarescu et al., 2013
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-79"></a>
### [Rank #79] AMR 2.0 / SemEval-2016 Meaning Representation

- **Global Impact Rank**: `#79` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AMR 2.0 / SemEval-2016 Meaning Representation`
- **Core NLP Task / Domain**: `Semantic Parsing & Information Extraction`
- **Citation Impact**: `~1,620 (Approx. Index)`
- **Primary Reference & Authors**: May, 2016

#### Architectural Specifications & Benchmark Details
Expanded broad-coverage semantic graph banks with wikiification, coreference, and sense-tagged frames (May, 2016).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
May, 2016
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-80"></a>
### [Rank #80] CONLL-2012 Shared Task / Coreference

- **Global Impact Rank**: `#80` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CONLL-2012 Shared Task / Coreference`
- **Core NLP Task / Domain**: `Semantic Parsing & Information Extraction`
- **Citation Impact**: `~1,600 (Approx. Index)`
- **Primary Reference & Authors**: Pradhan et al., 2012

#### Architectural Specifications & Benchmark Details
Standardized the multilingual coreference resolution benchmark partitions over OntoNotes 5.0 (Pradhan et al., 2012).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Pradhan et al., 2012
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-185"></a>
### [Rank #185] RealToxicityPrompts

- **Global Impact Rank**: `#185` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `RealToxicityPrompts`
- **Core NLP Task / Domain**: `LLM Safety & Toxicity`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Gehman et al., 2020

#### Architectural Specifications & Benchmark Details
Compiled 100,000 naturally occurring sentence-level prompts from web text to measure neural toxic degeneration in pretrained LMs (Gehman et al., 2020).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Gehman et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-186"></a>
### [Rank #186] ToxiGen

- **Global Impact Rank**: `#186` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ToxiGen`
- **Core NLP Task / Domain**: `Implicit Hate Speech`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Hartvigsen et al., 2022

#### Architectural Specifications & Benchmark Details
Generated 274,000 toxic and benign statements about 13 minority groups using adversarial machine-in-the-loop generation (Hartvigsen et al., 2022).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Hartvigsen et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-195"></a>
### [Rank #195] BC5CDR (BioCreative V)

- **Global Impact Rank**: `#195` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `BC5CDR (BioCreative V)`
- **Core NLP Task / Domain**: `Biomedical NER & Relation`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Li et al., 2016

#### Architectural Specifications & Benchmark Details
Annotated 1,500 PubMed articles with chemical and disease entities and document-level chemical-induced-disease relations (Li et al., 2016).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Li et al., 2016
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-197"></a>
### [Rank #197] JNLPBA / GENIA

- **Global Impact Rank**: `#197` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `JNLPBA / GENIA`
- **Core NLP Task / Domain**: `Molecular Biology NER`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Annotated 2,000 MEDLINE abstracts with biological terms across protein, DNA, RNA, cell line, and cell type classes (Kim et al., 2003 / Collier & Kim, 2004).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-227"></a>
### [Rank #227] ToTTo

- **Global Impact Rank**: `#227` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ToTTo`
- **Core NLP Task / Domain**: `Table-to-Text Generation`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Parikh et al., 2020

#### Architectural Specifications & Benchmark Details
Controlled table-to-text dataset with 120,000 examples where human annotators revised Wikipedia sentences to match highlighted table cells alone (Parikh et al., 2020).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Parikh et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-233"></a>
### [Rank #233] WebNLG

- **Global Impact Rank**: `#233` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WebNLG`
- **Core NLP Task / Domain**: `RDF-to-Text Generation`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Gardent et al., 2017

#### Architectural Specifications & Benchmark Details
Aligned DBpedia RDF triples across 15 semantic categories with human-written lexicalizations (Gardent et al., 2017).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Gardent et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-234"></a>
### [Rank #234] DART

- **Global Impact Rank**: `#234` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DART`
- **Core NLP Task / Domain**: `Open-Domain Table-to-Text`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Nan et al., 2021

#### Architectural Specifications & Benchmark Details
Merged semantic triples from WikiSQL, WTQ, WebNLG, and E2E into a unified 82,191-instance open-domain data-to-text corpus (Nan et al., 2021).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Nan et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-249"></a>
### [Rank #249] RAGTruth

- **Global Impact Rank**: `#249` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `RAGTruth`
- **Core NLP Task / Domain**: `Retrieval-Grounded Hallucination`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Niu et al., 2024

#### Architectural Specifications & Benchmark Details
Annotated 18,000 word-level and span-level hallucinations produced by LLMs in retrieval-augmented generation settings (Niu et al., 2024).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Niu et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-255"></a>
### [Rank #255] ConceptNet 5.5

- **Global Impact Rank**: `#255` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ConceptNet 5.5`
- **Core NLP Task / Domain**: `Semantic Parsing & Information Extraction`
- **Citation Impact**: `~405 (Approx. Index)`
- **Primary Reference & Authors**: Speer et al., 2017

#### Architectural Specifications & Benchmark Details
Built an open multilingual knowledge graph connecting words and phrases with labeled commonsense edges designed to integrate with word embeddings (Speer et al., 2017).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Speer et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-257"></a>
### [Rank #257] DBpedia

- **Global Impact Rank**: `#257` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DBpedia`
- **Core NLP Task / Domain**: `Semantic Parsing & Information Extraction`
- **Citation Impact**: `~395 (Approx. Index)`
- **Primary Reference & Authors**: Auer et al., 2007

#### Architectural Specifications & Benchmark Details
Crowd-sourced community effort to extract structured multilingual information from Wikipedia infoboxes into a linked open data graph (Auer et al., 2007).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Auer et al., 2007
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-258"></a>
### [Rank #258] Freebase

- **Global Impact Rank**: `#258` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Freebase`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `~390 (Approx. Index)`
- **Primary Reference & Authors**: Bollacker et al., 2008

#### Architectural Specifications & Benchmark Details
Collaboratively built tuple database of human knowledge that powered early entity linking, distant supervision, and KBQA datasets (Bollacker et al., 2008).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Bollacker et al., 2008
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-259"></a>
### [Rank #259] Wikidata5M

- **Global Impact Rank**: `#259` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Wikidata5M`
- **Core NLP Task / Domain**: `Semantic Parsing & Information Extraction`
- **Citation Impact**: `~385 (Approx. Index)`
- **Primary Reference & Authors**: Wang et al., 2021

#### Architectural Specifications & Benchmark Details
Aligned 5 million Wikidata entities with Wikipedia text descriptions to benchmark joint knowledge graph and language representation learning (Wang et al., 2021).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Wang et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-271"></a>
### [Rank #271] ASAP (Automated Student Assessment Prize)

- **Global Impact Rank**: `#271` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ASAP (Automated Student Assessment Prize)`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `~325 (Approx. Index)`
- **Primary Reference & Authors**: Shermis & Hamner, 2012

#### Architectural Specifications & Benchmark Details
Standardized eight essay sets written by US grade 7–10 students for automated essay scoring research (Shermis & Hamner, 2012).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Shermis & Hamner, 2012
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-272"></a>
### [Rank #272] BEA-2019 / W&I+LOCNESS

- **Global Impact Rank**: `#272` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `BEA-2019 / W&I+LOCNESS`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `~320 (Approx. Index)`
- **Primary Reference & Authors**: Bryant et al., 2019

#### Architectural Specifications & Benchmark Details
Write & Improve and LOCNESS corpora standardized Grammatical Error Correction across learner proficiency levels (Bryant et al., 2019).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Bryant et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-273"></a>
### [Rank #273] CoNLL-2014 GEC / NUCLE

- **Global Impact Rank**: `#273` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CoNLL-2014 GEC / NUCLE`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `~315 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
National University of Singapore Corpus of Learner English annotated with error tags and corrections for grammatical error correction (Dahlmeier et al., 2013 / Ng et al., 2014).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-279"></a>
### [Rank #279] Flickr30k Entities

- **Global Impact Rank**: `#279` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Flickr30k Entities`
- **Core NLP Task / Domain**: `Phrase Grounding`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Plummer et al., 2015

#### Architectural Specifications & Benchmark Details
Augmented Flickr30k captions with 244,000 coreference chains linking text phrases to 276,000 manual bounding boxes (Plummer et al., 2015).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Plummer et al., 2015
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-287"></a>
### [Rank #287] i2b2 / n2c2 Clinical Tasks

- **Global Impact Rank**: `#287` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `i2b2 / n2c2 Clinical Tasks`
- **Core NLP Task / Domain**: `Medical Concept Extraction`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Uzuner et al., 2011

#### Architectural Specifications & Benchmark Details
Standardized shared task corpora for clinical de-identification, medication extraction, temporal relations, and cohort selection (Uzuner et al., 2011).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Uzuner et al., 2011
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-294"></a>
### [Rank #294] Persuasive Essays / Stab & Gurevych

- **Global Impact Rank**: `#294` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Persuasive Essays / Stab & Gurevych`
- **Core NLP Task / Domain**: `Argument Mining`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Stab & Gurevych, 2014

#### Architectural Specifications & Benchmark Details
Annotated 402 student essays with argument components (major claims, claims, premises) and support/attack argumentative relations (Stab & Gurevych, 2014).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Stab & Gurevych, 2014
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-296"></a>
### [Rank #296] LITBANK

- **Global Impact Rank**: `#296` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `LITBANK`
- **Core NLP Task / Domain**: `Computational Literary NLP`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Bamman et al., 2019

#### Architectural Specifications & Benchmark Details
Annotated 100 works of English-language fiction with entities, events, and long-document coreference chains (Bamman et al., 2019).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Bamman et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-298"></a>
### [Rank #298] WritingPrompts

- **Global Impact Rank**: `#298` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WritingPrompts`
- **Core NLP Task / Domain**: `Neural Story Generation`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Fan et al., 2018

#### Architectural Specifications & Benchmark Details
Paired 300,000 creative human-written stories with high-concept prompts from Reddit's r/WritingPrompts community (Fan et al., 2018).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Fan et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-309"></a>
### [Rank #309] TimeBank

- **Global Impact Rank**: `#309` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `TimeBank`
- **Core NLP Task / Domain**: `Relation Extraction`
- **Citation Impact**: `~265 (Approx. Index)`
- **Primary Reference & Authors**: Pustejovsky et al., 2003

#### Architectural Specifications & Benchmark Details
The foundational corpus of 183 news articles annotated according to the TimeML specification for events, times, and temporal link relations (Pustejovsky et al., 2003).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Pustejovsky et al., 2003
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-310"></a>
### [Rank #310] TempEval-3

- **Global Impact Rank**: `#310` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `TempEval-3`
- **Core NLP Task / Domain**: `Relation Extraction`
- **Citation Impact**: `~262 (Approx. Index)`
- **Primary Reference & Authors**: UzZaman et al., 2013

#### Architectural Specifications & Benchmark Details
Standardized temporal information extraction datasets (TimeBank + AQUAINT + Silver data) for temporal expression extraction and temporal relation classification (UzZaman et al., 2013).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
UzZaman et al., 2013
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-311"></a>
### [Rank #311] MATRES

- **Global Impact Rank**: `#311` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MATRES`
- **Core NLP Task / Domain**: `Relation Extraction`
- **Citation Impact**: `~260 (Approx. Index)`
- **Primary Reference & Authors**: Ning et al., 2018

#### Architectural Specifications & Benchmark Details
Multi-Axis Temporal Relations dataset achieved significantly higher inter-annotator agreement on temporal ordering by separating main timeline events from hypothetical and conditional axes (Ning et al., 2018).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Ning et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-316"></a>
### [Rank #316] clevr-humans / Compositional Generalization (SCAN)

- **Global Impact Rank**: `#316` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `clevr-humans / Compositional Generalization (SCAN)`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `~248 (Approx. Index)`
- **Primary Reference & Authors**: Lake & Baroni, 2018

#### Architectural Specifications & Benchmark Details
Simplified versions of navigation commands testing zero-shot compositional generalization and systematicity in sequence-to-sequence models (Lake & Baroni, 2018).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Lake & Baroni, 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-317"></a>
### [Rank #317] CFQ (Compositional Freebase Questions)

- **Global Impact Rank**: `#317` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CFQ (Compositional Freebase Questions)`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `~246 (Approx. Index)`
- **Primary Reference & Authors**: Keysers et al., 2020

#### Architectural Specifications & Benchmark Details
Generated realistic natural language questions paired with SPARQL queries specifically partitioned by Maximum Compound Divergence (MCD) to test compositional generalization (Keysers et al., 2020).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Keysers et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-318"></a>
### [Rank #318] COGS

- **Global Impact Rank**: `#318` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `COGS`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `~244 (Approx. Index)`
- **Primary Reference & Authors**: Kim & Linzen, 2020

#### Architectural Specifications & Benchmark Details
Compositional Generalization Challenge based on Semantic Interpretation mapping sentences to lambda-calculus logical forms across structural and lexical generalization splits (Kim & Linzen, 2020).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Kim & Linzen, 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-319"></a>
### [Rank #319] GeoQuery

- **Global Impact Rank**: `#319` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `GeoQuery`
- **Core NLP Task / Domain**: `Text-to-SQL Semantic Parsing`
- **Citation Impact**: `~242 (Approx. Index)`
- **Primary Reference & Authors**: Zelle & Mooney, 1996

#### Architectural Specifications & Benchmark Details
Classic semantic parsing dataset of 880 natural language questions about US geography paired with Prolog and SQL database queries (Zelle & Mooney, 1996).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Zelle & Mooney, 1996
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-323"></a>
### [Rank #323] MTOP

- **Global Impact Rank**: `#323` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MTOP`
- **Core NLP Task / Domain**: `Semantic Parsing & Information Extraction`
- **Citation Impact**: `~232 (Approx. Index)`
- **Primary Reference & Authors**: Li et al., 2021

#### Architectural Specifications & Benchmark Details
Multilingual Task-Oriented Semantic Parsing dataset containing 100,000 compositional hierarchical queries across 6 languages and 11 domains (Li et al., 2021).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Li et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-326"></a>
### [Rank #326] Penn Discourse TreeBank (PDTB 2.0/3.0)

- **Global Impact Rank**: `#326` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Penn Discourse TreeBank (PDTB 2.0/3.0)`
- **Core NLP Task / Domain**: `Discourse Parsing`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Annotated over 1 million words of Wall Street Journal text with explicit and implicit discourse connectives and sense hierarchies (Prasad et al., 2008 / Webber et al., 2019).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-327"></a>
### [Rank #327] RST Discourse Treebank (RST-DT)

- **Global Impact Rank**: `#327` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `RST Discourse Treebank (RST-DT)`
- **Core NLP Task / Domain**: `Rhetorical Structure`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Carlson et al., 2001

#### Architectural Specifications & Benchmark Details
Annotated 385 Wall Street Journal articles with hierarchical Rhetorical Structure Theory trees linking elementary discourse units (Carlson et al., 2001).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Carlson et al., 2001
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-330"></a>
### [Rank #330] GAP

- **Global Impact Rank**: `#330` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `GAP`
- **Core NLP Task / Domain**: `Gender-Balanced Coreference`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Webster et al., 2018

#### Architectural Specifications & Benchmark Details
Annotated 8,608 ambiguous pronoun-name pairs from Wikipedia to evaluate gender bias in coreference resolution (Webster et al., 2018).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Webster et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-332"></a>
### [Rank #332] WikiCoref / ECB+

- **Global Impact Rank**: `#332` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WikiCoref / ECB+`
- **Core NLP Task / Domain**: `Cross-Document Coreference`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Cybulska & Vossen, 2014

#### Architectural Specifications & Benchmark Details
Annotated Event Coreference Bank Plus across news clusters to evaluate within- and cross-document entity and event coreference (Cybulska & Vossen, 2014).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Cybulska & Vossen, 2014
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-333"></a>
### [Rank #333] WNUT-17

- **Global Impact Rank**: `#333` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WNUT-17`
- **Core NLP Task / Domain**: `Emerging & Rare NER`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Derczynski et al., 2017

#### Architectural Specifications & Benchmark Details
Standardized Named Entity Recognition over noisy user-generated social media text focusing on previously unseen surface forms (Derczynski et al., 2017).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Derczynski et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-334"></a>
### [Rank #334] Few-NERD

- **Global Impact Rank**: `#334` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Few-NERD`
- **Core NLP Task / Domain**: `Few-Shot Fine-Grained NER`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Ding et al., 2021

#### Architectural Specifications & Benchmark Details
Annotated 188,200 sentences from Wikipedia with 8 coarse and 66 fine-grained entity types for few-shot NER evaluation (Ding et al., 2021).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Ding et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-335"></a>
### [Rank #335] CrossNER

- **Global Impact Rank**: `#335` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CrossNER`
- **Core NLP Task / Domain**: `Cross-Domain NER`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Liu et al., 2021

#### Architectural Specifications & Benchmark Details
Provided fully labeled NER datasets across five specialized domains (AI, literature, music, politics, natural science) with domain-specific entity hierarchies (Liu et al., 2021).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Liu et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-336"></a>
### [Rank #336] MultiCoNER (v1 / v2)

- **Global Impact Rank**: `#336` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MultiCoNER (v1 / v2)`
- **Core NLP Task / Domain**: `Complex Multilingual NER`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Malmasi et al., 2022

#### Architectural Specifications & Benchmark Details
Large-scale multilingual benchmark for recognizing semantically ambiguous, low-context, and complex named entities (titles, creative works) across 11+ languages (Malmasi et al., 2022).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Malmasi et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-337"></a>
### [Rank #337] AIDA CoNLL-YAGO

- **Global Impact Rank**: `#337` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AIDA CoNLL-YAGO`
- **Core NLP Task / Domain**: `Entity Disambiguation`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Hoffart et al., 2011

#### Architectural Specifications & Benchmark Details
Augmented CoNLL-2003 NER mentions with manual links to YAGO, Wikipedia, and Freebase knowledge base identifiers (Hoffart et al., 2011).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Hoffart et al., 2011
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-338"></a>
### [Rank #338] BLINK / ZESHEL

- **Global Impact Rank**: `#338` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `BLINK / ZESHEL`
- **Core NLP Task / Domain**: `Zero-Shot Entity Linking`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Logeswaran et al., 2019

#### Architectural Specifications & Benchmark Details
Standardized zero-shot entity linking across specialized Wikia domains where test entities are unseen during training and defined only by text descriptions (Logeswaran et al., 2019).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Logeswaran et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-339"></a>
### [Rank #339] MAVEN

- **Global Impact Rank**: `#339` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MAVEN`
- **Core NLP Task / Domain**: `Massive Event Detection`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Wang et al., 2020

#### Architectural Specifications & Benchmark Details
Annotated 4,480 Wikipedia documents with 118,732 event mention instances across 168 event types to resolve data scarcity in event extraction (Wang et al., 2020).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Wang et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-340"></a>
### [Rank #340] RAMS

- **Global Impact Rank**: `#340` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `RAMS`
- **Core NLP Task / Domain**: `Document Event Arguments`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Ebner et al., 2020

#### Architectural Specifications & Benchmark Details
Roles Across Multiple Sentences annotated 9,124 event triggers and argument roles spanning a 5-sentence window around triggers (Ebner et al., 2020).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Ebner et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-341"></a>
### [Rank #341] WikiEvents

- **Global Impact Rank**: `#341` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WikiEvents`
- **Core NLP Task / Domain**: `End-to-End Document IE`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Li et al., 2021

#### Architectural Specifications & Benchmark Details
Provided full document-level event extraction annotations alongside coreferential argument chains and informative trigger spans (Li et al., 2021).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Li et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-342"></a>
### [Rank #342] SciERC

- **Global Impact Rank**: `#342` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SciERC`
- **Core NLP Task / Domain**: `Scientific Knowledge Graph`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Luan et al., 2018

#### Architectural Specifications & Benchmark Details
Annotated 500 scientific abstracts with scientific entities, relations, and coreference clusters to construct automated research knowledge graphs (Luan et al., 2018).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Luan et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-347"></a>
### [Rank #347] SciNLI

- **Global Impact Rank**: `#347` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SciNLI`
- **Core NLP Task / Domain**: `Scientific Text Entailment`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Sadat & Caragea, 2022

#### Architectural Specifications & Benchmark Details
Extracted 107,412 sentence pairs from computational linguistics papers linked by discourse markers for scientific natural language inference (Sadat & Caragea, 2022).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Sadat & Caragea, 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-349"></a>
### [Rank #349] WANLI

- **Global Impact Rank**: `#349` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WANLI`
- **Core NLP Task / Domain**: `Worker-and-AI NLI`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Liu et al., 2022

#### Architectural Specifications & Benchmark Details
Combined GPT-3 generation with human crowdworker filtering and revision to produce 107,000 challenging NLI examples (Liu et al., 2022).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Liu et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-412"></a>
### [Rank #412] SemEval-2024 Task 8 (Multigenerational Machine-Generated Text Detection)

- **Global Impact Rank**: `#412` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2024 Task 8 (Multigenerational Machine-Generated Text Detection)`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `~120 (Approx. Index)`
- **Primary Reference & Authors**: Wang et al., 2024

#### Architectural Specifications & Benchmark Details
Large-scale benchmark dataset containing human vs. LLM-generated text across diverse styles and frontier model families (Wang et al., 2024).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Wang et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-422"></a>
### [Rank #422] SemEval-2025 Task 9 (Automated Argument Synthesis)

- **Global Impact Rank**: `#422` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2025 Task 9 (Automated Argument Synthesis)`
- **Core NLP Task / Domain**: `Named Entity Recognition & Linking`
- **Citation Impact**: `~95 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Counter-argument generation benchmarks evaluating rhetorical structure and persuasion strength.

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-436"></a>
### [Rank #436] CoSQL

- **Global Impact Rank**: `#436` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CoSQL`
- **Core NLP Task / Domain**: `Conversational Text-to-SQL`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Yu et al., 2019

#### Architectural Specifications & Benchmark Details
Cross-domain conversational text-to-SQL benchmark containing 3,000 dialogs and 30,000 turns over 138 databases (Yu et al., 2019).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Yu et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-437"></a>
### [Rank #437] SParC

- **Global Impact Rank**: `#437` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SParC`
- **Core NLP Task / Domain**: `Cross-Domain Semantic Parsing`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Yu et al., 2019

#### Architectural Specifications & Benchmark Details
Collected 4,293 natural language question sequences mapping to complex SQL queries across multiple database schemas (Yu et al., 2019).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Yu et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-446"></a>
### [Rank #446] Mind2Web

- **Global Impact Rank**: `#446` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Mind2Web`
- **Core NLP Task / Domain**: `General Web Agent Eval`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Cheng et al., 2023

#### Architectural Specifications & Benchmark Details
Collected 2,000 open-ended web tasks across 137 domains and 31 websites to test general web navigation (Cheng et al., 2023).

#### Practical Engineering & Research Applications
- **Knowledge Graph Construction**: Extracts structured entity-relation-entity triples and event graphs from unstructured enterprise documents.
- **Conversational Business Intelligence**: Powers Text-to-SQL interfaces enabling non-technical users to query relational databases with natural language.
- **Document Intelligence & Legal Extraction**: Automatically extracts entities, monetary values, dates, and semantic role dependencies from contracts and forms.

#### Reference Citation
```text
Cheng et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

## 4. Engineering Implementation & Pipeline Integration Guide

### Training & Fine-Tuning Recipe
When integrating datasets from **Information Extraction, NER & Semantic Parsing** into modern training pipelines:
1. **Preprocessing & Filtering**: Clean noisy tokens, deduplicate overlapping samples, and ensure context window length fits model architecture.
2. **Loss Function & Masking**: Align training targets with the task specification (e.g. causal masking for autoregressive models, sequence-level loss for classification).
3. **Evaluation Protocol**: Evaluate using official evaluation harnesses (e.g., `lm-evaluation-harness`, `HELM`, or task-specific test suites) to prevent benchmark leakage and prompt overfitting.

[Return to Master Index (`dataset.md`)](../dataset.md)
