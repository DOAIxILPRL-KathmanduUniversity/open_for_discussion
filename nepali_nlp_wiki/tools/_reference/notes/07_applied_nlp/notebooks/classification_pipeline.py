import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🏷️ Classification Pipeline Lab

        End-to-end text classification with scikit-learn and transformers.
        """
    )
    return (mo,)


@app.cell
def _():
    from sklearn.datasets import fetch_20newsgroups
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import classification_report
    from sklearn.model_selection import train_test_split

    # Load a subset of 20 Newsgroups
    categories = ["sci.space", "comp.graphics", "rec.sport.baseball"]
    data = fetch_20newsgroups(subset="all", categories=categories)

    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    tfidf = TfidfVectorizer(max_features=10000, stop_words="english")
    X_train_vec = tfidf.fit_transform(X_train)
    X_test_vec = tfidf.transform(X_test)

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train_vec, y_train)

    y_pred = clf.predict(X_test_vec)
    print(classification_report(y_test, y_pred, target_names=data.target_names))
    return


if __name__ == "__main__":
    app.run()
