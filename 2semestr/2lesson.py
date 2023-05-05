file = open('D:/VS/2semestr/grades.csv', 'r')
result=[]
for line in file:
    arr = line.split(',')
    result.append(arr)

a = result[6]  
sum_grades = sum(map(int, result[6][1:]))
print(sum_grades)
# list_grates = a[1:]
# b = [int(i) for i in list_grates]
# print(sum(b))
file.close()


