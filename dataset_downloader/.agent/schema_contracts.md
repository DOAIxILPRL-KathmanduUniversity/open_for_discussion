# Target Schema Contracts & Export Specifications

All transformed datasets emitted by `downloader.py` adhere to the standard JSON Lines (`.jsonl`) schemas specified below.

---

## 1. SFT / Instruction Tuning Format (`export_format: gemma_instruction`)

Optimized for **Gemma 4**, **Llama 3**, and modern chat-tuned models. Every line in the `.jsonl` file must be a valid JSON object:

```json
{
  "task_type": "sft",
  "task": "reading_comprehension",
  "instruction": "दिएको सन्दर्भ पढेर सोधिएको प्रश्नको सही उत्तर दिनुहोस्।",
  "input": "सन्दर्भ: ... \n\nप्रश्न: ...",
  "output": "सही उत्तर ...",
  "messages": [
    {
      "role": "user",
      "content": "दिएको सन्दर्भ पढेर सोधिएको प्रश्नको सही उत्तर दिनुहोस्:\n\nसन्दर्भ: ...\n\nप्रश्न: ..."
    },
    {
      "role": "model",
      "content": "सही उत्तर ..."
    }
  ]
}
```

---

## 2. Pretraining Text Format (`export_format: text_stream`)

Used for continued pre-training, masked language modeling (RoBERTa), and causal language modeling:

```json
{
  "task_type": "pretrain",
  "task": "causal_language_modeling",
  "text": "नेपाल एक बहुभाषिक र बहुसांस्कृतिक देश हो..."
}
```

---

## 3. Similarity & Dense Retrieval Format (`export_format: embedding_pair`)

Optimized for **Gemma Embedding 2** and dual-encoder contrastive models (Bi-encoders, Contriever, BGE):

```json
{
  "task_type": "similarity",
  "task": "dense_retrieval_rag",
  "query": "search_query: नेपालको राजधानी कुन हो?",
  "positive": "नेपालको राजधानी काठमाडौं हो।",
  "negative": "पोखरा नेपालको पर्यटकीय सहर हो।",
  "score": 1.0
}
```

---

## 4. Platform Workflow Guidelines

| Platform | Recommended Fetch Method | Notes |
| :--- | :--- | :--- |
| **Hugging Face** | `hf_api_stream` | Zero API key needed. Streams JSON rows directly via `datasets-server.huggingface.co`. |
| **GitHub** | `raw_git_stream` | Direct raw URL curl via `raw.githubusercontent.com`. Handles text, CSV, and CoNLL-U parsing. |
| **Kaggle** | `kaggle_cli` | Downloads via official Kaggle CLI. Requires `~/.kaggle/kaggle.json` credentials for full archives. |

