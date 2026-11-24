# Prompt Engineering

## Principles
- Be specific and structured
- Provide examples (few-shot)
- Use system prompts for persona/constraints
- **Prompt Engineering as Playwriting**: Treat the prompt as a script where the model is an actor playing a role. Your job is to set the scene, define the character, and provide the dialogue history to ensure a consistent performance (Berryman & Ziegler, 2025).

## 1. ChatML Structure
Production prompts should use clear role separation:
- **System**: "You are a helpful assistant..." (Sets the world rules).
- **User**: "How do I..." (The specific request).
- **Assistant**: "To do that..." (The model's expected response start).

## Techniques
- **Zero-shot**: just the instruction
- **Few-shot**: instruction + examples
- **Chain-of-Thought (CoT)**: "think step by step"
    - **Zero-shot CoT**: Simply adding the phrase "Think step by step" can trigger reasoning patterns in models that haven't been explicitly trained on the logic (Raaijmakers, 2025).
- **ReAct**: reasoning + acting interleaved

## 3. Advanced Strategies (Souza & Regenstein, 2026)
- **Role Specification**: Defining a clear persona (e.g., "Financial Analyst") to steer the model's tone and expertise.
- **Negative Constraint Reinforcement**: Using explicit "Do Not" instructions for strict boundary control.
- **"Think Before You Speak" (Internal Monologue)**: Instructing the model to generate its reasoning/justification *before* the final answer to improve logical consistency.
- **Temperature Jittering**: Testing prompts across multiple temperature settings (0.0, 0.7, 1.0) to evaluate stability and creativity.

## 4. Systematic Evaluation (Promptfoo)
Don't just "vibe check" prompts. Use a config-driven approach:
- **Assertions**: Automate checks for **latency** (<1s), **cost** (<$0.01), and **regex** patterns.
- **LLM-Rubrics**: Use a judge model to grade prompts based on subjective criteria (e.g., "Does this sound like an expert?").
- **Cost vs. Latency Tradeoffs**: Identifying when a cheaper model (GPT-4o-mini) outperforms a larger one (GPT-4) on specific domain tasks.

### SOMA Assessment
A structured framework for evaluating completions (Berryman & Ziegler, 2025):
- **S**emantic: Does it mean the right thing?
- **O**bjective: Does it meet specific constraints (e.g., length, format)?
- **M**odal: Does it match the desired tone and persona?
- **A**esthetic: Is the formatting and presentation clean?

## 3. Prompting Instability
LLMs display significant sensitivity to minor perturbations (Raaijmakers, 2025):
- **Character Sensitivity**: Changing a semicolon to a dash or a "which" to a "what" can lead to qualitatively different outputs.
- **Order Sensitivity**: In N-shot prompting, the order of examples significantly impacts the result.
- **Temperature**: Higher temperature increases randomness, but even at low temperature, the "instability" of the prompt text remains a risk for evaluation.

## Tips
- Output format specification (JSON, markdown)
- Negative examples ("do NOT do X")
- Temperature and top-p for creativity control

---

#modern #prompting
