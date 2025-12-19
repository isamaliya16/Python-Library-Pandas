# access_element_by_position.py
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Accessing an element by position
print("Element at position 2:")
print(series[2])
