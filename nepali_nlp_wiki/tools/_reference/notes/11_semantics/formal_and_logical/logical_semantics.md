# Logical Semantics

> [!IMPORTANT] Gist
> Logical semantics (or Formal Semantics) uses mathematical logic to represent the meaning of natural language expressions, enabling computer systems to reason about the world.

## 1. Meaning and Denotation
- **Denotation**: The object or state of affairs in the world that an expression refers to.
- **Truth-Conditional Semantics**: To know the meaning of a sentence is to know the conditions under which it would be true.

## 2. Logical Representations
- **Propositional Logic**: Deals with simple propositions and connectives ($\land, \lor, \neg, \implies$).
- **First-Order Logic (FOL)**: Adds objects, predicates, and quantifiers ($\forall, \exists$).
    - **Example**: "Every student likes NLP" $\rightarrow \forall x (\text{Student}(x) \implies \text{Likes}(x, \text{NLP}))$.

## 3. Semantic Parsing & Lambda Calculus
Semantic parsing is the task of mapping natural language sentences to a formal meaning representation.
- **The Lambda Calculus**: A mathematical system for expressing function application and abstraction. It allows us to build complex meanings compositionally.
    - **Lambda Abstraction**: $\lambda x. \text{Like}(x, \text{NLP})$ (The property of liking NLP).
    - **Beta Reduction**: Applying a function to an argument. $(\lambda x. \text{Like}(x, \text{NLP}))(\text{John}) \rightarrow \text{Like}(\text{John}, \text{NLP})$.

## 4. Learning Semantic Parsers
- **From Derivations**: Learning from examples where the full mapping from syntax to logic is provided.
- **From Denotations**: Learning from questions and their answers in a database, without seeing the intermediate logical form (Weakly supervised learning).

---

#semantics #logic #lambda-calculus #formal-semantics
