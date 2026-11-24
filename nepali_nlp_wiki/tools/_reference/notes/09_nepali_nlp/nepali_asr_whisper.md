# Nepali Automatic Speech Recognition (Whisper-ASR)

> [!IMPORTANT] Gist
> Speech-to-Text for Nepali requires handling diverse accents and Devanagari script nuances. This module implements a fine-tuned Whisper model (`Whisper-Small-Nepali-ASR-OSLR54`) for high-accuracy transcription.

## 1. Model: Whisper-Small (ilprl)
The `ilprl/Whisper-Small-Nepali-ASR-OSLR54` is a transformer-based encoder-decoder model optimized for the **OSLR54** Nepali dataset.
- **Encoder**: Processes audio spectrograms into hidden representations.
- **Decoder**: Auto-regressively predicts Devanagari characters.

## 2. Inference Pipeline
Using the `transformers` library, we load the `WhisperProcessor` and `WhisperForConditionalGeneration`.
- **Sampling Rate**: 16,000 Hz (required by Whisper).
- **Batch Decoding**: `processor.batch_decode` with `skip_special_tokens=True` ensures clean Devanagari output.

## 3. UI Implementation (Gradio)
To make the model accessible, we wrap the inference logic in a **Gradio** web interface:
- **Input**: `gr.Audio(type="numpy")`.
- **Output**: `gr.Text()` (Transcribed Nepali).

---

## 4. Research Landscape: Speech Recognition
Nepali ASR has transitioned from traditional statistical models to modern end-to-end neural architectures:

- **Traditional Models (2017)**:
    - **Ssarma et al. (2017)**: HMM-based isolated word recognition, establishing baseline acoustic modeling.
- **Data Infrastructure (2018)**:
    - **Kjartansson et al. (2018)**: Released large-scale crowd-sourced speech corpora for Nepali (hosted on OpenSLR), which serves as the foundation for modern fine-tuning.
- **Neural Architectures (2019-2020)**:
    - **Regmi et al. (2019)**: Implemented RNN-CTC (Connectionist Temporal Classification) models for continuous speech.
    - **Bhatta et al. (2020)**: Combined CNN, GRU, and CTC for robust feature extraction and sequence modeling.
    - **Baral & Shrestha (2020)**: Focused on Large Vocabulary Continuous Speech Recognition (LVCSR) for Nepali.

---

**Notebook**: [nepali_asr_whisper_app.py](notebooks/nepali_asr_whisper_app.py)

#nepali-nlp #asr #whisper #speech-to-text #gradio #transformers
