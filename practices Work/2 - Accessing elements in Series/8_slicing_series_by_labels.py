# slicing_series_by_labels.py
import pandas as pd

# Creating a Series with custom index
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)

# Slicing the Series by labels
print("Slicing from 'b' to 'd':")
print(series['b':'d'])
