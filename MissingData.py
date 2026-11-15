import numpy as np
import pandas as pd

data = {
    "A":[1, 2, 3, 4],
    "B":[5, np.nan, 7, 8],
    "C":[9, 10, np.nan, np.nan],
    "D":[np.nan, 12, 13, 14]
}

df = pd.DataFrame(data)

# print(df.loc[1] )

print(df.isna().sum())
print(df.isnull().any())


#Removing rows with missing values
# remove use only rows 
df2 = df.dropna()
print(df2)

df3=df.dropna(thresh=3)
print(df3)

#Filling missing values
# df4= df.fillna(0,inplace=True)
# print(df)


df.fillna(df.mean(), inplace=True)
print(df)

