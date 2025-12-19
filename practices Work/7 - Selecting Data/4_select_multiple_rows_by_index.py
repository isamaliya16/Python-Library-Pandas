# select_multiple_rows_by_index.py

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Selecting multiple rows by index
first_two_rows = df.iloc[0:2]
print(first_two_rows)

