# Masterclass: Corpus Analysis & Exploratory NLP

> [!IMPORTANT] Gist
> Understanding the "lexical pulse" of a corpus is the first step in any NLP project. NLTK provides powerful tools for statistical analysis, concordance (context search), and semantic similarity exploration.

## 1. Corpus Acquisition
Using the **Kaggle Nepali News Dataset**, we focus on domain-specific subsets (e.g., **Agriculture**) to understand how specialized language is used in Nepali media.

## 2. Statistical Analysis with NLTK
The `nltk.Text` object wraps a list of tokens and enables high-level statistical queries:

### A. Concordance (Word-in-Context)
Reveals every occurrence of a word together with some context. 
- *Example*: Searching for "खेती" (farming) in an agricultural corpus shows the verbs associated with it (e.g., "गर्ने", "बढाउने").

### B. Distributional Similarity
The `similar()` function identifies words that appear in similar contexts.
- *Example*: In a Nepali news corpus, searching for "छ" (is) might yield "हो" or "गरेको", revealing functional synonyms in the grammar.

### C. Common Contexts
Identifies the shared linguistic environments of two or more words.
- *Example*: `document.common_contexts(["खेती", "सुरु"])` might reveal contexts like "व्यावसायिक _ गर्न", highlighting common collocations.

## 3. Workflow: From Raw Text to Analysis
1.  **Tokenization**: Splitting raw strings into word units (`nltk.word_tokenize`).
2.  **Normalization**: (Optional) Lowercasing or removing punctuation for cleaner statistics.
3.  **Exploration**: Using `FreqDist` to find the most common terms and `Concordance` to understand usage patterns.

---

**Notebook**: [corpus_analysis_masterclass.py](notebooks/corpus_analysis_masterclass.py) (NLTK & Kaggle Dataset)

#corpus-linguistics #nltk #nepali #exploratory-nlp #tokenization #concordance
