import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🧭 Word Vectors Explorer

        Load pre-trained word vectors and explore semantic relationships.
        """
    )
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        ## Setup

        To use this notebook, download GloVe vectors first:
        ```bash
        # Download 50d vectors (~66MB)
        wget https://nlp.stanford.edu/data/glove.6B.zip
        unzip glove.6B.zip
        ```

        Or use `gensim` to load Word2Vec / GloVe:
        ```python
        import gensim.downloader as api
        model = api.load("glove-wiki-gigaword-50")
        ```
        """
    )
    return


@app.cell
def _():
    # Placeholder: load vectors and explore
    # model.most_similar("king")
    # model.most_similar(positive=["king", "woman"], negative=["man"])
    pass
    return


if __name__ == "__main__":
    app.run()
