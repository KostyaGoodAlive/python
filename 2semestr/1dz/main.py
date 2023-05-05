file = open('D:/VS/2semestr/1dz/recept.csv', 'r')
result=[]
for line in file:
    arr = line.split(',')
    result.append(arr)

a = int(result[1][1])
b = int(result[1][3])
c = int(result[2][1])
d = int(result[2][3])
print(f"{result[0][0]} , {result[0][3]}\n{result[1][0]} - {result[1][3]}\n{result[2][0]} - {result[2][3]} ")
print(f"total weight - {a + c} gram")
print(f"cost of all products - {b + d} UAH")

file.close()