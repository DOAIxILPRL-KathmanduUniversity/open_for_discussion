import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🏗️ Transformer from Scratch

        Build a minimal transformer encoder in PyTorch to understand the architecture.
        """
    )
    return (mo,)


@app.cell
def _():
    import torch
    import torch.nn as nn
    import math

    class ScaledDotProductAttention(nn.Module):
        def forward(self, Q, K, V, mask=None):
            d_k = Q.size(-1)
            scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
            if mask is not None:
                scores = scores.masked_fill(mask == 0, float("-inf"))
            attn = torch.softmax(scores, dim=-1)
            return torch.matmul(attn, V), attn

    class MultiHeadAttention(nn.Module):
        def __init__(self, d_model, n_heads):
            super().__init__()
            self.n_heads = n_heads
            self.d_k = d_model // n_heads
            self.W_q = nn.Linear(d_model, d_model)
            self.W_k = nn.Linear(d_model, d_model)
            self.W_v = nn.Linear(d_model, d_model)
            self.W_o = nn.Linear(d_model, d_model)
            self.attention = ScaledDotProductAttention()

        def forward(self, Q, K, V, mask=None):
            batch = Q.size(0)
            Q = self.W_q(Q).view(batch, -1, self.n_heads, self.d_k).transpose(1, 2)
            K = self.W_k(K).view(batch, -1, self.n_heads, self.d_k).transpose(1, 2)
            V = self.W_v(V).view(batch, -1, self.n_heads, self.d_k).transpose(1, 2)
            out, attn = self.attention(Q, K, V, mask)
            out = out.transpose(1, 2).contiguous().view(batch, -1, self.n_heads * self.d_k)
            return self.W_o(out)

    # Quick test
    mha = MultiHeadAttention(d_model=64, n_heads=4)
    x = torch.randn(2, 10, 64)  # batch=2, seq=10, dim=64
    out = mha(x, x, x)
    print(f"Input shape:  {x.shape}")
    print(f"Output shape: {out.shape}")
    return


if __name__ == "__main__":
    app.run()
