# select_rows_by_condition.py

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Selecting rows based on condition
age_above_30 = df[df['Age'] > 30]
print(age_above_30)
