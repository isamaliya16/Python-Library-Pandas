# 12_query_with_subquery.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Using query with subquery
min_age = df['age'].min()
result = df.query('age == @min_age')
print(result)
