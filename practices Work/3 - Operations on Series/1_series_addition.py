# series_addition.py
import pandas as pd

# Creating two Series
series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([1, 2, 3, 4, 5])

# Adding the Series
result = series1 + series2

print("Addition of two Series:")
print(result)
