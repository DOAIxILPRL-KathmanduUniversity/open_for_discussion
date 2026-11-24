# POS Tagging

## What
- Assign grammatical category to each token (noun, verb, adj, ...)
- Universal POS tagset (17 tags) vs. Penn Treebank (36 tags)

## Methods
1. **Rule-Based & TBL**:
    - **Brill Tagger (Transformation-Based Learning)**: A "succinct" bridge between rule-based and statistical methods.
        1. **Initial Tagging**: Assign the most frequent tag to each word (Everything is a noun by default).
        2. **Error Calculation**: Compare with a gold-standard corpus.
        3. **Rule Induction**: Find the transformation rule (e.g., "Change A to B if context is C") that reduces the most errors.
        4. **Iteration**: Apply the rule and repeat until no more significant improvements are found.
        - **Strength**: Compact, human-readable rules; fast execution (Booth, 2018).
2. **Probabilistic/Statistical Models**:
   - **HMM (Hidden Markov Model)**: Models the sequence as a Markov process with hidden states (tags). Uses transition probabilities $P(t_i|t_{i-1})$ and emission probabilities $P(w_i|t_i)$. Decoded via the **Viterbi Algorithm**.
   - **Maximum Entropy (Log-linear Models)**: Allows integrating overlapping features (capitalization, prefixes, neighboring words) without the independence assumptions of HMMs.
   - **CRF (Conditional Random Fields)**: Discriminative models that optimize the global probability of the entire tag sequence.
3. **Neural Models**:
   - **BiLSTM-CRF**: The current standard for capturing bidirectional context and label dependencies.
   - **Transformers**: Multi-head attention captures long-range dependencies more effectively than LSTMs.

## Bi-LSTM for POS Tagging
- Bi-LSTMs provide context from both left and right, which is essential for disambiguating meaning (e.g., "bank" as noun vs. verb).
- See [[05_sequence_models/bidirectional_lstm]] for architecture and math.
- **Notebook**: [bilstm_pos_lab.py](../05_sequence_models/notebooks/bilstm_pos_lab.py)

## Why It Matters
- Disambiguates meaning ("bank" as noun vs. verb)
- Required for lemmatization, parsing, NER

---

#classical #tagging
