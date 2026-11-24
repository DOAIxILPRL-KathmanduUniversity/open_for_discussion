# Text Simplification & Summarization

> [!IMPORTANT] Gist
> Text simplification aims to reduce linguistic complexity while preserving meaning, making information accessible to specific audiences (e.g., students, medical patients, or L2 learners). Synthesis (Summarization) focuses on extracting or generating the most relevant information from one or more documents (Jomaa, 2025).

## 1. Text Simplification
### Core Techniques
- **Lexical Simplification**: Replacing complex words with simpler synonyms (e.g., "commence" $\to$ "start").
- **WordNet-based Paraphrasing**: Utilizing semantic relations (synonymy, hyponymy) within knowledge bases like IndoWordNet to generate context-aware alternatives, particularly useful for low-resource languages like Nepali (see [IndoWordNet Extension](../../09_nepali_nlp/indowordnet_extension.md)).
- **Syntactic Simplification**: Breaking long, complex sentences into shorter, simpler ones and converting passive voice to active.
- **AI-Driven Simplification**: Large Language Models (LLMs) like ChatGPT can perform context-aware simplification that maintains the "discourse flow" better than rule-based systems.

### Applications
- **Medical Education**: Converting complex clinical texts into patient-friendly instructions or student-accessible summaries.
- **Language Learning (ELT)**: Adapting authentic texts to the proficiency level of learners without losing the core message.

## 2. Automatic Summarization (Synthesis)
### Approaches
- **Extractive Summarization**: Identifying and concatenating the most important sentences from the source text.
- **Abstractive Summarization**: Generating a new, concise text that captures the "gist" (often using Encoder-Decoder Transformers).
- **Multi-Document Synthesis**: Aggregating information from multiple sources to provide a comprehensive overview of a topic.

## 3. Impact of AI on Discourse
- **Discourse Markers**: When AI paraphrases or simplifies, it may alter or remove discourse markers (e.g., "however," "consequently"), potentially affecting the cohesive structure and the reader's understanding of logical relations (Alia et al., 2025).
- **Corrective Feedback**: AI tools provide real-time feedback on writing, acting as "Cyborg Editors" that suggest simpler phrasing and better structure.

## 4. Evaluation
- **SARI**: A metric specifically for simplification that measures how many "good" changes were made (keep, add, delete).
- **ROUGE**: The standard for summarization, measuring n-gram overlap between the generated and reference summaries.

---

#applied #simplification #summarization #llm #education #discourse
