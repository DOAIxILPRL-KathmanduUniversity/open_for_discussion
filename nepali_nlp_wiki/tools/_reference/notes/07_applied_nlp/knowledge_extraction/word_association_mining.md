# Word Association Mining

> [!IMPORTANT] Gist
> Word association mining is the task of discovering hidden relationships between words in a corpus. It distinguishes between words used in similar contexts (**Paradigmatic**) and words that occur together in the same context (**Syntagmatic**) (Zhai & Massung, 2016).

## 1. Paradigmatic vs. Syntagmatic
- **Paradigmatic Relations**: Words that can substitute for each other (e.g., *cat* and *dog* are both pets, appear near *leash*, *food*, *vet*). They have high **Contextual Similarity**.
- **Syntagmatic Relations**: Words that co-occur with each other (e.g., *cat* and *meow*, *bark* and *dog*). They have high **Co-occurrence Frequency**.

## 2. Discovery Methods
- **Context Vector Comparison**: Representing words by the words that surround them. If vectors are similar, the words are paradigmatically related.
- **Mutual Information (MI)**: Identifying syntagmatic associations by checking if $P(w_1, w_2) > P(w_1)P(w_2)$.
- **KL-Divergence**: Comparing the distribution of words in a "local" context vs. a "global" background corpus to find significant local associations.

## 3. The Role of Information Retrieval (IR)
IR is critical for text mining in two ways:
1. **Filtering**: Reducing a massive corpus to a relevant subset (e.g., "all texts about cats") before performing association mining.
2. **Validation**: Allowing the analyst to "drill down" into the source documents to verify if a discovered association is meaningful or just noise.

## 4. Evaluation
- **Human Judgment**: Comparing associations against human-generated lists (e.g., Word Association Norms).
- **Indirect Evaluation**: Using the associations to improve a downstream task like Query Expansion in a search engine.

---

#applied #mining #associations #similarity #ir #semantics
