# Multimodal (Vision-Language) & Speech/Audio NLP
**Visual Question Answering, Chart & Document AI, Speech-to-Text & Embodied Spatial Reasoning**

> **Category Navigation**: [Back to Master Dataset Index](../dataset.md) | Total Benchmarks in Category: **28**

## 1. Domain Overview & Technical Scope
This category unites benchmarks operating at the intersection of text with visual imagery, scanned documents, technical charts, acoustic audio, and physical spatial environments. It spans visual question answering (VQA, GQA), document and chart intelligence (MMMU, ChartQA, DocVQA, MathVista), transcribed speech corpora (Common Voice, Fleurs, LibriTTS, VoxPopuli), and real-world physical spatial reasoning (PIQA, RealWorldQA, SEED-Bench).

- **Key Applied Focus**: Vision-Language Model (VLM) pretraining, automated document and invoice processing, visual search engines, voice assistants, speech-to-text subtitling, assistive technology for the visually impaired, and embodied robotics.
- **Engineering & Verification Guidance**: Format visual inputs with high-resolution patch slicing or adaptive pooling. Always evaluate against optical character recognition (OCR) and document layout parsing baselines to identify visual vs textual reasoning failures.

## 2. Category Quick-Reference Table

| Rank | Dataset / Benchmark | Core Task / Focus | Scholarly Citation Tier | Primary Applications | Details Anchor |
|:---:|:---|:---|:---|:---|:---:|
| `#17` | **GQA** | Vision-Language & Multimodal Reasoning | 4,300 (Verified Index) | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-17) |
| `#18` | **PIQA** | Vision-Language & Multimodal Reasoning | 3,938 (Verified Index) | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-18) |
| `#276` | **VQA v1 / v2** | Visual Question Answering | ~300 to ~305 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-276) |
| `#277` | **NLVR2** | Visual-Linguistic Reasoning | ~300 to ~305 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-277) |
| `#278` | **MS COCO Captions** | Image Captioning | ~300 to ~305 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-278) |
| `#280` | **Conceptual Captions (CC3M/12M)** | Vision-Language Pretraining | ~300 to ~305 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-280) |
| `#281` | **Room-to-Room (R2R)** | Vision-and-Language Nav. | ~300 to ~305 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-281) |
| `#283` | **HowTo100M** | Instructional Video-Text | ~300 to ~305 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-283) |
| `#284` | **DocVQA** | Document Visual QA | ~300 to ~305 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-284) |
| `#384` | **LJSpeech** | Single-Speaker TTS | ~150 to ~178 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-384) |
| `#385` | **LibriTTS** | Multi-Speaker Text-to-Speech | ~150 to ~178 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-385) |
| `#386` | **VCTK Corpus** | Multi-Accent Speech/TTS | ~150 to ~178 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-386) |
| `#387` | **GigaSpeech** | Multi-Domain ASR | ~150 to ~178 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-387) |
| `#388` | **VoxPopuli** | Multilingual Speech/Text | ~150 to ~178 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-388) |
| `#390` | **AudioCaps / Clotho** | Audio-to-Text Captioning | ~150 to ~178 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-390) |
| `#398` | **SemEval-2020 Task 11** | Propaganda Technique ID | ~150 to ~178 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-398) |
| `#401` | **TroFi (TroFi Metaphor Corpus)** | Vision-Language & Multimodal Reasoning | ~150 (Approx. Index) | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-401) |
| `#403` | **Figlang2020 (SemEval-2020 Task 4)** | Vision-Language & Multimodal Reasoning | ~142 (Approx. Index) | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-403) |
| `#491` | **MMMU (Massive Multi-discipline Multimodal Understanding)** | Multimodal College Reasoning | High-Velocity Frontier / ~25 to ~85 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-491) |
| `#492` | **MathVista** | Visual Mathematical Reasoning | High-Velocity Frontier / ~25 to ~85 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-492) |
| `#493` | **ChartQA** | Chart Understanding & QA | High-Velocity Frontier / ~25 to ~85 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-493) |
| `#494` | **DocVQA / InfoVQA** | Document Visual Comprehension | High-Velocity Frontier / ~25 to ~85 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-494) |
| `#495` | **OCRBench** | Optical Character Recognition | High-Velocity Frontier / ~25 to ~85 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-495) |
| `#496` | **MTVQA** | Multilingual Multimodal QA | High-Velocity Frontier / ~25 to ~85 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-496) |
| `#497` | **SEED-Bench** | Multimodal LLM Evaluation | High-Velocity Frontier / ~25 to ~85 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-497) |
| `#498` | **MME (Multimodal Large Language Model Evaluation)** | Comprehensive Vision Benchmark | High-Velocity Frontier / ~25 to ~85 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-498) |
| `#499` | **RealWorldQA** | Physical Spatial Reasoning | High-Velocity Frontier / ~25 to ~85 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-499) |
| `#500` | **WildVision / LLaVA-Bench** | In-the-Wild Multimodal Prefs | High-Velocity Frontier / ~25 to ~85 citations | Vision-Language Model (VLM) Fine-Tuning | [Inspect](#rank-500) |

---

## 3. Comprehensive Dataset Profiles

<a id="rank-17"></a>
### [Rank #17] GQA

- **Global Impact Rank**: `#17` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `GQA`
- **Core NLP Task / Domain**: `Vision-Language & Multimodal Reasoning`
- **Citation Impact**: `4,300 (Verified Index)`
- **Primary Reference & Authors**: Hudson, D. A., & Manning, C. D. (2019). GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering. CVPR 2019. https://doi.org/10.1109/cvpr.2019.00686

#### Architectural Specifications & Benchmark Details
Leveraged Visual Genome scene graphs to construct 22 million compositional visual question answering queries paired with functional programs and consistency diagnostics (Hudson & Manning, 2019).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Hudson, D. A., & Manning, C. D. (2019). GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering. CVPR 2019. https://doi.org/10.1109/cvpr.2019.00686
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-18"></a>
### [Rank #18] PIQA

- **Global Impact Rank**: `#18` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `PIQA`
- **Core NLP Task / Domain**: `Vision-Language & Multimodal Reasoning`
- **Citation Impact**: `3,938 (Verified Index)`
- **Primary Reference & Authors**: Bisk, Y., Zellers, R., Le bras, R., Gao, J., & Choi, Y. (2020). PIQA: Reasoning about Physical Commonsense in Natural Language. AAAI 2020, 7432-7439. https://doi.org/10.1609/aaai.v34i05.6239

#### Architectural Specifications & Benchmark Details
Physical Interaction Question Answering introduced a two-choice benchmark testing naive physics and everyday object affordances through goal-solution pairs in natural language (Bisk et al., 2020).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Bisk, Y., Zellers, R., Le bras, R., Gao, J., & Choi, Y. (2020). PIQA: Reasoning about Physical Commonsense in Natural Language. AAAI 2020, 7432-7439. https://doi.org/10.1609/aaai.v34i05.6239
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-276"></a>
### [Rank #276] VQA v1 / v2

- **Global Impact Rank**: `#276` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `VQA v1 / v2`
- **Core NLP Task / Domain**: `Visual Question Answering`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Balanced open-ended questions about images where each question is paired with two visually similar images that yield different answers (Agrawal et al., 2015 / Goyal et al., 2017).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-277"></a>
### [Rank #277] NLVR2

- **Global Impact Rank**: `#277` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `NLVR2`
- **Core NLP Task / Domain**: `Visual-Linguistic Reasoning`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Suhr et al., 2019

#### Architectural Specifications & Benchmark Details
Collected 107,292 examples of English sentences paired with web image pairs requiring compositional and cardinality reasoning (Suhr et al., 2019).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Suhr et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-278"></a>
### [Rank #278] MS COCO Captions

- **Global Impact Rank**: `#278` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MS COCO Captions`
- **Core NLP Task / Domain**: `Image Captioning`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Chen et al., 2015

#### Architectural Specifications & Benchmark Details
Standardized over 1.5 million human-written descriptions across 330,000 images with 5–40 reference captions per image (Chen et al., 2015).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Chen et al., 2015
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-280"></a>
### [Rank #280] Conceptual Captions (CC3M/12M)

- **Global Impact Rank**: `#280` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Conceptual Captions (CC3M/12M)`
- **Core NLP Task / Domain**: `Vision-Language Pretraining`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Sharma et al., 2018

#### Architectural Specifications & Benchmark Details
Harvested and filtered millions of web image-alt-text pairs hypernymized into clean natural language descriptions (Sharma et al., 2018).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Sharma et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-281"></a>
### [Rank #281] Room-to-Room (R2R)

- **Global Impact Rank**: `#281` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Room-to-Room (R2R)`
- **Core NLP Task / Domain**: `Vision-and-Language Nav.`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Anderson et al., 2018

#### Architectural Specifications & Benchmark Details
Collected visually grounded natural language navigation instructions inside Matterport3D real-world building environments (Anderson et al., 2018).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Anderson et al., 2018
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-283"></a>
### [Rank #283] HowTo100M

- **Global Impact Rank**: `#283` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `HowTo100M`
- **Core NLP Task / Domain**: `Instructional Video-Text`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Miech et al., 2019

#### Architectural Specifications & Benchmark Details
Compiled 136 million video clips with narrated ASR transcripts from 1.22 million instructional web videos (Miech et al., 2019).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Miech et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-284"></a>
### [Rank #284] DocVQA

- **Global Impact Rank**: `#284` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DocVQA`
- **Core NLP Task / Domain**: `Document Visual QA`
- **Citation Impact**: `~300 to ~305 citations`
- **Primary Reference & Authors**: Mathew et al., 2021

#### Architectural Specifications & Benchmark Details
Annotated 50,000 questions over 12,000 scanned industrial and historical document images requiring OCR and layout understanding (Mathew et al., 2021).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Mathew et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-384"></a>
### [Rank #384] LJSpeech

- **Global Impact Rank**: `#384` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `LJSpeech`
- **Core NLP Task / Domain**: `Single-Speaker TTS`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Ito & Johnson, 2017

#### Architectural Specifications & Benchmark Details
Public-domain speech dataset of 13,100 short audio clips and normalized transcripts from a single speaker reading non-fiction books (Ito & Johnson, 2017).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Ito & Johnson, 2017
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-385"></a>
### [Rank #385] LibriTTS

- **Global Impact Rank**: `#385` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `LibriTTS`
- **Core NLP Task / Domain**: `Multi-Speaker Text-to-Speech`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Zen et al., 2019

#### Architectural Specifications & Benchmark Details
Derived 585 hours of 24kHz speech from LibriSpeech with preserved original text casing, punctuation, and sentence splits for neural TTS (Zen et al., 2019).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Zen et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-386"></a>
### [Rank #386] VCTK Corpus

- **Global Impact Rank**: `#386` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `VCTK Corpus`
- **Core NLP Task / Domain**: `Multi-Accent Speech/TTS`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Yamagishi et al., 2019

#### Architectural Specifications & Benchmark Details
Recorded 110 English speakers with diverse regional accents reading newspaper sentences selected for phonetic balance (Yamagishi et al., 2019).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Yamagishi et al., 2019
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-387"></a>
### [Rank #387] GigaSpeech

- **Global Impact Rank**: `#387` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `GigaSpeech`
- **Core NLP Task / Domain**: `Multi-Domain ASR`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Chen et al., 2021

#### Architectural Specifications & Benchmark Details
Compiled 10,000 hours of high-quality labeled English audio from audiobooks, podcasts, and YouTube across diverse speaking styles (Chen et al., 2021).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Chen et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-388"></a>
### [Rank #388] VoxPopuli

- **Global Impact Rank**: `#388` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `VoxPopuli`
- **Core NLP Task / Domain**: `Multilingual Speech/Text`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Wang et al., 2021

#### Architectural Specifications & Benchmark Details
Extracted 400,000 hours of unlabeled speech and 1,800 hours of transcribed/translated European Parliament speeches across 23 languages (Wang et al., 2021).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Wang et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-390"></a>
### [Rank #390] AudioCaps / Clotho

- **Global Impact Rank**: `#390` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `AudioCaps / Clotho`
- **Core NLP Task / Domain**: `Audio-to-Text Captioning`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Crowdsourced natural language descriptions for environmental sound clips in the wild from AudioSet and Freesound (Kim et al., 2019 / Drossos et al., 2020).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-398"></a>
### [Rank #398] SemEval-2020 Task 11

- **Global Impact Rank**: `#398` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SemEval-2020 Task 11`
- **Core NLP Task / Domain**: `Propaganda Technique ID`
- **Citation Impact**: `~150 to ~178 citations`
- **Primary Reference & Authors**: Da San Martino et al., 2020

#### Architectural Specifications & Benchmark Details
Annotated news articles with 14 fine-grained propagandistic persuasion techniques (loaded language, straw man, appeal to fear) at span level (Da San Martino et al., 2020).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Da San Martino et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-401"></a>
### [Rank #401] TroFi (TroFi Metaphor Corpus)

- **Global Impact Rank**: `#401` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `TroFi (TroFi Metaphor Corpus)`
- **Core NLP Task / Domain**: `Vision-Language & Multimodal Reasoning`
- **Citation Impact**: `~150 (Approx. Index)`
- **Primary Reference & Authors**: Birke & Sarkar, 2006

#### Architectural Specifications & Benchmark Details
Collected 1,733 literal and metaphorical instances of 50 English verbs extracted from the Wall Street Journal corpus (Birke & Sarkar, 2006).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Birke & Sarkar, 2006
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-403"></a>
### [Rank #403] Figlang2020 (SemEval-2020 Task 4)

- **Global Impact Rank**: `#403` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `Figlang2020 (SemEval-2020 Task 4)`
- **Core NLP Task / Domain**: `Vision-Language & Multimodal Reasoning`
- **Citation Impact**: `~142 (Approx. Index)`
- **Primary Reference & Authors**: Ghosh et al., 2020

#### Architectural Specifications & Benchmark Details
Standardized English and Italian datasets for detecting and interpreting figurative language, sarcasm, metaphor, and irony in tweets and idioms (Ghosh et al., 2020).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Ghosh et al., 2020
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-491"></a>
### [Rank #491] MMMU (Massive Multi-discipline Multimodal Understanding)

- **Global Impact Rank**: `#491` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MMMU (Massive Multi-discipline Multimodal Understanding)`
- **Core NLP Task / Domain**: `Multimodal College Reasoning`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Yue et al., 2024

#### Architectural Specifications & Benchmark Details
Collected 11,500 college-level multidisciplinary multimodal questions featuring diagrams, charts, and equations (Yue et al., 2024).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Yue et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-492"></a>
### [Rank #492] MathVista

- **Global Impact Rank**: `#492` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MathVista`
- **Core NLP Task / Domain**: `Visual Mathematical Reasoning`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Lu et al., 2024

#### Architectural Specifications & Benchmark Details
Visual math problem-solving benchmark combining text, geometry diagrams, function plots, and charts (Lu et al., 2024).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Lu et al., 2024
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-493"></a>
### [Rank #493] ChartQA

- **Global Impact Rank**: `#493` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `ChartQA`
- **Core NLP Task / Domain**: `Chart Understanding & QA`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Masry et al., 2022

#### Architectural Specifications & Benchmark Details
Collected 9,600 human-written and 23,100 automated questions over complex business and scientific charts (Masry et al., 2022).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Masry et al., 2022
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-494"></a>
### [Rank #494] DocVQA / InfoVQA

- **Global Impact Rank**: `#494` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `DocVQA / InfoVQA`
- **Core NLP Task / Domain**: `Document Visual Comprehension`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Mathew et al., 2021

#### Architectural Specifications & Benchmark Details
Standardized document-centric visual question answering benchmarks over scanned technical manuals and reports (Mathew et al., 2021).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Mathew et al., 2021
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-495"></a>
### [Rank #495] OCRBench

- **Global Impact Rank**: `#495` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `OCRBench`
- **Core NLP Task / Domain**: `Optical Character Recognition`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Liu et al., 2023

#### Architectural Specifications & Benchmark Details
Diagnostic benchmark evaluating low-level text spotting, layout analysis, and handwriting recognition in VLMs (Liu et al., 2023).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Liu et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-496"></a>
### [Rank #496] MTVQA

- **Global Impact Rank**: `#496` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MTVQA`
- **Core NLP Task / Domain**: `Multilingual Multimodal QA`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Tiong et al., 2023

#### Architectural Specifications & Benchmark Details
Evaluated multimodal question answering across 10 non-Latin and Latin scripts in real-world visual contexts (Tiong et al., 2023).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Tiong et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-497"></a>
### [Rank #497] SEED-Bench

- **Global Impact Rank**: `#497` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `SEED-Bench`
- **Core NLP Task / Domain**: `Multimodal LLM Evaluation`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Li et al., 2023

#### Architectural Specifications & Benchmark Details
Generative and multiple-choice multimodal benchmark covering 12 evaluation dimensions including action recognition and spatial relation reasoning (Li et al., 2023).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Li et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-498"></a>
### [Rank #498] MME (Multimodal Large Language Model Evaluation)

- **Global Impact Rank**: `#498` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `MME (Multimodal Large Language Model Evaluation)`
- **Core NLP Task / Domain**: `Comprehensive Vision Benchmark`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Fu et al., 2023

#### Architectural Specifications & Benchmark Details
Evaluated vision-language models across 14 perception and cognition subtasks without prompt leakage (Fu et al., 2023).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Fu et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-499"></a>
### [Rank #499] RealWorldQA

- **Global Impact Rank**: `#499` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `RealWorldQA`
- **Core NLP Task / Domain**: `Physical Spatial Reasoning`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Canonical benchmark publication (see dataset documentation)

#### Architectural Specifications & Benchmark Details
Evaluated real-world physical and spatial understanding across real-world physical objects and everyday scenes (xAI, 2024).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Canonical benchmark publication (see dataset documentation)
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

<a id="rank-500"></a>
### [Rank #500] WildVision / LLaVA-Bench

- **Global Impact Rank**: `#500` (Top 500 Scholarly & Industry Corpus)
- **Canonical Benchmark Name**: `WildVision / LLaVA-Bench`
- **Core NLP Task / Domain**: `In-the-Wild Multimodal Prefs`
- **Citation Impact**: `High-Velocity Frontier / ~25 to ~85 citations`
- **Primary Reference & Authors**: Liu et al., 2023

#### Architectural Specifications & Benchmark Details
Crowdsourced multimodal preference and evaluation testbeds capturing wild user interactions with vision-language assistants (Liu et al., 2023).

#### Practical Engineering & Research Applications
- **Vision-Language Model (VLM) Fine-Tuning**: Trains models to jointly process visual scenes, diagrams, photographs, and natural language prompts.
- **Document & Chart Comprehension**: Powers financial and technical document OCR, infographic extraction, and visual question answering.
- **Speech Transcription & Translation**: Powers voice assistants, multi-speaker diarization, real-time translation, and audio captioning.

#### Reference Citation
```text
Liu et al., 2023
```

[▲ Back to Category Table](#2-category-quick-reference-table) | [Back to Master Index](../dataset.md)

---

## 4. Engineering Implementation & Pipeline Integration Guide

### Training & Fine-Tuning Recipe
When integrating datasets from **Multimodal (Vision-Language) & Speech/Audio NLP** into modern training pipelines:
1. **Preprocessing & Filtering**: Clean noisy tokens, deduplicate overlapping samples, and ensure context window length fits model architecture.
2. **Loss Function & Masking**: Align training targets with the task specification (e.g. causal masking for autoregressive models, sequence-level loss for classification).
3. **Evaluation Protocol**: Evaluate using official evaluation harnesses (e.g., `lm-evaluation-harness`, `HELM`, or task-specific test suites) to prevent benchmark leakage and prompt overfitting.

[Return to Master Index (`dataset.md`)](../dataset.md)
