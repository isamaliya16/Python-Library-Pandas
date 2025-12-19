# series_operations.py
import pandas as pd

# Creating two Series
data1 = [10, 20, 30, 40, 50]
data2 = [5, 10, 15, 20, 25]
series1 = pd.Series(data1)
series2 = pd.Series(data2)

# Performing arithmetic operations
print("Addition of two Series:")
print(series1 + series2)

print("Subtraction of two Series:")
print(series1 - series2)

print("Multiplication of two Series:")
print(series1 * series2)

print("Division of two Series:")
print(series1 / series2)
