# Importing pandas library
import pandas as pd

# Creating two DataFrames with different indexes
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
data2 = {'A': [7, 8], 'B': [9, 10]}
df1 = pd.DataFrame(data1, index=['a', 'b', 'c'])
df2 = pd.DataFrame(data2, index=['a', 'b'])

# Aligning data before performing operations
aligned_sum = df1.add(df2, fill_value=0)

# Printing the aligned sum
print("Aligned Sum of DataFrames:")
print(aligned_sum)
