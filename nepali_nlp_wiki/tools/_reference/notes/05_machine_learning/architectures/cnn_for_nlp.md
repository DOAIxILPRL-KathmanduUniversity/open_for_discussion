# CNN for NLP: Kernels of Knowledge

> [!IMPORTANT] Gist
> While RNNs process text sequentially, Convolutional Neural Networks (CNNs) use "kernels" or filters to capture local patterns (n-grams) regardless of their position in the text. This is often described as finding "kernels of knowledge" (Hobson et al., 2024).

## 1. How CNNs Work for Text
- **1D Convolutions**: Filters slide over word embeddings to detect specific phrases or patterns.
- **Kernels**: Small windows (e.g., size 3 for trigrams) that learn to recognize important linguistic features.
- **Max-Pooling**: Reducing the output of the convolution to the most significant feature discovered, making the model invariant to the pattern's location.

## 2. Advantages for NLP
- **Parallelism**: Unlike RNNs, CNNs can process all parts of the text simultaneously, leading to faster training.
- **Local Context**: Excellent for text classification and sentiment analysis where specific "trigger words" or phrases determine the outcome.

## 3. Architecture
1. **Input Layer**: Word embeddings (e.g., Word2Vec, GloVe).
2. **Convolutional Layer**: Multiple filters of varying sizes.
3. **Pooling Layer**: Max-pooling over time.
4. **Fully Connected Layer**: Final classification or regression.

---

#sequence-models #cnn #convolution #text-classification
