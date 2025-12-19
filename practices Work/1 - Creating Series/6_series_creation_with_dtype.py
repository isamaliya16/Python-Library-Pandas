# series_creation_with_dtype.py
import pandas as pd

# Creating a Series with a specified data type
data = [10, 20, 30, 40, 50]
series_with_dtype = pd.Series(data, dtype='float64')

print("Series with specified data type:")
print(series_with_dtype)
