# Text-to-Speech (TTS)

> [!IMPORTANT] Gist
> TTS (Speech Synthesis) is the inverse of ASR. It converts symbolic text into an acoustic waveform. Modern neural TTS produces speech that is often indistinguishable from human voices.

## 1. The TTS Pipeline
1.  **Text Frontend**:
    - **Normalization**: "St." $\rightarrow$ "Street" or "Saint" (Context dependent).
    - **Grapheme-to-Phoneme (G2P)**: Converting written characters to phonetic sounds (e.g., `knife` $\rightarrow$ `/naɪf/`).
2.  **Acoustic Model**: Maps phonemes/text to acoustic features (like Mel-Spectrograms).
    - **Classic**: Unit Selection (stitching recorded clips).
    - **Neural**: Tacotron, FastSpeech.
3.  **Vocoder**: Converts the abstract acoustic features (spectrogram) into an actual audio waveform (PCM).
    - **Classic**: Griffin-Lim.
    - **Neural**: WaveNet, HiFi-GAN, WaveGlow.

## 2. Key Challenges
- **Prosody & Intonation**: Making the voice sound natural rather than "robotic." Capturing emotion, rhythm, and stress.
- **Homographs**: "I read (past) the book" vs. "I read (present) the book."
- **Efficiency**: Generating high-fidelity audio in real-time on low-power devices.

## 3. Advanced Neural Architectures
- **Autoregressive (Tacotron 2)**: Generates one frame of audio at a time. High quality but slow.
- **Non-Autoregressive (FastSpeech 2)**: Generates the entire spectrogram in parallel. Extremely fast and robust to word skipping or repeating.
- **Zero-Shot Voice Cloning**: Learning to synthesize speech in a new voice using only a few seconds of audio (e.g., Vall-E).

## 4. Evaluation Metrics
- **Mean Opinion Score (MOS)**: Human listeners rate audio from 1 (Bad) to 5 (Excellent).
- **MCD (Mel-Cepstral Distortion)**: An objective distance metric between generated and ground truth audio.

---

#speech-processing #tts #synthesis #vocoder #prosody #neural-audio
