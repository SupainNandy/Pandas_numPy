import numpy as np
import pandas as pd

#Merging 2 DataFrames
employees = pd.DataFrame({
    "employee_id": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "department": ["HR", "IT", "Finance", "Marketing"]
})

salaries = pd.DataFrame({
    "employee_id": [1, 2, 5, 6],
    "Salary": [70000, 80000, 90000, 100000],
    "bonus": [5000, 6000, 7000, 8000]
})



df=pd.merge(employees,salaries, on='employee_id')
print(df)


df2=pd.merge(employees,salaries, on='employee_id',how='outer')
print(df2)


df3=pd.merge(employees,salaries, on='employee_id',how='left')
print(df3)



data1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"]
})

data2 = pd.DataFrame({
    "A": ["A4", "A5", "A6", "A7"],
    "B": ["B4", "B5", "B6", "B7"],
    "C": ["C4", "C5", "C6", "C7"],
    "D": ["D4", "D5", "D6", "D7"]
})

#row wise concatenation
df5=pd.concat([data1,data2])
print(df5)

#column wise concatenation
df6=pd.concat([data1,data2],axis=1)
print(df6)


#join of 2 DataFrames
data3 = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K3"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"]
})

data4 = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"]
})

print(data3.join(data4.set_index('key'), on='key'))


