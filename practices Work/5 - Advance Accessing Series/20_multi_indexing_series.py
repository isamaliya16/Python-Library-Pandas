# multi_indexing_series.py
import pandas as pd

# Creating a Pandas Series with multi-index
index = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
series = pd.Series([10, 20, 30, 40], index=index)

# Accessing elements in multi-index series
print(series['a'])
print(series['b', 2])
