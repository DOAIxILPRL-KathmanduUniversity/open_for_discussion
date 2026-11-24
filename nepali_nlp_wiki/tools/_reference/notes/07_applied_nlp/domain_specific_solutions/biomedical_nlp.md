# Biomedical NLP & Knowledge Discovery

> [!IMPORTANT] Gist
> Biomedical NLP (BioNLP) is a specialized field focused on extracting and integrating knowledge from massive biological and clinical text repositories (PubMed, EHRs). It relies on precise entity mapping and relation extraction.

## 1. Terminological Resources
BioNLP is driven by large-scale ontologies and metathesauri:
- **UMLS (Unified Medical Language System)**: A massive knowledge base connecting over 100 vocabularies (SNOMED-CT, MeSH, ICD-10).
- **MeSH (Medical Subject Headings)**: Used for indexing and searching life science information.
- **Gene Ontology (GO)**: Standardized vocabulary for gene product attributes.

## 2. Specialized Information Extraction (IE)
Biomedical texts require extracting complex relations between biological entities:
- **Protein-Protein Interaction (PPI)**: Identifying which proteins interact and how.
- **PTM Extraction (Post-Translational Modification)**: Rule-based systems like **RLIMS-P** extract protein substrates, kinases, and phosphorylation sites from literature (Narayanaswamy et al., 2009).
- **Event Extraction**: Moving beyond binary relations to extract "events" (e.g., binding, regulation) with multiple participants and attributes.

## 3. Clinical Text Mining
Analyzing Clinical Notes (EHRs) poses unique challenges:
- **Abbreviations & Acronyms**: High density of ambiguous shorthand (e.g., "PT" for patient, physical therapy, or prothrombin time).
- **De-identification**: Removing Protected Health Information (PHI) to comply with HIPAA/GDPR.
- **Section Parsing**: Identifying different segments of a clinical note (Chief Complaint, History of Present Illness, Plan).

## 4. Question Answering (BioQA)
Fact-based QA is replaced by complex information needs:
- **PICO Format**: Organizing questions by **P**atient/Problem, **I**ntervention, **C**omparison, and **O**utcome (Niu & Hirst, 2009).
- **Semantic Class Analysis**: Using the PICO framework to structure answers from clinical literature.

## 5. Shared Tasks & Benchmarks
The development of BioNLP is steered by community shared tasks (Cohen, 2010):
- **BioCreative (Critical Assessment of Information Extraction in Biology)**: Focuses on **GM** (Gene Mention) recognition and **GN** (Gene Normalization).
    - **Closed Systems**: Use only the provided training data.
    - **Open Systems**: Allowed to use external lexical resources (e.g., specific species databases).
- **BioNLP Shared Task**: Focuses on fine-grained **Event Extraction** (extracting triggers, themes, and causes of biological events).
- **TREC Genomics Track**: Focused on large-scale document retrieval and question answering in the life sciences.

---

#applied #biomedical #bio-nlp #umls #ehr
