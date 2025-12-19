# select_with_loc.py

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Selecting rows and columns using loc
selection = df.loc[0:1, 'Name':'Age']
print(selection)
