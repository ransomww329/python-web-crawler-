# Python Web Crawler

lightweight python crawler built for recon and link mapping.  
It scans any target URL and digs out internal links for you to analyze, hijack, or mess with.  
can be extended with form parsing, XSS scanning, SSRF probes, whatever.

make requests, I am updating this tool weekly as long as this message stands

---

## Features

Recursively crawls internal links
Handles broken pages gracefully
Uses `requests` and `BeautifulSoup4`
easy to extend — add form sniffers, filters, etc.

---

## usage

```bash
git clone https://github.com/ransomww329/python-web-crawler-
cd python-web-crawler-
python3 -m venv venv && source venv/bin/activate && pip install requests beautifulsoup4
python3 crawler.py
