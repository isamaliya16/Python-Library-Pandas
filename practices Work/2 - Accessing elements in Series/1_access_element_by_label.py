# access_element_by_label.py
import pandas as pd

# Creating a Series with custom index
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)

# Accessing an element by label
print("Element with label 'c':")
print(series['c'])
