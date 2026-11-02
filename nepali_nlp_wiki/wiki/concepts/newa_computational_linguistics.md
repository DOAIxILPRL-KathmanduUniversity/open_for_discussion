---
okf_version: "0.2"
type: "concept"
title: "Nepal Bhasa (Newar) Computational Linguistics & Historical Corpora"
description: "Comprehensive foundational concept node for Nepal Bhasa (Newari / new / newa1246), documenting its Tibeto-Burman grammar, scripts (Devanagari, Prachalit, Ranjana), classical epigraphy, dialects, and modern NLP ecosystem."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T11:20:00Z"
language:
  - "new" # ISO 639-3
script:
  - "Devanagari"
  - "Prachalit (Newa, U+11400–U+1147F)"
  - "Ranjana"
tags:
  - newar
  - nepal-bhasa
  - tibeto-burman
  - epigraphy
  - manuscripts
  - low-resource-nlp
---

# Nepal Bhasa (Newar) Computational Linguistics & Historical Corpora

## Linguistic & Typological Profile
**Nepal Bhasa** (नेपालभाषा / नेवाः भाय्, ISO 639-3: `new`, Glottocode: `newa1246`) is a Sino-Tibetan (Tibeto-Burman) language indigenous to the Kathmandu Valley and surrounding regions of Nepal.

Unlike Indo-Aryan languages (such as Nepali and Hindi), Nepal Bhasa exhibits:
- **Ergative-Absolutive Syntax**: Split ergativity dictated by tense, aspect, and agent volition.
- **Evidentiality & Conjunct/Disjunct Verb Agreement**: Egophoricity where verb endings indicate whether the speaker is the conscious actor or an external observer.
- **Rich Numeral Classifiers**: Elaborate classifier systems categorizing nouns by animacy, shape, and physical dimensionality.
- **Poly-Scriptal Heritage**: Historically recorded in indigenous scripts—**Prachalit (Nepal Lipi, Unicode U+11400–U+1147F)**, **Ranjana Lipi**, and **Bhujinmol**—and contemporarily published in **Devanagari**.

---

## 1. Classical Epigraphy & Medieval Manuscripts
The language possesses an unbroken millennium-long written tradition with significant manuscript archives:
- **Mānavanyāyaśāstraṭīkā (1407 AD / NS 527)**: Oldest secular legal treatise and commentary in Classical Newari (Cambridge MS Add.2137).
- **Amarakośavivṛti (1386 AD / NS 506)**: Bilingual Newari lexical commentary on Amarasiṃha's Sanskrit thesaurus (Cambridge MS Add.1698).
- **Gopālarājavaṃśāvalī (1387–1390 AD)**: Vellum royal chronicle of the Nepal Valley written in mixed Sanskrit and archaic Classical Newar.
- **Hitopadeśa (Cambridge MS Add.1591)** & **Pañcarakṣā (1205/1459 AD)**: Palm-leaf Buddhist and narrative manuscripts preserving medieval morphological transitions.

---

## 2. Dialectology & Regional Isolates
Beyond standard Kathmandu and Patan dialects, Newar encompasses archaic isolate varieties:
- **Dolakha Newar**: An archaic conservative dialect retaining distinctive verbal inflections and archaic suffixes lost in Valley dialects.
- **Pahari**: Spoken in hilly periphery settlements (Chitlang, Pharping).
- **Bhaktapur Dialect**: Preserves historical glottal stops and vowel length contrasts.

---

## 3. Publicly Available Datasets & Pre-training Corpora

| Corpus / Dataset | Platform | Modality | Scope & Description | Link |
| :--- | :--- | :--- | :--- | :--- |
| **FineWeb-2 (`new_Deva`)** | Hugging Face | Web Text | Filtered web text paragraphs in Devanagari Newari extracted from Common Crawl. | [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) |
| **FinePDFs (`new_Deva`)** | Hugging Face | Documents | Cleaned text extracted from public PDF documents in Newari. | [FinePDFs](https://huggingface.co/datasets/HuggingFaceFW/finepdfs) |
| **MADLAD-400 (`new`)** | Google Research | Clean Text | Document-level cleaned web corpus supporting low-resource MT pre-training. | [MADLAD-400](https://huggingface.co/datasets/google/madlad-400) |
| **OSCAR (2201 & 2301)** | Hugging Face | Common Crawl | Deduplicated web paragraphs identified as Newari. | [OSCAR](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201) |
| **GlotCC-V1 & Glot500** | CIS-LMU | Web Text | Massive multilingual crawls including `new-Deva` splits. | [Glot500](https://huggingface.co/datasets/cis-lmu/Glot500) |
| **CulturaX Mini** | Hugging Face | Clean Crawl | High-quality deduplicated web dataset for tail languages. | [CulturaX](https://huggingface.co/datasets/devngho/culturax-mini-nonshuffled) |
| **FLORES-200 (`new_Deva`)** | Meta AI | Parallel MT | Multi-way sentence-aligned parallel benchmark for low-resource translation. | [FLORES-200](https://github.com/facebookresearch/flores) |
| **IndicCorp v2 (`new`)** | AI4Bharat | Monolingual | Curated Indic text collection including web crawled Devanagari Newar text. | [AI4Bharat IndicCorp](https://ai4bharat.iitm.ac.in/) |
| **OpenSLR 84 (Spoken Newar)** | OpenSLR | Audio / Speech | High quality speech data and crowd-sourced recordings for Newari ASR. | [OpenSLR 84](https://openslr.org/84/) |
| **DACON Diachronic Newar Corpus** | Cambridge / Zenodo | Philology / Lexicon | Machine-readable transcription and dictionary corpus of diachronic Newar epigraphy and palm-leaf manuscripts. | [Zenodo](https://zenodo.org/records/12887386) / [Cambridge Apollo](https://doi.org/10.17863/cam.111572) |
| **Newari Literature Scraped Text Corpus** | Kaggle | Monolingual Literature | Aggregated digital literary texts and cultural articles in Nepal Bhasa collected to support low-resource tokenization and language modeling. | [Kaggle](https://www.kaggle.com/) |

---

## 4. Academic Research & NLP Literature

| Topic | Key Authors & Landmark Publications |
| :--- | :--- |
| **Grammar & Morphosyntax** | Carol Genetti (2007): *A Grammar of Dolakha Newar*; Austin Hale & Kedar P. Shrestha (2006): *Newari (Nepal Bhasa)*; David Hargreaves (2005): *Functional Syntax of Nepal Bhasa*. |
| **Classical Lexicography** | Kashinath Tamot, Ian Alsop, Kamal P. Malla (2000): *A Dictionary of Classical Newari: Compiled from Manuscript Sources* (Cinnamas, Nepal Bhasa Dictionary Committee). |
| **OCR & Script Analysis** | Research on Prachalit and Ranjana character segmentation, Shirorekha detection, and handwritten manuscript restoration using CNNs. |
| **Speech Processing** | Acoustic modeling for low-resource Newari using Kaldi, wav2vec 2.0, and Whisper multilingual fine-tunes. |

---

## Connected Graph Nodes
- **Extended Manuscripts & Heritage**: [Newar Extended Manuscripts & Heritage](wiki/concepts/newa_extended_resources.md)
- **Web Portals & Media Archives**: [Newar Web Portals & Digital Media](wiki/concepts/newa_media_portals_and_archives.md)

