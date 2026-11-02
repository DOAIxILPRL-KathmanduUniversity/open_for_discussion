# Step-by-Step Curation Workflow for 2026 NLP Engineers

When curating a new public dataset for the registry, execute the following 5-step protocol:

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  1. Web Search   │ ──> │ 2. Live Inspect  │ ──> │ 3. Verify Purity │ ──> │ 4. Map & Format  │ ──> │ 5. Test & Commit │
└──────────────────┘     └──────────────────┘     └──────────────────┘     └──────────────────┘     └──────────────────┘
```

---

### Step 1: Web Search & Repository Discovery
- Query public platforms:
  - Hugging Face: `site:huggingface.co/datasets nepali <task>`
  - GitHub: `site:github.com nepali dataset <task>`
  - Kaggle: `site:kaggle.com/datasets nepali <task>`
- Confirm that the repository actually exists and is publicly accessible.

---

### Step 2: Live Webpage / API Inspection
- Do not guess column names. Retrieve actual sample rows:
  - For Hugging Face:
    ```bash
    curl -s "https://datasets-server.huggingface.co/rows?dataset=<ORG/REPO>&config=default&split=train&offset=0&limit=2"
    ```
  - For GitHub:
    ```bash
    curl -s "https://raw.githubusercontent.com/<ORG/REPO>/<BRANCH>/<PATH>" | head -n 30
    ```
- Identify exact column names (e.g. `premise`, `hypothesis`, `context`, `question`, `text`).

---

### Step 3: Devanagari Purity & License Verification
- Verify open licensing: `MIT`, `Apache-2.0`, `CC-BY`, `CC-BY-SA`, or `OpenRAIL`.
- Confirm Devanagari character content ($\text{U}+0900$ to $\text{U}+097\text{F}$). Reject spam, corrupted fonts, or non-Nepali text.

---

### Step 4: Author Workflow YAML
Create a new recipe in `workflows/<platform>/<task_name>.yaml`:
```yaml
id: sft_new_task_hf
name: "Human Readable Name"
platform: huggingface # huggingface | github | kaggle
task_type: sft # sft | pretrain | similarity
task: domain_qa
source_url: "https://huggingface.co/datasets/example/dataset"
license: cc-by-4.0
language: ne
script: Devanagari

workflow:
  repo_id: "example/dataset"
  split: train
  fetch_method: "hf_api_stream"
  raw_fields:
    context: "source_context"
    question: "source_query"

mapping:
  instruction: "दिएको सन्दर्भको आधारमा उत्तर दिनुहोस्।"
  input_template: "सन्दर्भ: {context}\nप्रश्न: {question}"
  output_template: "{answers}"
  task_prefix: "नेपाली प्रश्नोत्तर:\n\n"

export_format: gemma_instruction
test_sample_limit: 5
```

---

### Step 5: Test Verification & Auto-Cleanup
Execute the verification test via `downloader.py`:
```bash
python downloader.py test sft_new_task_hf
```
- The test command will fetch 5 rows, format them, validate types, display sample JSON, and automatically purge the temporary file.
- Once verified, if the dataset represents a notable resource, update the corresponding node in `nepali_nlp_wiki/wiki/datasets/`.

