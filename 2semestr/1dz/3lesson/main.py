# from googletrans import Translator
import pandas as pd
# translator = Translator()
# data = pd.read_excel('2semestr/1dz/3lesson/Grades.xlsx')
# a =translator.translate(data, src = 'en', dest ='uk')
# print(a.text)
# print(a.text)




products = ['Water','Milk', 'Melon', 'Apples']
price = ['15','50','200','60']
data = pd.DataFrame(list(zip(products, price), columns = ['Products', 'Price']))
