# Mathematical Reasoning, Formal Proofs & Logic
**Multi-Step Math Word Problems, Symbolic Deduction, Interactive Theorem Proving & Olympiad Benchmarks**

> **Category Navigation**: [Back to Master Dataset Index](../dataset.md) | Total Benchmarks in Category: **21**

## 1. Domain Overview & Technical Scope
This category includes the benchmarks and problem collections designed to stress-test formal mathematical calculation, multi-step informal reasoning, logical consistency, and interactive theorem proving in formal languages (Lean, Isabelle, Metamath). From grade-school arithmetic (GSM8K, SVAMP) to high-school/collegiate competitions (MATH, Omni-MATH, miniF2F), these datasets serve as the primary testbed for Chain-of-Thought (CoT) and search-based reasoning.

- **Key Applied Focus**: Fine-tuning reasoning models (o1-style / test-time compute scaling), training formal theorem provers, automated homework solvers, engineering verification engines, and neuro-symbolic logic integration.
- **Engineering & Verification Guidance**: Incorporate step-by-step reasoning verification (PRMs / outcome verifiers) and program-aided generation (PAL / code execution). Always sanitize mathematical inputs to LaTeX format and test across perturbed variations (e.g., GSM-Symbolic) to prevent memorization.

## 2. Category Quick-Reference Table

| Rank | Dataset / Benchmark | Core Task / Focus | Scholarly Citation Tier | Primary Applications | Details Anchor |
|:---:|:---|:---|:---|:---|:---:|
| `#5` | **GSM8K** | Mathematical Problem Solving | 11,761 (Verified Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-5) |
| `#53` | **MATH** | Mathematical Problem Solving | ~3,750 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-53) |
| `#60` | **BAbI Tasks** | Mathematical Problem Solving | ~2,800 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-60) |
| `#104` | **SVAMP** | Mathematical Problem Solving | ~1,070 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-104) |
| `#105` | **AQuA-RAT** | Mathematical Problem Solving | ~1,060 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-105) |
| `#106` | **MathQA** | Mathematical Problem Solving | ~1,050 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-106) |
| `#122` | **LogiQA** | Mathematical Problem Solving | ~890 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-122) |
| `#123` | **ReClor** | Mathematical Problem Solving | ~885 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-123) |
| `#124` | **ProofWriter** | Formal Theorem Proving & Proofs | ~880 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-124) |
| `#125` | **FOLIO** | Mathematical Problem Solving | ~870 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-125) |
| `#221` | **GSM-Symbolic / GSM-Plus** | Mathematical Problem Solving | ~450 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-221) |
| `#222` | **TheoremQA** | Formal Theorem Proving & Proofs | ~445 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-222) |
| `#223` | **OlympiadBench** | Mathematical Problem Solving | ~440 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-223) |
| `#224` | **MuSR** | Mathematical Problem Solving | ~435 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-224) |
| `#225` | **PlanBench** | Mathematical Problem Solving | ~430 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-225) |
| `#315` | **SpartQA / StepGame** | Mathematical Problem Solving | ~250 (Approx. Index) | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-315) |
| `#476` | **ProofNet** | Formal Mathematical Reasoning | High-Velocity Frontier / ~25 to ~85 citations | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-476) |
| `#477` | **miniF2F** | Formal Theorem Proving | High-Velocity Frontier / ~25 to ~85 citations | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-477) |
| `#478` | **LeanDojo Benchmark** | Theorem Proving Data | High-Velocity Frontier / ~25 to ~85 citations | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-478) |
| `#479` | **NaturalProofs** | Mathematical Reasoning | High-Velocity Frontier / ~25 to ~85 citations | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-479) |
| `#480` | **Omni-MATH** | Olympiad Mathematics | High-Velocity Frontier / ~25 to ~85 citations | Test-Time Compute & Chain-of-Thought (CoT) | [Inspect](#rank-480) |

---

## 3. Comprehensive Dataset Profiles

<a id="rank-5"></a>
### [Rank #5] GSM8K

- **Global Impact Rank**: `#5` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `GSM8K`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `11,761 (Verified Index)`
- **Primary Reference & Authors**: Cobbe, K., Kosaraju, V., Bavarian, M., et al. (2021). Training Verifiers to Solve Math Word Problems. arXiv. https://doi.org/10.48550/arxiv.2110.14168

#### Architectural Specifications & Benchmark Details
Released 8,500 linguistically diverse grade-school math word problems with natural language step-by-step solutions to benchmark multi-step informal reasoning in large language models (Cobbe et al., 2021).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Cobbe, K., Kosaraju, V., Bavarian, M., et al. (2021). Training Verifiers to Solve Math Word Problems. arXiv. https://doi.org/10.48550/arxiv.2110.14168
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-53"></a>
### [Rank #53] MATH

- **Global Impact Rank**: `#53` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MATH`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~3,750 (Approx. Index)`
- **Primary Reference & Authors**: Hendrycks et al., 2021

#### Architectural Specifications & Benchmark Details
Compiled 12,500 competition-level mathematics problems from AMC 10, AMC 12, and AIME with full step-by-step LaTeX derivations to measure formal mathematical problem-solving (Hendrycks et al., 2021).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Hendrycks et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-60"></a>
### [Rank #60] BAbI Tasks

- **Global Impact Rank**: `#60` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `BAbI Tasks`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~2,800 (Approx. Index)`
- **Primary Reference & Authors**: Weston et al., 2015

#### Architectural Specifications & Benchmark Details
Designed 20 synthetic toy QA tasks testing elementary reasoning skills—such as pathfinding, induction, and counting—in memory networks (Weston et al., 2015).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Weston et al., 2015
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-104"></a>
### [Rank #104] SVAMP

- **Global Impact Rank**: `#104` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SVAMP`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~1,070 (Approx. Index)`
- **Primary Reference & Authors**: Patel et al., 2021

#### Architectural Specifications & Benchmark Details
Simple Variations on Arithmetic Math word Problems created adversarial perturbations over ASDiv to test whether models rely on shallow heuristics (Patel et al., 2021).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Patel et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-105"></a>
### [Rank #105] AQuA-RAT

- **Global Impact Rank**: `#105` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AQuA-RAT`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~1,060 (Approx. Index)`
- **Primary Reference & Authors**: Ling et al., 2017

#### Architectural Specifications & Benchmark Details
Compiled 100,000 algebraic word problems paired with natural language step-by-step rationales (Ling et al., 2017).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Ling et al., 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-106"></a>
### [Rank #106] MathQA

- **Global Impact Rank**: `#106` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MathQA`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~1,050 (Approx. Index)`
- **Primary Reference & Authors**: Amini et al., 2019

#### Architectural Specifications & Benchmark Details
Annotated 37,000 multiple-choice math word problems with executable domain-specific operation programs over AQuA (Amini et al., 2019).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Amini et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-122"></a>
### [Rank #122] LogiQA

- **Global Impact Rank**: `#122` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `LogiQA`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~890 (Approx. Index)`
- **Primary Reference & Authors**: Liu et al., 2020

#### Architectural Specifications & Benchmark Details
Sourced 8,678 logical comprehension multiple-choice problems from National Civil Servants Examinations of China, translated into English (Liu et al., 2020).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Liu et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-123"></a>
### [Rank #123] ReClor

- **Global Impact Rank**: `#123` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ReClor`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~885 (Approx. Index)`
- **Primary Reference & Authors**: Yu et al., 2020

#### Architectural Specifications & Benchmark Details
Extracted 6,138 logical reasoning reading comprehension questions from standardized graduate admission exams (GMAT and LSAT) (Yu et al., 2020).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Yu et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-124"></a>
### [Rank #124] ProofWriter

- **Global Impact Rank**: `#124` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ProofWriter`
- **Core NLP Task / Domain**: `Formal Theorem Proving & Proofs`
- **Citation Impact**: `~880 (Approx. Index)`
- **Primary Reference & Authors**: Tafjord et al., 2021

#### Architectural Specifications & Benchmark Details
Generated synthetic rulebases and natural language proofs to evaluate multi-hop deductive and abductive logical reasoning (Tafjord et al., 2021).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Tafjord et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-125"></a>
### [Rank #125] FOLIO

- **Global Impact Rank**: `#125` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `FOLIO`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~870 (Approx. Index)`
- **Primary Reference & Authors**: Han et al., 2022

#### Architectural Specifications & Benchmark Details
Expert-written open-domain natural language reasoning dataset annotated with parallel first-order logic formulas (Han et al., 2022).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Han et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-221"></a>
### [Rank #221] GSM-Symbolic / GSM-Plus

- **Global Impact Rank**: `#221` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `GSM-Symbolic / GSM-Plus`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~450 (Approx. Index)`
- **Primary Reference & Authors**: Mirzadeh et al., 2024

#### Architectural Specifications & Benchmark Details
Created symbolic templates and adversarial mathematical perturbations over GSM8K to measure fragile vs. genuine mathematical reasoning (Mirzadeh et al., 2024).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Mirzadeh et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-222"></a>
### [Rank #222] TheoremQA

- **Global Impact Rank**: `#222` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `TheoremQA`
- **Core NLP Task / Domain**: `Formal Theorem Proving & Proofs`
- **Citation Impact**: `~445 (Approx. Index)`
- **Primary Reference & Authors**: Chen et al., 2023

#### Architectural Specifications & Benchmark Details
Curated 800 theorem-driven questions requiring models to apply university-level theorems from math, physics, EE, and finance (Chen et al., 2023).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Chen et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-223"></a>
### [Rank #223] OlympiadBench

- **Global Impact Rank**: `#223` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `OlympiadBench`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~440 (Approx. Index)`
- **Primary Reference & Authors**: He et al., 2024

#### Architectural Specifications & Benchmark Details
Bilingual multimodal benchmark featuring 8,476 Olympiad-level mathematics and physics competition problems (He et al., 2024).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
He et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-224"></a>
### [Rank #224] MuSR

- **Global Impact Rank**: `#224` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MuSR`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~435 (Approx. Index)`
- **Primary Reference & Authors**: Sprague et al., 2023

#### Architectural Specifications & Benchmark Details
Multistep Soft Reasoning benchmark evaluating LLMs on complex murder mysteries, object placement, and team allocation narratives (Sprague et al., 2023).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Sprague et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-225"></a>
### [Rank #225] PlanBench

- **Global Impact Rank**: `#225` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `PlanBench`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~430 (Approx. Index)`
- **Primary Reference & Authors**: Valmeekam et al., 2023

#### Architectural Specifications & Benchmark Details
Standardized classical AI planning domains (BlocksWorld, Logistics) translated into natural language to test LLM planning and verification (Valmeekam et al., 2023).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Valmeekam et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-315"></a>
### [Rank #315] SpartQA / StepGame

- **Global Impact Rank**: `#315` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SpartQA / StepGame`
- **Core NLP Task / Domain**: `Mathematical Problem Solving`
- **Citation Impact**: `~250 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Benchmarks for spatial relational reasoning in natural language text requiring multi-hop qualitative spatial calculus deduction (Mirzaee et al., 2021 / Shi et al., 2022).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-476"></a>
### [Rank #476] ProofNet

- **Global Impact Rank**: `#476` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ProofNet`
- **Core NLP Task / Domain**: `Formal Mathematical Reasoning`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Azerbayev et al., 2023

#### Architectural Specifications & Benchmark Details
Benchmark of 371 undergraduate-level mathematics problems paired with Lean theorem prover formal statements (Azerbayev et al., 2023).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Azerbayev et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-477"></a>
### [Rank #477] miniF2F

- **Global Impact Rank**: `#477` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `miniF2F`
- **Core NLP Task / Domain**: `Formal Theorem Proving`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Zheng et al., 2021

#### Architectural Specifications & Benchmark Details
Collected Olympiad and high school competition math problems formalized in Lean, Isabelle, and Metamath (Zheng et al., 2021).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Zheng et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-478"></a>
### [Rank #478] LeanDojo Benchmark

- **Global Impact Rank**: `#478` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `LeanDojo Benchmark`
- **Core NLP Task / Domain**: `Theorem Proving Data`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Yang et al., 2023

#### Architectural Specifications & Benchmark Details
Extracted 100,000+ theorem proving interaction data points from Lean mathematical library repositories (Yang et al., 2023).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Yang et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-479"></a>
### [Rank #479] NaturalProofs

- **Global Impact Rank**: `#479` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `NaturalProofs`
- **Core NLP Task / Domain**: `Mathematical Reasoning`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Welleck et al., 2021

#### Architectural Specifications & Benchmark Details
Paired informal mathematical theorem proofs from Wikipedia and textbooks with formal LaTeX proof steps (Welleck et al., 2021).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Welleck et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-480"></a>
### [Rank #480] Omni-MATH

- **Global Impact Rank**: `#480` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Omni-MATH`
- **Core NLP Task / Domain**: `Olympiad Mathematics`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Gao et al., 2024

#### Architectural Specifications & Benchmark Details
Comprehensive benchmark of 4,442 extremely challenging Olympiad math problems categorized by 33 sub-fields (Gao et al., 2024).

#### Practical Engineering & Research Applications
- **Test-Time Compute & Chain-of-Thought (CoT)**: Benchmarks reasoning trace generation, self-correction loops, and verifier-guided tree search.
- **Automated Theorem Proving (ATP)**: Trains formal proof synthesizers in interactive theorem environments (Lean 4, Isabelle, Metamath).
- **Neuro-Symbolic Software & STEM Solvers**: Powers educational tutoring agents, formal hardware/software verification, and competition problem-solving.

#### Reference Citation
```text
Gao et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

## 4. Engineering Implementation & Pipeline Integration Guide

### Training & Fine-Tuning Recipe
When integrating datasets from **Mathematical Reasoning, Formal Proofs & Logic** into modern training pipelines:
1. **Preprocessing & Filtering**: Clean noisy tokens, deduplicate overlapping samples, and ensure context window length fits model architecture.
2. **Loss Function & Masking**: Align training targets with the task specification (e.g. causal masking for autoregressive models, sequence-level loss for classification).
3. **Evaluation Protocol**: Evaluate using official evaluation harnesses (e.g., `lm-evaluation-harness`, `HELM`, or task-specific test suites) to prevent benchmark leakage and prompt overfitting.

[Return to Master Index (`dataset.md`)](../dataset.md)
