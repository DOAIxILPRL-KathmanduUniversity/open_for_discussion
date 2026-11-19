# Domain-Specific NLP: Biomedical, Legal, Finance & Scholarly IR/RAG
**Clinical EHRs, Legal Contract Reasoning, Financial Filings & Scientific Fact Verification**

> **Category Navigation**: [Back to Master Dataset Index](../dataset.md) | Total Benchmarks in Category: **38**

## 1. Domain Overview & Technical Scope
This category is dedicated to high-stakes vertical domains that demand specialized terminology, strict factual fidelity, and rigorous citation grounding. It includes clinical electronic health records and medical licensing (PubMedQA, MedQA, MIMIC-III/IV), legal case law and contracts (LexGLUE, CUAD, CaseHOLD, ContractNLI), financial report QA (FinQA, TAT-QA), scholarly literature mining (ScienceQA, S2ORC, QASPER), and state-of-the-art information retrieval and RAG benchmarking (MS MARCO, BEIR, FEVER, RAGAS).

- **Key Applied Focus**: Clinical decision support systems, legal contract risk auditing, automated financial equity research, scholarly literature meta-analysis, and enterprise enterprise-grade Retrieval-Augmented Generation (RAG).
- **Engineering & Verification Guidance**: Enforce retrieval grounding and reference attribution. In medical and legal deployments, configure high-temperature rejection thresholds to abstain on uncertain responses and require verifiable inline source citations.

## 2. Category Quick-Reference Table

| Rank | Dataset / Benchmark | Core Task / Focus | Scholarly Citation Tier | Primary Applications | Details Anchor |
|:---:|:---|:---|:---|:---|:---:|
| `#19` | **FEVER** | Domain-Specific Retrieval & Verification | 3,349 (Verified Index) | Clinical & Medical Decision Support | [Inspect](#rank-19) |
| `#24` | **MS MARCO** | Domain-Specific Retrieval & Verification | 2,466 (Verified Index) | Clinical & Medical Decision Support | [Inspect](#rank-24) |
| `#33` | **ScienceQA** | Scholarly QA | 288 (Verified Index) | Clinical & Medical Decision Support | [Inspect](#rank-33) |
| `#47` | **BEIR** | Zero-Shot Information Retrieval | ~1,000 to ~4,500+ (Foundational Benchmark Tier) | Clinical & Medical Decision Support | [Inspect](#rank-47) |
| `#96` | **PubMedQA** | Biomedical QA | ~1,120 to ~1,600 citations | Clinical & Medical Decision Support | [Inspect](#rank-96) |
| `#97` | **MedQA (USMLE)** | Clinical NLP | ~1,120 to ~1,600 citations | Clinical & Medical Decision Support | [Inspect](#rank-97) |
| `#98` | **S2ORC** | Scholarly NLP | ~1,120 to ~1,600 citations | Clinical & Medical Decision Support | [Inspect](#rank-98) |
| `#133` | **QASPER** | Scientific Document QA | ~860 to ~870 citations | Clinical & Medical Decision Support | [Inspect](#rank-133) |
| `#145` | **GovReport** | Long-Report Summarization | ~860 to ~870 citations | Clinical & Medical Decision Support | [Inspect](#rank-145) |
| `#146` | **BillSum** | Legislative Summarization | ~860 to ~870 citations | Clinical & Medical Decision Support | [Inspect](#rank-146) |
| `#189` | **LIAR** | Fake News Detection | ~550 to ~650 citations | Clinical & Medical Decision Support | [Inspect](#rank-189) |
| `#190` | **FakeNewsNet** | Misinformation & Social | ~550 to ~650 citations | Clinical & Medical Decision Support | [Inspect](#rank-190) |
| `#191` | **SciFact** | Scientific Claim Verif. | ~550 to ~650 citations | Clinical & Medical Decision Support | [Inspect](#rank-191) |
| `#192` | **VitaminC** | Contrastive Fact Verif. | ~550 to ~650 citations | Clinical & Medical Decision Support | [Inspect](#rank-192) |
| `#196` | **NCBI Disease Corpus** | Biomedical Entity Linking | ~550 to ~650 citations | Clinical & Medical Decision Support | [Inspect](#rank-196) |
| `#198` | **CORD-19** | Epidemic Scholarly Corpus | ~550 to ~650 citations | Clinical & Medical Decision Support | [Inspect](#rank-198) |
| `#200` | **FinQA /LexGLUE** | Domain-Specific Reasoning | ~550 to ~650 citations | Clinical & Medical Decision Support | [Inspect](#rank-200) |
| `#226` | **TabFact** | Table Fact Verification | ~425 to ~430 citations | Clinical & Medical Decision Support | [Inspect](#rank-226) |
| `#230` | **TAT-QA** | Financial Table+Text QA | ~425 to ~430 citations | Clinical & Medical Decision Support | [Inspect](#rank-230) |
| `#236` | **TREC-CAR** | Complex Answer Retrieval | ~425 to ~430 citations | Clinical & Medical Decision Support | [Inspect](#rank-236) |
| `#237` | **NFCorpus** | Biomedical Information Ret. | ~425 to ~430 citations | Clinical & Medical Decision Support | [Inspect](#rank-237) |
| `#240` | **Touché-2020** | Argument Retrieval | ~425 to ~430 citations | Clinical & Medical Decision Support | [Inspect](#rank-240) |
| `#244` | **HoVer** | Multi-Hop Fact Verification | ~425 to ~430 citations | Clinical & Medical Decision Support | [Inspect](#rank-244) |
| `#245` | **FEVEROUS** | Structured + Text Verification | ~425 to ~430 citations | Clinical & Medical Decision Support | [Inspect](#rank-245) |
| `#246` | **AVeriTeC** | Real-World Fact-Checking | ~425 to ~430 citations | Clinical & Medical Decision Support | [Inspect](#rank-246) |
| `#250` | **RAGAS /ARES Eval Sets** | RAG Pipeline Benchmarking | ~425 to ~430 citations | Clinical & Medical Decision Support | [Inspect](#rank-250) |
| `#286` | **MIMIC-III / MIMIC-IV Notes** | Clinical NLP | ~300 to ~305 citations | Clinical & Medical Decision Support | [Inspect](#rank-286) |
| `#288` | **MedMCQA** | Medical Entrance QA | ~300 to ~305 citations | Clinical & Medical Decision Support | [Inspect](#rank-288) |
| `#289` | **ChemProt / DDI Corpus** | Pharmacovigilance IE | ~300 to ~305 citations | Clinical & Medical Decision Support | [Inspect](#rank-289) |
| `#290` | **CUAD** | Legal Contract Review | ~300 to ~305 citations | Clinical & Medical Decision Support | [Inspect](#rank-290) |
| `#291` | **CaseHOLD / Pile of Law** | Legal Pretraining & Holdings | ~300 to ~305 citations | Clinical & Medical Decision Support | [Inspect](#rank-291) |
| `#295` | **IBM Debater Datasets** | Computational Argumentation | ~300 to ~305 citations | Clinical & Medical Decision Support | [Inspect](#rank-295) |
| `#300` | **ACL Anthology Network / OCL** | Scholarly Bibliometrics | ~300 to ~305 citations | Clinical & Medical Decision Support | [Inspect](#rank-300) |
| `#345` | **PeerRead** | Computational Peer Review | ~225 to ~228 citations | Clinical & Medical Decision Support | [Inspect](#rank-345) |
| `#348` | **SciTail** | Science Exam Entailment | ~225 to ~228 citations | Clinical & Medical Decision Support | [Inspect](#rank-348) |
| `#350` | **ContractNLI** | Document-Level Legal NLI | ~225 to ~228 citations | Clinical & Medical Decision Support | [Inspect](#rank-350) |
| `#399` | **dreaddit / CLPsych Shared Tasks** | Mental Health NLP | ~150 to ~178 citations | Clinical & Medical Decision Support | [Inspect](#rank-399) |
| `#474` | **Early Modern English Medical Texts** | Domain-Specific Retrieval & Verification | ~28 (Approx. Index) | Clinical & Medical Decision Support | [Inspect](#rank-474) |

---

## 3. Comprehensive Dataset Profiles

<a id="rank-19"></a>
### [Rank #19] FEVER

- **Global Impact Rank**: `#19` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `FEVER`
- **Core NLP Task / Domain**: `Domain-Specific Retrieval & Verification`
- **Citation Impact**: `3,349 (Verified Index)`
- **Primary Reference & Authors**: Thorne, J., Vlachos, A., Christodoulopoulos, C., & Mittal, A. (2018). FEVER: a Large-scale Dataset for Fact Extraction and VERification. NAACL 2018. https://doi.org/10.18653/v1/n18-1074

#### Architectural Specifications & Benchmark Details
Fact Extraction and VERification generated 185,445 claims by mutating Wikipedia sentences, requiring systems to retrieve evidentiary sentences and classify claims as supported, refuted, or not enough info (Thorne et al., 2018).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Thorne, J., Vlachos, A., Christodoulopoulos, C., & Mittal, A. (2018). FEVER: a Large-scale Dataset for Fact Extraction and VERification. NAACL 2018. https://doi.org/10.18653/v1/n18-1074
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-24"></a>
### [Rank #24] MS MARCO

- **Global Impact Rank**: `#24` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MS MARCO`
- **Core NLP Task / Domain**: `Domain-Specific Retrieval & Verification`
- **Citation Impact**: `2,466 (Verified Index)`
- **Primary Reference & Authors**: Bajaj, P., Campos, D., Craswell, N., et al. (2016). MS MARCO: A Human Generated MAchine Reading COmprehension Dataset. arXiv. https://doi.org/10.48550/arxiv.1611.09268

#### Architectural Specifications & Benchmark Details
Released 100,000 real Bing search queries with 1 million retrieved web passages and human-synthesized free-form answers, becoming the foundational dataset for neural passage ranking and dense retrieval (Bajaj et al., 2016).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Bajaj, P., Campos, D., Craswell, N., et al. (2016). MS MARCO: A Human Generated MAchine Reading COmprehension Dataset. arXiv. https://doi.org/10.48550/arxiv.1611.09268
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-33"></a>
### [Rank #33] ScienceQA

- **Global Impact Rank**: `#33` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ScienceQA`
- **Core NLP Task / Domain**: `Scholarly QA`
- **Citation Impact**: `288 (Verified Index)`
- **Primary Reference & Authors**: Saikh, T., Ghosal, T., Mittal, A., Ekbal, A., & Bhattacharyya, P. (2022). ScienceQA: a novel resource for question answering on scholarly articles. IJDL 23, 289-301. https://doi.org/10.1007/s00799-022-00329-y

#### Architectural Specifications & Benchmark Details
Developed a benchmark dataset for generating and answering factoid and non-factoid questions over academic articles (Saikh et al., 2022).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Saikh, T., Ghosal, T., Mittal, A., Ekbal, A., & Bhattacharyya, P. (2022). ScienceQA: a novel resource for question answering on scholarly articles. IJDL 23, 289-301. https://doi.org/10.1007/s00799-022-00329-y
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-47"></a>
### [Rank #47] BEIR

- **Global Impact Rank**: `#47` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `BEIR`
- **Core NLP Task / Domain**: `Zero-Shot Information Retrieval`
- **Citation Impact**: `~1,000 to ~4,500+ (Foundational Benchmark Tier)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Unified 18 diverse retrieval datasets across nine tasks (fact-checking, bio-IR, argument retrieval) for out-of-distribution evaluation.

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-96"></a>
### [Rank #96] PubMedQA

- **Global Impact Rank**: `#96` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `PubMedQA`
- **Core NLP Task / Domain**: `Biomedical QA`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Jin et al., 2019

#### Architectural Specifications & Benchmark Details
Annotated 1,000 expert-labeled and 211,000 artificially generated biomedical research questions answered with yes/no/maybe over PubMed abstracts (Jin et al., 2019).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Jin et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-97"></a>
### [Rank #97] MedQA (USMLE)

- **Global Impact Rank**: `#97` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MedQA (USMLE)`
- **Core NLP Task / Domain**: `Clinical NLP`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Jin et al., 2021

#### Architectural Specifications & Benchmark Details
Collected multilingual multiple-choice medical board examination questions from the US, Mainland China, and Taiwan (Jin et al., 2021).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Jin et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-98"></a>
### [Rank #98] S2ORC

- **Global Impact Rank**: `#98` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `S2ORC`
- **Core NLP Task / Domain**: `Scholarly NLP`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Lo et al., 2020

#### Architectural Specifications & Benchmark Details
Released a 81.1-million English academic paper graph with structured full text, inline citations, and PDF parses (Lo et al., 2020).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Lo et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-133"></a>
### [Rank #133] QASPER

- **Global Impact Rank**: `#133` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `QASPER`
- **Core NLP Task / Domain**: `Scientific Document QA`
- **Citation Impact**: `~860 to ~870 citations`
- **Primary Reference & Authors**: Dasigi et al., 2021

#### Architectural Specifications & Benchmark Details
Created 5,049 information-seeking questions over 1,585 full-text NLP research papers written by domain practitioners (Dasigi et al., 2021).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Dasigi et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-145"></a>
### [Rank #145] GovReport

- **Global Impact Rank**: `#145` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `GovReport`
- **Core NLP Task / Domain**: `Long-Report Summarization`
- **Citation Impact**: `~860 to ~870 citations`
- **Primary Reference & Authors**: Huang et al., 2021

#### Architectural Specifications & Benchmark Details
Paired 19,466 lengthy U.S. Government Accountability Office and Congressional Research Service reports with expert-written executive summaries (Huang et al., 2021).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Huang et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-146"></a>
### [Rank #146] BillSum

- **Global Impact Rank**: `#146` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `BillSum`
- **Core NLP Task / Domain**: `Legislative Summarization`
- **Citation Impact**: `~860 to ~870 citations`
- **Primary Reference & Authors**: Kornilova & Eidelman, 2019

#### Architectural Specifications & Benchmark Details
Gathered 22,218 US Congressional and California state bills with reference human summaries to test complex legal structure extraction (Kornilova & Eidelman, 2019).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Kornilova & Eidelman, 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-189"></a>
### [Rank #189] LIAR

- **Global Impact Rank**: `#189` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `LIAR`
- **Core NLP Task / Domain**: `Fake News Detection`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Wang, 2017

#### Architectural Specifications & Benchmark Details
Collected 12,836 short political statements from PolitiFact.com labeled on a six-grade truthfulness scale with speaker metadata (Wang, 2017).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Wang, 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-190"></a>
### [Rank #190] FakeNewsNet

- **Global Impact Rank**: `#190` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `FakeNewsNet`
- **Core NLP Task / Domain**: `Misinformation & Social`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Shu et al., 2020

#### Architectural Specifications & Benchmark Details
Aggregated news content, spatiotemporal social context, and user engagement dynamics from PolitiFact and GossipCop (Shu et al., 2020).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Shu et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-191"></a>
### [Rank #191] SciFact

- **Global Impact Rank**: `#191` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SciFact`
- **Core NLP Task / Domain**: `Scientific Claim Verif.`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Wadden et al., 2020

#### Architectural Specifications & Benchmark Details
Created 1,409 expert-written scientific claims paired with PubMed abstracts annotated with veracity labels and sentence-level rationales (Wadden et al., 2020).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Wadden et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-192"></a>
### [Rank #192] VitaminC

- **Global Impact Rank**: `#192` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `VitaminC`
- **Core NLP Task / Domain**: `Contrastive Fact Verif.`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Schuster et al., 2021

#### Architectural Specifications & Benchmark Details
Gathered 447,000 contrastive claim-evidence pairs derived from real-world Wikipedia revisions where factual details changed (Schuster et al., 2021).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Schuster et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-196"></a>
### [Rank #196] NCBI Disease Corpus

- **Global Impact Rank**: `#196` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `NCBI Disease Corpus`
- **Core NLP Task / Domain**: `Biomedical Entity Linking`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Fully annotated 793 PubMed abstracts with 6,892 disease mentions mapped to MeSH and OMIM concept identifiers (Doğan et al., 2014).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-198"></a>
### [Rank #198] CORD-19

- **Global Impact Rank**: `#198` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CORD-19`
- **Core NLP Task / Domain**: `Epidemic Scholarly Corpus`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Wang et al., 2020

#### Architectural Specifications & Benchmark Details
Assembled over 1 million scholarly articles on COVID-19 and historical coronaviruses for literature discovery and biomedical QA (Wang et al., 2020).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Wang et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-200"></a>
### [Rank #200] FinQA /LexGLUE

- **Global Impact Rank**: `#200` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `FinQA /LexGLUE`
- **Core NLP Task / Domain**: `Domain-Specific Reasoning`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Chalkidis et al., 2022

#### Architectural Specifications & Benchmark Details
Established numerical reasoning over financial reports (Chen et al., 2021) and unified multi-task legal language understanding (Chalkidis et al., 2022).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Chalkidis et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-226"></a>
### [Rank #226] TabFact

- **Global Impact Rank**: `#226` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `TabFact`
- **Core NLP Task / Domain**: `Table Fact Verification`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Chen et al., 2020

#### Architectural Specifications & Benchmark Details
Collected 118,000 natural language statements annotated as entailed or refuted against 16,000 Wikipedia tables (Chen et al., 2020).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Chen et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-230"></a>
### [Rank #230] TAT-QA

- **Global Impact Rank**: `#230` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `TAT-QA`
- **Core NLP Task / Domain**: `Financial Table+Text QA`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Zhu et al., 2021

#### Architectural Specifications & Benchmark Details
Built 16,552 questions over real-world hybrid financial reports requiring numerical reasoning alongside span extraction (Zhu et al., 2021).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Zhu et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-236"></a>
### [Rank #236] TREC-CAR

- **Global Impact Rank**: `#236` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `TREC-CAR`
- **Core NLP Task / Domain**: `Complex Answer Retrieval`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Dietz et al., 2017

#### Architectural Specifications & Benchmark Details
Synthesized millions of hierarchical outline queries and paragraph relevance judgments from Wikipedia headings (Dietz et al., 2017).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Dietz et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-237"></a>
### [Rank #237] NFCorpus

- **Global Impact Rank**: `#237` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `NFCorpus`
- **Core NLP Task / Domain**: `Biomedical Information Ret.`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Boteva et al., 2016

#### Architectural Specifications & Benchmark Details
Extracted 3,244 non-technical natural language nutrition queries mapped to PubMed medical documents via relevance links (Boteva et al., 2016).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Boteva et al., 2016
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-240"></a>
### [Rank #240] Touché-2020

- **Global Impact Rank**: `#240` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Touché-2020`
- **Core NLP Task / Domain**: `Argument Retrieval`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Bondarenko et al., 2020

#### Architectural Specifications & Benchmark Details
Standardized comparative and controversial query datasets for argument retrieval over ClueWeb and Args.me (Bondarenko et al., 2020).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Bondarenko et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-244"></a>
### [Rank #244] HoVer

- **Global Impact Rank**: `#244` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `HoVer`
- **Core NLP Task / Domain**: `Multi-Hop Fact Verification`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Jiang et al., 2020

#### Architectural Specifications & Benchmark Details
Required verifying claims by extracting supporting evidence across up to four Wikipedia articles and multiple hops (Jiang et al., 2020).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Jiang et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-245"></a>
### [Rank #245] FEVEROUS

- **Global Impact Rank**: `#245` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `FEVEROUS`
- **Core NLP Task / Domain**: `Structured + Text Verification`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Aly et al., 2021

#### Architectural Specifications & Benchmark Details
Extended FEVER to require retrieving combined evidence from both unstructured text sentences and structured Wikipedia tables (Aly et al., 2021).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Aly et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-246"></a>
### [Rank #246] AVeriTeC

- **Global Impact Rank**: `#246` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AVeriTeC`
- **Core NLP Task / Domain**: `Real-World Fact-Checking`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Schlichtkrull et al., 2023

#### Architectural Specifications & Benchmark Details
Gathered 4,568 real-world fact-checked claims paired with web-retrieved question-answer evidence trees mitigating context leakage (Schlichtkrull et al., 2023).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Schlichtkrull et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-250"></a>
### [Rank #250] RAGAS /ARES Eval Sets

- **Global Impact Rank**: `#250` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `RAGAS /ARES Eval Sets`
- **Core NLP Task / Domain**: `RAG Pipeline Benchmarking`
- **Citation Impact**: `~425 to ~430 citations`
- **Primary Reference & Authors**: Es et al., 2024

#### Architectural Specifications & Benchmark Details
Established reference-free and synthetic evaluation testbeds for context relevance, faithfulness, and answer relevance in RAG (Es et al., 2024).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Es et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-286"></a>
### [Rank #286] MIMIC-III / MIMIC-IV Notes

- **Global Impact Rank**: `#286` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MIMIC-III / MIMIC-IV Notes`
- **Core NLP Task / Domain**: `Clinical NLP`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Johnson et al., 2016

#### Architectural Specifications & Benchmark Details
De-identified electronic health records and free-text discharge summaries from over 40,000 critical care patients (Johnson et al., 2016).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Johnson et al., 2016
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-288"></a>
### [Rank #288] MedMCQA

- **Global Impact Rank**: `#288` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MedMCQA`
- **Core NLP Task / Domain**: `Medical Entrance QA`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Pal et al., 2022

#### Architectural Specifications & Benchmark Details
Gathered 193,000 multiple-choice medical entrance exam questions (AIIMS & NEET PG) covering 2,400 healthcare topics (Pal et al., 2022).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Pal et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-289"></a>
### [Rank #289] ChemProt / DDI Corpus

- **Global Impact Rank**: `#289` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ChemProt / DDI Corpus`
- **Core NLP Task / Domain**: `Pharmacovigilance IE`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Herrero-Zazo et al., 2013

#### Architectural Specifications & Benchmark Details
Annotated drug-drug interactions and chemical-protein relations in biomedical literature and DrugBank texts (Herrero-Zazo et al., 2013).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Herrero-Zazo et al., 2013
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-290"></a>
### [Rank #290] CUAD

- **Global Impact Rank**: `#290` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CUAD`
- **Core NLP Task / Domain**: `Legal Contract Review`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Hendrycks et al., 2021

#### Architectural Specifications & Benchmark Details
Contract Understanding Atticus Dataset annotated 510 commercial legal contracts with 13,000+ clauses across 41 legal risk categories (Hendrycks et al., 2021).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Hendrycks et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-291"></a>
### [Rank #291] CaseHOLD / Pile of Law

- **Global Impact Rank**: `#291` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CaseHOLD / Pile of Law`
- **Core NLP Task / Domain**: `Legal Pretraining & Holdings`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Compiled 53,000 multiple-choice legal holding questions and a 256 GB corpus of court opinions, contracts, and administrative rules (Zheng et al., 2021 / Henderson et al., 2022).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-295"></a>
### [Rank #295] IBM Debater Datasets

- **Global Impact Rank**: `#295` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `IBM Debater Datasets`
- **Core NLP Task / Domain**: `Computational Argumentation`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Released large-scale corpora for context-dependent claim detection, evidence detection, and argument quality assessment (Rinott et al., 2015 / Toledo et al., 2019).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-300"></a>
### [Rank #300] ACL Anthology Network / OCL

- **Global Impact Rank**: `#300` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ACL Anthology Network / OCL`
- **Core NLP Task / Domain**: `Scholarly Bibliometrics`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Standardized full-text parses, citation graphs, and terminology annotations over computational linguistics papers (Radev et al., 2013 / Rohatgi et al., 2023).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-345"></a>
### [Rank #345] PeerRead

- **Global Impact Rank**: `#345` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `PeerRead`
- **Core NLP Task / Domain**: `Computational Peer Review`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Kang et al., 2018

#### Architectural Specifications & Benchmark Details
Gathered 14,700 paper drafts paired with accept/reject decisions and 10,700 written peer reviews from top AI/NLP venues (Kang et al., 2018).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Kang et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-348"></a>
### [Rank #348] SciTail

- **Global Impact Rank**: `#348` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SciTail`
- **Core NLP Task / Domain**: `Science Exam Entailment`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Khot et al., 2018

#### Architectural Specifications & Benchmark Details
Created 27,000 entailment pairs derived entirely from natural multiple-choice science questions and web sentences without crowdworker authoring artifacts (Khot et al., 2018).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Khot et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-350"></a>
### [Rank #350] ContractNLI

- **Global Impact Rank**: `#350` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ContractNLI`
- **Core NLP Task / Domain**: `Document-Level Legal NLI`
- **Citation Impact**: `~225 to ~228 citations`
- **Primary Reference & Authors**: Koreeda & Manning, 2021

#### Architectural Specifications & Benchmark Details
Annotated non-disclosure agreements (NDAs) where systems classify whether a contract entails, contradicts, or is neutral to legal hypotheses alongside evidence spans (Koreeda & Manning, 2021).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Koreeda & Manning, 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-399"></a>
### [Rank #399] dreaddit / CLPsych Shared Tasks

- **Global Impact Rank**: `#399` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `dreaddit / CLPsych Shared Tasks`
- **Core NLP Task / Domain**: `Mental Health NLP`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Turcan & McKeown, 2019

#### Architectural Specifications & Benchmark Details
Standardized stress analysis and psychological distress identification datasets over multi-domain long-form social media posts (Turcan & McKeown, 2019).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Turcan & McKeown, 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-474"></a>
### [Rank #474] Early Modern English Medical Texts

- **Global Impact Rank**: `#474` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Early Modern English Medical Texts`
- **Core NLP Task / Domain**: `Domain-Specific Retrieval & Verification`
- **Citation Impact**: `~28 (Approx. Index)`
- **Primary Reference & Authors**: Taavitsainen et al., 2011

#### Architectural Specifications & Benchmark Details
Specialized historical scientific corpora tracking early modern lexical evolution (Taavitsainen et al., 2011).

#### Practical Engineering & Research Applications
- **Clinical & Medical Decision Support**: Powers medical exam QA, electronic health record (EHR) extraction, and clinical trial matching.
- **Legal Tech & Contract Intelligence**: Automates clause identification, non-disclosure agreement risk scoring, and statute citation mapping.
- **Enterprise RAG & Fact Verification**: Benchmarks dense retrieval engines, citation verifiers, and hallucination detectors in high-stakes domains.

#### Reference Citation
```text
Taavitsainen et al., 2011
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

## 4. Engineering Implementation & Pipeline Integration Guide

### Training & Fine-Tuning Recipe
When integrating datasets from **Domain-Specific NLP: Biomedical, Legal, Finance & Scholarly IR/RAG** into modern training pipelines:
1. **Preprocessing & Filtering**: Clean noisy tokens, deduplicate overlapping samples, and ensure context window length fits model architecture.
2. **Loss Function & Masking**: Align training targets with the task specification (e.g. causal masking for autoregressive models, sequence-level loss for classification).
3. **Evaluation Protocol**: Evaluate using official evaluation harnesses (e.g., `lm-evaluation-harness`, `HELM`, or task-specific test suites) to prevent benchmark leakage and prompt overfitting.

[Return to Master Index (`dataset.md`)](../dataset.md)
