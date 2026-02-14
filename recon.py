# recon.py
import cloudscraper
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import random
from config import HEADERS, TIMEOUT, MAX_PAGES, PROXIES

def same_domain(base, url):
    return urlparse(base).netloc == urlparse(url).netloc

async def fetch(session, url):
    proxy = random.choice(PROXIES) if PROXIES else None
    try:
        # Using cloudscraper for the initial request to bypass WAF challenges
        scraper = cloudscraper.create_scraper(browser={'browser': 'chrome', 'platform': 'windows', 'desktop': True})
        
        async with session.get(url, timeout=TIMEOUT, proxy=proxy) as r:
            return await r.text()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

async def crawl(start_url):
    visited = set()
    to_visit = [start_url]
    base_domain = urlparse(start_url).netloc

    # Using aiohttp with cloudscraper capabilities is tricky; 
    # for simplicity in crawling, we use direct aiohttp, 
    # but actual auditing requests should use cloudscraper.
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        while to_visit and len(visited) < MAX_PAGES:
            url = to_visit.pop(0)
            if url in visited:
                continue

            html = await fetch(session, url)
            visited.add(url)

            soup = BeautifulSoup(html, "html.parser")

            for tag in soup.find_all("a", href=True):
                link = urljoin(url, tag["href"])
                if same_domain(start_url, link) and link not in visited:
                    to_visit.append(link)

    return list(visited)
