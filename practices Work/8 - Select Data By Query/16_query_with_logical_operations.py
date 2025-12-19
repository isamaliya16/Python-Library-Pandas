# 16_query_with_logical_operations.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Using query with logical operations
result = df.query('(age > 25) and (age < 30)')
print(result)
