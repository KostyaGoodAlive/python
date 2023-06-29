import requests
from bs4 import BeautifulSoup


response = requests.get('http://yermilovcentre.org/medias/')

soup = BeautifulSoup(response.content, 'html.parser')

for title in soup.select_one('.row title-text'):
    print(title.text)