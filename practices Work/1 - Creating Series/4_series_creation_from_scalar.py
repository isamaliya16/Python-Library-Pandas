# series_creation_from_scalar.py
import pandas as pd

# Creating a Series from a scalar value
scalar_value = 5
index = ['a', 'b', 'c', 'd', 'e']
series_from_scalar = pd.Series(scalar_value, index=index)

print("Series from scalar value:")
print(series_from_scalar)
