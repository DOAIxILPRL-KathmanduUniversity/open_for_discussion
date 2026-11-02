# Nepali Dataset Downloader & Workflow Harness

A lightweight, developer-first toolkit for discovering, verifying, and streaming public Nepali NLP datasets across **Hugging Face**, **GitHub**, and **Kaggle** into standardized JSONL formats ready for **Gemma instruction tuning**, **causal pretraining**, and **Gemma Embedding 2 retrieval**.

---

## 🚀 Quickstart

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Discover Verified Workflows
```bash
python downloader.py list
```

### 3. Inspect a Dataset Recipe
```bash
python downloader.py info sft_qa_hf
```

### 4. Test Verification Mode (Zero Clutter)
Downloads 5 live samples into a temporary buffer, verifies Devanagari text formatting and target schema, prints the record, and automatically deletes the temporary file:
```bash
python downloader.py test sft_qa_hf
python downloader.py test similarity_nli_hf
python downloader.py test sft_pos_treebank_git
```

### 5. Download Custom Dataset Slice
Fetch any requested row count (with safe clamping so asking for 10,000 on a 100-row dataset gracefully saves what is available):
```bash
python downloader.py download sft_qa_hf --limit 50 --output nepali_squad_50.jsonl
python downloader.py download similarity_nli_hf --limit 50 --output nepali_nli_50.jsonl
```

### 6. Browse the Nepali NLP Wiki
Inspect cross-referenced knowledge nodes in the shared agent wiki:
```bash
python downloader.py wiki
```

---

## 📁 Repository Structure

```
dataset_downloader/
├── README.md                      # This documentation
├── requirements.txt               # Minimal runtime dependencies
├── downloader.py                  # Standalone CLI tool
├── workflows/                     # Verified YAML recipes categorized by platform
│   ├── huggingface/               # Hugging Face recipes (SFT QA, Pretrain Corpus, Similarity NLI)
│   ├── github/                    # GitHub recipes (Universal Dependencies CoNLL-U treebank)
│   └── kaggle/                    # Kaggle recipes (Cleaned Wikipedia text)
├── sft/
│   └── example.json               # Canonical Gemma instruction tuning sample
├── pretrain/
│   └── example.json               # Canonical pretraining text sample
├── similarity/
│   └── example.json               # Canonical Gemma Embedding 2 retrieval sample
└── .agent/                        # Autonomous agent operational guide
    ├── README.md                  # Curation agent mandate
    ├── curation_workflow.md       # SOP for discovering and testing new datasets
    └── schema_contracts.md        # Technical specs for JSONL target formats
```

---

## 🎯 Supported Task Families & Target Formats

1. **`sft/` (Supervised Fine-Tuning / Gemma Instruction Tuning)**:
   - Evaluates or fine-tunes chat models with full `messages` (`user` / `model`), `instruction`, `input`, and `output`.
   - *Note: Audio TTS generation is intentionally excluded.*
2. **`pretrain/` (Unsupervised Text Streams)**:
   - Clean Devanagari text lines for masked or causal language model pre-training.
3. **`similarity/` (Dense Retrieval / RAG)**:
   - Contrastive pairs and triplets (`query`, `positive`, `negative`, `score`) for training dense retrieval embeddings like Gemma Embedding 2.

