# series_subtraction.py
import pandas as pd

# Creating two Series
series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([1, 2, 3, 4, 5])

# Subtracting the Series
result = series1 - series2

print("Subtraction of two Series:")
print(result)
