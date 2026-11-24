# Empathetic Conversational Agents

> [!IMPORTANT] Gist
> Modern conversational agents strive to move beyond literal meaning to recognize and elicit emotions, using hierarchical models for empathetic social interaction (Pillai & Tedesco, 2024).

## 1. Empathetic Dialogue Modeling
- **Unsupervised Hierarchical Model**: Learning high-level conversation structures (intents, themes) without explicit labels, followed by refinement using supervised or reinforcement learning.
- **Eliciting Sentiments**: The agent is trained to select responses that elicit positive sentiments or express empathy based on the user's emotional state.

## 2. Paralinguistic Aspects (Non-Literal Content)
- **EMOTRON**: An expressive Text-to-Speech (TTS) system that uses spectrogram regression loss combined with emotional classification loss to generate voice with conditioned emotions.
- **Affective Interactions**: Handling irony, satire, and empathy in both textual and vocal modalities.

## 3. Dialogue State Tracking (DST)
- **Adapter Modules**: Small, trainable units inserted into pre-trained models to adapt them to specific dialogue tasks without re-training the entire model.
- **LSTMs with Attention**: Used for keeping context flowing and remembering long-term dependencies in the conversation state.

---

#applied-nlp #conversational-agents #empathy #emotron #paralinguistics #adapter-modules
