# Research: Nepali Speech, Sign Language & Multimodal NLP

> [!IMPORTANT] Gist
> Multimodal Nepali NLP is rapidly expanding from ASR/TTS to Image Captioning and Sign Language Translation, leveraging transfer learning and cross-modal architectures (CNN-Transformer).

## 1. Speech Processing (ASR & TTS)

### Automatic Speech Recognition (ASR)
- **OpenSLR (SLR54)**: ~9,200 minutes of read speech.
- **Whisper Fine-tuning**:
    - **Method**: Segmented custom audio into 15-30s chunks; removed silences.
    - **Augmentation**: Added 8000Hz white noise for robustness.
    - **Impact**: Reduced WER from 54.4% (baseline) to **23.8%** (Medium model).

### Text-to-Speech (TTS)
- **Architecture**: **FastPitch** (Acoustic) + **HiFi-GAN** (Vocoder).
- **Danphe & Munal Models**: "Munal" (fine-tuned on multi-speaker SLR43) achieved a MOS of 3.70.
- **Preprocessing**: IndicXlit used to transliterate Devanagari to Roman script for acoustic processing.

## 2. Multimodal Applications

### Image Captioning
- **Dataset**: **Flickr8k_Nepali** (>40k pairs).
- **Models**:
    - **CNN-RNN**: EfficientNetB0 encoder + BiLSTM decoder.
    - **CNN-Transformer**: MobileNetV3 encoder + Transformer decoder (simplified architecture without the Transformer encoder).
- **Metrics**: BLEU-4 scores ~0.34 for RNN-based; ~0.15 for simplified Transformer decoders.

### Video Captioning
- **Dataset**: Translated MSVD corpus.
- **Best Architecture**: EfficientNetB0 + BiLSTM (1024 units). BLEU-4: 17; METEOR: 46.

### Sign Language Recognition (NSL23)
- **Sign Language to Nepali**: First public video dataset for Nepali Sign Language alphabets.
- **ASL to Nepali Translation**: fine-tuned ResNet50/VGG16 on ASL signs (99% accuracy) + gTTS for spoken Nepali output.

## 3. Specialized Multimodal Tasks
- **Structured IE (OCR)**: Extraction from scanned official notices using layout transformers.
- **Endangered Language OCR**: Using Nepali text as a high-resource anchor for OCR post-correction on **Yakkha** books.

---

#nepali #asr #tts #image-captioning #sign-language #whisper #fastpitch #multimodal
