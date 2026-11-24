# LLM Alignment & RLHF

> [!IMPORTANT] Gist
> Alignment is the process of fine-tuning an LLM to be **Helpful, Honest, and Harmless (HHH)**. Since base models merely mimic the internet, **Reinforcement Learning from Human Feedback (RLHF)** is required to transform a raw "completion engine" into a reliable "assistant" (Berryman & Ziegler, 2025; Anthropic, 2021).

## 1. The HHH Framework
To be useful in production, a model must align with three core criteria:
- **Helpful**: Follows instructions, provides concise and useful answers, and stays on track.
- **Honest**: Avoids hallucinations. If the model is uncertain, it should express doubt or state that it doesn't know.
- **Harmless**: Does not generate offensive, discriminatory, or dangerous content.

## 2. The RLHF Process
Creating an aligned model involves a complex pipeline of four models and three training stages:

| Stage | Process | Description |
| :--- | :--- | :--- |
| **1. Base Model** | Pre-training | Predicts the next token based on a massive corpus (e.g., GPT-3). |
| **2. SFT Model** | Supervised Fine-Tuning | Fine-tuned on ~10k-15k human-generated "ideal" assistant transcripts. |
| **3. Reward Model** | Preference Learning | Human judges rank multiple completions for the same prompt. A model is trained to predict these rankings. |
| **4. RLHF Model** | PPO Optimization | The SFT model is optimized against the Reward Model using **Proximal Policy Optimization (PPO)** to maximize "helpfulness" scores. |

### The Alignment Tax
Optimizing purely for human preference can sometimes decrease a model's raw reasoning intelligence or performance on specific natural language tasks. This "tax" is mitigated by mixing original pre-training data into the RLHF fine-tuning process.

## 3. Instruct vs. Chat Models
- **Instruct Models**: Trained to follow a single, direct command (e.g., "Summarize this...").
- **Chat Models**: Trained on **ChatML** or similar markup to manage multi-turn conversations.
    - **System Message**: Sets the persona, rules, and constraints (not part of the dialogue).
    - **User Message**: The human's input.
    - **Assistant Message**: The model's response.

## 4. Keeping LLMs Honest
Honesty is difficult to teach via rote examples because "truth" depends on the model's internal knowledge state. RLHF helps the model learn to **calibrate** its confidence:
- High confidence $\rightarrow$ Direct, assertive language.
- Low confidence $\rightarrow$ Hedging phrases ("Based on my training data...", "I'm not entirely sure, but...").

## 5. Reinforcement Learning as Dialogue Interaction (Leblanc, 2024)
Beyond traditional RLHF, LLMs can be treated as **agents** in a dynamic environment:
- **Learning from Interaction**: The LLM interacts with an environment (e.g., a human user or a simulator) and receives rewards/penalties based on its actions.
- **Exploration vs. Exploitation**: In early training stages, the model explores different conversational styles (Exploration) before settling on high-reward behaviors (Exploitation).
- **Policy Networks**: Treating the LLM as a policy network that maps conversational states (history) to actions (completions).
- **Q-Learning with DQNs**: Implementing reinforcement learning algorithms like **Deep Q-Networks** to optimize long-term reward in multi-turn interactions.

---

#llm-engineering #alignment #rlhf #hhh #ppo #chatml #instruction-tuning
