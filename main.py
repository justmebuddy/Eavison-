# main.py
import asyncio
import cloudscraper
from recon import crawl
from risk import score_url
from audit import analyze_response
from db import save_scan, save_finding, cur

# Expanded Payloads
PAYLOADS = [
    "' OR 1=1--",
    "\" OR \"1\"=\"1",
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>"
]

def run_scan(target):
    print("Crawling target...")
    # recon.py handles crawling
    urls = asyncio.run(crawl(target))
    print("Total discovered URLs:", len(urls))

    scraper = cloudscraper.create_scraper()

    for url in urls:
        print("\nScanning:", url)
        risk = score_url(url)
        save_scan(url, risk)

        try:
            # Active payload testing using cloudscraper
            response = scraper.get(url, timeout=5)
            findings = analyze_response(url, response.text, response.headers)

            if findings:
                for f in findings:
                    save_finding(url, f)
                    print("Finding:", f)

            for payload in PAYLOADS:
                try:
                    # Basic parameter manipulation for testing
                    test_url = url + ("&" if "?" in url else "?") + "test=" + payload
                    test_response = scraper.get(test_url, timeout=5)
                    extra_findings = analyze_response(test_url, test_response.text, test_response.headers)

                    for f in extra_findings:
                        save_finding(test_url, f)
                        print("Payload Finding:", f)
                except:
                    pass
        except:
            print("Request failed:", url)

    print("\n=== SCAN COMPLETED ===")

if __name__ == "__main__":
    target = input("Enter target URL: ").strip()
    run_scan(target)
