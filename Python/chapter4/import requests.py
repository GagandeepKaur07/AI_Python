import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com'
response = requests.get(url)

if response.status_code ==200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            print(href)
else:
    print("Failled to retrive the webpage.")