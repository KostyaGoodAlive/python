import requests
from bs4 import BeautifulSoup
response = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(response.content , "html.parser")
for post in soup.find('.text'):
    print(post.text)



