# Meaning-Text Theory (MTT)

> [!IMPORTANT] Gist
> Meaning-Text Theory (MTT), pioneered by Igor Mel'čuk, is a dependency-based linguistic framework that views language as a mapping between a set of meanings and a set of texts through multiple levels of representation.

## 1. The Multi-Level Mapping
MTT posits that a sentence is transformed through several layers:
1.  **Semantic Representation (SemR)**: A network of semantic nodes and relations.
2.  **Deep Syntactic Representation (DSyntR)**: A dependency tree capturing core semantic relations, neutralizing voice and function words.
3.  **Surface Syntactic Representation (SSyntR)**: A tree capturing the literal syntactic dependencies (auxiliaries, agreement).
4.  **Morphological & Phonological levels**: Final textual realization.

## 2. Lexical Functions (LFs)
One of the most powerful aspects of MTT is its system of ~56 universal **Lexical Functions**. These describe the restricted collocations between words:
- **Syn (Synonym)**: $Syn(murder) = assassination$.
- **Anti (Antonym)**: $Anti(big) = small$.
- **Magn (Intensifier)**: $Magn(rain) = heavy$; $Magn(smoker) = heavy$.
- **Oper1 (Commit/Perform)**: Describes the "light verb" used with a noun where the agent is the subject. $Oper1(murder) = commit$.
- **Func1 (Occur)**: $Func1(war) = break\_out$.

## 3. Microstructure & Government Patterns
A lexical unit in an MTT-based dictionary includes:
- **Semantic Definition**: A formal breakdown of the concept.
- **Government Pattern (GP)**: A table describing how semantic arguments are realized syntactically.
    - *Example*: For the verb "GIVE", the GP specifies that the Recipient (Arg 3) can be realized as an Indirect Object with "to" or a direct Dative.
- **Lexical Combinatorics**: The full list of Lexical Functions applicable to that word.

## 4. Significance for NLP
- **NLG (Generation)**: LFs provide a principled way to choose the "natural" word for a concept (e.g., knowing that we "commit" a crime but "wage" a war).
- **Paraphrasing**: DSyntR allows for easy transformation between passive and active voices or between different lexical realizations of the same meaning.
- **MT**: Serves as a deep interlingua that captures the "logic" of the sentence before surface-level language-specific constraints are applied.

---

#semantics #mtt #melcuk #lexical-functions #dependency-syntax
