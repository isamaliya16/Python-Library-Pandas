# select_with_iloc.py

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Selecting rows and columns using iloc
selection = df.iloc[0:2, 0:2]
print(selection)
