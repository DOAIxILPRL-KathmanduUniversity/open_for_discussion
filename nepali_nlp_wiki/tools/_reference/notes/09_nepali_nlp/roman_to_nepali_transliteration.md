# Roman-to-Nepali Transliteration (Seq2Seq LSTM)

> [!IMPORTANT] Gist
> Transliteration is the process of converting text from one script (e.g., Roman/Latin) to another (e.g., Devanagari) based on phonetic similarity. This module implements a character-level Encoder-Decoder LSTM to map Romanized Nepali to its native Devanagari form.

## 1. Sequence-to-Sequence (Seq2Seq) Architecture
The model follows the classic "Thought Vector" paradigm:
- **Encoder**: An LSTM layer that processes the Roman input sequence and compresses it into a final state vector ($h, c$).
- **Decoder**: An LSTM layer initialized with the encoder's state. It predicts characters one-by-one, using the previous character as input.
- **Teacher Forcing**: During training, the actual ground truth character is fed to the decoder at each step to ensure stability.

## 2. Character-Level Tokenization
Since transliteration is a phonetic mapping at the grapheme level, we operate on **Characters** rather than words:
- **Input Vocabulary**: `[a, b, c, ..., z, <PAD>]`
- **Output Vocabulary**: `[अ, आ, क, ख, ..., ।, <PAD>, \t, \n]`
- **Special Tokens**: `\t` (Start of Sequence), `\n` (End of Sequence).

## 3. Training Dynamics
- **Dataset**: `Saugatkafley/Nepali-Roman-Transliteration` (Hugging Face).
- **Loss**: Categorical Crossentropy (predicting the probability distribution over the character set).
- **Optimization**: RMSprop is preferred for sequence models to prevent gradient explosion.

---

**Notebook**: [roman_nepali_transliteration.py](notebooks/roman_nepali_transliteration.py)

#nepali-nlp #transliteration #seq2seq #lstm #keras #deep-learning
