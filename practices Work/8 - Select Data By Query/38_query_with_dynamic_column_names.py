# 39_query_with_dynamic_column_names.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Using query with dynamic column names
column_name = 'age'
result = df.query(f'{column_name} > 25')
print(result)
