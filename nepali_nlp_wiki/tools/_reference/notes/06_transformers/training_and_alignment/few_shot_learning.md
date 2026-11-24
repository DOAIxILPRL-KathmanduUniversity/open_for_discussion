# Few-Shot & Zero-Shot Learning

> [!IMPORTANT] Gist
> In many real-world scenarios, labeled data is scarce or non-existent. LLMs enable classification and generation without extensive fine-tuning through zero-shot and few-shot paradigms (Tunstall et al., 2022).

## 1. Zero-Shot Learning
The model performs a task it was never explicitly trained on, relying solely on its pre-training knowledge and natural language descriptions.
- **Example**: "Classify the sentiment of this text: [TEXT]"

## 2. Few-Shot Learning (In-Context)
Providing the model with a few examples (demonstrations) within the prompt to guide its behavior.
- **Prompt Structure**: [Example 1] -> [Label 1] ... [Target Text] -> ?

## 3. Data Augmentation for NLP
Techniques to artificially increase the size of a training set:
- **Back-translation**: Translating text to another language and back to create paraphrases.
- **Synonym Substitution**: Replacing words with their synonyms.
- **LLM-based Generation**: Using a model to generate synthetic training data.

---

#transformers #few-shot #zero-shot #data-augmentation
