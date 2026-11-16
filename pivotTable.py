import numpy as np
import pandas as pd


data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['North', 'South', 'East', 'West'] * 5,
    'Sales': np.random.randint(100, 1000, size=20),
    'Units': np.random.randint(1, 20, size=20),
    'Rep': ['John', 'Alice', 'Bob', 'Eve'] * 5
}

df = pd.DataFrame(data)
print("DataFrame: ")
print(df)
print("Pivot Table: ")
print(df.pivot_table(values='Sales', index='Region', columns='Product', aggfunc='sum', fill_value=0)) #bydefault aggfunc is mean, fill_value is NaN
#output:
# Product     A     B     C     D
# Region                         
# East        0     0  1871     0
# North    2879     0     0     0
# South       0  2651     0     0
# West        0     0     0  2223

print("Pivot Table with multiple aggregation functions: ")
print(df.pivot_table(values=['Sales', 'Units'], index='Region', columns='Product', aggfunc=['sum', 'mean'], fill_value=0))


#Cross Tabulation

print("Cross Tabulation: ")
print(pd.crosstab(df['Region'], df['Product'], values=df['Sales'], aggfunc='sum', margins=True, margins_name='Total'))
#Pivot table and crosstab are similar, but pivot table is more flexible and can handle multiple aggregation functions, while crosstab is more limited and is mainly used for frequency counts.
