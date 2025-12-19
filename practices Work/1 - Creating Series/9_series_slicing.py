# series_slicing.py
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Slicing the Series
print("Slicing from position 1 to 3:")
print(series[1:4])
