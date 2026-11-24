# Semantic Representation: AMR, MRS, and DMRS

> [!IMPORTANT] Gist
> Semantic representation formalisms aim to capture the meaning of a sentence in a machine-readable graph structure that is independent of syntactic variations.

## 1. Abstract Meaning Representation (AMR)
AMR is a rooted, labeled, directed acyclic graph where nodes represent concepts and edges represent semantic relations.
- **Rooted**: There is a single top-level concept (the "focus").
- **PropBank Based**: Relations often use PropBank frames (e.g., `:arg0`, `:arg1`).
- **Abstract**: It ignores morphosyntactic details (tense, number, articles) to focus on the core logical meaning.
- **Example**: "Max wants to eat" $\rightarrow$ `(w / want-01 :arg0 (m / Max) :arg1 (e / eat-01 :arg0 m))`.

## 2. Minimal Recursion Semantics (MRS)
MRS is a framework for computational semantics that handles **quantifier scope** through underspecification.
- **Elementary Predicates (EPs)**: The basic units of meaning.
- **Handles**: Labels assigned to EPs to indicate scope.
- **qeq ($=_{q}$)**: "Equality modulo quantifiers" – a constraint used to represent scope relationships without resolving them into a single tree.

## 3. Dependency MRS (DMRS)
A graph-based simplification of MRS that uses a dependency structure instead of handles and variables.
- **Nodes**: Elementary Predicates.
- **Edges**: Represent the relationship between predicates (e.g., `ARG1`, `MOD`).
- **Graph Transformation**: DMRS is often the target of Graph Rewriting systems (like GREW) that convert syntactic dependencies into semantic links.

## 4. Comparison
| Feature | AMR | MRS/DMRS |
| :--- | :--- | :--- |
| **Focus** | Predicate-argument structure | Quantifier scope & logic |
| **Linking** | Concepts to PropBank frames | Semantic predicates (lexical) |
| **Underspecification** | Low (resolves ambiguity) | High (preserves ambiguity) |
| **Application** | Summarization, IE | Exact logical reasoning |

## 5. OntoSem & Formal Reasoning
Advanced representation models integrate world knowledge for deep analysis (Huang et al., 2010).
- **OntoSem (Ontological Semantics)**: A model that produces a **Text Meaning Representation (TMR)** by drawing from an ontology and a fact repository. It excels at interpreting "events of change" (e.g., increase/decrease) by mapping them to formal ontological transitions.
- **OWL DL (Web Ontology Language - Description Logic)**: A formal language for representing knowledge on the Semantic Web. Mapping semantic structures (like FrameNet) to OWL DL enables **DL-reasoning**, allowing systems to automatically detect contradictions or infer new facts from annotated text.

## 6. Formal Concept Analysis (FCA)
FCA is a mathematical framework used for knowledge representation and conceptual knowledge processing (Kapetanios et al., 2014).
- **Formal Context**: A triplet $(G, M, I)$ where $G$ is a set of objects, $M$ is a set of attributes, and $I$ is a binary relation indicating which objects have which attributes.
- **Formal Concept**: A pair $(A, B)$ where $A$ is the set of all objects sharing attributes in $B$, and $B$ is the set of all attributes shared by objects in $A$.
- **Concept Lattice**: A hierarchical visualization of all formal concepts in a context, showing sub-concept/super-concept relationships.
- **NLP Application**: Used for **Text Segmentation**, **Summarization**, and building ontologies automatically from text by identifying shared attributes between linguistic entities.

---

#semantics #amr #mrs #dmrs #representation
