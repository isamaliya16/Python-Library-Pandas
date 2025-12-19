# access_elements_with_loc.py
import pandas as pd

# Creating a Series with custom index
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)

# Accessing elements using loc
# loc is typically used for label indexing and can access multiple columns
print("Element with label 'd' using loc:")
print(series.loc['d'])
