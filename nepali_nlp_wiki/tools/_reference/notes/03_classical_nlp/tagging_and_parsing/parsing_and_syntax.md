# Parsing & Syntax

## 1. Text Normalization and Preprocessing
- **Normalization**: Converting all characters to lowercase, handling punctuation, and removing "stop words" to prepare text for syntax analysis.
- **Morphological Analysis**: Analyzing the base/root forms (stemming/lemmatization) and identifying inflectional features like tense and pluralization.

## 2. Edit Distance
- **Minimum Edit Distance**: The minimum number of operations (insertions, deletions, substitutions) required to transform one string into another.
- **Application**: Used in spelling correction, error detection, and quantifying string similarity.

## 3. Context-Free Grammar (CFG)
A formal grammar used to model the syntax of natural languages through production rules (e.g., $S \rightarrow NP \ VP$).

## 4. Probabilistic CFG (PCFG)
Assigns a probability $P$ to each production rule $A \rightarrow \beta$, such that $\sum_{\beta} P(A \rightarrow \beta) = 1$.
- **Goal**: Disambiguate multiple possible trees by selecting the one with the highest total probability ($P(Tree) = \prod_{rules} P(i)$).
- **Learning**: Probabilities are estimated from a **Treebank** (a corpus of hand-parsed sentences).

## Linguistic Foundations
- **Heads and Modifiers**: Every phrase has a central word (Head) that determines its syntactic category (e.g., a "Noun Phrase" has a Noun as its head).
## Syntactic Formalisms
- **X-Bar Theory**: Bridges phrase structure and complex syntax via intermediate levels.
- **HPSG (Head-Driven Phrase Structure Grammar)**: A highly lexicalized constraint-based formalism that uses **feature structures** and **unification** to represent linguistic information.
- **LTAG (Lexicalized Tree-Adjoining Grammar)**: Uses trees as basic units (initial and auxiliary) rather than rewrite rules, allowing for better handling of long-range dependencies.

## Parsing Approaches
- **Top-Down**: Starts from the goal ($S$) and tries to find a path to the input tokens.
- **Bottom-Up**: Starts from the tokens and groups them into larger constituents (e.g., **Shift-Reduce**).
- **Tabular Parsing (Chart)**: Stores intermediate results in a "chart" to avoid redundant calculations (essential for polynomial-time parsing). **Earley** and **CKY** are the most common implementations (Kurdi, 2016).
- **Transition-Based Dependency Parsing**: Incremental Shift-Reduce.
- **Graph-Based Dependency Parsing**: Maximum Spanning Tree (MST).

## Tools & Libraries
- **Constituency**: Stanford Parser, Berkeley Neural Parser.
- **Dependency**: spaCy, Stanza, MaltParser.

## Why It Matters
- Relation extraction
- Information extraction
- Machine translation alignment

---

#classical #syntax
