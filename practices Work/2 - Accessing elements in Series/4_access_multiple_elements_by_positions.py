# access_multiple_elements_by_positions.py
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Accessing multiple elements by positions
print("Elements at positions 1 and 3:")
print(series[[1, 3]])
