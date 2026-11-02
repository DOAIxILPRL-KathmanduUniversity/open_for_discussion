---
okf_version: "0.2"
type: "dataset"
title: "Nepali Speech Datasets (ASR & TTS)"
description: "Curated collection of automatic speech recognition (ASR) and text-to-speech (TTS) audio corpora for the Nepali language."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T10:00:00Z"
modality: "audio"
task: "speech-processing"
language:
  - "ne"
script: "Devanagari"
tags:
  - speech
  - asr
  - tts
  - audio-corpora
---

# Nepali Speech Datasets (ASR & TTS)

## Overview
Speech technology in Nepali requires clean, transcribed acoustic corpora with phonetically balanced phonetic representations. This node aggregates the primary open speech corpora identified in the literature.

## Curated Datasets

| Dataset | Type | Description | Source / Access |
| :--- | :--- | :--- | :--- |
| **OpenSLR 54 (Large Nepali ASR)** | ASR | 150,000+ utterances; large-scale crowd-sourced read speech corpus in Nepali with Devanagari text transcriptions. | [OpenSLR 54](https://www.openslr.org/54/) |
| **OpenSLR 43 (Nepali TTS)** | TTS | High-quality multi-speaker female TTS dataset collected by Google with phonetically aligned `line_index.tsv` transcripts (CC BY-SA 4.0). | [OpenSLR 43](https://www.openslr.org/43/) |
| **OpenSLR 143 (Nepali TTS Male/Female)** | TTS | Extended multi-speaker dataset explicitly providing paired male and female studio speech recordings for Tacotron 2 and acoustic modeling (CC BY-NC-SA 4.0). | [OpenSLR 143](https://www.openslr.org/143/) |
| **tonibirat Nepali ASR Benchmark** | ASR | 50 GB normalized speech benchmark for cross-architecture evaluation of Whisper, Conformer, and Wav2Vec2 models on Nepali. | [Hugging Face](https://huggingface.co/datasets/tonibirat/nepali-asr-benchmark-50gb) |
| **Cleaned OpenSLR Nepali ASR** | ASR | Audited and noise-scrubbed subset of OpenSLR 54 with invalid Unicode transcriptions removed for end-to-end CTC training. | [Hugging Face: spktsagar](https://huggingface.co/datasets/spktsagar/openslr-nepali-asr-cleaned) |
| **Nepali ASR Whisper Fine-tuning Data** | ASR | Standardized audio-text splits adapted for OpenAI Whisper fine-tuning across diverse acoustic conditions. | [Hugging Face: Firoj112](https://huggingface.co/datasets/Firoj112/nepali-asr-whisper) |
| **Combined SLR Nepali TTS** | TTS | Merged and volume-normalized speech corpus uniting SLR43 and SLR143 studio recordings for Tacotron2 and VITS synthesis. | [Hugging Face: lilgoose7777](https://huggingface.co/datasets/lilgoose7777/slr-combined-nepali-tts) |
| **Kokoro Nepali TTS Fine-Tuning Corpus** | TTS | High-fidelity 24kHz single-speaker aligned dataset prepared for training Kokoro-82M TTS voices in Nepali. | [Hugging Face: Firoj112](https://huggingface.co/datasets/Firoj112/nepali-kokoro-ft-data) |
| **Nepali Audio Deepfake Dataset** | Audio / Safety | Paired real and synthesized audio clips for benchmarking synthetic speech and voice clone detection models in Nepali. | [Hugging Face: bibekshrestha2070](https://huggingface.co/datasets/bibekshrestha2070/nepali-audio-deepfake-dataset) |
| **Mozilla Common Voice Nepali** | ASR | Crowd-sourced multi-accent scripted read speech corpus with gender and age demographic metadata. | [Common Voice](https://commonvoice.mozilla.org/ne) / [Hugging Face](https://huggingface.co/datasets/deepdml/common_voice_26_0) |
| **OpenSLR 84 (Spoken Newar / Nepal Bhasa)** | ASR | Crowd-sourced spoken audio dataset covering spontaneous and read Nepal Bhasa utterances. | [OpenSLR 84](https://www.openslr.org/84/) |
| **Faith Comes By Hearing (FCBH) Bible Audio** | Audio | Long-form spoken Nepali audio recordings spanning chapter-verse alignments across regional dialects. | [FCBH Audio](https://www.faithcomesbyhearing.com/) |
| **LDC-IL Nepali Speech Corpus** | ASR | 43 hours of sentence-aligned continuous speech across regional Nepali dialects recorded by Language Data Consortium for Indian Languages. | [LDC-IL](https://ldcil.org/) |
| **Rural Women Bhojpuri ASR Dataset** | ASR | Targeted regional Terai speech dataset collecting authentic maternal and agricultural dialects for inclusive ASR. | [AI4Bharat / Hugging Face](https://huggingface.co/datasets/ai4bharat/Rural_Women_Bhojpuri) |
| **Nepali Parliamentary Speech Dataset** | ASR | Transcribed legislative audio recordings from parliamentary debates featuring diverse oratorical speeds and formal registers. | [Kaggle](https://www.kaggle.com/datasets/ishworsubedii/nepali-speech-to-text-dataset) |
| **sanoTTS & tamracar Speech Repositories** | TTS | Open-source end-to-end Tacotron and ESPnet pipelines trained on Nepali phonetics. | [GitHub: Ampixa](https://github.com/Ampixa/sanoTTS) / [GitHub: tamracar](https://github.com/tamracar/nepali-tts) |

## Interconnected Graph Nodes
- **Papers**: [Speech Processing Papers](wiki/papers/speech_papers.md)
- **Institutions**: [ILPRL](wiki/institutions/ilprl.md), [Language Technology Kendra](wiki/institutions/ltk.md)

