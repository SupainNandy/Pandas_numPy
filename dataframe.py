import numpy as np
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Salary": [70000, 80000, 90000, 100000]
}

#Create DataFrame 
print(pd.DataFrame(data))

#we can also create DataFrame from list of dictionaries
data_list = [
    ['jhon', 25, 'New York', 70000],
    ['Bob', 30, 'Los Angeles', 80000],
    ['Charlie', 35, 'Chicago', 90000],
    ['David', 40, 'Houston', 100000]
]

df2=pd.DataFrame(data_list)

print(df2)
