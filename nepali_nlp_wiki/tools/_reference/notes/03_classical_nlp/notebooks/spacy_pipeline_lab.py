import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🔬 spaCy Pipeline Lab

        Explore tokenization, POS tagging, NER, and dependency parsing with spaCy.

        ```bash
        # First, download the model:
        python -m spacy download en_core_web_sm
        ```
        """
    )
    return (mo,)


@app.cell
def _():
    import spacy

    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Apple is looking at buying a U.K. startup for $1 billion.")

    # Tokens + POS
    for token in doc:
        print(f"{token.text:15} {token.pos_:8} {token.dep_:12} {token.head.text}")
    return (doc,)


@app.cell
def _(doc):
    # Named Entities
    for ent in doc.ents:
        print(f"{ent.text:20} {ent.label_:10} {ent.start_char}-{ent.end_char}")
    return


if __name__ == "__main__":
    app.run()
