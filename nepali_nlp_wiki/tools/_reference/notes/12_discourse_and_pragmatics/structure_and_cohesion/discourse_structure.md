# Discourse Structure & Relations

> [!IMPORTANT] Gist
> Discourse analysis moves beyond the sentence level to understand how sequences of sentences form a coherent whole. This involves tracking entities across sentences and identifying the logical relationships between spans of text.

## 1. Entity-Based Coherence
Models that track how "salient" entities transition between sentences.
- **Centering Theory**: Focuses on the "Center of Attention." It tracks the **Forward-Looking Centers** (Cf) and the **Backward-Looking Center** (Cb). Coherence is measured by the type of transition (e.g., *Continue*, *Retain*, *Smooth Shift*, *Rough Shift*).
- **The Entity Grid**: A matrix representation where rows are sentences and columns are entities. Each cell indicates the entity's grammatical role (Subject, Object, Neither) or absence (-). Coherent texts show recurring patterns of entity prominence (Eisenstein, 2018).

## 2. Discourse Relations
Linguistic frameworks for describing the logical connection between text segments.
- **Shallow Discourse Relations (PDTB)**: Focuses on local relations signaled by connectives (e.g., *because, however, although*).
- **Rhetorical Structure Theory (RST)**: A hierarchical model where the text is parsed into a tree of **Nuclear** (primary) and **Satellite** (supporting) spans.
    - **Example Relations**: *Elaboration*, *Contrast*, *Condition*, *Explanation*.

## 3. Discourse Segmentation
- **Topic Segmentation**: Dividing a long document into sections based on changes in topic (e.g., **TextTiling**).
- **Functional Segmentation**: Dividing text based on its purpose (e.g., *Introduction*, *Methods*, *Results* in scientific papers).

---

#discourse #coherence #rst #pdtb #centering-theory
