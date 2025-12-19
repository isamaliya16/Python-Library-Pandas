# series_creation_with_index.py
import pandas as pd

# Creating a Series with custom index
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series_with_index = pd.Series(data, index=index)

print("Series with custom index:")
print(series_with_index)
