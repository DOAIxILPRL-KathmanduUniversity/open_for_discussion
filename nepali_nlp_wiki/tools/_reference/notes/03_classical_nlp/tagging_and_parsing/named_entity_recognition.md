# Named Entity Recognition

## Entity Types
- PERSON, ORG, GPE, DATE, MONEY, ...
- Domain-specific: GENE, DRUG, CROP
- **Cybersecurity**: IP, URL, HASH, MALWARE, THREAT_ACTOR (Holzer, 2016)

## NER Misidentification Challenges
In technical domains (e.g., APT reports), standard NER models often fail:
- **Overlapping Boundaries**: Technical strings (URLs, complex file paths) misidentified as dates or locations.
- **Gazetteer Limitations**: Static lists of malware families become obsolete within days.
- **Case Sensitivity**: Software names and protocols often violate standard capitalization rules.

## Approaches
- Rule/gazetteer-based
- CRF with hand-crafted features
- BiLSTM-CRF (Lample et al., 2016)
- Transformer fine-tuning (current SOTA)

## Transliteration Discovery
In multilingual NER, entities often appear as transliterations (e.g., "Obama" in English vs. "ओबामा" in Hindi).
- **Transliteration Discovery**: Automatically identifying and mapping these variants across languages using **constraint-driven learning** (Goldwasser et al., 2009).
- **Phonetic Mapping**: Using acoustic or character-level alignment to link names that sound similar but are written in different scripts.
- **Goal**: Enhances cross-lingual IE by ensuring that a single entity is identified regardless of the language or script.

## Bi-LSTM for NER
- Concatenates forward and backward hidden states to capture bidirectional context.
- Often paired with a CRF layer for label dependency modeling.
- See [[05_sequence_models/bidirectional_lstm]] for architecture and math.
- **Notebook**: [kazakh_ner_arch.py](notebooks/kazakh_ner_arch.py)

## Evaluation
- Entity-level F1 (exact match vs. partial)
- CoNLL-2003 benchmark

## Bi-LSTM-CNN-CRF Architecture
A standard architecture for sequence labeling in low-resource settings combines local, global, and dependency features (Hayinaer et al., 2025):
1. **CNN Layer**: Captures local features and character/subword patterns.
2. **Bi-LSTM Layer**: Encodes bidirectional global context.
3. **Multi-Head Attention**: Selectively weights relevant contextual features.
4. **CRF Layer**: Models dependencies between adjacent labels to find the optimal sequence.

## CRF Scoring Function
The CRF layer calculates the score of a label sequence $Y = \{y_1, y_2, \dots, y_n\}$ for a hidden state sequence $H = \{h_1, h_2, \dots, h_n\}$ (Lafferty et al., 2001; Hayinaer et al., 2025):

$$s(H, Y) = \sum_{i=1}^{n} P_{i, y_i} + \sum_{i=1}^{n} T_{y_{i-1}, y_i}$$

Where:
- $P_{i, y_i}$ is the emission score (probability of tag $y_i$ at position $i$).
- $T_{y_{i-1}, y_i}$ is the transition matrix score (probability of moving from tag $y_{i-1}$ to $y_i$).
- The optimal sequence $Y^*$ is found via the **Viterbi algorithm**: $Y^* = \text{argmax}(s(H, Y))$.

## Performance in Low-Resource Domains
- Kazakh NER in tourism domains faces challenges like fuzzy boundaries and nested entities (e.g., a city name inside a scenic spot name).
- Models using **Word + Stem embeddings** outperform word-only models by capturing morphological structure (Hayinaer et al., 2025).


## Negation & Context Detection
- Clinical NER must handle negation ("no fever"), uncertainty ("possible pneumonia"), and temporal context ("history of diabetes") (Saha et al., 2026)
- Systems must distinguish between present conditions, absent conditions, and historical mentions within the same narrative (Au Yeung et al., 2024)

## Relation Extraction (RE)
- Identifies relationships between extracted entities: drug-disease interactions, symptom-diagnosis associations, temporal event chains (Kreimeyer et al., 2017)
- RE enables structured knowledge extraction from free-text clinical narratives

## Notable Systems & Benchmarks
- **MedCAT** (Medical Concept Annotation Tool): 26,086 annotations across 556 SNOMED-CT concepts, deployed in UK NHS (Au Yeung et al., 2024)
- **cTAKES**: rule-based pipeline for clinical NER, negation detection, and concept mapping (Savova et al., 2010)
- **MetaMap**: maps biomedical text to UMLS Metathesaurus concepts (Bodenreider, 2004)

---

**Notebook**: [spacy_pipeline_lab.py](notebooks/spacy_pipeline_lab.py)

#classical #ner
