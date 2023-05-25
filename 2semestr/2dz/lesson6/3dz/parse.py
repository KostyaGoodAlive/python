from bs4 import BeautifulSoup

with open('2semestr/2dz/lesson6/index.html',) as file:
    soup = BeautifulSoup(file, 'html.parser')



div = soup.find(id = '1')
div_2 = soup.find(id = '2')
print(div.text)
print(div_2.text)
