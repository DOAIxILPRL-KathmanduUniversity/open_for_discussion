# Research: Natural Language Generation (UNL Deconverter)

> [!IMPORTANT] Gist
> The **UNL (Universal Networking Language) Deconverter** for Nepali represents an early Interlingua approach to generation, focusing on translating semantic graphs into syntactically correct SOV sentences.

## 1. Generation Process (UNL to Nepali)

### Stage 1: Syntax Planning
- **Goal**: Mapping the UNL semantic graph to the Nepali **Subject-Object-Verb (SOV)** pattern.
- **Mechanism**: A **Priority Matrix** of UNL relations (e.g., `agt` [agent], `obj`, `ben` [beneficiary]) decides the linear word order.

### Stage 2: Morphology Generation
- **Dictionary Mapping**: Mapping Universal Words (UWs) to Nepali roots.
- **Affixation**:
    - **Case Markers**: Added based on relations (e.g., `agt` relation triggers the `le` marker).
    - **Inflections**: Attributes like `@pl` (plural) trigger `haru`, and tense attributes trigger specific verb endings.
    - **Function Words**: Automatically introducing conjunctions based on logical relations.

## 2. Significance
- **Language Independence**: Allows generating Nepali from any language represented in UNL.
- **Morphological Focus**: Demonstrates that for rich languages like Nepali, much of the generation logic is handled at the morphological level rather than just syntax.

---

#nepali #nlg #unl #interlingua #morphology #generation
