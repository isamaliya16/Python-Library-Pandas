# access_series_element_label.py
import pandas as pd

# Creating a Pandas Series with custom labels
series = pd.Series([1000, 2000, 3000], index=['a', 'b', 'c'])

# Accessing elements by label
print(series['a'])  # Output: 1000
print(series['c'])  # Output: 3000
