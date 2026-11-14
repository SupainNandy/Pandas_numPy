# Pandas: Series vs. DataFrame (Definitions, Differences & Examples)

This document provides a comprehensive technical comparison between the two core data structures in the Pandas library: **Series** and **DataFrame**.

---

## 1. Definitions

### What is a Pandas Series?
A **Series** is a one-dimensional (1D) labeled array capable of holding any data type (integers, strings, floating-point numbers, Python objects, etc.).
* It has only **one axis**: the **index** (row labels).
* Every element in a Series shares the same underlying data type (`dtype`).
* Think of a Series as a **single column** in a spreadsheet or a SQL table.

### What is a Pandas DataFrame?
A **DataFrame** is a two-dimensional (2D), size-mutable, tabular data structure with labeled axes (rows and columns).
* It has **two axes**:
  * **Axis 0:** Rows (identified by row index labels).
  * **Axis 1:** Columns (identified by column header labels).
* Each column in a DataFrame can hold a different data type (**heterogeneous**): one column can contain strings, another integers, and another floats.
* Think of a DataFrame as a **complete spreadsheet table** or a SQL table.

### The Fundamental Relationship
The core architectural connection between the two structures is:
> **A DataFrame is essentially an aligned collection of Series objects sharing a common index.**
When you extract a single column from a DataFrame, it returns a `Series`. Conversely, when you align multiple `Series` along a shared index, they form a `DataFrame`.

---

## 2. Visual Representation

```
      PANDAS SERIES (1D)                       PANDAS DATAFRAME (2D)
      
         Index    Data                          Index     Col 0       Col 1       Col 2
        +-----+  +----+                        +-----+  +---------+ +-------+ +----------+
        |  0  |  | 25 |                        |  0  |  |  Alice  | |   25  | | New York |
        |  1  |  | 30 |                        |  1  |  |   Bob   | |   30  | |    LA    |
        |  2  |  | 35 |                        |  2  |  | Charlie | |   35  | | Chicago  |
        +-----+  +----+                        +-----+  +---------+ +-------+ +----------+
        dtype: int64                                       Series 1    Series 2   Series 3
                                                        (object)     (int64)    (object)
```

---

## 3. Key Differences: Series vs. DataFrame

| Feature | Pandas Series | Pandas DataFrame |
| :--- | :--- | :--- |
| **Dimensionality** | 1-Dimensional (1D) | 2-Dimensional (2D) |
| **Visual Structure** | Single column with an index | Tabular grid of rows and columns |
| **Axes** | 1 axis: `index` (Axis 0) | 2 axes: `index` (Axis 0) and `columns` (Axis 1) |
| **Data Homogeneity** | Homogeneous (single data type per Series) | Heterogeneous (columns can hold different data types) |
| **Attribute `.shape`** | Returns tuple with 1 element: `(n,)` | Returns tuple with 2 elements: `(rows, cols)` |
| **Attribute `.ndim`** | Always `1` | Always `2` |
| **Size Mutability** | Size is immutable (cannot add elements in-place without returning a new object) | Size is mutable (columns and rows can be inserted or deleted dynamically) |
| **Extraction Result** | Extracting a single element returns a scalar | Extracting a single column returns a `Series` |

---

## 4. Practical Code Examples

### Example 1: Creating a Series (1D)

```python
import pandas as pd

# Creating a Series representing Age
ages = pd.Series([25, 30, 35, 40], name="Age")

print(ages)
print("Type:", type(ages))
print("Shape:", ages.shape)
print("Dimensions:", ages.ndim)
```

#### Output:
```text
0    25
1    30
2    35
3    40
Name: Age, dtype: int64
Type: <class 'pandas.core.series.Series'>
Shape: (4,)
Dimensions: 1
```

---

### Example 2: Creating a DataFrame (2D)

Using the dataset from `dataframe.py`:

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
print("Type:", type(df))
print("Shape:", df.shape)
print("Dimensions:", df.ndim)
```

#### Output:
```text
      Name  Age         City  Salary
0    Alice   25     New York   70000
1      Bob   30  Los Angeles   80000
2  Charlie   35      Chicago   90000
3    David   40      Houston  100000

Type: <class 'pandas.core.frame.DataFrame'>
Shape: (4, 4)
Dimensions: 2
```

---

### Example 3: Extracting a Column from DataFrame (Proving it is a Series)

When you select a single column from a DataFrame, Pandas returns that column as a `Series`:

```python
age_column = df["Age"]

print(age_column)
print("Data type of extracted column:", type(age_column))
```

#### Output:
```text
0    25
1    30
2    35
3    40
Name: Age, dtype: int64
Data type of extracted column: <class 'pandas.core.series.Series'>
```

> **Important Syntax Note:**
> * `df["Age"]` (single brackets) returns a **Series** (`1D`).
> * `df[["Age"]]` (double brackets) returns a **DataFrame** with a single column (`2D`).

---

### Example 4: Constructing a DataFrame from Multiple Individual Series

Since a DataFrame is a collection of Series, you can combine separate Series into a DataFrame:

```python
names = pd.Series(["Alice", "Bob", "Charlie"])
scores = pd.Series([85, 92, 78])

# Combining multiple Series into a dictionary
student_df = pd.DataFrame({
    "Student_Name": names,
    "Score": scores
})

print(student_df)
```

#### Output:
```text
  Student_Name  Score
0        Alice     85
1          Bob     92
2      Charlie     78
```

---

## 5. Summary: When to Use Which?

* **Use a Series when:**
  * You are working with a single sequence or column of values (e.g., daily temperature readings, closing stock prices of one stock, student grades).
  * You need 1D label-based lookups.

* **Use a DataFrame when:**
  * You have multi-attribute data representing real-world entities (e.g., a customer database with Name, Age, Email, Order History).
  * You need to perform multi-column filtering, aggregations, joins, or prepare datasets for Machine Learning models.
