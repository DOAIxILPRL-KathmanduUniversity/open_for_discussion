import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🤗 HuggingFace Fine-tuning Lab

        Fine-tune a pre-trained model on a text classification task.
        """
    )
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        ## Pipeline

        ```python
        from transformers import pipeline

        classifier = pipeline("sentiment-analysis")
        result = classifier("I love NLP!")
        print(result)
        ```

        ## Fine-tuning Steps
        1. Load dataset with `datasets`
        2. Tokenize with `AutoTokenizer`
        3. Load model with `AutoModelForSequenceClassification`
        4. Train with `Trainer` API
        """
    )
    return


@app.cell
def _():
    from transformers import pipeline

    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    results = classifier([
        "NLP is fascinating!",
        "I hate debugging tokenizers.",
        "Transformers changed everything.",
    ])
    for r in results:
        print(f"{r['label']:10} {r['score']:.4f}")
    return


if __name__ == "__main__":
    app.run()
