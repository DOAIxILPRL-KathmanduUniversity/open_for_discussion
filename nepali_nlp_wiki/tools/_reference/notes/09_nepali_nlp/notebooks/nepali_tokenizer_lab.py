import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🇳🇵 Nepali Tokenizer Lab

        Explore tokenization challenges for Devanagari text.
        """
    )
    return (mo,)


@app.cell
def _():
    import unicodedata
    import re

    nepali_text = "नेपाली भाषा प्रशोधन एउटा चुनौतीपूर्ण क्षेत्र हो।"

    # Unicode normalization
    normalized = unicodedata.normalize("NFC", nepali_text)

    # Simple whitespace tokenization
    tokens = normalized.split()
    print(f"Tokens: {tokens}")
    print(f"Count:  {len(tokens)}")

    # Character-level analysis
    for char in "प्रशोधन":
        print(f"  U+{ord(char):04X}  {unicodedata.name(char, '?'):40} {char}")
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Exercises

        1. Compare tokenization of `"संयुक्त"` at character vs. syllable level
        2. Write a Devanagari sentence splitter using `।` (purna viram)
        3. Count unique Devanagari characters vs. Latin in a mixed text
        """
    )
    return


if __name__ == "__main__":
    app.run()
