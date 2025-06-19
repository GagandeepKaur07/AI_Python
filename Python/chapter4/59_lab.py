import requests
from bs4 import BeautifulSoup
url='https://aimicrodegree.org/category-details/10/'
response=requests.get(url)
if response.status_code==200:
    print("Successfully fetched the web page! ")
else:
    print(f"Failed to fetch the web page. Status code :{response.status_code}")

soup = BeautifulSoup(response.text, 'lxml')
#extract the  title from the page
title = soup.title.string
print(f"page Title :{ title}")

# extract all hyperlinks
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    text=link.get_text()
    print(f"Link text: {text}, URL : {href}")

paragraphs= soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.get_text())