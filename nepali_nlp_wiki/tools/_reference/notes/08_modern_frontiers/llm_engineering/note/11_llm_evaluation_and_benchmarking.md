# LLM Evaluation & Benchmarking

> [!IMPORTANT] Gist
> Evaluation is the process of closing the "Evals Gap" between traditional deterministic software testing and the non-deterministic, generative behavior of LLMs (Souza & Regenstein, 2026).

## 1. The Evals Gap
Traditional testing validates *functionality* against static requirements. LLM evaluation must assess *emergent properties* (reasoning, creativity) and handle stochasticity:
- **Non-Determinism**: Even with the same input, models may produce different outputs due to sampling.
- **Subjectivity**: Metrics must often measure "helpfulness" or "naturalness" rather than boolean correctness.
- **Contamination**: Risks of test data being present in the model's training set.

## 2. Evaluation Taxonomy
### A. Metrics-Based (Extrinsic)
- **BLEU / ROUGE**: Measuring n-gram overlap for translation and summarization.
- **METEOR**: Considering synonyms and paraphrasing.
- **BERTScore**: Using contextual embeddings for semantic similarity.
- **CIDEr / SPICE**: Specialized metrics for image captioning and scene graphs.

### B. Model-Based (LLM-as-a-Judge)
Using a more capable model (e.g., GPT-4o) to evaluate a smaller model's output.
- **Prompt-based**: Using numerical scales (1-10) or Likert-style rubrics.
- **Pairwise Comparison**: The judge model decides which of two outputs is better.
- **Think Before You Speak**: Requiring the judge to explain its reasoning *before* outputting a final score to improve evaluation consistency.

### C. Meta-Evaluation
Evaluating the evaluators to ensure the "Judge" is reliable:
- **Judge Arena**: ELO-based leaderboards for evaluator models.
- **Human Correlation**: Measuring how well LLM-as-a-Judge scores align with expert human judgments.

## 3. Open-Source Evaluation Frameworks
### [LangSmith](https://smith.langchain.com/)
- **Golden Datasets**: Creating ground-truth datasets for regression testing.
- **Tracing**: Full observability into the LLM chain to identify where failure occurs.

### [Promptfoo](https://www.promptfoo.dev/)
- **Configuration-Driven**: Using `promptfooconfig.yaml` to define providers, prompts, and test cases.
- **Assertions**: Automating checks for cost, latency, and specific LLM-rubrics.

### [LightEval](https://github.com/huggingface/lighteval)
- **Scaling**: A lightweight framework from HuggingFace for running standard benchmarks (MMLU, ARC) locally.

## 4. Major Benchmarks
| Benchmark | Focus | Target Capability |
| :--- | :--- | :--- |
| **MMLU** | Multi-task Knowledge | General knowledge across 57 subjects. |
| **ARC (AGI)** | Fluid Intelligence | Ability to solve novel logic puzzles with minimal "cognitive priors." |
| **HumanEval** | Code Generation | Synthesizing functional code from natural language. |
| **LiveBench** | Contamination Resistance | Frequently updated tasks to prevent model memorization. |
| **ZebraLogic** | Logical Reasoning | Logic grid puzzles (Constraint Satisfaction Problems). |
| **BAbI Tasks** | Reasoning | Text-based reasoning and memory. |

## 5. Inference Performance & Visualization (Leblanc, 2024)
Production evaluation goes beyond accuracy to include **Resource Efficiency**:
- **Latency & Throughput**: Measuring time-to-first-token (TTFT) and tokens-per-second (TPS).
- **Arithmetic Intensity**: Analyzing the ratio of compute operations to memory access to identify bottlenecks.
- **Visualization Tools**:
    - **TensorBoard**: Monitoring loss curves, gradient norms, and weight distributions in real-time.
    - **Weights & Biases (WandB) / Comet.ML**: Tracking experiments, hyperparameter sweeps, and model versioning.
    - **Attention Visualization**: Using tools to see which words the model attends to most (Saliency Maps).
- **Hardware Metrics**: Profiling with **NVIDIA Nsight** or **Google Xprof** to optimize for GPUs/TPUs.

---

#modern-frontiers #llm-evals #benchmarking #langsmith #promptfoo #souza-hard-parts
