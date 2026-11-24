# History & Evolution of NLP

> [!IMPORTANT] Gist
> The history of NLP is a transition from symbolic pattern-matching and micro-world logic to massive statistical models and transformers. Understanding early milestones like ELIZA and SHRDLU provides context for the "AI Winters" and the eventual dominance of data-driven approaches.

## 1. Symbolic & Rule-Based Era (1950s - 1980s)
The earliest systems relied on hand-crafted rules and strict logical formalisms.
- **Turing Test (1950)**: Alan Turing proposed a behavioral test for machine intelligence—can a machine pass for a human in a text-based conversation?
- **ELIZA (1966)**: Developed by Joseph Weizenbaum, ELIZA was one of the first "chatbots." It used simple pattern matching and substitution to mimic a Rogerian psychotherapist (e.g., "Tell me more about [X]"). It famously demonstrated the "ELIZA Effect," where humans attribute deep meaning to shallow machine responses.
- **SHRDLU (1968-1970)**: Terry Winograd's "Blocks World" system. It demonstrated high-level understanding within a strictly constrained micro-domain (moving blocks). It integrated syntax, semantics, and reasoning, but was impossible to scale to "real-world" language.

## 2. The Statistical Revolution (1990s - 2010s)
With the availability of large corpora (like the Penn Treebank) and increased computing power, NLP shifted from "What are the rules?" to "What is the probability?"
- **HMMs & CRFs**: Probabilistic models for sequence labeling (POS tagging, NER).
- **IBM Models**: Foundational statistical models for machine translation.
- **The Empirical Turn**: A move away from rationalist (Noam Chomsky-style) linguistics toward empiricist, data-driven methods (Jurafsky & Martin).

## 3. The Neural Turn (2013 - Present)
- **Word Embeddings (2013)**: Word2Vec and GloVe introduced dense vector representations, capturing semantic relationships mathematically (e.g., $King - Man + Woman = Queen$).
- **Transformers (2017)**: The "Attention is All You Need" paper revolutionized the field, leading to BERT, GPT, and the current era of Large Language Models (LLMs).

## 4. Why NLP is Hard
The "Succinct" challenges of human language (Booth, 2018):
- **Ambiguity**: "I saw the man with the telescope" (Who has the telescope?).
- **Context**: Meaning changes based on surrounding information.
- **Sarcasm & Idioms**: Figurative language that breaks literal rules.
- **Exceptions**: Natural languages are filled with historical irregularities.

---

#meta #history #evolution #eliza #shrdlu #turing
