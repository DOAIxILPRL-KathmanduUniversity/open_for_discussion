"""
🚀 PRO-SCRAPER ENGINE (LOCAL-FIRST VERSION)
------------------------------------------
A high-performance, asynchronous web crawler for low-resource languages.
Optimized for resilience, politeness, and multi-modal data collection.

Dependencies: pip install httpx aiosqlite beautifulsoup4 yarl
"""

import asyncio
import aiosqlite
import httpx
from bs4 import BeautifulSoup
from yarl import URL
import os
import hashlib
import time

# --- CONFIGURATION ---
BASE_DIR = 'crawler_data'
LOCAL_DB = os.path.join(BASE_DIR, 'crawler.db')
DATA_DIRS = {
    'pdf': os.path.join(BASE_DIR, 'downloads/PDF'),
    'image': os.path.join(BASE_DIR, 'downloads/IMG')
}

# Ensure directories exist
for path in DATA_DIRS.values():
    os.makedirs(path, exist_ok=True)

TARGET_SEEDS = [
    "https://moald.gov.np",
    "https://pmamp.gov.np"
]
ALLOWED_DOMAINS = ('.gov.np', '.edu.np', '.org.np')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (ProScraper/1.0; Research Crawler)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

class ProScraper:
    def __init__(self):
        self.db = None
        self.client = httpx.AsyncClient(
            headers=HEADERS, verify=False, timeout=30.0,
            follow_redirects=True, limits=httpx.Limits(max_connections=50)
        )
        self.html_queue = asyncio.Queue()
        self.media_queue = asyncio.Queue()
        self.visited = set()
        self.downloaded = set()
        self.retry_counts = {}
        self.domain_locks = {}
        self.active_tasks = 0

    async def setup(self):
        log("⚙️ Initializing database...")
        self.db = await aiosqlite.connect(LOCAL_DB)
        await self.db.execute("PRAGMA journal_mode=WAL")
        await self.db.executescript("""
            CREATE TABLE IF NOT EXISTS visited (url TEXT PRIMARY KEY);
            CREATE TABLE IF NOT EXISTS frontier (url TEXT PRIMARY KEY);
            CREATE TABLE IF NOT EXISTS dead_letter (url TEXT PRIMARY KEY, reason TEXT);
            CREATE TABLE IF NOT EXISTS downloads (url TEXT PRIMARY KEY, path TEXT);
        """)
        await self.db.commit()

        # Load state
        async with self.db.execute("SELECT url FROM visited UNION SELECT url FROM dead_letter") as cur:
            async for row in cur: self.visited.add(row[0])
        async with self.db.execute("SELECT url FROM downloads") as cur:
            async for row in cur: self.downloaded.add(row[0])

        # Inject seeds if empty
        async with self.db.execute("SELECT COUNT(*) FROM frontier") as cur:
            count = (await cur.fetchone())[0]
            if count == 0:
                log("🌱 Injecting seeds...")
                for seed in TARGET_SEEDS:
                    if seed not in self.visited:
                        await self.html_queue.put(seed)
                        await self.db.execute("INSERT OR IGNORE INTO frontier VALUES (?)", (seed,))
                await self.db.commit()

    def _get_lock(self, domain):
        if domain not in self.domain_locks:
            self.domain_locks[domain] = asyncio.Semaphore(2)
        return self.domain_locks[domain]

    async def handle_failure(self, url, worker_id, reason):
        if "Hard Fail" in reason or ("?" in url and "Soft Fail" in reason):
            log(f"[W{worker_id}] 🚫 BAN | {url} ({reason})")
            self.visited.add(url)
            await self.db.execute("DELETE FROM frontier WHERE url = ?", (url,))
            await self.db.execute("INSERT OR REPLACE INTO dead_letter VALUES (?, ?)", (url, reason))
            await self.db.commit()
            return

        attempts = self.retry_counts.get(url, 0) + 1
        self.retry_counts[url] = attempts
        if attempts < 3:
            await self.html_queue.put(url)
        else:
            log(f"[W{worker_id}] ❌ STRIKE 3 | {url}")
            self.visited.add(url)
            await self.db.execute("DELETE FROM frontier WHERE url = ?", (url,))
            await self.db.execute("INSERT OR REPLACE INTO dead_letter VALUES (?, ?)", (url, "Retry Limit"))
            await self.db.commit()

    async def html_worker(self, worker_id):
        while True:
            url = await self.html_queue.get()
            self.active_tasks += 1
            domain = URL(url).host
            if not domain:
                self.html_queue.task_done()
                self.active_tasks -= 1
                continue

            async with self._get_lock(domain):
                try:
                    resp = await self.client.get(url)
                    if resp.status_code == 200:
                        soup = BeautifulSoup(resp.text, 'html.parser')
                        new_links = 0
                        for tag in soup.find_all(['a', 'img']):
                            raw = tag.get('href') if tag.name == 'a' else tag.get('src')
                            if not raw or raw.startswith(('mailto:', 'javascript:', 'tel:', '#')): continue
                            
                            try:
                                full_url = str(URL(url).join(URL(raw)).with_fragment(None))
                                target_domain = URL(full_url).host
                                if target_domain and any(target_domain.endswith(ext) for ext in ALLOWED_DOMAINS):
                                    if full_url.lower().endswith(('.pdf', '.jpg', '.jpeg', '.png', '.webp')):
                                        if full_url not in self.downloaded:
                                            self.downloaded.add(full_url)
                                            await self.media_queue.put(full_url)
                                    elif full_url not in self.visited:
                                        self.visited.add(full_url)
                                        await self.html_queue.put(full_url)
                                        await self.db.execute("INSERT OR IGNORE INTO frontier VALUES (?)", (full_url,))
                                        new_links += 1
                            except Exception: pass
                        
                        await self.db.execute("DELETE FROM frontier WHERE url = ?", (url,))
                        await self.db.execute("INSERT OR IGNORE INTO visited VALUES (?)", (url,))
                        await self.db.commit()
                        log(f"[W{worker_id}] ✅ OK: {url} (+{new_links})")
                    else:
                        await self.handle_failure(url, worker_id, f"Status {resp.status_code}")
                except Exception as e:
                    await self.handle_failure(url, worker_id, type(e).__name__)
                finally:
                    self.active_tasks -= 1
                    self.html_queue.task_done()

    async def media_worker(self, worker_id):
        while True:
            url = await self.media_queue.get()
            self.active_tasks += 1
            try:
                ext = url.split('.')[-1].lower()
                folder = 'pdf' if ext == 'pdf' else 'image'
                domain = URL(url).host
                dest_dir = os.path.join(DATA_DIRS[folder], domain.replace('.', '_'))
                os.makedirs(dest_dir, exist_ok=True)

                raw_name = url.split('/')[-1].split('?')[0]
                clean = "".join([c for c in raw_name if c.isalnum() or c in (".", "_", "-")])
                if not clean or len(clean) > 80:
                    clean = hashlib.md5(url.encode()).hexdigest()[:12] + f".{ext}"
                
                path = os.path.join(dest_dir, clean)
                if not os.path.exists(path):
                    async with self.client.stream("GET", url) as r:
                        if r.status_code == 200:
                            with open(path, 'wb') as f:
                                async for chunk in r.aiter_bytes(): f.write(chunk)
                            
                            if folder == 'image' and os.path.getsize(path) < 5048:
                                os.remove(path)
                                continue
                                
                            await self.db.execute("INSERT OR IGNORE INTO downloads VALUES (?, ?)", (url, path))
                            await self.db.commit()
                            log(f"[DL{worker_id}] 💾 Saved: {clean}")
            except Exception: pass
            finally:
                self.active_tasks -= 1
                self.media_queue.task_done()

async def main():
    scraper = ProScraper()
    await scraper.setup()
    tasks = []
    for i in range(10): tasks.append(asyncio.create_task(scraper.html_worker(i)))
    for i in range(5): tasks.append(asyncio.create_task(scraper.media_worker(i)))
    
    try:
        while True:
            await asyncio.sleep(10)
            if scraper.html_queue.qsize() == 0 and scraper.media_queue.qsize() == 0 and scraper.active_tasks == 0:
                break
    finally:
        for t in tasks: t.cancel()
        await scraper.db.close()
        await scraper.client.aclose()

if __name__ == "__main__":
    asyncio.run(main())
