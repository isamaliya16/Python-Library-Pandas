# access_elements_with_iloc.py
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Accessing elements using iloc
# iloc is used for integer indexing
print("Element at position 3 using iloc:")
print(series.iloc[3])
