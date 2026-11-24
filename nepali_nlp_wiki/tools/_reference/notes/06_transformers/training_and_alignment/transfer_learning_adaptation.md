# Transfer Learning Adaptation Strategies

> [!IMPORTANT] Gist
> Modern NLP relies on adapting large pre-trained models to specific tasks. Strategies like ULMFiT and Knowledge Distillation allow for high performance even with limited labeled data (Azunre, 2021).

## 1. ULMFiT (Universal Language Model Fine-Tuning)
Introduced by Howard & Ruder (2018), this framework established the "3-stage" transfer learning process:
1.  **LM Pre-training**: Training on a massive general corpus (e.g., Wikipedia).
2.  **LM Fine-tuning**: Adapting the language model to the target domain's data (e.g., legal or medical text).
3.  **Classifier Fine-tuning**: Adding a task-specific head and training it with specialized techniques:
    *   **Discriminative Fine-tuning**: Using different learning rates for different layers (lower layers capture general features, higher layers capture task-specific ones).
    *   **Gradual Unfreezing**: Unfreezing layers one by one starting from the top to prevent "catastrophic forgetting."
    *   **Slanted Triangular Learning Rates (STLR)**: Increasing the learning rate linearly at the start and decaying it slowly to achieve rapid convergence.

## 2. Knowledge Distillation
- **Teacher-Student Paradigm**: A large "Teacher" model (e.g., BERT-Large) transfers its knowledge to a smaller "Student" model (e.g., DistilBERT).
- **Soft Targets**: The student learns to match the teacher's output probability distribution (logits) rather than just the hard labels.
- **DistilBERT**: Reduces BERT size by 40% while retaining 97% of its performance and being 60% faster (Sanh et al., 2019; Azunre, 2021).

## 3. Parameter-Efficient Fine-Tuning (PEFT)
- **Adapters**: Small, trainable modules inserted between transformer layers. During fine-tuning, only the adapter weights are updated while the backbone remains frozen.
- **ALBERT (A Lite BERT)**:
    - **Factorized Embedding Parameterization**: Splitting the large vocabulary matrix into two smaller ones.
    - **Cross-Layer Parameter Sharing**: Using the same weights across all transformer layers to drastically reduce the number of unique parameters.

## 4. Sequential vs. Multitask Adaptation
- **Sequential Adaptation**: Fine-tuning on Task A, then Task B. Risk of "catastrophic forgetting" of Task A.
- **Multitask Adaptation**: Training on multiple tasks (e.g., GLUE benchmark) simultaneously to learn a more robust, generalized representation.

---

#transformers #transfer-learning #ulmfit #distillation #bert
