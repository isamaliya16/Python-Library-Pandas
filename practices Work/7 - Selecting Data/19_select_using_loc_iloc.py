# select_using_loc_iloc.py

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Selecting specific rows and columns using loc and iloc together
selection = df.loc[df['Age'] > 25].iloc[:, [0, 2]]
print(selection)
