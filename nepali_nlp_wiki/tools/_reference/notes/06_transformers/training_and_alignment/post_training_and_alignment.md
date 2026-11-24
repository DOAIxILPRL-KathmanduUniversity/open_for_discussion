# LLM Post-training & Alignment

> [!IMPORTANT] Gist
> Post-training transforms a raw base model (trained on next-token prediction) into a helpful assistant through Instruction Tuning and Alignment (RLHF/DPO) to ensure safety, honesty, and helpfulness (Jurafsky & Martin, 2026).

## 1. Supervised Instruction Tuning (SFT)
Fine-tuning the base model on a curated dataset of (Prompt, Response) pairs. This teaches the model the "chat" format.

## 2. Alignment: RLHF & DPO
Aligning model behavior with human preferences.
- **RLHF (Reinforcement Learning from Human Feedback)**: 
    1. Collect human preferences (ranking outputs).
    2. Train a **Reward Model**.
    3. Optimize the LLM using **PPO** (Proximal Policy Optimization).
- **DPO (Direct Preference Optimization)**: A simpler alternative that optimizes the model directly on preference data without an explicit reward model.

## 3. Test-Time Compute
Strategies to improve model reasoning during inference, such as **Chain of Thought (CoT)** or **Self-Correction** (Jurafsky Ch 10.4).

---

#transformers #alignment #rlhf #llm
