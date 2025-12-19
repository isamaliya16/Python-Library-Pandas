# boolean_indexing_series.py
import pandas as pd

# Creating a Pandas Series
series = pd.Series([5, 10, 15, 20, 25])

# Boolean indexing
print(series[series > 15])  # Output: 20, 25
