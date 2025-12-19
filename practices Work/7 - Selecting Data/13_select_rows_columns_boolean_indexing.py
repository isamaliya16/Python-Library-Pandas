# select_rows_columns_boolean_indexing.py

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Selecting rows and columns using boolean indexing
selection = df.loc[df['Age'] > 25, ['Name', 'City']]
print(selection)
