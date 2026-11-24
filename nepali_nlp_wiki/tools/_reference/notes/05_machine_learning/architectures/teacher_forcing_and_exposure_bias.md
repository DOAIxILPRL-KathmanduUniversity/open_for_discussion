# Teacher Forcing & Exposure Bias

> [!IMPORTANT] Gist
> Sequence models are trained by being "spoon-fed" the correct answers, but at inference time, they must rely on their own (potentially wrong) previous predictions. This discrepancy is known as Exposure Bias.

## 1. Teacher Forcing
During training, the model's input at time $t$ is the **ground truth** (actual correct word) from time $t-1$, regardless of whether the model predicted the correct word or not.
- **Goal**: Accelerate training and prevent the model from drifting into "word salad" early on.
- **Analogy**: A teacher correcting a student immediately after every word during a recitation.

## 2. Exposure Bias
During inference (generation), the ground truth is unavailable. The model must use its own prediction $\hat{y}_{t-1}$ as the input for time $t$.
- **The Problem**: If the model makes a small error at step 1, it is "exposed" to a context it never saw during training. These errors accumulate, leading to nonsensical output.
- **Discrepancy**: The training distribution (clean ground truth) $\neq$ Inference distribution (noisy model output).

## 3. Mitigating Exposure Bias
- **Scheduled Sampling**: Gradually transition from feeding ground truth to feeding the model's own predictions during training.
- **RL-based Training (REINFORCE)**: Optimizing for the final sequence metric (like BLEU or ROUGE) rather than the next-word cross-entropy loss.
- **Contrastive Learning**: Training the model to distinguish between its own "bad" generations and "good" human text.

## 4. Connection to Transformers
While RNNs suffer heavily from exposure bias due to their recurrent nature, Transformers also face this challenge in autoregressive generation (decoder-only models like GPT). The discrepancy remains between the teacher-forced training phase and the free-running inference phase.

---

#sequence-models #training #optimization #exposure-bias #teacher-forcing
