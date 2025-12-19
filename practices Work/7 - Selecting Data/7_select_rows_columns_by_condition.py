# select_rows_columns_by_condition.py

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Selecting rows and specific columns based on condition
selected_data = df.loc[df['Age'] > 25, ['Name', 'City']]
print(selected_data)
