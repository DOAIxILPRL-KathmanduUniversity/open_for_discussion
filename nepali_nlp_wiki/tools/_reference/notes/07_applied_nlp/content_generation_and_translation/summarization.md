# Summarization

## Types of Summarization
- **Extractive**: Selecting key sentences directly from the source.
- **Abstractive**: Generating new text that captures key points (BART, T5, Pegasus).
- **Single-Document vs. Multi-Document**: Aggregating information from one vs. many sources.
- **Generic vs. Query-Focused**: Providing a general overview vs. answering a specific user question.

## Advanced Statistical Models
- **BSTM (Bayesian Sentence based Topic Model)**: Uses term-sentence and term-document associations for multi-document summarization.
- **FGB (Factorization with Given Bases)**: Groups and summarizes documents simultaneously.
- **TAOS (Topic Aspect-Oriented Summarization)**: Uses "topic factors" to represent different aspects of a topic (e.g., capital words for entities).

## Models & Tools
- **TextRank**: Graph-based extractive ranking.
- **LED**: Optimized for long documents.

## Evaluation
- ROUGE-1, ROUGE-2, ROUGE-L
- BERTScore for semantic similarity
- Human evaluation remains gold standard

## LLM-Based Summarization
- LLMs generate structured summaries from voice transcripts or short-form input, producing full document-length output (Lee et al., 2023)
- Automatic summarization of long document histories extracts key entities, events, and outcomes into concise briefs (Pivovarov and Elhadad, 2015)
- Speech-to-text + NLP pipeline: voice → ASR transcription → NLP summarization → structured output (Cho et al., 2024)
- NLP-aided summarization reduced documentation time by up to 40–50% in benchmark studies (Saha et al., 2026)

## 3. Specialized Domains
### Legal Document Summarization
Summarizing legal judgments and case law requires preserving specific legal entities and reasoning chains.
- **Hybrid Models**: Combining **extractive** (selecting key sentences) and **abstractive** (rewriting for clarity) techniques to produce more readable and accurate legal summaries.
- **Graph-Based Summarization**: Using sentence similarity networks to identify the most central nodes (sentences) for extraction.

---

#applied #summarization
