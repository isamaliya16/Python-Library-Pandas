# 09_query_with_missing_values.py

import pandas as pd

# Creating a DataFrame with missing values
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, None, 32]}
df = pd.DataFrame(data)

# Using query to select rows without missing values in 'age'
result = df.query('age == age')
print(result)
