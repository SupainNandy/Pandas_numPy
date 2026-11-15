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

columns = ['Name', 'Age', 'City', 'Salary']

df2=pd.DataFrame(data_list,columns=columns)


#-----------------------------------------------------------------------------
print(df2)

#Selecting and indexing data of columns

print(df2['Name'] ) # Selecting a single column

#output:
#0      jhon
#1       Bob
#2    Charlie
#3     David

print(df2[['Name', 'Age']]) # Selecting multiple columns
#output:
#      Name  Age
#0     jhon   25
#1      Bob   30
#2  Charlie   35
#3    David   40

#------------------------------------------------------------------------
#Create new column in DataFrame

df2["Desgnation"] = ["Engineer", "Manager", "Analyst", "Director"]

print(df2)

#Removing a column from DataFrame
df2.drop("Desgnation", axis=1,inplace=True)
#axsis=1 means we are dropping a column,
#axis=0 means we are dropping a row
#inplace=True means we are modifying the original DataFrame, if inplace=False then it will return a new DataFrame without modifying the original one.
print(df2)

#------------------------------------------------------------------------
#Selecting rows from DataFrame
print(df2.loc[0])# Selecting a single row by index.
# loc-> location based indexing, it is used to select rows and columns by labels or boolean array.
#Name          jhon
# Age             25
# City      New York
# Salary       70000
# Name: 0, dtype: object

print(df2.loc[[0, 1]]) # Selecting multiple rows by index.
#output:
#    Name  Age         City  Salary
#0   jhon   25     New York   70000
#1    Bob   30  Los Angeles   80000



#------------------------------------------------------------------------
#Selecting subset of rows and columns from DataFrame
print(df2.loc[[0,1]][["City","Salary"]])# Selecting subset of rows and columns by index and column labels.



#------------------------------------------------------------------------
#Conditional selection  DataFrame

#Q1-> Select all rows where Age is greater than 30
print("Select all rows where Age is greater than 30")
print(df2[df2["Age"]>30])
#output:
#      Name  Age     City  Salary
#2  Charlie   35  Chicago   90000
#3    David   40  Houston  100000
 

# Q2-> Select the row where age is 30 above and city is New York
print("Select the row where age is 30 above and city is New York")
print(df2[(df2["Age"]>30)&(df2["City"]=="Chicago")])
