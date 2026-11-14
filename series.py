import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {1:10, 2:20, 3:30}

print(pd.Series(my_list))
#output:
# 0    10
# 1    20
# 2    30

#with custom index
print(pd.Series(my_list, index=labels))
#output:
# a    10
# b    20
# c    30

#create series with array
print(pd.Series(arr))
#output:
# 0    10
# 1    20
# 2    30

# If i put 2 dimensional array it will give error
# If i give 2 dimensional array it will become DataFrame

#Craete series from dictionary
print(pd.Series(d))
