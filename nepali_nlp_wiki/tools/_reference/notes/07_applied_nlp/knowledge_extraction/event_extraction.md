# Event Extraction

> [!IMPORTANT] Gist
> Event Extraction (EE) is a high-level Information Extraction task that identifies "who did what to whom, when, and where." It transforms unstructured text into structured "event records."

## 1. Event Anatomy (ACE/ERE Framework)
- **Event Trigger**: The word or phrase that most clearly expresses the event occurrence (usually a verb or noun like "fired," "merger," "protest").
- **Event Arguments**: The participants involved in the event.
- **Argument Roles**: The specific function of an participant (e.g., *Agent*, *Victim*, *Buyer*, *Place*, *Time*).
- **Event Type & Subtype**: Categorizing the event (e.g., `Conflict.Attack`, `Business.Merge`).

## 2. The Extraction Task
1.  **Trigger Detection**: Identifying words like "acquired" in "Company A acquired Company B."
2.  **Event Classification**: Determining that "acquired" refers to a `Business.Transaction`.
3.  **Argument Identification**: Finding "Company A" and "Company B."
4.  **Role Filling**: Assigning `Buyer` to "Company A" and `Target` to "Company B."

## 3. NLP Methodologies
- **Pattern-Based**: Using regex or dependency patterns (e.g., `[ORG] acquire [ORG]`). Robust but brittle to variations.
- **Feature-Based**: Using POS tags, NER types, and syntactic paths.
- **Neural/End-to-End**: Using Transformers to predict triggers and arguments simultaneously in a sequence-to-sequence or joint modeling approach.

## 4. Challenges
- **Event Coreference**: Identifying that "the merger" and "this acquisition" refer to the same event.
- **Modality & Factuality**: Distinguishing between an event that *happened* ("He was arrested") and one that is *hypothetical* ("He might be arrested").
- **Sparse Arguments**: An event's participants might be scattered across multiple sentences.

## 5. Negation & Scope Handling
Extracting events requires identifying if an event actually occurred or was negated (Blanco & Moldovan, 2012).
- **Negation Detection**: Identifying negation triggers (e.g., "no," "not," "never," "failed to").
- **Scope of Negation**: Determining which parts of the sentence are affected by the negation (e.g., in "He did not buy the car," the event `Business.Transaction` is negated).
- **Heuristics for Negation**: Using dependency paths to trace the relationship between the negation word and the event trigger.
- **Commonsense Knowledge**: Inferring implied negation (e.g., "He forgot to call" implies that the `Communication` event did *not* happen).

## 6. Applications
- **Intelligence & OSINT**: Tracking movements of threat actors or geopolitical events.
- **Financial Analytics**: Monitoring corporate actions (mergers, bankruptcy) for high-frequency trading.
- **Bio-NLP**: Extracting protein-protein interactions or gene expressions from research papers.

---

#applied #ie #event-extraction #triggers #arguments #factuality
