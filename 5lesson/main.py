file = open('5lesson/text.txt', 'w+')

while True:
    a = input("Введи ім/'я або натистни q щоб закінчити операцію: ")
    file.write(a)
    print(a)
    if a == 'q':
       print('Ви завершили операцію')
       break
       
    

file.close()