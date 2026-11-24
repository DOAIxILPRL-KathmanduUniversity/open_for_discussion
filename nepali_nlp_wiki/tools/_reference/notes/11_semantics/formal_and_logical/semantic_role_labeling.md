# Predicate-Argument Semantics (SRL)

> [!IMPORTANT] Gist
> Predicate-argument semantics focuses on "who did what to whom," identifying the relationship between a central predicate (usually a verb) and its participants (arguments).

## 1. Semantic Roles
A semantic role (or thematic role) describes the underlying relationship between an argument and a predicate.
- **Agent**: The intentional doer of the action.
- **Patient/Theme**: The entity undergoing the action or change.
- **Instrument**: The tool used to perform the action.
- **Goal**: The destination of the action.

## 2. Major Semantic Frameworks
### PropBank (Proposition Bank)
PropBank uses **Proto-roles** (Arg0, Arg1, ...) to avoid the ambiguity of universal labels like "Agent."
- **Arg0**: Typically the Agent.
- **Arg1**: Typically the Patient.
- **Example**: "John (Arg0) ate the apple (Arg1)."
- Uses **Sense Tags** (e.g., `eat.01`) to handle different predicate meanings.

### FrameNet
Based on **Frame Semantics**, it groups predicates into "Frames" (e.g., `Applying_heat`) with specific **Frame Elements** (FE).
- **Frame**: `Applying_heat`.
- **FEs**: `Cook`, `Food`, `Heating_instrument`.
- **Lexical Units**: bake, boil, fry, grill.

## 3. Semantic Role Labeling (SRL)
The task of automatically identifying the predicates and their arguments in a sentence.
- **Feature-Based Approach**: Uses syntactic features (path from verb to NP in a parse tree), voice (active/passive), and POS tags.
- **Constrained Optimization**: Ensuring that arguments do not overlap and that core roles are filled only once.
- **Neural SRL**: Using Bi-LSTMs or Transformers to encode the entire sentence and predict roles directly, often without explicit parse trees (Eisenstein, 2018).

---

#semantics #srl #propbank #framenet
