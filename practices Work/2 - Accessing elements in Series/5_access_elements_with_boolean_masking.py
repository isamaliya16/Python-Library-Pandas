# access_elements_with_boolean_masking.py
import pandas as pd

# Creating a Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Accessing elements with boolean masking
print("Elements greater than 30:")
print(series[series > 30])
