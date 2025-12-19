# slicing_series_by_positions.py
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Slicing the Series by positions
print("Slicing from position 1 to 3:")
print(series[1:4])
