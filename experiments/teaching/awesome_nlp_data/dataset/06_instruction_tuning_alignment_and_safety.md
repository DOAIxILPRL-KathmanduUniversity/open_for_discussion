# Instruction Tuning, Alignment, Safety & AI Governance
**Instruction Datasets, Human Feedback Preferences, Adversarial Red-Teaming & Frontier Risks**

> **Category Navigation**: [Back to Master Dataset Index](../dataset.md) | Total Benchmarks in Category: **26**

## 1. Domain Overview & Technical Scope
This category captures the datasets critical for converting raw pretrained foundation models into helpful, honest, and harmless conversational assistants. It includes supervised instruction tuning datasets (ShareGPT, Alpaca Data, FLAN), human preference pairs for RLHF/DPO (HH-RLHF), hallucination and truthfulness benchmarks (TruthfulQA), fairness and social bias audits (WinoBias, StereoSet, BBQ), and frontier biosecurity/cybersecurity benchmarks (WMDP, CyberSecEval).

- **Key Applied Focus**: Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), Reinforcement Learning from Human Feedback (RLHF), safety guardrail classifier training, automated red-teaming, and enterprise compliance auditing.
- **Engineering & Verification Guidance**: Carefully balance helpfulness and safety data mixtures to prevent "refusal collapse". For preference datasets, ensure length-bias mitigation and check pairwise consistency across different annotator demographics.

## 2. Category Quick-Reference Table

| Rank | Dataset / Benchmark | Core Task / Focus | Scholarly Citation Tier | Primary Applications | Details Anchor |
|:---:|:---|:---|:---|:---|:---:|
| `#50` | **TruthfulQA** | Hallucination & Factuality | ~1,000 to ~4,500+ (Foundational Benchmark Tier) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-50) |
| `#86` | **Davidson Hate Speech** | Safety & Moderation | ~1,120 to ~1,600 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-86) |
| `#93` | **WinoBias** | Fairness & Coreference | ~1,120 to ~1,600 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-93) |
| `#94` | **StereoSet** | Algorithmic Fairness | ~1,120 to ~1,600 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-94) |
| `#95` | **CrowS-Pairs** | Social Bias Evaluation | ~1,120 to ~1,600 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-95) |
| `#101` | **ShareGPT / Vicuna Benchmark** | Instruction Tuning & Alignment | ~1,110 (Approx. Index) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-101) |
| `#102` | **Alpaca Data / Self-Instruct** | Instruction Tuning & Alignment | ~1,100 (Approx. Index) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-102) |
| `#103` | **HH-RLHF** | Human Preference Alignment | ~1,080 (Approx. Index) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-103) |
| `#187` | **HateXplain** | Explainable Hate Speech | ~550 to ~650 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-187) |
| `#188` | **OLID (OffensEval)** | Offensive Language ID | ~550 to ~650 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-188) |
| `#202` | **FLAN Collection** | Instruction Tuning & Alignment | ~545 (Approx. Index) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-202) |
| `#203` | **Super-NaturalInstructions** | Instruction Tuning & Alignment | ~540 (Approx. Index) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-203) |
| `#204` | **P3 / Public Pool of Prompts** | Instruction Tuning & Alignment | ~535 (Approx. Index) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-204) |
| `#207` | **LIMA** | Instruction Tuning & Alignment | ~520 (Approx. Index) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-207) |
| `#216` | **IFEval** | Instruction Tuning & Alignment | ~475 (Approx. Index) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-216) |
| `#217` | **AlpacaEval** | Instruction Tuning & Alignment | ~470 (Approx. Index) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-217) |
| `#218` | **Arena-Hard / WildBench** | Instruction Tuning & Alignment | ~465 (Approx. Index) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-218) |
| `#219` | **WildChat** | Instruction Tuning & Alignment | ~460 (Approx. Index) | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-219) |
| `#391` | **Social Bias Frames (SBIC)** | Pragmatic Bias & Offensiveness | ~150 to ~178 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-391) |
| `#392` | **BBQ (Bias Benchmark for QA)** | Ambiguous Context Bias | ~150 to ~178 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-392) |
| `#394` | **ETHICS** | Machine Moral Philosophy | ~150 to ~178 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-394) |
| `#486` | **Scalable Oversight Benchmarks** | LLM Safety & Alignment | High-Velocity Frontier / ~25 to ~85 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-486) |
| `#487` | **DeceptionBench** | LLM Truthfulness & Deception | High-Velocity Frontier / ~25 to ~85 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-487) |
| `#488` | **WMDP (Weapons of Mass Destruction Proxy)** | Biosecurity & Safety Benchmark | High-Velocity Frontier / ~25 to ~85 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-488) |
| `#489` | **CyberSecEval** | Cybersecurity Risk Evaluation | High-Velocity Frontier / ~25 to ~85 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-489) |
| `#490` | **AdvGLUE v2** | Adversarial Robustness | High-Velocity Frontier / ~25 to ~85 citations | Supervised Fine-Tuning (SFT) & Alignment | [Inspect](#rank-490) |

---

## 3. Comprehensive Dataset Profiles

<a id="rank-50"></a>
### [Rank #50] TruthfulQA

- **Global Impact Rank**: `#50` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `TruthfulQA`
- **Core NLP Task / Domain**: `Hallucination & Factuality`
- **Citation Impact**: `~1,000 to ~4,500+ (Foundational Benchmark Tier)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Designed 817 questions across 38 categories crafted to trigger imitative falsehoods induced by human misconceptions in pretraining data.

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-86"></a>
### [Rank #86] Davidson Hate Speech

- **Global Impact Rank**: `#86` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Davidson Hate Speech`
- **Core NLP Task / Domain**: `Safety & Moderation`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Davidson et al., 2017

#### Architectural Specifications & Benchmark Details
Distinguished hate speech from offensive language across 25,000 labeled tweets, highlighting lexical bias in automated moderation (Davidson et al., 2017).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Davidson et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-93"></a>
### [Rank #93] WinoBias

- **Global Impact Rank**: `#93` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WinoBias`
- **Core NLP Task / Domain**: `Fairness & Coreference`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Zhao et al., 2018

#### Architectural Specifications & Benchmark Details
Created Winograd-style coreference sentences to measure and mitigate occupational gender bias in NLP systems (Zhao et al., 2018).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Zhao et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-94"></a>
### [Rank #94] StereoSet

- **Global Impact Rank**: `#94` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `StereoSet`
- **Core NLP Task / Domain**: `Algorithmic Fairness`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Nadeem et al., 2021

#### Architectural Specifications & Benchmark Details
Measured stereotypical biases across gender, profession, race, and religion in pretrained masked and autoregressive models (Nadeem et al., 2021).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Nadeem et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-95"></a>
### [Rank #95] CrowS-Pairs

- **Global Impact Rank**: `#95` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CrowS-Pairs`
- **Core NLP Task / Domain**: `Social Bias Evaluation`
- **Citation Impact**: `~1,120 to ~1,600 citations`
- **Primary Reference & Authors**: Nangia et al., 2020

#### Architectural Specifications & Benchmark Details
Provided 1,508 crowd-sourced minimal sentence pairs contrasting historically disadvantaged and advantaged groups in the U.S. (Nangia et al., 2020).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Nangia et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-101"></a>
### [Rank #101] ShareGPT / Vicuna Benchmark

- **Global Impact Rank**: `#101` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ShareGPT / Vicuna Benchmark`
- **Core NLP Task / Domain**: `Instruction Tuning & Alignment`
- **Citation Impact**: `~1,110 (Approx. Index)`
- **Primary Reference & Authors**: Chiang et al., 2023

#### Architectural Specifications & Benchmark Details
Curated 70,000+ user-shared ChatGPT conversations alongside an 80-question GPT-4 evaluation suite that catalyzed open-source instruction tuning (Chiang et al., 2023).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Chiang et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-102"></a>
### [Rank #102] Alpaca Data / Self-Instruct

- **Global Impact Rank**: `#102` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Alpaca Data / Self-Instruct`
- **Core NLP Task / Domain**: `Instruction Tuning & Alignment`
- **Citation Impact**: `~1,100 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Introduced the 52,000 instruction-following dataset generated via self-instruct bootstrapping from text-davinci-003 (Taori et al., 2023 / Wang et al., 2022).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-103"></a>
### [Rank #103] HH-RLHF

- **Global Impact Rank**: `#103` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `HH-RLHF`
- **Core NLP Task / Domain**: `Human Preference Alignment`
- **Citation Impact**: `~1,080 (Approx. Index)`
- **Primary Reference & Authors**: Bai et al., 2022

#### Architectural Specifications & Benchmark Details
Anthropic's Human Helpful and Harmless preference dataset containing 170,000+ pairwise comparisons for reinforcement learning from human feedback (Bai et al., 2022).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Bai et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-187"></a>
### [Rank #187] HateXplain

- **Global Impact Rank**: `#187` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `HateXplain`
- **Core NLP Task / Domain**: `Explainable Hate Speech`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Mathew et al., 2021

#### Architectural Specifications & Benchmark Details
Annotated posts from Twitter and Gab across hate, offensive, and normal labels alongside target communities and token-level rationales (Mathew et al., 2021).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Mathew et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-188"></a>
### [Rank #188] OLID (OffensEval)

- **Global Impact Rank**: `#188` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `OLID (OffensEval)`
- **Core NLP Task / Domain**: `Offensive Language ID`
- **Citation Impact**: `~550 to ~650 citations`
- **Primary Reference & Authors**: Zampieri et al., 2019

#### Architectural Specifications & Benchmark Details
Introduced a hierarchical three-level annotation schema for offensive language, categorization, and target identification in tweets (Zampieri et al., 2019).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Zampieri et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-202"></a>
### [Rank #202] FLAN Collection

- **Global Impact Rank**: `#202` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `FLAN Collection`
- **Core NLP Task / Domain**: `Instruction Tuning & Alignment`
- **Citation Impact**: `~545 (Approx. Index)`
- **Primary Reference & Authors**: Longpre et al., 2023

#### Architectural Specifications & Benchmark Details
Aggregated and formatted 1,836 tasks with diverse instruction templates and chain-of-thought rationales for large-scale instruction tuning (Longpre et al., 2023).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Longpre et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-203"></a>
### [Rank #203] Super-NaturalInstructions

- **Global Impact Rank**: `#203` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Super-NaturalInstructions`
- **Core NLP Task / Domain**: `Instruction Tuning & Alignment`
- **Citation Impact**: `~540 (Approx. Index)`
- **Primary Reference & Authors**: Wang et al., 2022

#### Architectural Specifications & Benchmark Details
Curated 1,616 diverse NLP tasks paired with expert-written declarative task definitions, positive examples, and negative explanations (Wang et al., 2022).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Wang et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-204"></a>
### [Rank #204] P3 / Public Pool of Prompts

- **Global Impact Rank**: `#204` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `P3 / Public Pool of Prompts`
- **Core NLP Task / Domain**: `Instruction Tuning & Alignment`
- **Citation Impact**: `~535 (Approx. Index)`
- **Primary Reference & Authors**: Sanh et al., 2022

#### Architectural Specifications & Benchmark Details
Unified over 170 English NLP datasets into 2,000+ structured prompt templates used to train the T0 zero-shot model (Sanh et al., 2022).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Sanh et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-207"></a>
### [Rank #207] LIMA

- **Global Impact Rank**: `#207` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `LIMA`
- **Core NLP Task / Domain**: `Instruction Tuning & Alignment`
- **Citation Impact**: `~520 (Approx. Index)`
- **Primary Reference & Authors**: Zhou et al., 2023

#### Architectural Specifications & Benchmark Details
Demonstrated the "Superficial Alignment Hypothesis" using a carefully curated 1,000-example instruction tuning dataset (Zhou et al., 2023).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Zhou et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-216"></a>
### [Rank #216] IFEval

- **Global Impact Rank**: `#216` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `IFEval`
- **Core NLP Task / Domain**: `Instruction Tuning & Alignment`
- **Citation Impact**: `~475 (Approx. Index)`
- **Primary Reference & Authors**: Zhou et al., 2023

#### Architectural Specifications & Benchmark Details
Instruction-Following Evaluation focused on 25 categories of "verifiable instructions" (word counts, formatting constraints, keyword frequency) evaluated programmatically (Zhou et al., 2023).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Zhou et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-217"></a>
### [Rank #217] AlpacaEval

- **Global Impact Rank**: `#217` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AlpacaEval`
- **Core NLP Task / Domain**: `Instruction Tuning & Alignment`
- **Citation Impact**: `~470 (Approx. Index)`
- **Primary Reference & Authors**: Li et al., 2023

#### Architectural Specifications & Benchmark Details
Provided an automated, fast, length-controlled LLM-as-a-judge benchmark validated against 20,000 human pairwise annotations (Li et al., 2023).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Li et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-218"></a>
### [Rank #218] Arena-Hard / WildBench

- **Global Impact Rank**: `#218` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Arena-Hard / WildBench`
- **Core NLP Task / Domain**: `Instruction Tuning & Alignment`
- **Citation Impact**: `~465 (Approx. Index)`
- **Primary Reference & Authors**: Lin et al., 2024

#### Architectural Specifications & Benchmark Details
Extracted challenging real-world user queries from wild chat logs to benchmark frontier LLMs with high separability (Lin et al., 2024).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Lin et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-219"></a>
### [Rank #219] WildChat

- **Global Impact Rank**: `#219` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WildChat`
- **Core NLP Task / Domain**: `Instruction Tuning & Alignment`
- **Citation Impact**: `~460 (Approx. Index)`
- **Primary Reference & Authors**: Zhao et al., 2024

#### Architectural Specifications & Benchmark Details
Released 1 million real-world user-ChatGPT interaction logs containing diverse multilingual prompts, jailbreak attempts, and toxic edge cases (Zhao et al., 2024).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Zhao et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-391"></a>
### [Rank #391] Social Bias Frames (SBIC)

- **Global Impact Rank**: `#391` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Social Bias Frames (SBIC)`
- **Core NLP Task / Domain**: `Pragmatic Bias & Offensiveness`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Sap et al., 2020

#### Architectural Specifications & Benchmark Details
Annotated 150,000 structured pragmatic frames explaining the implied stereotype, target group, and offensiveness of social media posts (Sap et al., 2020).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Sap et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-392"></a>
### [Rank #392] BBQ (Bias Benchmark for QA)

- **Global Impact Rank**: `#392` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `BBQ (Bias Benchmark for QA)`
- **Core NLP Task / Domain**: `Ambiguous Context Bias`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Parrish et al., 2022

#### Architectural Specifications & Benchmark Details
Hand-built question sets testing whether QA models fall back on social stereotypes when context is underspecified vs. disambiguated (Parrish et al., 2022).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Parrish et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-394"></a>
### [Rank #394] ETHICS

- **Global Impact Rank**: `#394` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ETHICS`
- **Core NLP Task / Domain**: `Machine Moral Philosophy`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Hendrycks et al., 2021

#### Architectural Specifications & Benchmark Details
Benchmark of 130,000 examples evaluating language models across five classical ethical frameworks: justice, deontology, virtue ethics, utilitarianism, and commonsense morality (Hendrycks et al., 2021).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Hendrycks et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-486"></a>
### [Rank #486] Scalable Oversight Benchmarks

- **Global Impact Rank**: `#486` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Scalable Oversight Benchmarks`
- **Core NLP Task / Domain**: `LLM Safety & Alignment`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Bowman et al., 2022

#### Architectural Specifications & Benchmark Details
Datasets designed to test whether human supervisors can reliably oversee super-human AI outputs (Bowman et al., 2022).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Bowman et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-487"></a>
### [Rank #487] DeceptionBench

- **Global Impact Rank**: `#487` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DeceptionBench`
- **Core NLP Task / Domain**: `LLM Truthfulness & Deception`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Perez et al., 2022

#### Architectural Specifications & Benchmark Details
Controlled evaluation testbeds measuring strategic deception and unprompted hallucination masking in language models (Perez et al., 2022).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Perez et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-488"></a>
### [Rank #488] WMDP (Weapons of Mass Destruction Proxy)

- **Global Impact Rank**: `#488` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WMDP (Weapons of Mass Destruction Proxy)`
- **Core NLP Task / Domain**: `Biosecurity & Safety Benchmark`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Li et al., 2024

#### Architectural Specifications & Benchmark Details
Standardized multiple-choice evaluation suite measuring hazardous knowledge risks in biological and chemical domains (Li et al., 2024).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Li et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-489"></a>
### [Rank #489] CyberSecEval

- **Global Impact Rank**: `#489` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CyberSecEval`
- **Core NLP Task / Domain**: `Cybersecurity Risk Evaluation`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Bhatt et al., 2023

#### Architectural Specifications & Benchmark Details
Meta's benchmark suite measuring cybersecurity vulnerability generation, insecure coding, and prompt injection susceptibility (Bhatt et al., 2023).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Bhatt et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-490"></a>
### [Rank #490] AdvGLUE v2

- **Global Impact Rank**: `#490` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AdvGLUE v2`
- **Core NLP Task / Domain**: `Adversarial Robustness`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Wang et al., 2024

#### Architectural Specifications & Benchmark Details
Hardened adversarial evaluation benchmark testing model vulnerability to multi-layer textual perturbations (Wang et al., 2024).

#### Practical Engineering & Research Applications
- **Supervised Fine-Tuning (SFT) & Alignment**: Converts base models into conversational assistants capable of following multi-turn constraints.
- **RLHF / DPO Preference Optimization**: Provides curated pairwise response preferences to align models with human helpfulness and harmlessness.
- **Safety Guardrails & Compliance Auditing**: Evaluates vulnerabilities to jailbreaks, toxic speech, biosecurity hazards, and prompt injection attacks.

#### Reference Citation
```text
Wang et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

## 4. Engineering Implementation & Pipeline Integration Guide

### Training & Fine-Tuning Recipe
When integrating datasets from **Instruction Tuning, Alignment, Safety & AI Governance** into modern training pipelines:
1. **Preprocessing & Filtering**: Clean noisy tokens, deduplicate overlapping samples, and ensure context window length fits model architecture.
2. **Loss Function & Masking**: Align training targets with the task specification (e.g. causal masking for autoregressive models, sequence-level loss for classification).
3. **Evaluation Protocol**: Evaluate using official evaluation harnesses (e.g., `lm-evaluation-harness`, `HELM`, or task-specific test suites) to prevent benchmark leakage and prompt overfitting.

[Return to Master Index (`dataset.md`)](../dataset.md)
