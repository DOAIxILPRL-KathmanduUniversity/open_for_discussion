# The Distributional Hypothesis

> [!IMPORTANT] Gist
> "You shall know a word by the company it keeps" (J.R. Firth, 1957). The distributional hypothesis is the theoretical foundation of all modern vector-based NLP.

## 1. The Core Concept
The meaning of a word is defined by its usage and the contexts in which it appears. Words that occur in similar contexts tend to have similar meanings.
- **Example**: If we see "The cat sat on the ___" and "The dog sat on the ___", we can infer that "cat" and "dog" share a semantic category.

## 2. Historical Roots
- **Zellig Harris (1954)**: Distributional Structure. Language can be described in terms of the distribution of its elements.
- **John Rupert Firth (1957)**: Collocational meaning.
- **Ludwig Wittgenstein**: "Meaning is use."

## 3. From Counts to Vectors
How do we turn a hypothesis into math?
- **Co-occurrence Matrix**: Create a matrix where rows are words and columns are context words. Each cell counts how often they appear together.
- **Vector Space Model (VSM)**: Each row becomes a vector in a high-dimensional space.
- **Cosine Similarity**: If two vectors point in the same direction, they are distributionally similar.

## 4. Strengths and Weaknesses
- **Strengths**: Unsupervised (no labeling needed), captures subtle semantic nuances, scales with data.
- **Weaknesses**:
    - **Antonyms**: "Hot" and "Cold" appear in almost identical contexts ("The weather is ___"), making them highly similar in vector space despite being opposites.
    - **Polysemy**: A single vector often collapses multiple meanings (the "Bank" problem).

---

#representation #theory #distributional-hypothesis #firth #harris
