import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md(
        """
        # 🔍 RAG Local Lab

        Build a minimal RAG pipeline with local embeddings and FAISS.
        """
    )
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        ## Architecture

        ```
        Documents → Chunker → Embedder → FAISS Index
                                              ↓
        Query → Embedder → Similarity Search → Top-K chunks
                                              ↓
                              LLM(query + chunks) → Answer
        ```

        ## Setup
        ```bash
        pip install faiss-cpu sentence-transformers
        ```
        """
    )
    return


@app.cell
def _():
    # Placeholder: implement when dependencies are installed
    # from sentence_transformers import SentenceTransformer
    # import faiss
    # import numpy as np
    #
    # model = SentenceTransformer("all-MiniLM-L6-v2")
    # docs = ["...", "...", "..."]
    # embeddings = model.encode(docs)
    # index = faiss.IndexFlatL2(embeddings.shape[1])
    # index.add(embeddings)
    pass
    return


if __name__ == "__main__":
    app.run()
