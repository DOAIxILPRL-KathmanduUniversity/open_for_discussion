# Viterbi & Beam Search

> [!IMPORTANT] Gist
> Sequence models (HMMs, CRFs, Transformers) generate a probability distribution over labels. Viterbi and Beam Search are the algorithms used to find the most likely sequence of labels from these distributions.

## 1. The Decoding Problem
In a sequence labeling task (like POS tagging), for a sentence of length $N$ with $T$ possible tags, there are $T^N$ possible tag sequences. Exhaustive search is impossible ($O(T^N)$).

## 2. Viterbi Algorithm (Dynamic Programming)
Used when the model has local dependencies (like HMMs or CRFs).
- **The Core Idea**: The best path to a tag $t$ at time $i$ depends only on the best paths to all possible tags at time $i-1$.
- **Complexity**: $O(N \cdot T^2)$.
- **Backpointer**: We store a "backpointer" at each step to reconstruct the optimal path once we reach the end.
- **Limitation**: Only works for models with a limited "history" (e.g., bigram or trigram dependencies).

## 3. Beam Search (Heuristic Search)
Used for models with long-range dependencies where Viterbi is too expensive or impossible (e.g., Seq2Seq, Transformers).
- **The Core Idea**: Instead of keeping *all* possible paths, we keep only the top-$k$ most likely partial sequences (where $k$ is the **Beam Width**).
- **Process**:
    1.  At each step, expand all $k$ active sequences.
    2.  Score all new candidates.
    3.  Prune and keep only the top $k$.
- **Complexity**: $O(N \cdot k \cdot T)$.
- **Trade-off**: Larger $k$ increases accuracy but slows down inference.

## 4. Comparison
| Feature | Viterbi | Beam Search |
| :--- | :--- | :--- |
| **Optimality** | Guaranteed global optimum | Heuristic (not guaranteed) |
| **Use Case** | HMM, CRF, FST | RNN, Transformer, MT |
| **Complexity** | $O(N \cdot T^2)$ | $O(N \cdot k \cdot T)$ |

---

#classical #inference #decoding #viterbi #beam-search #dynamic-programming
