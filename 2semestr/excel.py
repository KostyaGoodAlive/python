# import pandas as pd
# data = pd.read_excel('Grades.xlsx', sheet_name=['Student2', 'Student1'])
# print(data)
import pandas as pd
data = pd.read_excel('Grades.xlsx', usecols=['Subject', 'Grade'])
print(data)