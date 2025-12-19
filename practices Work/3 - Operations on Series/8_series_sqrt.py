# series_sqrt.py
import pandas as pd
import numpy as np

# Creating a Series
series = pd.Series([1, 4, 9, 16, 25])

# Applying square root
result = np.sqrt(series)

print("Square root of Series:")
print(result)
