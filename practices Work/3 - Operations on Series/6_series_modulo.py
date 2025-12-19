# series_modulo.py
import pandas as pd

# Creating two Series
series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([3, 5, 7, 9, 11])

# Modulo operation
result = series1 % series2

print("Modulo operation on Series:")
print(result)
