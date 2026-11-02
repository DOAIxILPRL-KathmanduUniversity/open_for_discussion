---
okf_version: "0.2"
type: concept
title: "Nepali Code-Switching & Romanized Nepali (Nepanglish)"
description: "Theoretical and computational analysis of code-switching, Romanized Nepali orthography, language identification (LID), and transliteration systems."
status: stable
version: 1.0.0
timestamp: "2026-11-02T12:16:00+05:45"
domain:
  - sociolinguistics
  - code-switching
  - transliteration
  - tokenization
languages:
  - nepali
  - english
script:
  - Latin
  - Devanagari
tags:
  - code-mixing
  - romanized-nepali
  - nepanglish
  - transliteration
  - lid
---

# Nepali Code-Switching & Romanized Nepali (Nepanglish)

## Overview
In digital communication across Nepal (social media, SMS, messaging applications), users predominantly write Nepali using the Latin alphabet (**Romanized Nepali**) or switch fluidly between Nepali and English within the same sentence or conversational turn (**Nepanglish** or Nepali-English code-mixing). This poses substantial challenges for standard Natural Language Processing pipelines calibrated strictly on formal Devanagari text.

---

## 1. Orthographic Characteristics & Ambiguities

### Non-Standardized Phonetic Spelling
Unlike Devanagari, which has strict phonemic orthography, Romanized Nepali lacks any official standard transliteration standard. A single word can be spelled in dozens of phonetic variants:
- **तपाईं (You - formal)** $\rightarrow$ `tapai`, `tapaii`, `tapaai`, `tapae`, `twapaai`
- **राम्रो (Good)** $\rightarrow$ `ramro`, `raamro`, `ramroo`
- **छ (Is / Exists)** $\rightarrow$ `cha`, `chha`, `xa`, `xha`
- **धेरै (A lot)** $\rightarrow$ `dherai`, `dherei`, `dhry`

### Character Merging & Consonant Collisions
1. **Aspiration Loss**: Unaspirated vs. aspirated stops often collapse in informal typing:
   - क (*ka*) vs. ख (*kha*) $\rightarrow$ both frequently typed as `k` or `kh`.
   - त (*ta* dental) vs. ट (*ṭa* retroflex) $\rightarrow$ both typed as `t`.
2. **Sibilant Neutralization**: Devanagari distinguishes dental स (*sa*), retroflex ष (*ṣa*), and palatal श (*śa*), but informal Romanization writes all three simply as `s` or `sh`.
3. **Schwa Ambiguity**: The inherent vowel /ʌ/ is inconsistently represented by `a`, `u`, or omitted altogether (e.g., *gar-chu* vs. *garchhu* vs. *grchu*).

---

## 2. Linguistic Phenomena in Social Media

### Intra-Sentential vs. Inter-Sentential Code-Switching
- **Inter-Sentential**: Alternating full sentences between Nepali and English:
  - *"Exam siddhiyo. Now I can finally sleep for two days."*
- **Intra-Sentential**: Switching languages within a single clause or phrase:
  - *"Yo movie ko ending ekdam emotional thiyo, cried so hard."*

### Morphological Hybridization (Matrix Language Frame)
Nepali typically serves as the **Matrix Language (ML)** providing grammatical inflections, while English acts as the **Embedded Language (EL)** providing lexical roots:
- **Case Markers on English Nouns**:
  - `college-ma` (in college) $\leftarrow$ *college* + विभक्ति `-मा`
  - `ticket-ko` (of the ticket) $\leftarrow$ *ticket* + विभक्ति `-को`
  - `laptop-le` (by the laptop) $\leftarrow$ *laptop* + विभक्ति `-ले`
- **Verbalizers on English Verbs**:
  - `apply garnu` (to apply) $\leftarrow$ English verb stem + Nepali auxiliary *garnu*
  - `cancel vayo` (got cancelled) $\leftarrow$ English verb stem + Nepali intransitive *hunu/bhayo*

---

## 3. Computational Challenges & Tasks

| Task | Core Challenge | Key Approaches & Models |
| :--- | :--- | :--- |
| **Language Identification (LID)** | Word-level token classification (`ne`, `en`, `mixed`, `univ`); ambiguity of short homographs (e.g., *to*, *in*, *man*). | Character n-gram fastText, CRF taggers, mBERT token classifiers. |
| **Machine Transliteration** | Mapping unstandardized Latin spelling into normalized Devanagari script. | Syllable-level FSTs, Seq2Seq Transformers (ByT5), phonetic heuristics (`npttf2utf`). |
| **Subword Tokenizer Fertility** | Latin-tokenized LLM vocabularies (e.g., LLaMA, GPT-4) split Romanized Nepali into fragmented character subwords, inflating token counts by $3\times$ to $6\times$. | Byte-level BPE, vocabulary extension, Indic-adapted tokenizers. |
| **Abusive / Hate Speech Detection** | Obfuscated toxic words using digit-letter substitutions (e.g., `muj1`, `kukur`) and dialect slang. | Multitask BiLSTM-CRF, XLM-RoBERTa fine-tuned on code-mixed social annotations. |

---

## 4. Notable Benchmarks & Datasets

| Benchmark | Scope | Links & References |
| :--- | :--- | :--- |
| **LinCE Code-Switching Benchmark** | Centralized benchmark for linguistic code-switching evaluation across sentiment, LID, and POS. | [LinCE Benchmark](https://ritual.uh.edu/lince/) / [arXiv:2005.04322](https://arxiv.org/abs/2005.04322) |
| **FIRE NLU of Devanagari Script Languages** | Shared task evaluating hate speech and topic classification in code-mixed Devanagari social media. | FIRE Proceedings (2024) / [arXiv:2412.08163](https://arxiv.org/abs/2412.08163) |
| **Merishna Suwal Code-Mixed Sentiment & NER** | Social media comments labeled for abusive tone and targeted entities in Romanized Nepali. | [Kaggle](https://www.kaggle.com/datasets/merishnasuwal/offensive-language-ner-and-sentiment-analysis-data) |
| **Nepali-English Abusive Language Corpus** | Parallel evaluation set for code-mixed toxic text detection. | [arXiv:2504.21026](https://arxiv.org/abs/2504.21026) |

---

## Related Vault Nodes
- [[devanagari_nlp]]
- [[devanagari_phonology_and_orthography]]
- [[nepali_morphosyntax_and_grammar]]
- [[classification_datasets]]

