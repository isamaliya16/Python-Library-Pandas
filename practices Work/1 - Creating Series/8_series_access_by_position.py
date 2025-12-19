# series_access_by_position.py
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Accessing elements by position
print("Access element by position 2:")
print(series[2])
