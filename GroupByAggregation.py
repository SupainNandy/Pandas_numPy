import numpy as np
import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Store':["S1", "S1", "S2", "S2", "S1", "S2"],
    'Sales': [100, 200, 150, 300, 250, 400],
    'Quantity': [10, 20, 15, 30, 25, 40],
    'Date': pd.date_range('2023-01-01', periods=6)
}


df = pd.DataFrame(data)
print(df)

#Group by category and calculate sum of Sales and Quantity
d1= df.groupby('Category')[['Sales', 'Quantity']].sum()
print(d1) 

#Group by Strore and calculate mean of Sales and Quantity
d2 = df.groupby('Store')[['Sales',"Quantity"]].sum()
print(d2)

#Group by multiple columns and calculate sum of Sales and Quantity
d3 = df.groupby(['Category', 'Store'])[['Sales', 'Quantity']].sum()
print(d3)


#-------------------------------------------------------------

#Aggregation 

print(df["Sales"].mean())


print(df["Sales"].median())

print(df["Sales"].max())

print(df["Sales"].min())


print(df["Sales"].std())



print(df['Sales'].agg(['mean', 'median', 'max', 'min', 'std']))