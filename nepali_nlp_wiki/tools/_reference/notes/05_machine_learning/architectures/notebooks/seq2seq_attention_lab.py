import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🔗 Seq2Seq & Attention Lab

        Visualize attention weights and understand the encoder-decoder flow.
        """
    )
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        ## Attention Intuition

        Given encoder states $h_1, h_2, ..., h_n$ and decoder state $s_t$:

        1. Compute alignment scores: $e_{t,i} = a(s_t, h_i)$
        2. Normalize: $\\alpha_{t,i} = \\text{softmax}(e_{t,i})$
        3. Context vector: $c_t = \\sum_i \\alpha_{t,i} h_i$
        """
    )
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    # Simulated attention weights for a translation example
    src = ["le", "chat", "est", "sur", "le", "tapis"]
    tgt = ["the", "cat", "is", "on", "the", "mat"]

    # Random plausible attention weights
    np.random.seed(42)
    attn = np.eye(6) * 0.6 + np.random.rand(6, 6) * 0.1
    attn = attn / attn.sum(axis=1, keepdims=True)

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.imshow(attn, cmap="Blues")
    ax.set_xticks(range(len(src)))
    ax.set_xticklabels(src, rotation=45)
    ax.set_yticks(range(len(tgt)))
    ax.set_yticklabels(tgt)
    ax.set_xlabel("Source")
    ax.set_ylabel("Target")
    ax.set_title("Attention Weights")
    plt.tight_layout()
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
