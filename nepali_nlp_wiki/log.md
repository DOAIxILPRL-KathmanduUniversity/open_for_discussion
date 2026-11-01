# Nepali NLP Wiki Audit & Change Log

All modifications, additions, and entity syntheses executed by agents or human curators are recorded here to maintain provenance and lineage.

---

### [2026-11-01] Repository Initialization
- **Author**: Antigravity AI Agent
- **Action**: Initialized Nepali NLP Wiki compliant with Google Open Knowledge Format (OKF v0.2) and Karpathy's LLM-wiki paradigm.
- **Created Modules**:
  - `index.md`: Master bundle index.
  - `.agent`: Operational guideline protocol.
  - `tools/wiki_cli.py`: Graph linter, validator, search query engine, and ingest scaffolding.
  - Starter OKF nodes: `wiki/institutions/ilprl.md`, `wiki/models/nepali_bert.md`, `wiki/concepts/devanagari_tokenization.md`.


---

### [2026-11-01] Architecture Preparation for Datasets & Papers
- **Author**: Antigravity AI Agent
- **Action**: Prepared OKF schema definitions and templates for datasets and research papers without populating entries.
- **Modifications**:
  - Defined starter templates: `tools/templates/dataset.md` and `tools/templates/paper.md`.
  - Registered `dataset` and `paper` types in `tools/wiki_cli.py`.
  - Empty target directories `wiki/datasets/` and `wiki/papers/` ready for user curation.
  - Confirmed Obsidian vault initialization at root (`.obsidian` configuration verified).
