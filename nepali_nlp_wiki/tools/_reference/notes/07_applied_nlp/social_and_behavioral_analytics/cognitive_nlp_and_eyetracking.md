# Cognitive NLP & Eye-tracking

> [!IMPORTANT] Gist
> Cognitive NLP leverages human behavioral data—specifically eye-tracking (gaze patterns)—to model text complexity, improve annotation quality, and build multimodal NLP systems.

## 1. Eye-Movement Metrics
Humans process text through alternating phases of stability and rapid movement:
- **Fixations**: Brief moments where the eyes are still, focusing on a word (indicates lexical access and processing).
- **Saccades**: Rapid jumps between fixations.
- **Regressions**: Backward saccades (indicates re-processing or syntactic re-analysis).
- **Scanpaths**: The complete sequence of fixations and saccades across a text.

## 2. Modeling Annotation Complexity
Eye-tracking data is used to predict the "cognitive effort" required for linguistic tasks:
- **Translation Complexity Index (TCI)**: Predicted using eye-movement features (total fixation duration, number of fixations). Helps in crowdsourcing by "binning" sentences into easy, medium, and hard categories for fair payment models.
- **Sentiment Annotation Complexity (SAC)**: Measures effort in labeling polarity. Humans often "home in" on subjectivity-bearing phrases before deciding the final label.
- **Word Sense Disambiguation (WSD)**: Lexicographers follow a three-stage process:
    1.  **Hypothesis Generation** ($T_{hypo}$): Formulating initial sense ideas.
    2.  **Clue Search** ($T_{clue}$): Finding context to support or eliminate senses.
    3.  **Gloss Matching** ($T_{gloss}$): Final selection.
    *   **Insight**: Verbs are ~75% more difficult to disambiguate than other parts of speech (Mishra et al., 2013).

## 3. Gaze-Augmented NLP Systems
Multimodal systems use gaze data as an auxiliary input or training signal:
- **Weakly Supervised POS Tagging**: Combining raw text with gaze features (lexical access, regressions) to improve tagger accuracy in low-resource domains.
- **Sentence Compression**: Multitask Bi-LSTMs learn to predict which words humans skip while reading, identifying unimportant portions for automated compression (Klerke et al., 2016).
- **MT Evaluation**: Using gaze time and fixation counts to correlate with human judgments of translation quality (BLEU vs. Gaze).

---

#applied #cognitive-science #eyetracking #annotation #tci #sac
