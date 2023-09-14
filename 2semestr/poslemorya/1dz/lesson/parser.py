
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.get('https://comfy.ua/ua/smartfon/brand__apple/', headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")

devices = soup.select('.products-list-item')


for device in devices:
    item = {
        "name": device.select_one('.products-list-item__name').text,
        "code": device.select_one('.products-list-item__code').text.strip().replace('Код: ', ''),
        "old_price": int(device.select_one('.products-list-item__actions-price-old').text[:20].replace('₴', '').replace('\n', '').replace(' ', '').strip()),
        "current_price": int(device.select_one('.products-list-item__actions-price-current').text[:20].replace('₴', '').replace('\n', '').replace(' ', '').strip()),
        "reviews": int(device.select_one('.products-list-item__reviews').text)
    }
    print(item)