# Minimum Edit Distance

> [!IMPORTANT] Gist
> Edit distance quantifies how similar two strings are by counting the minimum number of operations (insertions, deletions, substitutions) required to transform one into the other (Levenshtein, 1966).

## 1. Operations
- **Insertion**: Adding a character.
- **Deletion**: Removing a character.
- **Substitution**: Replacing one character with another.

## 2. Levenshtein Distance
A specific version of edit distance where substitutions have a cost of 2 (in some versions) or 1.
- **Application**: Spell checking, DNA sequencing, and calculating **Word Error Rate (WER)** in speech recognition.

## 3. Algorithm: Dynamic Programming
The distance is computed using a 2D matrix where $dp[i][j]$ represents the distance between the first $i$ characters of string A and the first $j$ characters of string B.

---

#classical #algorithms #edit-distance
