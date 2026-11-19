# Summarization & Conversational Dialogue Systems
**Abstractive/Extractive Summarization, Multi-Turn State Tracking & Empathetic Chat**

> **Category Navigation**: [Back to Master Dataset Index](../dataset.md) | Total Benchmarks in Category: **64**

## 1. Domain Overview & Technical Scope
This category encompasses single- and multi-document summarization benchmarks as well as conversational and task-oriented dialogue systems. It includes extreme and headline summarization (XSum, Gigaword), article and meeting condensation (CNN/Daily Mail, QMSum, DialogSum), task-oriented dialogue state tracking (MultiWOZ 2.0–2.4), and persona/empathetic conversational agents (Persona-Chat, DailyDialog, EmpatheticDialogues).

- **Key Applied Focus**: Executive briefing generation, meeting transcription synthesis, conversational commerce agents, automated customer support triage, mental health counseling assistants, and document distillation pipelines.
- **Engineering & Verification Guidance**: Combine n-gram overlap metrics (ROUGE-1/2/L) with factual consistency evaluators (FactCC, QAGS) to prevent hallucinated statements in summaries. For dialogue systems, track Joint Goal Accuracy (JGA) alongside user turn satisfaction.

## 2. Category Quick-Reference Table

| Rank | Dataset / Benchmark | Core Task / Focus | Scholarly Citation Tier | Primary Applications | Details Anchor |
|:---:|:---|:---|:---|:---|:---:|
| `#3` | **MMLU** | Text Summarization | 12,141 (Verified Index) | Executive & News Summarization | [Inspect](#rank-3) |
| `#14` | **CNN / Daily Mail Summarization** | Text Summarization | 4,556 (Verified Index) | Executive & News Summarization | [Inspect](#rank-14) |
| `#26` | **CoQA** | Task-Oriented / Conversational Dialogue | 1,798 (Verified Index) | Executive & News Summarization | [Inspect](#rank-26) |
| `#29` | **QuAC** | Conversational QA | 1,192 (Verified Index) | Executive & News Summarization | [Inspect](#rank-29) |
| `#46` | **MultiWOZ** | Task-Oriented Dialogue | ~1,000 to ~4,500+ (Foundational Benchmark Tier) | Executive & News Summarization | [Inspect](#rank-46) |
| `#70` | **Gigaword** | Text Summarization | ~2,100 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-70) |
| `#71` | **SAMSum** | Task-Oriented / Conversational Dialogue | ~2,050 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-71) |
| `#72` | **Multi-News** | Text Summarization | ~1,950 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-72) |
| `#83` | **Persona-Chat** | Open-Domain Dialogue | ~1,120 to ~1,600 citations | Executive & News Summarization | [Inspect](#rank-83) |
| `#84` | **DailyDialog** | Conversational NLP | ~1,120 to ~1,600 citations | Executive & News Summarization | [Inspect](#rank-84) |
| `#85` | **Ubuntu Dialogue Corpus** | Dialogue Retrieval | ~1,120 to ~1,600 citations | Executive & News Summarization | [Inspect](#rank-85) |
| `#87` | **EmpatheticDialogues** | Affective Computing | ~1,120 to ~1,600 citations | Executive & News Summarization | [Inspect](#rank-87) |
| `#100` | **CLINC150 / Banking77** | Intent Classification | ~1,120 to ~1,600 citations | Executive & News Summarization | [Inspect](#rank-100) |
| `#134` | **SCROLLS** | Long-Context Benchmark | ~860 to ~870 citations | Executive & News Summarization | [Inspect](#rank-134) |
| `#144` | **QMSum** | Meeting Summarization | ~860 to ~870 citations | Executive & News Summarization | [Inspect](#rank-144) |
| `#147` | **Reddit TIFU** | Abstractive Summarization | ~860 to ~870 citations | Executive & News Summarization | [Inspect](#rank-147) |
| `#148` | **WikiHow** | Procedural Summarization | ~860 to ~870 citations | Executive & News Summarization | [Inspect](#rank-148) |
| `#149` | **BookSum** | Literary Summarization | ~860 to ~870 citations | Executive & News Summarization | [Inspect](#rank-149) |
| `#150` | **DialogSum** | Spoken Dialogue Summ. | ~860 to ~870 citations | Executive & News Summarization | [Inspect](#rank-150) |
| `#163` | **Common Voice** | Text Summarization | ~750 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-163) |
| `#179` | **Cornell Movie-Dialogs** | Conversational Modeling | ~550 to ~650 citations | Executive & News Summarization | [Inspect](#rank-179) |
| `#180` | **Topical-Chat** | Knowledge-Grounded Chat | ~550 to ~650 citations | Executive & News Summarization | [Inspect](#rank-180) |
| `#181` | **Wizard of Wikipedia** | Knowledge-Grounded Chat | ~550 to ~650 citations | Executive & News Summarization | [Inspect](#rank-181) |
| `#182` | **ConvAI2** | Dialogue Competition | ~550 to ~650 citations | Executive & News Summarization | [Inspect](#rank-182) |
| `#183` | **SGD (Schema-Guided Dialogue)** | Task-Oriented Dialogue | ~550 to ~650 citations | Executive & News Summarization | [Inspect](#rank-183) |
| `#184` | **Taskmaster-1** | Spoken/Written Dialogue | ~550 to ~650 citations | Executive & News Summarization | [Inspect](#rank-184) |
| `#205` | **UltraChat / UltraFeedback** | Task-Oriented / Conversational Dialogue | ~530 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-205) |
| `#231` | **RotoWire** | Data-to-Text Generation | ~425 to ~430 citations | Executive & News Summarization | [Inspect](#rank-231) |
| `#232` | **E2E NLG Challenge** | Meaning-to-Text Generation | ~425 to ~430 citations | Executive & News Summarization | [Inspect](#rank-232) |
| `#235` | **KILT** | Knowledge-Intensive NLP | ~425 to ~430 citations | Executive & News Summarization | [Inspect](#rank-235) |
| `#254` | **BabelNet** | Text Summarization | ~410 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-254) |
| `#256` | **YAGO** | Text Summarization | ~400 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-256) |
| `#282` | **TVQA** | Video-Subtitle QA | ~300 to ~305 citations | Executive & News Summarization | [Inspect](#rank-282) |
| `#299` | **EMP (Empathetic / Moral Stories)** | Normative Social Reasoning | ~300 to ~305 citations | Executive & News Summarization | [Inspect](#rank-299) |
| `#320` | **ATIS (Air Travel Information System)** | Text Summarization | ~240 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-320) |
| `#321` | **SNIPS** | Text Summarization | ~238 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-321) |
| `#322` | **MASSIVE** | Text Summarization | ~235 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-322) |
| `#324` | **SMCalFlow** | Task-Oriented / Conversational Dialogue | ~230 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-324) |
| `#328` | **STAC** | Multiparty Dialogue Discourse | ~225 to ~228 citations | Executive & News Summarization | [Inspect](#rank-328) |
| `#329` | **Molweni** | Multiparty Reading Comp. | ~225 to ~228 citations | Executive & News Summarization | [Inspect](#rank-329) |
| `#344` | **arXiv / PubMed Long Summarization** | Long-Document Summarization | ~225 to ~228 citations | Executive & News Summarization | [Inspect](#rank-344) |
| `#346` | **SciCite / ACL-ARC** | Citation Intent Classification | ~225 to ~228 citations | Executive & News Summarization | [Inspect](#rank-346) |
| `#374` | **KLUE** | Task-Oriented / Conversational Dialogue | ~180 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-374) |
| `#382` | **MELD** | Multimodal Emotion in Chat | ~150 to ~178 citations | Executive & News Summarization | [Inspect](#rank-382) |
| `#389` | **SUPERB** | Speech Processing Universal | ~150 to ~178 citations | Executive & News Summarization | [Inspect](#rank-389) |
| `#400` | **Empathetic / Counseling (ESConv)** | Emotional Support Dialogue | ~150 to ~178 citations | Executive & News Summarization | [Inspect](#rank-400) |
| `#410` | **SemEval-2024 Task 3 (Multimodal Emotion Cause Analysis)** | Task-Oriented / Conversational Dialogue | ~125 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-410) |
| `#411` | **SemEval-2024 Task 6 (The Legal Eval Challenge)** | Text Summarization | ~122 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-411) |
| `#413` | **SemEval-2024 Task 9 (BRAINTEASER)** | Text Summarization | ~118 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-413) |
| `#418` | **SemEval-2025 Task 5 (Financial Narrative Summarization)** | Text Summarization | ~105 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-418) |
| `#421` | **SemEval-2025 Task 8 (Code-Mixed Conversational Intent Tracking)** | Task-Oriented / Conversational Dialogue | ~98 (Approx. Index) | Executive & News Summarization | [Inspect](#rank-421) |
| `#426` | **MultiWOZ 2.1–2.4** | Task-Oriented Dialogue | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-426) |
| `#427` | **KvRET (Knowledge-Aware Retrieval Dialogue)** | Task-Oriented Dialogue | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-427) |
| `#428` | **Camrest676** | Task-Oriented Dialogue | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-428) |
| `#429` | **WOZ 2.0** | Task-Oriented Dialogue | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-429) |
| `#430` | **Frames Dataset** | Task-Oriented Dialogue | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-430) |
| `#431` | **E-commerce QA / AliMe** | Conversational Commerce | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-431) |
| `#432` | **INSPIRED** | Empathetic Recommendation | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-432) |
| `#433` | **DuConv** | Knowledge-Grounded Dialog | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-433) |
| `#434` | **KdConv** | Multi-Domain Knowledge Dialog | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-434) |
| `#435` | **Mutual** | Multi-Turn Reasoning Dialog | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-435) |
| `#439` | **HyKAS** | Hybrid Knowledge QA | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-439) |
| `#440` | **Simulated Dialogues (Meta-Sim)** | Reinforcement Learning Dialog | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-440) |
| `#444` | **ToolBench Suite** | Multi-Step Tool Execution | ~85 to ~88 citations | Executive & News Summarization | [Inspect](#rank-444) |

---

## 3. Comprehensive Dataset Profiles

<a id="rank-3"></a>
### [Rank #3] MMLU

- **Global Impact Rank**: `#3` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MMLU`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `12,141 (Verified Index)`
- **Primary Reference & Authors**: Hendrycks, D., Burns, C., Basart, S., et al. (2020). Measuring Massive Multitask Language Understanding. arXiv. https://doi.org/10.48550/arxiv.2009.03300

#### Architectural Specifications & Benchmark Details
Measuring Massive Multitask Language Understanding created a 57-subject evaluation benchmark spanning STEM, humanities, and social sciences to test zero-shot and few-shot pretraining knowledge (Hendrycks et al., 2020).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Hendrycks, D., Burns, C., Basart, S., et al. (2020). Measuring Massive Multitask Language Understanding. arXiv. https://doi.org/10.48550/arxiv.2009.03300
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-14"></a>
### [Rank #14] CNN / Daily Mail Summarization

- **Global Impact Rank**: `#14` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CNN / Daily Mail Summarization`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `4,556 (Verified Index)`
- **Primary Reference & Authors**: See, A., Liu, P. J., & Manning, C. D. (2017). Get To The Point: Summarization with Pointer-Generator Networks. arXiv. https://doi.org/10.48550/arxiv.1704.04368

#### Architectural Specifications & Benchmark Details
Formulated the standard multi-sentence abstractive and extractive summarization benchmark setup from news articles paired with story highlights (See et al., 2017).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
See, A., Liu, P. J., & Manning, C. D. (2017). Get To The Point: Summarization with Pointer-Generator Networks. arXiv. https://doi.org/10.48550/arxiv.1704.04368
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-26"></a>
### [Rank #26] CoQA

- **Global Impact Rank**: `#26` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CoQA`
- **Core NLP Task / Domain**: `Task-Oriented / Conversational Dialogue`
- **Citation Impact**: `1,798 (Verified Index)`
- **Primary Reference & Authors**: Reddy, S., Chen, D., & Manning, C. D. (2019). CoQA: A Conversational Question Answering Challenge. TACL, 7, 249-266. https://doi.org/10.1162/tacl_a_00266

#### Architectural Specifications & Benchmark Details
Conversational Question Answering gathered 127,000 questions across 8,000 multi-turn dialogues over text passages across seven domains, featuring free-form answers with extractive rationales (Reddy et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Reddy, S., Chen, D., & Manning, C. D. (2019). CoQA: A Conversational Question Answering Challenge. TACL, 7, 249-266. https://doi.org/10.1162/tacl_a_00266
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-29"></a>
### [Rank #29] QuAC

- **Global Impact Rank**: `#29` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `QuAC`
- **Core NLP Task / Domain**: `Conversational QA`
- **Citation Impact**: `1,192 (Verified Index)`
- **Primary Reference & Authors**: Choi, E., He, H., Iyyer, M., et al. (2018). QuAC: Question Answering in Context. EMNLP 2018. https://doi.org/10.18653/v1/d18-1241

#### Architectural Specifications & Benchmark Details
Collected 100,000 questions across 14,000 asymmetric student-teacher information-seeking dialogues with heavy coreference dependencies (Choi et al., 2018).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Choi, E., He, H., Iyyer, M., et al. (2018). QuAC: Question Answering in Context. EMNLP 2018. https://doi.org/10.18653/v1/d18-1241
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-46"></a>
### [Rank #46] MultiWOZ

- **Global Impact Rank**: `#46` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MultiWOZ`
- **Core NLP Task / Domain**: `Task-Oriented Dialogue`
- **Citation Impact**: `~1,000 to ~4,500+ (Foundational Benchmark Tier)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Collected over 10,000 human-to-human written conversations spanning multiple domains and dialogue states for booking and information tasks.

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-70"></a>
### [Rank #70] Gigaword

- **Global Impact Rank**: `#70` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Gigaword`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `~2,100 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Compiled a massive archive of newswire text data from seven international press agencies, widely utilized for headline generation and sentence compression (Graff et al., 2003 / Napoles et al., 2012).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-71"></a>
### [Rank #71] SAMSum

- **Global Impact Rank**: `#71` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SAMSum`
- **Core NLP Task / Domain**: `Task-Oriented / Conversational Dialogue`
- **Citation Impact**: `~2,050 (Approx. Index)`
- **Primary Reference & Authors**: Gliwa et al., 2019

#### Architectural Specifications & Benchmark Details
Created 16,000 messenger-like chat dialogues written by linguists paired with concise third-person abstractive summaries (Gliwa et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Gliwa et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-72"></a>
### [Rank #72] Multi-News

- **Global Impact Rank**: `#72` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Multi-News`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `~1,950 (Approx. Index)`
- **Primary Reference & Authors**: Fabbri et al., 2019

#### Architectural Specifications & Benchmark Details
Provided the first large-scale dataset for multi-document news summarization, pairing human-written summaries from Newser.com with clusters of source news articles (Fabbri et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Fabbri et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-83"></a>
### [Rank #83] Persona-Chat

- **Global Impact Rank**: `#83` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Persona-Chat`
- **Core NLP Task / Domain**: `Open-Domain Dialogue`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Zhang et al., 2018

#### Architectural Specifications & Benchmark Details
Collected 160,000 utterances between crowdworkers conditioned on explicit 5-sentence persona profiles (Zhang et al., 2018).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Zhang et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-84"></a>
### [Rank #84] DailyDialog

- **Global Impact Rank**: `#84` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DailyDialog`
- **Core NLP Task / Domain**: `Conversational NLP`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Li et al., 2017

#### Architectural Specifications & Benchmark Details
Curated 13,118 high-quality multi-turn dialogues reflecting daily communication annotated with dialogue acts and emotions (Li et al., 2017).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Li et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-85"></a>
### [Rank #85] Ubuntu Dialogue Corpus

- **Global Impact Rank**: `#85` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Ubuntu Dialogue Corpus`
- **Core NLP Task / Domain**: `Dialogue Retrieval`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Lowe et al., 2015

#### Architectural Specifications & Benchmark Details
Extracted nearly 1 million multi-turn technical support logs from Ubuntu IRC channels for next-utterance classification (Lowe et al., 2015).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Lowe et al., 2015
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-87"></a>
### [Rank #87] EmpatheticDialogues

- **Global Impact Rank**: `#87` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `EmpatheticDialogues`
- **Core NLP Task / Domain**: `Affective Computing`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Rashkin et al., 2019

#### Architectural Specifications & Benchmark Details
Gathered 25,000 conversations grounded in specific emotional situations to train empathetic dialogue agents (Rashkin et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Rashkin et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-100"></a>
### [Rank #100] CLINC150 / Banking77

- **Global Impact Rank**: `#100` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CLINC150 / Banking77`
- **Core NLP Task / Domain**: `Intent Classification`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Larson et al., 2019

#### Architectural Specifications & Benchmark Details
Established the standard fine-grained and out-of-scope intent detection benchmarks for commercial conversational assistants (Larson et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Larson et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-134"></a>
### [Rank #134] SCROLLS

- **Global Impact Rank**: `#134` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SCROLLS`
- **Core NLP Task / Domain**: `Long-Context Benchmark`
- **Citation Impact**: `~860 to ~870 citations`
- **Primary Reference & Authors**: Shaham et al., 2022

#### Architectural Specifications & Benchmark Details
Standardized seven natural long-text tasks across summarization, question answering, and natural language inference over thousands of tokens (Shaham et al., 2022).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Shaham et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-144"></a>
### [Rank #144] QMSum

- **Global Impact Rank**: `#144` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `QMSum`
- **Core NLP Task / Domain**: `Meeting Summarization`
- **Citation Impact**: `~860 to ~870 citations`
- **Primary Reference & Authors**: Zhong et al., 2021

#### Architectural Specifications & Benchmark Details
Annotated query-based multi-domain meeting transcripts from product design, academic, and parliamentary committees (Zhong et al., 2021).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Zhong et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-147"></a>
### [Rank #147] Reddit TIFU

- **Global Impact Rank**: `#147` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Reddit TIFU`
- **Core NLP Task / Domain**: `Abstractive Summarization`
- **Citation Impact**: `~860 to ~870 citations`
- **Primary Reference & Authors**: Kim et al., 2019

#### Architectural Specifications & Benchmark Details
Extracted 120,000 informal narrative posts from the r/TIFU subreddit paired with user-written TL;DR summaries (Kim et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Kim et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-148"></a>
### [Rank #148] WikiHow

- **Global Impact Rank**: `#148` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WikiHow`
- **Core NLP Task / Domain**: `Procedural Summarization`
- **Citation Impact**: `~860 to ~870 citations`
- **Primary Reference & Authors**: Koupaee & Wang, 2018

#### Architectural Specifications & Benchmark Details
Compiled 230,000 how-to articles where step-level bolded headers serve as multi-sentence abstractive summaries of instructional paragraphs (Koupaee & Wang, 2018).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Koupaee & Wang, 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-149"></a>
### [Rank #149] BookSum

- **Global Impact Rank**: `#149` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `BookSum`
- **Core NLP Task / Domain**: `Literary Summarization`
- **Citation Impact**: `~860 to ~870 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Aligned books from Project Gutenberg with chapter-level and book-level summaries from CliffsNotes and SparkNotes (Kryściński et al., 2021).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-150"></a>
### [Rank #150] DialogSum

- **Global Impact Rank**: `#150` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DialogSum`
- **Core NLP Task / Domain**: `Spoken Dialogue Summ.`
- **Citation Impact**: `~860 to ~870 citations`
- **Primary Reference & Authors**: Chen et al., 2021

#### Architectural Specifications & Benchmark Details
Provided 13,460 real-life spoken scenario dialogues with manually labeled abstractive summaries and topic tags (Chen et al., 2021).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Chen et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-163"></a>
### [Rank #163] Common Voice

- **Global Impact Rank**: `#163` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Common Voice`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `~750 (Approx. Index)`
- **Primary Reference & Authors**: Ardila et al., 2020

#### Architectural Specifications & Benchmark Details
Mozilla's massive crowdsourced, open-license multilingual transcribed voice corpus spanning over 100 high- and low-resource languages (Ardila et al., 2020).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Ardila et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-179"></a>
### [Rank #179] Cornell Movie-Dialogs

- **Global Impact Rank**: `#179` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Cornell Movie-Dialogs`
- **Core NLP Task / Domain**: `Conversational Modeling`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Danescu-Niculescu-Mizil & Lee, 2011

#### Architectural Specifications & Benchmark Details
Provided 220,579 conversational exchanges between 10,292 pairs of movie characters with metadata (Danescu-Niculescu-Mizil & Lee, 2011).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Danescu-Niculescu-Mizil & Lee, 2011
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-180"></a>
### [Rank #180] Topical-Chat

- **Global Impact Rank**: `#180` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Topical-Chat`
- **Core NLP Task / Domain**: `Knowledge-Grounded Chat`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Gopalakrishnan et al., 2019

#### Architectural Specifications & Benchmark Details
Collected 11,000 human-human conversations grounded in unstructured reading sets across eight broad topics (Gopalakrishnan et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Gopalakrishnan et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-181"></a>
### [Rank #181] Wizard of Wikipedia

- **Global Impact Rank**: `#181` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Wizard of Wikipedia`
- **Core NLP Task / Domain**: `Knowledge-Grounded Chat`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Dinan et al., 2019

#### Architectural Specifications & Benchmark Details
Paired 22,311 open-domain dialogues directly with retrieved Wikipedia sentences selected at each conversational turn (Dinan et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Dinan et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-182"></a>
### [Rank #182] ConvAI2

- **Global Impact Rank**: `#182` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ConvAI2`
- **Core NLP Task / Domain**: `Dialogue Competition`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Dinan et al., 2020

#### Architectural Specifications & Benchmark Details
Standardized the NeurIPS 2018 conversational intelligence challenge dataset combining Persona-Chat with automated and human evaluations (Dinan et al., 2020).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Dinan et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-183"></a>
### [Rank #183] SGD (Schema-Guided Dialogue)

- **Global Impact Rank**: `#183` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SGD (Schema-Guided Dialogue)`
- **Core NLP Task / Domain**: `Task-Oriented Dialogue`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Rastogi et al., 2020

#### Architectural Specifications & Benchmark Details
Released over 20,000 multi-domain conversations across 16 domains to test zero-shot API and schema generalization (Rastogi et al., 2020).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Rastogi et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-184"></a>
### [Rank #184] Taskmaster-1

- **Global Impact Rank**: `#184` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Taskmaster-1`
- **Core NLP Task / Domain**: `Spoken/Written Dialogue`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Byrne et al., 2019

#### Architectural Specifications & Benchmark Details
Collected 13,215 task-based dialogues across six domains using both Wizard-of-Oz spoken turns and self-dialogues (Byrne et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Byrne et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-205"></a>
### [Rank #205] UltraChat / UltraFeedback

- **Global Impact Rank**: `#205` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `UltraChat / UltraFeedback`
- **Core NLP Task / Domain**: `Task-Oriented / Conversational Dialogue`
- **Citation Impact**: `~530 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Released 1.4 million multi-turn instructional dialogues and 64,000 fine-grained AI preference annotations that powered Zephyr and open DPO models (Ding et al., 2023 / Cui et al., 2023).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-231"></a>
### [Rank #231] RotoWire

- **Global Impact Rank**: `#231` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `RotoWire`
- **Core NLP Task / Domain**: `Data-to-Text Generation`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Wiseman et al., 2017

#### Architectural Specifications & Benchmark Details
Paired NBA basketball game box-score statistics tables with full-length professionally written game summaries (Wiseman et al., 2017).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Wiseman et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-232"></a>
### [Rank #232] E2E NLG Challenge

- **Global Impact Rank**: `#232` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `E2E NLG Challenge`
- **Core NLP Task / Domain**: `Meaning-to-Text Generation`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Novikova et al., 2017

#### Architectural Specifications & Benchmark Details
Provided 50,000 crowd-sourced restaurant descriptions mapped to structured dialogue act meaning representations (Novikova et al., 2017).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Novikova et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-235"></a>
### [Rank #235] KILT

- **Global Impact Rank**: `#235` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `KILT`
- **Core NLP Task / Domain**: `Knowledge-Intensive NLP`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Petroni et al., 2021

#### Architectural Specifications & Benchmark Details
Unified 11 datasets across fact-checking, entity linking, slot filling, dialogue, and open-domain QA grounded in a single Wikipedia snapshot (Petroni et al., 2021).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Petroni et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-254"></a>
### [Rank #254] BabelNet

- **Global Impact Rank**: `#254` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `BabelNet`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `~410 (Approx. Index)`
- **Primary Reference & Authors**: Navigli & Ponzetto, 2012

#### Architectural Specifications & Benchmark Details
Merged WordNet with Wikipedia, Wikidata, and OmegaWiki into a massive multilingual encyclopedic dictionary and semantic network (Navigli & Ponzetto, 2012).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Navigli & Ponzetto, 2012
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-256"></a>
### [Rank #256] YAGO

- **Global Impact Rank**: `#256` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `YAGO`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `~400 (Approx. Index)`
- **Primary Reference & Authors**: Suchanek et al., 2007

#### Architectural Specifications & Benchmark Details
Extracted a massive semantic knowledge base from Wikipedia, WordNet, and GeoNames with over 10 million entities and 120 million facts (Suchanek et al., 2007).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Suchanek et al., 2007
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-282"></a>
### [Rank #282] TVQA

- **Global Impact Rank**: `#282` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `TVQA`
- **Core NLP Task / Domain**: `Video-Subtitle QA`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Lei et al., 2018

#### Architectural Specifications & Benchmark Details
Built 152,545 multiple-choice questions grounded in both video frames and aligned character dialogue subtitles across six TV shows (Lei et al., 2018).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Lei et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-299"></a>
### [Rank #299] EMP (Empathetic / Moral Stories)

- **Global Impact Rank**: `#299` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `EMP (Empathetic / Moral Stories)`
- **Core NLP Task / Domain**: `Normative Social Reasoning`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Emelin et al., 2021

#### Architectural Specifications & Benchmark Details
Structured crowd-sourced narratives testing goal-directed social reasoning conditioned on moral norms and consequences (Emelin et al., 2021).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Emelin et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-320"></a>
### [Rank #320] ATIS (Air Travel Information System)

- **Global Impact Rank**: `#320` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ATIS (Air Travel Information System)`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `~240 (Approx. Index)`
- **Primary Reference & Authors**: Hemphill et al., 1990

#### Architectural Specifications & Benchmark Details
Foundational spoken and written language understanding corpus for flight booking intent detection and slot filling (Hemphill et al., 1990).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Hemphill et al., 1990
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-321"></a>
### [Rank #321] SNIPS

- **Global Impact Rank**: `#321` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SNIPS`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `~238 (Approx. Index)`
- **Primary Reference & Authors**: Coucke et al., 2018

#### Architectural Specifications & Benchmark Details
Crowdsourced voice assistant benchmark covering seven commercial intent domains (music, weather, restaurant booking, movie schedules) for NLU slot filling (Coucke et al., 2018).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Coucke et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-322"></a>
### [Rank #322] MASSIVE

- **Global Impact Rank**: `#322` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MASSIVE`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `~235 (Approx. Index)`
- **Primary Reference & Authors**: FitzGerald et al., 2023

#### Architectural Specifications & Benchmark Details
Multilingual Amazon Slu Resource Package localized 1 million realistic virtual assistant utterances across 51 languages with slot and intent annotations (FitzGerald et al., 2023).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
FitzGerald et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-324"></a>
### [Rank #324] SMCalFlow

- **Global Impact Rank**: `#324` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SMCalFlow`
- **Core NLP Task / Domain**: `Task-Oriented / Conversational Dialogue`
- **Citation Impact**: `~230 (Approx. Index)`
- **Primary Reference & Authors**: Andreas et al., 2020

#### Architectural Specifications & Benchmark Details
Task-oriented dialogue dataset featuring 41,000 multi-turn calendar, weather, people, and place conversations annotated with executable dataflow programs (Andreas et al., 2020).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Andreas et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-328"></a>
### [Rank #328] STAC

- **Global Impact Rank**: `#328` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `STAC`
- **Core NLP Task / Domain**: `Multiparty Dialogue Discourse`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Asher et al., 2016

#### Architectural Specifications & Benchmark Details
Annotated strategic chat negotiations from The Settlers of Catan with Segmented Discourse Representation Theory (SDRT) graphs (Asher et al., 2016).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Asher et al., 2016
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-329"></a>
### [Rank #329] Molweni

- **Global Impact Rank**: `#329` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Molweni`
- **Core NLP Task / Domain**: `Multiparty Reading Comp.`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Li et al., 2020

#### Architectural Specifications & Benchmark Details
Built 10,000 discourse-annotated multiparty dialogues derived from the Ubuntu Chat Corpus with extractive QA pairs (Li et al., 2020).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Li et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-344"></a>
### [Rank #344] arXiv / PubMed Long Summarization

- **Global Impact Rank**: `#344` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `arXiv / PubMed Long Summarization`
- **Core NLP Task / Domain**: `Long-Document Summarization`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Cohan et al., 2018

#### Architectural Specifications & Benchmark Details
Standardized full-text scientific paper datasets paired with abstracts to test discourse-aware long-sequence summarization (Cohan et al., 2018).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Cohan et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-346"></a>
### [Rank #346] SciCite / ACL-ARC

- **Global Impact Rank**: `#346` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SciCite / ACL-ARC`
- **Core NLP Task / Domain**: `Citation Intent Classification`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Annotated citation contexts in scientific papers by rhetorical intent (background, method, result comparison) (Cohan et al., 2019 / Jurgens et al., 2018).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-374"></a>
### [Rank #374] KLUE

- **Global Impact Rank**: `#374` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `KLUE`
- **Core NLP Task / Domain**: `Task-Oriented / Conversational Dialogue`
- **Citation Impact**: `~180 (Approx. Index)`
- **Primary Reference & Authors**: Park et al., 2021

#### Architectural Specifications & Benchmark Details
Korean Language Understanding Evaluation benchmark spanning 8 diverse tasks including dependency parsing, NER, relation extraction, and dialogue state tracking (Park et al., 2021).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Park et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-382"></a>
### [Rank #382] MELD

- **Global Impact Rank**: `#382` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MELD`
- **Core NLP Task / Domain**: `Multimodal Emotion in Chat`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Poria et al., 2019

#### Architectural Specifications & Benchmark Details
Multimodal EmotionLines Dataset containing 13,000 utterances from Friends TV dialogues with audio, visual, and text emotion annotations (Poria et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Poria et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-389"></a>
### [Rank #389] SUPERB

- **Global Impact Rank**: `#389` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SUPERB`
- **Core NLP Task / Domain**: `Speech Processing Universal`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Yang et al., 2021

#### Architectural Specifications & Benchmark Details
Standardized benchmark evaluating self-supervised speech representations across 10+ tasks including ASR, intent classification, and slot filling (Yang et al., 2021).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Yang et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-400"></a>
### [Rank #400] Empathetic / Counseling (ESConv)

- **Global Impact Rank**: `#400` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Empathetic / Counseling (ESConv)`
- **Core NLP Task / Domain**: `Emotional Support Dialogue`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Liu et al., 2021

#### Architectural Specifications & Benchmark Details
Emotional Support Conversation dataset annotated with helping skills and multi-turn support strategies grounded in psychological theory (Liu et al., 2021).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Liu et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-410"></a>
### [Rank #410] SemEval-2024 Task 3 (Multimodal Emotion Cause Analysis)

- **Global Impact Rank**: `#410` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2024 Task 3 (Multimodal Emotion Cause Analysis)`
- **Core NLP Task / Domain**: `Task-Oriented / Conversational Dialogue`
- **Citation Impact**: `~125 (Approx. Index)`
- **Primary Reference & Authors**: Ghosal et al., 2024

#### Architectural Specifications & Benchmark Details
Collected conversational and visual dialogues annotated with causal triggers for emotional reactions (Ghosal et al., 2024).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Ghosal et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-411"></a>
### [Rank #411] SemEval-2024 Task 6 (The Legal Eval Challenge)

- **Global Impact Rank**: `#411` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2024 Task 6 (The Legal Eval Challenge)`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `~122 (Approx. Index)`
- **Primary Reference & Authors**: Chalkidis et al., 2024

#### Architectural Specifications & Benchmark Details
Standardized multi-lingual legal judgment prediction, court decision summarization, and statute mapping (Chalkidis et al., 2024).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Chalkidis et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-413"></a>
### [Rank #413] SemEval-2024 Task 9 (BRAINTEASER)

- **Global Impact Rank**: `#413` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2024 Task 9 (BRAINTEASER)`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `~118 (Approx. Index)`
- **Primary Reference & Authors**: Jiang et al., 2024

#### Architectural Specifications & Benchmark Details
Lateral thinking and trick reasoning questions that trap models relying on literal surface-level statistical associations (Jiang et al., 2024).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Jiang et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-418"></a>
### [Rank #418] SemEval-2025 Task 5 (Financial Narrative Summarization)

- **Global Impact Rank**: `#418` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2025 Task 5 (Financial Narrative Summarization)`
- **Core NLP Task / Domain**: `Text Summarization`
- **Citation Impact**: `~105 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Long-document corporate filing summarization under strict numerical and factual fidelity constraints.

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-421"></a>
### [Rank #421] SemEval-2025 Task 8 (Code-Mixed Conversational Intent Tracking)

- **Global Impact Rank**: `#421` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2025 Task 8 (Code-Mixed Conversational Intent Tracking)`
- **Core NLP Task / Domain**: `Task-Oriented / Conversational Dialogue`
- **Citation Impact**: `~98 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Multi-turn conversational intent tracking benchmarks across South Asian code-mixed dialogues.

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-426"></a>
### [Rank #426] MultiWOZ 2.1–2.4

- **Global Impact Rank**: `#426` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MultiWOZ 2.1–2.4`
- **Core NLP Task / Domain**: `Task-Oriented Dialogue`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Cleaned and corrected state-tracking dialogue versions of the MultiWOZ multi-domain booking benchmark (Eric et al., 2020 / Ye et al., 2022).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-427"></a>
### [Rank #427] KvRET (Knowledge-Aware Retrieval Dialogue)

- **Global Impact Rank**: `#427` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `KvRET (Knowledge-Aware Retrieval Dialogue)`
- **Core NLP Task / Domain**: `Task-Oriented Dialogue`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Eric et al., 2017

#### Architectural Specifications & Benchmark Details
Collected 3,000 multi-turn dialogs grounded in structured calendar, weather, and ride-sharing knowledge bases (Eric et al., 2017).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Eric et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-428"></a>
### [Rank #428] Camrest676

- **Global Impact Rank**: `#428` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Camrest676`
- **Core NLP Task / Domain**: `Task-Oriented Dialogue`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Young et al., 2013

#### Architectural Specifications & Benchmark Details
Simplified restaurant search and booking dialogue corpus used for early slot-filling and dialog state tracking (Young et al., 2013).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Young et al., 2013
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-429"></a>
### [Rank #429] WOZ 2.0

- **Global Impact Rank**: `#429` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WOZ 2.0`
- **Core NLP Task / Domain**: `Task-Oriented Dialogue`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Mrksic et al., 2017

#### Architectural Specifications & Benchmark Details
Single-domain restaurant reservation dialogue corpus designed to evaluate dialogue state tracking accuracy (Mrksic et al., 2017).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Mrksic et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-430"></a>
### [Rank #430] Frames Dataset

- **Global Impact Rank**: `#430` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Frames Dataset`
- **Core NLP Task / Domain**: `Task-Oriented Dialogue`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: El Asri et al., 2017

#### Architectural Specifications & Benchmark Details
1,369 complex hotel and flight travel planning multi-turn dialogs involving database modifications (El Asri et al., 2017).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
El Asri et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-431"></a>
### [Rank #431] E-commerce QA / AliMe

- **Global Impact Rank**: `#431` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `E-commerce QA / AliMe`
- **Core NLP Task / Domain**: `Conversational Commerce`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Huang et al., 2019

#### Architectural Specifications & Benchmark Details
Massive-scale customer service dialogue datasets from e-commerce platforms handling user intent matching (Huang et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Huang et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-432"></a>
### [Rank #432] INSPIRED

- **Global Impact Rank**: `#432` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `INSPIRED`
- **Core NLP Task / Domain**: `Empathetic Recommendation`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Rebuffel et al., 2022

#### Architectural Specifications & Benchmark Details
Collected 1,000 human-human movie recommendation dialogues incorporating persuasive and empathetic conversational strategies (Rebuffel et al., 2022).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Rebuffel et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-433"></a>
### [Rank #433] DuConv

- **Global Impact Rank**: `#433` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DuConv`
- **Core NLP Task / Domain**: `Knowledge-Grounded Dialog`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Wu et al., 2019

#### Architectural Specifications & Benchmark Details
Built 30,000 Chinese conversational dialogues flowing naturally from entity knowledge graph paths (Wu et al., 2019).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Wu et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-434"></a>
### [Rank #434] KdConv

- **Global Impact Rank**: `#434` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `KdConv`
- **Core NLP Task / Domain**: `Multi-Domain Knowledge Dialog`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Zhou et al., 2020

#### Architectural Specifications & Benchmark Details
Curated Chinese knowledge-driven conversational dataset spanning movies, music, and travel (Zhou et al., 2020).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Zhou et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-435"></a>
### [Rank #435] Mutual

- **Global Impact Rank**: `#435` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Mutual`
- **Core NLP Task / Domain**: `Multi-Turn Reasoning Dialog`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Cui et al., 2020

#### Architectural Specifications & Benchmark Details
Chinese multi-turn dialogue dataset where models must select the correct next response requiring complex reasoning (Cui et al., 2020).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Cui et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-439"></a>
### [Rank #439] HyKAS

- **Global Impact Rank**: `#439` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `HyKAS`
- **Core NLP Task / Domain**: `Hybrid Knowledge QA`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Li et al., 2020

#### Architectural Specifications & Benchmark Details
Knowledge-grounded dialogue dataset integrating structured facts and unstructured passages for dialogue response generation (Li et al., 2020).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Li et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-440"></a>
### [Rank #440] Simulated Dialogues (Meta-Sim)

- **Global Impact Rank**: `#440` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Simulated Dialogues (Meta-Sim)`
- **Core NLP Task / Domain**: `Reinforcement Learning Dialog`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Schatzmann et al., 2007

#### Architectural Specifications & Benchmark Details
Synthetic simulation framework environments for training goal-oriented dialogue policies via RL (Schatzmann et al., 2007).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Schatzmann et al., 2007
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-444"></a>
### [Rank #444] ToolBench Suite

- **Global Impact Rank**: `#444` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ToolBench Suite`
- **Core NLP Task / Domain**: `Multi-Step Tool Execution`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Qin et al., 2023

#### Architectural Specifications & Benchmark Details
Massive collection of open-source REST APIs structured for complex agentic workflow planning (Qin et al., 2023).

#### Practical Engineering & Research Applications
- **Executive & News Summarization**: Condenses long articles, meeting transcripts, and corporate releases into concise abstractive summaries.
- **Task-Oriented Conversational Systems**: Powers multi-turn reservation, booking, and customer service bots with rigorous dialogue state tracking.
- **Empathetic & Persona-Based Chat**: Trains virtual companions, conversational tutors, and mental health support bots to maintain consistent tone.

#### Reference Citation
```text
Qin et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

## 4. Engineering Implementation & Pipeline Integration Guide

### Training & Fine-Tuning Recipe
When integrating datasets from **Summarization & Conversational Dialogue Systems** into modern training pipelines:
1. **Preprocessing & Filtering**: Clean noisy tokens, deduplicate overlapping samples, and ensure context window length fits model architecture.
2. **Loss Function & Masking**: Align training targets with the task specification (e.g. causal masking for autoregressive models, sequence-level loss for classification).
3. **Evaluation Protocol**: Evaluate using official evaluation harnesses (e.g., `lm-evaluation-harness`, `HELM`, or task-specific test suites) to prevent benchmark leakage and prompt overfitting.

[Return to Master Index (`dataset.md`)](../dataset.md)
