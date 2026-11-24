# Speech Act Theory

> [!IMPORTANT] Gist
> Language is a form of action. Speech Act Theory (Austin & Searle) moves beyond *what* is said to *what is being done* by the speaker. This is the foundation of intent classification in dialogue systems.

## 1. The Three Levels of an Act
When we speak, we perform three simultaneous acts:
- **Locutionary Act**: The literal act of uttering a sentence with specific meaning and reference.
- **Illocutionary Act**: The intended effect or "force" of the utterance (e.g., promising, ordering, questioning).
- **Perlocutionary Act**: The actual effect on the listener (e.g., persuading, frightening, enlightening).

## 2. Searle's Taxonomy of Illocutionary Acts
1.  **Assertives**: Committing the speaker to the truth of a proposition (e.g., stating, claiming).
2.  **Directives**: Trying to get the listener to do something (e.g., ordering, requesting, advising).
3.  **Commissives**: Committing the speaker to a future course of action (e.g., promising, threatening).
4.  **Expressives**: Expressing a psychological state (e.g., thanking, apologizing, congratulating).
5.  **Declarations**: Changing the state of the world by virtue of the utterance (e.g., "I pronounce you husband and wife").

## 3. Indirect Speech Acts
Where the illocutionary force is different from the literal locutionary meaning.
- **Example**: "Can you pass the salt?"
    - **Literal**: A question about physical ability.
    - **Act**: A request for action (Directive).
- **NLP Challenge**: Recognizing intent when the syntactic form (Question) contradicts the pragmatic function (Request).

## 4. NLP Applications
- **Dialogue Systems**: Moving from "Slot Filling" to "Intent Classification."
- **NLU**: Identifying user goals (e.g., "Is there a flight to NYC?" = "Book a flight").
- **Toxicity Detection**: Distinguishing between a literal statement and a "threat" (Commissive).

---

#pragmatics #dialogue #intent #speech-acts #austin #searle
