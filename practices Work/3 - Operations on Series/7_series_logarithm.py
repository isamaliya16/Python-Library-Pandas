# series_logarithm.py
import pandas as pd
import numpy as np

# Creating a Series
series = pd.Series([1, 2, 3, 4, 5])

# Applying natural logarithm
result = np.log(series)

print("Natural logarithm of Series:")
print(result)
