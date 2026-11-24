# Neural LM Basics

## Machines that Read and Write
The evolution of NLP has transformed computers into machines that don't just process characters, but "read" and "write" human language.
- **Language Understanding**: Enabling machines to interpret intent and context.
- **Language Generation**: Empowering computers to produce creative and coherent responses.
- **Creative Power**: Leveraging Generative Deep Learning (e.g., GANs, Transformers) to master the "Creative Power of AI."

## From N-grams to Neural
- Bengio et al. (2003) — first neural LM
- Continuous word representations replace discrete counts
- Fixed context window → learned representations

## Architecture
- Embedding layer → hidden layers → softmax over vocabulary
- Training: cross-entropy loss, teacher forcing

## Feed-Forward Networks (MLP)
A Feed-Forward Network (or Multi-Layer Perceptron) is the basic unit of deep learning models. It consists of:
- **Input Layer**: The feature vector $x$.
- **Hidden Layers**: Intermediate trainable representations $\phi(x)$.
- **Output Layer**: The final prediction $\hat{y}$ (often a softmax over the vocabulary).

$$\hat{y} = \sigma(\phi(x) \cdot w + b)$$

### Activation Functions
Neurons use activation functions to introduce non-linearity, allowing the network to learn complex patterns:
- **Sigmoid**: Maps output to $[0, 1]$.
- **ReLU (Rectified Linear Unit)**: $f(x) = \max(0, x)$. It replaces negative values with zero, preventing the "vanishing gradient" problem and allowing for faster training in deep networks (Dunn, 2022).

## Regularization (L2)
To prevent overfitting where the model relies too much on a few features, we add a penalty to the loss function based on the magnitude of weights:
$$\text{Loss} = \text{CrossEntropy} + \lambda \sum w^2$$
- This encourages the model to spread weight across more features, improving its ability to generalize to unseen data.

---

#lm #deep-learning
