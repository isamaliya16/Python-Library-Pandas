# 19_query_with_renaming_columns.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Using query and then renaming columns
result = df.query('age > 25').rename(columns={'name': 'person', 'age': 'years'})
print(result)
