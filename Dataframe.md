# Pandas: Comprehensive DataFrame Guide

This document provides a complete technical guide to Pandas **DataFrames**, covering everything implemented and practiced in `dataframe.py`.

---

## 1. What is a DataFrame?

A **DataFrame** is a two-dimensional (2D), size-mutable tabular data structure with labeled axes (rows and columns).
* **Axis 0 (Rows):** Vertical axis represented by row index labels.
* **Axis 1 (Columns):** Horizontal axis represented by column header names.
* **Heterogeneous Data:** Different columns can hold different data types (`int64`, `float64`, `object`/string, `bool`, etc.).

---

## 2. DataFrame Creation Methods

### Method A: Creating from a Dictionary of Lists
When passing a dictionary, the dictionary **keys** become the column headers, and the list values become the column entries.

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Salary": [70000, 80000, 90000, 100000]
}

df = pd.DataFrame(data)
print(df)
```

#### Output:
```text
      Name  Age         City  Salary
0    Alice   25     New York   70000
1      Bob   30  Los Angeles   80000
2  Charlie   35      Chicago   90000
3    David   40      Houston  100000
```

---

### Method B: Creating from a 2D Nested List with Custom Column Names
You can pass raw row data as a nested list and explicitly provide column names using the `columns` parameter.

```python
data_list = [
    ['jhon', 25, 'New York', 70000],
    ['Bob', 30, 'Los Angeles', 80000],
    ['Charlie', 35, 'Chicago', 90000],
    ['David', 40, 'Houston', 100000]
]

columns = ['Name', 'Age', 'City', 'Salary']

df2 = pd.DataFrame(data_list, columns=columns)
print(df2)
```

#### Output:
```text
      Name  Age         City  Salary
0     jhon   25     New York   70000
1      Bob   30  Los Angeles   80000
2  Charlie   35      Chicago   90000
3    David   40      Houston  100000
```

---

## 3. Column Selection and Indexing

### A. Selecting a Single Column (Returns a Series)
Using single square brackets returns a 1-dimensional `pd.Series`:

```python
print(df2['Name'])
```

#### Output:
```text
0       jhon
1        Bob
2    Charlie
3      David
Name: Name, dtype: object
```

### B. Selecting Multiple Columns (Returns a DataFrame)
To extract multiple columns, pass a Python list of column names inside double brackets `[[ ... ]]`:

```python
print(df2[['Name', 'Age']])
```

#### Output:
```text
      Name  Age
0     jhon   25
1      Bob   30
2  Charlie   35
3    David   40
```

> **Important Rule:**
> * `df['Column']` -> Returns a **1D Series**.
> * `df[['Column']]` or `df[['Col1', 'Col2']]` -> Returns a **2D DataFrame**.

---

## 4. Column Manipulation: Adding and Dropping Columns

### A. Creating a New Column
You can assign a list or array directly to a new column name. The list length must equal the number of rows in the DataFrame:

```python
df2["Desgnation"] = ["Engineer", "Manager", "Analyst", "Director"]
print(df2)
```

#### Output:
```text
      Name  Age         City  Salary Desgnation
0     jhon   25     New York   70000   Engineer
1      Bob   30  Los Angeles   80000    Manager
2  Charlie   35      Chicago   90000    Analyst
3    David   40      Houston  100000   Director
```

### B. Dropping a Column with `.drop()`
To delete a column, use the `.drop()` method:

```python
df2.drop("Desgnation", axis=1, inplace=True)
print(df2)
```

#### Key Parameters Explained:
* **`axis=1` vs `axis=0`:**
  * `axis=1` (or `axis='columns'`): Refers to the horizontal axis (drops columns).
  * `axis=0` (or `axis='index'`): Refers to the vertical axis (drops rows). Default is `axis=0`.
* **`inplace=True` vs `inplace=False`:**
  * `inplace=False` (default): Does not change the original DataFrame. It creates and returns a new copy without the dropped column.
  * `inplace=True`: Directly mutates the existing DataFrame in memory and returns `None`.

---

## 5. Row Selection Using `.loc[]`

The `.loc[]` accessor is label-based, used to select rows and columns by index labels or boolean masks.

### A. Selecting a Single Row (Returns a Series)
```python
print(df2.loc[0])
```

#### Output:
```text
Name          jhon
Age             25
City      New York
Salary       70000
Name: 0, dtype: object
```
* Notice that selecting a single row returns a **Series**, where column names become the index of the Series.

### B. Selecting Multiple Rows (Returns a DataFrame)
Pass a list of row labels to retrieve multiple rows:

```python
print(df2.loc[[0, 1]])
```

#### Output:
```text
   Name  Age         City  Salary
0  jhon   25     New York   70000
1   Bob   30  Los Angeles   80000
```

---

## 6. Adding New Rows to a DataFrame

There are two primary ways to add new rows:

### Method 1: Using `.loc[]` with an Index Identifier
```python
# Inserting row at explicit index 4
df2.loc[4] = ['Emma', 28, 'Boston', 85000]

# Auto-indexing: using len(df2) to append to the end
df2.loc[len(df2)] = ['Frank', 32, 'Seattle', 95000]
```

### Method 2: Modern Concatenation (`pd.concat`)
*(Note: `df.append()` was deprecated and removed in recent Pandas releases. Use `pd.concat()` instead).*

```python
new_row = pd.DataFrame([{
    'Name': 'Grace',
    'Age': 29,
    'City': 'Miami',
    'Salary': 88000
}])

df2 = pd.concat([df2, new_row], ignore_index=True)
```

---

## 7. Selecting Subsets of Rows and Columns

You can slice both rows and columns simultaneously.

### Approach A: Chained Indexing
```python
print(df2.loc[[0, 1]][["City", "Salary"]])
```

### Approach B: Standard 2D `.loc[rows, columns]` Syntax (Preferred)
In professional code, passing both row and column targets in a single `.loc[]` call is cleaner and avoids chained assignment warnings:

```python
print(df2.loc[[0, 1], ["City", "Salary"]])
```

#### Output:
```text
          City  Salary
0     New York   70000
1  Los Angeles   80000
```

---

## 8. Conditional Selection & Filtering (Boolean Masking)

Conditional selection allows you to filter rows based on logical conditions applied to column values.

### How Boolean Masking Works Internally
When you evaluate an expression like `df2["Age"] > 30`, Pandas generates a Boolean Series:
```text
0    False
1    False
2     True
3     True
Name: Age, dtype: bool
```
Passing this Boolean Series back into `df2[...]` extracts only the rows where the condition evaluated to `True`.

---

### Case 1: Single Condition
**Problem:** Select all rows where `Age` is greater than 30.

```python
print(df2[df2["Age"] > 30])
```

#### Output:
```text
      Name  Age     City  Salary
2  Charlie   35  Chicago   90000
3    David   40  Houston  100000
```

---

### Case 2: Compound Conditions (Bitwise Logical Operators)
**Problem:** Select rows where `Age` is greater than 30 **AND** `City` is Chicago.

```python
print(df2[(df2["Age"] > 30) & (df2["City"] == "Chicago")])
```

#### Output:
```text
      Name  Age     City  Salary
2  Charlie   35  Chicago   90000
```

#### Critical Rules for Compound Conditions in Pandas:
1. **Always wrap each condition in parentheses `(...)`:**
   In Python, bitwise operators (`&`, `|`, `~`) have higher operator precedence than comparison operators (`>`, `<`, `==`). Writing `df2["Age"] > 30 & df2["City"] == "Chicago"` causes a syntax/evaluation error. Parentheses ensure conditions evaluate before the logical operator.
2. **Use bitwise operators instead of Python keywords:**
   * Use `&` instead of `and`
   * Use `|` instead of `or`
   * Use `~` instead of `not`
   *(Python keywords evaluate truthiness on the whole container, whereas bitwise operators perform element-wise logical operations across the Series).*

---

## 9. Quick Syntax Summary

| Operation | Syntax Example | Return Type |
| :--- | :--- | :--- |
| Create DataFrame | `pd.DataFrame(data)` | DataFrame |
| Select Single Column | `df['Name']` | Series (1D) |
| Select Multiple Columns | `df[['Name', 'Age']]` | DataFrame (2D) |
| Add New Column | `df['New_Col'] = values_list` | In-place update |
| Drop Column | `df.drop('Col', axis=1, inplace=True)` | Modifies original |
| Select Single Row | `df.loc[0]` | Series (1D) |
| Select Multiple Rows | `df.loc[[0, 1]]` | DataFrame (2D) |
| Add New Row | `df.loc[len(df)] = [val1, val2, ...]` | In-place insert |
| Slice Rows and Columns | `df.loc[[0, 1], ['City', 'Salary']]` | DataFrame |
| Single Condition Filter | `df[df['Age'] > 30]` | DataFrame |
| Multiple Conditions Filter | `df[(df['Age'] > 30) & (df['City'] == 'Chicago')]` | DataFrame |
