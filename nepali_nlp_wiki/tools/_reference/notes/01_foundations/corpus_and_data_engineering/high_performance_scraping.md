# Guide: High-Performance Asynchronous Web Scraping

> [!IMPORTANT] Gist
> Scaling from a simple script to a production-grade crawler requires three pillars: **Concurrency** (Async), **Persistence** (State recovery), and **Politeness** (Rate limiting).

## 1. The Architecture of a "Pro" Scraper

Traditional sequential scraping is too slow for 100k+ documents. A professional engine uses the **Worker-Queue Pattern**:

1.  **Stateful Frontier**: Use a database (SQLite) to track URLs: `Visited`, `Queue (Frontier)`, and `Dead Letter` (failed).
2.  **Asynchronous Workers**: Multiple workers pull from the queue simultaneously using `asyncio` and `httpx`.
3.  **Media Pipelines**: Separate queues for HTML parsing and binary (PDF/Image) downloads to prevent bottlenecks.
4.  **Resilience**: Periodic checkpoints (e.g., syncing to Google Drive) to ensure progress isn't lost during crashes or environment timeouts.

## 2. Implementation: The "GovScraper" Engine

This engine is optimized for high-density data collection from `.gov.np` and `.edu.np` domains.

### Masterclass Example (Python)

```python
import asyncio
import aiosqlite
import httpx
from bs4 import BeautifulSoup
from yarl import URL
import hashlib
import os

class ProScraper:
    def __init__(self, seeds, allowed_domains):
        self.seeds = seeds
        self.allowed_domains = allowed_domains
        self.client = httpx.AsyncClient(verify=False, timeout=30.0, follow_redirects=True)
        self.html_queue = asyncio.Queue()
        self.media_queue = asyncio.Queue()
        self.visited = set()

    async def setup_db(self):
        """Persistent state management survives execution crashes."""
        self.db = await aiosqlite.connect('crawler.db')
        await self.db.executescript("""
            CREATE TABLE IF NOT EXISTS visited (url TEXT PRIMARY KEY);
            CREATE TABLE IF NOT EXISTS frontier (url TEXT PRIMARY KEY);
        """)
        # Load existing state into memory
        async with self.db.execute("SELECT url FROM visited") as cur:
            async for row in cur: self.visited.add(row[0])

    async def html_worker(self, worker_id):
        """Parses HTML and discovers new links."""
        while True:
            url = await self.html_queue.get()
            try:
                resp = await self.client.get(url)
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.text, 'html.parser')
                    for tag in soup.find_all(['a', 'img']):
                        raw = tag.get('href') or tag.get('src')
                        # Logic to resolve absolute URLs and filter domains
                        # ... (See Implementation Details below)
            finally:
                self.html_queue.task_done()
```

## 3. Key Pro-Features Explained

### A. Instant Banning & Retry Logic
Avoid wasting cycles on broken links. If a URL returns a **Hard Fail** (404, 403) or is a parameterized search URL (`?search=...`) that soft-fails, ban it instantly by moving it to a `dead_letter` table.

### B. Media Filtering (Size-based)
To maintain a high-quality corpus, filter out "noise" images (icons, spacers).
```python
# Check file size before committing to database
file_size = os.path.getsize(path)
if file_size < 5048:  # Skip anything under 5 KB
    os.remove(path)
    continue 
```

### C. Domain Locking (Politeness)
Never overwhelm a single server. Use a `Semaphore` keyed to the domain name to limit concurrent connections per site.
```python
def _get_lock(self, domain):
    if domain not in self.domain_locks:
        self.domain_locks[domain] = asyncio.Semaphore(2) # Max 2 concurrent hits
    return self.domain_locks[domain]
```

## 4. Maintenance & Cleanup
- **Deduplication**: Use `hashlib` to create unique filenames based on the URL to prevent duplicate downloads.
- **Progress Sync**: For long-running crawls, implement a background `sync_loop` to back up the local SQLite DB to external storage periodically.

## 5. Ethical Guidelines
- **Identify Yourself**: Use a descriptive `User-Agent`.
- **Respect Robots.txt**: Always check if crawling is permitted on specific paths.
- **Frequency**: Keep your `Semaphore` low to avoid triggering DDoS protections.

---

**Notebook**: [pro_scraper_engine.py](notebooks/pro_scraper_engine.py) (Local-first implementation)

#scraping #data-engineering #async #python #httpx #crawler
