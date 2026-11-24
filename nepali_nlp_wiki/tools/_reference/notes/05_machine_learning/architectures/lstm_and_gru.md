# LSTM & GRU

## LSTM (Hochreiter & Schmidhuber, 1997)
- Cell state acts as "conveyor belt" for long-range info
- Three gates: forget, input, output
- Solves vanishing gradient problem

## GRU (Cho et al., 2014)
- Simplified LSTM — two gates: reset, update
- Fewer parameters, often similar performance
- Merges cell state and hidden state

## When to Use
- Pre-transformer era: go-to for sequence tasks
- Still useful for small data, edge deployment
- Largely superseded by transformers at scale

## Variants
- **Bidirectional LSTM**: See [[05_sequence_models/bidirectional_lstm]] for canonical architecture and math.

---

#sequence #deep-learning
