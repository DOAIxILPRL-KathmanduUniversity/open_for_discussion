# Semantic Analysis

> [!IMPORTANT] Gist
> Semantic analysis aims to bridge the gap between word-level meaning and context-dependent interpretation. It encompasses lexical semantics, word sense disambiguation, and the study of relationships between lexemes (WordNet).

## 🎓 Lecturer's Scaffolding: Meaning Layers
1. **Lexical Semantics**: The study of word meanings and their relations.
2. **Lexemes**: The basic abstract unit of a language's vocabulary (e.g., "run," "runs," "ran" share the lexeme *run*).
3. **Semantic Grammar**: A grammar where categories are semantic (e.g., `Destination` instead of `NP`).

## 🔬 Researcher's Synthesis: Word Relations
- **Synonymy**: Different words with similar meanings (e.g., *big*, *large*).
- **Antonymy**: Words with opposite meanings (e.g., *hot*, *cold*).
- **Hyponymy**: IS-A relationship (*apple* is a hyponym of *fruit*).
- **Polysemy**: One word with multiple related meanings.
    - **Regular Polysemy**: Productively related sense families (e.g., all count nouns for animals can also be mass nouns for their meat).
- **Homonymy**: One word with multiple unrelated meanings (*bat* as animal vs. sports equipment).
- **Evaluating Embeddings via Lexical Semantics**:
    - **Thematic Fit**: Evaluating how well embeddings find nouns that fulfill semantic roles for specific verbs (e.g., "cut" and "cake" vs. "cut" and "cat"). High-quality embeddings should assign higher scores to more plausible "fit" pairs.
    - **Outlier Word Detection**: Identifying which word in a set doesn't belong (e.g., "laptop" in a set of animals). Strong embeddings cluster semantically similar entities, making outliers mathematically distinct (Zhang et al., 2021).

## 1. WordNet & Multiword Expressions (MWE)
- **WordNet**: A database of **Synsets** (meaning units).
    - **Nouns**: Organized by **Hypernymy** (is-a), **Meronymy** (part-of), and **Holonymy** (composed-of).
    - **Verbs**: Organized by **Troponymy** (X is a *way* of doing Y; e.g., "whisper" is a troponym of "talk").
    - **Adjectives**: Organized by **Antonymy** (direct pairs like hot/cold).
    - **Types vs. Instances**: Distinguishes between categories (e.g., *mountain* is a type) and specific individuals (e.g., *Mount Rainier* is an instance).
- **MWEs**: Expressions like "kick the bucket" that straddle the boundary between lexical and compositional semantics. They vary in **compositionality** and **syntactic flexibility**.

### Tool: Interactive WordNet Graph Visualization
To understand the complex hierarchy of WordNet, we can visualize relationships using `networkx` and `matplotlib`.

- **Synonyms**: Edges connecting words within the same Synset.
- **Hypernyms/Hyponyms**: Vertical edges showing the IS-A hierarchy.
- **Meronyms/Holonyms**: Edges showing PART-OF relationships.
- **Antonyms**: Edges showing semantic opposition (mostly for adjectives).

**The Graph Utility**: By modeling a word and its neighbors as a graph, we can apply centrality measures (like PageRank) to assist in Word Sense Disambiguation.

## 2. Word Sense Disambiguation (WSD) & Induction (WSI)
- **WSD**: Identifying the correct sense.
    - **Lesk Algorithm**: Overlap between context and definitions.
    - **Selectional Restrictions**: Soft constraints on the type of argument expected to fill a semantic role.
    - **Evolutionary Game Theory (EGT)**: Modeling WSD as a non-cooperative game where words are "players" and senses are "strategies." The system converges to a Nash equilibrium where sense assignments are mutually consistent across the entire context window (Tripodi et al., 2014; Sharp & Delmonte, 2014).
- **Word Sense Induction (WSI)**: Discovering senses directly from data by clustering.

## 3. Graph-based Word Sense Disambiguation
An unsupervised approach that models sense disambiguation as a graph problem (Sinha & Mihalcea, 2009).
- **The Graph**: Nodes represent word senses, and edges represent semantic relations (from WordNet or distributional similarity).
- **Centrality Algorithms**: Using **PageRank** or **HITS** to find the most "central" sense for a word within its context. The intuition is that the correct senses of different words in a sentence will "vote" for each other through semantic connections.
- **Advantages**: Does not require large labeled training sets; can be applied to any language with a WordNet-like resource.
- **Optimal Relation Weighting ($\lambda$ parameters)**: Research indicates that not all relations are equally useful for disambiguation. Winning configurations for unsupervised algorithms follow this hierarchy (Kim & Kwon, 2021):
    - **Coordinate Term**: 0.5 (Highest context identifying influence)
    - **Hyponym**: 0.4 (High relevance for sense narrowing)
    - **Hyponym of Coordinate**: 0.1
    - **Hypernym**: 0.0 (Introduces too much semantic noise)
- **Solving the Data Deficiency Problem**: In low-resource settings where training data for a target word is missing, the **$\chi^2$ (chi-square)** statistic can be calculated between *related* words in the hierarchy rather than the ambiguous word itself. This WordNet-driven prior probability estimation achieved 86.3% accuracy in resolving ambiguous words.

## 4. Affect Lexicons
Lexicons like **SentiWordNet** or **LIWC** map words to sentiment/emotion scores.
- **Induction**: Creating lexicons automatically using semi-supervised methods (e.g., starting with a few seed words and expanding via word similarity).

---

#semantics #wordnet #wsd
