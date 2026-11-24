# Question Answering

## Types
- **Extractive QA**: span extraction from context (SQuAD)
- **Abstractive QA**: generate answer in own words
- **Open-domain QA**: retriever + reader pipeline

## Key Models
- BERT for SQuAD (predict start/end tokens)
- T5 (text-to-text framing)
- RAG (retrieval-augmented generation)

## Machine Reading Comprehension (MRC)
While QA is the broader task, **MRC** focuses on a machine's ability to "read" a passage and answer questions about it.
- **MRC Task Types**:
    - **Cloze Tests**: Filling in missing words in a passage.
    - **Multiple-Choice**: Selecting the correct answer from candidates.
    - **Span Extraction**: Identifying the exact start/end of the answer in the text (e.g., SQuAD).
    - **Free-Form Answering**: Generating a natural language response.

## Evaluation Metrics
Beyond EM and F1, modern MRC evaluation uses:
- **HEQ (Human Equivalence Score)**: Measures how close the system is to human performance.
- **METEOR**: Uses stemming and synonymy for more robust matching than BLEU.
- **ROUGE**: Measures n-gram recall between system and reference answers.
- **Exact Match (EM)**: Requires the predicted span to match the ground truth exactly.

## LLM QA Benchmarks
- **Med-PaLM**: 86.5% accuracy on MedQA, exceeding USMLE passing benchmarks (Singhal et al., 2025a)
- **GPT-4**: demonstrates strong clinical reasoning and multi-step QA on domain-specific question sets (Saha et al., 2026)
- LLM-based QA systems support real-time decision support by answering complex queries grounded in document context (Mesk​ó and Topol, 2023)

---

#applied #qa
