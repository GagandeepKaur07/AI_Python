import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

def fetch_page(url):
    try:
        response= requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error feching {url} : {e}")
        return None
def extract_links(html,base_url):
    soup = BeautifulSoup(html, 'lxml')
    links=[]
    for link in soup.find_all('a',href=True):
        full_url = urljoin(base_url, link['href'])
        links.append(full_url)
    return links
# the main crawing function
def crawl(start_url, max_depth=2):
    visited= set()
    to_visit=[(start_url,0)]

    while to_visit:
        current_url, depth = to_visit.pop(0)

        if depth > max_depth:
            continue
        if current_url in visited:
            continue
        print(f"Crawling : {current_url}")
        visited.add(current_url)

        html = fetch_page(current_url)
        if html is None:
            continue

        links = extract_links(html, current_url)
        for link in links:
            if link not in visited:
                to_visit.append((link, depth+1))

            time.sleep(1)

start_url = "https://edunetfoundation.org/"
crawl(start_url, max_depth=2)

