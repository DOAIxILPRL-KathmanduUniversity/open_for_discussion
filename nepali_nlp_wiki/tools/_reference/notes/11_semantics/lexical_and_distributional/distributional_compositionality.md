# Distributional Compositionality

> [!IMPORTANT] Gist
> If individual words are vectors, how do we represent phrases and sentences? **Compositionality** is the mathematical bridge between word-level distributional semantics and sentence-level meaning.

## 1. The Compositionality Problem
The principle of compositionality states that the meaning of an expression is determined by the meaning of its parts and the rules for combining them. In vector space, we need an operator $\oplus$ such that $v_{phrase} = v_{word1} \oplus v_{word2}$.

## 2. Simple Vector Operations
- **Vector Addition**: $v = v_1 + v_2$.
    - **Pros**: Simple, results in a vector of the same size.
    - **Cons**: Commutative ($A+B = B+A$), so "dog bites man" = "man bites dog." Loses all word order and syntax.
- **Vector Multiplication (Element-wise)**: $v = v_1 \odot v_2$.
    - **Pros**: Captures interaction between word features.
    - **Cons**: Also commutative.

## 3. Advanced Composition (Mitchell & Lapata, 2008)
- **Matrix-Vector Multiplication**: One word (the predicate) is a matrix $M$, and the other (the argument) is a vector $v$. $v_{phrase} = Mv$.
    - **Pros**: Non-commutative. Captures how a verb modifies its object.
- **Tensor Products**: $v_{phrase} = v_1 \otimes v_2$.
    - **Cons**: The vector size explodes (a $d$-dim vector becomes $d^2$-dim), making it impractical for deep trees.

## 4. Deep Learning Solutions
Modern deep learning sidesteps explicit vector arithmetic using:
- **RNNs/LSTMs**: Sequential hidden state updates act as a continuous composition function.
- **Recursive Neural Networks (Tree-RNNs)**: Composes vectors according to a syntactic parse tree (bottom-up).
- **Transformers (Attention)**: Composes word vectors by selectively weighting and summing their neighbors' vectors.

---

#semantics #representation #compositionality #vector-math #mitchell-lapata
