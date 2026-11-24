# T5 & Unified Frameworks

> [!IMPORTANT] Gist
> "Text-to-Text Transfer Transformer" (T5) reframes every NLP task—classification, translation, summarization—as a text generation problem. This enables a single model to handle diverse tasks without specialized heads.

## 1. The Text-to-Text Paradigm (Raffel et al., 2019)
Before T5, models like BERT used different "heads" (linear layers) for different tasks. T5 standardizes everything:
- **Translation**: Input: `translate English to German: That is good.` $\rightarrow$ Output: `Das ist gut.`
- **Classification**: Input: `cola sentence: The course is jumping.` $\rightarrow$ Output: `unacceptable`
- **Summarization**: Input: `summarize: [Full Text]` $\rightarrow$ Output: `[Summary]`

## 2. Encoder-Decoder Architecture
Unlike BERT (Encoder-only) or GPT (Decoder-only), T5 uses the original **Encoder-Decoder** Transformer architecture.
- **Encoder**: Processes the input prefix (e.g., `translate English to German`).
- **Decoder**: Autoregressively generates the target text.
- **Training**: Pre-trained on the **C4 (Colossal Clean Crawled Corpus)** using a span-corruption objective (masking spans of text and asking the model to recover them).

## 3. Unified Benefits
- **Multi-task Learning**: A single set of weights can be fine-tuned simultaneously on multiple datasets.
- **Transferability**: Knowledge from one task (e.g., summarization) can improve performance on another (e.g., QA) due to the shared text format.
- **Zero-shot potential**: The model learns to follow natural language prompts (e.g., `summarize:`) during pre-training.

## 4. Modern Successors
- **FLAN-T5**: An instruction-tuned version of T5 that performs significantly better on zero-shot tasks by being trained on a massive collection of tasks phrased as instructions.
- **UnifiedQA**: A specialized version of T5 fine-tuned to handle various QA formats (multiple choice, extractive, abstractive) as a unified text task.

---

#transformers #t5 #multi-task #text-to-text #instruction-tuning
