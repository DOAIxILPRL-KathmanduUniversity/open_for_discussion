# Synthetic Data Engineering (Instruction Tuning)

> [!IMPORTANT] Gist
> Raw interactions from Google AI Studio are a goldmine for **Supervised Fine-Tuning (SFT)**. This module outlines how to transform previous prompts and model responses into high-fidelity JSONL datasets for the Sovereign Nepali Intelligence Registry.

## 1. Data Distillation Pipeline
To use your previous prompts effectively, we follow this transformation sequence:
1.  **Extraction**: Export your history from Google AI Studio (JSON/CSV).
2.  **Cleaning**: Remove metadata, retry attempts, and broken outputs.
3.  **Schema Mapping**: Map the data to a standard instruction format:
    ```json
    {
      "instruction": "नेपाली व्याकरणमा 'कर्ता' र 'क्रिया' को सम्बन्ध बुझाउनुहोस्।",
      "context": "Subject-Verb Agreement rules.",
      "response": "नेपाली व्याकरणमा कर्ताको लिङ्ग, वचन र पुरुष अनुसार क्रियाको रूप परिवर्तन हुन्छ..."
    }
    ```

## 2. Instruction Augmentation
If your prompts were simple, we can "harden" them using **Self-Instruct** logic:
- **Zero-Shot -> Few-Shot**: Add 2-3 examples of the desired output style before the prompt.
- **Chain-of-Thought (CoT)**: Force the model to explain its reasoning steps in Devanagari before providing the final answer.

## 3. High-Fidelity Multi-Turn Datasets
For complex tasks (like building the Grammar Checker), we use **Multi-Turn JSONL**. This preserves the "conversation flow" where you corrected the AI or asked for refinements.

---

### Implementation Tool: AI Studio to JSONL Converter
A custom Python script can be used to batch-process your `.json` exports into a training-ready format.

#nepali-nlp #synthetic-data #sft #instruction-tuning #google-ai-studio #devanagari
