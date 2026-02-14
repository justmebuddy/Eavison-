from urllib.parse import urljoin, urlparse

def normalize_url(base, link):
    return urljoin(base, link)

def is_valid_url(url):
    p = urlparse(url)
    return p.scheme in ("http", "https") and p.netloc != ""