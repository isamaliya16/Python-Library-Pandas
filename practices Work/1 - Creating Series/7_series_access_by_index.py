# series_access_by_index.py
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)

# Accessing elements by index
print("Access element by index 'c':")
print(series['c'])
