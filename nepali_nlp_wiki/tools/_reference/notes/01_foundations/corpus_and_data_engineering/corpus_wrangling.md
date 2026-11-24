# Corpus Wrangling & Ingestion

> [!IMPORTANT] Gist
> A corpus is not just a pile of text; it is a structured, managed collection of related documents. Robust ingestion requires handling provenance, schema predictability, and memory safety through streaming and multiprocessing (Bengfort et al., 2016).

## 1. Ingestion Strategies
- **Web Scraping**: Targeted extraction of specific elements from HTML (using `BeautifulSoup` or `Scrapy`). Requires handling `robots.txt` and rate limiting to be a "good web citizen."
- **Web Crawling**: Systematic traversal of link networks to index entire sites (spiders).
- **RSS Feeds**: Standardized XML syndication (using `feedparser`). Preferable for news/blogs as it provides a predictable schema and metadata (date, author, URL).
- **APIs**: The most structured way to ingest data (Twitter, Reddit, Search APIs), often yielding JSON with rich metadata.

## 2. Corpus Data Management
### Disk Structure
For large-scale corpora, organization on disk is critical for performance:
- **Hierarchical Storage**: Organizing documents by category/domain folders (e.g., `corpus/politics/doc1.txt`).
- **Metadata Sidecars**: Storing metadata in separate JSON/XML files alongside the raw text.

### Streaming & Memory Safety
Loading a multi-gigabyte corpus into memory is often impossible. 
- **Iterators & Generators**: Use Python's `yield` to process one document at a time.
- **Multiprocessing**: Distributing ingestion/preprocessing across multiple CPU cores to speed up "embarrassingly parallel" tasks.

## 3. Preprocessing & Wrangling
The transformation from raw HTML/JSON to model-ready features:
1. **Normalization**: Stripping HTML tags, handling encodings, and converting to lowercase.
2. **Readability**: Using metrics like the **Flesch-Kincaid Grade Level** or **Gunning Fog Index** to assess content complexity or filter out "junk" text.
3. **Segmentation**: Breaking discourse into paragraphs, and paragraphs into sentences.

## 4. The Model Selection Triple
Every NLP data product relies on the balance of three pillars:
- **Data**: The quality and domain-specificity of the corpus.
- **Features**: The vector representation (TF-IDF, Embeddings).
- **Algorithm**: The machine learning model (Naive Bayes, SVM, Transformer).

---

#foundations #wrangling #ingestion #corpus #scraping #rss
