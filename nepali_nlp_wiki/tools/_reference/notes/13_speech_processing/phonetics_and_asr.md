# Speech Processing: ASR & TTS

> [!IMPORTANT] Gist
> Speech processing bridges the gap between acoustic signals and text. **Automatic Speech Recognition (ASR)** converts audio to text, while **Text-to-Speech (TTS)** synthesizes human-like speech from text (Jurafsky & Martin, 2026).

## 1. Phonetics and Feature Extraction
- **Phonemes**: The smallest units of sound that distinguish meaning.
- **Log Mel Spectrum**: A representation of audio that emphasizes frequencies human ears are most sensitive to.
- **MFCCs**: Mel-Frequency Cepstral Coefficients, a standard feature for speech recognition.

## 2. Automatic Speech Recognition (ASR)
- **Task**: $Y^* = \text{argmax}_Y P(Y|X)$ (Find text $Y$ with highest probability given audio $X$).
- **Architectures**: Convolutional Neural Networks (CNNs), Encoder-Decoder (Whisper), and **CTC** (Connectionist Temporal Classification).
- **Metric**: **Word Error Rate (WER)** = $\frac{S + D + I}{N}$.

## 3. Text-to-Speech (TTS)
- **VALL-E / Audio Tokens**: Modern TTS treats audio as discrete tokens, using language models to predict the acoustic sequence.
- **Evaluation**: Mean Opinion Score (MOS) - human rating of naturalness.

---

#speech #asr #tts #phonetics
