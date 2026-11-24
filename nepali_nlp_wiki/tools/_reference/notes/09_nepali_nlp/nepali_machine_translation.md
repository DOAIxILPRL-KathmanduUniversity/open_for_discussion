# Case Study: Machine Translation for Nepali

> [!IMPORTANT] Gist
> Nepali MT research highlights the "low-resource bottleneck." Success depends on back-translation, multilingual training (Hindi/Bengali as anchors), and high-quality evaluation benchmarks like FLORES.

## 1. Key Benchmarks & Data

| Resource | Size | Role |
| :--- | :--- | :--- |
| **FLORES** | ~3,000 sentences | High-quality Wikipedia sentences. The standard for low-resource MT eval. |
| **NNC Parallel** | ~4M words | Foundation for early SMT and bilingual dictionaries. |
| **Hindi-Nepali** | 246k sentences | Private dataset using extensive back-translation to augment data. |
| **Tamang-Nepali** | 15,000 pairs | First known MT effort for this pair via crowdsourced alignment. |

## 2. Paradigms & Performance

### SMT vs NMT
- **Early Findings (2018)**: In extremely low-resource settings (<7k sentences), **Phrase-Based SMT (Moses)** often outperforms NMT (RNN/Attention).
- **Modern Performance**: Transformer-based models significantly outperform LSTMs, achieving BLEU ~21 on moderately sized corpora (20k pairs).
- **Semi-Supervised gains**: Back-translation and multilingual training (with Hindi) are the largest drivers of performance, increasing BLEU by up to 13.5 points on FLORES.

### Alignment from Comparable Corpora
- Lexicon-based alignment algorithms (scoring translated words vs sentence length) achieved **F-Measure 88.7%** on mining parallel sentences from comparable news sources.

## 3. Endangered Languages (Tamang)
- **Vocabulary**: 1k vocabulary size found optimal for Transformer training in very low-resource (15k pair) settings.
- **Script**: Devanagari preferred over Tamyig for wider digital applicability.

## 4. Bias in MT
- **Gender Bias**: Evaluation of occupational bias and coreference in Nepali-English translation.
- **Linguistic Formality**: High-resource anchors often miss Nepali-specific formality levels (e.g., *tā*, *timi*, *tapāi*).

---

#nepali #machine-translation #smt #nmt #flores #back-translation #low-resource
