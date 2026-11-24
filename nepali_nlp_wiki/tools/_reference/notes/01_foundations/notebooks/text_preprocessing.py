import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🧹 Text Preprocessing Lab

        Hands-on exploration of text cleaning, normalization, and regex patterns.
        """
    )
    return (mo,)


@app.cell
def _():
    import re
    import unicodedata

    sample_text = """
    <p>Hello, World! This is an NLP notebook. 🎉</p>
    It has   extra   spaces and MIXED case.
    Unicode: café, naïve, नेपाली
    """

    # Step 1: Remove HTML
    cleaned = re.sub(r"<[^>]+>", "", sample_text)

    # Step 2: Normalize unicode
    cleaned = unicodedata.normalize("NFC", cleaned)

    # Step 3: Collapse whitespace
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    print(cleaned)
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Exercises

        1. Write a regex to extract all email addresses from a string
        2. Normalize Devanagari text with `unicodedata.normalize("NFC", text)`
        3. Build a reusable `clean_text()` function
        """
    )
    return


if __name__ == "__main__":
    app.run()
