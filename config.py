# config.py
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
TIMEOUT = 10
MAX_PAGES = 50
HEADERS = {"User-Agent": USER_AGENT}

# List of proxies (e.g., http://user:pass@host:port or http://host:port)
PROXIES = [
    "http://127.0.0.1:8080", # Replace with actual proxies
    "http://127.0.0.1:8081"
]
