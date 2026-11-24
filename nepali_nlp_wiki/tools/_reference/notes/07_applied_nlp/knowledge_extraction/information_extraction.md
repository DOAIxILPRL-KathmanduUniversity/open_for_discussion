# Information Extraction (IE)

> [!IMPORTANT] Gist
> Information Extraction is the process of identifying phrases of interest (entities, relations, events) from unstructured textual data and transforming them into structured formats.

## 1. Core Components
- **Named Entity Recognition (NER)**: Identifying and classifying entities like names, places, and times.
- **Relation Extraction**: Finding semantic relationships between entities (e.g., "Company A" *acquired* "Company B").
- **Assertion Status Detection**: Determining the "status" of an entity in context—specifically in clinical text (e.g., Is a symptom *Present*, *Absent*, *Possible*, or *Conditional*?) (Thomas, 2020).
- **Event Discovery**: Analyzing noisy feeds (social media) to extract venues, times, and participants across multiple messages.

## 2. Techniques
- **Hidden Markov Models (HMMs)**: Used to extract relevant fields from research papers and narrative reports.
- **HMM-profiles**: Used in bioinformatics (e.g., Pfam) to identify and align protein domains semi-automatically.
- **Support Vector Machines (SVM)**: Applied to Arabic text for tokenization and POS tagging.
- **MetaMap**: Specifically designed for extracting concepts from medical abstracts and health-related text.

## 3. Case Studies & Tools
- **CONSTRUE**: A legacy system used by Reuters to categorize and index news stories automatically.
- **MITA (Intelligent Text Analyzer)**: Extracts information from life insurance applications (Metlife).
- **Blank Slate Language Processor (BSLP)**: Analyzes open-ended questionnaires in advertising.

---

#applied-nlp #ie #entities #events
