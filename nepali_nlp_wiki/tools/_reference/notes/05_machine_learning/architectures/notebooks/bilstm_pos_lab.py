import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🏷️ Bi-LSTM for POS Tagging

        This notebook demonstrates the implementation of a Bidirectional LSTM for Part-of-Speech tagging. 
        Bi-LSTMs are "canonical" for this task as they provide context from both left and right directions.
        """
    )
    return (mo,)


@app.cell
def _():
    import torch
    import torch.nn as nn
    import torch.optim as optim

    class BiLSTMPOSTagger(nn.Module):
        def __init__(self, vocab_size, embedding_dim, hidden_dim, tagset_size):
            super(BiLSTMPOSTagger, self).__init__()
            self.embeddings = nn.Embedding(vocab_size, embedding_dim)
            
            # The LSTM takes word embeddings as inputs, and outputs hidden states
            # with dimensionality hidden_dim. bidirectional=True doubles the output size.
            self.lstm = nn.LSTM(embedding_dim, hidden_dim // 2, bidirectional=True, batch_first=True)
            
            # The linear layer that maps from hidden state space to tag space
            self.hidden2tag = nn.Linear(hidden_dim, tagset_size)

        def forward(self, sentence):
            embeds = self.embeddings(sentence)
            lstm_out, _ = self.lstm(embeds)
            tag_space = self.hidden2tag(lstm_out)
            return tag_space

    # Example initialization
    # hidden_dim must be even to split between forward and backward
    model = BiLSTMPOSTagger(vocab_size=50, embedding_dim=32, hidden_dim=64, tagset_size=17)
    print("Bi-LSTM POS Tagger initialized.")
    return BiLSTMPOSTagger, model, optim


@app.cell
def _(mo):
    mo.md(
        """
        ## Why Bidirectional?
        In POS tagging, a word's category often depends on what follows it. 
        For example:
        - "The *bank* is closed." (*bank* = Noun)
        - "I *bank* with Chase." (*bank* = Verb)
        
        The forward pass sees "The", while the backward pass sees "is closed". 
        Concatenating them allows the model to "see" the full context.
        """
    )
    return


if __name__ == "__main__":
    app.run()
