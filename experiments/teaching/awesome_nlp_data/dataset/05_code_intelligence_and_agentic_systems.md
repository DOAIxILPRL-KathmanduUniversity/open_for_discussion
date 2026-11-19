# Code Intelligence, Software Engineering & Agentic Systems
**Automated Code Synthesis, Repository Debugging, Tool Execution & Interactive Environments**

> **Category Navigation**: [Back to Master Dataset Index](../dataset.md) | Total Benchmarks in Category: **29**

## 1. Domain Overview & Technical Scope
This category covers the benchmarks assessing an AI system's ability to write, debug, test, and understand program code, as well as interact autonomously with operating systems, web browsers, and enterprise APIs. It includes canonical function-level generation (HumanEval, MBPP), real-world software engineering issue fixing (SWE-bench), repository-level completion (RepoBench, CrossCodeEval), and interactive agentic environments (GAIA, WebShop, OSWorld).

- **Key Applied Focus**: AI developer copilots, autonomous software engineering agents, automated regression testing, API integrationbots, enterprise browser navigation, and operating system workflow automation.
- **Engineering & Verification Guidance**: Benchmark agents in hermetically sealed container environments (e.g. Docker) with strict execution timeouts. Always report pass@k with unit test verification, and test agent trajectory efficiency (number of tool calls vs task success rate).

## 2. Category Quick-Reference Table

| Rank | Dataset / Benchmark | Core Task / Focus | Scholarly Citation Tier | Primary Applications | Details Anchor |
|:---:|:---|:---|:---|:---|:---:|
| `#36` | **HumanEval (Codex)** | Code Generation | ~1,000 to ~4,500+ (Foundational Benchmark Tier) | Autonomous Software Engineering | [Inspect](#rank-36) |
| `#54` | **MBPP** | Code Synthesis & Intelligence | ~3,450 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-54) |
| `#107` | **APPS** | Code Synthesis & Intelligence | ~1,040 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-107) |
| `#108` | **CodeSearchNet** | Code Synthesis & Intelligence | ~1,030 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-108) |
| `#109` | **CodeXGLUE** | Code Synthesis & Intelligence | ~1,015 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-109) |
| `#110` | **CONCODE** | Autonomous Agent & Tool Execution | ~1,000 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-110) |
| `#111` | **SWE-bench** | Autonomous Agent & Tool Execution | ~990 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-111) |
| `#112` | **GAIA** | Autonomous Agent & Tool Execution | ~980 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-112) |
| `#113` | **AgentBench** | Autonomous Agent & Tool Execution | ~970 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-113) |
| `#114` | **WebShop** | Autonomous Agent & Tool Execution | ~960 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-114) |
| `#115` | **ALFWorld** | Autonomous Agent & Tool Execution | ~950 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-115) |
| `#210` | **The Stack** | Code Synthesis & Intelligence | ~505 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-210) |
| `#211` | **LiveCodeBench** | Code Synthesis & Intelligence | ~500 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-211) |
| `#212` | **EvalPlus (HumanEval+ / MBPP+)** | Code Synthesis & Intelligence | ~495 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-212) |
| `#213` | **DS-1000** | Code Synthesis & Intelligence | ~490 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-213) |
| `#325` | **ToolBench / API-Bank** | Code Synthesis & Intelligence | ~228 (Approx. Index) | Autonomous Software Engineering | [Inspect](#rank-325) |
| `#441` | **ToolQA** | External Tool Knowledge QA | ~85 to ~88 citations | Autonomous Software Engineering | [Inspect](#rank-441) |
| `#442` | **RestGPT** | Real-World API Agent Eval | ~85 to ~88 citations | Autonomous Software Engineering | [Inspect](#rank-442) |
| `#443` | **Gorilla Benchmark** | API Function Calling | ~85 to ~88 citations | Autonomous Software Engineering | [Inspect](#rank-443) |
| `#445` | **WebArena** | Web Agent Benchmark | ~85 to ~88 citations | Autonomous Software Engineering | [Inspect](#rank-445) |
| `#447` | **VisualWebArena** | Multimodal Web Agents | ~85 to ~88 citations | Autonomous Software Engineering | [Inspect](#rank-447) |
| `#448` | **OSWorld** | Operating System Agents | ~85 to ~88 citations | Autonomous Software Engineering | [Inspect](#rank-448) |
| `#449` | **AndroidWorld** | Mobile Device Agent Eval | ~85 to ~88 citations | Autonomous Software Engineering | [Inspect](#rank-449) |
| `#450` | **CREPE** | Code Reasoning & Execution | ~85 to ~88 citations | Autonomous Software Engineering | [Inspect](#rank-450) |
| `#481` | **GAIA-2 / Advanced Agentic Suites** | Multimodal Agent Benchmarks | High-Velocity Frontier / ~25 to ~85 citations | Autonomous Software Engineering | [Inspect](#rank-481) |
| `#482` | **SWE-bench Lite / Multilingual** | Software Engineering Agents | High-Velocity Frontier / ~25 to ~85 citations | Autonomous Software Engineering | [Inspect](#rank-482) |
| `#483` | **DevGPT** | Real-World Developer Prompts | High-Velocity Frontier / ~25 to ~85 citations | Autonomous Software Engineering | [Inspect](#rank-483) |
| `#484` | **RepoBench** | Repository-Level Code Generation | High-Velocity Frontier / ~25 to ~85 citations | Autonomous Software Engineering | [Inspect](#rank-484) |
| `#485` | **CrossCodeEval** | Repository-Level Code Understanding | High-Velocity Frontier / ~25 to ~85 citations | Autonomous Software Engineering | [Inspect](#rank-485) |

---

## 3. Comprehensive Dataset Profiles

<a id="rank-36"></a>
### [Rank #36] HumanEval (Codex)

- **Global Impact Rank**: `#36` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `HumanEval (Codex)`
- **Core NLP Task / Domain**: `Code Generation`
- **Citation Impact**: `~1,000 to ~4,500+ (Foundational Benchmark Tier)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Released 164 hand-written Python programming problems with unit tests to evaluate functional correctness in code synthesis.

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-54"></a>
### [Rank #54] MBPP

- **Global Impact Rank**: `#54` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MBPP`
- **Core NLP Task / Domain**: `Code Synthesis & Intelligence`
- **Citation Impact**: `~3,450 (Approx. Index)`
- **Primary Reference & Authors**: Austin et al., 2021

#### Architectural Specifications & Benchmark Details
Mostly Basic Python Problems introduced 974 crowd-sourced entry-level Python programming tasks paired with automated unit test cases for evaluating code synthesis (Austin et al., 2021).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Austin et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-107"></a>
### [Rank #107] APPS

- **Global Impact Rank**: `#107` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `APPS`
- **Core NLP Task / Domain**: `Code Synthesis & Intelligence`
- **Citation Impact**: `~1,040 (Approx. Index)`
- **Primary Reference & Authors**: Hendrycks et al., 2021

#### Architectural Specifications & Benchmark Details
Automated Programming Progress Standard collected 10,000 introductory to collegiate competition Python coding problems with test cases (Hendrycks et al., 2021).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Hendrycks et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-108"></a>
### [Rank #108] CodeSearchNet

- **Global Impact Rank**: `#108` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CodeSearchNet`
- **Core NLP Task / Domain**: `Code Synthesis & Intelligence`
- **Citation Impact**: `~1,030 (Approx. Index)`
- **Primary Reference & Authors**: Husain et al., 2019

#### Architectural Specifications & Benchmark Details
Assembled 2 million (comment, code) pairs across Python, Java, JavaScript, PHP, Ruby, and Go for semantic code retrieval (Husain et al., 2019).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Husain et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-109"></a>
### [Rank #109] CodeXGLUE

- **Global Impact Rank**: `#109` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CodeXGLUE`
- **Core NLP Task / Domain**: `Code Synthesis & Intelligence`
- **Citation Impact**: `~1,015 (Approx. Index)`
- **Primary Reference & Authors**: Lu et al., 2021

#### Architectural Specifications & Benchmark Details
Unified 14 datasets across 10 diversified code intelligence tasks (clone detection, defect prediction, code translation, code repair) (Lu et al., 2021).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Lu et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-110"></a>
### [Rank #110] CONCODE

- **Global Impact Rank**: `#110` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CONCODE`
- **Core NLP Task / Domain**: `Autonomous Agent & Tool Execution`
- **Citation Impact**: `~1,000 (Approx. Index)`
- **Primary Reference & Authors**: Iyer et al., 2018

#### Architectural Specifications & Benchmark Details
Paired 100,000+ Java class member environments with natural language docstrings and source code (Iyer et al., 2018).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Iyer et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-111"></a>
### [Rank #111] SWE-bench

- **Global Impact Rank**: `#111` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SWE-bench`
- **Core NLP Task / Domain**: `Autonomous Agent & Tool Execution`
- **Citation Impact**: `~990 (Approx. Index)`
- **Primary Reference & Authors**: Jimenez et al., 2024

#### Architectural Specifications & Benchmark Details
Extracted 2,294 real-world GitHub issues and pull requests across 12 Python repositories to evaluate autonomous software engineering agents (Jimenez et al., 2024).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Jimenez et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-112"></a>
### [Rank #112] GAIA

- **Global Impact Rank**: `#112` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `GAIA`
- **Core NLP Task / Domain**: `Autonomous Agent & Tool Execution`
- **Citation Impact**: `~980 (Approx. Index)`
- **Primary Reference & Authors**: Mialon et al., 2023

#### Architectural Specifications & Benchmark Details
General AI Assistants benchmark designed 466 real-world multi-step questions requiring web browsing, multi-modality, and tool-use proficiency (Mialon et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Mialon et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-113"></a>
### [Rank #113] AgentBench

- **Global Impact Rank**: `#113` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AgentBench`
- **Core NLP Task / Domain**: `Autonomous Agent & Tool Execution`
- **Citation Impact**: `~970 (Approx. Index)`
- **Primary Reference & Authors**: Liu et al., 2023

#### Architectural Specifications & Benchmark Details
Evaluated LLMs as autonomous agents across 8 interactive environments including operating systems, databases, knowledge graphs, and web shopping (Liu et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Liu et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-114"></a>
### [Rank #114] WebShop

- **Global Impact Rank**: `#114` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WebShop`
- **Core NLP Task / Domain**: `Autonomous Agent & Tool Execution`
- **Citation Impact**: `~960 (Approx. Index)`
- **Primary Reference & Authors**: Yao et al., 2022

#### Architectural Specifications & Benchmark Details
Simulated an e-commerce website with 1.18 million real-world products and 12,087 crowd-sourced text instructions for grounded language navigation (Yao et al., 2022).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Yao et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-115"></a>
### [Rank #115] ALFWorld

- **Global Impact Rank**: `#115` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ALFWorld`
- **Core NLP Task / Domain**: `Autonomous Agent & Tool Execution`
- **Citation Impact**: `~950 (Approx. Index)`
- **Primary Reference & Authors**: Shridhar et al., 2020

#### Architectural Specifications & Benchmark Details
Aligned interactive TextWorld environments with embodied physical tasks from the ALFRED benchmark for abstract-to-embodied reasoning (Shridhar et al., 2020).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Shridhar et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-210"></a>
### [Rank #210] The Stack

- **Global Impact Rank**: `#210` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `The Stack`
- **Core NLP Task / Domain**: `Code Synthesis & Intelligence`
- **Citation Impact**: `~505 (Approx. Index)`
- **Primary Reference & Authors**: Kocetkov et al., 2022

#### Architectural Specifications & Benchmark Details
Compiled over 6 terabytes of permissively licensed source code across 358 programming languages to train StarCoder and code LLMs (Kocetkov et al., 2022).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Kocetkov et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-211"></a>
### [Rank #211] LiveCodeBench

- **Global Impact Rank**: `#211` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `LiveCodeBench`
- **Core NLP Task / Domain**: `Code Synthesis & Intelligence`
- **Citation Impact**: `~500 (Approx. Index)`
- **Primary Reference & Authors**: Jain et al., 2024

#### Architectural Specifications & Benchmark Details
Introduced a contamination-free, continuously updated coding benchmark harvested from LeetCode, AtCoder, and CodeForces competitions (Jain et al., 2024).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Jain et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-212"></a>
### [Rank #212] EvalPlus (HumanEval+ / MBPP+)

- **Global Impact Rank**: `#212` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `EvalPlus (HumanEval+ / MBPP+)`
- **Core NLP Task / Domain**: `Code Synthesis & Intelligence`
- **Citation Impact**: `~495 (Approx. Index)`
- **Primary Reference & Authors**: Liu et al., 2023

#### Architectural Specifications & Benchmark Details
Augmented classic code synthesis benchmarks with 80x more automated test inputs to expose fragile, edge-case-failing LLM code (Liu et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Liu et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-213"></a>
### [Rank #213] DS-1000

- **Global Impact Rank**: `#213` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DS-1000`
- **Core NLP Task / Domain**: `Code Synthesis & Intelligence`
- **Citation Impact**: `~490 (Approx. Index)`
- **Primary Reference & Authors**: Lai et al., 2023

#### Architectural Specifications & Benchmark Details
Collected 1,000 realistic data science coding problems sourced from StackOverflow spanning NumPy, Pandas, SciPy, Scikit-learn, PyTorch, and Matplotlib (Lai et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Lai et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-325"></a>
### [Rank #325] ToolBench / API-Bank

- **Global Impact Rank**: `#325` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ToolBench / API-Bank`
- **Core NLP Task / Domain**: `Code Synthesis & Intelligence`
- **Citation Impact**: `~228 (Approx. Index)`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Large-scale instruction-tuning and evaluation benchmarks containing 16,000+ real-world RESTful APIs and multi-step tool-use trajectories (Qin et al., 2023 / Li et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-441"></a>
### [Rank #441] ToolQA

- **Global Impact Rank**: `#441` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ToolQA`
- **Core NLP Task / Domain**: `External Tool Knowledge QA`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Zhuang et al., 2023

#### Architectural Specifications & Benchmark Details
Benchmark testing whether models can answer questions by querying external functional APIs (weather, calculators, flight trackers) (Zhuang et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Zhuang et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-442"></a>
### [Rank #442] RestGPT

- **Global Impact Rank**: `#442` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `RestGPT`
- **Core NLP Task / Domain**: `Real-World API Agent Eval`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Song et al., 2023

#### Architectural Specifications & Benchmark Details
Evaluated LLM agents executing multi-step tasks across real-world REST APIs (Song et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Song et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-443"></a>
### [Rank #443] Gorilla Benchmark

- **Global Impact Rank**: `#443` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Gorilla Benchmark`
- **Core NLP Task / Domain**: `API Function Calling`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Patil et al., 2023

#### Architectural Specifications & Benchmark Details
Curated large-scale API instruction-tuning dataset to evaluate reliable function calling and tool selection in LLMs (Patil et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Patil et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-445"></a>
### [Rank #445] WebArena

- **Global Impact Rank**: `#445` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WebArena`
- **Core NLP Task / Domain**: `Web Agent Benchmark`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Zhou et al., 2023

#### Architectural Specifications & Benchmark Details
Realistic web environment suite (e-commerce, forums, enterprise dashboards) evaluating autonomous browser agents (Zhou et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Zhou et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-447"></a>
### [Rank #447] VisualWebArena

- **Global Impact Rank**: `#447` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `VisualWebArena`
- **Core NLP Task / Domain**: `Multimodal Web Agents`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Koh et al., 2024

#### Architectural Specifications & Benchmark Details
Challenging multimodal web navigation and task completion benchmark requiring visual comprehension (Koh et al., 2024).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Koh et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-448"></a>
### [Rank #448] OSWorld

- **Global Impact Rank**: `#448` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `OSWorld`
- **Core NLP Task / Domain**: `Operating System Agents`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Xie et al., 2024

#### Architectural Specifications & Benchmark Details
Evaluated multimodal agents performing complex open-ended tasks across desktop operating systems (Xie et al., 2024).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Xie et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-449"></a>
### [Rank #449] AndroidWorld

- **Global Impact Rank**: `#449` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AndroidWorld`
- **Core NLP Task / Domain**: `Mobile Device Agent Eval`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Rawles et al., 2024

#### Architectural Specifications & Benchmark Details
Standardized interactive Android environment benchmarking autonomous smartphone agents (Rawles et al., 2024).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Rawles et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-450"></a>
### [Rank #450] CREPE

- **Global Impact Rank**: `#450` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CREPE`
- **Core NLP Task / Domain**: `Code Reasoning & Execution`
- **Citation Impact**: `~85 to ~88 citations`
- **Primary Reference & Authors**: Nashid et al., 2023

#### Architectural Specifications & Benchmark Details
Benchmark suite testing LLM debugging, runtime exception prediction, and patch verification (Nashid et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Nashid et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-481"></a>
### [Rank #481] GAIA-2 / Advanced Agentic Suites

- **Global Impact Rank**: `#481` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `GAIA-2 / Advanced Agentic Suites`
- **Core NLP Task / Domain**: `Multimodal Agent Benchmarks`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Mialon et al., 2024

#### Architectural Specifications & Benchmark Details
Next-generation agent evaluation datasets testing complex tool orchestration across multi-application enterprise environments (Mialon et al., 2024).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Mialon et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-482"></a>
### [Rank #482] SWE-bench Lite / Multilingual

- **Global Impact Rank**: `#482` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SWE-bench Lite / Multilingual`
- **Core NLP Task / Domain**: `Software Engineering Agents`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Jimenez et al., 2024

#### Architectural Specifications & Benchmark Details
Filtered subsets of GitHub software engineering tasks for streamlined evaluation of code-fixing agents (Jimenez et al., 2024).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Jimenez et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-483"></a>
### [Rank #483] DevGPT

- **Global Impact Rank**: `#483` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DevGPT`
- **Core NLP Task / Domain**: `Real-World Developer Prompts`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Jain et al., 2023

#### Architectural Specifications & Benchmark Details
Released large-scale developer-ChatGPT interaction logs capturing authentic software development debugging and code generation workflows (Jain et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Jain et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-484"></a>
### [Rank #484] RepoBench

- **Global Impact Rank**: `#484` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `RepoBench`
- **Core NLP Task / Domain**: `Repository-Level Code Generation`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Liu et al., 2023

#### Architectural Specifications & Benchmark Details
Benchmark evaluating large language models on cross-file repository-level code completion and retrieval (Liu et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Liu et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-485"></a>
### [Rank #485] CrossCodeEval

- **Global Impact Rank**: `#485` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `CrossCodeEval`
- **Core NLP Task / Domain**: `Repository-Level Code Understanding`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Ding et al., 2023

#### Architectural Specifications & Benchmark Details
Evaluated cross-file code completion and intelligence across multiple programming languages (Ding et al., 2023).

#### Practical Engineering & Research Applications
- **Autonomous Software Engineering**: Evaluates end-to-end coding agents on discovering, reproducing, and fixing complex GitHub issues (SWE-bench).
- **Tool Calling & API Orchestration**: Trains foundation models to generate executable API calls, query SQL databases, and operate web interfaces.
- **Developer Copilots**: Powers repository-level code autocompletion, real-time bug detection, unit test synthesis, and docstring-to-code generation.

#### Reference Citation
```text
Ding et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

## 4. Engineering Implementation & Pipeline Integration Guide

### Training & Fine-Tuning Recipe
When integrating datasets from **Code Intelligence, Software Engineering & Agentic Systems** into modern training pipelines:
1. **Preprocessing & Filtering**: Clean noisy tokens, deduplicate overlapping samples, and ensure context window length fits model architecture.
2. **Loss Function & Masking**: Align training targets with the task specification (e.g. causal masking for autoregressive models, sequence-level loss for classification).
3. **Evaluation Protocol**: Evaluate using official evaluation harnesses (e.g., `lm-evaluation-harness`, `HELM`, or task-specific test suites) to prevent benchmark leakage and prompt overfitting.

[Return to Master Index (`dataset.md`)](../dataset.md)
