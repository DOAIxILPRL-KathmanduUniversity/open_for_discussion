# Finite-State Machines in NLP

> [!IMPORTANT] Gist
> Finite-state automata (FSA) and transducers (FST) are foundational computational models for morphological analysis, tokenization, and simple rule-based generation. They represent sequences as paths through a graph of states and transitions.

## 1. Finite-State Automata (FSA)
An FSA is a directed graph where transitions are labeled with symbols. It is used to **recognize** or **accept** strings in a language.
- **Components**: States, Transitions, Start State, Final (Accept) States.
- **Types**: Deterministic (DFA) and Non-deterministic (NFA).

## 2. Finite-State Transducers (FST)
An FST is an extension of an FSA that has **two tapes**: an input tape and an output tape. It **maps** one string to another.
- **Application**: Morphological analysis (mapping surface form "cats" to "cat + plural").
- **Operations**: Composition, Inversion, Projection.

## 3. Weighted Finite-State Transducers (WFST)
WFSTs add a "weight" (score or probability) to each transition.
- **Algebra**: Weights are usually from a **Semiring** (e.g., Tropical semiring for shortest path, Real semiring for probabilities).
- **Usage**: Critical for **Statistical Machine Translation (SMT)** and **Speech Recognition**, where we want to find the "best" (highest weight) path through multiple possible transductions.
- **Operations**: $\epsilon$-removal, Determinization, and **Minimization** (essential for large-scale dictionary performance).

## 4. Modern Implementations & HFST
- **HFST (Helsinki Finite-State Technology)**: Provides a generic programming interface on top of low-level libraries like **SFST** and **OpenFST**. It enables building language-independent tools (lexicon compilers, rule compilers) that can swap underlying libraries for performance (Koskenniemi & Yli-Jyrä, 2009).
- **The Kleene Language**: A high-level weighted finite-state programming language designed for complex linguistic rule sets.
- **CLARIN**: A European infrastructure using these tools to provide unified processing for over 100 majority and minority languages.

## 5. Grammatical Inference (Grammar Induction)
Learning the structure of an unknown language from partial information (de la Higuera, 2010).
- **Identification in the Limit**: A learning process where the learner updates hypotheses as more data (informed or text-only) arrives, ideally converging on the target language.
- **State Merging Algorithms**: Starting from a **Prefix Tree Acceptor (PTA)** and merging states to generalize the language (e.g., **RPNI** for DFA, **Alergia** for Probabilistic Automata).
- **Red, Blue, and White States**: A coloring scheme used to manage states during the merging process to avoid undoing previous work.

## 6. Under-Resourced Languages & Morphology
FSMs are the primary tool for modeling the complex morphology of low-density languages (Bosch et al., 2010).
- **Nguni Language Cluster**: Modeling Zulu and Setswana verb morphology using nested FSTs to handle complex prefixing/suffixing chains.
- **Tonal Marking**: Handling tone in languages like Kinyarwanda within the finite-state pipeline.
- **OpenFst**: A widely used library for weighted finite-state transducers, critical for speech and multilingual IE.

## 7. Regular Expressions
Regex are algebraically equivalent to FSAs. They provide a compact syntax for describing finite-state patterns.

---

#classical #morphology #automata
