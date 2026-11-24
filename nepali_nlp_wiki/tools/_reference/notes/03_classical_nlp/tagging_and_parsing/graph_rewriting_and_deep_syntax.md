# Graph Rewriting & Deep Syntax

> [!IMPORTANT] Gist
> Graph rewriting is a programming paradigm that transforms linguistic structures (trees or graphs) into more abstract representations, such as Deep Syntax or Semantic Graphs, using local transformation rules.

## 1. Surface vs. Deep Syntax
- **Surface Syntax**: Represents the literal dependency structure of the sentence (e.g., passive voice, functional words like auxiliaries).
- **Deep Syntax**: Neutralizes variations in voice (diathesis) and abstracts away functional words. It focuses on the semantic arguments of predicates.
    - **Neutralization**: Passive "A book is given by Max" and active "Max gives a book" share the same Deep Syntax (Max = Subject, Book = Object).
    - **Inferred Links**: Explicitly marking the subject of an infinitive (e.g., in "I want to eat," *I* is the deep subject of *eat*).

## 2. Graph Rewriting Systems (GREW)
A modular approach to transforming graphs (Guillaume et al., 2018):
- **Pattern (Left Side)**: Describes the local configuration of nodes and edges to be matched, including negative constraints (e.g., "match node X if it does NOT have edge Y").
- **Commands (Right Side)**: Actions to perform on the match, such as `add_edge`, `del_edge`, or `shift_edge`.
- **Modularity**: Rules are grouped into **Packages** and executed according to **Strategies** (e.g., "apply package A until convergence, then move to package B").

## 3. Semantic Transformation
Graph rewriting is used to convert Deep Syntax into specialized semantic formalisms:
- **AMR (Abstract Meaning Representation)**: Highlights predicates and arguments, often using a standard dictionary like PropBank.
- **MRS/DMRS (Minimal Recursion Semantics)**: Handles quantifier scope and underspecification. DMRS uses a dependency-based graph where nodes are "eps" (elementary predicates).

## 4. Advantages
- **Ambiguity Handling**: Non-deterministic rewriting allows for multiple possible output graphs (e.g., for attachment ambiguity).
- **Local Analysis**: Rules only need to look at a small neighborhood of nodes, making the system scalable and easy to debug.

---

#classical #syntax #graphs #grew #amr #mrs
