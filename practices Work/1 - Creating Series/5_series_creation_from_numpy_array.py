# series_creation_from_numpy_array.py
import pandas as pd
import numpy as np

# Creating a Series from a NumPy array
data = np.array([10, 20, 30, 40, 50])
series_from_numpy = pd.Series(data)

print("Series from NumPy array:")
print(series_from_numpy)
