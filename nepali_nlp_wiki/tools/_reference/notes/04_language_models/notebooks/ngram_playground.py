import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🎲 N-gram Playground

        Build bigram/trigram models from scratch and generate text.
        """
    )
    return (mo,)


@app.cell
def _():
    from collections import Counter, defaultdict
    import random

    corpus = "the cat sat on the mat . the cat ate the fish . the dog sat on the log ."
    tokens = corpus.split()

    # Build bigram counts
    bigrams = defaultdict(Counter)
    for w1, w2 in zip(tokens, tokens[1:]):
        bigrams[w1][w2] += 1

    # Generate text
    word = "the"
    generated = [word]
    for _ in range(15):
        candidates = bigrams[word]
        if not candidates:
            break
        word = random.choices(list(candidates.keys()), weights=candidates.values())[0]
        generated.append(word)

    print(" ".join(generated))
    return


if __name__ == "__main__":
    app.run()
