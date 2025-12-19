# select_by_conditions_combined.py

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Selecting rows by combining multiple conditions
selection = df[(df['Age'] > 25) & (df['City'] != 'Chicago')]
print(selection)
