# Generative Ideation & Prompt Engineering

> [!IMPORTANT] Gist
> Generative ideation is an ecosystem that automates the transition from an idea to content (text, image, code) using AI-generated prompts (Rothman, 2024).

## 1. Automated Ideation Architecture
- **No-Prompt Instruction**: The system starts with a high-level goal and generates its own specific prompts for sub-tasks.
- **Divergent Association Task (DAT)**: Measuring a model's creativity by its ability to generate semantically distant concepts.

## 2. Advanced Prompt Engineering
- **Chain-of-Thought (CoT)**: Guiding the model to think step-by-step.
- **Metacognitive Prompting**: Emulating human metacognition to enhance NLU (Interpretation → Judgment → Critical Evaluation → Decision → Confidence Assessment).
- **Self-Verification Prompting**: A multi-turn dialogue where the model validates its own predictions to reduce hallucinations and over-prediction.

## 2. Prompt Components
- **Prompt Pilots**: Using a smaller model to "pilot" and refine the prompt for a larger model (e.g., GPT-3.5 refining for GPT-4).
- **Instructional Templates**: Standardizing the "Persona, Context, Task, Constraint" framework.

## 3. Parallelization & Time Complexity
- **O(1) Attention**: The revolutionary shift where the self-attention layer can process all tokens in a sequence simultaneously on a GPU/TPU, unlike the sequential O(n) nature of RNNs (Appendix A).

---

#modern-frontiers #prompt-engineering #ideation #complexity #parallelization
