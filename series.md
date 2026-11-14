# Detailed Guide: Understanding Pandas Series

This document provides an in-depth breakdown of all concepts, code structures, and behaviors implemented in `series.py`.

---

## 1. What is a Pandas Series?

A **Pandas Series** is a one-dimensional labeled array capable of holding data of any type (integer, string, float, Python objects, etc.).

Think of a Series as consisting of two parallel components:
1. **Index (Axis Labels):** An identifier assigned to each row/entry.
2. **Values (Data):** The actual stored data elements.

```
       Index      Data Values
     +-------+   +-----------+
     |   0   | ->|    10     |
     |   1   | ->|    20     |
     |   2   | ->|    30     |
     +-------+   +-----------+
       dtype: int64
```

Unlike plain Python lists or standard NumPy arrays, every element in a Pandas Series has an explicit label, allowing for label-based lookup, automatic data alignment, and relational operations.

---

## 2. Code Breakdown from `series.py`

### Step 1: Library Imports
```python
import numpy as np
import pandas as pd
```
* `pandas` provides high-level data analysis structures.
* `numpy` provides underlying numerical computing arrays and fast C-level operations.

---

### Step 2: Defining Input Data Structures
```python
labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {1: 10, 2: 20, 3: 30}
```
Here, four distinct data formats were prepared:
* `labels`: A Python list of string characters to be used as custom index identifiers.
* `my_list`: A standard standard 1D Python list.
* `arr`: A 1D NumPy ndarray.
* `d`: A Python dictionary with key-value pairs.

---

### Step 3: Creating a Series from a Python List (Default Index)

```python
print(pd.Series(my_list))
```

#### Output:
```text
0    10
1    20
2    30
dtype: int64
```

#### Technical Explanation:
* When no index is explicitly provided, Pandas automatically generates a default zero-based integer index: `0, 1, 2, ..., N-1` (implemented internally as a `RangeIndex`).
* The data type `dtype: int64` indicates that all values inside the Series are 64-bit integers.
* Terminal Output Note: In a `.py` script, wrapping the expression in `print()` is mandatory; otherwise, the Python interpreter computes the object in memory and exits without rendering it to stdout.

---

### Step 4: Creating a Series with Custom Index Labels

```python
print(pd.Series(my_list, index=labels))
```

#### Output:
```text
a    10
b    20
c    30
dtype: int64
```

#### Technical Explanation:
* The `index` parameter replaces the default numeric indexes (`0, 1, 2`) with the custom string labels (`'a', 'b', 'c'`).
* The positional order maps 1-to-1:
  * `'a'` maps to `10`
  * `'b'` maps to `20`
  * `'c'` maps to `30`
* **Rule:** The length of the index array must match the length of the data array. If lengths differ, Pandas raises a `ValueError: Length of values does not match length of index`.

---

### Step 5: Creating a Series from a NumPy Array

```python
print(pd.Series(arr))
```

#### Output:
```text
0    10
1    20
2    30
dtype: int64
```

#### Technical Explanation:
* Pandas Series is built directly on top of NumPy arrays. When converting a NumPy array to a Series, Pandas wraps the array in a Series container while maintaining NumPy's fast contiguous memory buffer.
* You can also assign custom labels to an array-backed series:
  ```python
  pd.Series(arr, index=labels)
  ```

---

### Step 6: 1-Dimensional Constraint vs. 2-Dimensional Data

In `series.py`, you noted:
```python
# If i put 2 dimensional array it will give error
# If i give 2 dimensional array it will become DataFrame
```

#### Technical Clarification:
1. **What happens if you pass a 2D array to `pd.Series`?**
   If you try:
   ```python
   matrix = np.array([[10, 20], [30, 40]])
   pd.Series(matrix)
   ```
   Python will raise:
   ```text
   ValueError: Data must be 1-dimensional, got ndarray of shape (2, 2) instead
   ```
   A `Series` is strictly one-dimensional (representing a single column or single row).

2. **How to handle 2-Dimensional Data?**
   To handle two-dimensional data (tables with both rows and columns), use **`pd.DataFrame`**:
   ```python
   df = pd.DataFrame(matrix, columns=['Col1', 'Col2'])
   ```
   A DataFrame is essentially a collection of Series sharing a common index.

---

### Step 7: Creating a Series from a Python Dictionary

```python
print(pd.Series(d))
```

#### Input Dictionary:
```python
d = {1: 10, 2: 20, 3: 30}
```

#### Output:
```text
1    10
2    20
3    30
dtype: int64
```

#### Technical Explanation:
* When a dictionary is passed to `pd.Series`:
  * The **keys** automatically become the **index labels**.
  * The **values** become the **data values**.
* Since Python 3.7+, dictionary insertion order is guaranteed, and Pandas preserves this order during Series initialization.
* If keys are strings:
  ```python
  capitals = {'USA': 'Washington D.C.', 'India': 'New Delhi', 'UK': 'London'}
  pd.Series(capitals)
  ```
  The index will be `['USA', 'India', 'UK']` with `dtype: object` (used for string/text data in Pandas).

---

## 3. Summary Reference Table

| Creation Method | Syntax | Index Used |
| :--- | :--- | :--- |
| From List (Default Index) | `pd.Series(my_list)` | Integer `RangeIndex(0, 1, 2, ...)` |
| From List + Custom Index | `pd.Series(my_list, index=labels)` | Explicit labels (`'a'`, `'b'`, `'c'`) |
| From NumPy 1D Array | `pd.Series(arr)` | Fast memory wrapper around ndarray |
| From Python Dictionary | `pd.Series(d)` | Dictionary keys automatically become index labels |
| Passing 2D Data to Series | `pd.Series(2D_array)` | Raises `ValueError` (Use `pd.DataFrame` instead) |
