# 15_query_with_index_column.py

import pandas as pd

# Creating a DataFrame and setting an index
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data).set_index('name')

# Using query with index column
result = df.query('name == "Alice"', engine='python')
print(result)
