file = open('5lesson/text.txt', 'w+')

while True:
    a = input("Введи ім/'я або натистни q щоб закінчити операцію: ")
    if a == 'q':
       print('Ви завершили операцію')
       break
    file.write(a)
    print(a)
   
       
    

file.close()