---
okf_version: "0.2"
type: "dataset"
title: "Nepali Multimodal, Sign Language & Vision-Language Datasets"
description: "Curated collection of verified open-access multimodal datasets for Nepali: Nepali Sign Language (NSL) video/image benchmarks, OCR character databases, and image captioning corpora."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T11:50:00Z"
modality: "multimodal"
task: "sign-language-and-vision-nlp"
language:
  - "ne"
tags:
  - multimodal
  - sign-language
  - zenodo
  - kaggle
  - vision-language
---

# Nepali Multimodal, Sign Language & Vision-Language Datasets

## Overview
Beyond purely textual corpora, multimodal NLP in Nepal encompasses video-to-sign translation, assistive vision technologies, and culturally situated image captioning. This node documents verified, publicly hosted datasets with open identifiers.

---

## 1. Nepali Sign Language (NSL) Benchmarks

| Dataset | Platform / DOI | Modality & Size | Description |
| :--- | :--- | :--- | :--- |
| **Nepali Sign Language Consonant & Vowel Video Dataset (NSL23)** | Zenodo: [`10.5281/zenodo.10478554`](https://zenodo.org/records/10478554) | 630 `.mov` videos (1,205 gestures) | Research-grade video benchmark covering 36 consonants and 13 vowels in Nepali Sign Language performed by 14 signers under diverse lighting and environmental conditions. |
| **Nepali Sign Language Character Dataset** | Kaggle: [`biratpoudelrocks/nepali-sign-language-character-dataset`](https://www.kaggle.com/datasets/biratpoudelrocks/nepali-sign-language-character-dataset) | Thousands of images | Static frame character dataset captured across plain and cluttered backgrounds for training MobileNetV2 and ResNet classification baselines. |

---

## 2. Devanagari Vision & Document OCR Datasets

| Dataset | Platform / Scope | Description |
| :--- | :--- | :--- |
| **Devanagari Handwritten Character Dataset (DHCD)** | Open Access / Kaggle | Standardized benchmark containing 92,000 isolated handwritten Devanagari character images (0-9 digits and 36 consonants) in $32 \times 32$ pixel grayscale format. |
| **Nepali Handwriting Dataset (NHD)** | GitHub: [`dahalsweekar/Nepali-Handwritten-Dataset`](https://github.com/dahalsweekar/Nepali-Handwritten-Dataset) | Camera-captured and scanned real-world Nepali handwritten text sentences and words for line/character level OCR detection. |
| **TrOCR Nepali Synthetic Lines Dataset** | Hugging Face: [`prashant0919/nepali-synthetic-ocr-lines`](https://huggingface.co/datasets/prashant0919/nepali-synthetic-ocr-lines) | Large synthetic Devanagari text-line rendering dataset for pretraining Transformer OCR architectures. |
| **Titung Nepali Books OCR Dataset** | Hugging Face: [`Titung/nepali-books-ocr-dataset-full`](https://huggingface.co/datasets/Titung/nepali-books-ocr-dataset-full) | Extensive full-page image OCR dataset comprising scanned Nepali books and printed works paired with transcribed text for fine-tuning Vision-Language and OCR models. |
| **Himalaya AI Devanagari OCR Dataset** | Hugging Face: [`himalaya-ai/devanagari_ocr_dataset`](https://huggingface.co/datasets/himalaya-ai/devanagari_ocr_dataset) | Diverse Devanagari document dataset containing multi-font printed pages and character segmentation masks. |
| **Nepali Flickr8k Captioning Dataset** | GitHub: [`bipeshrajsubedi/Flickr8k_Nepali_Dataset`](https://github.com/bipeshrajsubedi/Flickr8k_Nepali_Dataset) | 8,000 images paired with 40,000 localized Nepali descriptions (5 captions per image) for image-to-text generative vision models. |
| **Nepali Citizenship Card OCR Dataset** | Institutional / IOE GC | Cropped and annotated field recognition dataset for automated national identification extraction. |

---

## 3. Image Captioning, Culturally Situated Vision & Emotion

| Dataset | Scope / Platform | Description |
| :--- | :--- | :--- |
| **Parikar Nepali Food Classification** | Kaggle: [`aaravsubedi/parikar-nepali-food`](https://www.kaggle.com/datasets/aaravsubedi/parikar-nepali-food) | Image classification dataset covering traditional Nepali culinary dishes (Momo, Dal Bhat, Sel Roti, Yomari, Chatamari) for localized vision classification. |
| **Nepali Celeb Localized Face Dataset** | GitHub: [`amitpant7/Nepali-Celeb-Localized-Face-Dataset`](https://github.com/amitpant7/Nepali-Celeb-Localized-Face-Dataset) | Bounding box annotated face dataset of prominent Nepali public figures for facial recognition evaluation. |
| **Facial Emotion in Nepali Ethnic Groups** | Kaggle: [`suchanasubedi/facial-emotion-detection-for-nepali-ethnic-groups`](https://www.kaggle.com/datasets/suchanasubedi/facial-emotion-detection-for-nepali-ethnic-groups) | Facial expression and emotion classification corpus balanced across indigenous ethnic groups in Nepal (Aryan, Mongoloid, Newar, Tharu). |
| **Nepali Cultural Dress Dataset** | Hugging Face: [`34data/nepali-cultural-dress-dataset`](https://huggingface.co/datasets/34data/nepali-cultural-dress-dataset) | Computer vision benchmark for classifying traditional ethnic attire (Daura Suruwal, Gunyo Cholo, Haku Patasi, Bakhu). |
| **Nepali Socio-Cultural Image Captioning Corpus** | Multi-campus TU/IOE | Image-text pairs representing indigenous Nepali festivals (Dashain, Tihar, Indra Jatra), monuments, and cultural heritage paired with Devanagari descriptions. |

---

## Connected Graph Nodes
- **Toolkits**: [Nepali NLP Python Libraries](wiki/concepts/nepali_nlp_libraries.md)
- **Papers**: [OCR Papers](wiki/papers/ocr_papers.md), [Language Modeling Papers](wiki/papers/language_modeling_papers.md)
- **Institutions**: [IOE Pulchowk](wiki/institutions/ioe.md)

