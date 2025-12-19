# select_columns_by_list.py

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Selecting columns by list of column names
columns_to_select = ['Name', 'Age']
selected_data = df[columns_to_select]
print(selected_data)
