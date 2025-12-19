# fancy_indexing_series.py
import pandas as pd

# Creating a Pandas Series
series = pd.Series([3, 6, 9, 12, 15])

# Fancy indexing
print(series[[1, 3]])  # Output: 6, 12
