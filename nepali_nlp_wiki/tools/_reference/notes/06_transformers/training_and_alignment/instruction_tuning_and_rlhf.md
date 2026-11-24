# Instruction Tuning & RLHF

> [!IMPORTANT] Gist
> Pre-training makes a model "know" things; Instruction Tuning and RLHF make a model "helpful." These steps align the model's raw text-completion capabilities with human intent and safety.

## 1. Instruction Tuning (SFT)
The first step in alignment is **Supervised Fine-Tuning (SFT)**.
- **Process**: Train the model on a curated dataset of `(Prompt, Response)` pairs where humans have written high-quality answers to specific instructions.
- **Effect**: Transitions the model from a "document completer" (GPT) to an "assistant" (InstructGPT/ChatGPT).

## 2. RLHF (Reinforcement Learning from Human Feedback)
SFT is limited by the amount of human-written text available. RLHF uses human **preferences** to scale alignment.
- **Step 1: Reward Model (RM)**:
    - Humans rank model outputs (Output A is better than Output B).
    - A reward model is trained to predict these human preference scores.
- **Step 2: PPO (Proximal Policy Optimization)**:
    - The LLM generates responses, the RM scores them, and the LLM is updated to maximize this reward.
    - **KL Divergence Constraint**: Prevents the model from "forgetting" its pre-training knowledge or drifting into nonsensical high-reward patterns (Reward Hacking).

## 3. DPO (Direct Preference Optimization)
A more recent, efficient alternative to PPO (Rafailov et al., 2023).
- **Core Idea**: Instead of training a separate reward model and using complex RL, DPO directly optimizes the model to increase the probability of preferred responses relative to rejected ones.
- **Advantage**: Simpler to implement, more stable, and often more effective than traditional RLHF.

## 4. Alignment Issues
- **Reward Hacking**: The model finds a way to get a high score from the RM without actually being helpful (e.g., repeating "I am very helpful").
- **Mode Collapse**: The model loses diversity in its responses, becoming overly cautious or repetitive.
- **Syycophancy**: The model tends to agree with the user's bias rather than providing objective truth.

---

#transformers #alignment #rlhf #dpo #ppo #instruction-tuning
