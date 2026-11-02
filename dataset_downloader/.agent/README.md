# Agent Guide: Autonomous Dataset Curation & Workflow Engineering

Welcome to the **Autonomous Curation Protocol** for Nepali and regional language datasets.
This directory provides standard operating procedures (SOPs) for AI agents and 2026 NLP engineers to discover, verify, map, and standardize public datasets for LLM instruction tuning and embedding model training.

## Agent Responsibilities
1. **Fact-First Verification**: Never hallucinate dataset identifiers, row counts, or licensing. Always verify live endpoints via web search or public APIs before registering a recipe.
2. **Platform Ingestion Engineering**:
   - **Hugging Face**: Use streaming datasets-server endpoints or `load_dataset`.
   - **GitHub**: Stream direct raw URLs (e.g. `raw.githubusercontent.com`), parsing formats like `.conllu`, `.jsonl`, `.csv`.
   - **Kaggle**: Provide authenticated dataset slugs and unzip pipelines.
3. **Task Classification**:
   - **`sft/`**: Supervised instruction-following datasets formatted for Gemma (`messages`, `instruction`, `input`, `output`). *Note: TTS is explicitly excluded.*
   - **`pretrain/`**: Unsupervised raw Devanagari text streams.
   - **`similarity/`**: Query-passage triplets and contrastive pairs for dense retrieval / RAG (Gemma Embedding 2).
4. **Resilient Clamping**: Always support user-defined sample counts (`--limit N`). If a user requests 10,000 samples and only 100 exist, clamp gracefully to 100 without raising an error.
5. **No AI Slop**: Retain only tested, reproducible workflow YAMLs. If a proposed dataset cannot be verified with live sample data, do not register it.

## Directory Index
- [curation_workflow.md](curation_workflow.md): Step-by-step discovery, inspection, and registration SOP.
- [schema_contracts.md](schema_contracts.md): Exact YAML workflow schema and target JSONL specifications.

