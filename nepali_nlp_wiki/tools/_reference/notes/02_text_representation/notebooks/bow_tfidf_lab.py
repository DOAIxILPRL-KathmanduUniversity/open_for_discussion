# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.3",
# ]
# ///

import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 📊 BoW & TF-IDF Lab

        Compare Bag-of-Words and TF-IDF representations on a small corpus.
        """
    )
    return


@app.cell
def _():
    from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
    import pandas as pd

    corpus = [
        "NLP is the study of language and computers",
        "Language models predict the next word",
        "Computers can now understand language",
    ]

    # Bag of Words
    bow = CountVectorizer()
    bow_matrix = bow.fit_transform(corpus)
    df_bow = pd.DataFrame(bow_matrix.toarray(), columns=bow.get_feature_names_out())

    df_bow
    return (corpus,)


@app.cell
def _(corpus):
    from sklearn.feature_extraction.text import TfidfVectorizer
    import pandas as pd

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(corpus)
    df_tfidf = pd.DataFrame(
        tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out()
    )

    df_tfidf.round(3)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
