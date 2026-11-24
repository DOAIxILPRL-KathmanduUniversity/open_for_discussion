# Federated Learning for NLP

> [!IMPORTANT] Gist
> Federated Learning (FL) is a decentralized machine learning setting where multiple entities (clients) collaborate to train a model under the coordination of a central server, without exchanging raw data. This is critical for privacy-preserved NLP (Garg et al., 2024).

## 1. Core Architecture
- **Centralized FL**: A hub-and-spoke topology where a central server aggregates focused updates from clients.
- **Decentralized (Peer-to-Peer) FL**: Clients interact directly without a central server.
- **Client-Server Workflow**:
    1. Server initializes the model.
    2. Clients download the model and train on local data.
    3. Clients upload focused updates (gradients/parameters).
    4. Server aggregates updates to update the global model.

## 2. Key Algorithms
- **DSSGD (Distributed Selective SGD)**: Clients exchange model parameters selectively during training.
- **FedAvg (Federated Averaging)**: The most widely used algorithm for aggregating client updates by taking a weighted average of model weights.
- **FedProx**: Addresses heterogeneity in client data and systems by adding a proximal term to the objective.
- **SCAFFOLD**: Uses control variates to reduce "client drift" caused by non-IID data.

## 3. Security & Privacy
- **Differential Privacy**: Adding noise to updates to ensure individual data instances cannot be identified.
- **Secure Multiparty Computation (SMPC)**: Ensuring that no party can see the private data of others during the aggregation process.

## 4. NLP Applications
- **Next-Word Prediction**: Training on user chat history without uploading private texts.
- **Photo Quality Assessment**: Accessing user archives locally for personalized suggestions.

---

#modern-frontiers #federated-learning #privacy #security
