# 24_query_null_values_handling.py

import pandas as pd

# Creating a DataFrame with null values
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, None, 22, 32]}
df = pd.DataFrame(data)

# Using query to handle null values
result = df.query('age != age')
print(result)
