# access_element_with_get.py
import pandas as pd

# Creating a Series with custom index
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)

# Accessing an element using get method
print("Element with label 'c' using get:")
print(series.get('c'))

# Accessing an element with a default value if the label does not exist
print("Element with label 'f' using get with default value:")
print(series.get('f', 'Label not found'))
