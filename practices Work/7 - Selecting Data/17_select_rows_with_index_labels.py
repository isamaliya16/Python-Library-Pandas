# select_rows_with_index_labels.py

import pandas as pd

# Creating a DataFrame with custom index
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E'])

# Selecting rows using index labels
selection = df.loc[['B', 'D']]
print(selection)
