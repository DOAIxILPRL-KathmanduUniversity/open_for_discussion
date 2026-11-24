# Data Annotation Principles

> [!IMPORTANT] Gist
> Manual annotation is the **"Hidden Pillar"** where linguistics hides in modern NLP (Fort, 2016). High-quality data is the foundation of reliable supervised models; inconsistency in the "Gold Standard" degrades even the most advanced ML architectures.

## 1. The Annotation Pipeline
1.  **Guideline Drafting**: Building consensus through formal rules.
2.  **Pilot Study**: Iterative testing to refine guidelines and assess task difficulty.
3.  **Pre-campaign**: Data selection, recruiting, and **Annotator Training** (critical for consistency).
4.  **Main Annotation**: Distributed task execution.
5.  **Finalization/Adjudication**: Experts (judges) resolve disagreements to create the final **Gold Standard**.

## 2. Annotation Layers & Treebanks
Complex linguistic data is often annotated in distinct, hierarchical layers (Hajiˇ cová et al., 2010):
- **Morphological Layer**: Lemma and POS tagging (e.g., m-layer in PDT).
- **Analytical/Syntactic Layer**: Surface dependency or constituency structures (e.g., a-layer).
- **Tectogrammatical Layer**: Deep-syntax representing underlying semantic relations, coreference, and topic-focus articulation (e.g., t-layer in the Prague Dependency Treebank).
- **The Penn Treebank (PTB)**: The classic constituency-based corpus using a skeletal structure for rapid annotation of large volumes of text (Marcus et al., 1993).

## 3. Inter-Annotator Agreement (IAA)
IAA measures how much two or more annotators agree on the same data.
- **Percent Agreement**: Simple but flawed because it doesn't account for random chance.
- **Cohen's Kappa ($\kappa$)**: Used for two annotators.
    - $\kappa = \frac{p_o - p_e}{1 - p_e}$
    - $p_o$ = observed agreement, $p_e$ = expected agreement by chance.
- **Fleiss' Kappa**: Generalization of Cohen's Kappa for more than two annotators.
- **Krippendorff's Alpha ($\alpha$)**: The most robust metric; handles different data scales (nominal, ordinal, interval) and missing data.

## 4. The Expertise Triad
Quality is not just "expert vs. naive." Expertise exists in three layers:
- **Domain Expertise**: Knowledge of the subject (e.g., Medicine, Law).
- **Annotation Expertise**: Knowledge of the linguistic formalism (e.g., dependency syntax).
- **Task Expertise**: Familiarity with the specific tool and guidelines. (Productive crowdsourcing workers often become task experts).

## 5. Crowdsourcing & Gamification
- **Remunerated Platforms**: (e.g., MTurk) Transparent task, financial motivation. Ethical considerations include fair pay and "rejection" transparency.
- **GWAPs (Games With A Purpose)**: (e.g., *ZombiLingo*, *Phrase Detectives*) Volunteer, gamified tasks. Players' innate learning capacities are used to generate massive linguistic data.

## 6. Crowdsourcing via Mechanical Turk (MTurk)
MTurk has become a premier resource for optimizing sample sizes and minimizing costs in ANLP research (Strain & Booker, 2012).
- **HITs (Human Intelligence Tasks)**: Micro-tasks (e.g., sentiment labeling, paraphrase checking) posted for workers.
- **Worker Qualification**: Using "Gold Standard" test questions to filter for high-quality workers before allowing them to access the main task.
- **Institutional Review Board (IRB)**: Critical ethical oversight for research involving human participants (compensation, data privacy).
- **Pros & Cons**:
    - **Pros**: Rapid data collection, diverse worker pool, low cost.
    - **Cons**: Potential for "low-effort" responses, lack of linguistic training in workers, ethical concerns regarding fair wage.

## 7. Common Pitfalls
- **Label Drift**: Annotators changing their interpretation of a label over time.
- **Ambiguity**: Guidelines that don't cover overlapping cases (e.g., is "New York" a GPE or an ORG in "New York passed a law"?).
- **Annotator Bias**: Subjective interpretation affecting labels (common in sentiment or toxicity tasks).

---

#foundations #annotation #reliability #kappa #iaa
