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


---

### [2026-11-02] Concept-Wise Curation of NLP Papers & Datasets
- **Author**: Antigravity AI Agent
- **Action**: Ingested and synthesized verified Nepali NLP research papers, datasets, models, and institutions from `raw/dump1.md` strictly according to concept domains.
- **Excluded**:
  - All student club noise (KUAIC, meeting notes, Panchkhal day intros, team member rosters).
  - All non-NLP web bookmarks, casual YouTube shorts, and lifehacks.
- **Created Nodes**:
  - **Datasets** (`wiki/datasets/`):
    - `speech_datasets.md`: OpenSLR 54, High Quality TTS, Bible audio.
    - `translation_datasets.md`: FLORES-101/200, WMT19, PAN Localization.
    - `sentiment_datasets.md`: Movie reviews, editorial sentiment datasets.
    - `classification_datasets.md`: 16NepaliNews, iNLTK, SMS spam datasets.
    - `ner_datasets.md`: DanfeNER, EverestNER, CoNLL NER annotations.
    - `summarization_datasets.md`: XL-Sum Nepali sub-corpus, news summaries.
    - `morphology_pos_datasets.md`: Nelralec NT-01 corpus, PAN POS annotations.
    - `lexicon_wordnet_datasets.md`: Nepali WordNet synsets, SIL dictionaries, Hunspell wordlists.
    - `monolingual_text_datasets.md`: OSCAR Nepali crawl, Wikipedia dump, C4 multilingual.
  - **Research Papers** (`wiki/papers/`):
    - `speech_papers.md`: TTS synthesis, PSOLA/ESNOLA, CNN ASR.
    - `translation_papers.md`: FLORES MT benchmark, DOBHASE, Hindi-Nepali NMT.
    - `sentiment_papers.md`: Newspaper editorial polarity, appraisal theory, BiLSTM.
    - `classification_papers.md`: 16NepaliNews baselines, transformers, codebook vectors.
    - `ner_papers.md`: CRF taggers, BiLSTM-CRF, hybrid SVM NER.
    - `morphology_pos_papers.md`: Bal (2004), Prasain (2011), Hardie (2005 NT-01), Shrestha (2021).
    - `wordnet_wsd_papers.md`: IndoWordNet, PolyWordNet, Lesk measure WSD.
    - `language_modeling_papers.md`: NepBERTa, Nepali Transformer encoders, Unicode preprocessing.
    - `ocr_papers.md`: DevNet CNN, Bal & Rupakheti OCR, handwritten Devanagari benchmarks.
  - **Models** (`wiki/models/`):
    - `nepberta.md`: RoBERTa-based Nepali language model.
    - `npvec1_embeddings.md`: Word2Vec, FastText, and ELMo dense vectors.
    - `nepalibert.md`: Monolingual BERT-Base.
  - **Institutions** (`wiki/institutions/`):
    - `ilprl.md`: Information & Language Processing Research Lab (Kathmandu University).
    - `ltk.md`: Language Technology Kendra.
    - `naamii.md`: NAAMII.
  - **Concepts** (`wiki/concepts/`):
    - `devanagari_nlp.md`: Devanagari Unicode, abugida tokenization, and orthography.
- **Verification**: `python3 tools/wiki_cli.py lint` executed with 0 errors and 0 warnings.


---

### [2026-11-02] Public Repositories & Python Libraries Integration
- **Author**: Antigravity AI Agent
- **Action**: 
  - Purged all references to local file paths/unshared files across all nodes (e.g. replaced local translation references with public OPUS/CCAligned parallel data).
  - Researched publicly available, out-of-the-box Python NLP libraries and toolkits for Nepali.
  - Added new catalog node: `wiki/concepts/nepali_nlp_libraries.md` covering:
    - Tokenizers: `nepalitokenizers`, `nepalikit`, `indic-nlp-library`
    - Stemmers & Utilities: `nepali-stemmer`, `Nepali_nlp`
    - Font Converters: `nepali-converter`, `npttf2utf`
    - Speech & Vision: `supernova-teraitts`, `pytesseract` with `nep.traineddata`
  - Validated link graph: `python3 tools/wiki_cli.py lint` passed with 0 errors and 0 warnings.


---

### [2026-11-02] Ingestion of Newari (Nepal Bhasa) Catalogs
- **Author**: Antigravity AI Agent
- **Action**: Ingested and synthesized the Newari resources from `/catalogs/datasource.md` and `/catalogs/newari_resources_extended.md` into concept nodes using the `newa_` prefix.
- **Created Nodes**:
  - `wiki/concepts/newa_computational_linguistics.md`: Master computational linguistics concept node covering typological characteristics (Tibeto-Burman, ergative-absolutive, evidentiality), scripts (Devanagari, Prachalit Unicode U+11400, Ranjana), modern web corpora (FineWeb-2, MADLAD-400, OSCAR, Glot500, FLORES-200), speech corpora (OpenSLR 84), and core research publications.
  - `wiki/concepts/newa_extended_resources.md`: Comprehensive historical philology, classical epigraphy, and manuscript archives node covering Cambridge Digital Library palm-leaf manuscripts (Mānavanyāyaśāstraṭīkā 1407 AD, Amarakośavivṛti 1386 AD), Gopālarājavaṃśāvalī, Malla stone epigraphs, and Classical Newari dictionaries.
- **Verification**: `python3 tools/wiki_cli.py lint` executed with 0 errors and 0 warnings.


---

### [2026-11-02] Catalogs Ingestion Cleanup & Link Normalization
- **Author**: Antigravity AI Agent
- **Action**:
  - Removed boilerplate institution back-links (`ILPRL`, `NAAMII`) from concept nodes where they were repetitive.
  - Safely preserved original raw catalogs in `raw/` (`raw/datasource.md`, `raw/newari_resources_extended.md`) adhering to the OKF raw archival standard.
  - Completely deleted the redundant `/Users/paramanada/Desktop/ilprl_internship/catalogs` directory.
  - Re-ran linter: verified 0 errors, 0 warnings.


---

### [2026-11-02] Added Newar Media Portals & Digital Archives
- **Author**: Antigravity AI Agent
- **Action**: Ingested the Nepal Bhasa media portals, e-readers, encyclopedias, community weblogs, and broadcast channels into `wiki/concepts/newa_media_portals_and_archives.md`.
- **Sections Compiled**:
  - Online News & Journalism Portals (Lahana News, Nepalbhasa Times, NepalMandal, Subhay Post, Inap, etc.).
  - Interactive Reading & Graded Storybooks (Bloom Library, OLE E-Pustakalaya, Pagine App, GDL).
  - Open Encyclopedias & Database Dumps (Nepal Bhasa Wikipedia, Wikimedia Dumps, Wikidata, Newa Gyankosh).
  - Lexical & Academic Archives (NepalBhasa.org, Laykoo Magazine, Internet Archive).
  - Community Literary Weblogs & Song Lyrics (Silu ballad, Basanta Maharjan, Tikijhyā, Dapha notations).
  - Spoken Audio-Visual & Broadcast Channels (Lahana Media, Inap, Radio Nepal Newari Service).
- **Verification**: `python3 tools/wiki_cli.py lint` confirmed 0 errors and 0 warnings.


---

### [2026-11-02] Catalogs Ingestion Cleanup & Link Normalization
- **Author**: Antigravity AI Agent
- **Action**:
  - Removed boilerplate institution back-links (`ILPRL`, `NAAMII`) from concept nodes where they were repetitive.
  - Safely preserved original raw catalogs in `raw/` (`raw/datasource.md`, `raw/newari_resources_extended.md`) adhering to the OKF raw archival standard.
  - Completely deleted the redundant `/Users/paramanada/Desktop/ilprl_internship/catalogs` directory.
  - Re-ran linter: verified 0 errors, 0 warnings.


---

### [2026-11-02] Added Newar Media Portals & Digital Archives
- **Author**: Antigravity AI Agent
- **Action**: Ingested the Nepal Bhasa media portals, e-readers, encyclopedias, community weblogs, and broadcast channels into `wiki/concepts/newa_media_portals_and_archives.md`.
- **Sections Compiled**:
  - Online News & Journalism Portals (Lahana News, Nepalbhasa Times, NepalMandal, Subhay Post, Inap, etc.).
  - Interactive Reading & Graded Storybooks (Bloom Library, OLE E-Pustakalaya, Pagine App, GDL).
  - Open Encyclopedias & Database Dumps (Nepal Bhasa Wikipedia, Wikimedia Dumps, Wikidata, Newa Gyankosh).
  - Lexical & Academic Archives (NepalBhasa.org, Laykoo Magazine, Internet Archive).
  - Community Literary Weblogs & Song Lyrics (Silu ballad, Basanta Maharjan, Tikijhyā, Dapha notations).
  - Spoken Audio-Visual & Broadcast Channels (Lahana Media, Inap, Radio Nepal Newari Service).
- **Verification**: `python3 tools/wiki_cli.py lint` confirmed 0 errors and 0 warnings.


---

### [2026-11-02] Manual Line-by-Line Curation of Academic Papers
- **Author**: Antigravity AI Agent
- **Action**:
  - Moved `curated_nlp_papers.json` from `local/notes_dumps/` into `open_for_discussion/nepali_nlp_wiki/raw/`.
  - Audited all 191 entries line-by-line:
    - Filtered out 14 irrelevant medical pathology and civil engineering non-NLP false-positives (e.g. phyllodes tumors, aquifer subsidence).
    - Manually categorized each verified paper by conceptual task and methodology.
  - Appended structured bibliographic tables with full citations, authors, dates, and official DOIs to:
    - `sentiment_papers.md` (19 peer-reviewed papers)
    - `speech_papers.md` (28 peer-reviewed papers)
    - `ocr_papers.md` (20 peer-reviewed papers)
    - `classification_papers.md` (22 peer-reviewed papers)
    - `ner_papers.md` (16 peer-reviewed papers)
    - `morphology_pos_papers.md` (8 peer-reviewed papers)
    - `translation_papers.md` (3 peer-reviewed papers)
    - `language_modeling_papers.md` (61 peer-reviewed papers covering transformers, RAG, QA, and summarization)
  - Successfully verified graph schema: 0 errors, 0 warnings.


---

### [2026-11-02] Added IOE and NepJOL to Institutions
- **Author**: Antigravity AI Agent
- **Action**: Created dedicated institution nodes for Nepal's primary engineering research faculty and open-access publishing platform:
  - `wiki/institutions/ioe.md`: Institute of Engineering (IOE), Tribhuvan University (Pulchowk Campus, IOE Graduate Conference proceedings, JIE journal, and TUCL master's theses).
  - `wiki/institutions/nepjol.md`: Nepal Journals Online (national DOI journal indexer archiving domestic publications across JACEM, JHCoE, KJSE, JIE, and Nepalese Linguistics).
- **Verification**: `python3 tools/wiki_cli.py lint` executed with 0 errors and 0 warnings.


---

### [2026-11-02] Comprehensive File-by-File Audit & Synthesis of `raw/glossary`
- **Author**: Antigravity AI Agent
- **Action**: Conducted manual, file-by-file inspection of `raw/glossary/` folders (`languages/`, `linguistics/`, `algorithms/`, `models/`, `datasets/`), cross-checking facts and verifying live links against Zenodo, Hugging Face, arXiv, and Kaggle.
- **Created & Updated Nodes**:
  - `wiki/concepts/languages_of_nepal.md`: Synthesized 11 regional languages across Indo-Aryan (Maithili, Bhojpuri, Tharu, Doteli, Angika, Magahi) and Sino-Tibetan (Newar, Tamang, Magar, Gurung, Limbu, Sherpa) families, detailing scripts (Devanagari, Prachalit, Ranjana, Sirijunga).
  - `wiki/concepts/nlp_evaluation_metrics.md`: Compiled standard evaluation metrics (WER, CER, MOS, chrF++, BLEU, COMET, ROUGE, BPB, F1) and benchmarks (Nep-gLUE, NLUE, IndicGLUE, UD).
  - `wiki/concepts/devanagari_phonology_and_orthography.md`: Detailed abugida mechanics, schwa deletion rules, matras, anusvara vs. chandrabindu, yuktakshar ligatures, and G2P phonetic mapping.
  - `wiki/concepts/nepali_morphosyntax_and_grammar.md`: Mapped nominal case markers (vibhakti), honorific agreement tiers (anadar, madhyam, uchha, maha aadar), compound verb serialization, and IndoWordNet synset ontology.
  - `wiki/models/nepaligpt.md`: Verified open-weights generative model series (`universalml/NepaliGPT-2.0` on Hugging Face, arXiv:2405.00690).
  - `wiki/datasets/multimodal_sign_and_vision_datasets.md`: Curated verified multimodal benchmarks: Nepali Sign Language Video Dataset NSL23 (Zenodo: `10.5281/zenodo.10478554`), NSL character image dataset (Kaggle), DHCD Devanagari character set, and cultural image captioning sets.
- **Verification**: `python3 tools/wiki_cli.py lint` executed across all 38 files with 0 errors and 0 warnings.


---

### [2026-11-02] Comprehensive Audit of `raw/glossary/datasets` and `raw/glossary/papers`
- **Author**: Antigravity AI Agent
- **Action**: 
  - Scanned and cross-verified entries across `raw/glossary/datasets` (speech, text, vision, benchmark) and `raw/glossary/papers` against official registries (OpenSLR, Hugging Face, Kaggle, ACL Anthology, IEEE, arXiv).
  - Enriched `wiki/datasets/speech_datasets.md` with:
    - OpenSLR 43 (Google multi-speaker Nepali TTS)
    - OpenSLR 143 (Nepali male & female paired studio TTS)
    - Mozilla Common Voice (Nepali scripted read speech)
    - LDC-IL (43-hour sentence aligned corpus)
    - AI4Bharat Rural Women Bhojpuri speech corpus
    - Nepali Parliamentary Speech Dataset (Kaggle)
  - Enriched `wiki/datasets/multimodal_sign_and_vision_datasets.md` with:
    - Nepali Flickr8k Captioning (40,000 paired captions)
    - Nepali Handwriting Dataset NHD (`dahalsweekar`)
    - TrOCR synthetic lines (`prashant0919`)
  - Enriched `wiki/datasets/translation_datasets.md` with:
    - NepTam (ILPRL Nepali-Tamang LREC benchmark)
    - MaithiliMT multi-domain parallel corpus
    - Alpaca Nepali SFT instruction tuning corpus
  - Enriched `wiki/datasets/sentiment_datasets.md` with:
    - NepCov19Tweets (39k+ tweets on Hugging Face & Kaggle)
  - Enriched `wiki/papers/classification_papers.md` with verified ACL Anthology and IEEE publications (Offensive language detection, continuous sign language recognition).
- **Verification**: `python3 tools/wiki_cli.py lint` executed across 38 files with 0 errors and 0 warnings.


---

### [2026-11-02] In-Depth Synthesis of Question Answering, Vision, Pretraining, and Academic Literature
- **Author**: Antigravity AI Agent
- **Action**:
  - Filtered hallucinated synthetic entries (e.g., non-existent 2026 arXiv papers and co-author hallucinations) from `raw/glossary/` through discrete registry verification.
  - Created dedicated OKF node: `wiki/datasets/qa_and_instruction_datasets.md` cataloging verified Question Answering and SFT benchmarks:
    - Reading Comprehension & General QA: Nepali Belebele QA (`Yunika/Nepali-QA`), Nepali SQuAD (`Bibek1129/nepali_SQuAD`), Nepali Textbook QA (`dineshkarki/textbooks-qa-nepali`), NLUE QA Suite (`IRIIS-RESEARCH/NLUE`).
    - Domain QA: Nepal Legal QA Benchmark (`chhatramani/nepal-legal-qa-benchmark_v1`), Nepal Constitution QA (`chhatramaniyadav/nepal-constitution-qa-dataset-en`), Nepali Health QA (`NepaliAI/Nepali-Health-QA`), English-Nepali Medical Parallel QA (`Bibek-Poudel/ENG_NEP_MED_PARALLEL`).
    - SFT & Instruction Tuning: Alpaca Nepali SFT (`Saugatkafley/alpaca-nepali-sft`), Translation Instruction SFT (`ashokpoudel/English-Nepali-Translation-Instruction-Dataset`), TharuChat Multi-Dialect SFT (`prajwal-panth/tharu-chat`).
  - Enriched `wiki/datasets/monolingual_text_datasets.md` with:
    - `neBrahma-Nepali-Pretrain-Corpus` (2B token pretraining corpus), Titung Nepali Books text corpus, Himalaya AI Nepali compile, Team-Naya `nlp-doko` (350k sentences).
    - Regional pretraining corpora: BhojpuriCorpus (`Satyam810/BhojpuriCorpus`), MaithiliCorpus (`AiventraLab/maithili-corpus`), and Purvanchal linguistic resources (`singhakr/Bhojpuri-Magahi-and-Maithili-Linguistic-Resources`).
    - Official public civic repositories: Nepal Law Commission (`lawcommission.gov.np`), Nepal Gazette / Rajpatra (`rajpatra.dop.gov.np`), Supreme Court verdicts (`supremecourt.gov.np`), and Open Data Nepal (`opendatanepal.com`).
  - Enriched `wiki/datasets/lexicon_wordnet_datasets.md` with:
    - Digital *Nepali Brihat Sabdakosh* (`Titung/nepali-brihat-sabdakosh` on Hugging Face - 60,000+ definitions).
    - Nepali spellchecker lexical graph (`NishantLuitel/Nepali-Spell-Checker` on GitHub).
    - DACON diachronic Newar lexical corpus (Zenodo: `10.5281/zenodo.12887386`).
  - Enriched `wiki/datasets/multimodal_sign_and_vision_datasets.md` with:
    - Titung Nepali Books OCR dataset (`Titung/nepali-books-ocr-dataset-full`), Himalaya AI Devanagari OCR (`himalaya-ai/devanagari_ocr_dataset`).
    - Parikar Nepali Food dataset (`aaravsubedi/parikar-nepali-food`), Nepali Celeb Localized Faces (`amitpant7`), and ethnic facial emotion dataset (`suchanasubedi`).
  - Enriched `wiki/datasets/speech_datasets.md` with:
    - `tonibirat/nepali-asr-benchmark-50gb`, cleaned OpenSLR (`spktsagar`), Whisper FT audio (`Firoj112`), Kokoro TTS (`Firoj112`), and deepfake detection audio (`bibekshrestha2070`).
  - Enriched `wiki/datasets/summarization_datasets.md` with:
    - Dhakal Nepali News Summarization (`dhakal2444/nepali-news-dataset`) and ICISCT 2025 benchmark.
  - Enriched `wiki/datasets/ner_datasets.md` with:
    - Setopati NER (`oya163/nepali-ner`), Dadelani low-resource NER, and Merishna Suwal offensive NER (`merishnasuwal`).
  - Enriched `wiki/datasets/classification_datasets.md` with:
    - NeCCo Cultural Commonsense benchmark (`nepali-nlp/necco-benchmark`), `np20ng` (Nepali 20 Newsgroups), and Spandyie news dataset.
  - Enriched `wiki/datasets/sentiment_datasets.md` with:
    - NepEMO multi-label emotion dataset (arXiv:2512.22823) and tourism reviews dataset (`Safal08`).
  - Enriched `wiki/concepts/newa_computational_linguistics.md` with DACON Diachronic Newar Corpus (`10.5281/zenodo.12887386`).
  - Audited and verified academic publications across `wiki/papers/`:
    - `speech_papers.md`: Added Ghimire et al. (arXiv:2402.03050), Maharjan et al. (arXiv:2406.17825), Poudel et al. (arXiv:2411.12587), IEEE HMM ASR (`10.1109/icmlc.2017.8107745`), Maithili TTS (`10.1109/conecct47791.2019.9012903`), and AI4Bharat Next Billion ASR (`2111.03945`).
    - `translation_papers.md`: Added morphology-aware segmentation (`2103.11189`), WMT19 similar languages (`1908.06138`), grammar book LLM translation (`2409.19151`), BhashaVerse (`2412.04351`), and domain-specific MT (`10.3844/jcssp.2025.3041.3050`).
    - `morphology_pos_papers.md`: Added rule-based stemmer (arXiv:2002.09901), BiLSTM-CRF POS tagging (`10.1007/s11042-023-15679-1`), ANN POS (`10.5121/ijnlc.2018.7302`), affix removal stemmer (`10.5120/15882-3439`), and compound word splitting (`10.36548/jitdw.2022.3.007`).
    - `sentiment_papers.md`: Added IEEE CCIP bootstrap sentiment (`10.1109/ccip.2015.7100739`), NepEMO multi-label emotion (`2512.22823`), COVID-19 tweets classification (`2210.05425`), and multi-channel CNN (`2203.10286`).
    - `classification_papers.md`: Added anaphora resolution (`10.1109/compe49325.2020.9200135`), Monte Carlo plagiarism detection (`10.1109/cccs.2018.8586841`), LinCE code-switching benchmark (`2005.04322`), and FIRE NLU Devanagari challenge papers (`2412.08163`, `2412.17947`, `2412.17131`).
    - `ocr_papers.md`: Added optical text recognition transfer learning (`2404.02375`), RoundTripOCR (`2412.15248`), continuous sign language deep learning (`10.1109/icict60155.2024.10544519`), and video captioning (`2311.02699`).
    - `language_modeling_papers.md`: Added BERT-based grammatical error correction (`10.1109/inspect63485.2024.10896043`), prompt-based political topic modeling (`10.1109/icict64420.2025.11004776`), subword cross-lingual transfer (`10.18653/v1/2022.sigmorphon-1.7`), perplexity & tokenization study (`2404.18071`), and Passage to India embeddings (`2112.13800`).
    - `wordnet_wsd_papers.md`: Added Prasain et al. (IEEE NLP-KE 2008, `10.1109/nlpke.2008.4906758`).
- **Verification**: `python3 open_for_discussion/nepali_nlp_wiki/tools/wiki_cli.py lint` executed across all 39 files with 0 errors and 0 warnings.


---

### [2026-11-02] Ingestion of Multilingual Foundation Models, Code-Switching, and Institutional Leadership
- **Author**: Antigravity AI Agent
- **Action**:
  - Synthesized foundational multilingual model capabilities across IndicBERT, IndicTrans2, NLLB-200, mT5, mBART-50, and Whisper into a dedicated OKF node: `wiki/models/multilingual_foundation_models.md`.
  - Created dedicated concept node: `wiki/concepts/code_switching_and_romanized_nepali.md` detailing Romanized Nepali (Nepanglish), phonetic spelling ambiguities (lack of standardization), intra-/inter-sentential mixing, matrix language frame morphology, language identification (LID), and transliteration.
  - Enriched academic institution nodes with faculty leaders, lab directors, and principal investigators:
    - `wiki/institutions/ilprl.md`: Prof. Dr. Bal Krishna Bal (Director, pioneer of computational morphology and Nelralec).
    - `wiki/institutions/ioe.md`: Dr. Basanta Joshi, Dr. Aman Shakya, Dr. Arun Kumar Timalsina, Dr. Surendra Shrestha, and Dr. Sanjeeb Prasad Panday.
    - `wiki/institutions/naamii.md`: Dr. Binod Bhattarai, Dr. Danda Pani Paudel, and Dr. Bishesh Khanal.
    - `wiki/institutions/ltk.md`: Madan Puraskar Pustakalaya partnership, NepaLinux operating system, and PAN Localization initiatives.
- **Verification**: `python3 open_for_discussion/nepali_nlp_wiki/tools/wiki_cli.py lint` passed across 41 files with 0 errors and 0 warnings (Total compiled OKF nodes: 40).


---

### [2026-11-02] Comprehensive Dataset Cross-Check & Global Registry Integration
- **Author**: Antigravity AI Agent
- **Action**:
  - Cross-referenced user-provided Google Dataset Search, Kaggle, Hugging Face, IEEE DataPort, and Mendeley Data queries against wiki dataset nodes.
  - Enriched `wiki/datasets/monolingual_text_datasets.md`:
    - Added Rabindra Lamsal's landmark *A Large Scale Nepali Text Corpus* (90M+ words on IEEE DataPort, DOI: `10.21227/jxrd-d245`).
    - Added `silytics/Nepali-Text-Corpus` on Hugging Face.
    - Added `Boredoom17/Nepali-Flow-Roman` (307,000+ Romanized informal comments on Hugging Face).
    - Added digitized religious corpora (`lilgoose777/nepali-bible-corpus` and `dineshkarki/bhagavad-gita-nepali`).
    - Added Kaggle Wikipedia articles (`disisbig/nepali-wikipedia-articles`).
  - Enriched `wiki/datasets/classification_datasets.md`:
    - Added Ashok Kumar Pant's *Nepali News Dataset (Large)* on Kaggle (including Agriculture, Politics, Sports, Business).
    - Added *Setopati Fresh Nepali News Dataset* on Kaggle (`sanjaybhandari`).
    - Added *NaBI (Nepali Bias & Information Dataset)* on Hugging Face (`Utkarsha666/NaBI`).
    - Added *Code-Switched Customer Support Intents* on Kaggle (`sarveshchhetri` - 10k+ multi-intent queries).
  - Enriched `wiki/datasets/sentiment_datasets.md`:
    - Added *Nepal Border Sentiment Dataset* on Kaggle (`samirasharma` - geopolitical public sentiment on Lipulekh/Kalapani).
    - Added *Romanized Nepali Sentiment Analysis Dataset* on Kaggle.
  - Enriched `wiki/datasets/qa_and_instruction_datasets.md`:
    - Added *IndicDialogue Dataset* on Mendeley Data / NIH (DOI: `10.17632/wcb4bxbyxx.2` - conversational dialogues covering Nepali).
    - Added *Nepal Constitution Dataset* on Hugging Face (`ranjitraut/nepal-constitution-dataset` - 308 articles structured).
    - Added *Nepal Constitution Instruction QA* on Hugging Face (`nordenxgt`).
    - Added *Nepal Kanoon Patrika (NKP)* digitized Supreme Court law report archives (`nkp.gov.np`).
    - Added *Nepali Health Q&A Corpus* on Kaggle.
  - Enriched `wiki/datasets/summarization_datasets.md`:
    - Added *NEPHEAD News-Headline Corpus* on Hugging Face (`dsunil/NEPHEAD` - 261,101 news-headline pairs).
  - Enriched `wiki/datasets/translation_datasets.md`:
    - Added *Roman to Nepali Transliteration Dataset* on Hugging Face (`rajeshrai577/roman-to-nepali-dataset`).
    - Added *English to Nepali Translation Dataset* on Kaggle.
  - Enriched `wiki/concepts/newa_computational_linguistics.md`:
    - Added *Literature Scraped Text Corpus for Newari Language* on Kaggle.
- **Verification**: `python3 open_for_discussion/nepali_nlp_wiki/tools/wiki_cli.py lint` passed across 41 files with 0 errors and 0 warnings.


---

### [2026-11-02] Comprehensive Ingestion & Curation of Google Scholar 2025–2026 Academic Papers
- **Author**: Antigravity AI Agent
- **Action**:
  - Ingested and parsed all 1,696 lines across `raw/scholar2026.md` and `raw/scholar2025.md`.
  - Filtered out irrelevant non-NLP publications (e.g. medical pathology, oncology, groundwater hydrology, civil engineering, zoology).
  - Strictly selected peer-reviewed academic publications on Nepali NLP, Devanagari computational linguistics, and regional languages of Nepal (Newar/Nepal Bhasha, Tamang, Bhojpuri, Maithili, Achhami).
  - Deduplicated normalized titles against existing wiki bibliographies and synthesized **158 newly discovered publications** across 8 concept paper nodes:
    - `wiki/papers/translation_papers.md` (+7 papers): NepTam LREC parallel benchmark (Ghimire et al.), NepOOC-M multimodal bilingual benchmark, clinical translation fine-tuning (Ahmadnia et al.), gender bias in Nepali MT (Khadka & Bhattarai), and sign-to-speech translation.
    - `wiki/papers/sentiment_papers.md` (+19 papers): NEPSEE double-annotated benchmark (Baral et al.), NepaliXlit Romanized-to-Devanagari sentiment enhancement (Patel et al., ACL), MLESA-Net Reddit emotion analysis, and differential privacy fine-tuning on NepaliBERT.
    - `wiki/papers/ner_papers.md` (+22 papers): Achhami dialect NER & POS tagging (Dhamala et al., ACL SIGUL), low-resource event extraction with trigger phrase identification (Maharjan et al., ACL), and NepLEGiT legal entity extraction.
    - `wiki/papers/language_modeling_papers.md` (+79 papers): Nepali Passport QA (Begha, Acharya, Bal), ACM SIGIR Nepali information retrieval benchmark (Acharya & Bal), headline generation with monolingual/multilingual transformers (Dahal & Fujita, ACM TALLIP), NELSR legal case-to-statute retrieval, and NepGradeQA automated short-answer grading.
    - `wiki/papers/classification_papers.md` (+16 papers): Sentence-level topic classification benchmarking (Karki et al.), DistilBERT grievance classification (Thapaliya & Joshi), and code-mixed abusive language detection.
    - `wiki/papers/morphology_pos_papers.md` (+7 papers): Nepali lemmatization with multilingual transformers (Regmi, Dawadi, Bal, ACL), morphology-guided pre-tokenization (Shrestha & Pradhan), Pahari POS-tagged corpus, Prasta Nepali automated Byakaran grammar error correction, and NeDIOM Nepali idioms benchmark.
    - `wiki/papers/speech_papers.md` (+7 papers): Nwāchā Munā Nepal Bhasha speech corpus and proximal transfer ASR, SpeakPay financial speech recognition with LoRA, reward-guided Whisper fine-tuning, and NepConformer.
    - `wiki/papers/ocr_papers.md` (+1 paper): Structured information extraction from Nepali scanned documents using layout transformer and LLMs (Neupane et al., ACL).
- **Verification**: `python3 open_for_discussion/nepali_nlp_wiki/tools/wiki_cli.py lint` passed across all 41 files with 0 errors and 0 warnings (Total cataloged papers: 384+).


---

### [2026-11-02] Ingestion & Curation of Expanded Scholar 2025 Academic Literature
- **Author**: Antigravity AI Agent
- **Action**:
  - Ingested and parsed the expanded `raw/scholar2025.md` dump (expanded from 163 to 2,199 lines).
  - Filtered out irrelevant non-NLP entries (e.g. power side-channels, dentistry, orthopedics, qualitative sociological essays, pest control).
  - Extracted and deduplicated strictly relevant Nepali, Nepal Bhasha, and regional NLP research papers from 2024–2025.
  - Appended **63 newly validated publications** across 8 concept paper nodes:
    - `wiki/papers/language_modeling_papers.md` (+30 papers): TikNep TikTok NLP content analysis (Dhakal et al.), politico-economic bias in Nepali LMs (Thapa, Rauniyar et al., ACL), knowledge graph information extraction (Ghimire, Panday, Shakya), and judicial AI in Nepal.
    - `wiki/papers/translation_papers.md` (+8 papers): Bidirectional statistical MT for English-Nepali (Roy, Purkayastha, Paul), legal domain bidirectional MT (Poudel, Bal, Acharya), and ASL-to-Nepali translation (Paneru et al.).
    - `wiki/papers/speech_papers.md` (+7 papers): Low-resource corpus development strategies (Bal, Prasain, Ghimire), declarative intonation classification (Subba et al.), endangered language E2E ASR (Meelen, O'Neill, Coto-Solano), large vocabulary continuous speech recognition (Paudel, Bal, Shrestha), and pronunciation-aware syllable tokenizers (Ghimire, Bal, Prasain).
    - `wiki/papers/ner_papers.md` (+6 papers): Large language model potential for Nepali NER & POS (Subedi, Regmi, Bal), Hindi-Nepali cross-lingual NER (Yadav et al.), DanfeNER in Nepali tweets (Niraula & Chapagain), and BERT-based NER (Pande, Shakya, Panday, Joshi).
    - `wiki/papers/sentiment_papers.md` (+4 papers): Sentence embedding evaluation for sentiment (Adhikari, Wagle, Khanal), tweet sentiment analysis with transformers (Zimmer & Tripathee), and COVID-19 aspect-based sentiment (Parajuli, Devkota, Tamrakar; Regmi, Shakya, Joshi).
    - `wiki/papers/morphology_pos_papers.md` (+3 papers): Parts-of-speech tagging with BiLSTM-CRF-HMM (Pradhan & Yajnik), Nepali dependency parsing with transfer learning (Pandey, Shakya, Joshi), and spelling correction with ensemble learning (Bhattarai, Shakya, Joshi).
    - `wiki/papers/classification_papers.md` (+3 papers): BiLSTM profanity and offensiveness detection (Adhikari, Manandhar, Khanal), deep neural network news classification (Sah thesis), and NeHate hate speech dataset (Thapa, Rauniyar, Shiwakoti, ECAI).
    - `wiki/papers/ocr_papers.md` (+2 papers): Offline Nepali handwritten word recognition with deep learning (Vaidya & Bal) and RoundTripOCR post-OCR error correction (Kashid & Bhattacharyya).
- **Verification**: `python3 open_for_discussion/nepali_nlp_wiki/tools/wiki_cli.py lint` passed across all 41 files with 0 errors and 0 warnings (Total cataloged papers: 447+).

---

### [2026-11-02] Curation & Ground-Truth Extraction of Notes Dumps (18 Files)
- **Author**: Antigravity AI Agent
- **Action**:
  - Moved 18 files from `local/notes_dumps/` into `open_for_discussion/nepali_nlp_wiki/raw/notes_dumps/`.
  - Confirmed and executed deletion of unreferenced directory `raw/glossary/`.
  - Screened files to cleanly separate verifiable ground truth from opinionated notes and uncompleted benchmark proposals ("BalEval" / hypothetical model roadmaps) to prevent contaminating the wiki.
  - Extracted authentic historical, linguistic, and bibliographical knowledge into canonical wiki nodes:
    - `wiki/institutions/ilprl.md`: Enriched with the complete 5 historical research eras spanning 22 years (2004–2026), key faculty/alumni collaborators, and foundational milestones.
    - `wiki/concepts/nepali_morphosyntax_and_grammar.md`: Enriched with formal Paninian Karaka Theory (6 Karakas: Karta, Karma, Karana, Sampradana, Apadana, Adhikarana), dependency demand triad (Akanksha, Yogyata, Sannidhi), split ergativity rules, and agglutinative clitic stacking order.
    - `wiki/papers/ocr_papers.md`: Added Nepal Script CRNN-CTC OCR (Nakarmi et al., SIGUL 2024 / LREC 2026).
    - `wiki/papers/translation_papers.md`: Added trilingual English-Nepali-Tamang MT benchmark and PCDT toolkit (Acharya et al., EAMT 2026) and legal MT (Poudel et al., SIGUL 2024).
    - `wiki/papers/language_modeling_papers.md`: Added NepLEGiT pretrained legal transformer (Raut et al., 2026).
    - `wiki/papers/sentiment_papers.md`: Added profanity and offensiveness detection (Adhikari et al., ICON 2024).
  - Cross-verified public dataset coverage against the 564 HuggingFace catalog in `dataset_index.md`.
  - Deleted temporary `raw/notes_dumps/` files after complete review as instructed.
- **Verification**: `python3 open_for_discussion/nepali_nlp_wiki/tools/wiki_cli.py lint` passed across all 41 files with 0 errors and 0 warnings.

---

### [2026-11-02] Construction of Flat Dataset Downloader & Nelralec POS Tagset Node
- **Author**: Antigravity AI Agent
- **Action**:
  - Restructured legacy speculative `open_for_discussion/datasets/` into `open_for_discussion/dataset_downloader/`.
  - Established a flat 3-way taxonomy: `sft/` (Gemma instruction tuning, TTS excluded), `pretrain/` (causal LM text), and `similarity/` (Gemma Embedding 2 retrieval pairs).
  - Authored verified, fact-checked YAML workflows for Hugging Face (`Bibek1129/nepali_SQuAD_multiple_qsns`, `Sakonii/nepalitext-language-model-dataset`, `jangedoo/nepali-nli-20k`), GitHub (`UniversalDependencies/UD_Nepali-BK`), and Kaggle (`disisbig/nepali-wikipedia-articles`).
  - Created standalone CLI harness `downloader.py` featuring a zero-clutter `test` mode (downloads 5 samples to a temporary buffer, validates, prints, and automatically purges).
  - Formulated `.agent/` autonomous curation protocol (web search -> inspect webpage -> sample -> map -> output) and schema contracts.
  - Conformed user's new node `wiki/concepts/nepalitagsetpos.md` to OKF v0.2 frontmatter specifications.
- **Verification**: `python3 open_for_discussion/nepali_nlp_wiki/tools/wiki_cli.py lint` passed across all 42 files with 0 errors and 0 warnings.







