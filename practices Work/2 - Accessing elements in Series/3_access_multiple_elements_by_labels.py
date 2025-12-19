# access_multiple_elements_by_labels.py
import pandas as pd

# Creating a Series with custom index
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)

# Accessing multiple elements by labels
print("Elements with labels 'b' and 'd':")
print(series[['b', 'd']])
