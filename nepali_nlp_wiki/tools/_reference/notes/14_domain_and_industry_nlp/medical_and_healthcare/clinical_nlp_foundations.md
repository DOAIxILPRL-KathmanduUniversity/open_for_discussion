# Clinical NLP Foundations

> [!IMPORTANT] Gist
> Clinical language processing is the automated analysis of clinical notes to support healthcare delivery. It balances the tension between "expressivity" (narrative) and "structure" (EHR) (Demner-Fushman & Xu, 2024).

## 1. Historical Concepts
- **Problem-Oriented Medical Record (POMR)**: Introduced by Dr. Lawrence Weed, advocating that records should be structured around specific patient problems.
- **SOAP Notes**: The standard structure for progress notes:
    - **S**ubjective impressions.
    - **O**bjective data.
    - **A**ssessment of the situation.
    - **P**lan of action.
- **Dr. Weed's Philosophy**: "The writing of progress notes... should be the cornerstone of the physician’s scientific development." Notes should be linked to problems to ensure clinical reasoning is documented.

## 2. Expressivity vs. Structure
- **Narrative (Unstructured)**: Flexible and expressive, allowing clinicians to document nuances.
- **Structured (EHR)**: Necessary for automated reuse, analysis, and biosurveillance.
- **The Tension**: Highly structured documentation can hamper workflow, while highly expressive documentation is difficult for machines to analyze.

## 3. Clinical Redundancy & Redundancy Management
- **Information Overload**: Rapid accumulation of longitudinal notes often leads to redundant data, masking new and clinically relevant insights.
- **Copy-and-Paste (C&P)**: Highly prevalent (~80% of physicians) but generates noise. Redundant information increases with the size of the notes.
- **Automated Highlighting**: Using **Bigram Language Models** to identify new information based on preceding notes. Highlighting "new" content reduces the perceived workload of clinicians and improves diagnostic accuracy by increasing the contrast between targets and distractors (Su et al., 2020).

---

#domain-specific #clinical-nlp #pomr #soap #ehr
