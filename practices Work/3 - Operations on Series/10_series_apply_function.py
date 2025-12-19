# series_apply_function.py
import pandas as pd

# Creating a Series
series = pd.Series([10, 20, 30, 40, 50])

# Applying a custom function to the Series
def custom_function(x):
    return x * 2

result = series.apply(custom_function)

print("Applying a custom function to Series:")
print(result)
