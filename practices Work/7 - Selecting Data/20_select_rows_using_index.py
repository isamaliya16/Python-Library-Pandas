# select_rows_using_index.py

import pandas as pd

# Creating a DataFrame with custom index
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data, index=['P1', 'P2', 'P3', 'P4', 'P5'])

# Selecting rows using custom index
selection = df.loc['P2':'P4']
print(selection)
