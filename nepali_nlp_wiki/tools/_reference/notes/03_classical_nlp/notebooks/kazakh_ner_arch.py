import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🏗️ Bi-LSTM-CNN-CRF Architecture (Kazakh NER)

        Demonstrating the architecture proposed by Hayinaer et al. (2025) for low-resource Named Entity Recognition.
        
        The model benefits from:
        1. **Word + Stem Embeddings** (mitigating data sparsity)
        2. **CNN** (local feature extraction)
        3. **Bi-LSTM** (global context)
        4. **CRF** (label dependency modeling)
        """
    )
    return (mo,)


@app.cell
def _():
    import torch
    import torch.nn as nn

    class KazakhNERModel(nn.Module):
        def __init__(self, vocab_size, stem_vocab_size, embed_dim, hidden_dim, tagset_size):
            super().__init__()
            self.word_embeddings = nn.Embedding(vocab_size, embed_dim)
            self.stem_embeddings = nn.Embedding(stem_vocab_size, embed_dim)
            
            # CNN for character/local features (simulated here as a layer on combined embeddings)
            self.conv1d = nn.Conv1d(in_channels=embed_dim * 2, out_channels=64, kernel_size=3, padding=1)
            
            # Bi-LSTM
            self.lstm = nn.LSTM(64, hidden_dim // 2, num_layers=1, bidirectional=True, batch_first=True)
            
            # Linear layer to tag space
            self.hidden2tag = nn.Linear(hidden_dim, tagset_size)
            
        def forward(self, words, stems):
            # Combine Word and Stem embeddings (Additive/Concatenative only)
            w_emb = self.word_embeddings(words)
            s_emb = self.stem_embeddings(stems)
            x = torch.cat((w_emb, s_emb), dim=-1) # (batch, seq, embed*2)
            
            # CNN expects (batch, channels, seq)
            x = x.transpose(1, 2)
            x = torch.relu(self.conv1d(x))
            x = x.transpose(1, 2)
            
            # LSTM
            lstm_out, _ = self.lstm(x)
            
            # Tag space
            tag_space = self.hidden2tag(lstm_out)
            return tag_space

    # Example initialization
    model = KazakhNERModel(vocab_size=1000, stem_vocab_size=500, embed_dim=50, hidden_dim=128, tagset_size=7)
    print("Kazakh NER Model (Bi-LSTM-CNN-CRF backbone) initialized.")
    return KazakhNERModel, model


@app.cell
def _(mo):
    mo.md(
        """
        ## CRF Layer (Logic)
        The CRF layer computes the optimal sequence using the transition matrix.
        $$s(H, Y) = \sum P_{i, y_i} + \sum T_{y_{i-1}, y_i}$$
        
        In PyTorch, this is typically handled by `pytorch-crf` or custom transition parameter wrappers.
        """
    )
    return


if __name__ == "__main__":
    app.run()
