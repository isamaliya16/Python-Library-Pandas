# series_creation_from_dict.py
import pandas as pd

# Creating a Series from a dictionary
data = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
series_from_dict = pd.Series(data)

print("Series from dictionary:")
print(series_from_dict)
