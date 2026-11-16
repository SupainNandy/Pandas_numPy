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
print(df)