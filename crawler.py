import requests                       # fetch web pages
from bs4 import BeautifulSoup         # parse html
from urllib.parse import urljoin, urlparse  # fix relative links

visited = set()                       # store seen urls

def crawl(url, base_domain):
    if url in visited:
        return                        # skip if already crawled

    print(f'[*] {url}')               # show current url
    visited.add(url)                 # mark as visited

    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
    except:
        return                        # skip on error

    # grab and follow links
    for tag in soup.find_all('a', href=True):
        link = urljoin(url, tag['href'])             # make full url
        if base_domain in link and link not in visited:
            crawl(link, base_domain)                 # crawl it

if __name__ == '__main__':
    start_url = input('Enter start URL: ').strip()
    domain = urlparse(start_url).netloc
    crawl(start_url, domain)
