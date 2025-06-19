import requests
from bs4 import BeautifulSoup

# url = input("enter here URl: ") # take user input
url = 'https://web.whatsapp.com'
response = requests.get(url)
# print("Respone:",response.content)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)