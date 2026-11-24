# RNN Basics

## Key Ideas
- Process sequences one step at a time
- Hidden state carries information across timesteps
- h_t = f(W_h · h_{t-1} + W_x · x_t + b)

## Problems
- Vanishing / exploding gradients
- Difficulty with long-range dependencies
- Sequential computation (slow to train)

## Variants
- Elman RNN (vanilla)
- Jordan RNN
- Bidirectional RNN

---

#sequence #deep-learning
