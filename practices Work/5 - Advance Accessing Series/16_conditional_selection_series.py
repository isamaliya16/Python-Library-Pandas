# conditional_selection_series.py
import pandas as pd

# Creating a Pandas Series
series = pd.Series([2, 4, 6, 8, 10])

# Conditional selection
print(series[series % 4 == 0])  # Output: 4, 8
