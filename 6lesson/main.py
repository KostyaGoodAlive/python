file = open('6lesson/text.txt', 'w')
file.write('Banana\n')
file.write('Orange\n')
file.close()


file= open('6lesson/text.txt')
a = open('6lesson/file.txt' , 'w')

while True:
    symbol = file.read(1)
    
    if len(symbol) == 0:
        print('The end of the title')
        break
    else:
        a.write(f'{symbol}\n')

file.close()        
a.close()